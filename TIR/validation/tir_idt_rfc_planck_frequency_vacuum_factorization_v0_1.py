from __future__ import annotations
import json, math, random

SCHEMA='TIR_IDT_RFC_PLANCK_FREQUENCY_VACUUM_FACTORIZATION_VALIDATION_V0_1'

def main():
    rng=random.Random(20260924)
    max_ratio=0.0
    max_full_tetra=0.0

    for _ in range(5000):
        c=10**rng.uniform(1,10)
        hbar=10**rng.uniform(-40,-20)
        G=10**rng.uniform(-15,-5)
        q0=hbar*10**rng.uniform(-2,2)
        N=10**rng.uniform(-2,2)
        a_fs=10**rng.uniform(-2,2)
        chi=10**rng.uniform(-140,-1)

        omega_p=math.sqrt(c**5/(hbar*G))
        eps_p=c**7/(hbar*G**2)
        K0=q0*N/(2*a_fs*c**3)
        C=omega_p**4*chi
        rho=K0*C
        zeta=q0/hbar
        target=(N*zeta/(2*a_fs))*eps_p*chi
        max_ratio=max(max_ratio,abs(rho-target)/max(abs(target),1e-300))

        rho_full=(hbar*N/(2*math.pi*c**3))*omega_p**4*chi
        target_full=(N/(2*math.pi))*eps_p*chi
        max_full_tetra=max(
            max_full_tetra,
            abs(rho_full-target_full)/max(abs(target_full),1e-300)
        )

    r=(2/7)**224
    chi_legacy=2*math.pi*r

    checks=[
        {
            'name':'planck_frequency_dimensionful_factorization',
            'pass':max_ratio<1e-12,
            'max_relative_error':max_ratio,
        },
        {
            'name':'full_tetra_q0_hbar_specialization',
            'pass':max_full_tetra<1e-12,
            'max_relative_error':max_full_tetra,
        },
        {
            'name':'legacy_224_translation',
            'pass':abs(r-1.345110818116154e-122)/r<1e-14,
            'r_224':r,
            'chi_full_tetra_unit':chi_legacy,
        },
    ]

    passed=all(c['pass'] for c in checks)
    out={
        'schema':SCHEMA,
        'technical_status':'PASS' if passed else 'FAIL',
        'verdict':(
            'PASS_PLANCK_REFERENCE_FACTORIZATION_INTERNAL_DIMENSIONLESS_VACUUM_INVARIANT_OPEN'
            if passed else
            'FAIL_PLANCK_REFERENCE_FACTORIZATION'
        ),
        'canon_allowed':False,
        'checks':checks,
        'open_gates':[
            'INTERNAL_G_DERIVATION',
            'PHYSICAL_Q0_OVER_HBAR_BINDING',
            'PHYSICAL_PHASE_CELL_OCCUPATION',
            'INDEPENDENT_CHI_LAMBDA_TOPOLOGICAL_DERIVATION',
            'INDEPENDENT_224_EXPONENT_DERIVATION',
        ],
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=='__main__':
    main()
