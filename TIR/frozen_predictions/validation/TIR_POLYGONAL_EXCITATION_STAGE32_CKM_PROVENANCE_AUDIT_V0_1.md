# TIR Polygonal Excitation — Stage 32 CKM Provenance Audit v0.1

Status: `STAGE_32_CKM_UNITARY_CONSTRUCTION_PASS__PREDICTIVE_STATUS_POSTDICTIVE`

## Existing v7.9 line

The archived v7.9 CKM module constructs a standard three-angle/one-phase unitary matrix from structural expressions

```math
\lambda_0=\frac{L_4}{L_3+L_4}=\frac29,
```

```math
|V_{cb}|=\frac{(L_4/L_3)^2}{2}=\frac2{49},
```

```math
|V_{ub}|=\frac{(L_4/L_3)^2L_4}{(L_3+L_4)L_5}=\frac8{2205},
```

and

```math
J=\kappa^2\frac{L_4}{L_5}
\left(1-\frac{(L_4/L_5)^2}{2}\right).
```

Its provenance file explicitly records `PASS (Structural derivation, not a formal freeze)` and includes PDG comparisons in the same development record.

## Later refinements

The r1 script modifies the Cabibbo coordinate after the original PDG comparison:

```math
\lambda=\frac29+\frac27\kappa.
```

The current monograph chapter uses this corrected expression.

The current CP chapter additionally records that the earlier phase obtained by inverting the Jarlskog relation gave approximately `73.6 deg`, and replaces it with the direct geometric expression

```math
\delta=\arccos\frac25.
```

The chapter itself describes this replacement after comparison with the earlier result.

## Mathematical status

For either the original or refined angles, the standard CKM parameterization is exactly unitary up to floating-point residual. Reproduction gives

```text
v7.9 base: max |V V^dagger - I| = 2.22e-16
v7.9r1:    max |V V^dagger - I| = 2.22e-16
```

and determinant one to the same numerical precision.

## Epistemic status

The unitary construction is mathematically valid. The current numerical agreement with measured CKM entries is retained as postdictive structural evidence because the formula-development record and refinement steps already had access to CKM reference values.

This stage does not discard the CKM formulas. It separates

```text
unitary family-matrix construction: PASS
structural formula candidate: RETAIN
prospective prediction status: POSTDICTIVE
```

## Reproducibility closure

The Stage 32 executable is

`TIR/frozen_predictions/validation/scripts/ckm_provenance_stage32_v01.py`.

The append-only execution receipt is

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE32_CKM_PROVENANCE_AUDIT_RECEIPT_V0_1.json`.

The exact committed source was replayed in the assistant-local Python environment with return code `0`. The base and refined constructions both returned maximum unitarity residual `2.220446049250313e-16`; determinant residuals were of the same floating-point order. The executable contains no PDG numerical inputs. The `POSTDICTIVE` classification is retained from the documented development provenance rather than inferred from the replay.

## Next gate

Use the newly derived polygonal/McKay family geometry to test whether the constants entering the structural CKM candidate can be reconstructed from independently fixed geometric invariants, without using CKM data in that reconstruction.
