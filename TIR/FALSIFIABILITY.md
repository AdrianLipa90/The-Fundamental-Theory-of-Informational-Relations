# Falsifiability and Decision Criteria — v11.1 review

A TIR result is falsifiable only when the formula, observable, comparison
convention and decision rule are fixed before the relevant evidence is used for
model selection or repair.  This file therefore separates **current retained
failures**, **prospectively frozen tests**, and **open hypotheses that do not yet
have a valid falsification gate**.

## 1. Current retained physical failures and tensions

The current publication snapshot deliberately keeps these results visible.

| Observable | Active TIR value / relation | Comparison used by publication | Status |
|---|---:|---:|---|
| neutron EDM | \(d_n=5.3299\times10^{-26}\,e\,\mathrm{cm}\) | \(|d_n|<1.8\times10^{-26}\,e\,\mathrm{cm}\) (90% CL manuscript bound) | **PHYSICAL FAIL** — factor \(\approx2.96\) high |
| \(M_W\) relation | several-percent residual in active publication formula | reference mass used by frozen v11 table | **TENSION** |
| \(M_Z\) relation | several-percent residual in active publication formula | reference mass used by frozen v11 table | **TENSION** |
| isolated Collatz quarter-power mass trace | geometric-mean multiplicative error \(\approx9.967\) | frozen v10.1 comparison | **NOT A CLOSED DERIVATION** |

A technically correct computation can therefore be a physical FAIL.  No hidden
suppression factor, exponent change or candidate substitution is inserted after
the result to erase a failed gate.

## 2. Strong-CP / neutron-EDM gate

The active reviewed assignment is

\[
\theta_{\rm QCD}
=\kappa\left(\frac27\right)^{14}
\approx2.2208\times10^{-10}.
\]

With the fixed hadronic conversion coefficient used by the publication snapshot,
this maps to

\[
\boxed{
 d_n\approx5.3299\times10^{-26}\,e\,\mathrm{cm}
}.
\]

Against the manuscript bound

\[
1.8\times10^{-26}\,e\,\mathrm{cm},
\]

the frozen mapping fails.  The correct current statement is therefore:

- arithmetic / implementation may PASS;
- the frozen physical constraint **FAILS**;
- no unimplemented cancellation or suppression mechanism is counted as a rescue;
- changing the exponent or conversion after observing the bound would create a
  new hypothesis and must not retroactively convert the frozen result to PASS.

## 3. κ phase-rate: formal falsifiability versus physical testability

The reviewed identity

\[
\Gamma_{\mathcal I}
=\kappa\omega
=\frac{\ln2}{12}f
\]

is an exact algebraic consequence of the TIR definitions, so it is not itself an
empirical prediction until \(\Gamma_{\mathcal I}\) is tied to an operationally
measurable quantity.

Current classification:

| Component | Status |
|---|---|
| \(\kappa=\ln2/(24\pi)\) | TIR model postulate / structural definition |
| \(\omega=2\pi f\) | standard definition |
| \(d\mathcal I=\kappa d\phi\) | TIR definition |
| \(\Gamma_{\mathcal I}=(\ln2/12)f\) | exact conditional identity |
| physical surface-refresh observable | **OPEN — no empirical gate yet** |

To make the physical interpretation falsifiable, a future protocol must freeze:

1. the instrument-level observable corresponding to \(\Gamma_{\mathcal I}\);
2. the independent measurement of \(f\);
3. units and calibration;
4. uncertainty propagation;
5. the acceptance/rejection rule;
6. the no-refit policy.

Until then, the algebra can be validated technically but the physical
interpretation cannot receive an empirical PASS.

## 4. TIR ↔ Secret-of-a-Half boundary

The cross-review contains an exact negative result relevant to falsification
logic.  In the declared DHSE-001 Stage-M finite universe,

\[
N_n(q)=N_n(1/q)
\]

does **not** force \(q=1\) to maximize \(N_n\).  Word lengths 1 and 4 are exact
counterexamples.

Therefore a TIR claim of dynamical preference at a self-dual point must freeze
and test the **additional mechanism** that creates extremality.  Reciprocal
symmetry alone is insufficient.

## 5. Prospectively frozen component

The v10.7 separable candidate family remains the principal explicitly
prospective TIR component.  It has:

- a finite frozen candidate set;
- two orthogonal target observables;
- a post-freeze data gate;
- a no-refit/no-substitution rule.

Those candidates must be evaluated using their preregistered likelihood and
comparison conventions.  A candidate that fails may be rejected, but a new
formula introduced after viewing the target data is a new experiment, not a
repair of the old prediction.

## 6. Statements that are not currently valid frozen predictions

Older documents used broad statements such as:

- exact future values for dark-energy equation of state;
- absolute exclusion of a fourth neutrino/sterile state;
- infinite proton lifetime;
- postulated future gauge-boson values after an unspecified coupling repair;
- a hypothetical neutron-EDM value after an unspecified suppression factor.

Unless a live review document supplies a frozen derivation, observable,
uncertainty model and decision rule, these are **not counted as active
prospective TIR predictions** in the v11.1 review state.

## 7. Framework-level failure modes

The programme should lose support, require revision, or reject a submodel when
one of the following occurs under a properly frozen test:

1. a claimed exact derivation contains a mathematical error or hidden assumption;
2. an implementation receipt fails to reproduce its declared exact/formal result;
3. a prospective physical observable violates its frozen acceptance rule;
4. a claimed independent prediction is shown to depend on an undisclosed target
   value or external anchor;
5. a proposed universal relation fails in a new sector under the same frozen
   operator and conventions;
6. a supposedly unique structural choice is shown to belong to a large equally
   successful alternative family without a selection theorem;
7. a self-duality-based extremality claim lacks the additional condition required
   by the exact DHSE counterexample;
8. a simpler model with equal or better prospective likelihood and lower effective
   complexity dominates under an agreed comparison protocol.

## 8. Invariant

\[
\boxed{
\text{falsifiability}
=
\text{frozen claim}
+
\text{operational observable}
+
\text{decision rule}
+
\text{no post-hoc repair}
}
\]

A failed prediction is retained as evidence about the model rather than removed
from the record.
