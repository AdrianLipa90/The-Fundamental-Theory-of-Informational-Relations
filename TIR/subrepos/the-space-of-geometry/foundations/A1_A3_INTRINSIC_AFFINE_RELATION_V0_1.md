# A1+A3 Intrinsic Affine Relation v0.1

Status: `TIR_INTRINSIC_AFFINE_RELATION_TYPING_CANDIDATE`

Scope: reduce the final A3 torsor-typing gate by asking for the primitive point relation to use only the affine structure already supplied by the quantum-point state carrier, with no auxiliary origin, axis or background tensor.

## 1. Imported carrier

The binary quantum-point state hull is the affine space

\[
\mathcal A_2=\frac12I+V,
\qquad
V=\operatorname{Herm}_0(2)\cong\mathbb R^3.
\]

A relation law is a map

\[
R:\mathcal A_2\times\mathcal A_2\to V.
\]

## 2. Intrinsic affine naturality

Call `R` intrinsic to the affine carrier when it respects every affine change of frame

\[
F(x)=Lx+a,
\qquad L\in GL(V),
\]

through

\[
\boxed{
R(Fx,Fy)=L\,R(x,y).
}
\]

This condition says that the relation is built from the ordered endpoints and the affine structure itself; it introduces no preferred origin, basis, direction or additional background object.

Translation covariance immediately gives

\[
R(x+a,y+a)=R(x,y),
\]

so there exists a map `f:V->V` such that

\[
\boxed{R(x,y)=f(y-x).}
\]

## 3. Naturality theorem

For every `L in GL(V)`, affine naturality implies

\[
\boxed{f(Lv)=L f(v).}
\]

Take any nonzero `v`. Every invertible linear transformation that fixes `v` must also fix `f(v)`. The common fixed subspace of the stabilizer of `v` is exactly the line `span(v)`. Therefore

\[
f(v)=c(v)v.
\]

The group `GL(V)` acts transitively on nonzero vectors, so covariance forces

\[
c(Lv)=c(v).
\]

Hence `c(v)` is one constant `c` on `V\setminus\{0\}`. Continuity at zero gives

\[
\boxed{f(v)=c\,v}
\]

for all `v in V`.

Thus every continuous intrinsic affine vector relation law has the form

\[
\boxed{
R(x,y)=c\,(y-x).
}
\]

## 4. Distinction preservation and normalization

A3 requires the relation representation to preserve nontrivial distinguishability. Therefore the zero map is excluded:

\[
\boxed{c\ne0.}
\]

The remaining magnitude is a global choice of relation unit; its sign is orientation.

For the intrinsic torsor displacement itself,

\[
c=1.
\]

For the Pauli-coordinate convention used in the spatial branch,

\[
\boxed{
\mathcal E_{xy}=2(\rho_y-\rho_x),
}
\]

so the displayed coordinate normalization is `c=2` relative to density-operator difference.

## 5. A1+A3 inheritance candidate

A1 supplies the foundational minimality rule. A3 types physical structure as distinguishable informational relations.

The candidate inheritance is:

> the primitive ordered relation between two quantum-point states is represented by the minimal intrinsic vector relation available from their admitted affine carrier, with no additional origin, axis or background structure.

Under this rule, affine naturality is the mathematical expression of source-minimal relationality. The theorem above then gives

\[
\boxed{
R(\rho_x,\rho_y)=c(\rho_y-\rho_x),
\qquad c\ne0.
}
\]

Choosing the standard Pauli coordinate normalization gives the already registered relation generator

\[
\boxed{
\mathcal E_{xy}=2(\rho_y-\rho_x).
}
\]

This reduces the final bridge from an arbitrary physical identification to a single explicit inheritance question: whether A1 minimality and A3 relational primacy select an intrinsic affine-natural relation law.

## 6. Consequences

Once the intrinsic affine relation is admitted,

\[
\mathcal E_{yx}=-\mathcal E_{xy},
\]

\[
\mathcal E_{xz}=\mathcal E_{xy}+\mathcal E_{yz},
\]

and

\[
\mathcal E_{xy}+\mathcal E_{yz}+\mathcal E_{zx}=0
\]

follow exactly.

The translation space is already

\[
V\cong\mathbb R^3,
\]

and the `SU(2)` adjoint action supplies the physical `SO(3)` rotational symmetry and the invariant quadratic metric up to scale.

## 7. Relation to A5 and A8

A5 is now used at the measurement layer:

\[
\frac12\operatorname{Tr}(\mathcal E^2)
\]

is the arithmetic invariant measuring squared relation length.

A8 is used at the contextual closure layer. For the intrinsic affine relation, same-chart endpoint composition already closes exactly. If a downstream comparison introduces nontrivial transport or incompatible contexts, A8 types the resulting defect for a higher-order curvature/holonomy closure rather than altering the local affine theorem.

## 8. Claim classes

| Statement | Class |
|---|---|
| translation-natural relation depends only on `y-x` | EXACT AFFINE GEOMETRY |
| continuous `GL(V)`-equivariant `f:V->V` has form `c I` | EXACT NATURALITY THEOREM |
| distinction preservation removes `c=0` | EXACT CONDITIONAL |
| intrinsic affine vector relation is unique up to scale/orientation | EXACT CONDITIONAL |
| A1+A3 select affine naturality/no auxiliary background structure | TIR FOUNDATIONAL INHERITANCE GATE |
| under that inheritance, relation-as-state-difference closes | EXACT CONDITIONAL |
