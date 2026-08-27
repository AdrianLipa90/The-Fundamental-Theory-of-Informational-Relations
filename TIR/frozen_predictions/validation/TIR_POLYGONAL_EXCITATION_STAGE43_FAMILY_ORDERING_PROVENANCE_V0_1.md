# TIR Polygonal Excitation — Stage 43 Family Ordering Provenance v0.1

Status: `STAGE_43_ORDERING_PRINCIPLE_FOUND__EXACT_WEIGHT_MAP_OPEN`

## Scope

This stage audits whether TIR already contains an ordering principle capable of selecting a trajectory through the family `SU(3)_F` Lie algebra established in Stage 42.

No CKM entries, masses, or newly fitted coefficients are introduced.

## Existing ordered accumulation

The foundational phase/intention Hamiltonian defines an accumulated intention phase over ordered Collatz steps:

```math
\Theta_{\mathcal I}(K)
=
\sum_{k=0}^{K-1}
\rho_s(k)
\,\langle\hat{\mathcal I}_s(\tau_k,k)\rangle.
```

Thus the sequence index `k` is part of the pre-existing formal structure. The model already contains an ordered dynamical scaffold rather than only an unordered family label set.

## Canonical derivation debt

The Euler-Berry working freeze explicitly retains

```text
exact Collatz/twin-prime rhythm rho_s(k)
```

as an open derivation debt.

Therefore the existence of step ordering and the exact numerical weight map must be kept separate.

## Reference simulation boundary

The archived `collatz_phase_sim.py` uses a bounded rhythm with default

```text
eta = 0.35
```

and its own source states that the exact rhythm map is a model choice.

Accordingly Stage 43 does not promote `eta=0.35`, the bounded rhythm formula, or the reference simulation defaults into the family-mixing selector.

## Result

```text
ordered Collatz-step accumulation: PRESENT
exact rho_s(k) formula: OPEN DERIVATION DEBT
reference eta=0.35: MODEL-CHOICE INPUT
eta promoted to family selector: NO
```

The family program therefore has a pre-existing ordering principle, but the exact weights needed for a quantitative ordered `SU(3)_F` evolution remain to be derived or independently frozen.

## Consequence for Stage 42

Stage 42 establishes

```math
\operatorname{Lie}\langle iD_0,iC_0\rangle
=\mathfrak{su}(3)_F.
```

Stage 43 identifies an existing ordered evolution scaffold that could select a specific group trajectory once `rho_s(k)` is fixed.

The admissible future form is structurally of the type

```math
U_F(K)
=\prod_{k=0}^{K-1}
\exp\big[-i\,\Delta\tau_k\,H_F(k)\big]
```

with the product ordered by the pre-existing step index. This formula is a generic ordered-evolution representation of the existing Hamiltonian scaffold; the exact map from each Collatz step to the family generator remains the next derivation gate.

## Evidential status

```text
ordering principle: FOUND
exact weight map: OPEN
CKM input: NONE
mass input: NONE
reference simulation coefficient promoted: NONE
```

## Reproducibility

Executable provenance audit:

`TIR/frozen_predictions/validation/scripts/family_ordering_provenance_stage43_v01.py`

Receipt:

`TIR/frozen_predictions/validation/results/TIR_POLYGONAL_STAGE43_FAMILY_ORDERING_PROVENANCE_RECEIPT_V0_1.json`

## Next gate

Derive the family-generator assignment from the discrete Collatz transition itself before evaluating a new mixing matrix. The first test should use only exact transition properties — parity branch, normalized step direction, or graph transition incidence — and reject any continuous rhythm parameter that is not already independently fixed.
