# Reproducibility Guide — v12 synchronization

TIR uses separate reproducibility layers for structural derivations, numerical implementations, historical formula snapshots, empirical comparison, and publication assembly. A `PASS` is scoped to the exact layer and revision named by its receipt.

## 1. Legacy formula reproducibility

```text
python3 TIR/run_audit.py --json
```

This retains the selected historical implementation subset under schema `TIR_SELECTED_LEGACY_REPRODUCIBILITY_V11_1`. Its result certifies reproducibility of that frozen subset.

## 2. Canonical κ structural derivation

Canonical theorem surface:

```text
TIR/foundations/TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md
```

Validator:

```text
python3 TIR/validation/tir_kappa_flavour_mixing_normalization_v0_1.py
```

The structural chain is

\[
V_F\cong\mathbb C^3,
\qquad
\dim\mathfrak{su}(3)_F=8,
\qquad
N_{\rm mix}=3\times8=24,
\]

\[
\Delta\phi_{1/2}=\pi,
\qquad
\Phi_{\rm mix}=24\pi,
\qquad
H_2(1/2)=\ln2,
\]

hence

\[
\boxed{\kappa=\frac{\ln2}{24\pi}}.
\]

The validator checks the three-flavour multiplicity, Lie-algebra dimension, 24-channel incidence count, half-turn phase, total \(24\pi\) measure, and the independent tetrahedral-order crosscheck. Its classification is `TIR_INTERNAL_DERIVED_NORMALIZATION_FROM_FLAVOUR_MIXING_GEOMETRY`.

## 3. κ phase-rate audit

```text
python3 TIR/validation/kappa_phase_rate_identity_v11_1.py
```

Conditional on the canonical normalization and the declared information-phase relation,

\[
\frac1{24}(\ln2)\pi^{-1}\times2\pi f
=\frac1{12}(\ln2)f,
\]

so

\[
\boxed{\Gamma_{\mathcal I}=\kappa\omega=\frac{\ln2}{12}f}.
\]

This audit checks exact \(\pi\)-factor cancellation, the rational prefactor \(1/12\), representative numerical implementations, and the rank-three constraint certificate for \((\kappa,\omega,f,\Gamma_{\mathcal I})\). Operational calibration of a physical \(\Gamma_{\mathcal I}\) observable remains an `OPEN` evidence gate.

## 4. v12 discrete-label audit

The v12 migration validates the finite Collatz orbit used for \(L_3\) and exhaustively checks all \(6!=720\) quark-prime permutations. The arithmetic constraints leave two candidates related by \(b\leftrightarrow t\); the typed monotone flavour-order rule selects the canonical assignment uniquely.

Use the v12 discrete-label validator and its receipt under `TIR/validation/` when reviewing Chapter 10.

## 5. v12 coefficient-forcing audit

```text
python3 TIR/validation/tir_coefficient_role_orientation_forcing_v0_1.py
```

The validator certifies the role-slot bijection, identity as the unique role-preserving slot permutation, gradient-sign scale independence, runtime deadband behaviour, and consensus-orientation uniqueness. The active completion gate is extraction of the four typed integer magnitudes \(|h|,|a|,|b|,|c|\).

## 6. v12 flavour-sector diagnostics

Chapter 12 carries a dedicated diagnostic receipt for the legacy neutrino absolute-action formula/value mismatch. Chapter 13 carries a flavour-mixing audit that preserves the PMNS reactor-angle tension and the historical CKM \(J\)-proxy residual as diagnostics.

These diagnostics are evidence inputs to Chapter 19 rather than independent current-status owners.

## 7. Unified Evidence Matrix audit

```text
python3 TIR/validation/tir_v12_evidence_matrix_consistency_v0_1.py
```

The current publication owner for observable verdicts is

```text
TIR/monograph/v12/chapters/ch19_unified_evidence_matrix.tex
```

The audit checks the allowed Claim Class, Timing and Verdict vocabularies, unique row identities, retention of the charged-lepton precision failures, PMNS \(\theta_{13}\) tension, neutron-EDM failure, and v12 formula quarantines.

Receipt:

```text
TIR/validation/TIR_V12_EVIDENCE_MATRIX_CONSISTENCY_V0_1.json
```

## 8. Historical source contract

```text
python3 TIR/validation/review_source_contract_v11_1.py
```

This remains the source-contract audit for the reviewed v11 publication topology. Version 12 preserves those sources as provenance while compiling through `TIR/monograph/tir_monograph_v12.tex`.

## 9. Publication validation

The v11 authoritative sequence remains maintained by `.github/workflows/compile-metatime-monograph.yml`. Version 12 requires an exact-head build and its own source/claim audits before publication promotion. Workflow evidence attaches only to the commit it tested.

## Reviewer checklist

1. Run the canonical κ flavour-mixing validator.
2. Run the κ phase-rate validator.
3. Run the discrete-label and coefficient-forcing validators.
4. Run the v12 neutrino/flavour diagnostics.
5. Run `tir_v12_evidence_matrix_consistency_v0_1.py` and inspect the full status triples.
6. Inspect retained `FAIL`, `TENSION`, `OPEN`, and `QUARANTINED` rows in Chapter 19.
7. Compile `TIR/monograph/tir_monograph_v12.tex` twice and run the exact-head publication preflight before promotion.
