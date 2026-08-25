# TIR Polygonal Excitation — Stage 49 Collatz Möbius / Poincaré Lift v0.1

Status: `STAGE_49_COLLATZ_MOBIUS_POINCARE_LIFT_PASS`

## Purpose

Stage 48 encoded each frozen Collatz path as an exact word in two branch symbols. Stage 49 asks whether those branch maps already possess a canonical geometric representation before any family-space operator is introduced.

They do: both Collatz branches are real Möbius transformations.

## Branch maps as projective matrices

For the even branch

```math
E(x)=\frac{x}{2},
```

use the projective matrix

```math
M_E\sim\begin{pmatrix}1&0\\0&2\end{pmatrix}.
```

For the odd branch

```math
O(x)=3x+1,
```

use

```math
M_O\sim\begin{pmatrix}3&1\\0&1\end{pmatrix}.
```

A nonzero scalar multiple represents the same Möbius map. Normalizing each positive determinant to one gives

```math
\widehat M_E=
\begin{pmatrix}
1/\sqrt2&0\\
0&\sqrt2
\end{pmatrix},
```

and

```math
\widehat M_O=
\frac1{\sqrt3}
\begin{pmatrix}
3&1\\
0&1
\end{pmatrix}.
```

Therefore

```math
\widehat M_E,\widehat M_O\in SL(2,\mathbb R),
```

and their projective actions lie in `PSL(2,R)`.

## Hyperbolic action

For

```math
g=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL(2,\mathbb R),
```

the standard action on the upper half-plane is

```math
z\mapsto\frac{az+b}{cz+d}.
```

Its imaginary part transforms as

```math
\operatorname{Im}(gz)=\frac{\operatorname{Im}z}{|cz+d|^2}>0,
```

so the upper half-plane is preserved.

On the real boundary, the two normalized matrices act exactly as the original Collatz affine branches.

The Cayley transform

```math
w=\frac{z-i}{z+i}
```

conjugates this action to the Poincaré disk. Consequently every finite Collatz branch word determines a canonical orientation-preserving hyperbolic disk isometry.

## Branch type

The normalized traces are

```math
\operatorname{tr}(\widehat M_E)=\frac3{\sqrt2}>2,
```

and

```math
\operatorname{tr}(\widehat M_O)=\frac4{\sqrt3}>2.
```

Thus both branch generators are hyperbolic elements of `PSL(2,R)`.

## Exact word maps to the Stage 47 common seed

For the first family word

```text
w1 = OEOE
```

the exact affine composite is

```math
x\mapsto\frac94x+\frac54,
```

so

```math
15\mapsto35.
```

For the middle seed the empty word is the identity.

For the 90-step third-family word, the exact affine composite is

```math
x\mapsto
\frac{3^{34}}{2^{56}}x
+
\frac{137178808275158393}{72057594037927936},
```

where

```math
3^{34}=16677181699666569,
\qquad
2^{56}=72057594037927936.
```

Substitution gives exactly

```math
143\mapsto35.
```

The slope `3^34/2^56` is fixed solely by the exact odd/even branch counts; the translation term retains the full branch ordering information.

## Result

There is a canonical geometric lift

```math
\boxed{
\{E,O\}^*
\longrightarrow
PSL(2,\mathbb R)
\longrightarrow
\operatorname{Isom}^+(\mathbb D_{\rm Poincare}).
}
```

Therefore the Collatz words found in Stage 48 already act naturally on hyperbolic geometry. No distance-to-amplitude kernel and no CKM input is required for this statement.

## Boundary

The Möbius/Poincaré representation is a two-dimensional projective/hyperbolic representation. Stage 49 does not identify it with the three-dimensional unitary family carrier `SU(3)_F`.

The relationship between this exact hyperbolic representation and the already-derived three-dimensional family carrier is a separate gate.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/collatz_mobius_poincare_stage49_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE49_COLLATZ_MOBIUS_POINCARE_RECEIPT_V0_1.json`
