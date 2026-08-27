# TIR Polygonal Excitation — Stage 64 Selector Provenance Gate v0.1

Status: `STAGE_64_CANONICAL_SCALAR_SELECTOR_REMAINS_OPEN_PASS`

Gate type: `formal_provenance_audit_with_algebraic_checks`

## Purpose

Stage 63 establishes that the rigid `A_seed/D0` embedding resolves the two cubic invariant directions independently and therefore leaves one scalar dynamical condition to be supplied before a unique cubic family action can be frozen.

Stage 64 audits previously existing TIR structures for such a condition. The gate records their canonical roles and promotion status before any new family-dynamics ansatz is introduced.

No CKM entries, observed masses, fitted coefficients, or retrospective target selection are used.

## Candidate-source audit

### 1. Canonical information scale

The repository fixes

```math
\kappa=\frac{\ln2}{24\pi}.
```

Its established role is a global action scale applied after dimensionless structural costs are assembled.

For a cubic coefficient vector

```math
c=(c_{iso},c_{A5}),
```

multiplication by `kappa` gives

```math
c\mapsto\kappa c,
```

which leaves the projective ratio

```math
[c_{iso}:c_{A5}]
```

unchanged. Thus `kappa` fixes overall scale rather than the missing relative cubic direction.

### 2. Quadratic A5 invariant

Stage 60 gives exactly one degree-two invariant on the five-dimensional carrier. It supplies the invariant norm/radius. The cubic invariant multiplicity remains two, so quadratic normalization leaves the cubic projective line unresolved.

### 3. Icosahedral geometry and rigid embedding

Stages 58–62 provide the explicit `A5` five-carrier, full `su(3)_F` generation, the `A_seed/D0` intertwiner, and embedding rigidity.

Stage 63 then verifies a rank-two frozen probe matrix. Therefore these structures fix carrier and orientation while retaining both cubic invariant directions as distinguishable dynamical channels.

### 4. Ordered Collatz dynamics

Stage 43 records that ordered Collatz-step accumulation is already present:

```math
\Theta_{\mathcal I}(K)
=\sum_k\rho_s(k)\langle\hat{\mathcal I}_s(k)\rangle.
```

The same provenance gate retains the exact rhythm `rho_s(k)` as an open derivation debt.

Stage 48 further freezes the exact branch words and isolates the remaining interface:

```text
branch symbol -> family-space operator
exact per-step rhythm/weight
```

Thus Collatz supplies canonical order and exact discrete words; its quantitative family-space weight/operator map remains the next dynamical layer.

### 5. Euler–Berry coherence

The canonical working v1.5 status module lists

```text
Define the Euler--Berry constructive coherence functional
```

as a formal debt.

The v1.3 coherence gate also records `full_constructive_eulerberry_interference` as open. Therefore Euler–Berry currently supplies a declared destination for constructive coherence rather than a frozen scalar selector for the Stage-60 cubic pair.

### 6. Zeta coherence

The established role of the zeta layer is a coherence/alignment gate at the critical half-axis. The formal-status module retains the exact zeta-to-vertex weighting and constructive coherence functional as derivation debts. Accordingly this layer remains available as future input once its functional is canonically fixed.

## Structural-enumeration verdict

The audited sources separate cleanly into established roles:

```text
kappa                  -> overall scale
quadratic A5 invariant -> norm / radius
A5 + rigid embedding   -> carrier + orientation
Collatz                 -> exact order + branch words; quantitative operator/rhythm open
Euler--Berry            -> constructive-coherence functional open
zeta                    -> coherence axis; exact weighting functional open
```

Therefore the Stage-63 missing scalar condition remains an explicit derivation target after provenance audit.

This gate freezes that status before any new candidate selector is tested.

## Evidential status

```text
gate_type: formal_provenance_audit_with_algebraic_checks
independent_computation: PARTIAL
uses_observed_CKM: NO
uses_observed_masses: NO
uses_fitted_coefficients: NO
new_selector_promoted: NO
canonical_scalar_selector_status: OPEN
```

## Source ledger

- `archive/v7.9/full/10_standard_model_derivation_stages/11_metatime_sm_full_action_seed_arbitration_v1_0/METATIME_SM_FULL_ACTION_SEED_ARBITRATION_v1_0.md`
- `archive/v7.9/full/13_formal_status_and_phase_axis_action_v1_5/METATIME_SM_FORMAL_STATUS_PHASE_AXIS_ACTION_v1_5.md`
- `archive/v7.9/full/10_standard_model_derivation_stages/13_metatime_sm_eulerberry_coherence_gate_v1_3/EULERBERRY_COHERENCE_GATE_SCHEMA_v1_3.json`
- `TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE43_FAMILY_ORDERING_PROVENANCE_V0_1.md`
- `TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE48_COLLATZ_BRANCH_WORD_OPERATOR_INTERFACE_V0_1.md`
- `TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE60_A5_LOW_ORDER_INVARIANT_SELECTOR_V0_1.md`
- `TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE63_RIGID_EMBEDDING_CUBIC_SELECTOR_NOGO_V0_1.md`

## Reproducibility

Algebraic companion audit:

`TIR/frozen_predictions/validation/scripts/selector_provenance_stage64_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE64_SELECTOR_PROVENANCE_RECEIPT_V0_1.json`

## Next gate

A new scalar dynamical condition may now be proposed only as a separately frozen ansatz/hypothesis before any CKM, mass, or other physical-target comparison. The minimal candidate should add no continuous fitted parameter and should use the already rigid `A_seed/D0` carrier.
