# TIR Polygonal Excitation — Stage 19 Exceptional Conjugation Z2 v0.1

Status: `STAGE_19_EXCEPTIONAL_CONJUGATION_Z2_PASS`

## Exact branch involution

The E7 branch contains the conjugate pair

```math
27_{+2}\leftrightarrow\overline{27}_{-2}.
```

The E8 branch contains

```math
(27,3)\leftrightarrow(\overline{27},\overline3).
```

Define the conjugation map C on these representation labels by exchanging each pair and fixing the real adjoint/core sectors. Direct application gives

```math
C^2=1.
```

The resulting representation-level grading is therefore an exact Z2.

## Existing TIR interface

The archived TIR chain already contains:

- the CP1/Bloch two-pole chiral axis;
- a one-generation chiral representation/projection table;
- a pre-mass sector-orientation layer.

The current operator gate is the explicit intertwiner between that TIR chiral orientation and the exceptional conjugation map C.

## Next gate

Use a cyclic order-three element in the SU(3) factor together with C and test the order of the combined six-state action on the triplet/conjugate-triplet carrier.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/exceptional_conjugation_stage19_v01.py`

Expected verdict: `PASS`.
