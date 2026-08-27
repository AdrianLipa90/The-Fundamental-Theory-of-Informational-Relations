# TIR Polygonal Excitation — Stage 52 Compact Real-Form Sym2 Bridge v0.1

Status: `STAGE_52_COMPACT_REAL_FORM_SYM2_BRIDGE_PASS_SELECTION_OPEN`

## Purpose

Stage 51 proves that the Stage 50 split-real representation cannot be converted into `SU(3)_F` by a fixed similarity transformation. Stage 52 tests the mathematically distinct route through complexification and change of real form.

## Complexification and real forms

The split real Lie algebra and compact Lie algebra have the same complexification:

```math
\mathfrak{sl}(2,\mathbb R)\otimes\mathbb C
\cong
\mathfrak{sl}(2,\mathbb C)
\cong
\mathfrak{su}(2)\otimes\mathbb C.
```

Thus the Stage 49/50 split-real branch geometry and a compact `SU(2)` representation can be related only after passing through the common complex algebra. This is a change of real form, not a change of basis inside the original real representation.

## Symmetric square of the compact fundamental

Let the spin-one generators on the basis `m=+1,0,-1` be

```math
J_z=\begin{pmatrix}1&0&0\\0&0&0\\0&0&-1\end{pmatrix},
```

```math
J_x=\frac1{\sqrt2}
\begin{pmatrix}
0&1&0\\
1&0&1\\
0&1&0
\end{pmatrix},
```

and

```math
J_y=\frac1{\sqrt2}
\begin{pmatrix}
0&-i&0\\
i&0&-i\\
0&i&0
\end{pmatrix}.
```

They satisfy

```math
[J_x,J_y]=iJ_z,
\qquad
[J_y,J_z]=iJ_x,
\qquad
[J_z,J_x]=iJ_y.
```

All `J_a` are Hermitian and traceless. Therefore

```math
T_a=-iJ_a
```

are anti-Hermitian and traceless, hence

```math
T_a\in\mathfrak{su}(3).
```

They generate the three-dimensional spin-one image of `SU(2)`:

```math
\boxed{
\operatorname{Sym}^2(SU(2))\subset SU(3).
}
```

## Relation to Stage 50

The Stage 50 polynomial representation and the present compact spin-one representation are two real-form realizations associated with the same complex representation of `sl(2,C)`:

```text
split real form:   Sym^2(SL(2,R)) -> SO(1,2)-type carrier
compact real form: Sym^2(SU(2))   -> SO(3)-type subgroup of SU(3)
```

The first preserves an indefinite quadratic form; the second preserves a positive-definite Hermitian norm.

## Result

There is a mathematically valid three-dimensional compact bridge into the family-unitary group:

```math
\boxed{
\mathfrak{sl}(2,\mathbb R)
\xrightarrow{\text{complexify}}
\mathfrak{sl}(2,\mathbb C)
\xleftarrow{\text{compact real form}}
\mathfrak{su}(2)
\xrightarrow{\operatorname{Sym}^2}
\mathfrak{su}(3).
}
```

This resolves the representation-dimension mismatch without contradicting the Stage 51 no-go, because the operation is a change of real form rather than a similarity unitarization of the split-real generators.

## Selection boundary

The current TIR branch does not yet contain a derived rule selecting the compact real form from the Collatz/Poincaré split-real dynamics. Therefore Stage 52 establishes availability of the compact bridge, not its dynamical selection.

No CKM or mass input is used.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/compact_real_form_sym2_stage52_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE52_COMPACT_REAL_FORM_SYM2_RECEIPT_V0_1.json`
