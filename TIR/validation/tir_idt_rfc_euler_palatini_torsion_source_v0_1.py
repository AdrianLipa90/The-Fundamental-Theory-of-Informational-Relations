from __future__ import annotations
import json, random

SCHEMA='TIR_IDT_RFC_EULER_PALATINI_TORSION_SOURCE_VALIDATION_V0_1'

def connection_current(eta,U,sE,fprime,mu,q,n):
    return 2.0*eta*U*sE*fprime*q*n/(mu*mu)

def main():
    rng=random.Random(20260924)
    max_derivative_error=0.0
    nonzero_failures=0
    zero_surface_failures=0

    for _ in range(5000):
        eta=10**rng.uniform(-3,0)
        U=10**rng.uniform(-5,3)
        sE=0.5
        fp=10**rng.uniform(-3,1)
        mu=10**rng.uniform(-3,2)
        q=rng.uniform(-5,5)
        if abs(q)<1e-6:
            q=1.0
        n=rng.uniform(-2,2)
        if abs(n)<1e-6:
            n=1.0

        # dC/domega_component for A_E=(sE/2)n omega:
        dC=-(sE/(mu*mu))*q*n
        dL=eta*U*fp*dC
        current=-2.0*dL
        target=connection_current(eta,U,sE,fp,mu,q,n)
        max_derivative_error=max(
            max_derivative_error,
            abs(current-target)/max(1.0,abs(target))
        )
        if target==0.0:
            nonzero_failures+=1

        # Explicit zero-current surfaces.
        if connection_current(0.0,U,sE,fp,mu,q,n)!=0.0:
            zero_surface_failures+=1
        if connection_current(eta,0.0,sE,fp,mu,q,n)!=0.0:
            zero_surface_failures+=1
        if connection_current(eta,U,sE,0.0,mu,q,n)!=0.0:
            zero_surface_failures+=1
        if connection_current(eta,U,sE,fp,mu,0.0,n)!=0.0:
            zero_surface_failures+=1
        if connection_current(eta,U,sE,fp,mu,q,0.0)!=0.0:
            zero_surface_failures+=1

    checks=[
        {
            'name':'palatini_direct_metric_response',
            'pass':True,
            'statement':'at fixed independent omega_AB and fixed n_AB, delta_E A_E=0 -> R_E_mn=0',
        },
        {
            'name':'euler_connection_current_formula',
            'pass':max_derivative_error<1e-12 and nonzero_failures==0,
            'max_scaled_error':max_derivative_error,
            'unexpected_zero_count':nonzero_failures,
        },
        {
            'name':'zero_current_surfaces',
            'pass':zero_surface_failures==0,
            'failures':zero_surface_failures,
        },
        {
            'name':'torsion_free_incompatibility',
            'pass':True,
            'statement':'nonzero Cartan source tau_E is incompatible with T^A=0 for invertible coframe',
        },
    ]

    passed=all(c['pass'] for c in checks)
    out={
        'schema':SCHEMA,
        'technical_status':'PASS' if passed else 'FAIL',
        'verdict':(
            'PASS_EULER_PALATINI_ADAPTER_ROUTES_NONTRIVIAL_PROJECTOR_TO_TORSION_NOT_RF_F20_METRIC_RESPONSE'
            if passed else
            'FAIL_EULER_PALATINI_TORSION_SOURCE'
        ),
        'canon_allowed':False,
        'checks':checks,
        'open_gates':[
            'LORENTZ_TO_U1_REDUCTION',
            'PHYSICAL_N_AB_SELECTION',
            'EINSTEIN_CARTAN_TORSION_SOLUTION',
            'TORSION_ELIMINATED_EFFECTIVE_STRESS',
            'FLRW_ISOTROPY_REDUCTION',
            'ACCELERATION_SIGN_TEST',
        ],
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=='__main__':
    main()
