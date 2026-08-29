# The Space of Geometry — Research Spine v0.9

Status: `TIR_SPACE_OF_GEOMETRY_LOCAL_DEPENDENCY_FORK_V0_9_CANDIDATE`

## 1. Dependency correction

After the canonical three-real-dimensional relation carrier is obtained, local Euclidean closure and the minimal finite-cell theorem are parallel consequences.

The exact dependency graph is

\[
\boxed{
\text{FIRST DISTINCTION}
\to
\mathbb C^2
\to
\rho_x
\to
\mathcal A_2
\to
\delta(\rho_x,\rho_y)
\to
V=\operatorname{Herm}_0(2)\cong\mathbb R^3
}
\]

followed by the fork

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

This keeps theorem dependency exact: the tetrahedral finite-cell theorem is a derived local geometry result, while Pythagorean closure follows directly from the Euclidean inner-product carrier.

## 2. Canonical relation carrier

For the normalized binary quantum-point state hull,

\[
\mathcal A_2=\frac12I+V,
\qquad
V=\operatorname{Herm}_0(2),
\]

every ordered pair has the unique endpoint-carrying affine displacement

\[
\boxed{
\delta_{xy}=\rho_y-\rho_x.
}
\]

The generator-normalized relation is

\[
\boxed{
\mathcal E_{xy}=2(\rho_y-\rho_x)
=(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma.
}
\]

Trace normalization gives

\[
\boxed{\dim_{\mathbb R}V=3.}
\]

## 3. Euclidean branch

The `SU(2)` conjugation action induces `SO(3)` on `V`. The positive invariant inner product is unique up to scale and in Pauli normalization is

\[
\boxed{
\langle A,B\rangle=\frac12\operatorname{Tr}(AB).
}
\]

Hence

\[
\|\mathcal E_{xy}\|^2
=|\mathbf r_y-\mathbf r_x|^2.
\]

Affine endpoint composition gives

\[
\mathcal E_{xz}=\mathcal E_{xy}+\mathcal E_{yz}.
\]

For consecutive relation vectors `A,B`,

\[
\|A+B\|^2
=\|A\|^2+\|B\|^2+2\langle A,B\rangle.
\]

With

\[
A\perp B\iff\langle A,B\rangle=0,
\]

we obtain

\[
\boxed{a^2+b^2=c^2.}
\]

This is the direct local Euclidean endpoint.

## 4. Minimal finite-cell branch

The same real dimension three implies that a full-dimensional affine simplex requires at least four vertices:

\[
\boxed{m\ge4.}
\]

At the minimum,

\[
\boxed{\Delta^3.}
\]

The abstract simplex has

\[
\operatorname{Aut}(\Delta^3)\cong S_4,
\]

and all six edges lie in one automorphism orbit.

For

\[
q_{ij}=\frac12\operatorname{Tr}(\mathcal E_{ij}^2),
\]

A5 provides the arithmetic geometric measure and A7 gives invariance of the edge-measure law under the intrinsic simplex automorphism action. Therefore

\[
q_{ij}=q_*
\]

for all six edges. Thus

\[
\boxed{\Delta^3\to\text{regular tetrahedron}.}
\]

## 5. Tetrahedral invariants

For centered normalized directions,

\[
\boxed{
\sum_{a=1}^{4}n_a=0,
\qquad
n_a\cdot n_b=-\frac13\quad(a\ne b),
}
\]

with

\[
\boxed{
G=\frac43I_4-\frac13\mathbf1\mathbf1^T
}
\]

and

\[
\boxed{
\sum_an_an_a^T=\frac43I_3.
}
\]

The oriented rotational subgroup is `A_4 subset SO(3)` and its `SU(2)` lift is `2T`.

## 6. Informational convergence

The qubit has three real Bloch parameters, so normalized informational completeness requires at least four outcomes. The minimal symmetric rank-one frame is tetrahedral and has the same Gram relation

\[
\boxed{n_a\cdot n_b=-\frac13.}
\]

Thus the finite-cell branch and qubit informational branch independently converge on one tetrahedral tight-frame geometry.

## 7. Paper architecture

The manuscript should present two theorems after the common carrier theorem:

**Theorem E — Local Euclidean closure.** The canonical affine relation carrier of normalized binary quantum points is a three-real-dimensional inner-product space with additive endpoint composition, hence supports the Pythagorean norm identity.

**Theorem T — Minimal finite cell.** Minimal full-dimensional finite support of the same carrier is a 3-simplex; A5+A7 invariance on its intrinsic edge orbit makes it regular.

The informational SIC result is then an independent convergence theorem on the same regular tetrahedral Gram frame.

## 8. Status boundary

The common carrier theorem, Euclidean branch, and finite-cell branch are locally closed at the TIR axiom/model level. Global triangulation, curvature, holonomy, torsion sectors, physical scale calibration and the TIR x Time spacetime join remain downstream programmes.
