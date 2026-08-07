# TIR ↔ Secret of a Half cross-review — 2026-08-07

Status: **review branch / no main promotion**

This document is the canonical cross-review record for the 2026-08-07 alignment
between Metatime/TIR and `secret-of-a-half`.  It records only relations that are
already exact under stated definitions, together with the boundaries that remain
open.

## 1. Exact half-side statements

The `secret-of-a-half` programme currently contains the following exact
structural facts:

1. Binary Shannon entropy is uniquely maximal at
   \[
   p=\frac12,
   \qquad
   H_2(1/2)=\ln2.
   \]
2. Binary complement
   \[
   C(p)=1-p
   \]
   has the unique fixed point `p=1/2`.
3. In projective odds
   \[
   q=\frac{p}{1-p},
   \]
   complement is conjugate to reciprocal inversion
   \[
   q\mapsto\frac1q,
   \]
   whose unique positive fixed point is `q=1`.
4. The same `p=1/2` is the Fisher–Rao geodesic midpoint of the two labelled
   Bernoulli endpoints.

These statements do not by themselves prove a zeta bridge.

## 2. Exact TIR phase-rate subsystem conditional on its definitions

TIR defines

\[
\kappa\equiv\frac{\ln2}{24\pi}.
\]

For angular phase

\[
\omega\equiv\frac{d\phi}{dt}=2\pi f
\]

and informational phase increment

\[
d\mathcal I\equiv\kappa\,d\phi,
\]

the following is an exact algebraic consequence:

\[
\boxed{
\Gamma_{\mathcal I}
\equiv\frac{d\mathcal I}{dt}
=\kappa\omega
=\frac{\ln2}{12}f
}.
\]

One complete phase cycle therefore carries

\[
\boxed{
\Delta\mathcal I_{\rm cycle}=2\pi\kappa=\frac{\ln2}{12}
}.
\]

No new continuous coefficient appears in this conversion.

## 3. Constraint manifold

Define

\[
\mathbf q=(\kappa,\omega,f,\Gamma_{\mathcal I})\in\mathbb R^4
\]

with constraints

\[
C_1=\kappa-\frac{\ln2}{24\pi}=0,
\qquad
C_2=\omega-2\pi f=0,
\qquad
C_3=\Gamma_{\mathcal I}-\kappa\omega=0.
\]

The constraint Jacobian has rank three everywhere, hence this subsystem is a
one-dimensional regular constraint manifold.  It may be globally parametrized
by `f`:

\[
\boxed{
\mathbf q(f)=
\left(
\frac{\ln2}{24\pi},
2\pi f,
f,
\frac{\ln2}{12}f
\right)
}.
\]

Interpretation: once the TIR normalization and `dI = κ dφ` are accepted, only
one continuous degree of freedom remains among these four named quantities.

## 4. What the half contributes to TIR

The exact bridge currently available is structural, not yet dynamical or
physical:

\[
\frac12
\xrightarrow{H_2}
\ln2
\xrightarrow{\text{TIR normalization}}
\kappa
\xrightarrow{d\mathcal I=\kappa d\phi}
\Gamma_{\mathcal I}.
\]

The first arrow is an exact information-theoretic theorem.  The second contains
the discrete TIR normalization postulate.  The third is a TIR definition whose
rate consequence is exact.

This separation must remain explicit.  In particular, the chain is not a proof
that standard physics independently derives `κ`.

## 5. Important negative theorem from DHSE-001 Stage M

Reciprocal self-duality alone does **not** imply that a dynamical statistic is
maximized at the self-dual point.

For the complete primitive positive integer Möbius universe with `K=6`, target
radius `1/10`, and binary word lengths `1..4`, DHSE-001 Stage M exactly
classifies the forcing-count step function on all `q>0`.

The exact maximizers are:

- length 1: two reciprocal off-centre intervals;
- length 2: `{1}`;
- length 3: `{1}`;
- length 4: a narrow reciprocal doublet adjacent to, but excluding, `1`.

Therefore

\[
\boxed{
N(q)=N(1/q)
\;\not\Rightarrow\;
q=1\text{ is a global maximum}
}.
\]

This is useful for TIR because any future claim that a self-dual or half state
is dynamically preferred must identify the additional condition that creates
the extremum: positivity, convexity, monotonicity, variational structure,
holonomic closure, or another explicit theorem.

## 6. Code-level corrections made during this review

### TIR

- Added deterministic implementation audit for
  `κω = (ln2/12)f`.
- Added an idempotent post-generator patch so the publication builder cannot
  silently erase the reviewed phase-rate section.
- Corrected the spin-1/2 Berry-phase normalization language: a full-sphere solid
  angle `4π` gives phase magnitude `2π` modulo `2π`; a phase of magnitude `π`
  corresponds, for example, to a hemisphere solid angle `2π`.
- Reclassified `κ` consistently as a TIR structural definition/postulate rather
  than a standard-physics derivation.
- Repaired the monograph workflow so PR validation checks the actual PR head
  instead of a hard-coded historical branch.

### Secret of a Half

- Added a conservative fixed-width arithmetic certificate before the vectorized
  Stage M sweep.
- For the declared `K=6`, word lengths `1..4`, the worst conservative comparison
  bound is
  \[
  121\,(12^4)^2=52{,}027{,}785{,}216<2^{63}-1,
  \]
  so the current int64 implementation cannot overflow on the declared theorem
  domain.
- Added regression tests for this certificate and an explicit refusal boundary
  for uncertified larger word lengths.
- Registered Stage M as an exact finite computer-assisted theorem and its
  symmetry result as an exact finite counterexample to the stronger central
  maximum inference.

## 7. Claim classes after review

| Statement | Status |
|---|---|
| `H_2(1/2)=ln2`, unique binary entropy maximum | EXACT |
| complement ↔ reciprocal conjugacy | EXACT |
| positive reciprocal fixed point `q=1 ↔ p=1/2` | EXACT |
| Fisher–Rao midpoint at `1/2` | EXACT |
| `κ = ln2/(24π)` | TIR MODEL POSTULATE / STRUCTURAL DEFINITION |
| `ω=2πf` | STANDARD DEFINITION |
| `Γ_I=κω=(ln2/12)f` | EXACT CONDITIONAL IDENTITY |
| constraint-manifold dimension `1` | EXACT CONDITIONAL STATEMENT |
| physical `surface-refresh` identification | OPEN OPERATIONAL INTERPRETATION |
| Stage M finite forcing classification | EXACT FINITE COMPUTER-ASSISTED THEOREM |
| reciprocal symmetry alone forces central maximum | FALSE IN DECLARED STAGE M UNIVERSE |
| canonical zeta-state bridge | OPEN |
| RH closure from current half construction | OPEN / CONDITIONAL ONLY |

## 8. Next review targets

1. Identify every remaining live TIR document that still states the old Berry
   normalization or treats `κ` as already derived from standard physics.
2. Separate historical/archive copies from live publication sources; archives
   remain immutable.
3. Add cross-reference from the live Metatime paper to the constraint-manifold
   result and correct stale numerical/claim language there.
4. Characterize which Stage M composition sectors keep the central peak and
   which bifurcate into reciprocal doublets.
5. Only after those invariants are stable, propagate the reviewed operators into
   the vectorized PhaseNav/NOEMA implementation.
