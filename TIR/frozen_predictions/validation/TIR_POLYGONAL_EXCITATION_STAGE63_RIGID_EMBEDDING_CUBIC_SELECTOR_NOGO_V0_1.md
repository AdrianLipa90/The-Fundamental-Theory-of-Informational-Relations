# TIR Polygonal Excitation — Stage 63 Rigid-Embedding Cubic Selector No-Go v0.1

Status: `STAGE_63_RIGID_EMBEDDING_CUBIC_SELECTOR_NONUNIQUENESS_PASS`

## Purpose

Stage 60 established that the five-dimensional `A5` carrier has a two-dimensional cubic invariant space. Stages 61–62 then fixed a parameter-free and rigid embedding of the frozen TIR family operators into that carrier. Stage 63 tests whether the already frozen operators `A_seed` and `D0` reduce the two cubic invariant directions to one without adding a new scalar condition.

No CKM entries, masses, fitted coefficients, or amplitude kernels are used.

## Frozen operators

Use

```math
A=A_{seed}=\frac12(E_{12}+E_{21}),
```

and

```math
D_0=\operatorname{diag}\left(-\frac13,0,\frac1{\sqrt5}\right)
-\frac13\operatorname{tr}\!\left[\operatorname{diag}\left(-\frac13,0,\frac1{\sqrt5}\right)\right]I.
```

The Stage-60 cubic invariants are

```math
I_{iso}(S)=\operatorname{tr}(S^3),
```

and

```math
I_{A5}(S)=\sum_{a=1}^{6}\left[\operatorname{tr}(SQ_a)\right]^3.
```

Let `T_iso` and `T_A5` denote their symmetric trilinear polarizations.

## Exact probe values

The pure `A` cubic and the mixed `A D^2` channel vanish for both invariant directions:

```math
T_{iso}(A,A,A)=T_{A5}(A,A,A)=0,
```

```math
T_{iso}(A,D_0,D_0)=T_{A5}(A,D_0,D_0)=0.
```

The two non-zero frozen probe channels are

```math
T_{iso}(D_0,D_0,D_0)
=\frac{\sqrt5}{675}+\frac{17}{1215},
```

```math
T_{A5}(D_0,D_0,D_0)
=\frac{98}{6075}+\frac{28\sqrt5}{3375},
```

and

```math
T_{iso}(A,A,D_0)
=-\frac{\sqrt5}{30}-\frac1{36},
```

```math
T_{A5}(A,A,D_0)
=-\frac{\sqrt5}{75}-\frac1{45}.
```

Form the evaluation matrix

```math
M_{probe}=
\begin{pmatrix}
T_{iso}(D_0,D_0,D_0) & T_{A5}(D_0,D_0,D_0)\\
T_{iso}(A,A,D_0) & T_{A5}(A,A,D_0)
\end{pmatrix}.
```

Its determinant is exactly

```math
\boxed{
\det M_{probe}
=\frac{100\sqrt5+259}{182250}
>0.
}
```

Therefore

```math
\boxed{\operatorname{rank}M_{probe}=2.}
```

## Result

The rigid Stage-61/62 embedding does not collapse the two-dimensional cubic invariant space to a unique one-dimensional action. Instead, the frozen operators distinguish both invariant directions independently.

Thus geometry plus embedding rigidity supplies the carrier and fixes its orientation, but a unique cubic family action still requires one additional scalar dynamical condition.

This condition cannot be chosen retrospectively from CKM or mass agreement without a new freeze.

## Evidential status

```text
A5 cubic invariant dimension: 2
embedding orientation: rigid from Stage 62
frozen operator probe rank: 2
unique cubic selector from geometry alone: NO
new scalar dynamical condition required: YES
uses observed CKM: NO
uses observed masses: NO
uses fitted coefficients: NO
```

## Reproducibility

Executable:

`TIR/frozen_predictions/validation/scripts/rigid_embedding_cubic_selector_stage63_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE63_RIGID_EMBEDDING_CUBIC_SELECTOR_RECEIPT_V0_1.json`
