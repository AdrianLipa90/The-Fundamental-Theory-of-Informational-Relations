# A1+A3 Source-Minimality to Affine Naturality v0.1

Status: `TIR_SOURCE_MINIMALITY_AFFINE_NATURALITY_BRIDGE_CANDIDATE`

Scope: isolate the last non-mathematical step in the local Space of Geometry derivation. The exact affine theorem is separated from the TIR inheritance rule that selects a background-free primitive relation law.

## 1. Imported primitive data

The binary quantum point supplies the normalized affine carrier

\[
\mathcal A_2=\frac12I+V,
\qquad
V=\operatorname{Herm}_0(2)\cong\mathbb R^3.
\]

At the primitive local relation layer the declared source data are only

\[
\boxed{(\rho_x,\rho_y;\mathcal A_2,V).}
\]

A candidate vector relation is

\[
R:\mathcal A_2\times\mathcal A_2\to V.
\]

## 2. Source-minimal law signature

Define a primitive relation law to be **source-minimal** when its value is determined only by the admitted endpoint states and the affine structure already present in their carrier.

Equivalently, no independent primitive datum such as

\[
o\in\mathcal A_2,
\qquad
n\in V,
\qquad
B:V\to V,
\qquad
\text{or any additional background tensor}
\]

is introduced at this dependency layer unless it has an upstream source.

This is a dependency-typing statement. It does not select a coordinate system; it restricts the signature of the primitive law.

## 3. Background-free definability implies affine naturality

If a relation is constructed only from the ordered pair and the affine carrier structure, its form must commute with every affine automorphism of the same source data.

For

\[
F(x)=Lx+a,
\qquad L\in GL(V),
\]

the intrinsic relation therefore obeys

\[
\boxed{
R(Fx,Fy)=L\,R(x,y).
}
\]

This is the operational mathematical meaning of **no additional affine background structure**.

A law that depended on a separately selected origin, axis, basis or tensor would require that object to be transformed as extra input. With no such input in the primitive signature, the relation must be natural under the full affine automorphism group.

Thus, once source-minimality of the law signature is admitted,

\[
\boxed{
\text{SOURCE MINIMALITY}
\Longrightarrow
\text{AFFINE NATURALITY}.
}
\]

The implication is definitional at the level of the declared construction language: `source-minimal` means that the law is built only from the affine pair and its native structure.

## 4. Exact naturality theorem

Translation covariance gives

\[
R(x+a,y+a)=R(x,y),
\]

so there is a map

\[
f:V\to V
\]

with

\[
R(x,y)=f(y-x).
\]

Full affine naturality gives

\[
\boxed{f(Lv)=Lf(v)}
\qquad\forall L\in GL(V).
\]

For nonzero `v`, every invertible map fixing `v` must also fix `f(v)`. The common fixed subspace of the stabilizer of `v` is

\[
\operatorname{span}(v),
\]

hence

\[
f(v)=c(v)v.
\]

Because `GL(V)` acts transitively on nonzero vectors,

\[
c(v)=c
\]

is constant on `V\\{0}`. Continuity at zero yields

\[
\boxed{f(v)=cv.}
\]

Therefore every continuous source-minimal affine-natural vector relation has the form

\[
\boxed{
R(x,y)=c(y-x).
}
\]

## 5. A3 distinction preservation

Information Primacy types physical structure through distinguishable relations.

A relation law with

\[
c=0
\]

collapses every ordered pair to the same zero relation. Under distinction preservation,

\[
\boxed{c\ne0.}
\]

Thus

\[
\boxed{
R(x,y)=c(y-x),\qquad c\ne0.
}
\]

The magnitude of `c` is the global relation-unit convention and its sign fixes orientation.

If the relation is typed more strongly as the actual torsor translation that carries `x` to `y`, then

\[
\boxed{c=1}
\]

intrinsically. The spatial Pauli-coordinate convention uses

\[
\mathcal E_{xy}=2(\rho_y-\rho_x),
\]

which is the same torsor displacement expressed in the established generator normalization.

## 6. A1+A3 inheritance surface

A1 supplies minimality at the primitive carrier level. A3 supplies relational/informational primacy.

The narrow remaining TIR inheritance question is now:

\[
\boxed{
\texttt{A1\_DEPENDENCY\_MINIMALITY\_APPLIES\_TO\_PRIMITIVE\_LAW\_SIGNATURE}.
}
\]

If A1 minimality is inherited by the primitive relation-law signature, then no unsourced background object is admitted at that layer. Together with A3 relational primacy, the primitive relation is source-minimal; source-minimality yields affine naturality; and the exact theorem fixes the relation to the affine displacement up to unit/orientation.

The chain is

\[
\boxed{
A1\ \text{dependency minimality}
+A3\ \text{relational primacy}
\to
\text{source-minimal relation signature}
\to
\text{affine naturality}
\to
R(x,y)=c(y-x),\ c\ne0.
}
\]

## 7. Consequence for local geometry

For quantum points,

\[
R(\rho_x,\rho_y)\propto\rho_y-\rho_x
\in\operatorname{Herm}_0(2).
\]

Therefore the local relational translation carrier is

\[
\boxed{
\operatorname{Herm}_0(2)\cong\mathbb R^3.
}
\]

The torsor identities supply endpoint composition, while the unique `SU(2)`-invariant positive quadratic form is, up to scale,

\[
\boxed{
\langle A,B\rangle=\frac12\operatorname{Tr}(AB).
}
\]

The downstream chain then remains theorem-driven:

\[
\mathbb R^3
\to
\Delta^3
\to
\text{regular tetrahedral local frame}
\to
\text{angle / orthogonality}
\to
\text{Pythagorean closure}.
\]

## 8. Claim classes

| Statement | Class |
|---|---|
| a law using only affine pair data is natural under affine automorphisms, under the declared source-minimal construction language | EXACT BY DEFINITION OF SOURCE-MINIMALITY |
| continuous affine-natural `R:A x A -> V` has form `c(y-x)` | EXACT NATURALITY THEOREM |
| distinction preservation requires `c != 0` | EXACT CONDITIONAL |
| torsor-translation typing fixes `c=1` intrinsically | EXACT AFFINE GEOMETRY |
| Pauli generator normalization corresponds to `E=2(rho_y-rho_x)` | EXACT CONVENTION |
| A1 minimality propagates from carrier minimality to primitive law-signature minimality | TIR FOUNDATIONAL INHERITANCE GATE |
| under that inheritance, the local spatial relation bridge closes | EXACT CONDITIONAL |
