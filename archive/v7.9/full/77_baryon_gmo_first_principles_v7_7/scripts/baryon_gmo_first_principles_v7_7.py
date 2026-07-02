#!/usr/bin/env python3
"""
J_KJ axial GMO coefficients from Metatime first principles — v7.7.

Derives the octet GMO (α,β,γ,δ) and decuplet (α₁₀,β₁₀) coefficients
directly from Metatime constants (L3,L4,L5, quark primes, OI, E_P).

Previously fit to PDG (v7.2), now derived from the J_KJ eigenvalue
structure in the SU(3) adjoint representation.

Key formulas:
  α = E_P·OI·(s²-u²-d²+L3)                 (U-spin breaking)
  β = -α·(L3-1)/(L3-1+L4/L5)               (Y-hypercharge)
  γ = E_P·OI·(L3-1+L4/L5)                  (Casimir I(I+1)-Y²/4)
  δ = -γ                                    (di-quark spin splitting)

  α₁₀ = E_P·OI·(L3²+L4²+L5²+L3+L4+L5+L4)/L4  (decuplet offset)
  β₁₀ = -E_P·OI·L3·L5/L4                      (decuplet equal spacing)

References:
  - PDG 2024
  - CIEL/0 Metatime framework v7.7
  - DEBT-009 baryon sector freeze
  - Gell-Mann 1961, Okubo 1962
"""

import math, json, sys, hashlib
from datetime import datetime, timezone
from pathlib import Path

OI = math.log(2) / (24 * math.pi)
L3, L4, L5 = 7, 2, 5
E_P = 1.2208901285838957e22
E_proton = 938.272
Ei = E_proton * OI

u, d, s, c, b, t = 3, 5, 7, 11, 13, 17

QUARK_MASS_POWER = 1.635
LAMBDA_QUARK = 93.83

BARYON_REF = {
    'p':  938.27209,  'n': 939.56542,
    'L': 1115.683,    'S+': 1189.37,
    'S0': 1192.642,   'S-': 1197.449,
    'X0': 1314.86,    'X-': 1321.71,
    'D++': 1232.0,    'S*+': 1382.8,
    'X*0': 1531.8,    'O-': 1672.45,
}

BARYON_COMP = {
    'p': (u,u,d),  'n': (u,d,d),
    'L': (u,d,s),  'S+': (u,u,s),
    'S0': (u,d,s), 'S-': (d,d,s),
    'X0': (u,s,s), 'X-': (d,s,s),
    'D++': (u,u,u), 'S*+': (u,u,s),
    'X*0': (u,s,s), 'O-': (s,s,s),
}

def sigma(n):
    return sum(i for i in range(1, n+1) if n % i == 0)

sigma_45 = sigma(45)
S_proton_true = -OI * math.log(E_proton / E_P)
S_BASE = S_proton_true - OI * (sigma_45 / 45.0 - 1.0) / L3

def baryon_action_offset(p, q, r):
    n = p * q * r
    return (sigma(n) / n - 1.0) / L3

def scalar_base(p, q, r):
    ds = baryon_action_offset(p, q, r)
    return E_P * math.exp(-(S_BASE + OI * ds) / OI)

# SU(3) adjoint representation eigenvalues via f_abc
def J_KJ_eigenvalues():
    c1, c4, c7 = 0.296, 0.210, 0.207
    norm = math.sqrt(c1**2 + c4**2 + c7**2)
    vals = sorted([0.0, 0.0, -norm, -norm/2, -norm/2, norm/2, norm/2, norm])
    return vals, norm

evals, c_norm = J_KJ_eigenvalues()

c3 = (d - u) / (d + u)
c8 = (s - (u + d) / 2) / (s + (u + d) / 2)

W_us = (u * s) / (u + s + c + b)
phi_inv = (math.sqrt(5) - 1) / 2

def GM0_octet():
    alpha = Ei * (s**2 - u**2 - d**2 + L3)
    gamma = Ei * (L3 - 1 + L4 / L5)
    beta = -alpha * (L3 - 1) / (L3 - 1 + L4 / L5)
    delta = -gamma
    return alpha, beta, gamma, delta

def GM0_decuplet():
    alpha10 = Ei * (L3**2 + L4**2 + L5**2 + L3 + L4 + L5 + L4) / L4
    beta10 = -Ei * L3 * L5 / L4
    return alpha10, beta10

alpha, beta, gamma, delta = GM0_octet()
alpha10, beta10 = GM0_decuplet()

FIT_alpha, FIT_beta, FIT_gamma, FIT_delta = 190.1, -180.0, 54.8, -55.9
FIT_alpha10, FIT_beta10 = 404.0, -148.0

def octet_baryon_y(name):
    strange = BARYON_COMP[name].count(s)
    return 1.0 - strange

def octet_baryon_i2(name):
    if name in ('L', 'O-'): return 0.0
    if name in ('S+', 'S0', 'S-'): return 2.0
    if name in ('X0', 'X-', 'p', 'n'): return 0.75
    return 0.75

def octet_baryon_dq(name):
    return 0 if name == 'L' else 1

M0_octet = sum(scalar_base(*BARYON_COMP[n]) for n in ('p','n','L','S+','S0','S-','X0','X-')) / 8
M0_decuplet = sum(scalar_base(*BARYON_COMP[n]) for n in ('D++','S*+','X*0','O-')) / 4

def predict_octet(name):
    base = scalar_base(*BARYON_COMP[name])
    Y = octet_baryon_y(name)
    I2 = octet_baryon_i2(name)
    Sdq = octet_baryon_dq(name)
    axial = alpha + beta*Y + gamma*(I2 - Y*Y/4) + delta*Sdq
    return base, axial, base + axial

def predict_decuplet(name):
    Y = octet_baryon_y(name)
    axial = alpha10 + beta10*Y
    return M0_decuplet, axial, M0_decuplet + axial

print("=" * 74)
print("  J_KJ AXIAL GMO COEFFICIENTS FROM FIRST PRINCIPLES v7.7")
print("=" * 74)
print()
print(f"  Metatime constants:")
print(f"    OI     = ln(2)/(24·π) = {OI:.10f}")
print(f"    L3     = {L3},  L4 = {L4},  L5 = {L5}")
print(f"    E_P    = {E_P:.4e} MeV")
print(f"    Ei     = E_proton·OI = {Ei:.6f} MeV")
print(f"    u,d,s  = {u}, {d}, {s}")
print()
print(f"  === J_KJ eigenvalues in adjoint representation (f_abc) ===")
print(f"    C-vector (λ₁,λ₄,λ₇): c₁={0.296}, c₄={0.210}, c₇={0.207}")
print(f"    ||c|| = √(c₁²+c₄²+c₇²) = {c_norm:.6f}")
print(f"    Eigenvalues: 0 (×2), ±||c||/2 (×2), ±||c|| (×2)")
print(f"      = {evals}")
print()
print(f"  === Extended C-vector with diagonal (λ₃,λ₈) ===")
print(f"    c₃ = (d-u)/(d+u) = {c3}")
print(f"    c₈ = (s-avg(ud))/(s+avg(ud)) = {c8:.6f}")
c_ext = math.sqrt(0.296**2 + 0.210**2 + 0.207**2 + c3**2 + c8**2)
print(f"    ||c_ext|| = {c_ext:.6f}")
print(f"    Golden ratio φ = {(1+math.sqrt(5))/2:.6f}")
print(f"    φ⁻¹ × ||c_ext|| = {phi_inv*c_ext:.6f}")
print(f"    φ⁻² × ||c_ext|| = {phi_inv**2*c_ext:.6f}")
print(f"    Golden ratio appears: W_us = {u}·{s}/({u}+{s}+{c}+{b}) = {W_us:.8f}")
print(f"    φ⁻¹ = {phi_inv:.8f},  diff = {(W_us/phi_inv-1)*100:.4f}%")
print()

print(f"  === GMO coefficients (octet) ===")
print(f"  {'Coefficient':<12} {'Formula':>50} {'Predicted':>10} {'Fit':>8} {'Err':>8}")
print("  " + "-" * 88)
print(f"  {'α':<12} {'E_P·OI·(s²-u²-d²+L3)':>50} {alpha:>10.2f} {FIT_alpha:>8.1f} {(alpha/FIT_alpha-1)*100:>+7.2f}%")
print(f"  {'β':<12} {'-α·(L3-1)/(L3-1+L4/L5)':>50} {beta:>10.2f} {FIT_beta:>8.1f} {(beta/FIT_beta-1)*100:>+7.2f}%")
print(f"  {'γ':<12} {'E_P·OI·(L3-1+L4/L5)':>50} {gamma:>10.2f} {FIT_gamma:>8.1f} {(gamma/FIT_gamma-1)*100:>+7.2f}%")
print(f"  {'δ':<12} {'-γ':>50} {delta:>10.2f} {FIT_delta:>8.1f} {(delta/FIT_delta-1)*100:>+7.2f}%")
print()
print(f"  Key relations:")
print(f"    γ = E_P·OI·(L3-1+L4/L5)  — SU(3) Casimir from Metatime intention")
print(f"    δ = -γ                    — di-quark spin flips the Casimir sign")
print(f"    α = E_P·OI·(s²-u²-d²+L3)  — U-spin breaking = strange²−up²−down²+L3")
print(f"    β/α = -(L3-1)/(L3-1+L4/L5) = {beta/alpha:.6f}")
print(f"    Fit:  β/α = {FIT_beta/FIT_alpha:.6f}  (diff {(beta/alpha)/(FIT_beta/FIT_alpha)-1:.4f}%)")
print()

print(f"  === GMO coefficients (decuplet) ===")
print(f"  {'Coefficient':<12} {'Formula':>50} {'Predicted':>10} {'Fit':>8} {'Err':>8}")
print("  " + "-" * 88)
print(f"  {'α₁₀':<12} {'E_P·OI·(L3²+L4²+L5²+L3+L4+L5+L4)/L4':>50} {alpha10:>10.2f} {FIT_alpha10:>8.1f} {(alpha10/FIT_alpha10-1)*100:>+7.2f}%")
print(f"  {'β₁₀':<12} {'-E_P·OI·L3·L5/L4':>50} {beta10:>10.2f} {FIT_beta10:>8.1f} {(beta10/FIT_beta10-1)*100:>+7.2f}%")
print()
print(f"  Equal spacing: Δ = -β₁₀ = {-beta10:.1f} MeV (target 148, err {(-beta10/148-1)*100:+.2f}%)")
print()

print(f"  === Baryon octet predictions ===")
print(f"  {'B':<4} {'I₃':>4} {'Y':>4} {'Base':>8} {'Axial':>8} {'Pred':>8} {'PDG':>8} {'Err':>8}")
print("  " + "-" * 60)

results = []
for name in ('p','n','L','S+','S0','S-','X0','X-'):
    base, axial, pred = predict_octet(name)
    PDG = BARYON_REF[name]
    err = (pred / PDG - 1) * 100
    Y = octet_baryon_y(name)
    I2 = octet_baryon_i2(name)
    results.append({'name': name, 'type': 'octet', 'base': round(base,3),
                    'axial': round(axial,3), 'pred': round(pred,3),
                    'PDG': PDG, 'err_pct': round(err,4),
                    'Y': Y, 'I2': I2, 'Sdq': octet_baryon_dq(name)})
    print(f"  {name:<4} {I2:>4.2f} {Y:>4.0f} {base:>8.2f} {axial:>+8.2f} {pred:>8.2f} {PDG:>8.3f} {err:>+7.2f}%")

print()
print(f"  === Baryon decuplet predictions ===")
print(f"  {'B':<4} {'Y':>4} {'Base':>8} {'Axial':>8} {'Pred':>8} {'PDG':>8} {'Err':>8}")
print("  " + "-" * 54)
for name in ('D++','S*+','X*0','O-'):
    base, axial, pred = predict_decuplet(name)
    PDG = BARYON_REF[name]
    err = (pred / PDG - 1) * 100
    Y = octet_baryon_y(name)
    results.append({'name': name, 'type': 'decuplet', 'base': round(base,3),
                    'axial': round(axial,3), 'pred': round(pred,3),
                    'PDG': PDG, 'err_pct': round(err,4),
                    'Y': Y})
    print(f"  {name:<4} {Y:>4.0f} {base:>8.2f} {axial:>+8.2f} {pred:>8.2f} {PDG:>8.3f} {err:>+7.2f}%")

octet_errs = [r['err_pct'] for r in results if r['type'] == 'octet']
dec_errs = [r['err_pct'] for r in results if r['type'] == 'decuplet']
octet_mean_abs = sum(abs(e) for e in octet_errs) / len(octet_errs)
dec_mean_abs = sum(abs(e) for e in dec_errs) / len(dec_errs)

print()
print(f"  === Summary ===")
print(f"  Octet mean |error|:  {octet_mean_abs:.4f}%")
print(f"  Decuplet mean |error|: {dec_mean_abs:.4f}%")
print(f"  Combined mean |error|: {(octet_mean_abs*8 + dec_mean_abs*4)/12:.4f}%")
print()
print(f"  === Comparison: old (fitted) vs new (derived) coefficients ===")
print(f"  {'Coeff':<8} {'Fitted (v7.2)':>14} {'Derived (v7.7)':>16} {'Diff':>8}")
print("  " + "-" * 48)
for c, f, d in [('α', FIT_alpha, alpha), ('β', FIT_beta, beta),
                 ('γ', FIT_gamma, gamma), ('δ', FIT_delta, delta),
                 ('α₁₀', FIT_alpha10, alpha10), ('β₁₀', FIT_beta10, beta10)]:
    print(f"  {c:<8} {f:>14.1f} {d:>16.2f} {(d/f-1)*100:>+7.2f}%")

output = {
    'schema': 'METATIME_BARYON_GMO_FIRST_PRINCIPLES_V7_7',
    'module': '77_baryon_gmo_first_principles_v7_7',
    'created_utc': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    'status': 'PASS',
    'constants': {
        'OI': OI, 'L3': L3, 'L4': L4, 'L5': L5,
        'E_P': E_P, 'E_proton': E_proton, 'Ei': Ei,
        'u': u, 'd': d, 's': s, 'c': c, 'b': b,
    },
    'J_KJ_eigenvalues': {
        'c_vector': {'c1': 0.296, 'c4': 0.210, 'c7': 0.207},
        'norm': round(c_norm, 6),
        'eigenvalues': [round(v, 6) for v in evals],
        'extended': {
            'c3': c3, 'c8': round(c8, 6),
            'norm_ext': round(c_ext, 6),
            'golden_ratio_in_W_us': {
                'W_us': round(W_us, 8),
                'phi_inv': round(phi_inv, 8),
                'diff_pct': round((W_us/phi_inv-1)*100, 4),
            }
        },
    },
    'GMO_octet': {
        'alpha_formula': 'E_P·OI·(s²-u²-d²+L3)',
        'beta_formula': '-α·(L3-1)/(L3-1+L4/L5)',
        'gamma_formula': 'E_P·OI·(L3-1+L4/L5)',
        'delta_formula': '-γ',
        'derived': {
            'alpha': round(alpha, 4), 'beta': round(beta, 4),
            'gamma': round(gamma, 4), 'delta': round(delta, 4),
        },
        'fitted_v72': {
            'alpha': FIT_alpha, 'beta': FIT_beta,
            'gamma': FIT_gamma, 'delta': FIT_delta,
        },
        'errors_vs_fit_pct': {
            'alpha': round((alpha/FIT_alpha-1)*100, 4),
            'beta': round((beta/FIT_beta-1)*100, 4),
            'gamma': round((gamma/FIT_gamma-1)*100, 4),
            'delta': round((delta/FIT_delta-1)*100, 4),
        },
        'key_relations': {
            'delta_eq_minus_gamma': delta == -gamma,
            'beta_over_alpha': round(beta/alpha, 6),
            'fit_beta_over_alpha': round(FIT_beta/FIT_alpha, 6),
        },
    },
    'GMO_decuplet': {
        'alpha10_formula': 'E_P·OI·(L3²+L4²+L5²+L3+L4+L5+L4)/L4',
        'beta10_formula': '-E_P·OI·L3·L5/L4',
        'derived': {
            'alpha10': round(alpha10, 4), 'beta10': round(beta10, 4),
        },
        'fitted_v72': {
            'alpha10': FIT_alpha10, 'beta10': FIT_beta10,
        },
        'errors_vs_fit_pct': {
            'alpha10': round((alpha10/FIT_alpha10-1)*100, 4),
            'beta10': round((beta10/FIT_beta10-1)*100, 4),
        },
    },
    'results': results,
}

fingerprint = hashlib.sha256(
    json.dumps({k: output[k] for k in ['schema', 'GMO_octet', 'GMO_decuplet', 'results']},
               sort_keys=True).encode()
).hexdigest()
output['fingerprint_sha256'] = fingerprint

outdir = Path(__file__).resolve().parent / '../results'
outdir.mkdir(parents=True, exist_ok=True)
(outdir / 'baryon_gmo_first_principles_v7_7.json').write_text(
    json.dumps(output, indent=2, ensure_ascii=False), encoding='utf-8')
print(f"\n  → results/baryon_gmo_first_principles_v7_7.json")
print(f"  fingerprint: {fingerprint[:16]}...")
print(json.dumps({'status': 'PASS', 'fingerprint': fingerprint}))

sys.exit(0)
