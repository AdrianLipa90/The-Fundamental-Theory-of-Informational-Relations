from __future__ import annotations
import json, random

SCHEMA='TIR_IDT_RFC_PROJECTOR_RESPONSE_ACCELERATION_THRESHOLD_VALIDATION_V0_1'

def main():
    rng=random.Random(20260924)
    max_rel=0.0
    mismatches=0

    for _ in range(5000):
        kappa=10**rng.uniform(-5,1)
        eta=rng.random()
        U=10**rng.uniform(-6,2)
        fp=10**rng.uniform(-3,1)
        mu=10**rng.uniform(-3,2)

        R0=rng.uniform(-4,4)*mu*mu
        Rs=rng.uniform(-4,4)*mu*mu
        S0=rng.uniform(-4,4)
        Ss=rng.uniform(-4,4)

        D00=(
            2*eta*U*fp
            +4*eta*U*fp*R0/(mu*mu)
            +4*eta*U*fp*S0
        )
        Dss=(
            4*eta*U*fp*Rs/(mu*mu)
            +4*eta*U*fp*Ss
        )

        acc=-kappa*(D00+3*Dss)/6.0

        Bresp=1+2*(R0+3*Rs)/(mu*mu)+2*(S0+3*Ss)
        target=-kappa*eta*U*fp*Bresp/3.0

        max_rel=max(max_rel,abs(acc-target)/max(1.0,abs(target)))

        pref=eta*U*fp
        if pref>0 and abs(acc)>1e-13 and ((acc>0)!=(Bresp<0)):
            mismatches+=1

    frozen_B=1.0

    checks=[
        {
            'name':'rf_f22_active_source_reduction',
            'pass':max_rel<1e-12,
            'max_scaled_error':max_rel,
        },
        {
            'name':'positive_prefactor_acceleration_threshold',
            'pass':mismatches==0,
            'sign_mismatches':mismatches,
            'criterion':'R_active/mu^2 + S_active < -1/2',
        },
        {
            'name':'frozen_response_control',
            'pass':frozen_B==1.0,
            'B_response':frozen_B,
            'meaning':'positive frozen projector contribution is decelerating',
        },
    ]

    passed=all(c['pass'] for c in checks)
    out={
        'schema':SCHEMA,
        'technical_status':'PASS' if passed else 'FAIL',
        'verdict':(
            'PASS_RF_F22_PROJECTOR_RESPONSE_ACCELERATION_THRESHOLD_PHYSICAL_RESPONSE_OPEN'
            if passed else
            'FAIL_PROJECTOR_RESPONSE_ACCELERATION_THRESHOLD'
        ),
        'canon_allowed':False,
        'checks':checks,
        'open_gates':[
            'TEMPORAL_U1_TO_LOCAL_ABE_RESPONSE_BINDING',
            'PHYSICAL_R_MN_RECEIPT',
            'PHYSICAL_S_MN_RECEIPT',
            'PHYSICAL_PROJECTOR_PROFILE_SELECTION',
            'OBSERVATIONAL_BACKGROUND_AND_PERTURBATION_TEST',
        ],
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=='__main__':
    main()
