# Tests Index

This index organizes the canonical testing layer.

## Role
Tests are the executable epistemic gate of the repository.
No module should be treated as stable or derived without tests appropriate to its layer.

## Test categories
- `symbolic/` — exact/algebraic identities and structural invariants
- `numeric/` — numerical realizations, stability checks, convergence checks
- `regression/` — canonical behavior preserved across changes
- `falsification/` — explicit failure-target checks tied to falsification criteria

## Current state
The category folders exist, but they are still mostly placeholders.
This means the repository has testing structure without enough object-level coverage.

## Test obligations by layer
- axioms: structural consistency and dependency discipline
- definitions: registry/definition coherence
- derivations: explicit equation or dependency checks where executable
- code modules: unit and integration tests
- constants: invariant/value-path tests
- sectors: inheritance and no-local-redefinition tests

## Immediate next step
Replace placeholder test READMEs with real tests for:
1. initial conditions
2. closure rollback/acceptance logic
3. registry coherence
4. constant dependency integrity
