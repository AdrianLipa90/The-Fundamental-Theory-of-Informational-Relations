# Metatime Monograph Status — v11.1 review

**Review date:** 7 August 2026  
**Live review branch:** `agent/kappa-phase-refresh-identity-v0.1`  
**Pull request:** #80  
**Promotion:** review-only; not merged to `main`

This file describes the current reviewed monograph sources. Historical v9/v10
page counts, ZIP names and aggregate accuracy claims remain repository
provenance; they are not the current publication status.

## Live publication sources

The review compiles two documents:

- `TIR/monograph/metatime_monograph.tex` — long publication candidate;
- `TIR/metatime_paper.tex` — short Metatime paper.

The authoritative build, preflight and artifact generation are defined in
`.github/workflows/compile-metatime-monograph.yml`.  Page count and artifact
hashes are build outputs and are not hard-coded here; a validation PASS applies
only to the exact commit tested by that workflow.

## 7 August review additions

### Exact conditional κ phase-rate closure

TIR defines

\[
\kappa=\frac{\ln2}{24\pi},
\qquad
d\mathcal I=\kappa\,d\phi,
\]

and standard angular-frequency notation gives

\[
\omega=\frac{d\phi}{dt}=2\pi f.
\]

Therefore

\[
\boxed{
\Gamma_{\mathcal I}
=\frac{d\mathcal I}{dt}
=\kappa\omega
=\frac{\ln2}{12}f
},
\qquad
\boxed{
\Delta\mathcal I_{\rm cycle}=\frac{\ln2}{12}
}.
\]

This identity is algebraically exact conditional on the TIR definitions.  The
normalization \(\kappa=\ln2/(24\pi)\) remains a TIR structural definition/model
postulate, and a physical surface-refresh interpretation remains operationally
open.

### Constraint manifold

The four named quantities
\((\kappa,\omega,f,\Gamma_{\mathcal I})\) satisfy three independent
constraints.  The corresponding Jacobian has rank three, so the declared
subsystem has one continuous degree of freedom and may be parametrized by \(f\):

\[
\mathbf q(f)=
\left(
\frac{\ln2}{24\pi},
2\pi f,
f,
\frac{\ln2}{12}f
\right).
\]

### Corrected Berry normalization

The live reviewed text uses

\[
\gamma=-\frac{\Omega}{2}\pmod{2\pi}.
\]

A hemisphere solid angle gives phase magnitude \(\pi\); a full-sphere solid
angle \(4\pi\) gives magnitude \(2\pi\), trivial modulo \(2\pi\).  The older
`4π/2 = π` statement is not part of the reviewed source.

### TIR ↔ Secret-of-a-Half interface

Appendix P and the cross-review record separate the logical types in

\[
\frac12
\xrightarrow{\;H_2\;}
\ln2
\xrightarrow{\;\text{TIR definition}\;}
\kappa
\xrightarrow{\;d\mathcal I=\kappa d\phi\;}
\Gamma_{\mathcal I}.
\]

The exact half-side entropy theorem does not derive the TIR denominator
\(24\pi\).  The exact downstream phase-rate identity does not establish its
physical interpretation.

The sibling DHSE-001 Stage-M theorem also supplies the exact finite boundary

\[
\boxed{
\text{reciprocal self-duality}
\not\Rightarrow
\text{dynamical maximum at the self-dual point}
}.
\]

Any TIR use of self-duality as a stability or attractor argument therefore needs
an additional theorem or condition.

## Evidence architecture

The current monograph distinguishes:

- established mathematics and external data;
- TIR model definitions/postulates;
- exact consequences conditional on those definitions;
- retrospective phenomenological assignments;
- diagnostics, no-go results and retained failures;
- prospectively frozen predictions;
- external anchors and conversion inputs.

The old statement “mean error across all 26 SM parameters” is withdrawn.  The
publication does not combine heterogeneous observables, anchors, upper limits,
running quantities and retrospective assignments into one global percentage.

## Retained physical tensions

The publication record keeps failures visible, including:

- active gauge-boson relations at several-percent tension;
- the frozen strong-CP→neutron-EDM mapping
  \[
  d_n\approx5.3299\times10^{-26}\,e\,\mathrm{cm},
  \]
  approximately \(2.96\) times the
  \(1.8\times10^{-26}\,e\,\mathrm{cm}\) manuscript bound;
- the isolated Collatz quarter-power mass trace as an incomplete retrospective
  diagnostic rather than a closed spectrum derivation.

A technically correct calculation may therefore be a physical FAIL.

## Reproducibility layers

- `TIR/run_audit.py --json` — selected legacy reproducibility subset; not a
  global physical validation.
- `TIR/validation/kappa_phase_rate_identity_v11_1.py` — exact symbolic factor
  certificate plus numerical implementation checks and rank certificate.
- `TIR/validation/review_source_contract_v11_1.py` — protects the reviewed live
  source topology and claim boundaries.
- `TIR/monograph/apply_kappa_phase_rate_patch.py` — restores reviewed κ material
  after the retained v11.0 source generator.
- `TIR/apply_metatime_paper_review_patch.py` — synchronizes the short paper.

## Current gate

A review commit is publication-ready only when the exact-head workflow completes
successfully after that commit.  No older PDF hash, page count or workflow PASS
is inherited automatically by a later head.
