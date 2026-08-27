# Claim Hierarchy — v11.1 review

This is the live claim taxonomy used by the reviewed Metatime/TIR sources.  It
supersedes the older Milligan-era A/B/C/D/E table where several structural
postulates and retrospective assignments had been placed in stronger classes.
Historical classifications remain in repository history and `archive/`.

## Publication classes

| Class | Meaning |
|---|---|
| **A** | Established mathematical identity or external experimental result supported by standard sources. |
| **B** | TIR/Metatime model postulate or structural definition. |
| **C** | Retrospective phenomenological assignment developed with access to some or all target values. |
| **D** | Diagnostic result, retained failure, falsification witness, or restricted no-go theorem. |
| **E** | Prospectively frozen prediction with a declared observable and no-refit rule. |
| **F** | External anchor, scale, convention, or conversion input supplied to the construction. |

An exact theorem **conditional on class-B definitions** is recorded as an exact
formal consequence, but the exactness of the consequence does not promote the
underlying postulate to class A.

## A. Established ingredients

| Claim | Status / reason |
|---|---|
| Binary Shannon entropy is uniquely maximal at \(p=1/2\), with \(H_2(1/2)=\ln2\). | Standard information theory. |
| \(\omega=2\pi f\). | Standard conversion between cyclic and angular frequency. |
| Spin-\(1/2\) Berry phase satisfies \(\gamma=-\Omega/2\pmod{2\pi}\). | Standard geometric-phase result. |
| Rotational tetrahedral group \(A_4\) has order 12; full tetrahedral group is isomorphic to \(S_4\) of order 24. | Standard group theory. |
| External comparison values and bounds used by a frozen publication snapshot. | Class A only as quoted external facts when supported by the cited source; they are not TIR predictions. |

## B. TIR structural definitions and postulates

| Claim | Current status |
|---|---|
| \(\kappa\equiv\ln2/(24\pi)\). | **B — model postulate / structural definition.** The numerator and standard phase/group ingredients motivate the form, but standard physics does not independently derive the full coefficient. |
| \((L_3,L_4,L_5)=(7,2,5)\). | B — discrete structural choice; no unique first-principles derivation currently established. |
| Quark-prime labels \((u,d,s,c,b,t)=(3,5,7,11,13,17)\). | B — discrete assignment; alternatives require explicit falsification/comparison. |
| Exponential mass ansatz \(m=E_P e^{-S/\kappa}\) in the declared sectors. | B/C depending on the sector-specific action construction; not a universal established mass law. |
| Tetrahedral/NOEMA operator assignments to flavour or mixing observables. | B — model geometry until a physical derivation and prospective transfer test are supplied. |
| Informational phase definition \(d\mathcal I=\kappa\,d\phi\). | B — TIR definition. |

## Exact formal consequences conditional on class B

These statements are mathematically exact **once their stated TIR definitions
are adopted**.

### κ phase-rate closure

\[
\kappa=\frac{\ln2}{24\pi},
\qquad
\omega=2\pi f,
\qquad
d\mathcal I=\kappa d\phi
\]

give

\[
\boxed{
\Gamma_{\mathcal I}
=\frac{d\mathcal I}{dt}
=\kappa\omega
=\frac{\ln2}{12}f
},
\]

with

\[
\boxed{
\Delta\mathcal I_{\rm cycle}=\frac{\ln2}{12}
}.
\]

The exact factor certificate is implemented in
`TIR/validation/kappa_phase_rate_identity_v11_1.py`.

### Constraint manifold

The constraints

\[
\kappa-\frac{\ln2}{24\pi}=0,
\qquad
\omega-2\pi f=0,
\qquad
\Gamma_{\mathcal I}-\kappa\omega=0
\]

have rank three in the four named quantities
\((\kappa,\omega,f,\Gamma_{\mathcal I})\).  Therefore the declared subsystem is
one-dimensional, parametrized by \(f\), conditional on the TIR definitions.

## C. Retrospective phenomenological assignments

This class includes formula families that were developed or selected with
access to their comparison targets.  Close numerical agreement is descriptive
and hypothesis-generating, not independent confirmation.

Examples include historical charged-lepton, baryon, meson, flavour, gauge,
Higgs, strong-CP and cosmological relations where the formula architecture or
sector mapping was developed against already known values.

For these assignments:

- do not report a heterogeneous global mean percentage as evidence;
- preserve scheme/scale caveats for running quantities;
- disclose external anchors and discrete choices;
- retain negative residuals and failed sectors.

## D. Diagnostics, failures and no-go results

| Result | Current status |
|---|---|
| Gauge-boson mass relations | **Retained tension.** The active publication relations remain several percent away from the reference values used by the monograph. |
| Strong-CP → neutron-EDM mapping | **Physical FAIL under the frozen manuscript mapping.** \(\theta_{\rm QCD}\approx2.2208\times10^{-10}\) gives \(d_n\approx5.3299\times10^{-26}\,e\,\mathrm{cm}\), about \(2.96\) times the \(1.8\times10^{-26}\,e\,\mathrm{cm}\) manuscript bound. |
| Isolated Collatz quarter-power mass trace | Retrospective diagnostic; not a closed mass-spectrum derivation. |
| Restricted common up-sector baseline | No-go result for the frozen architecture tested by the v10 review line. |
| Reciprocal self-duality alone forces a dynamical maximum | **False in the declared DHSE-001 Stage-M universe.** Exact finite counterexamples occur at word lengths 1 and 4. |

A technically correct computation can therefore produce a physical FAIL.

## E. Prospectively frozen predictions

The v10.7 separable candidate family remains the principal prospective
component.  Its candidate formulas, orthogonal observables and no-refit rule are
frozen before the assigned future likelihood is inspected.

Only evaluation under the preregistered decision rule can provide prospective
support or falsification.  A failed candidate may not be replaced post hoc by a
new formula after viewing the target data.

## F. External anchors and inputs

External scales, measured reference values, fixed hadronic conversion factors,
renormalization conventions and other supplied quantities must be listed where
they enter.  A result depending on an anchor is not an independent prediction
of that anchor.

The current publication protocol, not an older shorthand count, is authoritative
for the exact list used by each sector.

## TIR ↔ Secret-of-a-Half interface

The reviewed chain is

\[
\boxed{
\frac12
\xrightarrow{\;H_2\;}
\ln2
\xrightarrow{\;\text{TIR structural definition}\;}
\kappa
\xrightarrow{\;d\mathcal I=\kappa d\phi\;}
\Gamma_{\mathcal I}
}.
\]

The arrows have different claim classes.  In particular, the exact entropy
maximum does not derive the TIR denominator \(24\pi\), and the exact phase-rate
identity does not prove a physical surface-refresh mechanism.

The sibling DHSE Stage-M result also establishes the boundary

\[
\boxed{
\text{reciprocal symmetry}
\not\Rightarrow
\text{central dynamical maximum}
}.
\]

See:
- `TIR/docs/cross_reviews/TIR_SECRET_HALF_2026-08-07.md`;
- monograph Appendix P.

## Promotion rule

A claim may move to a stronger class only when the required evidence is present
and reproducible.  In particular:

1. a model definition does not become class A because its consequences are exact;
2. retrospective agreement does not become prospective evidence;
3. a technical PASS does not become a physical PASS;
4. self-duality does not imply extremality without an additional theorem;
5. an open zeta/RH bridge remains open until every proof dependency is closed;
6. previous workflow PASS applies only to the exact commit that was tested.
