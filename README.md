# CIEL Foundations

CIEL Foundations is a fresh, standalone first-principles project. It is **not** the Omega runtime and it does **not** inherit source-of-truth status from prior tarballs. Its purpose is to derive the minimal ontology, geometry, closure law, coupling structure, constants, and sector maps that Omega may later consume **only through exported constants, operators, and constraints**.

## Primary rule
Every object in the project must have four synchronized representations:
1. ontology / role
2. mathematical definition or derivation
3. executable code
4. epistemic status and tests

No formula without code. No code without formula. No interpretation without an upstream formal object.

## Canonical workflow
Axiom -> Definition -> Derivation -> Implementation -> Test -> Status -> Interpretation

## Quick navigation
### Root entrypoints
- `INDEX.md` — root governance index
- `index.md` — global navigation spine
- `systems/CIEL_FOUNDATIONS/ORCHESTRATOR.md` — orchestration layer for active modules
- `registries/global_index_registry.yaml` — machine-readable root index authority
- `registries/global_cross_reference_map.yaml` — active global cross-reference spine for current foundations modules
- `registries/agent_authority_registry.yaml` — canonical agent-file authority
- `bibliography/README.md` — bibliography entrypoint

### Core governance
- `AGENT.md`
- `PROJECT_CHARTER.md`
- `ORGANIZATION.md`
- `STRUCTURE.md`
- `ROADMAP.md`

## Current active foundations modules
### Minimal projective / Berry / spin chain
- axioms: `AX-0001`, `AX-0002`, `AX-0003`
- definitions: `DEF-0001`, `DEF-0002`, `DEF-0003`
- derivations: `D-0001`, `D-0002`
- interface: `interfaces/IF-0001-minimal-cp1-berry-spin.yaml`
- code: `src/ciel_foundations/geometry/projective_state.py`, `src/ciel_foundations/holonomy/berry.py`, `src/ciel_foundations/closure/euler.py`, `src/ciel_foundations/solvers/minimal_cp1_berry_spin_solver.py`
- tests: `tests/test_projective_state.py`, `tests/test_berry_and_closure.py`
- paper: `whitepapers/WP-MOD-minimal-projective-berry-spin.md`
- LaTeX appendix: `LaTeX/appendices/APP-0001-minimal-cp1-berry-spin-numerical-derivations.tex`

### Tetrahedral relational frame
- definition: `DEF-0004`
- derivation: `D-0003`
- interface: `interfaces/IF-0002-tetrahedral-relational-frame.yaml`
- code: `src/ciel_foundations/solvers/tetrahedral_relational_frame_solver.py`
- tests: `tests/test_tetrahedral_relational_frame.py`
- paper: `whitepapers/WP-MOD-tetrahedral-relational-frame.md`
- LaTeX section: `LaTeX/sections/SEC-0002-tetrahedral-relational-frame.tex`
- LaTeX appendix: `LaTeX/appendices/APP-0002-tetrahedral-frame-numerical-derivations.tex`

### Local attractor / nonlocal holonomic vortex
- axiom: `AX-0005`
- definitions: `DEF-0005`, `DEF-0006`
- derivations: `D-0004`, `D-0005`
- interface: `interfaces/IF-0004-nonlocal-holonomic-vortex.yaml`
- code: `src/ciel_foundations/solvers/nonlocal_holonomic_vortex_solver.py`
- tests: `tests/test_nonlocal_holonomic_vortex.py`
- paper: `whitepapers/WP-MOD-local-attractor-holonomic-vortex.md`
- LaTeX section: `LaTeX/sections/SEC-0003-local-attractor-holonomic-vortex.tex`
- LaTeX appendix: `LaTeX/appendices/APP-0003-rotating-superfluid-field-numerical-derivations.tex`

### Fractal foundations spine at piko scale
- definition: `DEF-0007`
- derivation: `D-0006`
- interface: `interfaces/IF-0005-piko-fractal-spine.yaml`
- code: `src/ciel_foundations/solvers/piko_fractal_spine_solver.py`
- tests: `tests/test_piko_fractal_spine.py`
- paper: `whitepapers/WP-MOD-fractal-foundations-spine.md`
- LaTeX section: `LaTeX/sections/SEC-0004-fractal-foundations-spine.tex`
- LaTeX appendix: `LaTeX/appendices/APP-0004-piko-fractal-spine-numerical-derivations.tex`

## Scope
Included now:
- axioms
- state-space definitions
- derivations
- constants registry
- solver modules
- simulations and artifact tracking
- whitepapers and LaTeX sections
- bibliography and cross-reference infrastructure
- operational modes (external formalisms mapped into CIEL operational roles)
- assumptions, decisions, falsification criteria, interfaces, provenance, benchmarks

Excluded for now:
- Omega runtime
- CQCL runtime integration
- memory/agent layers
- UI/persona/prompt infrastructure

## Source of truth
Source of truth is stored in:
- Markdown / TeX for formal and explanatory text
- YAML for registries, interfaces, assumptions, provenance, and cross-reference maps
- Python for executable realization

PDF files are generated artifacts, not source of truth.

## Repository grouping by object type
- `axioms/` — frozen axioms and registry
- `definitions/` — formal objects and registries
- `derivations/` — derivation texts and dependency DAG
- `interfaces/` — module contracts
- `src/ciel_foundations/` — executable realization
- `tests/` — symbolic, numeric, and falsification-facing tests
- `whitepapers/` — paper-backed explanatory modules
- `LaTeX/` — publication sections and appendices
- `bibliography/` — literature support surfaces
- `Simulations/` — code, results, registry
- `artifacts/` / `provenance/` / `falsification/` — traceability and failure criteria

## Global cross-reference principle
Repository-wide navigation should behave like a global organizational coupling graph:
\[
W_{ij}^{Global}: \text{object}_i \leftrightarrow \text{object}_j
\]
realized through hyperlinks, registries, dependency DAGs, interfaces, tests, simulations, artifacts, provenance, and bibliography.

# The-Fundamental-Theory-of-Informational-Relations
