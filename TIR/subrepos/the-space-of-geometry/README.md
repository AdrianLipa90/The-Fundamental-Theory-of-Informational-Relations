# The Space of Geometry

Status: `TIR_SUBREPO_RESEARCH_PROGRAM_V0_2`

Working title:

> **The Space of Geometry: From First Distinction to Pythagoras**

This TIR subrepo develops the shortest local spatial-geometric derivation from the primitive relational carrier to Pythagorean closure.

The current spine is

\[
\boxed{
0
\to P
\to \text{DISTINCTION}
\to \mathbb C^2
\to \operatorname{Herm}_0(2)
\to \text{minimal faithful }SO(3)\text{ carrier}
\to \mathbb R^3
\to \Delta^3
\to \text{distance / angle / orthogonality}
\to a^2+b^2=c^2.
}
\]

## Core result structure

The binary quantum carrier supplies

\[
\mathfrak g_{\rm rel}=\operatorname{Herm}_0(2)
\cong\mathbb R^3
\]

with canonical inner product

\[
\langle A,B\rangle=\frac12\operatorname{Tr}(AB)
\]

and adjoint rotational symmetry

\[
SU(2)/\{\pm I\}\cong SO(3).
\]

`SPATIAL_PROMOTION_UNIQUENESS_V0_1.md` proves the following conditional uniqueness statement: a minimal nonzero finite-dimensional real carrier that faithfully and orthogonally realizes the full primitive `SO(3)` symmetry has dimension three and is equivalent, up to orthogonal frame change, to the defining rotation representation. Therefore

\[
\boxed{
V_x\simeq\operatorname{Herm}_0(2)\simeq\mathbb R^3
}
\]

under the declared spatial-realization criterion, with invariant positive metric unique up to scale.

The central active gate is now to derive that realization criterion from the primitive TIR axioms.

## Minimal spatial cell

For a three-dimensional affine carrier, the minimal full-dimensional simplex has four vertices:

\[
\boxed{\Delta^3.}
\]

Under equal norm and full local isotropy,

\[
\sum_{a=1}^{4}n_a=0,
\qquad
n_a\cdot n_b=-\frac13\quad(a\ne b),
\]

so the minimal isotropic full-dimensional cell is the regular tetrahedron.

The tetrahedral qubit SIC remains an independent information-theoretic convergence check on the same finite structure.

## Euclidean endpoint

For local displacements `A,B`,

\[
\|A+B\|^2
=\|A\|^2+\|B\|^2+2\langle A,B\rangle.
\]

With

\[
A\perp B
\iff
\langle A,B\rangle=0,
\]

this gives

\[
\boxed{a^2+b^2=c^2.}
\]

This is the endpoint of the fundamental paper.

## Global geometry boundary

For a regular tetrahedron

\[
\theta_T=\arccos(1/3)
\]

and

\[
5\theta_T<2\pi<6\theta_T.
\]

Thus the regular tetrahedron is used as the minimal local isotropic cell. Global flat/curved continuum construction is treated as a downstream refinement problem rather than a prerequisite for Pythagorean closure.

## Current surfaces

- `RESEARCH_SPINE_V0_2.md`
- `foundations/SPATIAL_PROMOTION_UNIQUENESS_V0_1.md`
- `foundations/LOCAL_EUCLIDEAN_PYTHAGOREAN_CLOSURE_V0_1.md`
- `paper/PAPER_OUTLINE_V0_2.md`
- deterministic validation under `validation/`

TIR remains the parent Source of Truth for the primitive axioms, first-distinction theorem, generator construction, tetrahedral isotropy and endpoint-closure results.
