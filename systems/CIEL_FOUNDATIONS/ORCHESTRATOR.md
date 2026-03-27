# CIEL Foundations Orchestrator

## Status
`defined`

## Purpose
This file is the human-readable orchestration layer for the canonical foundations repository.
It does not replace the source-of-truth objects. It routes between them.

Organizationally, it plays the role of a repository-wide coupling spine:
\[
W_{ij}^{Global}: \text{object}_i \leftrightarrow \text{object}_j
\]
implemented through hyperlinks, registries, dependency DAGs, interfaces, tests, artifacts, provenance, and bibliography.

## Core rule
Nothing becomes stable here by narration alone.
Routing must always preserve:
\[
\text{Axiom} \to \text{Definition} \to \text{Derivation} \to \text{Implementation} \to \text{Test} \to \text{Status} \to \text{Interpretation}.
\]

## Layered entrypoints
### Governance
- [README.md](../../README.md)
- [AGENT.md](../../AGENT.md)
- [INDEX.md](../../INDEX.md)
- [index.md](../../index.md)
- [PROJECT_CHARTER.md](../../PROJECT_CHARTER.md)
- [ORGANIZATION.md](../../ORGANIZATION.md)
- [STRUCTURE.md](../../STRUCTURE.md)
- [ROADMAP.md](../../ROADMAP.md)
- [Agent authority](../../registries/agent_authority_registry.yaml)
- [Bibliography](../../bibliography/README.md)

### Canonical formal layer
- [axioms/](../../axioms/)
- [definitions/](../../definitions/)
- [derivations/](../../derivations/)
- [interfaces/](../../interfaces/)
- [registries/global_cross_reference_map.yaml](../../registries/global_cross_reference_map.yaml)

### Executable layer
- [src/ciel_foundations/](../../src/ciel_foundations/)
- [tests/](../../tests/)
- [Simulations/](../../Simulations/)
- [artifacts/](../../artifacts/)
- [provenance/](../../provenance/)
- [falsification/](../../falsification/)

### Paper and source layer
- [whitepapers/](../../whitepapers/)
- [LaTeX/](../../LaTeX/)
- [bibliography/](../../bibliography/)

## Current active module group
### Minimal projective / Berry / spin chain
- [AX-0001](../../axioms/AX-0001-projective-state-space.md)
- [AX-0002](../../axioms/AX-0002-kahler-fubini-study-structure.md)
- [AX-0003](../../axioms/AX-0003-spinor-sign-under-2pi.md)
- [DEF-0001](../../definitions/DEF-0001-projective-ray-and-cp1.md)
- [DEF-0002](../../definitions/DEF-0002-berry-connection-and-phase.md)
- [DEF-0003](../../definitions/DEF-0003-closure-functional.md)
- [D-0001](../../derivations/D-0001-hilbert-to-projective-cp1.md)
- [D-0002](../../derivations/D-0002-berry-phase-and-spinor-sign.md)
- [IF-0001](../../interfaces/IF-0001-minimal-cp1-berry-spin.yaml)

### Tetrahedral extension chain
- [DEF-0004](../../definitions/DEF-0004-regular-tetrahedron-on-s2.md)
- [D-0003](../../derivations/D-0003-regular-tetrahedron-on-s2.md)
- [IF-0002](../../interfaces/IF-0002-tetrahedral-relational-frame.yaml)

### Local attractor / nonlocal holonomic vortex chain
- [AX-0005](../../axioms/AX-0005-local-attractor-hierarchy.md)
- [DEF-0005](../../definitions/DEF-0005-local-attractor-and-order-parameter.md)
- [DEF-0006](../../definitions/DEF-0006-nonlocal-holonomic-vortex.md)
- [D-0004](../../derivations/D-0004-local-attractor-axis-and-coriolis.md)
- [D-0005](../../derivations/D-0005-spacetime-holonomic-circulation.md)
- [IF-0004](../../interfaces/IF-0004-nonlocal-holonomic-vortex.yaml)

### Fractal foundations spine chain
- [DEF-0007](../../definitions/DEF-0007-fractal-foundations-spine.md)
- [D-0006](../../derivations/D-0006-fractal-inheritance-chain.md)
- [IF-0005](../../interfaces/IF-0005-piko-fractal-spine.yaml)

### Tau from coupling chain
- [DEF-0008](../../definitions/DEF-0008-pairwise-coupling-kernel.md)
- [D-0007](../../derivations/D-0007-tau-from-coupling-laplacian.md)
- [IF-0006](../../interfaces/IF-0006-tau-from-coupling.yaml)
- [solver](../../src/ciel_foundations/solvers/tau_from_coupling_solver.py)
- [test](../../tests/test_tau_from_coupling.py)
- [whitepaper](../../whitepapers/WP-MOD-tau-from-coupling.md)
- [section](../../LaTeX/sections/SEC-0005-tau-from-coupling.tex)
- [appendix](../../LaTeX/appendices/APP-0005-tau-from-coupling-numerical-derivations.tex)

### Phase-aware kernel composition chain
- [DEF-0009](../../definitions/DEF-0009-phase-aware-kernel-composition.md)
- [D-0008](../../derivations/D-0008-kernel-from-holonomy-phase-and-closure.md)
- [IF-0007](../../interfaces/IF-0007-phase-aware-kernel-composition.yaml)
- [solver](../../src/ciel_foundations/solvers/phase_aware_kernel_solver.py)
- [test](../../tests/test_phase_aware_kernel.py)
- [whitepaper](../../whitepapers/WP-MOD-phase-aware-kernel-composition.md)
- [section](../../LaTeX/sections/SEC-0006-phase-aware-kernel-composition.tex)

## Routing policy
1. Start from `README.md`, `INDEX.md`, or `index.md`.
2. Enter the target object through its registry or interface.
3. Follow the dependency DAG upstream before touching downstream code.
4. Use this orchestrator only as a global navigator, never as an alternative source of truth.
5. Treat bibliography as support for attribution and context, not as an automatic epistemic upgrade.

## Next downstream modules to orchestrate
- active closure law
- white-thread primitives
- tensor-scalar extension
- algebra layer targets: SO(3), SU(2), U(1)
