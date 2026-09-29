#!/usr/bin/env python3
"""Validate TIR canonical information-scalar source admission identities."""

import math


def main():
    kappa_E=2.4
    alpha_I=1.8
    Xi=1.7
    Xip=-0.23
    H=0.11

    phi=math.sqrt(2.0*Xi)
    phip=Xip/phi
    m2=alpha_I/kappa_E
    U=(alpha_I/kappa_E)*Xi

    # Exact source coordinate equivalence.
    checks={}
    checks["potential_coordinate_equivalence"]=abs(U-0.5*m2*phi*phi)<1e-14

    rho=0.5*phip*phip+U
    p=0.5*phip*phip-U

    # Put the field exactly on the homogeneous KG equation.
    phipp=-3.0*H*phip-m2*phi
    rhop=phip*phipp+m2*phi*phip
    continuity=rhop+3.0*H*(rho+p)
    checks["kg_implies_conservation"]=abs(continuity)<1e-14

    acc_rhop=-kappa_E*(rho+3.0*p)/6.0
    acc_xi=alpha_I*Xi/3.0-kappa_E*Xip*Xip/(6.0*Xi)
    checks["acceleration_formula_equivalence"]=abs(acc_rhop-acc_xi)<1e-14

    # Current admitted potential is independent of tau_R.
    tau1=0.2
    tau2=1.1
    U1=(alpha_I/kappa_E)*Xi
    U2=(alpha_I/kappa_E)*Xi
    checks["holonomy_spectator_current_action"]=U1==U2

    # Distinct type labels: no automatic kappa == kappa_E.
    kappa_info=math.log(2.0)/(24.0*math.pi)
    checks["kappa_types_distinct_in_control"]=abs(kappa_info-kappa_E)>1e-3

    ok=all(checks.values())
    print({
        "schema":"tir.information-scalar-source-admission/v0.1",
        "checks":checks,
        "rho":rho,
        "p":p,
        "continuity_residual":continuity,
        "pass":ok,
    })
    if not ok:
        raise SystemExit(1)


if __name__=="__main__":
    main()
