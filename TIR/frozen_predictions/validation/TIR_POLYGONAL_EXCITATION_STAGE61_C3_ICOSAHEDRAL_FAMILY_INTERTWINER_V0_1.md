# TIR Polygonal Excitation — Stage 61 C3-Compatible Icosahedral Family Intertwiner v0.1

Status: `STAGE_61_C3_ICOSAHEDRAL_FAMILY_INTERTWINER_PASS`

## Purpose

Stages 58--60 identify the `N=5` five-dimensional carrier and its invariant structure. Stage 61 tests whether the previously frozen family operators `P3`, `A_seed`, and the ordered polygonal axis `D` admit an explicit parameter-free realization inside the same six-axis icosahedral quadrupole geometry.

No CKM entries, masses, fitted coefficients, or amplitude kernels are used.

## C3-compatible icosahedral embedding

Use the standard six unoriented icosahedral axes obtained from the 12 vertices

```math
(0,\pm1,\pm\varphi),
(\pm1,\pm\varphi,0),
(\pm\varphi,0,\pm1),
```

with `phi=(1+sqrt(5))/2`, labelled as `u_0,...,u_5` in the executable.

Use the frozen family cycle

```math
P_3=\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{pmatrix}.
```

This matrix is an orientation-preserving icosahedral symmetry and permutes the six axes as

```math
(0\;2\;1)(3\;5\;4).
```

Thus the six-axis carrier splits into two `C3` orbits of length three.

## Pair-sum / pair-difference decomposition

Pair the axes as

```text
(0,3), (1,4), (2,5).
```

Let

```math
Q_a=u_au_a^T-\frac13I
```

be the Stage 58 quadrupoles.

The three pair differences are exactly

```math
Q_0-Q_3=\frac{2}{\sqrt5}(E_{23}+E_{32}),
```

```math
Q_1-Q_4=\frac{2}{\sqrt5}(E_{12}+E_{21}),
```

```math
Q_2-Q_5=\frac{2}{\sqrt5}(E_{13}+E_{31}).
```

Therefore

```math
\operatorname{span}\{Q_i-Q_{i+3}\}_{i=0}^2
```

is exactly the three-dimensional off-diagonal real-symmetric sector.

The three pair sums

```math
Q_i+Q_{i+3}
```

are diagonal, satisfy one linear relation inherited from `sum_a Q_a=0`, and have span dimension two. They therefore equal the complete diagonal traceless sector.

Hence

```math
\boxed{
\operatorname{Sym}^2_0(\mathbb R^3)
=
\underbrace{\operatorname{span}\{Q_i-Q_{i+3}\}}_{3\;\mathrm{offdiag}}
\oplus
\underbrace{\operatorname{span}\{Q_i+Q_{i+3}\}}_{2\;\mathrm{diag}}.
}
```

The executable obtains ranks `3`, `2`, and total direct-sum rank `5`.

## Exact seed-incidence map

The frozen Stage 41 seed-incidence operator is

```math
A_{seed}=\begin{pmatrix}
0&1/2&0\\
1/2&0&0\\
0&0&0
\end{pmatrix}.
```

Using the exact pair-difference identity above,

```math
\boxed{
A_{seed}=\frac{\sqrt5}{4}(Q_1-Q_4).
}
```

Conjugating by `P3` generates the other two off-diagonal channels, so the complete `C3` orbit of `A_seed` has rank three and equals the pair-difference sector.

## Exact ordered-axis map

Let

```math
D=\operatorname{diag}\left(-\frac13,0,\frac1{\sqrt5}\right)
```

and remove its trace:

```math
D_0=D-\frac{\operatorname{tr}D}{3}I.
```

Define

```math
\alpha=\frac{19+3\sqrt5}{72},
\qquad
\beta=-\frac{5+3\sqrt5}{72},
\qquad
\gamma=-\frac7{36}.
```

These satisfy

```math
\alpha+\beta+\gamma=0.
```

The exact quadrupole reconstruction is

```math
\boxed{
D_0=
\alpha(Q_0+Q_3)
+\beta(Q_1+Q_4)
+\gamma(Q_2+Q_5).
}
```

Thus `D_0` lies entirely in the pair-sum / diagonal sector. Its `C3` orbit has rank two and spans that complete sector.

## Combined result

The two pre-existing TIR structures now fill complementary pieces of the same icosahedral five-dimensional carrier:

```text
C3 orbit of A_seed -> 3D pair-difference / off-diagonal sector
C3 orbit of D_0    -> 2D pair-sum / diagonal-traceless sector
```

Therefore

```math
\boxed{
\operatorname{span}\left(
\operatorname{Orb}_{C_3}(A_{seed})
\cup
\operatorname{Orb}_{C_3}(D_0)
\right)
=
\operatorname{Sym}^2_0(\mathbb R^3)
\cong\mathbf5_{A_5}.
}
```

This supplies an explicit `C3`-compatible intertwiner between the previously frozen family operators and the `N=5` icosahedral quadrupole realization.

## Boundary

The explicit compatible embedding is established. Uniqueness among all conjugate `A5` embeddings compatible with the same `C3` generator remains a separate gate.

## Evidential status

```text
P3 acts as icosahedral order-3 symmetry: PASS
six axes split into two C3 triples: PASS
pair-difference rank: 3
pair-sum rank: 2
combined rank: 5
A_seed exact quadrupole identity: PASS
D_0 exact pair-sum reconstruction: PASS
CKM input: NONE
mass input: NONE
fitted coefficients: NONE
```

## Reproducibility

Executable:

`TIR/frozen_predictions/validation/scripts/c3_icosahedral_family_intertwiner_stage61_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE61_C3_ICOSAHEDRAL_FAMILY_INTERTWINER_RECEIPT_V0_1.json`
