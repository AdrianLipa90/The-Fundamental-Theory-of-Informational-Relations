# Index

This file is the root governance map and canonical table of contents for the public Foundations repository.

## Index authority
Root navigation authority is split across four canonical layers:
- `README.md` — project purpose, quick navigation, active modules
- `INDEX.md` — root governance map and grouped canonical contents
- `index.md` — human-readable global navigation spine for indexed sectors and entrypoints
- `registries/global_index_registry.yaml` — machine-readable root index authority and policy

Cross-reference topology is split across:
- `registries/cross_reference_map.yaml` — legacy/imported sector topology map
- `registries/global_cross_reference_map.yaml` — active foundations cross-reference spine

## Role of this repository
This repository is the public first-principles theory layer for CIEL.
It is the place for:
- axioms
- definitions
- derivations
- constants
- executable theory modules
- tests
- falsification criteria
- whitepapers and LaTeX sections
- provenance and artifact tracking

It is not the Omega runtime and it is not a recovery/archive container.

## Canonical workflow
Axiom -> Definition -> Derivation -> Implementation -> Test -> Status -> Interpretation

## Root entrypoints
- `README.md` — high-level project purpose, quick navigation, active modules
- `AGENT.md` — mandatory startup algorithm and hard gates
- `PROJECT_CHARTER.md` — mission, deliverables, hard constraints
- `ORGANIZATION.md` — methodology, review gates, epistemic statuses
- `STRUCTURE.md` — directory logic and naming rules
- `ROADMAP.md` — long-range milestone ordering
- `systems/CIEL_FOUNDATIONS/ORCHESTRATOR.md` — orchestration layer for active modules
- `index.md` — global navigation spine
- `registries/global_index_registry.yaml` — machine-readable root index authority
- `registries/global_cross_reference_map.yaml` — active global cross-reference spine

## Canonical theory layers
### Formal layer
- `axioms/` — frozen axioms and axioms registry
- `definitions/` — canonical object definitions and registries
- `derivations/` — derivation documents and dependency graph
- `constants/` — constant registry and per-constant folders
- `interfaces/` — structured module contracts
- `assumptions/` — explicit assumptions and simplifications

### Executable layer
- `src/ciel_foundations/` — executable theory-facing code
- `tests/` — symbolic, numeric, regression, falsification tests
- `Simulations/` — simulation code/results plus registry
- `artifacts/` — generated artifact registry
- `provenance/` — lineage of runs, datasets, artifacts
- `falsification/` — failure criteria and module falsification matrix

### Paper layer
- `whitepapers/` — modular explanatory papers downstream of formal objects
- `LaTeX/` — publication build materials and appendices
- `bibliography/` — citation sources and cross-reference maps

### Support layers
- `operational_modes/` — external formalism -> CIEL operational role
- `reverse_operational_modes/` — CIEL object -> external analogy map
- `benchmarks/` — stability/performance benchmarks
- `environments/` — reproducible environment definitions
- `archive/` — quarantined non-canonical material

## Current active modules
### Minimal projective / Berry / spin foundations
- `AX-0001`, `AX-0002`, `AX-0003`
- `DEF-0001`, `DEF-0002`, `DEF-0003`
- `D-0001`, `D-0002`
- `interfaces/IF-0001-minimal-cp1-berry-spin.yaml`
- `src/ciel_foundations/geometry/projective_state.py`
- `src/ciel_foundations/holonomy/berry.py`
- `src/ciel_foundations/closure/euler.py`
- `src/ciel_foundations/solvers/minimal_cp1_berry_spin_solver.py`
- `tests/test_projective_state.py`
- `tests/test_berry_and_closure.py`
- `whitepapers/WP-MOD-minimal-projective-berry-spin.md`
- `LaTeX/appendices/APP-0001-minimal-cp1-berry-spin-numerical-derivations.tex`

### Tetrahedral relational frame
- `DEF-0004`
- `D-0003`
- `interfaces/IF-0002-tetrahedral-relational-frame.yaml`
- `src/ciel_foundations/solvers/tetrahedral_relational_frame_solver.py`
- `tests/test_tetrahedral_relational_frame.py`
- `whitepapers/WP-MOD-tetrahedral-relational-frame.md`
- `LaTeX/sections/SEC-0002-tetrahedral-relational-frame.tex`
- `LaTeX/appendices/APP-0002-tetrahedral-frame-numerical-derivations.tex`

### Current next-layer targets
- active closure law
- white-thread primitives
- tau-from-coupling layer
- tensor-scalar extension
- algebra targets `SO(3)`, `SU(2)`, `U(1)`

## Global cross-reference principle
Repository-wide navigation should behave like a global organizational coupling graph:
\[
W_{ij}^{Global}: \text{object}_i \leftrightarrow \text{object}_j
\]
realized through hyperlinks, registries, dependency DAGs, interfaces, tests, simulations, artifacts, and provenance.

## Normalization note
`INDEX.md` is the root governance map.
`index.md` is the navigation spine.
`README.md` is the public entrypoint.
`registries/global_index_registry.yaml` is the machine-readable authority.
No additional parallel root index should be introduced without explicit registry normalization.
