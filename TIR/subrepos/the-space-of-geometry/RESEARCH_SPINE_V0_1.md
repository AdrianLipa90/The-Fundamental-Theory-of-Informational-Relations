# The Space of Geometry — Research Spine v0.1

Status: `TIR_SPACE_OF_GEOMETRY_SPINE_CANDIDATE`

## 1. Primitive input

The subrepo imports the admitted TIR primitive line

\[
0\prec P\prec\{N,S\}\prec\frac12\prec\ln2\prec\mathbb C^2.
\]

The binary quantum carrier supplies the real traceless Hermitian generator space

\[
\boxed{
\mathfrak g_{\rm rel}
:=\operatorname{Herm}_0(2)
=\operatorname{span}_{\mathbb R}\{\sigma_x,\sigma_y,\sigma_z\}
\cong\mathbb R^3.
}
\]

With

\[
\langle A,B\rangle
=\frac12\operatorname{Tr}(AB),
\]

this carrier has the canonical Euclidean inner product.

## 2. Minimal spatial cell

Once the local spatial carrier is promoted to a three-dimensional affine/tangent carrier, the minimal full-dimensional simplex has four affinely independent vertices.

Thus

\[
\boxed{
\dim=3
\Longrightarrow
\Delta^3.
}
\]

For a center-based directional description the corresponding four equal-norm directions satisfy, under full isotropy,

\[
\sum_{a=1}^{4}\mathbf n_a=0,
\]

\[
\sum_{a=1}^{4}\mathbf n_a\mathbf n_a^T
=\frac43I_3,
\]

and therefore

\[
\boxed{
\mathbf n_a\cdot\mathbf n_b=-\frac13
\quad(a\neq b).
}
\]

This is the regular tetrahedral cell.

## 3. Distance

For a relational displacement generator

\[
\mathcal E=E^a\sigma_a,
\]

define

\[
\boxed{
\ell^2(\mathcal E)
=\frac12\operatorname{Tr}(\mathcal E^2)
=\delta_{ab}E^aE^b.
}
\]

Thus distance is inherited from the same generator metric that defines the three-dimensional carrier.

## 4. Angle

For nonzero displacements `A,B`, define

\[
\boxed{
\cos\theta(A,B)
=\frac{\langle A,B\rangle}{\|A\|\,\|B\|}.
}
\]

This gives the standard Euclidean angular relation directly from the Hilbert--Schmidt metric on `Herm_0(2)`.

## 5. Orthogonality

Orthogonality is the zero-inner-product relation

\[
\boxed{
A\perp B
\iff
\langle A,B\rangle=0.
}
\]

Because the Pauli basis is orthonormal,

\[
\frac12\operatorname{Tr}(\sigma_i\sigma_j)=\delta_{ij},
\]

three mutually orthogonal local directions exist canonically in the generator carrier.

## 6. Pythagorean closure

For arbitrary `A,B`,

\[
\|A+B\|^2
=\langle A+B,A+B\rangle
\]

so

\[
\boxed{
\|A+B\|^2
=\|A\|^2+\|B\|^2+2\langle A,B\rangle.
}
\]

If

\[
A\perp B,
\]

then

\[
\boxed{
\|A+B\|^2
=\|A\|^2+\|B\|^2.
}
\]

Let

\[
a=\|A\|,
\qquad
b=\|B\|,
\qquad
c=\|A+B\|.
\]

Then

\[
\boxed{a^2+b^2=c^2.}
\]

This is the Pythagorean closure endpoint.

## 7. Dependency chain

The intended derivation DAG is

```text
FIRST DISTINCTION
      |
      v
C^2
      |
      v
Herm_0(2)
      |
      +--> real dimension 3
      +--> inner product Tr(AB)/2
      +--> SU(2) adjoint -> SO(3)
      |
      v
SPATIAL PROMOTION
      |
      v
minimal full-dimensional simplex Delta^3
      |
      v
regular tetrahedral local cell
      |
      v
relational displacement norm
      |
      v
angle / orthogonality
      |
      v
PYTHAGOREAN CLOSURE
```

## 8. Main open gates

The research programme is concentrated on three proof gates:

- derive the physical spatial promotion of `Herm_0(2)` rather than merely declaring the identification;
- derive why minimal tetrahedral informational completeness and minimal tetrahedral spatial adjacency are one physical relation object;
- derive a regular gluing/refinement rule from tetrahedral local cells to a smooth spatial carrier while preserving endpoint closure and metric compatibility.

Everything after a regular Euclidean local carrier and Pythagorean closure belongs to established downstream geometry and may be imported by theorem reference where appropriate.
