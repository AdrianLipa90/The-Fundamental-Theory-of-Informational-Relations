# TIR Collatz–Fubini–Study Relational Phase Interface v0.1

**Date:** 2026-09-04  
**Status:** `MATHEMATICAL_INTERFACE_ADDED / PHYSICAL_BINDING_OPEN`

## 1. Upstream contract

This interface imports from Informational Dynamics of Time the discrete phase coordinate

\[
\zeta_C(n)=e^{2\pi i q(n)},
\qquad
q(Cn)=2q(n)\pmod1,
\]

for trajectories admitting the terminal Collatz cycle. The imported exact phase operator is

\[
\boxed{\zeta_C(Cn)=\zeta_C(n)^2}.
\]

The terminal anchors are

\[
q(1)=4/7,\qquad q(2)=2/7,\qquad q(4)=1/7,
\]

with

\[
q(n)\in\frac{1}{7\,2^{L_n}}\mathbb Z
\]

for an orbit reaching 1 after \(L_n\) steps.

## 2. Relational state extension

A TIR relation may now carry an explicit projective phase coordinate,

\[
\boxed{
R_{ij}
=
R_{ij}(S_i,S_j;\zeta_{ij})
}
\]

or in typed form

\[
\boxed{
R_{ij}
=
(\mathcal A_{ij},\phi_{ij},\widetilde\phi_{ij},\kappa,\ldots),
\qquad
\zeta_{ij}=e^{i\phi_{ij}}.
}
\]

Here \(\phi\in\mathbb R/2\pi\mathbb Z\) is projective phase and \(\widetilde\phi\in\mathbb R/4\pi\mathbb Z\) is an optional spinorial lift. They must not be conflated.

## 3. CP1 carrier

For any admitted two-state relation with basis \(|A\rangle,|B\rangle\), define

\[
|\Psi_{AB}\rangle
=
\frac{|A\rangle+\zeta_{AB}|B\rangle}{\sqrt{1+|\zeta_{AB}|^2}}.
\]

On the equal-weight relational section

\[
|\zeta_{AB}|=1,
\]

so

\[
|\Psi_{AB}\rangle
=
\frac{|A\rangle+e^{i\phi_{AB}}|B\rangle}{\sqrt2},
\qquad
\theta=\pi/2.
\]

This is a standard CP1 projective-state construction. The TIR-specific content is the assignment of a relational role to the phase coordinate.

## 4. Nucleon effective interface

At the effective nucleon/isospin level,

\[
|p\rangle\leftrightarrow|uud\rangle,
\qquad
|n\rangle\leftrightarrow|udd\rangle,
\]

while the two-nucleon relation may be represented as

\[
\boxed{
|\Psi_{pn}(\zeta)\rangle
=
\frac{|pn\rangle-\zeta|np\rangle}{\sqrt{1+|\zeta|^2}}.
}
\]

For \(|\zeta|=1\), \(\zeta=e^{i\phi}\) is the relative projective phase. At \(\zeta=1\) the displayed sign convention gives the antisymmetric isospin combination; at \(\zeta=-1\) it gives the symmetric combination.

This expression is an **effective nucleon-basis state**, not a claim that the physical deuteron is a literal free six-quark product state.

## 5. Relation to TIR information normalization

The canonical normalization remains

\[
\boxed{\kappa=\frac{\ln2}{24\pi}}.
\]

For any phase-carrying relation for which the existing TIR differential law

\[
d\mathcal I=\kappa\,d\phi
\]

is admitted, the imported phase itinerary supplies a discrete sequence of projective coordinates. It does **not** by itself determine elapsed physical time, energy, mass or interaction strength.

## 6. Transition-state interface

For a two-state sector \(|i\rangle,|f\rangle\),

\[
\mathcal H_{if}=\operatorname{span}\{|i\rangle,|f\rangle\},
\qquad
\mathbb P(\mathcal H_{if})\cong\mathbb CP^1,
\]

and

\[
|\psi\rangle
=
\frac{|i\rangle+\zeta_{if}|f\rangle}{\sqrt{1+|\zeta_{if}|^2}}.
\]

Thus the same projective geometry can carry nuclear and electronic two-state relations. This closes a **mathematical interface** only. A physical transition law still requires the Hamiltonian and the appropriate matrix element/selection operator.

## 7. Required downstream gates

The following remain OPEN:

1. derive the physical rule binding a TIR/IDT phase itinerary to an atomic Hamiltonian;
2. determine whether the phase factor modifies, reproduces or is redundant with standard transition amplitudes;
3. test whether any new selection suppression or spectral phase survives empirical comparison;
4. propagate the phase coordinate through the TIR–IDT ADM/Einstein interface without inserting a new metric term by analogy.

## 8. Claim firewall

**PASS / exact mathematics:** parity phase map imported from IDT; CP1 two-state representation; 2π projective / 4π spinorial distinction.

**MODEL-LEVEL TIR extension:** explicit relational phase coordinate \(\zeta_{ij}\).

**OPEN physics:** identification with measurable temporal, nuclear, chemical, spectroscopic or gravitational observables.
