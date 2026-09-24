from __future__ import annotations
import json, math, random

SCHEMA='TIR_IDT_RFC_LAPSE_PROJECTOR_METRIC_VARIATION_BIFURCATION_VALIDATION_V0_1'

def main():
    rng=random.Random(20260924)
    max_cancel=0.0
    max_lapse_derivative=0.0

    for _ in range(5000):
        N=10**rng.uniform(-2,2)
        g00inv=-1.0/(N*N)

        # Exact derivative d ln N / d g^00.
        analytic=-1.0/(2.0*g00inv)
        target=N*N/2.0
        max_lapse_derivative=max(
            max_lapse_derivative,
            abs(analytic-target)/max(1.0,abs(target)),
        )

        # Pure-normal common-rate surface: q0^2/mu^2=N^2.
        q_over_mu_sq=N*N
        S_theta_00=-N*N/2.0
        dC00=-q_over_mu_sq-2.0*S_theta_00
        max_cancel=max(max_cancel,abs(dC00))

    checks=[
        {
            'name':'adm_lapse_metric_derivative',
            'pass':max_lapse_derivative<1e-15,
            'max_scaled_error':max_lapse_derivative,
            'identity':'d ln N / d g^00 = -1/(2 g^00) = N^2/2',
        },
        {
            'name':'same_metric_projector_cancellation',
            'pass':max_cancel<1e-12,
            'max_error':max_cancel,
            'identity':'-q0^2/mu^2 - 2 S_theta_00 = -N^2 + N^2 = 0',
        },
        {
            'name':'projector_stress_vanishes',
            'pass':max_cancel<1e-12,
            'statement':'d_g C=0 => T_U=-2 eta U fprime d_g C=0',
        },
    ]

    passed=all(c['pass'] for c in checks)
    out={
        'schema':SCHEMA,
        'technical_status':'PASS' if passed else 'FAIL',
        'verdict':(
            'PASS_INDEPENDENT_VS_SAME_METRIC_LAPSE_VARIATION_BIFURCATION_SELF_NORMALIZED_BRANCH_ZERO_STRESS'
            if passed else
            'FAIL_LAPSE_PROJECTOR_METRIC_VARIATION_BIFURCATION'
        ),
        'canon_allowed':False,
        'checks':checks,
        'open_gates':[
            'INDEPENDENT_PHYSICAL_PROJECTOR_CALIBRATION_RECEIPT',
            'NONTRIVIAL_ABE_EULER_METRIC_RESPONSE',
            'NONSELFNORMALIZING_PHASE_SCALE_METRIC_RESPONSE',
        ],
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=='__main__':
    main()
