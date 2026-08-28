# TIR Relational Generator Space v0.1

Status: `TIR_SPATIAL_GENERATOR_CONSTRUCTION_CANDIDATE`

Scope: TIR-only construction of a real three-dimensional relational generator space from the first binary quantum carrier. The construction is algebraically exact once `H_2 ~= C^2` is admitted. Its promotion to the physical spatial tangent carrier is the explicit TIR spatial-identification gate.

## 1. Binary quantum carrier

From the primitive first distinction and A2,

\[
\boxed{\mathcal H_2\cong\mathbb C^2}.
\]

The real vector space of Hermitian operators on `C^2` is

\[
\operatorname{Herm}(2).
\]

Every element has a unique decomposition

\[
\boxed{
A=a_0 I+a_x\sigma_x+a_y\sigma_y+a_z\sigma_z,
\qquad a_\mu\in\mathbb R.
}
\]

Thus

\[
\dim_{\mathbb R}\operatorname{Herm}(2)=4.
\]

## 2. Remove the uniform component

The identity component

\[
a_0I
\]

acts equally on both primitive alternatives. It therefore carries no directional distinction between the two poles.

Define the traceless distinction-generator space

\[
\boxed{
\mathfrak g_{\rm rel}
:=\operatorname{Herm}_0(2)
=\{A=A^\dagger:\operatorname{Tr}A=0\}.
}
\]

It is spanned over the reals by

\[
\boxed{\{\sigma_x,\sigma_y,\sigma_z\}}.
\]

Therefore

\[
\boxed{\dim_{\mathbb R}\mathfrak g_{\rm rel}=3}.
\]

This is an exact linear-algebraic consequence of the binary complex quantum carrier.

## 3. Canonical metric on generator space

Define

\[
\boxed{
\langle A,B\rangle_{\rm HS}
:=\frac12\operatorname{Tr}(AB)
}
\]

for traceless Hermitian `A,B`.

The Pauli basis satisfies

\[
\frac12\operatorname{Tr}(\sigma_i\sigma_j)=\delta_{ij}.
\]

Hence `g_rel` carries a canonical positive-definite Euclidean inner product.

If

\[
A=\mathbf a\cdot\boldsymbol\sigma,
\qquad
B=\mathbf b\cdot\boldsymbol\sigma,
\]

then

\[
\boxed{\langle A,B\rangle_{\rm HS}=\mathbf a\cdot\mathbf b}.
\]

The associated norm is

\[
\|A\|^2=\frac12\operatorname{Tr}(A^2)=|\mathbf a|^2.
\]

## 4. Unit relational directions form a sphere

For

\[
A=\mathbf n\cdot\boldsymbol\sigma
\]

with `|n|=1`, the Pauli algebra gives

\[
A^2=I.
\]

Conversely, a traceless Hermitian `2x2` operator satisfying `A^2=I` has coefficient vector of unit norm.

Therefore the unit distinction-generator locus is

\[
\boxed{
\{A\in\mathfrak g_{\rm rel}:\|A\|=1\}
\cong S^2.
}
\]

This sphere lives inside the real three-dimensional generator space.

## 5. SU(2) acts as rotations

Let

\[
U\in SU(2).
\]

Conjugation acts on the generator space by

\[
\boxed{A\mapsto UAU^\dagger}.
\]

This action preserves:

\[
\operatorname{Tr}A=0,
\]

\[
\frac12\operatorname{Tr}(A^2),
\]

and the Hilbert--Schmidt inner product.

Hence it induces an orthogonal action on the coefficient vector `a in R^3`. The standard adjoint map is

\[
\boxed{
\operatorname{Ad}:SU(2)\to SO(3)
}
\]

with kernel `{+I,-I}`.

Thus

\[
\boxed{SU(2)/\{\pm I\}\cong SO(3)}.
\]

The same three-dimensional real carrier therefore supports the canonical rotational symmetry associated with the primitive two-state quantum relation.

## 6. Bloch map is internal to the same carrier

For a normalized pure state `|psi>`, define

\[
r_i=\langle\psi|\sigma_i|\psi\rangle.
\]

Then

\[
\boxed{\mathbf r=(r_x,r_y,r_z)\in S^2}
\]

for pure states, and

\[
\rho_\psi
=|\psi\rangle\langle\psi|
=\frac12(I+\mathbf r\cdot\boldsymbol\sigma).
\]

Therefore the projective Bloch sphere and the unit sphere of traceless Hermitian relation generators are represented in the same real coefficient space:

\[
\boxed{
\mathbb{CP}^1
\xrightarrow{\rm Bloch}
S^2\subset\mathfrak g_{\rm rel}\cong\mathbb R^3.
}
\]

This gives an explicit mathematical candidate for the earlier bridge `Xi` without identifying an already-existing external spatial sphere by notation alone.

## 7. Spatial promotion gate

TIR can now state the spatial construction gate sharply.

### Spatial Generator Postulate Candidate

At each primitive continuum locus `x`, identify the spatial tangent carrier with the relational distinction-generator space:

\[
\boxed{
T_x\Sigma\;\widehat{=}\;\mathfrak g_{\rm rel}
=\operatorname{Herm}_0(2).
}
\]

If this identification is admitted or derived from the continuum relation map, then immediately

\[
\boxed{\dim T_x\Sigma=3}
\]

and the canonical local metric is inherited from

\[
\boxed{
h_x(A,B)=\frac12\operatorname{Tr}(AB).
}
\]

This is stronger than simply observing that two spheres share topology: the same algebra supplies dimension, positive metric, unit sphere, and rotation group.

## 8. Relation to A4, A5, and A7

The construction gives independent convergence with three TIR axioms:

- **A4:** the unit locus in `g_rel` is a sphere, matching the selected isotropic enclosure geometry;
- **A5:** scalar geometric relations become traces, norms, angles, determinants, and winding invariants;
- **A7:** `SU(2)` conjugation induces `SO(3)` rotations preserving the generator metric.

Thus the candidate spatial tangent construction has the typed convergence

\[
\boxed{
\mathbb C^2
\to
\operatorname{Herm}_0(2)
\cong\mathbb R^3
\to
(S^2,SO(3),\langle\cdot,\cdot\rangle)
}
\]

with A4/A5/A7 acting as independent geometric, arithmetic, and symmetry checks.

## 9. What remains to derive

The algebraic carrier is exact. The remaining TIR task is the locality/continuum bridge:

\[
\boxed{
\text{finite relational generator spaces}
\longrightarrow
\text{smooth tangent bundle }T\Sigma.
}
\]

Concretely, the next gate must determine when neighboring local copies of `Herm_0(2)` admit transition maps that preserve the inner product and produce a consistent spatial connection.

That turns the next problem into a bundle/gluing problem rather than another dimension guess.

## 10. Claim classes

| Statement | TIR class |
|---|---|
| `Herm(2)` has real dimension 4 | EXACT LINEAR ALGEBRA |
| `Herm_0(2)` has real dimension 3 | EXACT LINEAR ALGEBRA |
| Pauli matrices are an orthonormal basis under `Tr(AB)/2` | EXACT MATRIX IDENTITY |
| unit traceless Hermitian generators form `S^2` | EXACT |
| `SU(2)` conjugation induces `SO(3)` rotations | STANDARD EXACT REPRESENTATION THEORY |
| pure-state Bloch map lands on the same coefficient `S^2` | STANDARD EXACT QUANTUM GEOMETRY |
| `T_x Sigma = Herm_0(2)` | TIR SPATIAL PROMOTION GATE |
| spatial dimension `n=3` after that promotion | EXACT CONDITIONAL |
| continuum tangent-bundle gluing | OPEN TIR DERIVATION GATE |
