#!/usr/bin/env python3
from __future__ import annotations
import json, math, random

SCHEMA="TIR_INTERLEAF_SHIFT_ORBITAL_RAPIDITY_MASS_BRIDGE_VALIDATION_V0_1"
TOL=2e-12

def inv2(a,b,d):
    det=a*d-b*b
    return ((d/det,-b/det),(-b/det,a/det))

def main():
    checks=[]
    rng=random.Random(20260924)

    max_shift=0.0
    for _ in range(64):
        c=299792458.0
        beta_t=tuple(rng.uniform(-0.7*c,0.7*c) for _ in range(3))
        b=tuple(x/c for x in beta_t)
        V=tuple(-x for x in beta_t)
        max_shift=max(max_shift,max(abs(V[i]/c+b[i]) for i in range(3)))
    checks.append({"name":"beta_t_to_shift_to_flow_sign_bridge","pass":max_shift<TOL,"max_error":max_shift})

    max_hyp=0.0
    max_q=0.0
    for beta in (0.0,0.01,0.2,0.7,0.95):
        chi=math.atanh(beta)
        max_hyp=max(max_hyp,abs(math.tanh(chi)-beta))
        q=math.tanh(chi/2)
        q2=0.0 if beta==0 else beta/(1+math.sqrt(1-beta*beta))
        max_q=max(max_q,abs(q-q2))
    checks += [
        {"name":"shift_norm_to_rapidity","pass":max_hyp<TOL,"max_error":max_hyp},
        {"name":"rapidity_to_poincare_radius","pass":max_q<TOL,"max_error":max_q},
    ]

    # Radial metric inverse and Misner-Sharp crosswalk.
    c=299792458.0; G=6.67430e-11
    max_inv=0.0
    max_mass=0.0
    for r in (1e3,1e6,1e9):
        for beta in (0.01,0.2,0.8):
            V=beta*c
            a=-(c*c-V*V); b=-V; d=1.0
            gi=inv2(a,b,d)
            target_grr=1-beta*beta
            max_inv=max(max_inv,abs(gi[1][1]-target_grr))
            m1=c*c*r*(1-gi[1][1])/(2*G)
            m2=r*V*V/(2*G)
            max_mass=max(max_mass,abs(m1-m2)/max(1.0,abs(m2)))
    checks += [
        {"name":"radial_inverse_metric_grr","pass":max_inv<5e-15,"max_error":max_inv},
        {"name":"misner_sharp_flow_mass_identity","pass":max_mass<2e-12,"max_relative_error":max_mass,"note":"floating subtraction 1-g^rr at beta=0.01"},
    ]

    # Vacuum V^2=C/r means constant invariant mass.
    max_const=0.0
    for C in (1e5,1e12,1e20):
        values=[]
        for r in (2.0,5.0,20.0,100.0):
            V2=C/r
            values.append(r*V2/(2*G))
        base=values[0]
        max_const=max(max_const,max(abs(x-base)/max(1.0,abs(base)) for x in values))
    checks.append({"name":"vacuum_C_over_r_constant_misner_sharp_mass","pass":max_const<TOL,"max_relative_error":max_const})

    # Orientation is representational.
    r=7.0; V=1234.5
    mplus=r*V*V/(2*G); mminus=r*(-V)*(-V)/(2*G)
    checks.append({"name":"flow_orientation_mass_invariance","pass":mplus==mminus})

    passed=all(x["pass"] for x in checks)
    receipt={
        "schema":SCHEMA,
        "technical_status":"PASS" if passed else "FAIL",
        "verdict":"PASS_EXACT_SHIFT_RAPIDITY_AND_INVARIANT_MASS_BRIDGE_PRODUCTION_INPUT_OPEN" if passed else "FAIL_SHIFT_RAPIDITY_MASS_BRIDGE",
        "canon_allowed":False,
        "production_beta_match":"OPEN_INPUT",
        "shift_is_physical_source":False,
        "checks":checks
    }
    print(json.dumps(receipt,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=="__main__":
    main()
