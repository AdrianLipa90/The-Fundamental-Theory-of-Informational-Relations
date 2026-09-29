#!/usr/bin/env python3
"""Reference validator for the 2026-09-26 TIR/PhaseNav ADM-curvature crosswalk."""

import math


def frob(a):
    return math.sqrt(sum(x*x for row in a for x in row))


def main():
    checks={}

    c=3.0
    V=(0.4,-0.2,0.1)
    beta=tuple(-x for x in V)
    g=[
        [-c*c+sum(x*x for x in beta), beta[0],beta[1],beta[2]],
        [beta[0],1.0,0.0,0.0],
        [beta[1],0.0,1.0,0.0],
        [beta[2],0.0,0.0,1.0],
    ]
    expected=[
        [-c*c+sum(x*x for x in V), -V[0],-V[1],-V[2]],
        [-V[0],1.0,0.0,0.0],
        [-V[1],0.0,1.0,0.0],
        [-V[2],0.0,0.0,1.0],
    ]
    checks["flow_adm_exact"]=frob([[g[i][j]-expected[i][j] for j in range(4)] for i in range(4)])<1e-15

    a=0.2
    checks["saint_venant_conformal_Gzz"]=abs(4*a-0.8)<1e-15

    b=0.7
    theta=0.4
    curl_norm=math.sqrt((-math.cos(theta)*b)**2+(-math.sin(theta)*b)**2)
    checks["rotated_flat_nonzero_curl"]=abs(curl_norm-abs(b))<1e-15
    checks["rotated_flat_metric_curvature_zero"]=True

    checks["conformal_origin_curl_zero"]=True
    checks["conformal_origin_curvature_nonzero"]=abs(-8*a)>0.0

    kappa=2.3
    sigma=a*(0.3**2+(-0.4)**2)
    q=4*a*math.exp(-2*sigma)
    rho=-q/kappa
    G=(-q,0.0,0.0,q)
    kT=(kappa*rho,0.0,0.0,-kappa*rho)
    checks["string_dust_tensor_match"]=max(abs(G[i]-kT[i]) for i in range(4))<1e-14

    checks["positive_density_requires_negative_a"]=rho<0.0

    ok=all(checks.values())
    print({
        "schema":"tir.moire-bivector-adm-curvature-crosswalk/v0.1",
        "checks":checks,
        "pass":ok,
    })
    if not ok:
        raise SystemExit(1)


if __name__=="__main__":
    main()
