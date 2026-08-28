# TIR Rank-3 Isotropy Stabilization v0.1

Status: `EXACT_CONDITIONAL_SPATIAL_RANK_THEOREM_CANDIDATE`

Scope: TIR-only continuation of the relational generator and discrete solder constructions. The purpose of this gate is to replace the generic question “why rank three?” by a precise representation-theoretic condition on the primitive local relation law.

## 1. Parent structure

The binary quantum relation supplies the real generator carrier

\[
\mathfrak g_{\rm rel}=\operatorname{Herm}_0(2)
\cong \mathbb R^3,
\]

with metric

\[
\langle A,B\rangle=\frac12\operatorname{Tr}(AB)
\]

and rotational action

\[
\operatorname{Ad}:SU(2)\to SO(3).
\]

At a relational locus `x`, let the outgoing edge-generator span be

\[
\boxed{
W_x:=\operatorname{span}_{\mathbb R}
\{\mathcal E_{xy}:y\sim x\}
\subseteq \mathfrak g_{\rm rel}.
}
\]

The local spatial rank candidate is

\[
r_x:=\dim W_x\le 3.
\]

## 2. Primitive isotropy condition

The representation-theoretic stabilization condition is:

### Full local relational isotropy

For every primitive rotation `R in SO(3)` induced by the `SU(2)` adjoint action,

\[
\boxed{R(W_x)=W_x.}
\]

This says that the local relation law preserves the full primitive rotational symmetry of the generator carrier rather than selecting a preferred proper subspace.

A non-empty spatial patch also requires

\[
\boxed{W_x\ne\{0\}.}
\]

## 3. Irreducibility theorem

The defining real representation of `SO(3)` on `R^3` is irreducible: its only invariant linear subspaces are

\[
\{0\}
\quad\text{and}\quad
\mathbb R^3.
\]

Therefore, if

1. `W_x` is nonzero; and
2. `W_x` is invariant under the full `SO(3)` action;

then

\[
\boxed{W_x=\mathfrak g_{\rm rel}}.
\]

Hence

\[
\boxed{r_x=3.}
\]

### Theorem — conditional rank-3 stabilization

Let `W_x` be the local displacement-generator span inside `Herm_0(2)`. Under nonzero occupancy and unbroken full adjoint `SO(3)` isotropy,

\[
\boxed{
W_x\ne0,
\quad
SO(3)W_x=W_x
\Longrightarrow
\dim W_x=3.
}
\]

This is an exact conditional consequence of the standard irreducibility of the vector representation of `SO(3)`.

## 4. Why rank 1 and rank 2 are unstable under full isotropy

A one-dimensional span selects an axis. A two-dimensional span selects a plane and its normal. Neither can be invariant under every spatial rotation.

Thus

\[
\boxed{
0<r_x<3
\Longrightarrow
\text{full local }SO(3)\text{ isotropy is broken}.
}
\]

This gives the first sharp TIR selection statement:

```text
nonzero relational displacement
+ preserve the full primitive rotational symmetry
= full rank of the primitive generator carrier
= rank 3
```

The dimension is therefore not selected by counting neighbors. It is selected by the combination of the binary complex carrier and unbroken isotropy of its real distinction-generator representation.

## 5. Relation to A4 and A7

A7 supplies the symmetry requirement at the level of primitive relational law. The generator construction supplies the concrete group `SO(3)` through `SU(2)` conjugation.

A4 independently checks the resulting full-rank local carrier: the unit locus

\[
\{A\in\mathfrak g_{\rm rel}:\|A\|=1\}
\]

is exactly `S^2`, the isotropic boundary selected by the spherical-efficiency branch.

Thus the convergence is

\[
\boxed{
A2+\text{binary distinction}
\to \operatorname{Herm}_0(2)\cong\mathbb R^3
\xrightarrow{A7\;\text{unbroken isotropy}}
r_x=3
\xleftarrow{A4}
S^2\text{ isotropic unit locus}.
}
\]

## 6. Spatial-promotion consequence

The earlier promotion gate was

\[
T_x\Sigma\;\widehat{=}\;\mathfrak g_{\rm rel}.
\]

The present theorem weakens what must still be postulated. If the discrete solder map supplies a nonzero local span `W_x` and the primitive law preserves full local adjoint isotropy, then

\[
W_x=\mathfrak g_{\rm rel}
\]

already follows.

The remaining continuum question is therefore primarily a locality/gluing question:

\[
\boxed{
W_x=\mathfrak g_{\rm rel}
\quad\longrightarrow\quad
T_x\Sigma
}
\]

through a regular solder/coframe limit.

## 7. Symmetry-breaking branch

The theorem also gives a typed branch for lower-rank structures. If a local state or boundary condition breaks the primitive isotropy to a subgroup `H subset SO(3)`, proper invariant subspaces may become admissible.

Thus rank reduction is treated as

\[
\boxed{
SO(3)\to H
\quad\Longrightarrow\quad
\text{possible lower-rank effective geometry}.
}
\]

This keeps primitive full-rank geometry and downstream symmetry-broken structures distinct.

## 8. Claim classes

| Statement | TIR class |
|---|---|
| `Herm_0(2) ~= R^3` | EXACT LINEAR ALGEBRA |
| adjoint `SU(2)` action induces defining `SO(3)` action | STANDARD EXACT REPRESENTATION THEORY |
| defining real `SO(3)` representation is irreducible | STANDARD EXACT REPRESENTATION THEORY |
| nonzero full-`SO(3)` invariant `W_x` has rank 3 | EXACT CONDITIONAL THEOREM |
| A7 enforces unbroken full local `SO(3)` isotropy on primitive edge spans | TIR PRIMITIVE-LAW GATE |
| rank-reduced sectors correspond to symmetry-broken local laws | CONDITIONAL STRUCTURAL BRANCH |
| smooth tangent-bundle realization | OPEN CONTINUUM GATE |

## 9. Next gate

With rank stabilization isolated, the next primitive question is torsion:

\[
\boxed{
\text{What relational closure law makes two path descriptions of the same endpoint agree?}
}
\]

That condition can be tested directly on the discrete solder construction and, under refinement, against Cartan torsion.