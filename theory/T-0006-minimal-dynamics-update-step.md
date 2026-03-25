# T-0006 Minimal Dynamics / Update Step

Status: defined

## Scope
This document states the conceptual and structural role of the minimal update-step operator for the current Metatime-compatible CP^1 foundations stack.

## Object links
- Definition: DEF-0009 closure
- Related derivations: D-0002-closure-operator, D-0004-state-to-phase-channels, D-0005-admissibility-correction-logic
- Derivation: D-0006-minimal-dynamics-update-step
- Notebook: NB-0006-minimal-dynamics-update-step
- Source module: src/ciel_foundations/closure/dynamics.py
- Simulations: Simulations/code/closure/dynamics_demo.py, Simulations/results/closure/

## Role
This layer introduces the first deterministic update step for the minimal channel state.

It answers:
1. how is a proposed channel update generated?
2. when is an update accepted?
3. when is rollback used?
4. when is correction used instead of rollback?

## Minimal regime
At this stage the dynamical object is the finite channel vector

Γ = (γ_1, γ_2)

and the proposed update is given by a finite increment vector

V = (ν_1, ν_2)

with step size dt.

No Fourier decomposition is used.
No white-thread coupling is used.
No higher-dimensional transport term is injected.

## Structural statement
A proposed step is first formed, then evaluated by the closure defect. The acceptance logic is deterministic and explicit.

## Core modes
- accept-if-nonworsening
- rollback
- correction

## Metatime compatibility
The current minimal step preserves:
- explicit phase channels
- explicit closure evaluation
- deterministic update logic
- explicit rollback/correction policy

## Falsification target
This module fails if:
- rollback-enabled updates accept a worse closure defect
- identical inputs yield different accepted outputs
- correction logic worsens closure
- branch-specific hidden logic determines the accepted step
