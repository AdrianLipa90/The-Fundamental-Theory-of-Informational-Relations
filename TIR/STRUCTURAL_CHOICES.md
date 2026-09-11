# Structural-Choice Audit — current TIR review

This ledger tracks discrete choices, internal structural derivations, external anchors and sector formula selections used by live TIR constructions.

## Legend

| Type | Meaning |
|---|---|
| `A` | Established external mathematical/physical ingredient. |
| `D_TIR` | Quantity derived internally from explicit TIR structural parents. |
| `P` | TIR structural law or definition. |
| `S` | Discrete structural selection among alternatives. |
| `R` | Retrospective formula/architecture choice made with access to target data. |
| `F` | External physical scale, convention or conversion input. |
| `E` | Prospectively frozen candidate or observable. |
| `D` | Diagnostic/failure/no-go construction. |

## Fundamental structural layer

| Symbol / rule | Value | Type | Current status |
|---|---:|---|---|
| binary entropy maximum | \(p=1/2\), \(H_2=\ln2\) | A | Exact information theory. |
| full angular closure | \(2\pi\) | A | Standard radian circle. |
| primitive half-turn | \(\pi=(1/2)(2\pi)\) | A + TIR root | Half coordinate mapped to angular closure. |
| flavour carrier | \(V_F\cong\mathbb C^3\) | D_TIR | Three-flavour family carrier. |
| flavour mixing group | \(SU(3)_F\) | D_TIR | Full CKM-form family carrier. |
| mixing-algebra dimension | \(\dim\mathfrak{su}(3)_F=8\) | A + D_TIR | \(3^2-1\). |
| mixing-channel count | \(N_{mix}=3\cdot8=24\) | D_TIR | Generator × flavour incidence count. |
| \(\kappa\) | \(\ln2/(24\pi)\) | D_TIR | Derived from \(I_\star=\ln2\) over the \(24\pi\) primitive mixing-phase measure. |
| Platonic index alphabet | \(\{3,4,5\}\) | A | Exact consequence of the convex Platonic Schläfli classification. |
| tetrahedral root group | \(A_4\) | A + TIR root | Common finite rotational root for the triangular Platonic branch. |
| \(L_4\) | \([S_4:A_4]=2\) | D_TIR | Exact subgroup-index consequence. |
| \(L_5\) | \([A_5:A_4]=5\) | D_TIR | Exact subgroup-index consequence using an \(A_4\) point stabilizer in \(A_5\). |
| root-extension closure | \(X_3^{\rm closure}=S_4/A_4\sqcup A_5/A_4\) | P | TIR structural closure rule over the two non-self-dual Platonic extensions. |
| \(L_3\) | \(|X_3^{\rm closure}|=7\) | D_TIR | Exact cardinality consequence \(2+5=7\). |
| informational phase rule | \(d\mathcal I=\kappa d\phi\) | P | TIR information-phase law. |

The κ derivation is

\[
\boxed{
N_F=3,
\qquad
\dim\mathfrak{su}(3)_F=3^2-1=8,
\qquad
N_{mix}=3\cdot8=24,
}
\]

\[
\boxed{
\Delta\phi_{1/2}=\frac12(2\pi)=\pi,
\qquad
\Phi_{mix}=24\pi,
}
\]

and therefore

\[
\boxed{
\kappa
=\frac{H_2(1/2)}{\Phi_{mix}}
=\frac{\ln2}{3(3^2-1)\pi}
=\frac{\ln2}{24\pi}.
}
\]

Canonical derivation:

`TIR/foundations/TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md`.

Validator:

`TIR/validation/tir_kappa_flavour_mixing_normalization_v0_1.py`.

The spatial branch independently supplies

\[
|\operatorname{Aut}(\Delta^3)|=|S_4|=24,
\]

as a finite-symmetry crosscheck of the same integer.

## Platonic L-constant closure

For convex regular polyhedra,

\[
\frac1p+\frac1q>\frac12,
\qquad p,q\ge3,
\]

gives exactly

\[
\{3,3\},\{3,4\},\{3,5\},\{4,3\},\{5,3\}.
\]

The triangular branch has rotational groups

\[
A_4,\qquad S_4,\qquad A_5,
\]

and the common tetrahedral root yields

\[
\boxed{L_4=[S_4:A_4]=2},
\qquad
\boxed{L_5=[A_5:A_4]=5}.
\]

With the explicit TIR root-extension closure rule

\[
X_3^{\rm closure}=S_4/A_4\sqcup A_5/A_4,
\]

one obtains

\[
\boxed{L_3=|X_3^{\rm closure}|=2+5=7}.
\]

Hence

\[
\boxed{(L_3,L_4,L_5)=(7,2,5)}.
\]

This is an exact TIR-internal structural derivation conditional on the declared closure rule. The pre-existing Collatz/twin-prime route is retained as an independent arithmetic crosscheck rather than used as an input to the Platonic derivation.

Canonical derivation:

`TIR/foundations/TIR_PLATONIC_L_CONSTANTS_CLOSURE_V0_1.md`.

Validator:

`TIR/validation/tir_platonic_l_constants_closure_v0_1.py`.

A specifically \(CP^3\)-Kähler derivation and all physical identifications remain separate downstream questions.

## Exact phase-rate consequence

\[
\Gamma_{\mathcal I}
=\kappa\omega
=\frac{\ln2}{12}f
\]

for \(\omega=2\pi f\). This consequence introduces no additional continuous coefficient.

## Discrete flavour labels

| Label | Value | Type |
|---|---:|---|
| \(q(u)\) | 3 | S |
| \(q(d)\) | 5 | S |
| \(q(s)\) | 7 | S |
| \(q(c)\) | 11 | S |
| \(q(b)\) | 13 | S |
| \(q(t)\) | 17 | S |

Their sector-level uniqueness and predictive validation are tracked separately from the κ mixing-multiplicity derivation and the Platonic L-constant closure.

## External scales and inputs

Common examples include the Planck scale in selected mass constructions, proton mass in selected hadronic/electroweak relations, QCD colour count where used as an external Standard-Model input, hadronic conversion coefficients, and renormalization conventions.

## Charged-lepton architecture

Representative forms include

\[
S_e=\frac12-3\kappa+\frac{\kappa}{L_3}-\frac{\kappa^2}{2}
\]

and the declared exponential mass law

\[
m=E_Pe^{-S/\kappa}.
\]

Their sector assignments retain their own S/R provenance.

## Baryon and hadronic architecture

The octet, decuplet and related coefficient/baseline mappings retain sector-specific provenance and explicit empirical residuals.

## Neutrino / PMNS architecture

The current PMNS branch uses the three-flavour carrier and tetrahedral relation geometry. Formula-level angle and mass assignments retain their individual provenance. The carrier-level facts

\[
V_F\cong\mathbb C^3,
\qquad
SU(3)_F,
\qquad
\dim\mathfrak{su}(3)_F=8
\]

are the parents used by the κ normalization theorem.

## CKM architecture

The family-mixing carrier is represented by

\[
V_F^{mix}=R_{23}R_{13}(\delta)R_{12}\in SU(3)_F.
\]

Current validation establishes its group-theoretic home independently of the numerical angle formulas.

## Gauge / electroweak / Higgs architecture

These sectors retain their formula-specific empirical audits and residuals. Existing tensions remain explicit in the validation ledger.

## Strong CP

The active strong-CP mapping and neutron-EDM conversion remain frozen diagnostic surfaces with their current empirical verdict retained.

## TIR ↔ Secret-of-a-Half interface

The current structural chain is

\[
\boxed{
\frac12
\xrightarrow{H_2}
\ln2
\xrightarrow{3\times8\;SU(3)_F\;mixing\;+\;\pi\;half\!\!-turn}
\kappa
\xrightarrow{d\mathcal I=\kappa d\phi}
\Gamma_{\mathcal I}.
}
\]

## Audit invariant

Every formula records its upstream structural parents, data visibility during formula selection, dimensional anchors, evidence class, discrete alternatives where relevant, and prospective decision rule when one exists.
