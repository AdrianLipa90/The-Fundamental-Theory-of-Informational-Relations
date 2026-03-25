# T-0004 State to Phase Channels

Status: defined

## Scope
This document states the conceptual and structural role of the minimal operator that maps a projective two-level state into a finite angular channel set suitable for the minimal closure operator.

## Object links
- Definitions: DEF-0004 state, DEF-0009 closure
- Related derivations: D-0002-closure-operator, D-0003-state-vectorization
- Derivation: D-0004-state-to-phase-channels
- Notebook: NB-0004-state-to-phase-channels
- Source module: src/ciel_foundations/closure/phase_channels.py
- Simulations: Simulations/code/closure/state_to_closure_demo.py, Simulations/results/closure/

## Role of the operator
The operator builds the first explicit bridge between projective state and closure evaluation.

It answers:
1. How do we obtain a finite angular channel set from a normalized two-level state?
2. How do we do this without Fourier decomposition or arbitrary discretization?
3. How do we preserve gauge invariance with respect to global phase?

## Minimal regime
At the foundational start, the active channel set is the minimal two-angle chart induced by the Bloch-sphere realization:
- polar channel
- azimuthal channel

No white-thread coupling is used.
No Fourier/modal expansion is used.
No higher-dimensional channel family is injected.

## Structural statement
The minimal phase-channel operator is downstream of Bloch vectorization and upstream of closure evaluation.

## Admissibility role
The extracted channel tuple feeds the minimal closure operator directly. The resulting closure defect is therefore a deterministic function of the state.

## Falsification target
This module fails if:
- global phase changes alter the extracted channels away from chart conventions
- identical states produce different channel tuples
- closure values derived from the channels fail to be deterministic
- pole handling is inconsistent or hidden
