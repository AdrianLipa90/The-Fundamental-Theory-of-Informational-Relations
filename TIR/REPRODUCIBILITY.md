# Reproducibility Guide — reviewed 2026-08-07 state

This repository has several reproducibility layers.  They answer different
questions and their PASS states must not be conflated.

## 1. Selected legacy formula reproducibility

Run:

```text
python3 TIR/run_audit.py --json
```

This checks nine selected legacy observables against their frozen engineering
tolerances and reports schema
`TIR_SELECTED_LEGACY_REPRODUCIBILITY_V11_1`.

A PASS here means only that the selected historical implementation remains
reproducible.  It is **not** a physical PASS for TIR, not a proof that every
observable is derived, and not a statistically meaningful global accuracy
score.

The underlying historical ledger remains in `TIR/metatime_audit.py`.

## 2. Exact κ phase-rate audit

Run:

```text
python3 TIR/validation/kappa_phase_rate_identity_v11_1.py
```

The primary certificate is symbolic at the factor/exponent level:

\[
\frac1{24}(\ln2)\pi^{-1}\times2\pi f
=\frac1{12}(\ln2)f.
\]

It checks exact cancellation of the powers of \(\pi\), the rational prefactor
\(1/12\), representative numerical implementations, and the rank-three
constraint certificate for
\((\kappa,\omega,f,\Gamma_{\mathcal I})\).

Claim boundary:
- `κ = ln2/(24π)` is a TIR structural definition/model postulate;
- `ω = 2πf` is a standard definition;
- `Γ_I = κω = (ln2/12)f` is exact conditional on the stated definitions;
- physical identification of `Γ_I` as a surface-refresh observable remains open.

## 3. Reviewed source contract

Run:

```text
python3 TIR/validation/review_source_contract_v11_1.py
```

The contract checks that the live sources still contain:
- exactly one κ phase-rate section and one constraint-manifold section;
- the corrected spin-1/2 Berry-phase normalization;
- Appendix P and the TIR ↔ Secret-of-a-Half interface;
- the negative theorem that reciprocal self-duality alone does not imply a
  dynamical extremum;
- the reviewed source-code/reproducibility appendix;
- the explicit technical-vs-physical boundary of the legacy runner.

## 4. Publication source preparation

The reviewed source order is:

```text
normalize_build_sources.py
→ prepare_publication_candidate_v11_0.py
→ apply_kappa_phase_rate_patch.py
→ apply_metatime_paper_review_patch.py
→ exact validators
→ citation audit
→ LaTeX compilation
→ publication preflight
```

The post-generation patches are intentional.  The v11.0 generator is retained
as a historical deterministic transform, while the 7 August review is applied
idempotently afterwards.

## 5. Full publication validation

The authoritative sequence is maintained by:

`.github/workflows/compile-metatime-monograph.yml`

It validates the exact pull-request head, compiles both:
- `TIR/monograph/metatime_monograph.pdf`;
- `TIR/metatime_paper.pdf`;

and checks citation/reference integrity, metadata, embedded fonts, `qpdf`
integrity, retained physical failures, exact κ receipts and source-contract
receipts.

Do not infer PASS for a new commit from an older successful workflow run.  The
workflow result must correspond to the exact reviewed head.

## Requirements

For the legacy selected audit, Python's standard library is sufficient for the
runner itself and the historical `metatime_audit.py` path it imports.

The publication and wider validation environment additionally requires the
Python and LaTeX dependencies declared by the corresponding scripts/workflow.
The GitHub workflow is the source of truth for the publication toolchain.

## Reviewer checklist

1. Run `TIR/run_audit.py --json` and inspect the **claim boundary**, not only the
   PASS/FAIL field.
2. Run `TIR/validation/kappa_phase_rate_identity_v11_1.py` and verify the exact
   factor certificate reports `pi_cancelled_exactly: true` and prefactor
   `[1,12]`.
3. Run `TIR/validation/review_source_contract_v11_1.py`.
4. Read `TIR/STRUCTURAL_CHOICES.md` and the v11 publication protocol before
   interpreting parameter-count statements.
5. Inspect the retained physical failures, especially the active neutron-EDM
   result and gauge-boson tension.
6. Read `TIR/docs/cross_reviews/TIR_SECRET_HALF_2026-08-07.md` before using the
   half formalism in a TIR derivation; the arrows in the cross-relation have
   different logical types.
