# v7.0 — e→μ Release Refinement Gate

## Status

- technical: PASS
- formal: PASS_E_MU_RELEASE_REFINEMENT_GATE_INSTALLED
- substantive: E_MU_RELEASE_REFINED_DERIVATION_GATE_PASS_NOT_CANON
- canon_allowed: false
- mass_spectrum_closure_claimed: false

## Purpose

This module closes the active e→μ release-refinement debt as a derivation gate. It does not claim full spectrum canon.
The rule is frozen before scoring and does not use the electron, muon, or tau measured masses as derivation inputs.

## Frozen formula

```text
R_e_mu = 5*OI + 2*OI/L3 + ((L3+1)/2)*OI^2
```

Components:

- `5*OI`: five-step generation bridge in the information-preference ladder.
- `2*OI/L3`: twin-prime / return-axis correction at base `L3=7`.
- `((L3+1)/2)*OI^2`: White Thread quadratic amplitude correction with spin-half weighted L3+1 sector count.

## Derived release

```text
OI = 0.009193150006360484
L3 = 7
R_e_mu = 0.048930420347491774
mu/e predicted ratio = 204.892793895118
```

## Scoring-only comparison after freeze

```text
target mu/e ratio = 206.768291793946
energy-ratio relative error = -0.907053%
action relative error = -0.170904%
```

## Charged-lepton reconstruction after replacing old e→μ gate

| particle | predicted MeV | reference MeV (scoring only) | relative error |
|---|---:|---:|---:|
| electron | 0.511642050984 | 0.510998950000 | 0.125852% |
| muon | 104.831769300437 | 105.658380000000 | -0.782343% |
| tau | 1767.504069634979 | 1776.860000000000 | -0.526543% |


Aggregate metrics:

```text
mean_abs_relative_error = 0.478246%
max_abs_relative_error = 0.782343%
tau/mu ratio error = 0.257817%
tau/e ratio error = -0.651575%
```

## Boundary

This is a gate result, not a canon claim. The correct next step is a sealed charged-lepton reconstruction benchmark using the v7.0 e→μ release.
