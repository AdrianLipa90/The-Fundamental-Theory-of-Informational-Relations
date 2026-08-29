# The Space of Geometry

Status: `TIR_SUBREPO_RESEARCH_PROGRAM_V0_5`

Working title:

> **The Space of Geometry: From First Distinction to Pythagoras**

This TIR subrepo develops the shortest local spatial-geometric derivation from the primitive quantum point to Pythagorean closure.

The current shortest spine is

\[
\boxed{
0
\to P
\to \text{DISTINCTION}
\to \mathbb C^2
\to \rho_x
\to \mathcal A_2=\frac12 I+\operatorname{Herm}_0(2)
\to \text{source-minimal intrinsic relation}
\to \rho_y-\rho_x
\to \operatorname{Herm}_0(2)\cong\mathbb R^3
\to \Delta^3
\to \text{distance / angle / orthogonality}
\to a^2+b^2=c^2.
}
\]

## Core result structure

The binary quantum carrier gives normalized point states

\[
\rho_x=\frac12(I+\mathbf r_x\cdot\boldsymbol\sigma)
\]

whose trace-one Hermitian affine hull is

\[
\boxed{
\mathcal A_2=\frac12I+\operatorname{Herm}_0(2).
}
\]

The translation space is therefore

\[
\boxed{
\operatorname{Herm}_0(2)\cong\mathbb R^3.
}
\]

An affine space is a torsor for its translation space. Hence every ordered pair has a unique origin-independent displacement

\[
\boxed{
\delta(\rho_x,\rho_y)=\rho_y-\rho_x.
}
\]

With the Pauli normalization used in TIR,

\[
\boxed{
\mathcal E_{xy}=2(\rho_y-\rho_x)
=(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma.
}
\]

This exact affine construction gives reversal, endpoint composition and triangular closure automatically:

\[
\mathcal E_{yx}=-\mathcal E_{xy},
\qquad
\mathcal E_{xz}=\mathcal E_{xy}+\mathcal E_{yz}.
\]

The invariant quadratic metric is

\[
\boxed{
\langle A,B\rangle=\frac12\operatorname{Tr}(AB),
}
\]

with

\[
\|\mathcal E_{xy}\|^2=|\mathbf r_y-\mathbf r_x|^2.
\]

## Source-minimal relation theorem

The primitive relation-law signature at this layer contains only

\[
(\rho_x,\rho_y;\mathcal A_2,V).
\]

If no independent origin, axis, basis or background tensor is introduced, the law is intrinsic to the affine pair and therefore natural under affine frame changes

\[
F(x)=Lx+a.
\]

Every continuous affine-natural vector relation then has the exact form

\[
\boxed{R(x,y)=c(y-x).}
\]

A3 distinction preservation requires

\[
\boxed{c\ne0.}
\]

Thus state-difference geometry is unique up to global unit and orientation once the primitive relation signature is source-minimal. If the relation is typed as the actual torsor translation, its intrinsic normalization is `c=1`; the Pauli generator convention displays the same relation with factor `2` relative to density-operator difference.

## Minimal spatial cell

For a three-dimensional affine carrier, the minimal full-dimensional simplex is

\[
\boxed{\Delta^3.}
\]

Under the registered local symmetry/equivalence condition,

\[
\sum_{a=1}^{4}n_a=0,
\qquad
n_a\cdot n_b=-\frac13\quad(a\ne b),
\]

so the minimal isotropic cell is the regular tetrahedron.

The same four pure-state directions are also a minimal affine frame of the normalized qubit-state hull and the tetrahedral qubit SIC frame.

## Euclidean endpoint

For local relation displacements `A,B`,

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

## Current foundational gate

The local mathematical chain is exact after one narrow TIR inheritance rule:

\[
\boxed{
\texttt{A1\_DEPENDENCY\_MINIMALITY\_APPLIES\_TO\_PRIMITIVE\_LAW\_SIGNATURE}.
}
\]

Operationally: A1 minimality is inherited by the first primitive relation law, so that this law may use only structure already sourced upstream. Together with A3 relational primacy this selects a source-minimal intrinsic relation; affine naturality then fixes it to `c(y-x)`.

A5 supplies the arithmetic measurement layer through invariants such as `Tr(E^2)/2`. A8 acts as the consistency/context-lift layer: local affine endpoint closure is exact, while nontrivial loop/context defects are retained for downstream curvature and holonomy.

## Global geometry boundary

For a regular tetrahedron

\[
\theta_T=\arccos(1/3),
\qquad
5\theta_T<2\pi<6\theta_T.
\]

The tetrahedron is therefore used as the minimal local isotropic cell. Global refinement, curvature, holonomy, torsion sectors and the TIR x Time spacetime join remain downstream.

## Current surfaces

- `RESEARCH_SPINE_V0_5.md`
- `foundations/QUANTUM_POINT_AFFINE_SPATIAL_CARRIER_V0_1.md`
- `foundations/RELATIONAL_STATE_DIFFERENCE_UNIQUENESS_V0_1.md`
- `foundations/QUANTUM_RELATION_AFFINE_TORSOR_V0_1.md`
- `foundations/A1_A3_INTRINSIC_AFFINE_RELATION_V0_1.md`
- `foundations/A1_A3_SOURCE_MINIMALITY_NATURALITY_V0_1.md`
- `foundations/SPATIAL_PROMOTION_UNIQUENESS_V0_1.md`
- `foundations/RELATIONAL_COCYCLE_AFFINE_CLOSURE_V0_1.md`
- `foundations/LOCAL_EUCLIDEAN_PYTHAGOREAN_CLOSURE_V0_1.md`
- deterministic validation under `validation/`

TIR remains the parent Source of Truth for the primitive axioms, first-distinction theorem, quantum-point carrier, tetrahedral isotropy and closure crosslinks.
