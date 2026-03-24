# Source Package Index

This index organizes the executable theory-facing Python package.

## Role
`src/ciel_foundations/` is the executable realization layer of the public theory repository.
It is downstream of:
- axioms
- definitions
- derivations
- interfaces

It is upstream of:
- tests
- artifacts
- whitepapers that reference executable realization

## Current packages
- `initial_conditions/`
- `bloch/`
- `closure/`
- `holonomy/`
- `tau_solver/`
- `genesis/`

## Current state
Package structure exists, but most modules are still minimal stubs.
That means source layout is established, but executable content remains to be expanded.

## Rule
No package here may become the hidden source of truth for objects that are not registered upstream.

## Immediate next step
Upgrade packages in this order:
1. initial_conditions
2. closure
3. holonomy
4. tau_solver
5. genesis
6. bloch dynamics integration
