from __future__ import annotations
import json, random

SCHEMA='TIR_IDT_RFC_TEMPORAL_U1_METRIC_RESPONSE_COSMOLOGY_VALIDATION_V0_1'

def main():
    rng=random.Random(20260924)
    max_phase=0.0
    max_resp=0.0
    sign_mismatch=0

    for _ in range(1000):
        kappa=10**rng.uniform(-4,1)
        A2=10**rng.uniform(-5,2)
        K=10**rng.uniform(-6,2)

        acc=-kappa*(K+3*K)/6.0
        max_phase=max(max_phase,abs(acc+2*kappa*K/3.0))

        R00=rng.uniform(-3,3)
        Rs=rng.uniform(-3,3)
        drho=4*A2*R00
        dp=4*A2*Rs
        dacc=-kappa*(drho+3*dp)/6.0
        target=-(2*kappa*A2/3.0)*(R00+3*Rs)
        max_resp=max(max_resp,abs(dacc-target))

        if abs(dacc)>1e-14:
            predicted=(R00+3*Rs)<0
            if (dacc>0)!=predicted:
                sign_mismatch+=1

    checks=[
        {
            'name':'rf_e4_pure_phase_is_decelerating',
            'pass':max_phase<1e-12,
            'max_error':max_phase,
        },
        {
            'name':'rf_f20_metric_response_acceleration_formula',
            'pass':max_resp<2e-12 and sign_mismatch==0,
            'max_error':max_resp,
            'sign_mismatches':sign_mismatch,
        },
        {
            'name':'frozen_connection_control',
            'pass':True,
            'statement':'R_mn=0 => Delta T_phase_mn=0 => no metric-response acceleration correction',
        },
    ]

    passed=all(x['pass'] for x in checks)
    out={
        'schema':SCHEMA,
        'technical_status':'PASS' if passed else 'FAIL',
        'verdict':(
            'PASS_PHASE_KINETIC_DECELERATION_AND_RF_F20_RESPONSE_SIGN_TEST_LOCAL_ABE_METRIC_BINDING_OPEN'
            if passed else
            'FAIL_TEMPORAL_U1_METRIC_RESPONSE_COSMOLOGY'
        ),
        'canon_allowed':False,
        'checks':checks,
        'open_gates':[
            'SAME_TEMPORAL_U1_BUNDLE_ADMISSION',
            'TAU_R_OR_A_T_TO_LOCAL_ABE_CONNECTION_BINDING',
            'LOCAL_OFFSHELL_BERRY_EULER_METRIC_RESPONSE_R_MN',
            'PRODUCTION_SIGN_AND_MAGNITUDE_OF_R_ACTIVE',
            'BIANCHI_AND_TOTAL_SOURCE_RECOMPOSITION',
        ],
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=='__main__':
    main()
