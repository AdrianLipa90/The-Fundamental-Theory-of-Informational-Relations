# Index

This file is the root navigation layer for the public theory repository.

## Index authority
Root navigation authority is split explicitly across three canonical layers:
- `INDEX.md` — human-readable root governance and repository map
- `index.md` — human-readable global navigation spine for indexed sectors and entrypoints
- `registries/global_index_registry.yaml` — machine-readable root index authority and policy

`registries/cross_reference_map.yaml` remains the sector/object topology map rather than the root authority registry.

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

## Root map
- `README.md` — high-level repository purpose and scope
- `AGENT.md` — mandatory startup algorithm and hard gates
- `MASTER_PLAN.md` — execution plan for converting scaffold -> real theory program
- `PROJECT_CHARTER.md` — mission, deliverables, hard constraints
- `ORGANIZATION.md` — methodology, review gates, epistemic statuses
- `STRUCTURE.md` — directory logic and naming rules
- `ROADMAP.md` — long-range milestone ordering
- `index.md` — global navigation spine for indexed sectors and imported entrypoints
- `registries/global_index_registry.yaml` — machine-readable root index authority

## Canonical theory layers
- `axioms/` — frozen axioms and axioms registry
- `definitions/` — canonical object definitions and registries
- `derivations/` — derivation documents and dependency graph
- `constants/` — constant registry and per-constant folders
- `src/ciel_foundations/` — executable theory-facing code
- `tests/` — symbolic, numeric, regression, falsification tests
- `falsification/` — failure criteria and module falsification matrix
- `interfaces/` — structured module contracts
- `assumptions/` — explicit assumptions and simplifications
- `whitepapers/` — modular explanatory papers downstream of formal objects
- `LaTeX/` — publication build materials

## Support layers
- `Simulations/` — simulation code/results plus registry
- `artifacts/` — generated artifact registry
- `provenance/` — lineage of runs, datasets, artifacts
- `bibliography/` — citation sources and cross-reference maps
- `operational_modes/` — external formalism -> CIEL operational role
- `reverse_operational_modes/` — CIEL object -> external analogy map
- `benchmarks/` — stability/performance benchmarks
- `environments/` — reproducible environment definitions
- `archive/` — quarantined non-canonical material

## Current scaffold state
At the moment, the repository has the correct structural categories but many inner objects are still placeholders.
Immediate indexing priority is:
1. map every existing object to its registry
2. mark placeholders vs real content
3. create canonical entry points for future work
4. ensure no downstream code outruns upstream formal objects

## Entry points for next work
- start foundational object indexing in `definitions/`
- wire `axioms/` -> `definitions/` -> `derivations/`
- replace placeholder tests with object-level tests
- make constants folders derivation-bearing rather than placeholder-only
