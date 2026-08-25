# TIR Polygonal Excitation — Stage 35 Hermitian Family Pair from Pre-CKM Cross-Holonomy v0.1

Status: `STAGE_35_HERMITIAN_FAMILY_PAIR_PASS_WITH_INPUT_PROVENANCE_AND_CP_BOUNDARY`

## Input

Use the archived signed up/down structural cross-Gram matrix from v3.4,

`archive/v7.9/full/32_debt9_projection_orientation_sector_basis_v3_4/results/up_down_basis_overlap_matrix_v3_4.csv`,

blob SHA

`9394ca738bc41ab78b084cd03202016fa0c9bb05`.

The archived source label is `up_down_basis_overlap_not_CKM`.

The source rows declare `uses_observed_mass=False` and `uses_observed_mixing=False`. The heavy-quark orientation rows for `c`, `b`, and `t` carry source status `old_doc_bridge_ansatz_quarantined`; this provenance remains active in the present gate.

## Canonical Hermitian construction

For the real cross-sector map `O_ud`, define

```math
H_u=O_{ud}O_{ud}^{T},
\qquad
H_d=O_{ud}^{T}O_{ud}.
```

Both matrices are real symmetric positive-semidefinite operators. They share the squared singular-value spectrum of `O_ud`.

The reproduced spectrum is

```math
\operatorname{spec}(H_u)=\operatorname{spec}(H_d)
\approx
(0.9999269945,\ 0.1700635936,\ 0.05536972169).
```

The shared-spectrum residual is

```text
6.661338147750939e-16
```

and both Hermiticity residuals are exactly zero in the replay.

## Noncommutation gate

The family operators satisfy

```math
[H_u,H_d]\neq0.
```

The reproduced infinity norm is

```text
||[H_u,H_d]||_inf = 0.37940977777058743
```

so the up and down sectors possess distinct eigenframes in the common three-dimensional label space.

## Relative eigenframe

Diagonalize

```math
U_u^{T}H_uU_u=D,
\qquad
U_d^{T}H_dU_d=D,
```

with eigenvalues sorted descending and a deterministic right-handed eigenframe convention. The relative transformation is

```math
V_{rel}=U_u^{T}U_d.
```

The replay gives

```math
V_{rel}\approx
\begin{pmatrix}
-0.3451722030 & 0.1569840770 & 0.9253173238\\
 0.0385656854 & 0.9874517994 & -0.1531392562\\
-0.9377466812 & -0.0171739176 & -0.3468951115
\end{pmatrix}.
```

Checks:

```text
max |V_rel^T V_rel - I| = 3.3306690738754696e-16
|det(V_rel)-1| = 2.220446049250313e-16
```

Thus the relative eigenframe is an orientation-preserving orthogonal transformation and therefore lies in the real `SO(3)` subgroup of the Stage 34 family `SU(3)_F` carrier.

## CP boundary

Because the archived cross-Gram is real, the induced relative transformation is real. Its Jarlskog invariant is

```math
J(V_{rel})=0.
```

The Stage 35 mechanism therefore supplies nontrivial family misalignment while leaving the complex CP phase as the next operator-level gate. A complex TIR-native holonomy/Berry contribution is required before a nonzero Jarlskog invariant can arise from this construction.

## Provenance boundary

```text
noncommuting H_u/H_d mechanism: PASS
relative unitary/orthogonal eigenframe: PASS
observed mass used in source: false
observed mixing used in source: false
heavy-quark orientation provenance: QUARANTINED
CP from real cross-Gram: J = 0
physical promotion: BLOCKED_PENDING_CLEAN_COMPLEX_TIR_NATIVE_SECTOR_OPERATOR
```

## Reproducibility

Executable:

`TIR/frozen_predictions/validation/scripts/hermitian_family_pair_stage35_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE35_HERMITIAN_FAMILY_PAIR_RECEIPT_V0_1.json`

The exact committed source was replayed in the assistant-local Python environment with return code `0`.

## Next gate

Construct a complex sector map from already-existing TIR holonomy/Berry-phase objects, without introducing CKM entries or a fitted phase, and repeat the Hermitian-pair test. The required target is a clean complex `H_u,H_d` pair whose relative diagonalizer lies in `SU(3)_F` with nonzero Jarlskog invariant.
