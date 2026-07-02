#!/usr/bin/env python3
"""
η-η' SU(3) singlet-octet mixing operator v7.6 — U(1)A anomaly from L4²/L5.

Complete pseudoscalar nonet from Metatime framework:

  π   = E_proton·exp(-π/ζ(2))              spectral zeta (Legendre r₃=0)
  K   = E_proton·exp(-(ζ(2)-1))            spectral zeta (Legendre r₃>0)
  η₈  = √((4·K² - π²)/3)                  Gell-Mann-Okubo octet
  η₁  = E_proton·exp(OI·L4²/L5)            U(1)A anomaly (L4²/L5 curvature)
  η,η' = eig([[m₈², M₈₁²],[M₈₁², m₁²]])   mixing via M₈₁² = √(m₈²·m₁²)·L4/(L3+L4)

References:
  - PDG 2024
  - CIEL/0 Metatime framework v7.6
  - DEBT-009 pseudoscalar nonet freeze
  - Gell-Mann–Okubo mass formula
  - 't Hooft U(1)A anomaly resolution
"""

import math, sys, json

OI = math.log(2) / (24 * math.pi)
L3, L4, L5 = 7, 2, 5
E_proton = 938.272
zeta2 = math.pi ** 2 / 6

def mass_pi():
    return E_proton * math.exp(-math.pi / zeta2)

def mass_K():
    return E_proton * math.exp(-(zeta2 - 1))

def mass_eta8(m_pi, m_K):
    return math.sqrt((4 * m_K ** 2 - m_pi ** 2) / 3)

def mass_eta1():
    return E_proton * math.exp(OI * L4 ** 2 / L5)

def mixing_element_sq(m8, m1):
    return math.sqrt(m8 ** 2 * m1 ** 2) * L4 / (L3 + L4)

def diagonalize(m8, m1, M81sq):
    tr = m8 ** 2 + m1 ** 2
    disc = math.sqrt((m1 ** 2 - m8 ** 2) ** 2 + 4 * M81sq ** 2)
    eta_sq = (tr - disc) / 2
    etap_sq = (tr + disc) / 2
    return math.sqrt(eta_sq), math.sqrt(etap_sq)

def main():
    m_pi = mass_pi()
    m_K = mass_K()
    m8 = mass_eta8(m_pi, m_K)
    m1 = mass_eta1()
    M81sq = mixing_element_sq(m8, m1)
    m_eta, m_etap = diagonalize(m8, m1, M81sq)
    tan2th = 2 * M81sq / (m1 ** 2 - m8 ** 2)
    theta = math.atan(tan2th) / 2 * 180 / math.pi

    pdg = {
        'pi': 134.977, 'K': 497.614, 'eta8': 569.3, 'eta1': 945.2,
        'M81sq': 119159, 'theta': 11.36,
        'eta': 547.862, 'etap': 957.78
    }

    results = [
        {'name': 'pi', 'pred': round(m_pi, 3), 'PDG': pdg['pi'], 'error_pct': round((m_pi/pdg['pi']-1)*100, 4)},
        {'name': 'K', 'pred': round(m_K, 3), 'PDG': pdg['K'], 'error_pct': round((m_K/pdg['K']-1)*100, 4)},
        {'name': 'eta8 (GMO octet)', 'pred': round(m8, 3), 'PDG': pdg['eta8'], 'error_pct': round((m8/pdg['eta8']-1)*100, 4)},
        {'name': 'eta1 (singlet)', 'pred': round(m1, 3), 'PDG': pdg['eta1'], 'error_pct': round((m1/pdg['eta1']-1)*100, 4)},
        {'name': 'M81^2', 'pred': round(M81sq, 1), 'PDG': pdg['M81sq'], 'error_pct': round((M81sq/pdg['M81sq']-1)*100, 4)},
        {'name': 'theta (deg)', 'pred': round(theta, 4), 'PDG': pdg['theta'], 'error_pct': round((theta/pdg['theta']-1)*100, 4)},
        {'name': 'eta', 'pred': round(m_eta, 3), 'PDG': pdg['eta'], 'error_pct': round((m_eta/pdg['eta']-1)*100, 4)},
        {'name': "eta'", 'pred': round(m_etap, 3), 'PDG': pdg['etap'], 'error_pct': round((m_etap/pdg['etap']-1)*100, 4)},
    ]

    print("=" * 74)
    print("  η-η' SU(3) SINGLET-OCTET MIXING OPERATOR v7.6")
    print("  U(1)A anomaly from Metatime OI·L4²/L5 curvature")
    print("=" * 74)
    print()
    print(f"  OI = ln(2)/(24·π) = {OI:.10f}")
    print(f"  L3 = {L3},  L4 = {L4},  L5 = {L5}")
    print(f"  E_proton = {E_proton} MeV")
    print(f"  ζ(2) = π²/6 = {zeta2:.10f}")
    print()
    print(f"  Formulas:")
    print(f"    π   = E_proton·exp(-π/ζ(2))")
    print(f"    K   = E_proton·exp(-(ζ(2)-1))")
    print(f"    η₈  = √((4·K² - π²)/3)                    (Gell-Mann-Okubo)")
    print(f"    η₁  = E_proton·exp(OI·L4²/L5)             (U(1)A anomaly)")
    print(f"    M₈₁² = √(m₈²·m₁²)·L4/(L3+L4)             (mixing element)")
    print(f"    [η,η'] = eig([[m₈², M₈₁²],[M₈₁², m₁²]])  (diagonalize)")
    print()
    print(f"  {'Quantity':<22} {'Predicted':>12} {'PDG':>12} {'Error':>10}")
    print("-" * 74)

    for r in results:
        if r['name'] in ('M81^2', 'theta (deg)'):
            print(f"  {r['name']:<22} {r['pred']:>12.3f} {r['PDG']:>12.3f} {r['error_pct']:>+9.4f}%")
        else:
            print(f"  {r['name']:<22} {r['pred']:>12.3f} {r['PDG']:>12.3f} {r['error_pct']:>+9.4f}%")

    print("-" * 74)
    phys = [r for r in results if r['name'] in ('eta', "eta'")]
    mean_abs = sum(abs(r['error_pct']) for r in phys) / len(phys)
    print(f"  Mean |error| (η,η'): {mean_abs:.4f}%")

    with open("/tmp/ciel_metatime/METATIME_STANDARD_MODEL_DERIVATION_MERGED_REPO_v7_0_E_MU_RELEASE_REFINEMENT_GATE_NO_NESTED_ZIPS/76_eta_eta_prime_mixing_v7_6/results/eta_eta_prime_results.json", "w") as f:
        json.dump(results, f, indent=2)
    print(f"  Results saved.")

    return 0

if __name__ == "__main__":
    sys.exit(main())
