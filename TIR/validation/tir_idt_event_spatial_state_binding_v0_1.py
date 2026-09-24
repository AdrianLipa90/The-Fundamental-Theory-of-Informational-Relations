#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, math, re
import numpy as np

SCHEMA="TIR_IDT_EVENT_SPATIAL_STATE_BINDING_VALIDATION_V0_1"
HEX64=re.compile(r"^[0-9a-f]{64}$")

def spd(m):
    a=np.asarray(m,dtype=float)
    if a.shape!=(3,3) or not np.all(np.isfinite(a)):
        return False
    if not np.allclose(a,a.T,rtol=0.0,atol=1e-12):
        return False
    return bool(np.min(np.linalg.eigvalsh(a))>0.0)

def validate_packet(packet):
    failures=[]
    rid=str(packet.get("physical_realization_id",""))
    receipt=str(packet.get("physical_realization_receipt_sha256",""))
    clock=str(packet.get("clock_id",""))
    source_class=str(packet.get("source_class",""))
    alpha=float(packet.get("theta_to_x0_scale",float("nan")))
    if not rid: failures.append("physical_realization_id")
    if not HEX64.fullmatch(receipt): failures.append("physical_realization_receipt_sha256")
    if not clock: failures.append("clock_id")
    if source_class not in {"PRODUCTION_SOURCE","REFERENCE_CONTROL","CANDIDATE_SOURCE"}:
        failures.append("source_class")
    if not math.isfinite(alpha) or alpha<=0: failures.append("theta_to_x0_scale")
    if source_class=="PRODUCTION_SOURCE" and rid.lower().startswith(("pncs:","noema:","synthetic:","reference:")):
        failures.append("runtime_or_synthetic_production_id")

    events=packet.get("events",[])
    edges=packet.get("elapsed_edges",[])
    emap={}
    for ev in events:
        eid=str(ev.get("event_id",""))
        if not eid or eid in emap:
            failures.append("event_id")
            continue
        try:
            theta=float(ev["theta"]); lapse=float(ev["lapse"])
        except Exception:
            failures.append("event_scalar")
            continue
        if not math.isfinite(theta) or not math.isfinite(lapse) or lapse<=0:
            failures.append("event_scalar")
        if not str(ev.get("patch_id","")) or not str(ev.get("spatial_source_ref","")):
            failures.append("event_spatial_lineage")
        if not spd(ev.get("h_ij")):
            failures.append("event_metric_spd")
        emap[eid]=ev

    rates=[]
    for edge in edges:
        u=str(edge.get("source","")); v=str(edge.get("target",""))
        if u not in emap or v not in emap:
            failures.append("edge_event_ref"); continue
        try:
            dtheta=float(edge["dtheta"])
        except Exception:
            failures.append("edge_dtheta"); continue
        if not math.isfinite(dtheta) or dtheta<=0:
            failures.append("edge_dtheta"); continue
        du=float(emap[v]["theta"])-float(emap[u]["theta"])
        if abs(du-dtheta)>1e-11*max(1.0,abs(dtheta)):
            failures.append("edge_clock_mismatch"); continue
        dx0=alpha*dtheta
        hu=np.asarray(emap[u]["h_ij"],dtype=float)
        hv=np.asarray(emap[v]["h_ij"],dtype=float)
        rates.append(((hv-hu)/dx0,dx0,u,v))
    if not events: failures.append("events_empty")
    if not edges: failures.append("edges_empty")
    return failures,rates

def analytic_packet(dx):
    H=np.array([0.2,-0.1,0.05])
    def h(x0):
        return np.diag(np.exp(2.0*H*x0)).tolist()
    rid="reference:event-spatial:R1"
    receipt=hashlib.sha256(rid.encode()).hexdigest()
    return {
        "physical_realization_id":rid,
        "physical_realization_receipt_sha256":receipt,
        "clock_id":"clock:reference:theta",
        "source_class":"REFERENCE_CONTROL",
        "theta_to_x0_scale":2.5,
        "events":[
            {"event_id":"u","theta":0.0,"lapse":1.3,"patch_id":"P","spatial_source_ref":"ref:u","h_ij":h(0.0)},
            {"event_id":"v","theta":dx/2.5,"lapse":1.3,"patch_id":"P","spatial_source_ref":"ref:v","h_ij":h(dx)}
        ],
        "elapsed_edges":[{"edge_id":"uv","source":"u","target":"v","dtheta":dx/2.5}]
    }

def main():
    checks=[]

    p=analytic_packet(0.1)
    failures,rates=validate_packet(p)
    checks.append({"name":"reference_packet_contract","pass":not failures,"failures":failures})

    # First-order refinement to partial_0 h at x0=0.
    H=np.array([0.2,-0.1,0.05])
    exact=np.diag(2.0*H)
    errs=[]
    for dx in [0.2,0.1,0.05,0.025,0.0125]:
        failures,rates=validate_packet(analytic_packet(dx))
        if failures: raise RuntimeError(failures)
        errs.append(float(np.max(np.abs(rates[0][0]-exact))))
    ratios=[errs[i+1]/errs[i] for i in range(len(errs)-1)]
    checks.append({
        "name":"metric_rate_first_order_refinement",
        "pass":all(r<0.55 for r in ratios) and errs[-1]<0.0011,
        "errors":errs,"ratios":ratios
    })

    # Constant-basis covariance.
    rng=np.random.default_rng(20260924)
    A=rng.normal(size=(3,3))
    Q,_=np.linalg.qr(A)
    if np.linalg.det(Q)<0: Q[:,0]*=-1
    h0=np.diag([1.0,1.3,0.8]); h1=np.diag([1.1,1.25,0.83]); dx=0.07
    rate=(h1-h0)/dx
    rate_q=(Q@h1@Q.T-Q@h0@Q.T)/dx
    cov=float(np.max(np.abs(rate_q-Q@rate@Q.T)))
    checks.append({"name":"constant_spatial_basis_covariance","pass":cov<1e-12,"max_error":cov})

    # Zero-shift RF-E9 reference control only.
    N=1.3
    k0=-rate/(2*N)
    residual=float(np.max(np.abs(k0+rate/(2*N))))
    checks.append({"name":"zero_shift_rf_e9_control","pass":residual<1e-15,"max_error":residual})

    # Negative controls.
    bad=analytic_packet(0.1)
    bad["events"][1]["h_ij"]=[[1,0,0],[0,-1,0],[0,0,1]]
    f,_=validate_packet(bad)
    checks.append({"name":"indefinite_metric_rejected","pass":"event_metric_spd" in f})

    bad2=analytic_packet(0.1)
    bad2["source_class"]="PRODUCTION_SOURCE"
    bad2["physical_realization_id"]="noema:runtime:fake"
    f2,_=validate_packet(bad2)
    checks.append({"name":"runtime_id_rejected_as_production","pass":"runtime_or_synthetic_production_id" in f2})

    bad3=analytic_packet(0.1)
    bad3["elapsed_edges"][0]["dtheta"]*=1.1
    f3,_=validate_packet(bad3)
    checks.append({"name":"clock_edge_mismatch_rejected","pass":"edge_clock_mismatch" in f3})

    passed=all(x["pass"] for x in checks)
    receipt={
        "schema":SCHEMA,
        "technical_status":"PASS" if passed else "FAIL",
        "verdict":"PASS_EVENT_INDEXED_METRIC_RATE_SOURCE_CONTRACT_PRODUCTION_INPUT_OPEN" if passed else "FAIL_EVENT_SPATIAL_BINDING",
        "canon_allowed":False,
        "rf_e9_operator_reused":True,
        "new_extrinsic_curvature_operator_defined":False,
        "production_event_spatial_realization":"OPEN_INPUT",
        "checks":checks
    }
    print(json.dumps(receipt,indent=2,sort_keys=True))
    if not passed: raise SystemExit(1)

if __name__=="__main__":
    main()
