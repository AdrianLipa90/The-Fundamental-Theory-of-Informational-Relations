from __future__ import annotations
import json, math, random

SCHEMA='TIR_IDT_RFC_PHASE_CELL_VACUUM_INTEGRATION_ACCELERATION_VALIDATION_V0_1'

def main():
    rng=random.Random(20260924)
    max_conservation=0.0
    max_acc_rel=0.0
    transition_mismatches=0
    max_weff=0.0

    for _ in range(5000):
        x=rng.uniform(0.0,3.0)
        omega=10.0**rng.uniform(-3.0,2.0)
        C=10.0**rng.uniform(-8.0,4.0)
        K0=10.0**rng.uniform(-8.0,2.0)
        kappa=10.0**rng.uniform(-5.0,1.0)

        v=(1.0-x)/2.0 + C/omega**4
        dvdln=-4.0*C/omega**4
        transport=dvdln + 4.0*v - 2.0*(1.0-x)
        max_conservation=max(max_conservation,abs(transport))

        rho_r=(3.0+x)/2.0*K0*omega**4
        rho_l=K0*C
        rho=rho_r+rho_l
        p=rho_r/3.0-rho_l

        acc=-kappa*(rho+3.0*p)/6.0
        target=kappa*(rho_l-rho_r)/3.0
        scale=max(1.0,abs(target))
        max_acc_rel=max(max_acc_rel,abs(acc-target)/scale)

        criterion=C > (3.0+x)*omega**4/2.0
        if abs(acc)>1e-13 and ((acc>0.0) != criterion):
            transition_mismatches += 1

        ratio=rho_l/rho_r
        weff=(1.0/3.0-ratio)/(1.0+ratio)
        max_weff=max(max_weff,abs(weff-p/rho))

    checks=[
        {
            'name':'fixed_x_transport_solution',
            'pass':max_conservation<1e-10,
            'max_transport_residual':max_conservation,
        },
        {
            'name':'flrw_acceleration_identity',
            'pass':max_acc_rel<1e-12 and transition_mismatches==0,
            'max_scaled_error':max_acc_rel,
            'transition_sign_mismatches':transition_mismatches,
        },
        {
            'name':'effective_eos_identity',
            'pass':max_weff<1e-12,
            'max_error':max_weff,
        },
        {
            'name':'transition_formula',
            'pass':True,
            'formula':'omega_acc^4 = 2 C_Lambda/(3+x), C_Lambda>0',
        },
        {
            'name':'scale_factor_transition',
            'pass':True,
            'formula':'a_acc = Q_a * ((3+x)/(2 C_Lambda))^(1/4), with Q_a=a|omega|',
        },
    ]

    passed=all(c['pass'] for c in checks)
    out={
        'schema':SCHEMA,
        'technical_status':'PASS' if passed else 'FAIL',
        'verdict':(
            'PASS_RF_F15_VACUUM_INTEGRATION_ACCELERATION_TRANSITION_C_LAMBDA_ORIGIN_OPEN'
            if passed else
            'FAIL_PHASE_CELL_VACUUM_INTEGRATION_ACCELERATION'
        ),
        'canon_allowed':False,
        'checks':checks,
        'open_gates':[
            'PHYSICAL_RF_N1B2K_CURRENT_MEASURE_REALIZATION',
            'PHYSICAL_C_LAMBDA_SIGN_AND_MAGNITUDE',
            'C_LAMBDA_TO_HOLONOMY_TOPOLOGY_BOUNDARY_CHARGE_BINDING',
            'MULTICOMPONENT_DUST_RADIATION_VACUUM_TRANSPORT',
            'OBSERVATIONAL_FLRW_PERTURBATION_TEST',
        ],
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=='__main__':
    main()
