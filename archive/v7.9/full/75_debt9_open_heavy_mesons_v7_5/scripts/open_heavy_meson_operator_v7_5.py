#!/usr/bin/env python3
"""
Open heavy meson operator v7.5 — semantic curvature inheritance on Poincaré disk.

Hidden heavy (J/psi, Upsilon):  lambda = OI * [p^2 + sum_lighter_heavy(q^2 - L3^2 + L3/L5)]
Open heavy (D, B):              see lambda_open() below

References:
  - PDG 2024
  - CIEL/0 Metatime framework v7.5
  - DEBT-009 heavy meson sector freeze
"""

import math, sys, json

# === FUNDAMENTAL CONSTANTS ===
OI = math.log(2) / (24 * math.pi)
L3, L4, L5 = 7, 2, 5
E0 = 1037.9
E_base = E0 * math.exp(-2 * OI)

QUARK_PRIMES = {'u': 3, 'd': 5, 's': 7, 'c': 11, 'b': 13, 't': 17}

def lambda_hidden(p):
    """Lambda for hidden heavy meson (qq-bar, both same prime p > 7)."""
    # sum over all lighter heavy quarks (q > 7, q < p)
    s = p ** 2
    for q in QUARK_PRIMES.values():
        if 7 < q < p:
            s += q ** 2 - L3 ** 2 + L3 / L5
    return OI * s

def lambda_open(p, q):
    """Lambda for open heavy meson (heavy p, light q)."""
    if p == 11:  # charm — first heavy, partial escape, boundary coupling c×(L3-1)
        base = p * (L3 - 1)
        if q == 7:  # s partner: extra from s at cavity center (r=0)
            base += (p - L3) * L5 * L4 / L3
    elif p == 13:  # bottom — full escape, λ from lighter quarks only (no b²)
        base = QUARK_PRIMES['u']**2 + QUARK_PRIMES['s']**2 + QUARK_PRIMES['c']**2  # u²+s²+c² = 179
        if q == 7:  # s partner
            base += (p - QUARK_PRIMES['c']) * (L3 - 1) / L3
    else:
        raise ValueError(f"Unknown heavy quark prime: {p}")
    return OI * base

def mass_from_lambda(lam):
    return E0 * math.exp(-lam) * math.exp(-2 * OI)

def mass_open(p, q):
    return mass_from_lambda(-lambda_open(p, q))

def mass_hidden(p):
    return mass_from_lambda(-lambda_hidden(p))

# === TEST ALL ===

MESONS = [
    # hidden heavy
    ('J/psi', 11, 11, 3096.90),
    ('Upsilon', 13, 13, 9460.30),
    # open charm
    ('D+', 11, 5, 1869.66),
    ('D0', 11, 3, 1864.84),
    ('D_s+', 11, 7, 1968.35),
    # open bottom
    ('B+', 13, 3, 5279.34),
    ('B0', 13, 5, 5279.66),
    ('B_s0', 13, 7, 5366.92),
]

def main():
    print("=" * 70)
    print("  OPEN HEAVY MESON OPERATOR v7.5")
    print("  Semantic curvature inheritance on Poincaré disk")
    print("=" * 70)
    print()
    print(f"  OI = ln(2)/(24*pi) = {OI:.10f}")
    print(f"  L3 = {L3},  L4 = {L4},  L5 = {L5}")
    print(f"  E0 = {E0:.2f} MeV,  E_base = {E_base:.2f} MeV")
    print()
    print(f"  {'Meson':<10} {'p':>3} {'q':>3} {'lam':>10} {'E_pred':>10} {'E_PDG':>10} {'err%':>8}")
    print("-" * 70)

    results = []
    for name, p, q, ref in MESONS:
        if p == q and p > 7:
            lam = lambda_hidden(p)
        else:
            lam = lambda_open(p, q)
        lam_val = -lam  # positive lambda for mass formula
        E_pred = mass_from_lambda(-lam)  # -lam because E = E0*exp(-(-lam))*exp(-2*OI)
        err = (E_pred - ref) / ref * 100

        results.append({
            'name': name,
            'p': p, 'q': q,
            'lambda': round(lam_val, 6),
            'E_pred': round(E_pred, 2),
            'E_PDG': ref,
            'error_pct': round(err, 2)
        })

        print(f"  {name:<10} {p:>3} {q:>3} {lam_val:>10.6f} {E_pred:>10.2f} {ref:>10.2f} {err:>+7.2f}%")

    print()
    print("-" * 70)
    print(f"  Mean |error|: {sum(abs(r['error_pct']) for r in results)/len(results):.3f}%")

    # Save results
    with open("/tmp/ciel_metatime/METATIME_STANDARD_MODEL_DERIVATION_MERGED_REPO_v7_0_E_MU_RELEASE_REFINEMENT_GATE_NO_NESTED_ZIPS/75_debt9_open_heavy_mesons_v7_5/results/open_heavy_meson_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"  Results saved.")

    return 0

if __name__ == "__main__":
    sys.exit(main())
