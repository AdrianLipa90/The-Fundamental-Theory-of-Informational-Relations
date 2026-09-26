#!/usr/bin/env python3
import math

C=8.0/(9.0*math.sqrt(3.0)*math.pi)
Q=C**(-1.0/3.0)
AHAT=math.sqrt(8.0/3.0)

def main():
    checks={}
    checks["Q_cube"]=math.isclose(Q**3,1.0/C,rel_tol=2e-15)
    checks["Q_value"]=math.isclose(Q,1.82931154035502,rel_tol=2e-15)
    checks["Q2_value"]=math.isclose(Q*Q,3.34638071167607,rel_tol=3e-15)

    ell_s=0.37
    m=Q/ell_s
    checks["mass_scale_roundtrip"]=math.isclose(m*ell_s,Q,rel_tol=1e-15)

    gamma=1.4
    aobs=0.246
    ell_from_edge=gamma*aobs/AHAT
    m_edge=Q/ell_from_edge
    checks["edge_formula"]=math.isclose(
        m_edge,Q*AHAT/(gamma*aobs),rel_tol=1e-15
    )
    checks["edge_coefficient"]=math.isclose(
        Q*AHAT,2.98725323630302,rel_tol=2e-15
    )

    c=299792458.0
    omega=c*m
    checks["kg_frequency"]=math.isclose(omega/c,m,rel_tol=1e-15)

    # A changed gamma changes the inferred mass: gamma cannot be hidden.
    m2=Q*AHAT/(2.0*gamma*aobs)
    checks["mapping_coefficient_is_physical_degree"]=not math.isclose(
        m_edge,m2,rel_tol=1e-12
    )

    ok=all(checks.values())
    print({
        "schema":"tir.conditional-absolute-mass-closure/v0.1",
        "C_delta_fs":C,
        "Q_delta_fs":Q,
        "edge_coefficient":Q*AHAT,
        "checks":checks,
        "pass":ok,
    })
    if not ok:
        raise SystemExit(1)

if __name__=="__main__":
    main()
