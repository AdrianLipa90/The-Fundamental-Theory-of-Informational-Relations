# TIR Polygonal Excitation — Stage 55 SU(3)/SO(3) Symmetric-Pair Closure v0.1

Status: `STAGE_55_SU3_SO3_SYMMETRIC_PAIR_PASS`

## Purpose

Stages 52--54 establish an embedded spin-one compact subgroup and the decomposition

```math
\mathfrak{su}(3)_F=\mathfrak k\oplus\mathfrak p,
\qquad
\dim\mathfrak k=3,
\qquad
\dim\mathfrak p=5.
```

Stage 55 tests the bracket structure of this decomposition.

## Compact subgroup

The spin-one representation of `SU(2)` has kernel `{+I,-I}`. Its image is therefore

```math
SU(2)/\mathbb Z_2\cong SO(3).
```

Thus the three-dimensional subalgebra from Stage 52 is

```math
\mathfrak k\cong\mathfrak{so}(3).
```

The five-dimensional Stage 53 complement is denoted `p`.

## Casimir projectors

Let

```math
\mathcal C(X)=\sum_a[J_a,[J_a,X]].
```

Stage 54 gives eigenvalue `2` on the spin-one sector and `6` on the spin-two sector. Hence exact polynomial projectors on the traceless Hermitian carrier are

```math
P_{\mathfrak k}=\frac{6I-\mathcal C}{4},
```

and

```math
P_{\mathfrak p}=\frac{\mathcal C-2I}{4}.
```

They have ranks three and five respectively.

## Symmetric-pair bracket relations

Using the Hermitian-generator bracket

```math
[A,B]_H=-i(AB-BA),
```

computational closure on independent bases of the two projected sectors gives

```math
\boxed{[\mathfrak k,\mathfrak k]\subset\mathfrak k},
```

```math
\boxed{[\mathfrak k,\mathfrak p]\subset\mathfrak p},
```

and

```math
\boxed{[\mathfrak p,\mathfrak p]\subset\mathfrak k}.
```

Maximum Hilbert-space matrix residuals in the forbidden projected sectors are below `8e-16`.

These are precisely the defining Lie-algebra relations of a compact symmetric pair.

## Geometric identification

The pair is the standard compact symmetric pair

```math
\boxed{(\mathfrak{su}(3),\mathfrak{so}(3))}.
```

Therefore the five-dimensional complement is the tangent representation of the symmetric space

```math
\boxed{SU(3)/SO(3)},
```

whose dimension is

```math
8-3=5.
```

Under the embedded `SO(3)` this tangent space is the irreducible spin-two carrier established in Stage 53.

## Mixing-structure consequence

Stage 53 proves that the `SO(3)` subgroup alone has rephasing-invariant `J=0`. Stage 55 now gives a precise geometric location of the additional family directions:

```text
SO(3) subgroup      -> three compact spin-one directions
SU(3)/SO(3) tangent -> five spin-two complement directions
full SU(3)_F        -> closure of both sectors
```

A nonzero complement coordinate is necessary to leave the CP-trivial spin-one subgroup, although nonzero complement alone is not asserted to be sufficient for a physical CP phase.

## Boundary

This stage is a group/representation result. It makes no particle assignment to the five-dimensional tangent sector and does not identify it with polygon level `N=5` without a separate finite-symmetry restriction test.

No CKM or mass data are used.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/su3_so3_symmetric_pair_stage55_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE55_SU3_SO3_SYMMETRIC_PAIR_RECEIPT_V0_1.json`
