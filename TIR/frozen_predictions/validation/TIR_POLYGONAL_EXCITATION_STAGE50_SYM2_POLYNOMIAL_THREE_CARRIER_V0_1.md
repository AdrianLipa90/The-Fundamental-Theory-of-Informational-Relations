# TIR Polygonal Excitation — Stage 50 Symmetric-Square Polynomial Three-Carrier v0.1

Status: `STAGE_50_SYM2_POLYNOMIAL_THREE_CARRIER_PASS_WITH_SIGNATURE_SEPARATION`

## Purpose

Stage 49 established a canonical two-dimensional Möbius representation of the Collatz branch alphabet in `PSL(2,R)`. Stage 50 applies the standard symmetric-square representation to determine whether the same branch dynamics has a canonical three-dimensional polynomial carrier.

## Binary quadratic carrier

Write a symmetric rank-two tensor / binary quadratic as

```math
S=\begin{pmatrix}x&y\\y&z\end{pmatrix},
```

or equivalently

```math
q(X,Y)=xX^2+2yXY+zY^2.
```

The coefficient vector is

```math
v=(x,y,z)^T\in\mathbb R^3.
```

For

```math
M=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL(2,\mathbb R),
```

act by

```math
S\mapsto MSM^T.
```

On `v`, this is the symmetric-square representation

```math
\rho_2(M)=
\begin{pmatrix}
a^2&2ab&b^2\\
ac&ad+bc&bd\\
c^2&2cd&d^2
\end{pmatrix}.
```

It obeys

```math
\rho_2(M_1M_2)=\rho_2(M_1)\rho_2(M_2)
```

and

```math
\det\rho_2(M)=(\det M)^3=1.
```

Thus the Stage 49 Collatz word representation has a canonical three-dimensional polynomial lift.

## Exact even-branch matrix

For

```math
\widehat M_E=
\begin{pmatrix}
1/\sqrt2&0\\
0&\sqrt2
\end{pmatrix},
```

the symmetric square is exactly rational:

```math
\boxed{
R_E=\rho_2(\widehat M_E)=
\begin{pmatrix}
1/2&0&0\\
0&1&0\\
0&0&2
\end{pmatrix}.
}
```

## Exact odd-branch matrix

For

```math
\widehat M_O=
\frac1{\sqrt3}
\begin{pmatrix}
3&1\\
0&1
\end{pmatrix},
```

the symmetric square again becomes exactly rational:

```math
\boxed{
R_O=\rho_2(\widehat M_O)=
\begin{pmatrix}
3&2&1/3\\
0&1&1/3\\
0&0&1/3
\end{pmatrix}.
}
```

Both have determinant one.

## Preserved polynomial invariant

The determinant of the symmetric tensor is

```math
Q(x,y,z)=xz-y^2.
```

Equivalently

```math
Q(v)=v^T Jv,
```

with

```math
J=
\begin{pmatrix}
0&0&1/2\\
0&-1&0\\
1/2&0&0
\end{pmatrix}.
```

Exact rational arithmetic gives

```math
\boxed{R_E^TJR_E=J},
```

and

```math
\boxed{R_O^TJ R_O=J}.
```

Therefore the canonical three-dimensional lift preserves an indefinite quadratic form of signature `(1,2)` up to overall sign convention. The image lies in a real `SO(1,2)`-type subgroup of `SL(3,R)`.

## Polynomial meaning

The lift is not an added dimensional label. It is forced by the action of Möbius transformations on degree-two binary polynomials / symmetric tensors:

```math
\boxed{
SL(2,\mathbb R)
\xrightarrow{\operatorname{Sym}^2}
SL(3,\mathbb R).
}
```

Thus the exact Collatz/Poincaré dynamics from Stage 49 canonically induces a three-component polynomial carrier.

## Relation to the existing family triplet

Both the exceptional family carrier and the symmetric-square carrier have dimension three, but their preserved metrics differ:

- the Stage 50 carrier preserves the indefinite form `xz-y^2`;
- the previously derived `SU(3)_F` carrier preserves a positive-definite Hermitian form.

Accordingly, dimension equality alone does not identify the two representations.

The exact result is a bridge candidate at the level of carrier dimension and polynomial action, with a mathematically explicit signature separation that must be resolved by a later complex/unitary lift if the two structures are to be related.

## Boundary

Stage 50 does not promote `SO(1,2)` to `SU(3)_F`, does not claim a physical family identification, and uses no CKM or mass data.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/sym2_polynomial_three_carrier_stage50_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE50_SYM2_POLYNOMIAL_THREE_CARRIER_RECEIPT_V0_1.json`
