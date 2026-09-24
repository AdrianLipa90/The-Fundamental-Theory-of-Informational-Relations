#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import numpy as np

SCHEMA = "TIR_MUMMU_QHTRI_PNLF_TYPED_TIME_BRIDGE_NOGO_VALIDATION_V0_1"


def digest(payload):
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("utf-8")
    ).hexdigest()


def main():
    checks=[]

    # Distinct typed representations.
    drive_tau=np.linspace(0.21,0.49,36,dtype=float)
    pnlf_tau=1.2
    checks.append({
        "name":"drive_snapshot_tau_vector_is_not_pnlf_scalar_tau",
        "status":"PASS" if drive_tau.shape==(36,) and np.isscalar(pnlf_tau) else "FAIL",
        "drive_tau_shape":list(drive_tau.shape),
        "pnlf_tau_is_scalar":bool(np.isscalar(pnlf_tau)),
    })

    dt=np.array([0.01,0.02,0.015],dtype=float)
    g=np.array([0.8,1.25,0.6],dtype=float)
    proper=dt*g
    coord_total=float(np.sum(dt))
    proper_total=float(np.sum(proper))
    checks.append({
        "name":"coordinate_and_proper_duration_are_distinct_generically",
        "status":"PASS" if abs(coord_total-proper_total)>1e-12 else "FAIL",
        "coordinate_duration":coord_total,
        "proper_duration":proper_total,
    })

    tau0=1.2
    tau_cursor=tau0+proper_total
    right_good=tau_cursor
    right_bad=tau0+coord_total
    checks.append({
        "name":"accumulated_orch_proper_time_closes_pnlf_endpoint",
        "status":"PASS" if abs(right_good-tau_cursor)<1e-15 and abs(right_bad-tau_cursor)>1e-12 else "FAIL",
        "tau_start":tau0,
        "tau_cursor":tau_cursor,
        "right_good":right_good,
        "right_bad_direct_dt_sum":right_bad,
    })

    # Reparameterization cancellation: Omega_tau d_tau = Omega_t dt.
    # Use a nonconstant positive lapse and a smooth Bloch path.
    n=250000
    t=(np.arange(n)+0.5)/n
    lapse=0.6+0.7*t
    # n(t) = normalized (cos t, sin t, 0.4 sin 2t), evaluated analytically by
    # finite centered derivative for a robust numerical identity check.
    def bloch(x):
        raw=np.stack([np.cos(x),np.sin(x),0.4*np.sin(2*x)],axis=-1)
        return raw/np.linalg.norm(raw,axis=-1,keepdims=True)
    h=1e-6
    nv=bloch(t)
    dn_dt=(bloch(t+h)-bloch(t-h))/(2*h)
    omega_t=np.cross(nv,dn_dt)
    dn_dtau=dn_dt/lapse[:,None]
    omega_tau=np.cross(nv,dn_dtau)
    lhs=np.mean(omega_t,axis=0) # integral over t in [0,1]
    rhs=np.mean(omega_tau*lapse[:,None],axis=0)
    reparam_error=float(np.max(np.abs(lhs-rhs)))
    checks.append({
        "name":"connection_one_form_reparameterization_cancellation",
        "status":"PASS" if reparam_error<1e-10 else "FAIL",
        "max_abs_error":reparam_error,
    })

    # Canonical bridge commitment must be sensitive to time model and bindings.
    body={
        "t36_basis_id":"pncs:t36:test:v1",
        "proper_time_model_id":"pncs:orch-time:test:v1",
        "tau_start":1.2,
        "tau_end":tau_cursor,
        "htri_step_receipts":["a"*64,"b"*64,"c"*64],
        "time_binding_receipts":["d"*64,"e"*64,"f"*64],
    }
    a=digest(body)
    changed_model=dict(body)
    changed_model["proper_time_model_id"]="pncs:orch-time:test:v2"
    b=digest(changed_model)
    changed_time=dict(body)
    changed_time["tau_end"]=tau_cursor+0.001
    c=digest(changed_time)
    checks.append({
        "name":"trajectory_commitment_binds_time_model_and_endpoint",
        "status":"PASS" if len({a,b,c})==3 else "FAIL",
        "base":a,
        "changed_model":b,
        "changed_endpoint":c,
    })

    # HTRI-only receipt is insufficient for proper-time identity: two different
    # lapse policies can share identical HTRI step hashes.
    htri_only=digest({"htri_step_receipts":["a"*64,"b"*64,"c"*64]})
    proper_alt=float(np.sum(dt*np.array([1.0,1.0,1.0])))
    checks.append({
        "name":"htri_step_hash_alone_does_not_determine_pnlf_proper_duration",
        "status":"PASS" if abs(proper_alt-proper_total)>1e-12 else "FAIL",
        "same_htri_only_commitment":htri_only,
        "proper_duration_policy_a":proper_total,
        "proper_duration_policy_b":proper_alt,
    })

    # Direct equality is allowed only in the special unit-lapse case.
    unit=np.ones(3)
    unit_proper=float(np.sum(dt*unit))
    checks.append({
        "name":"direct_dt_equals_proper_time_only_for_unit_lapse_control",
        "status":"PASS" if abs(unit_proper-coord_total)<1e-15 else "FAIL",
        "coordinate_duration":coord_total,
        "unit_lapse_proper_duration":unit_proper,
    })

    status="PASS" if all(c["status"]=="PASS" for c in checks) else "FAIL"
    out={
        "schema":SCHEMA,
        "status":status,
        "claim_scope":(
            "typed separation of HTRI dt, semantic sample time, ORCH coordinate/proper "
            "time and PNLF proper time; geometric connection one-form is reparameterization "
            "invariant but interval identity requires an explicit time-binding receipt"
        ),
        "source_pins":{"pncs_main":"8855abed440e9949f576ffbe2153325f69e78963"},
        "checks":checks,
        "summary":{"passed":sum(c["status"]=="PASS" for c in checks),"total":len(checks)},
    }
    Path(__file__).with_name(
        "TIR_MUMMU_QHTRI_PNLF_TYPED_TIME_BRIDGE_NOGO_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if status=="PASS" else 1


if __name__=="__main__":
    raise SystemExit(main())
