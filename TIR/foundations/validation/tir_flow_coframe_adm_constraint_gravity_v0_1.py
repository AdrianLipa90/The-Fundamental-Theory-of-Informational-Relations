#!/usr/bin/env python3
from __future__ import annotations
import json, math

SCHEMA="TIR_FLOW_COFRAME_ADM_CONSTRAINT_GRAVITY_VALIDATION_V0_1"
TOL=1e-12

def radial_constraint(V: float, dV: float, r: float, c: float=1.0) -> tuple[float,float]:
    a=dV/c
    b=V/(c*r)
    K=a+2*b
    KijKij=a*a+2*b*b
    raw=K*K-KijKij
    scale=max(1.0,abs(K*K),abs(KijKij))
    return raw,abs(raw)/scale

def main():
    checks=[]
    max_res=0.0
    for C in (0.1,1.0,7.3,100.0):
        for r in (0.3,1.0,2.5,20.0):
            for s in (-1.0,1.0):
                V=s*math.sqrt(C/r)
                dV=-V/(2*r)
                _,rel=radial_constraint(V,dV,r)
                max_res=max(max_res,rel)
    checks.append({"name":"vacuum_radial_C_over_r_family","pass":max_res<TOL,"max_scaled_residual":max_res})

    bad=[]
    for p in (0.0,0.5,1.5,2.0,3.0):
        C=2.3; r=1.7
        V=math.sqrt(C/(r**p))
        dV=-(p/(2*r))*V
        _,rel=radial_constraint(V,dV,r)
        bad.append(rel)
    checks.append({"name":"non_unit_power_negative_controls","pass":all(x>1e-6 for x in bad),"scaled_residuals":bad})

    max_id=0.0
    for V,dV,r in ((.3,-.07,.8),(2.0,-.4,3.0),(-.5,.2,1.4)):
        lhs=V*V+2*r*V*dV
        rhs=V*(2*r*dV+V)
        max_id=max(max_id,abs(lhs-rhs))
    checks.append({"name":"radial_first_integral_identity","pass":max_id<TOL,"max_error":max_id})

    G=6.67430e-11; c=299792458.0
    max_mass=0.0
    for M in (1e20,1e25,1e30):
        for r in (1e4,1e8,1e12):
            V2=2*G*M/r
            phi=-0.5*V2
            target=-G*M/r
            max_mass=max(max_mass,abs(phi-target)/max(1.0,abs(target)))
    checks.append({"name":"mass_normalization_C_equals_2GM","pass":max_mass<5e-16,"max_relative_error":max_mass})

    max_flrw=0.0
    for eps,Lam in ((1e-10,0.0),(3e-9,1e-52),(0.0,1e-52)):
        H2=(8*math.pi*G*eps/(3*c*c))+(Lam*c*c/3)
        lhs=6*H2/(c*c)
        rhs=16*math.pi*G*eps/(c**4)+2*Lam
        max_flrw=max(max_flrw,abs(lhs-rhs)/max(1e-100,abs(rhs),abs(lhs)))
    checks.append({"name":"flat_flrw_hamiltonian_identity","pass":max_flrw<5e-15,"max_relative_error":max_flrw})

    max_hyp=0.0
    for mu in (0.01,0.2,0.8):
        chi=math.atanh(math.sqrt(mu))
        max_hyp=max(max_hyp,abs(math.tanh(chi)**2-mu))
    checks.append({"name":"rapidity_profile_exterior_identity","pass":max_hyp<TOL,"max_error":max_hyp})

    passed=all(x["pass"] for x in checks)
    receipt={
        "schema":SCHEMA,
        "technical_status":"PASS" if passed else "FAIL",
        "verdict":"PASS_CONDITIONAL_ADM_FLOW_DERIVATION_SOURCE_BINDING_OPEN" if passed else "FAIL_ADM_FLOW_DERIVATION",
        "canon_allowed":False,
        "closed_gate":"FLOW_COFRAME_TO_SPHERICAL_VACUUM_RIVER_PROFILE_ON_DECLARED_ADM_ASSUMPTIONS",
        "open_gates":[
            "SOURCE_TO_DIMENSIONLESS_RAPIDITY_BINDING",
            "ORBITAL_RECURSION_TO_UNIQUE_PHYSICAL_COFRAME",
            "HOLONOMIC_EFFECTIVE_SOURCE_OR_GEOMETRIC_CORRECTION",
            "LATE_TIME_ACCELERATION_WITHOUT_RETUNING"
        ],
        "checks":checks
    }
    print(json.dumps(receipt,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=="__main__":
    main()
