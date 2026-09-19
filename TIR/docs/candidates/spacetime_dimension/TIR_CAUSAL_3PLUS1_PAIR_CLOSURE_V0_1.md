# TIR Causal 3+1 Pair Closure v0.1

Status: CANDIDATE_ONLY / EXACT_BINARY_HERMITIAN_CAUSAL_ORDER_THEOREM / MINKOWSKI_SIGNATURE_DERIVED / HALF_DIFFERENCE_UNIQUENESS_EXACT / PHYSICAL_EVENT_BINDING_CONDITIONAL / CANON_ALLOWED_FALSE

Date: 2026-09-19

## 1. Claim

This note formalizes the statement

\[
\boxed{
3_{\rm space}+1_{\rm scalar}
\longrightarrow
\text{nontrivial causal order on pairs}
\longrightarrow
\frac12\text{ centered relation representation}.
}
\]

The theorem is exact inside the admitted binary Hermitian carrier.

The remaining physical statement is only the identification of the admitted physical event relation with this Hermitian causal order.

## 2. Binary Hermitian carrier

Let

\[
\mathcal V:=\operatorname{Herm}(2).
\]

Every element has the unique Pauli decomposition

\[
\boxed{
X=tI+x\sigma_x+y\sigma_y+z\sigma_z.
}
\]

Therefore

\[
\mathcal V
=
\mathbb RI
\oplus
\operatorname{Herm}_0(2)
\]

with

\[
\boxed{
\dim_{\mathbb R}\mathbb RI=1,
\qquad
\dim_{\mathbb R}\operatorname{Herm}_0(2)=3.
}
\]

The scalar identity direction is invariant under SU(2) conjugation, whereas the traceless sector transforms through the defining SO(3) rotation representation.

Thus the decomposition is not only 1+3 by dimension; it is the exact decomposition into one rotational scalar and three rotational directions.

## 3. Determinant theorem and Minkowski signs

Using the Pauli matrices,

\[
X=
\begin{pmatrix}
t+z & x-iy\\
x+iy & t-z
\end{pmatrix}.
\]

Hence

\[
\begin{aligned}
\det X
&=
(t+z)(t-z)-(x-iy)(x+iy)\\
&=
t^2-z^2-x^2-y^2.
\end{aligned}
\]

Therefore

\[
\boxed{
\det X=t^2-|\mathbf x|^2.
}
\]

In the basis

\[
\{I,\sigma_x,\sigma_y,\sigma_z\}
\]

the determinant quadratic form has matrix

\[
\boxed{
\eta=\operatorname{diag}(1,-1,-1,-1).
}
\]

Up to the overall sign convention, this is exactly the Minkowski signature.

The relative sign is therefore not inserted independently once the determinant of the primitive Hermitian carrier is selected as the quadratic invariant.

## 4. Why the scalar direction must have the opposite sign

Consider an arbitrary quadratic form on

\[
\mathbb R\oplus\mathbb R^3
\]

that is invariant under the full spatial SO(3) action.

Write

\[
Q(t,\mathbf x)
=
a t^2
+
2t\,\mathbf c\cdot\mathbf x
+
\mathbf x^\top B\mathbf x.
\]

Spatial rotational invariance for every \(R\in SO(3)\) requires

\[
\mathbf c=R\mathbf c
\]

for every R, hence

\[
\boxed{\mathbf c=0}.
\]

Likewise,

\[
B=R^\top BR
\]

for every rotation, so irreducibility of the defining three-dimensional rotation representation gives

\[
\boxed{B=bI_3}.
\]

Therefore every rotationally invariant quadratic form has the form

\[
\boxed{
Q(t,\mathbf x)=a t^2+b|\mathbf x|^2.
}
\]

If a and b have the same sign, Q is definite and has no nonzero null cone.

If a=0 or b=0, the form is degenerate.

Therefore a nondegenerate rotationally invariant quadratic form with nonzero null directions requires

\[
\boxed{
ab<0.
}
\]

Hence a genuine causal cone forces the scalar direction and the three spatial directions to carry opposite signs.

The Hermitian determinant fixes the normalization

\[
a=1,\qquad b=-1.
\]

## 5. The positive cone

The eigenvalues of

\[
X=tI+\mathbf x\cdot\boldsymbol\sigma
\]

are

\[
\boxed{
\lambda_\pm=t\pm|\mathbf x|.
}
\]

Thus

\[
X\succeq0
\quad\Longleftrightarrow\quad
t\ge|\mathbf x|.
\]

Define

\[
\boxed{
\mathcal C_+
=
\{X\in\operatorname{Herm}(2):X\succeq0\}.
}
\]

In Pauli coordinates,

\[
\boxed{
\mathcal C_+
=
\{(t,\mathbf x):t\ge|\mathbf x|\}.
}
\]

Its boundary is

\[
\det X=0,
\qquad
t\ge0,
\]

and its interior is

\[
\det X>0,
\qquad
t>0.
\]

Thus:

- timelike future displacement: \(\det X>0\);
- null future displacement: \(\det X=0\);
- spacelike displacement: \(\det X<0\).

## 6. The spatial-only no-go

Take a purely spatial element

\[
S=\mathbf x\cdot\boldsymbol\sigma
\in\operatorname{Herm}_0(2).
\]

Its eigenvalues are

\[
\pm|\mathbf x|.
\]

Therefore

\[
S\succeq0
\quad\Longleftrightarrow\quad
|\mathbf x|=0.
\]

Hence

\[
\boxed{
\operatorname{Herm}_0(2)\cap\mathcal C_+
=
\{0\}.
}
\]

This is the precise no-go statement:

\[
\boxed{
\text{the three-dimensional spatial distinction carrier alone admits no nonzero future causal displacement.}
}
\]

The one scalar identity component is exactly what turns the trivial spatial positivity cone into the nontrivial causal cone

\[
t\ge|\mathbf x|.
\]

This is the exact mathematical sense in which the spatial three-carrier requires the one scalar direction to support nontrivial causality.

## 7. Causality is a binary relation on endpoint pairs

Let \(\mathcal A\) be the affine event space modeled on \(\operatorname{Herm}(2)\).

Define

\[
\boxed{
A\preceq B
\quad\Longleftrightarrow\quad
B-A\in\mathcal C_+.
}
\]

This is a relation on two endpoints.

It is reflexive because

\[
0\in\mathcal C_+.
\]

It is antisymmetric because

\[
\mathcal C_+\cap(-\mathcal C_+)=\{0\}.
\]

It is transitive because the positive-semidefinite cone is closed under addition:

\[
B-A\in\mathcal C_+,
\qquad
C-B\in\mathcal C_+
\]

implies

\[
C-A=(C-B)+(B-A)\in\mathcal C_+.
\]

Equivalently, in Pauli coordinates,

\[
t_1\ge|\mathbf x_1|,
\qquad
t_2\ge|\mathbf x_2|
\]

gives

\[
t_1+t_2
\ge
|\mathbf x_1|+|\mathbf x_2|
\ge
|\mathbf x_1+\mathbf x_2|.
\]

Therefore the 3+1 cone composes causal relations exactly.

## 8. Why the factor one-half is forced

For two endpoints A,B, seek a centered representation

\[
A=M-H,
\qquad
B=M+H.
\]

Adding the two equations gives

\[
2M=A+B,
\]

hence

\[
\boxed{
M=\frac{A+B}{2}.
}
\]

Subtracting gives

\[
2H=B-A,
\]

hence

\[
\boxed{
H=\frac{B-A}{2}.
}
\]

So the factor \(1/2\) is not a convention.

It is uniquely forced by exact symmetric reconstruction of two endpoints around one center.

Under endpoint exchange,

\[
A\leftrightarrow B,
\]

one has

\[
M\mapsto M,
\qquad
H\mapsto-H.
\]

Thus M is the association center and H is the oriented dissociation.

## 9. Half-difference preserves causal class

Because

\[
H=\frac{B-A}{2}
\]

and two-by-two determinants scale quadratically,

\[
\det H
=
\frac14\det(B-A).
\]

Therefore

\[
\boxed{
\operatorname{sign}\det H
=
\operatorname{sign}\det(B-A).
}
\]

Also the positive cone is closed under multiplication by positive scalars, so

\[
\boxed{
B-A\in\mathcal C_+
\quad\Longleftrightarrow\quad
H\in\mathcal C_+.
}
\]

Hence dividing the relation by two centers the pair but does not change its causal type.

This gives the exact pair-level identity

\[
\boxed{
(A,B)
\longleftrightarrow
\left(
\frac{A+B}{2},
\frac{B-A}{2}
\right)
}
\]

while preserving causal orientation.

## 10. Composition in the centered relation variable

For three events A,B,C, define

\[
H_{AB}=\frac{B-A}{2},
\qquad
H_{BC}=\frac{C-B}{2},
\qquad
H_{AC}=\frac{C-A}{2}.
\]

Then

\[
\boxed{
H_{AC}=H_{AB}+H_{BC}.
}
\]

Therefore the half-difference representation preserves exact endpoint composition.

If

\[
H_{AB}\in\mathcal C_+,
\qquad
H_{BC}\in\mathcal C_+,
\]

then

\[
H_{AC}\in\mathcal C_+.
\]

So causality composes directly in the centered half-difference relation variable.

## 11. Main theorem

### Theorem — binary-Hermitian causal 3+1 pair closure

Assume:

1. the primitive local event-translation carrier is \(\operatorname{Herm}(2)\);
2. spatial relational directions are its traceless sector \(\operatorname{Herm}_0(2)\);
3. the future causal cone is the positive-semidefinite cone of Hermitian displacements.

Then:

\[
\boxed{
\operatorname{Herm}(2)
=
\mathbb RI
\oplus
\operatorname{Herm}_0(2)
\cong
\mathbb R^{1+3};
}
\]

\[
\boxed{
\det(tI+\mathbf x\cdot\boldsymbol\sigma)
=
t^2-|\mathbf x|^2;
}
\]

\[
\boxed{
\operatorname{Herm}_0(2)\cap\mathcal C_+
=
\{0\};
}
\]

\[
\boxed{
\mathcal C_+
=
\{(t,\mathbf x):t\ge|\mathbf x|\}
}
\]

is a nontrivial additive pointed cone;

\[
\boxed{
A\preceq B
\Longleftrightarrow
B-A\in\mathcal C_+
}
\]

defines a transitive causal partial order on endpoint pairs; and

\[
\boxed{
(A,B)
\longleftrightarrow
\left(
\frac{A+B}{2},
\frac{B-A}{2}
\right)
}
\]

is the unique centered two-endpoint decomposition, with the causal class preserved by the factor \(1/2\).

Thus, within the admitted primitive carrier,

\[
\boxed{
3_{\rm spatial}
+
1_{\rm scalar}
}
\]

is exactly what is required to turn the three-dimensional rotational relation carrier into a nontrivial composable causal order on pairs of endpoints.

## 12. What is proved and what is not

Proved exactly:

- real decomposition 1+3;
- rotational scalar versus rotational vector sectors;
- Minkowski determinant signature;
- necessity of opposite scalar/spatial signs for a nondegenerate rotationally invariant null cone;
- triviality of the spatial-only PSD causal cone;
- nontrivial future cone after adjoining the scalar direction;
- reflexivity, antisymmetry and transitivity of the cone order;
- uniqueness of midpoint/half-difference decomposition;
- preservation of causal class under division by two;
- exact additive composition in the half-difference variable.

Still conditional physically:

- that physical event translations are represented by \(\operatorname{Herm}(2)\);
- that the physical future relation is exactly the PSD cone order;
- the calibrated identification of the scalar coordinate with physical clock scale.

Therefore this theorem does not claim that abstract causality in every possible mathematical theory uniquely forces 3+1 dimensions.

It proves that once the already-derived TIR binary Hermitian carrier is admitted as the primitive event carrier, its internal algebra forces exactly the 1+3 Minkowski causal structure and the half-difference pair decomposition.

## 13. Claim classes

| Statement | Class |
|---|---|
| \(\operatorname{Herm}(2)=\mathbb RI\oplus\operatorname{Herm}_0(2)\) with dimensions \(1+3\) | EXACT |
| determinant is \(t^2-|\mathbf x|^2\) | EXACT |
| rotationally invariant nondegenerate null-cone form must have opposite scalar/spatial signs | EXACT CONDITIONAL ON SO(3) INVARIANCE |
| spatial-only PSD cone is \(\{0\}\) | EXACT |
| full PSD cone is \(t\ge|\mathbf x|\) | EXACT |
| PSD cone induces a partial order | EXACT |
| future cone is closed under composition | EXACT |
| midpoint/half-difference representation is unique | EXACT |
| division by two preserves causal type | EXACT |
| physical event carrier is \(\operatorname{Herm}(2)\) | PHYSICAL BINDING GATE |
| physical causality equals PSD cone order | PHYSICAL BINDING GATE |
