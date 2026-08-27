# TIR Polygonal Excitation — Stage 31 White-Thread Unitarity Audit v0.1

Status: `STAGE_31_WHITE_THREAD_STRUCTURAL_SIGNAL_PASS__DIRECT_MIXING_PROMOTION_BLOCKED`

## Frozen input

Use the existing v3.5 oriented open-holonomy overlaps, generated without observed masses, CKM, PMNS, old tau values, or fitted White-Thread values. Ordered as `(u,c,t)` rows and `(d,s,b)` columns,

```math
W_{open}=\begin{pmatrix}
0.409236985904&0.421257516041&0.247216544993\\
0.242738601882&0.236196188784&0.415445232193\\
0.265342576446&0.269575190990&0.376337259622
\end{pmatrix}.
```

The source itself labels every entry `structural_open_holonomy_only_not_CKM`.

## Singular spectrum

The singular values are

```math
\sigma(W_{open})\approx
(0.9654226674,\ 0.2144876181,\ 0.0039458125).
```

Thus the matrix is full rank numerically but has one very small singular direction.

## Direct unitarity gate

```math
\|W_{open}^TW_{open}-I_3\|_{\max}
\approx0.7031963776.
```

Therefore the open-holonomy overlap matrix is a structural coherence/overlap object rather than a unitary family-basis transformation.

Its determinant is

```math
\det W_{open}\approx-8.1706417\times10^{-4}.
```

The unique orthogonal polar factor exists because the matrix is nonsingular, but the raw-to-polar Frobenius distance is approximately `1.2689953658` and the polar determinant is `-1`.

## Result

The White-Thread layer preserves a mass-free structural relation between the up and down sectors, but it does not by itself close the unitary family-mixing gate. Any later CKM construction must contain an additional independently derived unitary transport / diagonalization step rather than renaming the overlap matrix.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/white_thread_unitarity_stage31_v01.py`
