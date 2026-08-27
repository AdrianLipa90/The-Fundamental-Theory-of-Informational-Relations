# TIR Polygonal Excitation — Stage 62 Family-Icosahedral Embedding Rigidity v0.1

Status: `STAGE_62_FAMILY_ICOSAHEDRAL_EMBEDDING_RIGIDITY_PASS`

## Purpose

Stage 61 constructs an explicit `C3`-compatible embedding of the frozen family operators into the `N=5` icosahedral quadrupole carrier. Stage 62 tests whether a continuous relative orientation remains after simultaneously preserving the frozen family cycle `P3`, the ordered polygonal axis `D0`, and the distinguished seed-incidence channel `A_seed`.

No CKM entries, masses, fitted coefficients, or amplitude kernels are used.

## Centralizer of the family cycle

The frozen family cycle

```math
P_3=\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{pmatrix}
```

is a rotation by `2pi/3` around the unit axis

```math
n=\frac1{\sqrt3}(1,1,1).
```

Within `SO(3)`, every orientation change that keeps this same `P3` generator fixed must belong to its centralizer, i.e. a rotation around the same axis `n`.

Thus before imposing the remaining frozen operators there is a continuous one-parameter orientation freedom.

## Ordered-axis rigidity

The Stage 61 ordered family operator is

```math
D_0
=\operatorname{diag}\left(-\frac13,0,\frac1{\sqrt5}\right)
-\frac13\operatorname{tr}\left[\operatorname{diag}\left(-\frac13,0,\frac1{\sqrt5}\right)\right]I.
```

Its three eigenvalues are distinct.

If a rotation `R` preserves the Stage 61 statement that `D0` lies in the pair-sum / diagonal sector, then

```math
R^TD_0R
```

must remain diagonal in the canonical family basis.

Because `D0` has a simple spectrum, the columns of `R` must therefore be eigenvectors of `D0`. Hence `R` must be an orientation-preserving signed permutation matrix.

Requiring simultaneously

```math
Rn=n
```

leaves exactly three such matrices:

```math
\boxed{R\in\{I,P_3,P_3^2\}.}
```

The executable independently enumerates all orientation-preserving signed permutation matrices and obtains exactly these three solutions.

Therefore the continuous centralizer is reduced to the discrete subgroup

```math
\boxed{C_3.}
```

## Seed-incidence label fixing

The frozen Stage 41 incidence operator is

```math
A_{seed}=\frac12(E_{12}+E_{21}),
```

which specifically represents the distinguished `1 <-> 2` family channel.

Under the residual three rotations,

```math
P_3^k A_{seed}(P_3^k)^T,
\qquad k=0,1,2,
```

the operator cycles through the three off-diagonal family channels.

Only

```math
k=0
```

preserves the exact labelled matrix `A_seed`.

Thus once the Stage 22 family ordering and the Stage 41 distinguished `1 <-> 2` channel are held fixed, the residual `C3` relabelling is removed.

## Result

The Stage 61 embedding has no continuous orientation parameter after the frozen family data are imposed:

```math
\boxed{
(P_3,D_0)\ \Rightarrow\ \text{orientation freedom }C_3,
}
```

and

```math
\boxed{
(P_3,D_0,A_{seed}\text{ with fixed family labels})
\ \Rightarrow\ \text{single labelled embedding}.
}
```

This closes the orientation-rigidity gate without reference to CKM or masses.

## Evidential status

```text
D0 simple spectrum: PASS
SO(3) centralizer of P3: one-axis rotations
signed-permutation solutions fixing n: 3
solutions: I, P3, P3^2
continuous orientation freedom after D0: NONE
residual C3 label freedom after fixed A_seed: NONE
CKM input: NONE
mass input: NONE
fitted coefficients: NONE
```

## Reproducibility

Executable:

`TIR/frozen_predictions/validation/scripts/family_icosahedral_embedding_rigidity_stage62_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE62_FAMILY_ICOSAHEDRAL_EMBEDDING_RIGIDITY_RECEIPT_V0_1.json`
