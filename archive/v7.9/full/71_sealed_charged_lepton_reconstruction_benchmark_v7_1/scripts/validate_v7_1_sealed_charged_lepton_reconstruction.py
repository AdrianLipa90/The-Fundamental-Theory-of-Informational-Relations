#!/usr/bin/env python3
"""v7.1 Sealed charged-lepton reconstruction benchmark — validation script.

Derives all predicted masses from the frozen operator pipeline ONLY.
No measured masses are used as inputs (scoring-only at the end).

Frozen pipeline:
  1. OI = ln(2) / (24·π)                                   [OP-OI, v5.3]
  2. L3 = 7                                                  [OP-COLLATZ, v4.5]
  3. S_e  = 1/2 - 3·OI + OI/L3 - OI²/2                      [OP-S_E, v6.7]
  4. R_em = 5·OI + 2·OI/L3 + ((L3+1)/2)·OI²                 [OP-R_E_MU, v7.0]
  5. R_mt = 3·OI - OI/L3 - (L3/2)·OI²                       [OP-R_MU_TAU, v6.8]
  6. E_P  = sqrt(ħ·c⁵/G) in MeV                              [OP-PLANCK-E0, v6.1]
  7. S_μ  = S_e - R_em
  8. S_τ  = S_μ - R_mt
  9. E_i  = E_P · exp(-S_i / OI)

Output: predicted MeV, relative errors vs scoring references.
"""

import math
import json

# ── Step 1-2: Fundamental constants ──────────────────────────────────────────
OI = math.log(2.0) / (24.0 * math.pi)
L3 = 7.0

print("=== Step 1: OI (Information Operator) ===")
print(f"  OI = ln(2) / (24·π) = {OI:.15f}")
assert abs(OI - 0.009193150006360484) < 1e-15, f"OI mismatch: {OI}"

print("\n=== Step 2: L3 (Collatz base channel) ===")
print(f"  L3 = {L3}")
assert L3 == 7.0

# ── Step 3: Electron action S_e ──────────────────────────────────────────────
print("\n=== Step 3: S_e (electron action, v6.7) ===")
S_e = 0.5 - 3.0*OI + OI/L3 - OI*OI/2.0
print(f"  S_e = 1/2 − 3·OI + OI/L3 − OI²/2")
print(f"      = {0.5} − {3.0*OI:.15f} + {OI/L3:.15f} − {OI*OI/2.0:.15f}")
print(f"      = {S_e:.15f}")
assert abs(S_e - 0.47369160012116457) < 1e-14, f"S_e mismatch: {S_e}"

# ── Step 4: e→μ release R_em ─────────────────────────────────────────────────
print("\n=== Step 4: R_em (e→μ release, v7.0) ===")
R_em = 5.0*OI + 2.0*OI/L3 + ((L3 + 1.0)/2.0) * OI*OI
term1 = 5.0*OI
term2 = 2.0*OI/L3
term3 = ((L3 + 1.0)/2.0) * OI*OI
print(f"  R_em = 5·OI + 2·OI/L3 + ((L3+1)/2)·OI²")
print(f"       = {term1:.15f} + {term2:.15f} + {term3:.15f}")
print(f"       = {R_em:.15f}")
assert abs(R_em - 0.048930420347491774) < 1e-14, f"R_em mismatch: {R_em}"

# ── Step 5: μ→τ release R_mt ─────────────────────────────────────────────────
print("\n=== Step 5: R_mt (μ→τ release, v6.8) ===")
R_mt = 3.0*OI - OI/L3 - (L3/2.0) * OI*OI
term1 = 3.0*OI
term2 = OI/L3
term3 = (L3/2.0) * OI*OI
print(f"  R_mt = 3·OI − OI/L3 − (L3/2)·OI²")
print(f"       = {term1:.15f} − {term2:.15f} − {term3:.15f}")
print(f"       = {R_mt:.15f}")
assert abs(R_mt - 0.025970343850677605) < 1e-14, f"R_mt mismatch: {R_mt}"

# ── Step 6: Planck energy E0 ─────────────────────────────────────────────────
print("\n=== Step 6: Planck energy E_P (v6.1) ===")
h = 6.62607015e-34       # J·s (exact, SI redefinition)
hbar = h / (2.0 * math.pi)  # J·s
c = 299792458.0          # m/s (exact)
G = 6.67430e-11          # m³·kg⁻¹·s⁻² (measured)
eV_J = 1.602176634e-19   # J/eV (exact, SI redefinition)
E_planck_J = math.sqrt(hbar * c**5 / G)
E_planck_eV = E_planck_J / eV_J
E_planck_MeV = E_planck_eV / 1.0e6
print(f"  E_P = sqrt(ħ·c⁵/G)")
print(f"       = {E_planck_J:.6f} J")
print(f"       = {E_planck_eV:.4e} eV")
print(f"       = {E_planck_MeV:.4e} MeV")
assert abs(E_planck_MeV - 1.2208901285838957e22) / 1.2208901285838957e22 < 1e-12

# ── Step 7-8: Derived actions ─────────────────────────────────────────────────
S_mu = S_e - R_em
S_tau = S_mu - R_mt
print(f"\n=== Step 7-8: Derived actions ===")
print(f"  S_μ = S_e − R_em = {S_e:.15f} − {R_em:.15f} = {S_mu:.15f}")
print(f"  S_τ = S_μ − R_mt = {S_mu:.15f} − {R_mt:.15f} = {S_tau:.15f}")

# ── Step 9: Predicted masses ─────────────────────────────────────────────────
print(f"\n=== Step 9: Predicted masses E_i = E_P · exp(-S_i / OI) ===")

E_e = E_planck_MeV * math.exp(-S_e / OI)
E_mu = E_planck_MeV * math.exp(-S_mu / OI)
E_tau = E_planck_MeV * math.exp(-S_tau / OI)
print(f"  E_e  = E_P · exp(-S_e/OI)  = {E_e:.6f} MeV")
print(f"  E_μ  = E_P · exp(-S_μ/OI)  = {E_mu:.6f} MeV")
print(f"  E_τ  = E_P · exp(-S_τ/OI)  = {E_tau:.6f} MeV")

# ── Scoring (references measured masses, NOT used as derivation inputs) ──────
print(f"\n=== Scoring (references — not inputs) ===")
ref = {"electron": 0.51099895, "muon": 105.65838, "tau": 1776.86}
pred = {"electron": E_e, "muon": E_mu, "tau": E_tau}

for p in ["electron", "muon", "tau"]:
    err = (pred[p] - ref[p]) / ref[p]
    print(f"  {p:>8}: predicted {pred[p]:>12.6f} MeV, reference {ref[p]:>10.6f} MeV, error {err:+.6f} ({abs(err)*100:.4f}%)")

errors = [abs(pred[p] - ref[p]) / ref[p] for p in ["electron", "muon", "tau"]]
mean_abs_err = sum(errors) / 3
print(f"\n  Mean absolute relative error: {mean_abs_err*100:.4f}%")
print(f"  Max absolute relative error:  {max(errors)*100:.4f}%")

# ── Assertions ────────────────────────────────────────────────────────────────
print(f"\n=== Assertions ===")
assert abs(E_e - 0.5116420509844719) < 1e-10, f"E_e mismatch: {E_e}"
assert abs(E_mu - 104.83176930043687) / 104.83176930043687 < 1e-10, f"E_mu mismatch: {E_mu}"
assert abs(E_tau - 1767.504069634979) / 1767.504069634979 < 1e-10, f"E_tau mismatch: {E_tau}"
assert mean_abs_err < 0.005, f"Mean abs error too high: {mean_abs_err}"
print("  ALL ASSERTIONS PASS")

# ── Summary JSON ──────────────────────────────────────────────────────────────
summary = {
    "schema": "METATIME_V7_1_DERIVATION_STEP_BY_STEP",
    "derivation_steps": [
        {"step": 1, "symbol": "OI", "formula": "ln(2)/(24·π)", "value": OI},
        {"step": 2, "symbol": "L3", "formula": "Collatz(3→5→...→1)", "value": L3},
        {"step": 3, "symbol": "S_e", "formula": "1/2 − 3·OI + OI/L3 − OI²/2", "value": S_e},
        {"step": 4, "symbol": "R_em", "formula": "5·OI + 2·OI/L3 + ((L3+1)/2)·OI²", "value": R_em},
        {"step": 5, "symbol": "R_mt", "formula": "3·OI − OI/L3 − (L3/2)·OI²", "value": R_mt},
        {"step": 6, "symbol": "E_P", "formula": "sqrt(ħ·c⁵/G)", "value_MeV": E_planck_MeV},
        {"step": 7, "symbol": "S_μ", "formula": "S_e − R_em", "value": S_mu},
        {"step": 8, "symbol": "S_τ", "formula": "S_μ − R_mt", "value": S_tau},
        {"step": 9, "symbol": "E_i", "formula": "E_P·exp(-S_i/OI)", "value_MeV": {"e": E_e, "μ": E_mu, "τ": E_tau}},
    ],
    "results": [
        {"particle": "electron", "predicted_mev": E_e, "reference_mev": ref["electron"], "rel_error": errors[0]},
        {"particle": "muon", "predicted_mev": E_mu, "reference_mev": ref["muon"], "rel_error": errors[1]},
        {"particle": "tau", "predicted_mev": E_tau, "reference_mev": ref["tau"], "rel_error": errors[2]},
    ],
    "metrics": {
        "mean_abs_relative_error": mean_abs_err,
        "max_abs_relative_error": max(errors),
        "particle_count": 3,
    },
    "official_status": {
        "technical": "PASS",
        "formal": "PASS_SEALED_CHARGED_LEPTON_RECONSTRUCTION_BENCHMARK_INSTALLED_V7_1",
        "canon": "DENIED",
    }
}

import sys
if "--json" in sys.argv:
    print(f"\n=== JSON OUTPUT ===")
    print(json.dumps(summary, indent=2))
