# ciel_foundations

This folder is the executable realization layer of the public theory repository.

## Role
Code here must remain downstream of:
- axioms
- definitions
- derivations
- interfaces
- assumptions

It is upstream of:
- tests
- artifacts
- benchmarks
- executable whitepaper references

## Maintenance rules
- Do not treat source code as the hidden source of truth.
- Every public object implemented here must have an upstream registry anchor.
- Every module should expose explicit input/output contracts.
- Every behavior change should be matched by tests and provenance updates.

## Current module order
1. initial_conditions
2. bloch
3. closure
4. holonomy
5. tau_solver
6. genesis
