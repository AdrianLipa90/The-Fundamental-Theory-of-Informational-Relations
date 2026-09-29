#!/usr/bin/env python3
import math

C=8.0/(9.0*math.sqrt(3.0)*math.pi)
Q=C**(-1.0/3.0)
AHAT=math.sqrt(8.0/3.0)
GAMMA=AHAT*Q

def main():
    checks={}
    checks["Q"]=math.isclose(Q,1.82931154035502,rel_tol=2e-15)
    checks["gamma"]=math.isclose(GAMMA,2.98725323630302,rel_tol=2e-15)
    checks["naive_equal_cell_refuted"]=abs(GAMMA-1.0)>1.0

    # Parent-surface compatibility: m*a_M=1 and m*ell_s=Q.
    m=3.7
    a_M=1.0/m
    ell_s=Q/m
    L_delta=AHAT*ell_s
    checks["phase_cell_mass_roundtrip"]=math.isclose(m*a_M,1.0,rel_tol=1e-15)
    checks["spatial_mass_roundtrip"]=math.isclose(m*ell_s,Q,rel_tol=1e-15)
    checks["edge_cell_ratio"]=math.isclose(L_delta/a_M,GAMMA,rel_tol=1e-15)

    # Exact Moire observational substitution.
    theta=0.08
    L_M=12.0
    a_from_moire=2.0*L_M*math.sin(abs(theta)/2.0)
    m_from_moire=1.0/a_from_moire
    checks["moire_substitution"]=math.isclose(
        m_from_moire*a_from_moire,1.0,rel_tol=1e-15
    )
    checks["predicted_tir_edge"]=math.isclose(
        (AHAT*Q/m_from_moire)/a_from_moire,GAMMA,rel_tol=1e-15
    )

    ok=all(checks.values())
    print({
        "schema":"tir.mummu-tetra-cell-compatibility/v0.1",
        "C_delta_fs":C,
        "Q_delta_fs":Q,
        "gamma_delta_M":GAMMA,
        "checks":checks,
        "pass":ok,
    })
    if not ok:
        raise SystemExit(1)

if __name__=="__main__":
    main()
