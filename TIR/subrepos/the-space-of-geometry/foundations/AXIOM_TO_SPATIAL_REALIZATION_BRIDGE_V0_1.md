# Axiom-to-Spatial-Realization Bridge v0.1

Status: `TIR_AXIOMATIC_SPATIAL_REALIZATION_BRIDGE_CANDIDATE`

Scope: reduce the remaining physical promotion gate to explicit consequences/candidate inheritance rules from the admitted TIR axioms. The exact representation-theoretic closure is supplied by `SPATIAL_PROMOTION_UNIQUENESS_V0_1.md`.

## 1. Imported exact structure

A2 supplies the binary quantum carrier

\[
\mathcal H_2\cong\mathbb C^2
\]

and therefore the traceless Hermitian relation-generator carrier

\[
\mathfrak g_{\rm rel}=\operatorname{Herm}_0(2).
\]

Its effective rotational group is

\[
\boxed{
G_{\rm rel}=PSU(2)=SU(2)/\{\pm I\}\cong SO(3).
}
\]

The quotient by `{+I,-I}` already removes the exact double-cover redundancy of the `SU(2)` action on real generator directions.

## 2. A3 -> distinguishability-preserving realization

A3 assigns foundational status to information/relational distinction.

Let

\[
\rho:G_{\rm rel}\to O(V_x,q_x)
\]

be the action of primitive relational rotations on a candidate physical local direction carrier.

If

\[
\ker\rho\ne\{e\},
\]

then two distinct elements of the already reduced physical rotation group act identically on every local direction. The realization has introduced an additional quotient

\[
G_{\rm rel}\to G_{\rm rel}/\ker\rho.
\]

Define the **distinguishability-preservation bridge condition**:

\[
\boxed{
\text{after declared gauge reduction, the spatial realization preserves distinct primitive relational transformations.}
}
\]

Under this condition,

\[
\boxed{\ker\rho=\{e\},}
\]

so the spatial action is faithful.

This is the precise A3 bridge candidate: no further information quotient is introduced between the primitive relation group and its spatial realization unless separately typed as gauge redundancy.

## 3. A5 + A7 -> invariant real quadratic geometry

A5 states that arithmetic measures geometry. A7 supplies law-level symmetry.

Let the local squared length be represented by a positive quadratic form

\[
q_x(v)>0\qquad(v\ne0).
\]

Symmetry of the geometric law requires

\[
q_x(\rho(g)v)=q_x(v)
\qquad
\forall g\in G_{\rm rel}.
\]

Hence

\[
\boxed{
\rho(G_{\rm rel})\subset O(V_x,q_x).
}
\]

Thus the physical direction carrier is a real orthogonal representation of the primitive rotational symmetry.

On the already constructed generator carrier the canonical realization is

\[
q(A)=\frac12\operatorname{Tr}(A^2).
\]

## 4. A1 + A3 -> minimal source-closed realization candidate

A1 supplies the primitive minimality principle at the foundation of the TIR dependency line. A3 says the physical content is carried by informational relations.

Define the **minimal source-closure bridge condition**:

> the local spatial carrier contains the smallest number of independent real directional degrees of freedom required to represent the admitted primitive relational information faithfully and symmetrically.

If a candidate carrier decomposes as

\[
V_x=V_{\rm sourced}\oplus W
\]

where `W` carries additional independent spatial directions with no source in the admitted primitive relation data, then `W` is superfluous to the minimal source-closed realization.

Under the bridge condition the selected carrier is therefore minimal among faithful real orthogonal `G_rel` representations.

This is the explicit place where the foundational point-minimality idea is extended to carrier minimality. It is kept as a named derivation candidate so the step remains auditable.

## 5. Representation-theoretic closure

The three bridge conditions now match the hypotheses of the exact theorem in `SPATIAL_PROMOTION_UNIQUENESS_V0_1.md`:

```text
A3 distinguishability preservation
        -> faithful action
A5 + A7 invariant geometric measure
        -> real orthogonal action
A1 + A3 minimal source closure
        -> minimal carrier
```

Therefore, conditionally,

\[
\boxed{
V_x\cong\mathbb R^3
\cong\operatorname{Herm}_0(2)
}
\]

up to orthogonal frame equivalence, and

\[
\boxed{
h_x=\lambda_x\,\frac12\operatorname{Tr}(AB),\qquad\lambda_x>0.}
\]

For dimensionless local geometry the canonical normalization is `lambda_x=1`.

## 6. Axiom dependency map

\[
\boxed{
\begin{array}{rcl}
A2 &\to& \mathbb C^2\to\operatorname{Herm}_0(2),\\[2mm]
A3 &\to& \text{distinguishability preservation / faithfulness},\\[2mm]
A5+A7 &\to& \text{invariant real quadratic measure / orthogonality},\\[2mm]
A1+A3 &\to& \text{minimal source-closed carrier},\\[2mm]
\text{representation theorem} &\to& V_x\cong\mathbb R^3.
\end{array}
}
\]

A4 then acts at the minimal isotropic-cell stage, where the unit directional locus and equal local weighting converge on the regular tetrahedron. A8 enters the downstream endpoint-closure/consistency layer.

## 7. Current theorem status

The group/representation closure is exact once the bridge conditions are admitted.

The remaining foundational audit is concentrated on two named bridge conditions:

1. **distinguishability preservation after declared gauge reduction** as the operational A3 spatial rule;
2. **minimal source closure** as the extension of A1+A3 from primitive carrier minimality to local spatial carrier minimality.

If these two conditions are promoted from candidates to derived TIR rules, the local spatial promotion closes.

## 8. Claim classes

| Statement | Class |
|---|---|
| `PSU(2) ~= SO(3)` acts faithfully on `Herm_0(2)` | EXACT |
| a nontrivial kernel creates an additional quotient of relational transformations | EXACT GROUP THEORY |
| invariant positive quadratic length makes the action orthogonal | EXACT |
| minimal faithful real orthogonal `SO(3)` carrier has dimension 3 | EXACT, UPSTREAM THEOREM |
| A3 selects distinguishability preservation after declared gauge reduction | TIR BRIDGE CANDIDATE |
| A1+A3 select minimal source closure | TIR BRIDGE CANDIDATE |
| admitting both bridge conditions yields local `V_x ~= Herm_0(2)` | EXACT CONDITIONAL |
