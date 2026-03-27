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
implemented through hyperlinks, registries, dependency DAGs, interfaces, tests, artifacts, and provenance.

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

### Paper layer
- [whitepapers/](../../whitepapers/)
- [LaTeX/](../../LaTeX/)

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
- [solver](../../src/ciel_foundations/solvers/minimal_cp1_berry_spin_solver.py)
- [tests](../../tests/test_projective_state.py)
- [tests](../../tests/test_berry_and_closure.py)
- [whitepaper](../../whitepapers/WP-MOD-minimal-projective-berry-spin.md)
- [appendix](../../LaTeX/appendices/APP-0001-minimal-cp1-berry-spin-numerical-derivations.tex)

### Tetrahedral extension chain
- [DEF-0004](../../definitions/DEF-0004-regular-tetrahedron-on-s2.md)
- [D-0003](../../derivations/D-0003-regular-tetrahedron-on-s2.md)
- [IF-0002](../../interfaces/IF-0002-tetrahedral-relational-frame.yaml)
- [solver](../../src/ciel_foundations/solvers/tetrahedral_relational_frame_solver.py)
- [test](../../tests/test_tetrahedral_relational_frame.py)
- [whitepaper](../../whitepapers/WP-MOD-tetrahedral-relational-frame.md)
- [section](../../LaTeX/sections/SEC-0002-tetrahedral-relational-frame.tex)
- [appendix](../../LaTeX/appendices/APP-0002-tetrahedral-frame-numerical-derivations.tex)

## Routing policy
1. Start from `INDEX.md` or `index.md`.
2. Enter the target object through its registry or interface.
3. Follow the dependency DAG upstream before touching downstream code.
4. Use this orchestrator only as a global navigator, never as an alternative source of truth.

## Next downstream modules to orchestrate
- active closure law
- white-thread primitives
- tau-from-coupling layer
- tensor-scalar extension
- algebra layer targets: SO(3), SU(2), U(1)
