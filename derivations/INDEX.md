# Derivations Index

This index organizes the derivation layer of the repository.

## Role
Derivations convert canonical definitions into explicit mathematical objects and executable obligations.
They must remain downstream of axioms and definitions, and upstream of code, tests, and interpretation.

## Canonical sources here
- `dependency_graph.yaml`
- `module_map.yaml`
- future `D-####-*.md` derivation documents

## Current state
The dependency graph and module map exist, but the repository still lacks a populated set of canonical derivation documents.
That means the structure of dependency exists, but the formal chain is not yet fully written.

## Required derivation sequence
1. initial conditions
2. Bloch dynamics
3. closure regulator
4. holonomy / white-thread layer
5. tau solver
6. genesis of constants
7. sector inheritance

## Rule
No derivation may silently introduce:
- new constants
- new dependencies
- hidden fitted inputs
- runtime-only assumptions

## Immediate next step
Convert dependency skeleton into explicit derivation files and bind each one to interfaces, tests, and falsification entries.
