from __future__ import annotations
import json, math, random

SCHEMA='TIR_IDT_RFC_EULER_CARTAN_TETRA_ISOTROPY_VALIDATION_V0_1'

TETRA=(
    (1/math.sqrt(3),1/math.sqrt(3),1/math.sqrt(3)),
    (1/math.sqrt(3),-1/math.sqrt(3),-1/math.sqrt(3)),
    (-1/math.sqrt(3),1/math.sqrt(3),-1/math.sqrt(3)),
    (-1/math.sqrt(3),-1/math.sqrt(3),1/math.sqrt(3)),
)

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def main():
    # Tetrahedral Gram relations.
    max_norm=max(abs(dot(s,s)-1.0) for s in TETRA)
    max_off=max(abs(dot(TETRA[i],TETRA[j])+1/3) for i in range(4) for j in range(i+1,4))

    first=[sum(s[i] for s in TETRA)/4 for i in range(3)]
    second=[[sum(s[i]*s[j] for s in TETRA)/4 for j in range(3)] for i in range(3)]
    max_first=max(abs(x) for x in first)
    max_second=max(abs(second[i][j]-(1/3 if i==j else 0.0)) for i in range(3) for j in range(3))

    # Cartan component check for random axis, using epsilon contractions.
    rng=random.Random(20260924)
    max_dual=0.0
    max_quad=0.0
    for _ in range(5000):
        raw=[rng.uniform(-1,1) for _ in range(3)]
        nr=math.sqrt(sum(x*x for x in raw))
        if nr<1e-12:
            raw=[1,2,3]; nr=math.sqrt(14)
        s=[x/nr for x in raw]
        kappa=10**rng.uniform(-4,1)
        sigma=rng.uniform(-10,10)

        # n12=s3, n23=s1, n31=s2.
        n12=s[2]; n23=s[0]; n31=s[1]
        T012=-kappa*sigma*n12
        T023=-kappa*sigma*n23
        T031=-kappa*sigma*n31

        # b1=T023, b2=T031, b3=T012 under 1/2 epsilon contraction.
        b=(T023,T031,T012)
        target=tuple(-kappa*sigma*x for x in s)
        max_dual=max(max_dual,max(abs(b[i]-target[i]) for i in range(3)))

        # T^A_BC T_A^BC = -2 kappa^2 sigma^2.
        q=-2*(T012*T012+T023*T023+T031*T031)
        target_q=-2*kappa*kappa*sigma*sigma
        max_quad=max(max_quad,abs(q-target_q)/max(1.0,abs(target_q)))

    checks=[
        {'name':'tetra_unit_norms','pass':max_norm<1e-12,'max_error':max_norm},
        {'name':'tetra_pair_dot','pass':max_off<1e-12,'max_error':max_off},
        {'name':'tetra_first_moment_zero','pass':max_first<1e-12,'max_error':max_first},
        {'name':'tetra_second_moment_isotropic','pass':max_second<1e-12,'max_error':max_second},
        {'name':'torsion_dual_axis','pass':max_dual<1e-12,'max_error':max_dual},
        {'name':'torsion_quadratic_contraction','pass':max_quad<1e-12,'max_scaled_error':max_quad},
    ]
    passed=all(c['pass'] for c in checks)
    out={
        'schema':SCHEMA,
        'technical_status':'PASS' if passed else 'FAIL',
        'verdict':(
            'PASS_LOCAL_EULER_CARTAN_TORSION_SINGLE_AXIS_ANISOTROPIC_TETRA_SECOND_MOMENT_ISOTROPIC'
            if passed else
            'FAIL_EULER_CARTAN_TETRA_ISOTROPY'
        ),
        'canon_allowed':False,
        'checks':checks,
        'open_gates':[
            'MICROSCOPIC_TETRA_TORSION_ENSEMBLE_REALIZATION',
            'TORSION_ELIMINATED_EFFECTIVE_STRESS',
            'EFFECTIVE_EOS_AND_SCALE_FACTOR_SCALING',
            'ACCELERATION_SIGN',
        ],
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=='__main__':
    main()
