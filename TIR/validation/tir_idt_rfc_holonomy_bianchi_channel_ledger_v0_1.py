from __future__ import annotations
import json, math, random

SCHEMA='TIR_IDT_RFC_HOLONOMY_BIANCHI_CHANNEL_LEDGER_VALIDATION_V0_1'

def main():
    rng=random.Random(20260924)
    max_partition=0.0
    max_acc=0.0
    max_missing=0.0

    for _ in range(1000):
        kappa=10**rng.uniform(-3,1)
        phip=rng.uniform(-3,3)
        K=0.5*phip*phip
        U=10**rng.uniform(-5,2)
        tau=rng.uniform(-math.pi,math.pi)

        D=math.sin(tau/2.0)**2
        C=math.cos(tau/2.0)**2
        max_partition=max(max_partition,abs(C+D-1.0))

        rho=K+U
        p=K-U
        a0=-kappa*(rho+3*p)/6.0

        rho_c=K+U*C
        p_c=K-U*C
        lambda_d=kappa*U*D
        a_split=-kappa*(rho_c+3*p_c)/6.0+lambda_d/3.0
        max_acc=max(max_acc,abs(a0-a_split))

        a_bad=-kappa*(K+3*K)/6.0+lambda_d/3.0
        predicted_missing=kappa*U*C/3.0
        max_missing=max(
            max_missing,
            abs((a0-a_bad)-predicted_missing),
        )

    checks=[
        {
            'name':'C_plus_D_partition',
            'pass':max_partition<1e-15,
            'max_error':max_partition,
        },
        {
            'name':'exact_D_to_Lambda_bookkeeping_invariance',
            'pass':max_acc<1e-12,
            'max_acceleration_error':max_acc,
        },
        {
            'name':'omitted_C_source_defect_exact',
            'pass':max_missing<1e-12,
            'max_error':max_missing,
            'defect':'a_original-a_omitC = kappa_E U_I C_h / 3',
        },
    ]

    passed=all(x['pass'] for x in checks)
    out={
        'schema':SCHEMA,
        'technical_status':'PASS' if passed else 'FAIL',
        'verdict':(
            'PASS_HOLONOMY_PARTITION_IS_BOOKKEEPING_UNLESS_TOTAL_SOURCE_CHANGES'
            if passed else
            'FAIL_HOLONOMY_BIANCHI_CHANNEL_LEDGER'
        ),
        'canon_allowed':False,
        'checks':checks,
        'next_gate':'DERIVE_NONZERO_CONSERVATION_COMPATIBLE_DELTA_T_HOL_FROM_INDEPENDENT_TEMPORAL_U1_PHYSICS_OR_TOPOLOGICAL_SECTOR',
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=='__main__':
    main()
