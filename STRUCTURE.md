# Structure

## Root directories
- `axioms/` frozen axioms and registry
- `definitions/` formal object definitions and registries
- `derivations/` derivation texts and dependency DAG
- `constants/` constants registry and per-constant folders
- `modules/` optional theory-facing module docs (reserved)
- `src/ciel_foundations/` executable code
- `tests/` symbolic, numeric, regression, falsification tests
- `whitepapers/` module/constant/sector whitepapers
- `LaTeX/` publication build materials by sections
- `Simulations/` simulation code, results, and registry
- `bibliography/` sources and citation cross-reference maps
- `operational_modes/` external formalism -> CIEL operational role
- `reverse_operational_modes/` CIEL object -> external analogies
- `assumptions/` explicit assumptions and simplifications
- `decisions/` architectural decision records (ADR)
- `artifacts/` registry of generated artifacts with hashes
- `falsification/` falsification matrix and module failure criteria
- `interfaces/` inter-module contracts
- `schemas/` validation schemas for registries
- `provenance/` lineage of runs, datasets, and result generation
- `benchmarks/` stability/performance benchmarks
- `environments/` reproducible environment definitions
- `archive/` quarantined legacy material and notebooks

## Naming
- axioms: `AX-####-slug.md`
- derivations: `D-####-slug.md`
- ADRs: `ADR-####-slug.md`
- whitepapers: `WP-{MOD|CONST|SECTOR|INTEGRATION}-slug.md`
- constants IDs: `CONST-*`
- assumptions IDs: `ASM-*`
- interfaces IDs: `IF-*`
- artifacts IDs: `ART-*`

## Rule
All new theory objects must first appear in a registry and only then in code or prose.
