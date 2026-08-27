# TIR Polygonal Excitation Stage 7 — Poincare Double-Cover Separation Test v0.1

**Date:** 2026-08-25 11:23 BST  
**Parent hypothesis:** `TIR_POLYGONAL_EXCITATION_POINCARE_ORBITAL_HYPOTHESIS_V0_1`  
**Status:** `STAGE_7_GEOMETRIC_SEPARATION_PASS`  
**Scope:** pure mathematics; no PDG, spectral, atomic, RGB, flavour, or other physical data are used.

## 1. Question

Stage 6 established a six-state lift of a three-state cyclic action by a binary sheet,

\[
G=P_3\otimes X_2,
\qquad G^6=I_6,
\qquad G^3\neq I_6.
\]

Stage 1 independently found that the equal-edge pole-to-polygon family reaches a geometric degeneracy at

\[
N=6.
\]

The present test asks whether these two occurrences of six are already the same geometric object after the Bloch/Klein/Poincare projection, without introducing any additional identification rule.

## 2. Equivariance of the Bloch-to-Poincare projection

Let an axis-preserving rotation act on a Bloch-ball point as

\[
R_\theta:(x+iy,z)\mapsto (e^{i\theta}(x+iy),z).
\]

The radial Klein-to-Poincare map is

\[
Y(X)=\frac{X}{1+\sqrt{1-|X|^2}}.
\]

Because the map depends only on the rotational invariant norm \(|X|\), it is equivariant under rotations about the axis:

\[
Y(R_\theta X)=R_\theta Y(X).
\]

After projection to the two-dimensional disk,

\[
z\mapsto e^{i\theta}z.
\]

For the tetrahedral base action \(\theta=2\pi/3\), the projected orbit therefore closes after three steps:

\[
z\mapsto \omega z\mapsto \omega^2 z\mapsto z,
\qquad \omega=e^{2\pi i/3}.
\]

Hence the ordinary Poincare disk retains a period-three orbit.

## 3. Spinor sheet and the double cover

The spinor lift carries an additional sign sheet. A minimal lifted state space is

\[
\widetilde{\mathbb D}=\mathbb D\times \mathbb Z_2.
\]

Define the lifted generator

\[
\widetilde G:(z,s)\mapsto (\omega z,-s),
\qquad s\in\{+1,-1\}.
\]

Then

\[
\widetilde G^3(z,s)=(z,-s),
\]

while

\[
\widetilde G^6(z,s)=(z,s).
\]

Thus the six-state structure is naturally a double cover of a three-point projected orbit:

\[
3\ \text{disk positions}\times 2\ \text{sheet states}=6\ \text{lifted states}.
\]

This result requires no physical interpretation.

## 4. Equal-edge polygon family at N=6

For the equal-edge pole-to-regular-N-gon construction on the unit Bloch sphere, Stage 1 derived

\[
c_N=\frac{\cos(2\pi/N)}{1-\cos(2\pi/N)}.
\]

The base radius is

\[
r_N=\sqrt{1-c_N^2}.
\]

At \(N=6\),

\[
c_6=1,
\qquad r_6=0.
\]

Therefore all six base vertices coincide with the polar point. Their projected Poincare coordinate is a single fixed point rather than a six-point orbit.

## 5. Separation result

The two mathematical structures are therefore distinct:

1. the Stage-6 six-state object is a **double-cover orbit** over three distinct projected positions;
2. the equal-edge \(N=6\) polygon is a **collapsed geometric configuration** with zero base radius.

Consequently,

\[
\boxed{
\text{six lifted states}\ \not\equiv\ \text{six polygon vertices at }N=6
}
\]

under the current assumptions.

There is no direct geometric identification between them without an additional operator or quotient map.

## 6. What survives

The following statements remain mathematically established within the staged construction:

- the Poincare projection is rotationally equivariant;
- the projected tetrahedral \(C_3\) orbit has period 3;
- its spinor/sign-sheet lift has period 6;
- the equal-edge polygon family degenerates at \(N=6\);
- these are two different six-related structures.

The coincidence of the number six remains a structural observation, not an identification theorem.

## 7. Falsification / next gate

The next allowed mathematical question is narrower:

> Does the existing TIR geometry contain a non-ad-hoc operator connecting polygonal cardinality \(N\), radial depth \(c_N\), and sheet holonomy such that an excitation transition can exchange polygonal degrees of freedom for double-cover degrees of freedom at the degeneracy boundary?

Until such an operator is derived, no equality between the two sixes is promoted.

## 8. Verdict

`STAGE_7_GEOMETRIC_SEPARATION_PASS`

The pure-mathematical test succeeds by separating two superficially similar six-fold structures. This is a constraining result: any later unification must be produced by an explicit operator rather than by numerical coincidence.
