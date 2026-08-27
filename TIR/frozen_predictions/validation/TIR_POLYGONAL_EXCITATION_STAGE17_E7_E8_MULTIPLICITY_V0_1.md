# TIR Polygonal Excitation — Stage 17 E7/E8 Multiplicity Separation v0.1

Status: `STAGE_17_EXACT_BRANCH_MULTIPLICITY_PASS`

## Scope

Pure branching and tensor-product arithmetic around the common E6 core reached from Stage 14. Physical family assignment remains an open gate.

## N=4 / E7 branch

The standard branch is

```math
133 \to 78_0\oplus 1_0\oplus 27_{+2}\oplus \overline{27}_{-2}.
```

Dimension closure:

```math
78+1+27+27=133.
```

On one 27 branch,

```math
27\to16\oplus10\oplus1
```

under SO(10), so the 16 carrier occurs with external multiplicity one.

## N=5 / E8 branch

The standard branch is

```math
248\to(78,1)\oplus(1,8)\oplus(27,3)\oplus(\overline{27},\overline3).
```

Dimension closure:

```math
78+8+3\cdot27+3\cdot27=248.
```

Restricting the positive 27 triplet further,

```math
(27,3)\to(16,3)\oplus(10,3)\oplus(1,3).
```

Therefore the E8 branch contains an exact SU(3)-triplet multiplicity carrier for the SO(10) 16:

```math
\dim(16,3)=48=3\cdot16.
```

The multiplicity factor 3 is fixed by the E8 -> E6 x SU(3) branching.

## N=4 versus N=5

```text
N=4 / E7: E6 core + one 27 + one conjugate 27 + U(1) singlet
N=5 / E8: E6 core + SU(3) adjoint + triplet 27 carrier + conjugate triplet carrier
```

This is an exact algebraic separation between the two surviving polygonal levels.

## Next gate

Compare the SU(3) triplet acting on `(27,3)` with the already-existing TIR tetrahedral `C^3 -> CP2 -> SU(3)` carrier. The required test is an intertwiner/equivalence test at representation level, with the `3` versus `bar(3)` orientation retained explicitly.

## Reproducibility

`TIR/frozen_predictions/validation/scripts/e7_e8_multiplicity_stage17_v01.py`

Expected verdict: `PASS`.
