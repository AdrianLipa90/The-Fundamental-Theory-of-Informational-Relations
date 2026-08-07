# Reviewer Orientation — Metatime/TIR

## What this repository is

Metatime/TIR is an **exploratory low-parameter phenomenological programme**, not
a completed first-principles derivation of the Standard Model.

The current reviewed structural layer uses:
- \(\kappa=\ln2/(24\pi)\) — TIR structural definition/model postulate;
- \((L_3,L_4,L_5)=(7,2,5)\) — discrete L-constants;
- prime-valued flavour labels \((u,d,s,c,b,t)=(3,5,7,11,13,17)\);
- declared external anchors and conversion inputs documented by the v11
  publication protocol.

The 7 August 2026 review adds the exact conditional phase-rate identity

\[
\boxed{
\Gamma_{\mathcal I}=\kappa\omega=\frac{\ln2}{12}f
},
\qquad \omega=2\pi f,
\]

and the corresponding one-dimensional constraint manifold for
\((\kappa,\omega,f,\Gamma_{\mathcal I})\).  This does not turn the TIR
normalization into an established standard-physics derivation and does not by
itself establish a physical surface-refresh observable.

## Start with the evidence classes

Before reading numerical matches, distinguish:

1. **established external mathematics/physics**;
2. **TIR structural definitions and postulates**;
3. **exact consequences conditional on those definitions**;
4. **retrospective phenomenological assignments**;
5. **prospectively frozen predictions**;
6. **technical implementation PASS/FAIL**;
7. **physical empirical PASS/FAIL**;
8. **open bridges and derivational debt**.

The publication protocol and claim ledgers are designed to prevent movement
between these classes without explicit evidence.

## Quick reproducibility checks

```text
python3 TIR/run_audit.py --json
python3 TIR/validation/kappa_phase_rate_identity_v11_1.py
python3 TIR/validation/review_source_contract_v11_1.py
```

The first command is a **selected legacy reproducibility subset**, not a global
physical validation.  The second certifies the κ phase-rate algebra, including
exact \(\pi\)-factor cancellation.  The third protects the reviewed publication
source topology and claim boundaries.

For the full publication build, use the exact sequence maintained by
`.github/workflows/compile-metatime-monograph.yml` rather than a copied command
transcript.

## Repository map for review

```text
TIR/
├── metatime_audit.py
├── run_audit.py
├── metatime_paper.tex
├── apply_metatime_paper_review_patch.py
├── REPRODUCIBILITY.md
├── STRUCTURAL_CHOICES.md
├── CLAIM_HIERARCHY.md
├── FALSIFIABILITY.md
├── CURRENT_STATUS.md
├── docs/
│   └── cross_reviews/
│       └── TIR_SECRET_HALF_2026-08-07.md
├── validation/
│   ├── kappa_phase_rate_identity_v11_1.py
│   └── review_source_contract_v11_1.py
└── monograph/
    ├── metatime_monograph.tex
    ├── appendices/
    │   ├── appA_kappa_derivation.tex
    │   ├── appI_source_code.tex
    │   ├── appO_publication_protocol.tex
    │   └── appP_secret_half_cross_relation.tex
    └── chapters/

archive/
└── historical releases, snapshots and audit material
```

Archive copies are historical provenance.  Review current live sources before
using an old archived claim as the present TIR position.

## Highest-value review targets

1. **κ normalization.** Verify that the numerator \(\ln2\), the discrete
   denominator choice \(24\pi\), and the exact downstream phase-rate consequence
   are not conflated into one first-principles theorem.
2. **Berry phase.** The reviewed text correctly uses
   \(\gamma=-\Omega/2\pmod{2\pi}\): hemisphere solid angle gives phase magnitude
   \(\pi\); full sphere gives \(2\pi\), trivial modulo \(2\pi\).
3. **TIR ↔ Secret-of-a-Half interface.** Read
   `docs/cross_reviews/TIR_SECRET_HALF_2026-08-07.md` and Appendix P.  The exact
   chain \(1/2\to\ln2\to\kappa\to\Gamma_{\mathcal I}\) contains arrows of
   different epistemic type and must not be used circularly.
4. **Self-duality boundary.** DHSE-001 Stage M gives an exact finite
   counterexample to the inference that reciprocal symmetry alone forces a
   dynamical maximum at the fixed point.
5. **Physical failures.** The active gauge-boson relations remain at several
   percent tension.  The current publication snapshot retains the neutron-EDM
   physical FAIL: approximately
   \(5.3299\times10^{-26}\,e\,\mathrm{cm}\), about \(2.96\) times the
   \(1.8\times10^{-26}\,e\,\mathrm{cm}\) bound used by the manuscript.
6. **Prospective evidence.** Check that frozen candidates and observables are not
   modified after target data are inspected.
7. **Model complexity.** “No continuously fitted coefficient” is not the same
   statement as “zero model complexity”; discrete structural choices and external
   anchors remain explicit.

## What this is NOT

- not a peer-reviewed confirmation of a final physical theory;
- not a proof that every Standard Model observable is independently derived;
- not a zero-complexity theory;
- not a licence to replace physical FAIL with technical PASS;
- not a proof that the TIR surface-refresh interpretation is physically real;
- not a proof of the Riemann Hypothesis through the Secret-of-a-Half interface.

## Publication state

The v11.0 publication candidate established the baseline claim/evidence
architecture.  The 7 August review extends it with the κ phase-rate closure,
corrected Berry normalization, exact source contracts, the reviewed short paper,
and the TIR ↔ Secret-of-a-Half appendix.

A successful workflow run is valid only for the exact commit it tested.  Do not
transfer a previous PASS to a later untested head.
