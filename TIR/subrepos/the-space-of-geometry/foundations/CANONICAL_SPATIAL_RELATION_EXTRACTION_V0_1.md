# Canonical Spatial Relation Extraction v0.1

Status: `EXACT_CANONICAL_AFFINE_SPATIAL_RELATION_CONSTRUCTION`

Scope: replace the source-minimality inheritance gate by an explicit canonical construction for the spatial branch. The construction extracts the unique affine displacement carried by an ordered pair of normalized quantum-point states.

## 1. Parent affine carrier

For the binary quantum point,

\[
\rho=\rho^\dagger,
\qquad
\operatorname{Tr}\rho=1,
\]

and the normalized two-level state hull is

\[
\boxed{
\mathcal A_2=\frac12I+V,
\qquad
V=\operatorname{Herm}_0(2)\cong\mathbb R^3.
}
\]

The affine space `A_2` is a torsor for `V`.

## 2. Unique endpoint-carrying relation

For every ordered pair

\[
(\rho_x,\rho_y)\in\mathcal A_2\times\mathcal A_2,
\]

there exists a unique vector

\[
\delta_{xy}\in V
\]

such that

\[
\boxed{
\rho_x+\delta_{xy}=\rho_y.
}
\]

By freeness of the translation action,

\[
\boxed{
\delta_{xy}=\rho_y-\rho_x.
}
\]

This construction requires only the two endpoints and their already admitted affine carrier.

## 3. Canonical naturality

For an affine isomorphism

\[
F(\rho)=L\rho+a
\]

with linear part `L`,

\[
\boxed{
\delta(F\rho_x,F\rho_y)=L\,\delta(\rho_x,\rho_y).
}
\]

Hence the endpoint-carrying displacement is functorial under affine frame changes.

It also obeys exactly

\[
\boxed{\delta_{yx}=-\delta_{xy},}
\]

\[
\boxed{\delta_{xz}=\delta_{xy}+\delta_{yz},}
\]

and

\[
\boxed{\delta_{xy}+\delta_{yz}+\delta_{zx}=0.}
\]

## 4. Spatial branch definition

Define the primitive vector relation exported by the TIR spatial branch as the canonical endpoint-carrying affine displacement of the quantum-point carrier:

\[
\boxed{
\mathfrak e_{xy}:=\delta(\rho_x,\rho_y)=\rho_y-\rho_x.
}
\]

The generator-normalized version is

\[
\boxed{
\mathcal E_{xy}:=2\mathfrak e_{xy}.
}
\]

Using

\[
\rho_x=\frac12(I+\mathbf r_x\cdot\boldsymbol\sigma),
\]

this becomes

\[
\boxed{
\mathcal E_{xy}
=(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma
\in\operatorname{Herm}_0(2).
}
\]

Thus the spatial branch has a canonical relation object before any coordinate origin, preferred axis or external spatial manifold is introduced.

## 5. Three-dimensionality

Because

\[
\dim_{\mathbb R}\operatorname{Herm}(2)=4
\]

and the trace-one condition has real codimension one,

\[
\boxed{
\dim_{\mathbb R}V=3.
}
\]

Therefore the canonical local vector relation carrier is

\[
\boxed{
V\cong\operatorname{Herm}_0(2)\cong\mathbb R^3.
}
\]

This is now a construction theorem for the spatial branch rather than a separate physical promotion map into a previously postulated tangent space.

## 6. Metric

The parent `SU(2)` action acts by conjugation on `V`:

\[
A\mapsto UAU^\dagger.
\]

The positive invariant quadratic form is, up to overall scale,

\[
\boxed{
\langle A,B\rangle
=\frac12\operatorname{Tr}(AB).
}
\]

In Pauli coefficients,

\[
\boxed{
\|\mathcal E_{xy}\|^2
=|\mathbf r_y-\mathbf r_x|^2.
}
\]

A5 reads the resulting arithmetic invariant as geometric measure.

## 7. Dependency status

The spatial construction requires the upstream binary quantum-point affine carrier and standard affine geometry. Its primitive vector relation is fixed by the endpoint-carrying universal property

\[
\rho_x+\mathfrak e_{xy}=\rho_y.
\]

Accordingly, the earlier source-minimality condition is retained as an audit explanation of why this construction carries no auxiliary background data, while the active spatial branch now uses the stronger endpoint-carrying universal property directly.

The current downstream frontier becomes

\[
\boxed{
\operatorname{Herm}_0(2)\cong\mathbb R^3
\to
\Delta^3
\to
\text{regularity from intrinsic simplex symmetry}
\to
\text{Pythagorean closure}.
}
\]

## 8. Claim classes

| Statement | Class |
|---|---|
| normalized Hermitian `2 x 2` states have affine hull `I/2 + Herm_0(2)` | EXACT |
| every ordered affine pair has a unique endpoint-carrying displacement | EXACT AFFINE GEOMETRY |
| the displacement is `rho_y-rho_x` | EXACT |
| displacement is affine-natural | EXACT |
| reversal and endpoint composition follow | EXACT |
| translation carrier has real dimension 3 | EXACT |
| `SU(2)` conjugation induces the standard `SO(3)` action | EXACT |
| invariant positive quadratic metric is unique up to scale | EXACT REPRESENTATION-THEORETIC RESULT |
| TIR spatial branch exports the endpoint-carrying displacement as its primitive vector relation | SPATIAL BRANCH DEFINITION |
