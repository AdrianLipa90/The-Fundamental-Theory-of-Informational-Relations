# TIR Polygonal Excitation — Stage 57 Platonic Triplet Tensor-Square v0.1

Status: `STAGE_57_ICOSAHEDRAL_TRIPLET_TENSOR_SQUARE_MATCH_PASS`

## Purpose

Stage 56 establishes that the five-dimensional spin-two family complement remains irreducible under the `N=5` rotational icosahedral group `A5`. Stage 57 tests whether the complete `3 + 5` family Lie-algebra decomposition is the tensor-square decomposition of the same Platonic rotational triplet.

## General SO(3) identity

For the three-dimensional vector/spin-one carrier `V`,

```math
V\otimes V
=\Lambda^2V\oplus\operatorname{Sym}^2V.
```

Under `SO(3)`,

```math
\Lambda^2V\cong V,
```

and

```math
\operatorname{Sym}^2V
\cong\mathbf1\oplus\operatorname{Sym}^2_0V,
```

where the traceless symmetric tensor has dimension five and is spin two. Thus

```math
\boxed{
\mathbf3\otimes\mathbf3
=\mathbf1\oplus\mathbf3\oplus\mathbf5.
}
```

Removing the scalar identity gives

```math
\operatorname{End}_0(V)
\cong\mathbf3\oplus\mathbf5,
```

which is the Stage 53--55 decomposition of `su(3)` under the embedded rotational subgroup.

## N=3: tetrahedral A4

For the tetrahedral rotational triplet,

```math
\mathbf3\otimes\mathbf3
=\mathbf1\oplus\mathbf1'\oplus\mathbf1''\oplus\mathbf3\oplus\mathbf3.
```

The antisymmetric part is one triplet,

```math
\Lambda^2\mathbf3=\mathbf3,
```

while

```math
\operatorname{Sym}^2\mathbf3
=\mathbf1\oplus\mathbf1'\oplus\mathbf1''\oplus\mathbf3.
```

Therefore the traceless symmetric five-dimensional sector splits as

```math
\mathbf1'\oplus\mathbf1''\oplus\mathbf3.
```

## N=4: octahedral S4

For the rotational three-dimensional irrep of the octahedral group,

```math
\mathbf3_{rot}\otimes\mathbf3_{rot}
=\mathbf1\oplus\mathbf2\oplus\mathbf3\oplus\mathbf3_{rot}.
```

The antisymmetric square returns the rotational triplet,

```math
\Lambda^2\mathbf3_{rot}=\mathbf3_{rot},
```

and

```math
\operatorname{Sym}^2\mathbf3_{rot}
=\mathbf1\oplus\mathbf2\oplus\mathbf3.
```

Hence the traceless symmetric sector is the reducible `2 + 3` found independently in Stage 56.

## N=5: icosahedral A5

For the icosahedral rotational triplet, use the class character

```math
\chi_3=(3,-1,0,\varphi,\bar\varphi),
```

where

```math
\varphi=\frac{1+\sqrt5}{2},
\qquad
\bar\varphi=\frac{1-\sqrt5}{2}.
```

The exact tensor-square character is

```math
\chi_3^2
=\chi_1+\chi_3+\chi_5.
```

Therefore

```math
\boxed{
\mathbf3\otimes\mathbf3
=\mathbf1\oplus\mathbf3\oplus\mathbf5.
}
```

with

```math
\boxed{\Lambda^2\mathbf3=\mathbf3}
```

and

```math
\boxed{\operatorname{Sym}^2\mathbf3=\mathbf1\oplus\mathbf5}.
```

Consequently

```math
\boxed{
\operatorname{Sym}^2_0\mathbf3=\mathbf5_{irr}.
}
```

## Exact bridge to the family Lie algebra

For `N=5`, the same decomposition can now be read in two independently obtained ways:

```text
Stage 53--55 continuous family algebra:
    su(3)_F under SO(3) = 3 + 5

Stage 57 finite icosahedral tensor algebra:
    End_0(3_A5) = Lambda^2(3) + Sym^2_0(3) = 3 + 5
```

The five-dimensional factor is the same representation type: traceless symmetric rank-two tensors / spin-two carrier, and Stage 56 establishes that it remains irreducible under `A5`.

## Result

The `N=5` icosahedral triplet reproduces the entire representation pattern underlying the family `su(3)` decomposition:

```math
\boxed{
\operatorname{End}_0(\mathbf3_{A_5})
=\mathbf3\oplus\mathbf5.
}
```

At `N=3` and `N=4` the analogous five-dimensional symmetric-traceless sector splits further.

## Boundary

This is an exact representation-theoretic identity. It does not equate the finite group `A5` with the continuous gauge/family group `SU(3)_F`, nor does it assign the finite irreps to physical particles without a separate dynamical map.

No CKM or mass data are used.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/platonic_triplet_tensor_square_stage57_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE57_PLATONIC_TRIPLET_TENSOR_SQUARE_RECEIPT_V0_1.json`
