# Spatial Promotion Uniqueness v0.1

Status: `EXACT_CONDITIONAL_SPATIAL_PROMOTION_THEOREM_CANDIDATE`

Scope: local TIR geometry. This note replaces a bare identification of `Herm_0(2)` with physical spatial directions by a representation-theoretic uniqueness statement under an explicit minimal spatial-realization criterion.

## 1. Imported primitive carrier

The first binary quantum carrier gives

\[
\mathcal H_2\cong\mathbb C^2
\]

and its traceless Hermitian generator space

\[
\boxed{
\mathfrak g_{\rm rel}=\operatorname{Herm}_0(2)
=\operatorname{span}_{\mathbb R}\{\sigma_x,\sigma_y,\sigma_z\}.
}
\]

Conjugation by `SU(2)` induces

\[
\operatorname{Ad}:SU(2)\to SO(3),
\qquad
SU(2)/\{\pm I\}\cong SO(3),
\]

and preserves

\[
\langle A,B\rangle_{\rm HS}=\frac12\operatorname{Tr}(AB).
\]

Thus `g_rel` is an exact real three-dimensional orthogonal carrier of the primitive adjoint rotational symmetry.

## 2. Spatial realization criterion

Let `V_x` denote the local real carrier in which physical relational displacements at a locus `x` are represented.

The candidate realization criterion is:

1. `V_x` is finite-dimensional and real;
2. the full primitive rotational symmetry `PSU(2) ~= SO(3)` acts continuously and orthogonally on `V_x`;
3. the action is faithful, so distinct primitive rotations remain distinct on local spatial directions;
4. `V_x` is minimal among nonzero real carriers satisfying 1--3.

These four requirements define the gate to be derived from the TIR axioms. Once admitted, the carrier dimension is fixed.

## 3. Minimal faithful dimension theorem

### One real dimension

A connected group acting continuously through `O(1)={+1,-1}` has connected image contained in the identity component. Hence the image is trivial. A faithful `SO(3)` action cannot occur in one real dimension.

### Two real dimensions

The image of connected `SO(3)` under a continuous orthogonal representation into `O(2)` lies in the identity component

\[
SO(2),
\]

which is abelian. Since `SO(3)` is nonabelian and perfect,

\[
[SO(3),SO(3)]=SO(3),
\]

any homomorphism from `SO(3)` into an abelian group has trivial image. Hence a faithful two-dimensional real orthogonal representation is excluded.

### Three real dimensions

The defining rotation representation

\[
SO(3)\hookrightarrow GL(3,\mathbb R)
\]

is faithful and orthogonal.

Therefore

\[
\boxed{
\dim_{\mathbb R}V_x=3
}
\]

for the minimal faithful real orthogonal spatial realization.

## 4. Uniqueness at minimal dimension

A faithful continuous three-dimensional orthogonal representation of connected `SO(3)` has image in `SO(3)`. Its Lie algebra map is an injective map

\[
\mathfrak{so}(3)\to\mathfrak{so}(3).
\]

Both Lie algebras have dimension three, so the map is an isomorphism. The resulting representation is equivalent, up to orthogonal change of frame, to the defining three-dimensional rotation representation.

Hence the minimal spatial carrier is unique up to orthogonal equivalence:

\[
\boxed{
V_x\cong\mathbb R^3.
}
\]

Because the adjoint action on `Herm_0(2)` is exactly this representation,

\[
\boxed{
V_x\cong\operatorname{Herm}_0(2)
}
\]

as real `SO(3)` representation spaces.

This is the promotion theorem in representation-theoretic form.

## 5. Metric uniqueness up to scale

The defining real representation of `SO(3)` is irreducible. Therefore an invariant positive-definite inner product is unique up to a positive scalar factor.

The generator carrier already supplies

\[
\boxed{
\langle A,B\rangle
=\frac12\operatorname{Tr}(AB).
}
\]

Thus every minimal faithful isotropic spatial realization has metric

\[
\boxed{
h_x=\lambda_x\,\langle\cdot,\cdot\rangle_{\rm HS},
\qquad \lambda_x>0.
}
\]

For the dimensionless local geometry used in this subrepo, choose the canonical Pauli normalization `lambda_x=1`. A physical unit scale is a downstream calibration layer.

## 6. Exact conditional theorem

### Theorem — minimal faithful spatial promotion

If local physical relational directions are required to form the minimal nonzero finite-dimensional real carrier that faithfully and orthogonally realizes the full primitive `PSU(2) ~= SO(3)` symmetry, then

\[
\boxed{
V_x\simeq\operatorname{Herm}_0(2)\simeq\mathbb R^3
}
\]

and its invariant positive metric is unique up to scale.

Consequently the earlier spatial promotion gate is reduced to one sharply typed physical question:

\[
\boxed{
\text{derive the minimal faithful real orthogonal realization criterion from the primitive TIR axioms.}
}
\]

## 7. Consequence for the tetrahedral cell

Once the theorem criterion is admitted,

\[
\dim V_x=3.
\]

The minimal full-dimensional affine simplex therefore has four vertices:

\[
\boxed{\Delta^3.}
\]

Under equal weighting and full local isotropy, the four center-to-vertex directions obey

\[
\sum_{a=1}^{4}n_a=0,
\qquad
n_a\cdot n_b=-\frac13\quad(a\ne b),
\]

so the minimal isotropic cell is the regular tetrahedron.

## 8. Claim classes

| Statement | Class |
|---|---|
| no faithful continuous orthogonal `SO(3)` carrier exists in real dimension 1 | EXACT GROUP THEORY |
| no faithful continuous orthogonal `SO(3)` carrier exists in real dimension 2 | EXACT GROUP THEORY |
| the defining real `SO(3)` carrier is faithful in dimension 3 | EXACT |
| minimal faithful real orthogonal carrier dimension is 3 | EXACT |
| `Herm_0(2)` realizes that carrier through `Ad SU(2)` | EXACT REPRESENTATION THEORY |
| invariant positive metric is unique up to scale | EXACT CONDITIONAL / SCHUR-TYPE UNIQUENESS |
| physical spatial directions satisfy the realization criterion | TIR DERIVATION GATE |
| spatial promotion follows once the criterion is admitted | EXACT CONDITIONAL |
