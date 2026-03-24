# AGENT.md

## Role of this repository
This repository is the public first-principles theory layer for CIEL. It is not Omega runtime, not a recovery container, and not a mixed archive. Omega may later consume only stabilized exports from this tree.

## Source-of-truth rule
Source of truth is limited to:
- Markdown / TeX for formal text
- YAML for registries, interfaces, assumptions, provenance, and dependency maps
- Python for executable realization

PDF files are generated artifacts only.

## Primary startup algorithm
Every work session in this repository must begin with the following algorithm.

1. Re-read `README.md`, `PROJECT_CHARTER.md`, `ORGANIZATION.md`, `STRUCTURE.md`, and `ROADMAP.md`.
2. Treat `main` as the only canonical base unless a branch is explicitly declared as the active working canon.
3. Determine the exact target layer of the requested work:
   - axiom
   - definition
   - derivation
   - implementation
   - test
   - status / falsification
   - interpretation
4. Register or update the object before adding downstream prose or code.
5. Check dependency direction explicitly:
   - axioms -> definitions -> derivations -> code -> tests -> artifacts -> interpretation
6. Do not add code without an upstream formal object.
7. Do not add interpretation that introduces new equations, constants, or dependencies.
8. Do not patch Omega-facing runtime logic into this repository.
9. Before claiming completion, update all affected registries, links, and status markers.
10. Before merge, verify that the change preserves a single source of truth and does not create parallel copies.

## Canonical workflow
Axiom -> Definition -> Derivation -> Implementation -> Test -> Status -> Interpretation

## Hard gates
A module may not be presented as stable or derived unless all of the following are true:
- assumptions are explicit
- interface is explicit
- dependency links are explicit
- tests exist
- falsification target exists
- provenance / artifacts can be traced
- registry entries are synchronized

## Public-repo hygiene
This repository is public and theory-facing.
It must not contain:
- raw recovery snapshots
- forensic merge debris
- private logs or local databases
- model binaries
- Omega runtime source-of-truth logic
- unpublished mixed archives

Public theory objects must enter by allowlisted canonical placement, not by dumping mixed tarball contents.

## Planning rule
Planning is not separate from structure.
Every plan must identify:
- current state
- target state
- dependency order
- concrete next artifacts
- tests / falsification criteria
- registry changes required

## Failure conditions
Work is not complete if any of the following remains true:
- the object is not registered
- the dependency path is ambiguous
- a placeholder is presented as derived content
- interpretation outruns derivation
- code exists without an upstream formal object
- tests or falsification criteria are missing
- multiple conflicting sources of truth exist for the same object

## Immediate priority of this repository
1. Freeze the foundational axioms in canonical form.
2. Populate definitions registries with real objects.
3. Turn placeholders in initial conditions, closure, holonomy, tau, and genesis into executable minimal modules.
4. Bind each module to tests and falsification entries.
5. Export only stabilized operators/constants/constraints downstream to Omega.
