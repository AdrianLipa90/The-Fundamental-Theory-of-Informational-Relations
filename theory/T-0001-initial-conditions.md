# T-0001 Initial Conditions

Status: defined

## Scope
This document states the conceptual and structural role of initial conditions in the CIEL foundations program.

## Object links
- Definitions: DEF-0002 information, DEF-0003 potential, DEF-0004 state, DEF-0005 boundary, DEF-0006 locality, DEF-0009 closure
- Derivation: D-0001-initial-conditions
- Notebook: NB-0001-initial-conditions
- Source module: src/ciel_foundations/initial_conditions/
- Simulations: Simulations/code/ic/, Simulations/results/ic/

## Role of initial conditions
Initial conditions are not treated as arbitrary numeric seeds. They are the first admissible structured state of the system under the declared foundational constraints.

The initial-conditions layer answers three questions:
1. What counts as an admissible initial state?
2. Which upstream structural objects determine that state?
3. Which data are primitive and which are derived at initialization?

## Foundational statement
An initial condition is a closure-admissible state-preparation object determined by declared structural inputs rather than by hidden fitted injection.

Minimal input tuple:
- potential
- chaos
- boundary condition
- locality condition
- optional arithmetic seed
- optional memory trace

Minimal output tuple:
- normalized projective state representative
- Bloch coordinates for the minimal two-level realization
- initialization metadata recording which inputs were active

## Non-arbitrariness rule
The initialization map must be deterministic from declared inputs. If two runs use the same declared inputs, they must yield the same canonical initialized state.

## Closure rule
No initial condition is admissible merely because it can be written down numerically. It must satisfy the active closure filter before entering downstream dynamics.

## Boundary/locality rule
Boundary and locality are not decorative tags. They determine what is allowed to count as an internal state-preparation regime and what is deferred to transport or sector coupling.

## Implementation target
The executable layer should expose a deterministic constructor that accepts the declared tuple of structural inputs and returns a canonical initialized state object with normalization and metadata checks.

## Falsification target
This module fails if any of the following is true:
- the same declared inputs yield non-identical initialized states
- normalization depends on hidden branch-specific logic
- closure admissibility is bypassed
- boundary/locality are declared but ignored in the executable mapping
