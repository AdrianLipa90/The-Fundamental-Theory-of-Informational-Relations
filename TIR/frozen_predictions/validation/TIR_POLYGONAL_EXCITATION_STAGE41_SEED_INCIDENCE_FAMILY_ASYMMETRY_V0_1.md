# TIR Polygonal Excitation — Stage 41 Seed-Incidence Family Asymmetry v0.1

Status: `STAGE_41_SEED_INCIDENCE_ASYMMETRY_PASS`

## Scope

This gate tests a discrete structural asymmetry already present in the frozen ordered family seeds

```math
s_1=(3,5),\qquad
s_2=(5,7),\qquad
s_3=(11,13).
```

No CKM entries, masses, or fitted coefficients are used.

## Incidence representation

Use the prime basis

```math
(3,5,7,11,13).
```

Represent each seed pair by its incidence vector and normalize by `sqrt(2)`:

```math
x_1=\frac1{\sqrt2}(1,1,0,0,0),
```

```math
x_2=\frac1{\sqrt2}(0,1,1,0,0),
```

```math
x_3=\frac1{\sqrt2}(0,0,0,1,1).
```

The exact Gram matrix is

```math
\boxed{
G_{seed}=
\begin{pmatrix}
1&1/2&0\\
1/2&1&0\\
0&0&1
\end{pmatrix}.
}
```

Therefore the off-diagonal incidence adjacency is

```math
\boxed{
A_{seed}=G_{seed}-I
=
\begin{pmatrix}
0&1/2&0\\
1/2&0&0\\
0&0&0
\end{pmatrix}.
}
```

## Exact asymmetry

The family-pair overlaps are

```math
\langle x_1,x_2\rangle=\frac12,
```

```math
\langle x_2,x_3\rangle=0,
```

```math
\langle x_1,x_3\rangle=0.
```

Thus the frozen seed data contain exactly one shared-prime channel:

```math
\boxed{s_1\leftrightarrow s_2.}
```

The distinguished element is the shared prime `5`.

## Spectral form

The adjacency spectrum is

```math
\left\{-\frac12,0,+\frac12\right\}.
```

The two non-zero eigenmodes are

```math
\frac{|s_1\rangle+|s_2\rangle}{\sqrt2},
\qquad
\frac{|s_1\rangle-|s_2\rangle}{\sqrt2},
```

while `s3` is an isolated incidence mode at this level.

## Result

The ordered seed triplet contains an intrinsic discrete asymmetry that singles out the `1<->2` family channel before any CKM comparison:

```text
shared-prime channel 1<->2: 1/2
shared-prime channel 2<->3: 0
shared-prime channel 1<->3: 0
```

This supplies precisely the type of channel distinction missing from the symmetric Stage 39 operator.

## Evidential status

```text
seed-incidence calculation: EXACT PASS
unique 1<->2 channel: PASS
continuous fit parameter: NONE
observed CKM input: NONE
physical mixing magnitude assignment: OPEN
```

The incidence value `1/2` is a structural overlap. This stage does not identify it directly with a CKM matrix element.

## Reproducibility

Executable:

`TIR/frozen_predictions/validation/scripts/seed_incidence_family_stage41_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE41_SEED_INCIDENCE_FAMILY_ASYMMETRY_RECEIPT_V0_1.json`

## Next gate

Introduce the exact incidence adjacency as an additional frozen operator alongside the ordered polygonal axis and the `C3` character holonomy. Test the minimal coefficient-free operator algebra first. Only after its output is frozen may the resulting family transformation be compared to the CKM hierarchy.
