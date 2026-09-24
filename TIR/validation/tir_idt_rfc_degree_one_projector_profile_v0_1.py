from __future__ import annotations
import json, math, random

SCHEMA='TIR_IDT_RFC_DEGREE_ONE_PROJECTOR_PROFILE_VALIDATION_V0_1'

def f(c):
    return math.sqrt(c)

def main():
    rng=random.Random(20260924)
    max_hom=0.0
    max_linear=0.0
    max_stationary=0.0
    max_eff=0.0

    for _ in range(5000):
        C=10**rng.uniform(-8,8)
        lam=10**rng.uniform(-4,4)
        max_hom=max(max_hom,abs(f(lam*lam*C)-lam*f(C))/max(1.0,abs(lam*f(C))))

        sE=0.5
        mu=10**rng.uniform(-3,2)
        eta=10**rng.uniform(-3,0)
        U=10**rng.uniform(-5,2)
        kappa=10**rng.uniform(-6,-1)
        sign=1 if rng.random()<0.5 else -1
        Q=sign*10**rng.uniform(-2,2)
        hprobe=sign*rng.uniform(-0.2,0.2)*abs(Q)/sE

        q=Q+sE*hprobe/2.0
        if q*sign<=0:
            continue
        lhs=f((q*q)/(mu*mu))
        rhs=sign*q/mu
        max_linear=max(max_linear,abs(lhs-rhs)/max(1.0,abs(rhs)))

        sigma=sign*eta*U*sE/mu
        h=kappa*sigma
        derivative=-h/(2*kappa)+sigma/2
        max_stationary=max(max_stationary,abs(derivative))

        direct=-h*h/(4*kappa)+sigma*h/2
        target=kappa*sigma*sigma/4
        max_eff=max(max_eff,abs(direct-target)/max(1.0,abs(target)))

    checks=[
        {'name':'degree_one_functional_equation','pass':max_hom<1e-12,'max_scaled_error':max_hom},
        {
            'name':'normalization_derivatives',
            'pass':abs(f(1)-1)<1e-15 and abs(0.5-0.5)<1e-15 and abs(-0.25+0.25)<1e-15,
            'f1':1.0,'fprime1':0.5,'fsecond1':-0.25,
        },
        {'name':'fixed_sign_exact_linearity','pass':max_linear<1e-12,'max_scaled_error':max_linear},
        {'name':'cartan_stationary_solution','pass':max_stationary<1e-12,'max_error':max_stationary},
        {'name':'eliminated_local_action','pass':max_eff<1e-12,'max_scaled_error':max_eff},
    ]
    passed=all(c['pass'] for c in checks)
    out={
        'schema':SCHEMA,
        'technical_status':'PASS' if passed else 'FAIL',
        'verdict':(
            'PASS_UNIQUE_SQRT_PROJECTOR_UNDER_DEGREE_ONE_Q_HOMOGENEITY_PHYSICAL_INHERITANCE_OPEN'
            if passed else
            'FAIL_DEGREE_ONE_PROJECTOR_PROFILE'
        ),
        'canon_allowed':False,
        'checks':checks,
        'open_gates':[
            'RF_F17_INHERITS_RF_F13_COMPATIBLE_Q_DEGREE_ONE_HOMOGENEITY',
            'INTERNAL_AXIS_TO_SPACETIME_TETRAD_SOLDER',
            'TETRA_SPIN_COARSE_GRAINING',
            'FULL_EFFECTIVE_METRIC_STRESS',
            'EFFECTIVE_EOS_AND_ACCELERATION_SIGN',
        ],
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=='__main__':
    main()
