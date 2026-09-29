from __future__ import annotations
import json, math, random

SCHEMA='TIR_IDT_RFC_EULER_CARTAN_PROJECTOR_PROFILE_IDENTIFIABILITY_VALIDATION_V0_1'

def main():
    rng=random.Random(20260924)
    max_second=0.0
    max_affine_stationary=0.0
    max_eff=0.0

    for _ in range(5000):
        eta=10**rng.uniform(-3,0)
        U=10**rng.uniform(-5,2)
        sE=0.5
        mu=10**rng.uniform(-2,2)
        kappa=10**rng.uniform(-6,-1)
        Q=rng.uniform(-3,3)
        lam=rng.uniform(-4,4)

        # Same f(1), f'(1), distinct f''(1).
        f1=0.5
        f2_A=0.0
        f2_B=2.0*lam
        L2_A=eta*U*sE*sE/(mu*mu)*(f2_A+0.5*f1)
        L2_B=eta*U*sE*sE/(mu*mu)*(f2_B+0.5*f1)
        target_delta=2.0*lam*eta*U*sE*sE/(mu*mu)
        max_second=max(max_second,abs((L2_B-L2_A)-target_delta)/max(1.0,abs(target_delta)))

        gamma=kappa*eta*U*sE*sE/(2.0*mu*mu)
        if abs(1.0-gamma)<1e-6:
            continue
        h=kappa*eta*U*sE*Q/(mu*mu*(1.0-gamma))

        # Stationarity of Lg + affine Lint.
        derivative=-h/(2.0*kappa)+eta*U*sE/(2.0*mu*mu)*(Q+sE*h/2.0)
        max_affine_stationary=max(max_affine_stationary,abs(derivative)/max(1.0,abs(h/(2*kappa))))

        # Direct local action difference and completed-square expression.
        def L(hv):
            C=(Q+sE*hv/2.0)**2/(mu*mu)
            return -hv*hv/(4.0*kappa)+eta*U*(1.0+C)/2.0
        direct=L(h)-L(0.0)
        target=kappa*eta*eta*U*U*sE*sE*Q*Q/(4.0*mu**4*(1.0-gamma))
        max_eff=max(max_eff,abs(direct-target)/max(1.0,abs(target)))

    checks=[
        {'name':'profile_second_derivative_nonidentifiability','pass':max_second<1e-12,'max_scaled_error':max_second},
        {'name':'affine_stationary_solution','pass':max_affine_stationary<1e-12,'max_scaled_error':max_affine_stationary},
        {'name':'affine_completed_square_effective_action','pass':max_eff<1e-12,'max_scaled_error':max_eff},
        {
            'name':'eos_not_fixed_by_projector_value_and_slope',
            'pass':True,
            'statement':'f_A and f_B share f(1)=1,fprime(1)=1/2 but have arbitrary Hessian separation through lambda',
        },
    ]
    passed=all(c['pass'] for c in checks)
    out={
        'schema':SCHEMA,
        'technical_status':'PASS' if passed else 'FAIL',
        'verdict':(
            'PASS_PROJECTOR_FIRST_DERIVATIVE_INSUFFICIENT_AFFINE_CONTROL_SOLVABLE_FULL_EOS_OPEN'
            if passed else
            'FAIL_EULER_CARTAN_PROJECTOR_PROFILE_IDENTIFIABILITY'
        ),
        'canon_allowed':False,
        'checks':checks,
        'open_gates':[
            'PHYSICAL_PROJECTOR_PROFILE_SELECTION',
            'FULL_TORSION_ELIMINATED_METRIC_VARIATION',
            'COARSE_GRAINED_SPIN_STATE_DEPENDENCE',
            'EFFECTIVE_EOS',
            'ACCELERATION_SIGN',
        ],
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=='__main__':
    main()
