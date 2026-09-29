#!/usr/bin/env python3
import math

C=8.0/(9.0*math.sqrt(3.0)*math.pi)

def main():
    checks={}
    a=0.246
    L=12.6
    d=(a/L)**2
    for idx,s in enumerate((0.01,0.2,3.0,100.0)):
        checks["moire_scale_invariance_"+str(idx)]=math.isclose(
            d,(s*a/(s*L))**2,rel_tol=1e-15,abs_tol=1e-18
        )

    gamma_s=1.7
    ell_s=gamma_s*a*math.sqrt(3.0/8.0)
    a_tir=ell_s*math.sqrt(8.0/3.0)
    checks["conditional_spatial_edge_roundtrip"]=math.isclose(
        a_tir,gamma_s*a,rel_tol=1e-15
    )

    families=((1.2,0.8,1.0),(2.0,1.7,0.5),(0.4,3.2,2.5))
    for idx,(q_s,mu_phi,r_m) in enumerate(families):
        r_alpha=r_m*mu_phi/(C*q_s**3)
        checks["rfs1_family_"+str(idx)]=math.isclose(
            r_alpha*q_s**3,r_m*mu_phi/C,rel_tol=1e-14
        )
        checks["positive_ralpha_"+str(idx)]=r_alpha>0.0

    r1=1.0/C
    r2=1.0/(C*8.0)
    checks["rfs1_nonunique_ralpha"]=not math.isclose(r1,r2,rel_tol=1e-12)

    kappa_info=math.log(2.0)/(24.0*math.pi)
    kappa_E_control=2.0
    checks["typed_kappas_distinct"]=not math.isclose(
        kappa_info,kappa_E_control,rel_tol=1e-12
    )

    ok=all(checks.values())
    print({
        "schema":"tir.moire-scale-alpha-normalization-audit/v0.1",
        "C_delta_fs":C,
        "checks":checks,
        "pass":ok,
    })
    if not ok:
        raise SystemExit(1)

if __name__=="__main__":
    main()
