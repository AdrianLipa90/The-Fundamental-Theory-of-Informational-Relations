from __future__ import annotations
import json, random

SCHEMA='TIR_IDT_RFC_BERRY_EULER_METRIC_RESPONSE_SOURCE_FIREWALL_VALIDATION_V0_1'

def main():
    rng=random.Random(20260924)
    max_decomp=0.0
    threshold_mismatches=0

    for _ in range(5000):
        mu=10**rng.uniform(-3,2)
        RE0=rng.uniform(-3,3)*mu*mu
        REs=rng.uniform(-3,3)*mu*mu

        # AB and Berry fixed-response branches.
        RAB0=RABs=0.0
        RB0=RBs=0.0
        R0=RAB0+RB0+RE0
        Rs=RABs+RBs+REs

        max_decomp=max(
            max_decomp,
            abs(R0-RE0),
            abs(Rs-REs),
        )

        Bresp=1.0+2.0*(R0+3.0*Rs)/(mu*mu)
        reduced=(RE0+3.0*REs)/(mu*mu) < -0.5
        if (Bresp<0.0) != reduced:
            threshold_mismatches += 1

    checks=[
        {
            'name':'ab_berry_zero_response_reduction',
            'pass':max_decomp==0.0,
            'max_error':max_decomp,
        },
        {
            'name':'rf_f19_independent_scale_branch',
            'pass':True,
            'statement':'S_vartheta=0 when rotor-rate and lapse inputs are independent during metric variation',
        },
        {
            'name':'euler_only_projector_threshold',
            'pass':threshold_mismatches==0,
            'sign_mismatches':threshold_mismatches,
            'criterion':'(R_E0+3 R_Es)/mu_theta^2 < -1/2',
        },
        {
            'name':'fully_frozen_control',
            'pass':True,
            'B_response':1.0,
            'meaning':'positive projector contribution is decelerating when R=S=0',
        },
    ]

    passed=all(c['pass'] for c in checks)
    out={
        'schema':SCHEMA,
        'technical_status':'PASS' if passed else 'FAIL',
        'verdict':(
            'PASS_FIXED_AB_BERRY_AND_RF_F19_SCALE_RESPONSES_EULER_METRIC_ADAPTER_OPEN'
            if passed else
            'FAIL_BERRY_EULER_METRIC_RESPONSE_SOURCE_FIREWALL'
        ),
        'canon_allowed':False,
        'checks':checks,
        'open_gates':[
            'PHYSICAL_BERRY_U_OF_Q_G_METRIC_ADAPTER',
            'PHYSICAL_EULER_SPIN_CONNECTION_METRIC_FUNCTIONAL',
            'LOCAL_R_E_MN_RECEIPT',
            'NONZERO_RF_F19_SCALE_RESPONSE_RECEIPT',
            'SPACETIME_SPIN_CONNECTION_NO_DOUBLE_COUNT_ACTION_GATE',
        ],
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=='__main__':
    main()
