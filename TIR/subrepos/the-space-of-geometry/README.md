# The Space of Geometry

Status: `TIR_SUBREPO_RESEARCH_PROGRAM_V0_6`

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
\to \operatorname{Aut}^+(\Delta^3)=A_4
\to \text{regular tetrahedral frame}
\to \text{distance / angle / orthogonality}
\to a^2+b^2=c^2.
}
\]

## Quantum-point affine carrier

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

Its translation space is

\[
\boxed{
V=\operatorname{Herm}_0(2)\cong\mathbb R^3.
}
\]

Every ordered pair has the intrinsic torsor displacement

\[
\boxed{
\delta(\rho_x,\rho_y)=\rho_y-\rho_x.
}
\]

With the established Pauli normalization,

\[
\boxed{
\mathcal E_{xy}=2(\rho_y-\rho_x)
=(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma.
}
\]

This gives reversal, endpoint composition and triangular closure exactly.

## Source-minimal relation theorem

If the primitive relation-law signature contains only the ordered endpoints and their admitted affine carrier, with no independent origin, axis, basis or background tensor, the law is natural under affine changes of frame. Every continuous affine-natural vector relation is

\[
\boxed{R(x,y)=c(y-x).}
\]

A3 distinction preservation requires

\[
\boxed{c\ne0.}
\]

The torsor translation fixes `c=1` intrinsically. The Pauli generator convention displays the same displacement with factor `2` relative to density-operator difference.

The remaining source inheritance gate is

\[
\boxed{
\texttt{A1\_DEPENDENCY\_MINIMALITY\_APPLIES\_TO\_PRIMITIVE\_LAW\_SIGNATURE}.
}
\]

## Minimal simplex and intrinsic symmetry

For a three-dimensional affine carrier,

\[
\dim\operatorname{Aff}\{x_1,\ldots,x_m\}\le m-1
\]

forces

\[
\boxed{m\ge4.}
\]

At the minimum the cell is the 3-simplex

\[
\boxed{\Delta^3.}
\]

The abstract unlabeled simplex has

\[
\boxed{\operatorname{Aut}(\Delta^3)\cong S_4}
\]

and, after orientation is fixed,

\[
\boxed{\operatorname{Aut}^+(\Delta^3)\cong A_4.}
\]

If this intrinsic oriented automorphism group is faithfully realized by Euclidean isometries, `A_4` acts transitively on all six edges. Hence all six edge lengths are equal and the simplex is regular.

Thus regularity follows from

\[
\boxed{
\Delta^3
+
\text{faithful isometric realization of intrinsic }A_4
\to
\text{regular tetrahedron}.
}
\]

This replaces equal-weight/moment-isotropy as the preferred primary regularity route. The moment identities become consequences:

\[
\sum_{a=1}^{4}n_a=0,
\qquad
n_a\cdot n_b=-\frac13\quad(a\ne b),
\]

\[
\boxed{
\sum_an_an_a^T=\frac43I_3.
}
\]

The remaining symmetry inheritance gate is

\[
\boxed{
\texttt{A3+A7\_FAITHFULLY\_REALIZE\_INTRINSIC\_ORIENTED\_SIMPLEX\_AUTOMORPHISMS\_ISOMETRICALLY}.
}
\]

The regular tetrahedral rotation group sits inside the parent carrier symmetry as

\[
A_4\subset SO(3)\cong PSU(2),
\]

with binary tetrahedral lift

\[
2T\subset SU(2).
\]

The same tetrahedral directions remain an independent qubit informational-completeness convergence check.

## Euclidean endpoint

The invariant relation metric is

\[
\boxed{
\langle A,B\rangle=\frac12\operatorname{Tr}(AB)
}
\]

up to global physical scale.

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

## Current proof frontier

The local mathematics is now theorem-driven after two narrowly isolated TIR inheritance rules:

\[
G_1:\ A1\ \text{minimality propagates to the primitive relation-law signature},
\]

\[
G_2:\ A3+A7\ \text{faithfully realize intrinsic oriented simplex automorphisms isometrically}.
\]

A5 occupies the arithmetic measurement layer through invariants such as `Tr(E^2)/2`. A8 acts as the consistency/context-lift layer when multiple local frames or nontrivial holonomy are compared.

## Global geometry boundary

For a regular tetrahedron

\[
\theta_T=\arccos(1/3),
\qquad
5\theta_T<2\pi<6\theta_T.
\]

The tetrahedron is used as a minimal local frame rather than as a pure regular-tetrahedral Euclidean honeycomb. Global refinement, curvature, holonomy, torsion sectors and the TIR x Time spacetime join remain downstream.

## Current surfaces

- `RESEARCH_SPINE_V0_6.md`
- `foundations/QUANTUM_POINT_AFFINE_SPATIAL_CARRIER_V0_1.md`
- `foundations/QUANTUM_RELATION_AFFINE_TORSOR_V0_1.md`
- `foundations/A1_A3_SOURCE_MINIMALITY_NATURALITY_V0_1.md`
- `foundations/MINIMAL_SIMPLEX_MAXIMAL_SYMMETRY_V0_1.md`
- `foundations/UNLABELED_SIMPLEX_AUTOMORPHISM_REGULARITY_V0_1.md`
- `foundations/LOCAL_EUCLIDEAN_PYTHAGOREAN_CLOSURE_V0_1.md`
- deterministic validation under `validation/`

TIR remains the parent Source of Truth for the primitive axioms, first-distinction theorem, quantum-point carrier and spatial closure crosslinks.
