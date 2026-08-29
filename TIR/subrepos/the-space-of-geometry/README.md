# The Space of Geometry

Status: `TIR_SUBREPO_LOCAL_DERIVATION_CLOSED_V0_8_CANDIDATE`

Working title:

> **The Space of Geometry: From First Distinction to Pythagoras**

This TIR subrepo develops the shortest local spatial-geometric construction from the primitive binary quantum point to Pythagorean closure.

The current spine is

\[
\boxed{
0
\to P
\to \text{DISTINCTION}
\to \mathbb C^2
\to \rho_x
\to \mathcal A_2=\frac12I+\operatorname{Herm}_0(2)
\to \delta(\rho_x,\rho_y)=\rho_y-\rho_x
\to \operatorname{Herm}_0(2)\cong\mathbb R^3
\to \Delta^3
\to \operatorname{Aut}(\Delta^3)=S_4
\xrightarrow{A5+A7}
\text{regular tetrahedron}
\to \text{distance / angle / orthogonality}
\to a^2+b^2=c^2.
}
\]

## Canonical spatial relation

The normalized two-level quantum state hull is

\[
\mathcal A_2=\frac12I+V,
\qquad
V=\operatorname{Herm}_0(2).
\]

Every ordered pair has a unique endpoint-carrying affine displacement

\[
\boxed{
\rho_x+\delta_{xy}=\rho_y,
\qquad
\delta_{xy}=\rho_y-\rho_x.
}
\]

The spatial branch exports this canonical torsor displacement as its primitive vector relation. In the established generator normalization,

\[
\boxed{
\mathcal E_{xy}=2(\rho_y-\rho_x)
=(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma.
}
\]

This immediately gives reversal, endpoint composition and triangular closure.

Because trace normalization removes one real dimension from `Herm(2)`,

\[
\boxed{
\dim_{\mathbb R}\operatorname{Herm}_0(2)=3,
}
\]

so the canonical relation carrier is

\[
\boxed{V\cong\mathbb R^3.}
\]

The parent `SU(2)` conjugation induces the standard

\[
PSU(2)\cong SO(3)
\]

action on this carrier.

## Metric

The positive invariant quadratic form is unique up to global scale. With Pauli normalization,

\[
\boxed{
\langle A,B\rangle=\frac12\operatorname{Tr}(AB).
}
\]

Hence

\[
\boxed{
\|\mathcal E_{xy}\|^2
=\frac12\operatorname{Tr}(\mathcal E_{xy}^2)
=|\mathbf r_y-\mathbf r_x|^2.
}
\]

A5 types this arithmetic invariant as geometric measure.

## Minimal cell

For `m` affine points,

\[
\dim\operatorname{Aff}\{x_1,\ldots,x_m\}\le m-1.
\]

Three-dimensional full support therefore requires

\[
\boxed{m\ge4.}
\]

and the minimum cell is

\[
\boxed{\Delta^3.}
\]

Tetrahedrality follows from three-dimensionality plus minimal full-dimensional affine support.

## A5+A7 regularity closure

The abstract unlabeled 3-simplex has

\[
\boxed{\operatorname{Aut}(\Delta^3)\cong S_4.}
\]

Its six edges form one `S_4` orbit. For every edge relation define

\[
q_{ij}=\frac12\operatorname{Tr}(\mathcal E_{ij}^2),
\qquad
\ell_{ij}=\sqrt{q_{ij}}.
\]

A7 law invariance on the intrinsic simplex automorphism action gives

\[
\boxed{
q_{\pi(i)\pi(j)}=q_{ij}
\qquad
\forall\pi\in S_4.
}
\]

One edge orbit therefore means one edge measure:

\[
q_{ij}=q_*,
\qquad
\ell_{ij}=\ell_*.
\]

All six tetrahedral edges are equal, so the cell is regular.

Thus the preferred shortest regularity route is

\[
\boxed{
\mathbb R^3
\to
\Delta^3
\xrightarrow{A5+A7}
\text{regular tetrahedron}.
}
\]

The earlier maximal-symmetry and moment-isotropy derivations remain independent crosschecks.

For centered normalized directions,

\[
\boxed{
\sum_{a=1}^{4}n_a=0,
\qquad
n_a\cdot n_b=-\frac13\quad(a\ne b),
}
\]

and

\[
\boxed{
\sum_an_an_a^T=\frac43I_3.
}
\]

The orientation-preserving rotational subgroup is

\[
A_4\subset SO(3),
\]

with binary tetrahedral lift

\[
2T\subset SU(2).
\]

The same four directions form the tetrahedral qubit SIC frame, giving an independent informational convergence on the same Gram geometry.

## Pythagorean endpoint

For local relation vectors `A,B`,

\[
\|A+B\|^2
=\|A\|^2+\|B\|^2+2\langle A,B\rangle.
\]

Orthogonality is

\[
A\perp B
\iff
\langle A,B\rangle=0.
\]

Therefore

\[
\boxed{a^2+b^2=c^2.}
\]

This is the endpoint of the fundamental paper.

## Status boundary

The local branch from the imported binary quantum-point carrier to Pythagorean closure is now closed at the TIR axiom/model level through canonical affine construction, standard representation theory, minimal simplex geometry and the A5+A7 intrinsic edge-orbit symmetry rule.

The upstream first-distinction construction remains parent TIR provenance. Global triangulation, curvature, holonomy, torsion sectors, physical scale calibration and the TIR x Time spacetime join remain downstream programmes.

## Current surfaces

- `RESEARCH_SPINE_V0_8.md`
- `foundations/CANONICAL_SPATIAL_RELATION_EXTRACTION_V0_1.md`
- `foundations/A5_A7_SIMPLEX_EDGE_ORBIT_REGULARITY_V0_1.md`
- `foundations/UNLABELED_SIMPLEX_AUTOMORPHISM_REGULARITY_V0_1.md`
- `foundations/LOCAL_EUCLIDEAN_PYTHAGOREAN_CLOSURE_V0_1.md`
- `validation/space_of_geometry_spine_v0_8.py`
- deterministic validation under `validation/`

TIR remains the parent Source of Truth for the primitive axioms, first-distinction theorem and binary quantum carrier.
