# TIR active validation frontier — 2026-08-27

Status: `ACTIVE_FRONTIER_INDEX / PUBLICATION_BASELINE_PRESERVED`

## Purpose

This file records the active post-v11.0 research frontier without rewriting the frozen publication baseline.

The current dependency split is

```text
PUBLICATION BASELINE
  v11.0 monograph + publication audits

ACTIVE FORMAL / VALIDATION FRONTIER
  κ / 1/2 cross-review
  information-area curvature cross-review
  polygonal-excitation validation through Stage 67
  TIR × RFC source-interface export
```

## Current active gates

### Charged-fermion mass programme

`TIR/validation/results/collatz_sector_holonomy_mass_audit_v10_2r1.json`

```text
technical_status                = PASS
methodological_status           = RETROSPECTIVE_STRUCTURAL_CANDIDATE_NOT_PROSPECTIVE_TEST
physical_mass_spectrum_status   = FAIL_OPEN
debt9_status                    = OPEN_NOT_CLOSED
canon_allowed                   = false
mass_derivation_claimed         = false
```

The current prospective path remains the frozen v10.7 candidate family:

`TIR/validation/results/separable_universal_candidate_family_v10_7.json`

Its future observables remain frozen under the declared no-refit rule.

### Gauge-matter carrier

Stage 27:

`TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE27_GAUGE_INVARIANT_QUARK_LINK_COUPLING_V0_1.md`

establishes the exact local gauge scalar

```math
B_{ij}=q_i^\dagger W_{ij}q_j.
```

Stage 28:

`TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE28_DISCRETE_GAUGE_MATTER_ACTION_V0_1.md`

establishes the locally gauge-invariant discrete color-plus-quark action form.

### Material-carrier threshold

Stage 67:

`TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE67_MATERIALITY_THRESHOLD_V0_1.md`

records

```text
strict N=6 equal-edge boundary       PASS
N=7 under the same strict rule       OUTSIDE_UNIT_SPHERE
gauge-matter source carrier          PASS
6+1 sourced-extension typing         PASS
absolute mass normalization          OPEN
bound-state energy                    OPEN
continuum stress-energy               OPEN
physical materiality                  OPEN
```

The optional `septahedral` alias is canonically typed at this frontier as

```text
GEOMETRIC_SIX_BOUNDARY_PLUS_SOURCE_ONE.
```

## TIR × RFC handoff

The active handoff is

```math
\mathcal C_{6+1}
\rightarrow
E_C
\rightarrow
M_C
\rightarrow
\rho_m
\rightarrow
\text{RFC continuum source tests}.
```

TIR currently supplies the first structural carrier. The energy, mass, density, and continuum-conservation arrows are the next derivational gates.

Cross-review:

`TIR/docs/cross_reviews/TIR_RFC_MATERIALITY_SOURCE_INTERFACE_2026-08-27.md`

## Next allowed work

Priority order:

1. derive a state-dependent gauge-invariant energy functional from already admitted `W`, quark carriers, Wilson loops, and holonomy invariants;
2. freeze that energy operator before consulting target hadron/nucleon masses;
3. test positivity/localization and conservation on graph states;
4. derive the dimensional scale with explicit provenance;
5. construct `M_C` and `rho_m` only after the energy gate passes;
6. export the resulting density/stress-energy object to RFC for Newton/Einstein closure tests.

GREMLIN remains a candidate-generation and relational-isomorphism audit layer. Executable validation receipts determine promotion.
