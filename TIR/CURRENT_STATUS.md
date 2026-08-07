# CURRENT STATUS — Metatime/TIR

**Review line:** v11.1-review  
**Review date:** 2026-08-07  
**Author:** Adrian Lipa  
**Branch:** `agent/kappa-phase-refresh-identity-v0.1`  
**Pull request:** #80 — `Review κ phase-rate closure and Metatime normalization`  
**Promotion:** review-only; not merged to `main`

This file describes the **live reviewed source state**.  Historical v7–v10
status reports and reviewer-era formula ledgers remain provenance in `archive/`
and must not be used as the current claim ledger without checking the live v11
publication sources.

## 1. Current scientific classification

Metatime/TIR is an **exploratory low-parameter phenomenological programme**.
It is not currently claimed as:

- an experimentally established replacement for the Standard Model;
- a complete first-principles derivation of all Standard Model observables;
- a zero-complexity theory;
- a proof that a proposed physical surface-refresh process exists;
- a proof of the Riemann Hypothesis through the Secret-of-a-Half interface.

The v11 publication architecture separates established results, model
postulates, retrospective assignments, diagnostics/failures, external anchors,
and prospectively frozen predictions.

## 2. κ normalization and exact phase-rate closure

TIR defines

\[
\boxed{\kappa\equiv\frac{\ln2}{24\pi}}.
\]

Current status of this equation:

- **classification:** model postulate / structural definition;
- **continuous fit:** none in the numerical coefficient itself;
- **discrete structural choices:** present and explicit;
- **standard-physics first-principles derivation:** not claimed.

For angular phase

\[
\omega\equiv\frac{d\phi}{dt}=2\pi f
\]

and the TIR definition

\[
d\mathcal I\equiv\kappa\,d\phi,
\]

the reviewed exact conditional identity is

\[
\boxed{
\Gamma_{\mathcal I}
\equiv\frac{d\mathcal I}{dt}
=\kappa\omega
=\frac{\ln2}{12}f
}.
\]

One complete phase cycle carries

\[
\boxed{
\Delta\mathcal I_{\rm cycle}=2\pi\kappa=\frac{\ln2}{12}
}.
\]

The cancellation of \(\pi\) is an exact consequence of converting angular rate
to cyclic frequency.  It is not an independent construction of \(\pi\).

### Constraint count

For

\[
\mathbf q=(\kappa,\omega,f,\Gamma_{\mathcal I})
\]

with

\[
C_1=\kappa-\frac{\ln2}{24\pi},
\qquad
C_2=\omega-2\pi f,
\qquad
C_3=\Gamma_{\mathcal I}-\kappa\omega,
\]

the constraint Jacobian has rank three.  Conditional on the definitions, the
subsystem is therefore one-dimensional:

\[
\boxed{
\mathbf q(f)=
\left(
\frac{\ln2}{24\pi},
2\pi f,
f,
\frac{\ln2}{12}f
\right)}.
\]

A physical identification of \(\Gamma_{\mathcal I}\) with a measurable
``surface-refresh rate'' remains an **open operational interpretation**.

## 3. Corrected Berry-phase normalization

The reviewed source uses the standard spin-\(1/2\) relation

\[
\gamma=-\frac{\Omega}{2}\pmod{2\pi}.
\]

Therefore:

- hemisphere solid angle \(|\Omega|=2\pi\) gives phase magnitude \(\pi\);
- full-sphere solid angle \(4\pi\) gives phase magnitude \(2\pi\), trivial modulo
  \(2\pi\).

The older statement `4π/2 = π` has been removed from the live reviewed
Metatime framework.  The factor \(\pi\) in the TIR normalization is treated as
a chosen spinorial/geometric reference phase scale, not as the Berry phase of a
full-sphere loop.

## 4. TIR ↔ Secret-of-a-Half interface

The reviewed typed chain is

\[
\boxed{
\frac12
\xrightarrow{\;H_2\;}
\ln2
\xrightarrow{\;\text{TIR definition}\;}
\kappa
\xrightarrow{\;d\mathcal I=\kappa d\phi\;}
\Gamma_{\mathcal I}
}.
\]

Logical types:

1. \(H_2(1/2)=\ln2\) and uniqueness of the binary entropy maximum are exact
   information theory;
2. \(\ln2\mapsto\kappa=\ln2/(24\pi)\) contains the TIR structural
   normalization postulate;
3. \(\kappa\mapsto\Gamma_{\mathcal I}=(\ln2/12)f\) is exact conditional on the
   TIR phase-information definition.

The interface is documented in:

- `TIR/docs/cross_reviews/TIR_SECRET_HALF_2026-08-07.md`;
- `TIR/monograph/appendices/appP_secret_half_cross_relation.tex`.

It must not be used circularly to prove the TIR normalization.

## 5. Exact negative theorem imported from DHSE-001 Stage M

The sibling `secret-of-a-half` review establishes, on its declared finite
Möbius universe,

\[
N_n(q)=N_n(1/q)
\]

but nevertheless finds off-centre global maximizers for word lengths 1 and 4.
Consequently,

\[
\boxed{
\text{reciprocal self-duality}
\not\Rightarrow
\text{dynamical extremum at the self-dual point}
}.
\]

TIR may therefore use self-duality as a symmetry constraint, but any claim of
preference, stability, attractor status, or extremality requires an additional
condition or theorem such as positivity, convexity, monotonicity, or a
variational principle.

## 6. Reproducibility layers

### Selected legacy subset

`TIR/run_audit.py --json`

- checks nine selected historical quantities against frozen engineering
  tolerances;
- reports schema `TIR_SELECTED_LEGACY_REPRODUCIBILITY_V11_1`;
- a technical PASS is **not** a full physical PASS or global accuracy score.

### Exact κ phase-rate audit

`TIR/validation/kappa_phase_rate_identity_v11_1.py`

Primary certificate tracks formal factors exactly:

\[
\frac1{24}(\ln2)\pi^{-1}\times2\pi f
=\frac1{12}(\ln2)f.
\]

It then performs secondary numerical implementation checks and records the
rank-three constraint certificate.

### Reviewed source contract

`TIR/validation/review_source_contract_v11_1.py`

Protects the reviewed κ sections, corrected Berry normalization, source-code
appendix, Appendix P, cross-review boundary and legacy technical/physical claim
separation.

## 7. Publication state

The long publication source is

`TIR/monograph/metatime_monograph.tex`

and the short paper source is

`TIR/metatime_paper.tex`.

The 7 August review adds:

- exact κ phase-rate and constraint-manifold sections;
- corrected Berry-phase normalization;
- a reviewed source-code/reproducibility appendix;
- Appendix P for the TIR ↔ Secret-of-a-Half interface;
- a synchronized short-paper patch;
- an exact-head CI source contract and publication preflight.

The authoritative workflow is:

`.github/workflows/compile-metatime-monograph.yml`.

**Validation rule:** a PASS belongs only to the exact commit tested.  A prior
green run must not be transferred to a later modified review head.

## 8. Physical tensions retained

The v11 publication protocol intentionally retains failures and tensions rather
than hiding them inside an aggregate score.

### Gauge sector

The active gauge-boson mass relations remain at several-percent tension with
the comparison values used by the monograph.  They are not promoted to precision
predictions.

### Strong CP / neutron EDM

For the active exponent-14 strong-CP assignment, the reviewed publication
snapshot gives approximately

\[
\theta_{\rm QCD}=2.2208\times10^{-10}
\]

and, with the fixed hadronic conversion coefficient used by the manuscript,

\[
\boxed{
d_n=5.3299\times10^{-26}\ e\,\mathrm{cm}
}.
\]

Against the manuscript bound

\[
1.8\times10^{-26}\ e\,\mathrm{cm},
\]

this is a factor of approximately \(2.96\) high.  The computation may be a
technical PASS while the empirical constraint is a **physical FAIL**.

### Collatz isolated mass trace

The isolated frozen Collatz quarter-power trace remains an incomplete
retrospective signal rather than a closed spectrum derivation.  Its known
multiplicative error is retained by the v11 publication protocol.

## 9. Prospective component

The v10.7 separable candidate family remains the principal frozen prospective
component.  Candidate formulas, orthogonal observables and no-refit rules must
remain fixed before the assigned future likelihood is inspected.

Retrospective formula assignments are not counted as independent confirmation
merely because they reproduce their development-era targets.

## 10. Current open mathematical and physical work

1. Determine whether the discrete denominator \(24\pi\) can acquire a stronger
   non-circular derivation, or remain explicitly a TIR normalization postulate.
2. Define an operational observable corresponding to
   \(\Gamma_{\mathcal I}\) before making a physical refresh-rate claim.
3. Characterize what additional conditions turn self-duality into extremality
   in the relevant dynamical sectors.
4. Continue the Collatz/holonomy and sector-specific derivational audits without
   hiding negative results.
5. Keep renormalization scale/scheme conventions explicit for scale-dependent
   particle quantities.
6. Evaluate frozen prospective candidates only against their preregistered
   observables and decision rules.
7. Maintain the Secret-of-a-Half zeta bridges as open unless their complete
   proof dependencies are actually closed.

## 11. Historical status

The previous v10.0 / Dr-Milligan-reviewed status document contained useful
historical review notes but also several now-stale statements, including old
sector classifications, build state, branch information and reproducibility
language.  Those historical records are preserved in repository history and
`archive/`; this file is the live review-state summary.

## Invariant

\[
\boxed{
\text{technical PASS}
\neq
\text{formal proof of every model assumption}
\neq
\text{physical PASS}
}
\]

Every promotion requires the evidence class appropriate to the claim being
promoted.
