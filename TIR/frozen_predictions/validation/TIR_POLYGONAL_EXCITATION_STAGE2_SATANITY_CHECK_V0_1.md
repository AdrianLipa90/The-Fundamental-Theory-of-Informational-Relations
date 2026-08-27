# TIR Polygonal Excitation — Stage 2 SATANITY CHECK v0.1

**Branch:** `hypothesis/polygonal-excitation-freeze-20260825`  
**Status:** `STRUCTURAL_COINCIDENCE_RECORDED_NOT_PHYSICALLY_PROMOTED`  
**Purpose:** test whether the first geometric degeneration at N=6 has an independent algebraic counterpart.

## Frozen parent

This document evaluates, without modifying, `TIR_POLYGONAL_EXCITATION_POINCARE_ORBITAL_HYPOTHESIS_V0_1.md`.

Stage 1 found that under the stronger regularity condition in which the polar-apex-to-base edges and adjacent base edges are equal while all vertices lie on the unit Bloch sphere,

\[
c_N=\frac{\cos(2\pi/N)}{1-\cos(2\pi/N)}.
\]

Hence

\[
c_3=-\frac13,\qquad c_4=0,\qquad c_5=\frac1{\sqrt5},\qquad c_6=1.
\]

At N=6 the base latitude reaches the polar apex and the equal-edge construction degenerates. For N>6 the same condition would require c_N>1 and therefore leaves the unit Bloch sphere.

## Independent cyclic-symmetry test

A regular N-point base carries cyclic rotational symmetry C_N. At N=6,

\[
C_6 \cong C_2\times C_3,
\]

because gcd(2,3)=1 and the Chinese remainder theorem gives

\[
\mathbb Z/6\mathbb Z \cong \mathbb Z/2\mathbb Z\times\mathbb Z/3\mathbb Z.
\]

Thus N=6 is simultaneously:

1. the first N after 3,4,5 for which the strong equal-edge Bloch-sphere geometry degenerates; and
2. a cyclic symmetry whose abstract group decomposes exactly into order-2 and order-3 factors.

This is a mathematically exact structural coincidence. It is not, by itself, evidence that the physical excitation hierarchy terminates at N=6, nor that order-2 and order-3 factors exhaust the physical degrees of freedom.

## Why this is nontrivial

The two statements arise from independent calculations:

- the geometric threshold follows from chord/apex distance equality on the unit sphere;
- the algebraic factorization follows from finite cyclic group structure.

No PDG values, atomic spectra, masses, fitted parameters, or post-hoc numerical targets enter either result.

## Falsification targets

The next stage must attempt to break the apparent correspondence by testing:

1. whether another admissible TIR-native geometric invariant allows nondegenerate N>=6 states without introducing an ad hoc degree of freedom;
2. whether the N=6 group decomposition has any operational effect on the Poincare projection, holonomy, or action functional rather than being only an abstract group isomorphism;
3. whether the same redundancy criterion predicts additional degeneration points that are absent geometrically;
4. whether C2 and C3 are genuinely prior structural factors in the relevant TIR excitation operator, rather than merely available factorizations of 6.

## Current verdict

`STAGE_2_STRUCTURAL_HIT_REQUIRES_OPERATOR_TEST`

The N=6 degeneration and C6 ≅ C2 × C3 decomposition coincide exactly, but no physical interpretation is promoted at this stage.
