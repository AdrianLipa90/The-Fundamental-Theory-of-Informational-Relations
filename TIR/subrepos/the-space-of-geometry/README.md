# The Space of Geometry

Status: `TIR_SUBREPO_LOCAL_DEPENDENCY_FORK_V0_9_CANDIDATE`

Working title:

> **The Space of Geometry: From First Distinction to Pythagoras**

This TIR subrepo develops a local relation geometry from the primitive binary quantum point and separates two consequences of the same three-dimensional carrier: direct Euclidean/Pythagorean closure and the minimal finite tetrahedral cell.

## Current dependency graph

The common carrier is

\[
\boxed{
0
\to P
\to \text{DISTINCTION}
\to \mathbb C^2
\to \rho_x
\to \mathcal A_2=\frac12I+\operatorname{Herm}_0(2)
\to \delta(\rho_x,\rho_y)=\rho_y-\rho_x
\to V=\operatorname{Herm}_0(2)\cong\mathbb R^3.
}
\]

From `V`, the derivation forks:

\[
\boxed{
V
\to
\begin{cases}
\text{invariant inner product}
\to
\text{distance / angle / orthogonality}
\to
\boxed{a^2+b^2=c^2},\\[2mm]
\text{minimal finite full-dimensional support}
\to
\Delta^3
\xrightarrow{A5+A7}
\text{regular tetrahedron}
\to
\text{tetrahedral Gram/SIC convergence}.
\end{cases}
}
\]

The tetrahedron is therefore the minimal finite-cell theorem of the three-dimensional carrier. Pythagorean closure follows directly from the Euclidean inner-product branch.

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

The spatial branch exports this canonical torsor displacement as its primitive vector relation. In Pauli generator normalization,

\[
\boxed{
\mathcal E_{xy}=2(\rho_y-\rho_x)
=(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma.
}
\]

This gives exactly

\[
\mathcal E_{yx}=-\mathcal E_{xy},
\qquad
\mathcal E_{xz}=\mathcal E_{xy}+\mathcal E_{yz},
\]

and triangular endpoint closure.

Because `Herm(2)` has four real dimensions and trace normalization removes one,

\[
\boxed{
\dim_{\mathbb R}V=3.
}
\]

## Euclidean branch

The parent `SU(2)` conjugation action induces

\[
PSU(2)\cong SO(3)
\]

on `V`. The positive invariant inner product is unique up to global scale. With Pauli normalization,

\[
\boxed{
\langle A,B\rangle=\frac12\operatorname{Tr}(AB).
}
\]

For relation vectors,

\[
\boxed{
\|\mathcal E_{xy}\|^2
=|\mathbf r_y-\mathbf r_x|^2.
}
\]

Endpoint composition supplies `C=A+B`. Hence

\[
\|A+B\|^2
=\|A\|^2+\|B\|^2+2\langle A,B\rangle.
\]

With

\[
A\perp B\iff\langle A,B\rangle=0,
\]

we obtain directly

\[
\boxed{a^2+b^2=c^2.}
\]

This is the principal endpoint of the fundamental paper.

## Minimal finite-cell branch

For `m` affine points,

\[
\dim\operatorname{Aff}\{x_1,\ldots,x_m\}\le m-1.
\]

Full support of a three-dimensional affine carrier requires

\[
\boxed{m\ge4.}
\]

At the minimum,

\[
\boxed{\Delta^3.}
\]

The abstract unlabeled 3-simplex has

\[
\boxed{\operatorname{Aut}(\Delta^3)\cong S_4,}
\]

and its six edges form one automorphism orbit.

Define the edge measure

\[
q_{ij}=\frac12\operatorname{Tr}(\mathcal E_{ij}^2),
\qquad
\ell_{ij}=\sqrt{q_{ij}}.
\]

A5 types `q_ij` as arithmetic geometric measure. A7 invariance of the edge-measure law under the intrinsic simplex automorphism action gives

\[
q_{\pi(i)\pi(j)}=q_{ij}.
\]

One edge orbit therefore gives one edge length. All six tetrahedral edges are equal, so the simplex is regular:

\[
\boxed{
\mathbb R^3
\to
\Delta^3
\xrightarrow{A5+A7}
\text{regular tetrahedron}.
}
\]

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

## Independent informational convergence

A qubit has three independent real Bloch coordinates. A normalized `m`-outcome probability vector has at most `m-1` independent real values, so informational completeness requires

\[
\boxed{m\ge4.}
\]

The minimal symmetric rank-one qubit frame is tetrahedral and obeys the same Gram relation

\[
\boxed{n_a\cdot n_b=-\frac13.}
\]

Thus the spatial finite-cell branch and the qubit measurement branch independently converge on the same regular tetrahedral frame geometry while retaining separate physical typing.

## Global geometry boundary

For a regular tetrahedron

\[
\theta_T=\arccos(1/3),
\qquad
5\theta_T<2\pi<6\theta_T.
\]

The tetrahedron is used as a minimal local finite frame. Global triangulation, curvature, holonomy, torsion sectors, physical scale calibration and the TIR x Time spacetime join remain downstream.

## Current surfaces

- `RESEARCH_SPINE_V0_9.md`
- `foundations/CANONICAL_SPATIAL_RELATION_EXTRACTION_V0_1.md`
- `foundations/A5_A7_SIMPLEX_EDGE_ORBIT_REGULARITY_V0_1.md`
- `foundations/UNLABELED_SIMPLEX_AUTOMORPHISM_REGULARITY_V0_1.md`
- `foundations/LOCAL_EUCLIDEAN_PYTHAGOREAN_CLOSURE_V0_1.md`
- `paper/MANUSCRIPT_V0_2.md`
- `validation/space_of_geometry_spine_v0_9.py`
- deterministic validation under `validation/`

TIR remains the parent Source of Truth for the primitive axioms, first-distinction theorem and binary quantum carrier.
