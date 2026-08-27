# TIR Polygonal Excitation — Stage 51 Symmetric-Square Unitarization No-Go v0.1

Status: `STAGE_51_POSITIVE_HERMITIAN_UNITARIZATION_NO_GO_PASS`

## Purpose

Stage 50 produced a canonical three-dimensional polynomial representation of the Collatz/Poincaré branch dynamics. Stage 51 tests whether that representation can be converted into the already-derived `SU(3)_F` carrier by a fixed change of basis.

The test is whether there exists a positive-definite Hermitian form `H` preserved by both Stage 50 generators.

## Immediate spectral obstruction

The even-branch polynomial generator is

```math
R_E=\operatorname{diag}(1/2,1,2).
```

Its eigenvalues are

```math
\{1/2,1,2\}.
```

A matrix preserving a positive-definite Hermitian form is similar to a unitary matrix and therefore has all eigenvalues on the unit circle.

Because `1/2` and `2` do not have unit modulus, no similarity transformation can turn `R_E` into a unitary matrix.

Hence the full Stage 50 representation cannot be conjugated into `SU(3)` while preserving the same group action.

## Exact invariant-form calculation

Let a real symmetric invariant form be

```math
H=H^T.
```

The equation

```math
R_E^T H R_E=H
```

with eigenvalue scales `(1/2,1,2)` forces

```math
H=\begin{pmatrix}
0&0&a\\
0&b&0\\
a&0&0
\end{pmatrix}.
```

Now impose the odd-branch condition

```math
R_O^T H R_O=H,
```

where

```math
R_O=
\begin{pmatrix}
3&2&1/3\\
0&1&1/3\\
0&0&1/3
\end{pmatrix}.
```

Exact arithmetic gives

```math
b=-2a.
```

Therefore every nondegenerate common invariant real symmetric form is proportional to

```math
\boxed{
H_0=\begin{pmatrix}
0&0&1\\
0&-2&0\\
1&0&0
\end{pmatrix}.
}
```

This is exactly the Stage 50 discriminant form up to scale.

Its eigenvalues are

```math
\{1,-1,-2\}
```

up to overall scale, so the form is necessarily indefinite.

## Result

The canonical polynomial lift has a unique nondegenerate invariant symmetric form up to scale, and that form is indefinite.

Therefore

```math
\boxed{
\operatorname{Sym}^2(\text{Collatz }PSL(2,\mathbb R))
\not\sim
SU(3)_F
}
```

by any fixed similarity transformation preserving the same representation.

The three-dimensional dimension match found in Stage 50 is genuine, but direct unitarization is mathematically obstructed.

## Consequence for the next gate

Any bridge to the compact unitary family carrier must change more than basis. It must introduce a distinct real-form selection / complex holonomy / compactification mechanism.

This agrees structurally with Stage 36, where non-removable complex holonomy was required for `J != 0`.

## Boundary

Stage 51 is a representation-theoretic no-go for direct positive-definite unitarization of the Stage 50 generators. It does not exclude a different representation obtained after complexification or a physically motivated change of real form.

No CKM or mass data are used.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/sym2_unitarization_nogo_stage51_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE51_SYM2_UNITARIZATION_NOGO_RECEIPT_V0_1.json`
