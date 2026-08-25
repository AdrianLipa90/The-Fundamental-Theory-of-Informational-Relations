# TIR Polygonal Excitation — Stage 30 Pre-CKM Cross-Gram Audit v0.1

Status: `STAGE_30_SECTOR_MISALIGNMENT_PASS__DIRECT_MIXING_PROMOTION_OPEN`

## Frozen input

Use the existing mass-free v3.4 cross-Gram matrix, whose repository label is explicitly `up_down_basis_overlap_not_CKM`:

```math
O=
\begin{pmatrix}
0.413565262551 & 0.172725480915 & -0.0920240308652\\
-0.178658169914 & -0.407201857972 & 0.859711828535\\
0.0375262746218 & 0.242736185591 & 0.137317039768
\end{pmatrix}.
```

The underlying Gram-Schmidt construction did not enter its deterministic degeneracy perturbation branch for the active up/down vectors; the orthogonalization residual norms remain finite and well above the `1e-10` guard.

## Rank and principal-angle spectrum

The matrix has full rank three. Its singular values are

```math
\sigma(O)=
(0.99996350,\ 0.41238767,\ 0.23530772).
```

For two orthonormal 3-frames embedded in the larger structural feature space, these singular values are the cosines of their principal angles. Thus the v3.4 construction contains genuine sector misalignment.

## Unitarity gate

Direct unitarity fails:

```math
\|O^TO-I_3\|_{\max}=0.795636810647112.
```

Therefore the frozen cross-Gram is a contraction between two different three-dimensional subspaces, rather than a unitary change of basis inside one common three-dimensional family space.

## Canonical polar factor

Because `O` is invertible, it has a unique orthogonal polar factor

```math
R=O(O^TO)^{-1/2}.
```

Numerically,

```math
R\approx
\begin{pmatrix}
0.99342537&0.09621794&0.06203337\\
-0.01488255&-0.42872325&0.90331328\\
-0.11351009&0.89829755&0.42447258
\end{pmatrix},
```

with

```math
R^TR=I_3,
\qquad
\det R=-1.
```

The Frobenius distance is

```math
\|O-R\|_F=0.9643871290605233.
```

The polar factor is a canonical mathematical diagnostic. Promotion of this orientation-reversing factor, or a rephased determinant-one version, to a physical family-mixing operator requires an independently derived TIR rule.

## Result

The existing TIR pre-mass orientation satisfies the Stage 29 necessity condition by producing nontrivial up/down sector misalignment. The same audit blocks direct identification of the raw cross-Gram with a physical unitary mixing matrix.

This preserves the structural signal while keeping the next operator-selection step prospective.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/preckm_cross_gram_stage30_v01.py`
