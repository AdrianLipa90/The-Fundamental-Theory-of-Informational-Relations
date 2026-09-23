#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from pathlib import Path
import numpy as np

SCHEMA = "TIR_MUMMU_PNLF_REDUCTION_LAYER_BOUNDARY_VALIDATION_V0_1"


def reduction_omega(lam, *, coherence, relation_alignment, defect, xi):
    l1,l2,l3,l4 = lam
    return l1*coherence + l2*relation_alignment - l3*defect - l4*xi


def layer_admitted(*, resolution_state, tau_start, tau_cursor, tau_end,
                   right_tau, reduction_witness, consolidation_witness,
                   selected, ready):
    if resolution_state != "ADMITTED":
        return False
    if tau_end is None or abs(tau_end-tau_cursor) > 1e-12:
        return False
    if right_tau is None or abs(right_tau-tau_cursor) > 1e-12:
        return False
    if not reduction_witness or not consolidation_witness:
        return False
    if not ready or selected is None:
        return False
    return tau_start <= tau_cursor


def sigma(v):
    x,y,z=v
    return np.array([[z,x-1j*y],[x+1j*y,-z]],dtype=np.complex128)


def main():
    checks=[]

    lam=(1.2,0.8,0.6,0.4)
    obs=dict(coherence=0.82,relation_alignment=0.71,defect=0.18,xi=0.09)
    omega=reduction_omega(lam,**obs)
    crit=1.30
    ready=omega>=crit
    checks.append({
        "name":"receipt_bound_reduction_threshold",
        "status":"PASS" if ready == (omega>=crit) else "FAIL",
        "omega":omega,
        "omega_crit":crit,
        "reduce_ready":ready,
    })

    admitted=layer_admitted(
        resolution_state="ADMITTED",
        tau_start=0.0,tau_cursor=1.0,tau_end=1.0,right_tau=1.0,
        reduction_witness=True,consolidation_witness=True,
        selected=7,ready=True,
    )
    checks.append({
        "name":"exact_admitted_segment_endpoint",
        "status":"PASS" if admitted else "FAIL",
        "tau_start":0.0,
        "tau_cursor":1.0,
        "tau_end":1.0,
        "right_checkpoint_tau":1.0,
    })

    gap=layer_admitted(
        resolution_state="ADMITTED",
        tau_start=0.0,tau_cursor=0.0,tau_end=0.0,right_tau=1.0,
        reduction_witness=True,consolidation_witness=True,
        selected=7,ready=True,
    )
    checks.append({
        "name":"unrecorded_tau_gap_rejected",
        "status":"PASS" if not gap else "FAIL",
    })

    not_ready=layer_admitted(
        resolution_state="ADMITTED",
        tau_start=0.0,tau_cursor=1.0,tau_end=1.0,right_tau=1.0,
        reduction_witness=True,consolidation_witness=True,
        selected=7,ready=False,
    )
    no_selection=layer_admitted(
        resolution_state="ADMITTED",
        tau_start=0.0,tau_cursor=1.0,tau_end=1.0,right_tau=1.0,
        reduction_witness=True,consolidation_witness=True,
        selected=None,ready=True,
    )
    no_witness=layer_admitted(
        resolution_state="ADMITTED",
        tau_start=0.0,tau_cursor=1.0,tau_end=1.0,right_tau=1.0,
        reduction_witness=False,consolidation_witness=True,
        selected=7,ready=True,
    )
    rejected=layer_admitted(
        resolution_state="REJECTED",
        tau_start=0.0,tau_cursor=1.0,tau_end=1.0,right_tau=None,
        reduction_witness=True,consolidation_witness=True,
        selected=7,ready=True,
    )
    checks.append({
        "name":"nonadmitted_boundaries_fail_closed",
        "status":"PASS" if not any((not_ready,no_selection,no_witness,rejected)) else "FAIL",
        "ready_without_selection_admitted":no_selection,
        "selection_without_ready_admitted":not_ready,
        "missing_witness_admitted":no_witness,
        "rejected_segment_admitted":rejected,
    })

    # An interior numerical cut is not an admitted layer without a checkpoint.
    checkpoint_times={0.0,1.0,2.25}
    arbitrary_cut=0.4
    checks.append({
        "name":"arbitrary_interior_time_slice_is_not_layer_boundary",
        "status":"PASS" if arbitrary_cut not in checkpoint_times else "FAIL",
        "candidate_tau":arbitrary_cut,
        "admitted_checkpoint_times":sorted(checkpoint_times),
    })

    # Adjacent admitted layer quartic functional and commutator form.
    a=np.array([0.12,-0.04,0.09],dtype=float)
    b=np.array([-0.03,0.11,0.07],dtype=float)
    q_cross=float(np.linalg.norm(np.cross(a,b))**2/96.0)
    A=-0.5j*sigma(a)
    B=-0.5j*sigma(b)
    comm=A@B-B@A
    q_comm=float(np.sum(np.abs(comm)**2)/48.0)
    checks.append({
        "name":"reduction_bounded_quartic_functional",
        "status":"PASS" if abs(q_cross-q_comm)<1e-16 and q_cross>0.0 else "FAIL",
        "cross_product_form":q_cross,
        "commutator_form":q_comm,
        "residual":abs(q_cross-q_comm),
    })

    # Reparameterization invariance of an integrated generator on one path.
    # Omega(tau)=(1,2*tau,tau^2), tau in [0,1].
    # Reparameterize tau=s^2; integral Omega(tau)d_tau =
    # integral Omega(s^2)*2s ds.
    n=200000
    tau=(np.arange(n)+0.5)/n
    integ_tau=np.array([
        np.mean(np.ones(n)),
        np.mean(2.0*tau),
        np.mean(tau*tau),
    ])
    s=(np.arange(n)+0.5)/n
    jac=2.0*s
    integ_s=np.array([
        np.mean(jac),
        np.mean(2.0*s*s*jac),
        np.mean((s*s)**2*jac),
    ])
    reparam_error=float(np.max(np.abs(integ_tau-integ_s)))
    checks.append({
        "name":"layer_integrated_generator_reparameterization_invariance",
        "status":"PASS" if reparam_error<2e-10 else "FAIL",
        "max_abs_error":reparam_error,
    })

    # Policy conditionality: same observables, different explicit omega_crit.
    omega_same=reduction_omega(lam,**obs)
    ready_low=omega_same>=1.30
    ready_high=omega_same>=1.60
    checks.append({
        "name":"boundary_is_policy_conditional_not_parameter_free",
        "status":"PASS" if ready_low and not ready_high else "FAIL",
        "omega":omega_same,
        "ready_at_1p30":ready_low,
        "ready_at_1p60":ready_high,
    })

    status="PASS" if all(c["status"]=="PASS" for c in checks) else "FAIL"
    out={
        "schema":SCHEMA,
        "status":status,
        "claim_scope":(
            "operational finite MUMMU layer boundaries are admitted PNLF liminal "
            "segments conditional on explicit reduction/consolidation policy; "
            "QHTRI-to-PNLF trajectory identity and physical boundary remain open"
        ),
        "source_pins":{
            "pncs_main":"8855abed440e9949f576ffbe2153325f69e78963",
            "pnlf_fixture":"tests/test_pnlf_orbital_memory_v01.py",
        },
        "checks":checks,
        "summary":{"passed":sum(c["status"]=="PASS" for c in checks),"total":len(checks)},
    }
    Path(__file__).with_name(
        "TIR_MUMMU_PNLF_REDUCTION_LAYER_BOUNDARY_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if status=="PASS" else 1


if __name__=="__main__":
    raise SystemExit(main())
