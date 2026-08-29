# Claim Hierarchy — current TIR review

This is the live claim taxonomy used by the TIR publication and validation surfaces. Historical classifications remain in repository history and archival surfaces.

## Publication classes

| Class | Meaning |
|---|---|
| **A** | Established mathematical identity or external experimental result supported by standard sources. |
| **B** | TIR structural law, model identification, or internally derived structural quantity whose upstream TIR premises remain explicit. |
| **C** | Retrospective phenomenological assignment developed with access to some or all target values. |
| **D** | Diagnostic result, retained failure, falsification witness, or restricted no-go theorem. |
| **E** | Prospectively frozen prediction with a declared observable and no-refit rule. |
| **F** | External anchor, scale, convention, or conversion input supplied to the construction. |

An exact theorem conditional on TIR structural premises is recorded as an exact formal consequence with those premises preserved in the dependency graph.

## A. Established ingredients

| Claim | Status / reason |
|---|---|
| Binary Shannon entropy is uniquely maximal at \(p=1/2\), with \(H_2(1/2)=\ln2\). | Standard information theory. |
| \(\omega=2\pi f\). | Standard conversion between cyclic and angular frequency. |
| Spin-\(1/2\) Berry phase satisfies \(\gamma=-\Omega/2\pmod{2\pi}\). | Standard geometric-phase result. |
| \(\dim\mathfrak{su}(3)=3^2-1=8\). | Standard Lie-group dimension formula. |
| Rotational tetrahedral group \(A_4\) has order 12; full tetrahedral group is isomorphic to \(S_4\) of order 24. | Standard group theory. |
| External comparison values and bounds used by a frozen publication snapshot. | External facts when supported by the cited source. |

## B. TIR structural layer

| Claim | Current status |
|---|---|
| \(\kappa=\ln2/(24\pi)\). | **TIR-internal derived structural normalization.** The denominator follows from the three-flavour \(SU(3)_F\) carrier, its eight-dimensional mixing algebra, and the primitive half-turn phase: \(24\pi=3(3^2-1)\pi\). |
| \((L_3,L_4,L_5)=(7,2,5)\). | Discrete TIR structural integers with their own sector provenance. |
| Quark-prime labels \((u,d,s,c,b,t)=(3,5,7,11,13,17)\). | Discrete flavour assignment with explicit sector validation. |
| Exponential mass ansatz \(m=E_P e^{-S/\kappa}\) in the declared sectors. | TIR sector law with sector-specific action construction. |
| Tetrahedral/NOEMA operator assignments to flavour or mixing observables. | TIR model geometry with separate empirical validation surfaces. |
| Informational phase definition \(d\mathcal I=\kappa\,d\phi\). | TIR information-phase law. |

### κ flavour-mixing normalization

The flavour carrier is

\[
V_F\cong\mathbb C^3,
\qquad
U_F\in SU(3)_F.
\]

Thus

\[
N_F=3,
\qquad
\dim\mathfrak{su}(3)_F=3^2-1=8.
\]

The generator-flavour channel count is

\[
\boxed{
N_{\rm mix}=3\cdot8=24.
}
\]

The primitive half coordinate maps one full angular turn to the half-turn unit

\[
\Delta\phi_{1/2}=\frac12(2\pi)=\pi.
\]

Therefore

\[
\boxed{
\Phi_{\rm mix}=N_{\rm mix}\Delta\phi_{1/2}=24\pi.
}
\]

With

\[
I_\star=H_2(1/2)=\ln2,
\]

the TIR information-per-mixing-phase normalization gives

\[
\boxed{
\kappa
=\frac{I_\star}{\Phi_{\rm mix}}
=\frac{\ln2}{3(3^2-1)\pi}
=\frac{\ln2}{24\pi}.
}
\]

The canonical derivation surface is

`TIR/foundations/TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md`.

The exact validator is

`TIR/validation/tir_kappa_flavour_mixing_normalization_v0_1.py`.

The spatial branch supplies the independent integer crosscheck

\[
3\dim\mathfrak{su}(3)_F
=24
=|S_4|.
\]

## Exact formal consequences of the κ layer

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
\Delta\mathcal I_{\rm cycle}=\frac{\ln2}{12}.
}
\]

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
\((\kappa,\omega,f,\Gamma_{\mathcal I})\). Therefore the declared subsystem is one-dimensional, parametrized by \(f\).

## C. Retrospective phenomenological assignments

This class contains sector formula families developed or selected with access to comparison targets. Their exact algebraic evaluation and empirical residuals are recorded separately.

Representative sectors include historical charged-lepton, baryon, meson, flavour, gauge, Higgs, strong-CP and cosmological relations.

## D. Diagnostics and falsification surfaces

| Result | Current status |
|---|---|
| Gauge-boson mass relations | Retained several-percent tension in the active publication formulas. |
| Strong-CP → neutron-EDM mapping | Physical FAIL under the frozen manuscript mapping; retained as an explicit falsification witness. |
| Isolated Collatz quarter-power mass trace | Retrospective diagnostic awaiting complete spectrum derivation. |
| Restricted common up-sector baseline | No-go result for the frozen architecture tested by the review line. |
| Reciprocal self-duality alone forces a dynamical maximum | Exact finite counterexamples occur at word lengths 1 and 4 in the declared DHSE-001 Stage-M universe. |

## E. Prospectively frozen predictions

The frozen candidate family preserves its candidate formulas, orthogonal observables and no-refit decision rules before assigned future likelihoods are inspected.

## F. External anchors and inputs

External scales, measured reference values, fixed hadronic conversion factors and renormalization conventions are declared at their point of use.

## TIR ↔ Secret-of-a-Half interface

The current dependency chain is

\[
\boxed{
\frac12
\xrightarrow{H_2}
\ln2
\xrightarrow{SU(3)_F\;3\times8\;\mathrm{mixing}\;+\;\pi\;\mathrm{half\!\!-turn}}
\kappa
\xrightarrow{d\mathcal I=\kappa d\phi}
\Gamma_{\mathcal I}.
}
\]

The numerator is supplied by the exact binary entropy theorem. The denominator is supplied by the three-flavour mixing multiplicity and the half-turn angular measure.

The sibling DHSE Stage-M result retains the separate dynamical constraint

\[
\boxed{
\text{reciprocal symmetry}
\not\Rightarrow
\text{central dynamical maximum}
}
\]

inside its declared finite universe.

## Promotion rule

Claim status is carried by explicit dependency provenance, deterministic validation where applicable, and the evidence class appropriate to each physical observable. A PASS is attached only to the exact commit and exact theorem surface tested.
