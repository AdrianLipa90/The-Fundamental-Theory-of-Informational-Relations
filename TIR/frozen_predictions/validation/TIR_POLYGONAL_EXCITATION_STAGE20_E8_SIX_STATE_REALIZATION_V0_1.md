# TIR Polygonal Excitation — Stage 20 E8 Six-State Realization v0.1

Status: `STAGE_20_E8_SIX_STATE_REALIZATION_PASS`

## Carrier

Use the conjugate E8 branch pair

```math
(27,3)\oplus(\overline{27},\overline3).
```

Represent the six discrete labels as

```math
(j,s),\qquad j\in Z_3,\quad s\in Z_2.
```

Here `j` is the cyclic basis index in the SU(3) triplet carrier and `s` records the conjugate branch.

## Operators

Let

```math
P_3:(j,s)\mapsto(j+1\bmod3,s)
```

and

```math
C:(j,s)\mapsto(j,1-s).
```

The 3-cycle permutation has determinant +1 and is an element of SU(3). The conjugation grading satisfies `C^2=1`. In this label realization the two actions commute.

Define

```math
G=P_3C.
```

Then exact finite action gives

```math
G^3=C,
\qquad
G^6=1.
```

The orbit starting at `(0,0)` is

```text
(0,0) -> (1,1) -> (2,0) -> (0,1) -> (1,0) -> (2,1) -> (0,0).
```

Thus `G` is a single 6-cycle and its permutation characteristic polynomial is

```math
\chi_G(\lambda)=\lambda^6-1.
```

After projection onto the triplet coordinate `j`, the period is three.

## Relation to Stage 6

The Stage 6 abstract six-state lift is realized on the exceptional E8 triplet/conjugate-triplet labels with the same orbit, the same projected period three, the same full period six, and the same characteristic polynomial.

The Stage 7 separation between this lifted six-state object and the polygonal N=6 geometric degeneration remains part of the validation lineage.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/e8_six_state_realization_stage20_v01.py`

Expected verdict: `PASS`.
