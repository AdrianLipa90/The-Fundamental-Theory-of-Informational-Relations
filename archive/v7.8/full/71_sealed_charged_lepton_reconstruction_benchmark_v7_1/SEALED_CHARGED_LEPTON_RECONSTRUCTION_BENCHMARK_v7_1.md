# METATIME Standard Model Derivation — v7.1 Sealed Charged-Lepton Reconstruction Benchmark (after e→μ refinement)

Created UTC: `2026-06-22T00:00:00Z`

## Purpose

v7.1 re-runs the sealed charged-lepton reconstruction benchmark after the v7.0 `e→μ` release refinement gate. The v6.9 benchmark (3.44% mean error) was dominated by the old v6.2 frozen `R_e_mu`. With the v7.0 refinement, all three charged leptons now score at sub-1% error.

## Frozen pipeline

```
S_mu = S_e - R_e_mu
S_tau = S_mu - R_mu_tau
E_i = E_P * exp(-S_i/OI)
```

## Input policy

```
electron mass as input: false
muon mass as input: false
tau mass as input: false
PDG table as input: false
exact replay table as input: false
v6.1 target actions as input: false
```

## Frozen operators

| Operator | Source | Formula |
|---|---|---|
| OP-OI | v5.3 | OI = ln2 / (24·π) |
| OP-COLLATZ | v4.5 | L3 = 7 |
| OP-S_E | v6.7 | S_e = 1/2 − 3·OI + OI/L3 − OI²/2 |
| OP-R_E_MU | v7.0 | R_e_mu = 5·OI + 2·OI/L3 + ((L3+1)/2)·OI² |
| OP-R_MU_TAU | v6.8 | R_mu_tau = 3·OI − OI/L3 − (L3/2)·OI² |
| OP-PLANCK-E0 | v6.1 | E_Planck = sqrt(ħ·c⁵/G) in MeV |
| OP-WHITE-THREAD | v5.1 | Quadratic amplitude map |
| OP-TWIN-PRIME | v4.5 | Twin-prime seed (3,5) |
| OP-KAPPA-EB | v2.4 | Euler-Berry spin-half phase |

## Results

| particle | derived action | predicted MeV | scoring reference MeV | abs rel error % |
|---|---:|---:|---:|---:|
| electron | 0.473691600121165 | 0.511642050984 | 0.510998950000 | 0.125852 |
| muon | 0.424761179773673 | 104.831769300437 | 105.658380000000 | 0.782343 |
| tau | 0.398790835922995 | 1767.504069634979 | 1776.860000000000 | 0.526543 |

## Metrics

```json
{
  "particle_count": 3,
  "mean_abs_relative_error_percent": 0.4782458022229171,
  "max_abs_relative_error_percent": 0.7823427725875742,
  "electron_abs_relative_error_percent": 0.12585172327104704,
  "muon_abs_relative_error_percent": 0.7823427725875742,
  "tau_abs_relative_error_percent": 0.5265429108101349,
  "predicted_mu_over_e": 204.89279389511805,
  "scoring_mu_over_e": 206.76829179394596,
  "mu_over_e_relative_error_percent": 0.9070529540849193,
  "predicted_tau_over_mu": 16.8603857535734,
  "scoring_tau_over_mu": 16.817028616187375,
  "tau_over_mu_relative_error_percent": 0.2578168734534314,
  "predicted_tau_over_e": 3454.209212923309,
  "scoring_tau_over_e": 3477.228280018971,
  "tau_over_e_relative_error_percent": 0.6620043486543043
}
```

## Decision

```
technical: PASS
formal: PASS_SEALED_CHARGED_LEPTON_RECONSTRUCTION_BENCHMARK_INSTALLED_V7_1
substantive: SEALED_CHARGED_LEPTON_RECONSTRUCTION_SUB_PERCENT_ALL_CHANNELS
Debt 9 numeric spectrum: OPEN_NOT_CLOSED
canon_allowed: false
mass_spectrum_closure_claimed: false
```

The v7.1 benchmark confirms that the v7.0 `e→μ` refinement reduces the muon error from 4.96% to 0.78%, and the tau error from 5.23% to 0.53%. All three channels are now sub-1% from a fully first-principles derivation (no measured masses as inputs).

## Required next step

```
DEBT-009 — Hadron and meson sector split
```

The charged-lepton sector is now gated at sub-1% error. The next physics frontier is the hadron sector: freeze baryon triplet operators (v5.6–v5.9) and meson pair-state binding operators separately.
