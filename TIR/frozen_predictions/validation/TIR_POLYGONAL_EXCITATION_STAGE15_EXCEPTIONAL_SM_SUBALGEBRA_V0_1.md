# TIR Polygonal Excitation — Stage 15 Exceptional SM Subalgebra v0.1

Status: `STAGE_15_PURE_LIE_ALGEBRA_PASS`

Parent chain: frozen polygonal excitation v0.1 -> Stages 10-14.

## Scope

This stage tests only an exact Lie-algebra embedding question. Particle assignments, masses, PDG values, CKM, PMNS and atomic data are absent from the active calculation.

Existing TIR dependencies used as structural targets:

- v3.8: CP1/Bloch weak-doublet geometry, a U(1)-type phase axis, and the one-generation hypercharge/anomaly skeleton.
- v3.9: tetrahedral residual triplet, complex carrier C^3, CP2, and the SU(3)-candidate Gell-Mann algebra.
- Stage 14: McKay lifts `2O <-> E7~` and `2I <-> E8~`.

## Exact regular subalgebra test

For a simply-laced Cartan matrix C, select disconnected simple-root subsets with Cartan blocks

```math
A_2 = \begin{pmatrix}2&-1\\-1&2\end{pmatrix},
\qquad
A_1=(2).
```

A Cartan direction

```math
H_Y=\sum_j h_j\alpha_j^\vee
```

commutes with the selected A2+A1 root generators when

```math
(C h)_i=0
```

for every selected root i.

### E7 witness

Using the repository script numbering,

- A1 node: 1,
- A2 nodes: 6,7,
- integral coroot direction:

```text
h_E7 = (4, 6, 8, 12, 9, 6, 3)
```

and direct multiplication gives

```text
C_E7 h_E7 = (0, 0, 0, 1, 0, 0, 0).
```

Therefore the U(1) direction has zero charge on the selected A1 and A2 roots while remaining nonzero.

### E8 witness

Using the same numbering convention,

- A1 node: 1,
- A2 nodes: 7,8,
- integral coroot direction:

```text
h_E8 = (10, 15, 20, 30, 24, 18, 12, 6)
```

and

```text
C_E8 h_E8 = (0, 0, 0, 1, 0, 0, 0, 0).
```

Again the U(1) direction commutes with the chosen A1+A2 roots and is nontrivial.

## Result

Both exceptional algebras therefore contain an explicit commuting rank-four reductive subalgebra

```math
A_2\oplus A_1\oplus \mathfrak u(1)
\cong
\mathfrak{su}(3)\oplus\mathfrak{su}(2)\oplus\mathfrak u(1).
```

This is an existence result with an explicit integral Cartan witness. The next gate is representation matching: test whether the already-frozen TIR one-generation hypercharge pattern is reproduced by a representation branch of the same exceptional chain.

## Reproducibility

Script:

`TIR/frozen_predictions/validation/scripts/exceptional_sm_subalgebra_stage15_v01.py`

Expected verdict:

`PASS`
