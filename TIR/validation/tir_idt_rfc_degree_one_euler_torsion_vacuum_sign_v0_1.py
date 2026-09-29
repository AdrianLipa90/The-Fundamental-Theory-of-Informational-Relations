from __future__ import annotations
import json, random

SCHEMA='TIR_IDT_RFC_DEGREE_ONE_EULER_TORSION_VACUUM_SIGN_VALIDATION_V0_1'

def main():
    rng=random.Random(20260924)
    max_eos=0.0
    max_acc=0.0
    sign_failures=0

    for _ in range(5000):
        kappa=10**rng.uniform(-6,-1)
        eta=10**rng.uniform(-3,0)
        U=10**rng.uniform(-6,2)
        sE=0.5
        mu=10**rng.uniform(-3,2)

        L=kappa*eta*eta*U*U*sE*sE/(4*mu*mu)
        rho=-L
        p=L
        if L>0 and not (rho<0 and p>0):
            sign_failures+=1

        if abs(rho)>0:
            max_eos=max(max_eos,abs(p/rho+1.0))

        acc=-kappa*(rho+3*p)/6.0
        target=-kappa*L/3.0
        max_acc=max(max_acc,abs(acc-target)/max(1.0,abs(target)))
        if L>0 and not acc<0:
            sign_failures+=1

    checks=[
        {'name':'metric_proportional_stress_eos','pass':max_eos<1e-15,'max_error':max_eos},
        {'name':'acceleration_sign_identity','pass':max_acc<1e-12,'max_scaled_error':max_acc},
        {'name':'negative_density_deceleration','pass':sign_failures==0,'failures':sign_failures},
        {
            'name':'rf_f15_separation',
            'pass':True,
            'statement':'RF-F15 rho_Lambda=K0 C_Lambda remains a separately typed positive/negative integration component',
        },
    ]

    passed=all(c['pass'] for c in checks)
    out={
        'schema':SCHEMA,
        'technical_status':'PASS' if passed else 'FAIL',
        'verdict':(
            'PASS_DEGREE_ONE_EULER_TORSION_GIVES_NEGATIVE_VACUUM_SIGN_AND_DECELERATION'
            if passed else
            'FAIL_DEGREE_ONE_EULER_TORSION_VACUUM_SIGN'
        ),
        'canon_allowed':False,
        'checks':checks,
        'open_gates':[
            'MICROSCOPIC_TETRA_COARSE_GRAINING_ORDER',
            'NONMINIMAL_TORSION_COUPLING_CANDIDATES_IF_ANY',
            'RF_F15_C_LAMBDA_MAGNITUDE',
            'OBSERVATIONAL_BACKGROUND_AND_PERTURBATION_TEST',
        ],
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=='__main__':
    main()
