# Initial Bloch State

## Metadata
- ID: GLOSS-0004
- Serial number: 4
- Canonical file name: bloch_state.md
- Status: planned
- Glossary registry row: glossary/registry.csv#4

## Short definition
The initial Bloch state is the first projective state generated from chaos, potential, and relation.

## Symbol
psi_0

## Equation
psi_0=(cos(theta/2), exp(i phi) sin(theta/2))^T

## Function / role
Serves as the initial state of the solver after primitive ontology is mapped onto Bloch geometry.

## Derivation path
- Axiom(s): AX-001-projective-state (downstream state consequence)
- Definition(s): state interface
- Derivation(s): D-0002-initial-conditions

## Code binding
- Module: src/ciel_foundations/initial_conditions/bloch_initializer.py
- Function/Class: initialize_bloch_state
- Tests: tests/numeric/test_bloch_initializer.py

## Cross references
- derivations/D-0002-initial-conditions.md
- interfaces/state_interface.yaml
- src/ciel_foundations/initial_conditions/

## Notes
This is the first state object downstream of the primitive ontology.