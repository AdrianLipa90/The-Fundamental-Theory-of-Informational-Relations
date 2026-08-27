# TIR Polygonal Excitation — Stage 40 Retrospective CKM Diagnostic v0.1

Status: `STAGE_40_FULL_CKM_SHAPE_FAIL__MECHANISM_RETAINED`

## Scope

Stage 39 was frozen before target comparison in that gate. Stage 40 now performs a retrospective comparison against the archived `METATIME_CKM_V7_9R1` construction.

No Stage 39 coefficient, axis, sector assignment, or operator is changed after opening the reference.

Both frozen sector assignments are scored and retained.

## Reference

The archived reference has fingerprint

`211beddf2e9e4a96264faf088ef75df3f3931ba1a630b1c0382fba7ebab7bd3b`

and structural magnitudes including

```text
|Vus| = 0.22484736
|Vub| = 0.00362812
|Vcb| = 0.04081606
|Vtd| = 0.00885537
|Vts| = 0.04000870
J_CP  = 3.11012e-05
```

The reference itself remains governed by the existing provenance classification: structural/postdictive rather than an independent prospective prediction.

## Assignment A

For the frozen Stage 39 assignment

```text
alpha_u = 2/7
alpha_d = 2/9
```

the matrix-level diagnostics are

```text
max absolute magnitude difference = 0.1873694982
mean absolute magnitude difference = 0.0513978777
Frobenius difference              = 0.2680143819
```

Key ratios `candidate/reference` are

```text
Vus = 0.16668
Vub = 4.67478
Vcb = 0.79566
Vtd = 1.94596
Vts = 0.80813
```

and

```text
|J_family| / J_reference = 0.64866.
```

## Assignment B

For the swapped frozen assignment

```text
alpha_u = 2/9
alpha_d = 2/7
```

the diagnostics are nearly identical:

```text
max absolute magnitude difference = 0.1874935647
mean absolute magnitude difference = 0.0513978777
Frobenius difference              = 0.2680201763
```

with

```text
Vus = 0.16613 x reference
Vub = 4.74962 x reference
Vcb = 0.79215 x reference
Vtd = 1.91530 x reference
Vts = 0.81171 x reference
|J_family| / J_reference = 0.64866.
```

No assignment is selected by fit.

## Verdict

The full CKM shape gate fails.

The dominant discrepancies are:

1. the Cabibbo-like `Vus` magnitude is strongly underproduced;
2. `Vub` is strongly overproduced;
3. `Vtd` is overproduced;
4. the CP invariant magnitude is below the archived structural CKM value.

The following Stage 39 results are retained because they pass independently of this quantitative comparison:

```text
unitary relative family transformation
near-identity hierarchical matrix
non-commuting Hermitian family operators
non-zero rephasing-invariant CP measure
parameter-free frozen construction
```

## Consequence

The minimal affine two-operator rule

```math
H(\alpha)=D+\alpha F_3DF_3^\dagger
```

with the Stage 33 endpoint weights does not reproduce the full CKM hierarchy.

The failure is preserved. The next gate must derive an additional structural distinction that specifically separates the large `1<->2` family mixing scale from the smaller `2<->3` and `1<->3` scales, without observable-specific correction factors.

## Reproducibility

Executable:

`TIR/frozen_predictions/validation/scripts/stage39_ckm_retrospective_stage40_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE40_STAGE39_CKM_RETROSPECTIVE_RECEIPT_V0_1.json`
