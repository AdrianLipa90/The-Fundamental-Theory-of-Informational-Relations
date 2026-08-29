# Quantum Point Affine Spatial Carrier v0.1

Status: `TIR_QUANTUM_POINT_AFFINE_SPATIAL_PROMOTION_CANDIDATE`

Scope: local TIR geometry. This note develops a shorter spatial-promotion route directly from the primitive quantum point and the affine structure of normalized two-level quantum states.

## 1. Primitive quantum point state

Let a primitive locus `x` carry a normalized two-level quantum state

\[
\rho_x=\rho_x^\dagger,\qquad \operatorname{Tr}\rho_x=1,
\]

on

\[
\mathcal H_2\cong\mathbb C^2.
\]

Every such state has Bloch form

\[
\boxed{
\rho_x=\frac12\left(I+\mathbf r_x\cdot\boldsymbol\sigma\right),
\qquad |\mathbf r_x|\le1.
}
\]

The affine hull of the normalized state space is

\[
\boxed{
\mathcal A_2
=\left\{\rho=\rho^\dagger:\operatorname{Tr}\rho=1\right\}
=\frac12 I+\operatorname{Herm}_0(2).
}
\]

Because `Herm(2)` has real dimension four and the trace constraint removes one real degree of freedom,

\[
\boxed{\dim_{\mathbb R}\mathcal A_2=3.}
\]

Its translation space is exactly

\[
\boxed{
T\mathcal A_2\equiv\operatorname{Herm}_0(2)
=\operatorname{span}_{\mathbb R}\{\sigma_x,\sigma_y,\sigma_z\}.
}
\]

This statement concerns the affine hull. It therefore remains valid whether the admitted primitive point states are pure, mixed, or a subset whose affine span is full.

## 2. Canonical relational difference

For two primitive loci `x,y`, define the normalized affine relation generator

\[
\boxed{
\mathcal E_{xy}:=2(\rho_y-\rho_x).
}
\]

The factor `2` is fixed by the standard Bloch normalization. Since the identity terms cancel,

\[
\boxed{
\mathcal E_{xy}
=(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma
\in\operatorname{Herm}_0(2).
}
\]

Thus the same three-real-dimensional carrier previously obtained from traceless Hermitian generators appears as the canonical affine difference space of normalized binary quantum states.

## 3. Exact endpoint composition

The affine difference immediately satisfies

\[
\mathcal E_{xx}=0,
\]

\[
\boxed{\mathcal E_{yx}=-\mathcal E_{xy},}
\]

and for any three admitted loci,

\[
\begin{aligned}
\mathcal E_{xy}+\mathcal E_{yz}
&=2(\rho_y-\rho_x)+2(\rho_z-\rho_y)\\
&=2(\rho_z-\rho_x)\\
&=\mathcal E_{xz}.
\end{aligned}
\]

Hence

\[
\boxed{
\mathcal E_{xz}=\mathcal E_{xy}+\mathcal E_{yz}.
}
\]

Equivalently,

\[
\boxed{
\mathcal E_{xy}+\mathcal E_{yz}+\mathcal E_{zx}=0.
}
\]

So the local affine endpoint-closure law is automatic once the primitive relation is represented by the canonical state difference.

## 4. Canonical Euclidean metric

Use the Hilbert--Schmidt generator metric

\[
\boxed{
\langle A,B\rangle
=\frac12\operatorname{Tr}(AB).
}
\]

For

\[
\mathcal E_{xy}
=(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma,
\]

the Pauli identity

\[
\frac12\operatorname{Tr}(\sigma_i\sigma_j)=\delta_{ij}
\]

gives

\[
\boxed{
\|\mathcal E_{xy}\|^2
=\frac12\operatorname{Tr}(\mathcal E_{xy}^2)
=|\mathbf r_y-\mathbf r_x|^2.
}
\]

Thus the affine quantum-point difference carrier already has the ordinary Euclidean quadratic form in Bloch coefficients.

## 5. Symmetry covariance

Under a common local unitary frame transformation

\[
\rho_x\mapsto U\rho_xU^\dagger,
\]

we obtain

\[
\boxed{
\mathcal E_{xy}\mapsto U\mathcal E_{xy}U^\dagger.
}
\]

The Hilbert--Schmidt metric is invariant under this conjugation. The effective action on coefficient vectors is

\[
PSU(2)\cong SO(3).
\]

Therefore the affine relation carrier, its metric, and its endpoint composition law are all compatible with the already derived TIR rotational symmetry.

## 6. Pure-state sphere and affine three-space

For pure qubit states,

\[
|\mathbf r|=1,
\]

so the pure-state locus is

\[
\boxed{S^2.}
\]

Its affine hull is nevertheless the full three-dimensional trace-one hyperplane. Four affinely independent pure states are sufficient to span that affine hull.

The regular tetrahedral pure-state set satisfies

\[
\sum_{a=1}^{4}\mathbf n_a=0,
\qquad
\mathbf n_a\cdot\mathbf n_b=-\frac13\quad(a\ne b),
\]

and is therefore simultaneously:

- a minimal four-point affine frame of the three-dimensional normalized qubit state hull;
- the minimal regular isotropic tetrahedral cell derived in the spatial branch;
- the tetrahedral qubit SIC frame used for informational completeness.

Once the physical relation is identified with the canonical quantum-point affine difference, these three appearances live on one mathematical carrier rather than on separately introduced copies of `R^3`.

## 7. Spatial-promotion theorem in affine form

### Theorem — conditional quantum-point affine promotion

Assume the primitive TIR point is represented by a normalized state of the admitted binary quantum carrier and that the primitive local physical relation `x -> y` is represented by the canonical affine information-state difference

\[
\mathcal E_{xy}=2(\rho_y-\rho_x).
\]

Then:

\[
\boxed{
\mathcal E_{xy}\in\operatorname{Herm}_0(2)\cong\mathbb R^3,
}
\]

endpoint composition is additive,

\[
\boxed{
\mathcal E_{xz}=\mathcal E_{xy}+\mathcal E_{yz},
}
\]

and the canonical invariant metric is

\[
\boxed{
\|\mathcal E_{xy}\|^2
=\frac12\operatorname{Tr}(\mathcal E_{xy}^2).
}
\]

The local spatial carrier, affine composition law and Euclidean quadratic structure therefore arise together from one relation object.

## 8. Axiom crosswalk

The shortest candidate dependency is

\[
\boxed{
\begin{array}{rcl}
A1 &\to& \text{primitive locus / point},\\[1mm]
A2 &\to& \text{normalized binary quantum point state }\rho_x,\\[1mm]
A3 &\to& \text{physical relation carried by informational state distinction},\\[1mm]
A5 &\to& \frac12\operatorname{Tr}(\mathcal E^2)\text{ as geometric measure},\\[1mm]
A7 &\to& SU(2)\text{-covariant / }SO(3)\text{-isotropic realization}.
\end{array}
}
\]

The remaining foundational gate is now one sharply typed rule:

\[
\boxed{
\texttt{RELATION\_AS\_CANONICAL\_QUANTUM\_STATE\_DIFFERENCE}.
}
\]

If this rule is derived from the primitive meaning of A1--A3, the separate minimal-faithful-representation criterion becomes a consistency/uniqueness cross-check rather than the primary promotion mechanism.

## 9. Claim classes

| Statement | Class |
|---|---|
| trace-one Hermitian `2 x 2` operators form a real affine 3-space | EXACT |
| its translation space is `Herm_0(2)` | EXACT |
| `E_xy=2(rho_y-rho_x)` is traceless Hermitian | EXACT |
| affine state differences satisfy reversal and endpoint composition | EXACT |
| Hilbert--Schmidt metric equals Euclidean Bloch-coefficient metric under the declared normalization | EXACT |
| common `SU(2)` conjugation induces `SO(3)` covariance and preserves the metric | EXACT |
| tetrahedral pure states affinely span the same 3-space and form the qubit SIC frame | EXACT / STANDARD QUANTUM INFORMATION |
| primitive physical relation is the canonical quantum-state affine difference | TIR FOUNDATIONAL BRIDGE CANDIDATE |
| admitting that bridge yields the local 3D Euclidean relation carrier directly | EXACT CONDITIONAL |
