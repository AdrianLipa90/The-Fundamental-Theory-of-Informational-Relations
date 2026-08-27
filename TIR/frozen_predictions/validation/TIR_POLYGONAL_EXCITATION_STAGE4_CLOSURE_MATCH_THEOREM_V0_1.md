# TIR Polygonal Excitation — Stage 4 Closure-Match Theorem v0.1

**Validation branch:** `hypothesis/polygonal-excitation-freeze-20260825`  
**Status:** `STAGE_4_STRUCTURAL_THEOREM_PASS`  
**Data use:** none  
**PDG use:** none  
**Atomic-spectrum use:** none  

## 1. Purpose

This stage tests whether the Stage 1 polygonal degeneracy at base cardinality six and the Stage 3 spinor closure at order six can be related without inserting an observable-dependent rule.

The frozen v0.1 hypothesis is not modified here.

## 2. Equal-edge pole-to-polygon family

Place the polar apex at

\[
A=(0,0,1)
\]

on the unit Bloch sphere. Let a regular \(N\)-gon base lie at latitude \(c\), with vertices

\[
B_k=\left(\sqrt{1-c^2}\cos\frac{2\pi k}{N},
          \sqrt{1-c^2}\sin\frac{2\pi k}{N},c\right).
\]

The squared apex-to-base edge length is

\[
\ell_A^2=2(1-c).
\]

The squared adjacent base-edge length is

\[
\ell_B^2=2(1-c^2)\left(1-\cos\frac{2\pi}{N}\right).
\]

For the non-degenerate equal-edge branch \(c\neq1\), imposing

\[
\ell_A=\ell_B
\]

gives

\[
c_N=\frac{\cos(2\pi/N)}{1-\cos(2\pi/N)}.
\]

The canonical tetrahedral value is recovered at \(N=3\):

\[
c_3=-\frac13.
\]

The next values are

\[
c_4=0,
\qquad
c_5=\frac1{\sqrt5},
\qquad
c_6=1.
\]

At \(N=6\), the non-degenerate branch meets the degenerate polar solution \(c=1\). For \(N>6\), the formal non-degenerate expression gives \(c_N>1\), outside the unit Bloch sphere. Thus under this strict equal-edge/unit-sphere condition the admissible non-degenerate sequence is

\[
N=3,4,5,
\]

with

\[
N_{\rm deg}=6
\]

as the first closure/degeneracy boundary.

## 3. Spinor lift of a cyclic base action

For a cyclic spatial rotation group \(C_m\), take its axis generator in \(SO(3)\),

\[
R_m=R_z\!\left(\frac{2\pi}{m}\right).
\]

Its standard spin-\(1/2\) lift to \(SU(2)\) is

\[
U_m=\exp\!\left(-\frac{i\pi}{m}\sigma_z\right).
\]

Then

\[
U_m^m=\exp(-i\pi\sigma_z)=-I,
\]

and

\[
U_m^{2m}=I.
\]

Therefore the lifted generator has order

\[
\operatorname{ord}(U_m)=2m.
\]

For the canonical tetrahedral base action \(C_3\), already present in TIR,

\[
\operatorname{ord}(U_3)=6.
\]

## 4. Closure-match theorem

Define the closure-match condition

\[
N_{\rm deg}=\operatorname{ord}(U_m).
\]

From the geometric derivation,

\[
N_{\rm deg}=6.
\]

From the spinor lift,

\[
\operatorname{ord}(U_m)=2m.
\]

Hence

\[
6=2m,
\]

which has the unique positive-integer solution

\[
\boxed{m=3}.
\]

### Theorem

Within the strict unit-Bloch-sphere, regular-base, equal-edge pole-to-polygon family, the first polygonal degeneracy cardinality equals the identity order of the spin-1/2 lift of the base cyclic action if and only if the base action is tetrahedral \(C_3\):

\[
\boxed{N_{\rm deg}=6=\operatorname{ord}(\widetilde C_3)}.
\]

No measured mass, spectral line, PDG value, or fitted coefficient enters this equality.

## 5. Scope of the result

This is a structural theorem under the explicitly stated geometric assumptions. It establishes an exact equality between two independently derived integer invariants:

- the first degeneracy cardinality of the strict equal-edge polygonal family;
- the identity order of the spinor lift of the canonical tetrahedral \(C_3\) action.

It does not by itself establish a physical causal identification between polygonal degeneracy and spinor closure.

The next validation gate is to test whether the existing TIR Bloch/Klein/Poincare transport maps these two closures to the same invariant or holonomy on the derived disk.

## 6. Falsification conditions

Stage 4 fails if any of the following is shown:

1. the Stage 1 equal-edge derivation is algebraically incorrect;
2. the canonical TIR base action is not \(C_3\);
3. the spin-1/2 lift of the relevant TIR rotation is not the standard double-cover lift used above;
4. an additional unstated assumption is required to obtain \(N_{\rm deg}=6=\operatorname{ord}(U_3)\).

Until the disk/holonomy gate is passed, no stronger physical claim is promoted.
