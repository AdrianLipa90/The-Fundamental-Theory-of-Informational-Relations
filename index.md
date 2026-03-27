# Canonical Index

This file is the human-readable navigation spine for the Foundations repository.
It complements `README.md` and `INDEX.md` by grouping current canonical entrypoints, active modules, registries, paper outputs, and executable bindings.

## Root navigation stack
- `README.md` — public entrypoint and quick navigation
- `INDEX.md` — root governance map and grouped canonical contents
- `index.md` — human-readable navigation spine
- `registries/global_index_registry.yaml` — machine-readable root authority
- `systems/CIEL_FOUNDATIONS/ORCHESTRATOR.md` — orchestration layer for active modules

## Canonical workflow
Axiom -> Definition -> Derivation -> Implementation -> Test -> Status -> Interpretation

## Governance and authority
- [README](README.md)
- [INDEX](INDEX.md)
- [AGENT](AGENT.md)
- [PROJECT_CHARTER](PROJECT_CHARTER.md)
- [ORGANIZATION](ORGANIZATION.md)
- [STRUCTURE](STRUCTURE.md)
- [ROADMAP](ROADMAP.md)
- [Global index registry](registries/global_index_registry.yaml)
- [Global cross-reference map](registries/global_cross_reference_map.yaml)
- [Agent authority registry](registries/agent_authority_registry.yaml)

## Active canonical modules
### Minimal projective / Berry / spin
- [DEF-0001](definitions/DEF-0001-projective-ray-and-cp1.md)
- [DEF-0002](definitions/DEF-0002-berry-connection-and-phase.md)
- [DEF-0003](definitions/DEF-0003-closure-functional.md)
- [D-0001](derivations/D-0001-hilbert-to-projective-cp1.md)
- [D-0002](derivations/D-0002-berry-phase-and-spinor-sign.md)
- [IF-0001](interfaces/IF-0001-minimal-cp1-berry-spin.yaml)

### Tetrahedral relational frame
- [DEF-0004](definitions/DEF-0004-regular-tetrahedron-on-s2.md)
- [D-0003](derivations/D-0003-regular-tetrahedron-on-s2.md)
- [IF-0002](interfaces/IF-0002-tetrahedral-relational-frame.yaml)

### Local attractor / nonlocal holonomic vortex
- [AX-0005](axioms/AX-0005-local-attractor-hierarchy.md)
- [DEF-0005](definitions/DEF-0005-local-attractor-and-order-parameter.md)
- [DEF-0006](definitions/DEF-0006-nonlocal-holonomic-vortex.md)
- [D-0004](derivations/D-0004-local-attractor-axis-and-coriolis.md)
- [D-0005](derivations/D-0005-spacetime-holonomic-circulation.md)
- [IF-0004](interfaces/IF-0004-nonlocal-holonomic-vortex.yaml)

### Fractal foundations spine at piko scale
- [DEF-0007](definitions/DEF-0007-fractal-foundations-spine.md)
- [D-0006](derivations/D-0006-fractal-inheritance-chain.md)
- [IF-0005](interfaces/IF-0005-piko-fractal-spine.yaml)

## Executable bindings
### Solvers
- [minimal_cp1_berry_spin_solver.py](src/ciel_foundations/solvers/minimal_cp1_berry_spin_solver.py)
- [tetrahedral_relational_frame_solver.py](src/ciel_foundations/solvers/tetrahedral_relational_frame_solver.py)
- [nonlocal_holonomic_vortex_solver.py](src/ciel_foundations/solvers/nonlocal_holonomic_vortex_solver.py)
- [piko_fractal_spine_solver.py](src/ciel_foundations/solvers/piko_fractal_spine_solver.py)

### Tests
- [test_projective_state.py](tests/test_projective_state.py)
- [test_berry_and_closure.py](tests/test_berry_and_closure.py)
- [test_tetrahedral_relational_frame.py](tests/test_tetrahedral_relational_frame.py)
- [test_nonlocal_holonomic_vortex.py](tests/test_nonlocal_holonomic_vortex.py)
- [test_piko_fractal_spine.py](tests/test_piko_fractal_spine.py)

### Simulations
- [sim_cp1_berry_spin.py](Simulations/code/sim_cp1_berry_spin.py)
- [sim_nonlocal_holonomic_vortex.py](Simulations/code/sim_nonlocal_holonomic_vortex.py)
- [sim_piko_fractal_spine.py](Simulations/code/sim_piko_fractal_spine.py)

## Paper outputs
### Whitepapers
- [WP-MOD-minimal-projective-berry-spin](whitepapers/WP-MOD-minimal-projective-berry-spin.md)
- [WP-MOD-tetrahedral-relational-frame](whitepapers/WP-MOD-tetrahedral-relational-frame.md)
- [WP-MOD-local-attractor-holonomic-vortex](whitepapers/WP-MOD-local-attractor-holonomic-vortex.md)
- [WP-MOD-fractal-foundations-spine](whitepapers/WP-MOD-fractal-foundations-spine.md)

### LaTeX
- [SEC-0002](LaTeX/sections/SEC-0002-tetrahedral-relational-frame.tex)
- [SEC-0003](LaTeX/sections/SEC-0003-local-attractor-holonomic-vortex.tex)
- [SEC-0004](LaTeX/sections/SEC-0004-fractal-foundations-spine.tex)
- [APP-0001](LaTeX/appendices/APP-0001-minimal-cp1-berry-spin-numerical-derivations.tex)
- [APP-0002](LaTeX/appendices/APP-0002-tetrahedral-frame-numerical-derivations.tex)
- [APP-0003](LaTeX/appendices/APP-0003-rotating-superfluid-field-numerical-derivations.tex)
- [APP-0004](LaTeX/appendices/APP-0004-piko-fractal-spine-numerical-derivations.tex)

## Registries and bibliography
- [definitions registry](definitions/definitions_registry.yaml)
- [derivations registry](derivations/derivations_registry.yaml)
- [simulations registry](Simulations/registry/simulations_registry.yaml)
- [artifacts registry](artifacts/artifacts_registry.yaml)
- [bibliography README](bibliography/README.md)
- [foundations seed bibliography](bibliography/foundations_seed.bib)

## Cross-reference principle
The repository-wide navigation spine behaves like an organizational coupling graph:
\[
W_{ij}^{Global}: \text{object}_i \leftrightarrow \text{object}_j
\]
implemented through hyperlinks, registries, dependency DAGs, interfaces, tests, simulations, artifacts, provenance, and bibliography.