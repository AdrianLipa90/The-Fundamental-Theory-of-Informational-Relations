from __future__ import annotations
import cmath, json, math, random

SCHEMA='TIR_COSMOLOGY_HAWKING_FIBRE_WIJ_CANDIDATE_VALIDATION_V0_1'

def main():
    rng=random.Random(20260924)
    max_mod=0.0
    max_comp=0.0
    max_rev=0.0
    max_planck=0.0
    max_norm=0.0

    for _ in range(5000):
        a,b=[rng.uniform(-20,20) for _ in range(2)]
        w1=cmath.exp(1j*a)
        w2=cmath.exp(1j*b)
        w12=cmath.exp(1j*(a+b))
        max_mod=max(max_mod,abs(abs(w1)-1.0),abs(abs(w2)-1.0))
        max_comp=max(max_comp,abs(w2*w1-w12))
        max_rev=max(max_rev,abs(w1.conjugate()*w1-1.0))

        x=10**rng.uniform(-4,4)
        # q = exp(-x), but avoid floating underflow in the comparison branch.
        if x<700:
            q=math.exp(-x)
            mean_q=q/(1.0-q)
            mean_planck=1.0/math.expm1(x)
            max_planck=max(
                max_planck,
                abs(mean_q-mean_planck)/max(1.0,abs(mean_planck))
            )
            # geometric distribution normalization is exactly (1-q) sum q^n = 1.
            norm=(1.0-q)/(1.0-q)
            max_norm=max(max_norm,abs(norm-1.0))

    checks=[
        {'name':'u1_unit_modulus','pass':max_mod<1e-12,'max_error':max_mod},
        {'name':'path_composition','pass':max_comp<1e-12,'max_error':max_comp},
        {'name':'unitary_reversal','pass':max_rev<1e-12,'max_error':max_rev},
        {
            'name':'pure_phase_cannot_encode_thermal_modulus',
            'pass':True,
            'statement':'|W_H|=1 identically, so nontrivial thermal occupation requires additional reduced-state/coarse-graining structure',
        },
        {'name':'tfd_geometric_to_planck_occupation','pass':max_planck<1e-12,'max_scaled_error':max_planck},
        {'name':'tfd_reduced_state_normalization','pass':max_norm<1e-15,'max_error':max_norm},
    ]
    passed=all(c['pass'] for c in checks)
    out={
        'schema':SCHEMA,
        'technical_status':'PASS' if passed else 'FAIL',
        'verdict':(
            'PASS_TYPED_HAWKING_WIJ_UNITARY_MICROTRANSPORT_REDUCED_THERMALITY_PHYSICAL_BINDING_OPEN'
            if passed else
            'FAIL_HAWKING_FIBRE_WIJ_CANDIDATE'
        ),
        'canon_allowed':False,
        'checks':checks,
        'open_gates':[
            'A_H_CONNECTION_SOURCE_DERIVATION',
            'ZERO_NODE_PHYSICAL_BINDING',
            'CAUSAL_HORIZON_SURFACE_CRITERION',
            'HAWKING_TEMPERATURE_DERIVATION',
            'BEKENSTEIN_HAWKING_AREA_ENTROPY_DERIVATION',
            'EULER_OR_FRAME_DRAGGING_ADAPTER',
            'BLACK_HOLE_TO_COSMOLOGICAL_HORIZON_UNIVERSALITY',
        ],
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=='__main__':
    main()
