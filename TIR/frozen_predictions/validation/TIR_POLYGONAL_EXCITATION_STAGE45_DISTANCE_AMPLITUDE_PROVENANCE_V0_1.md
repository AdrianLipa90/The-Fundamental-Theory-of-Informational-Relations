# TIR Polygonal Excitation — Stage 45 Distance-to-Amplitude Provenance Gate v0.1

Status: `STAGE_45_CANONICAL_DISTANCE_TO_AMPLITUDE_MAP_NOT_FOUND__PROVENANCE_NOGO_PASS`

## Scope

Stage 44 produced an exact, parameter-free Collatz orbit-intersection distance matrix for the three frozen family seeds. Stage 45 asks whether the existing TIR record already contains a canonical rule that converts such a path distance or cost into an amplitude.

No CKM entries or masses are used in this audit. No new kernel is introduced.

## v5.0 derivability audit

The archived v5.0 White-Thread audit records the available formal structure as

```text
W_ij = exp(i integral A)
```

for an open-path phase holonomy and a bounded but explicitly underived amplitude function

```text
Omega_ij = Omega0 f(|W_ij|, Delta arg W_ij, ...).
```

Its substantive verdict is

`NO_GO_FOR_STRONG_CHARGED_LEPTON_F_PROMOTION`.

The v5.0 record explicitly refuses to identify an undefined amplitude map with a derived operator.

## v5.1 candidate

The later v5.1 module proposes

```math
S_{ij}
=\frac{(\Delta\tau_{v2})^2}{2L_3\Delta G},
```

```math
F_{ij}=e^{-\kappa S_{ij}}.
```

Its own source marks this as a candidate constructed after the v5.0 derivability audit. The recorded substantive status is

`PARTIAL_DERIVATION_CANDIDATE_ROOT_GATES_PASS_ALLPAIR_FAIL`,

with

```text
canon_allowed = False
current_promotion = DENY_CURRENT.
```

Thus v5.1 is evidence that an exponential open-path action has been explored inside TIR, but it is not a canonical general distance-to-amplitude law.

## Consequence for Stage 44

The Stage 44 matrix

```math
D_C=
\begin{pmatrix}
0&4&88\\
4&0&90\\
88&90&0
\end{pmatrix}
```

cannot be inserted into the v5.1 denominator or exponent and presented as an already derived TIR rule. Such a substitution would create a new hypothesis.

Likewise, the following maps are not promoted by this stage:

```math
1/d_{ij},
\qquad
e^{-d_{ij}},
\qquad
e^{-\kappa d_{ij}}.
```

## Verdict

```text
phase-holonomy rule: PRESENT
canonical distance/path-cost -> amplitude rule: NOT FOUND
v5.1 exponential map: NON-CANON CANDIDATE WITH ALL-PAIR FAILURE
Stage 44 distance substitution into v5.1: NEW HYPOTHESIS, NOT EXISTING LAW
```

This is a provenance no-go result, not a failure of the Stage 44 integer geometry.

## Methodological consequence

Any use of the Collatz distance matrix as a family coupling must first be frozen as a separate candidate kernel before any quantitative CKM comparison. Multiple mathematically natural kernels may be frozen in parallel, but none may be selected retrospectively by best fit.

## Reproducibility

Executable provenance audit:

`TIR/frozen_predictions/validation/scripts/distance_amplitude_provenance_stage45_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE45_DISTANCE_AMPLITUDE_PROVENANCE_RECEIPT_V0_1.json`

## Next gate

Before freezing a kernel, audit whether the exact Stage 44 integer distances possess independently meaningful arithmetic relations to the already frozen structural constants. Such identities may constrain the admissible normalization or show that the distance hierarchy is already encoded by the same discrete geometry. Any arithmetic relation discovered at this point is retrospective and must be labelled accordingly.
