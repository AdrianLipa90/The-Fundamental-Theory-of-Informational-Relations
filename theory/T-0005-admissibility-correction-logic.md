# T-0005 Admissibility / Correction Logic

Status: defined

## Scope
This document states the conceptual and structural role of admissibility and correction logic in the minimal Metatime-compatible closure stack.

## Object links
- Definition: DEF-0009 closure
- Related derivations: D-0002-closure-operator, D-0004-state-to-phase-channels
- Derivation: D-0005-admissibility-correction-logic
- Notebook: NB-0005-admissibility-correction-logic
- Source module: src/ciel_foundations/closure/admissibility.py
- Simulations: Simulations/code/closure/admissibility_demo.py, Simulations/results/closure/

## Role
This layer decides what the system does when the closure defect is evaluated.

It answers:
1. when is a configuration admissible?
2. when is it rejected?
3. when is it corrected?
4. what is the minimal deterministic correction rule at the foundational CP^1 layer?

## Minimal regime
At this stage the logic acts only on the finite phase-channel vector.
No white-thread coupling is used.
No higher-dimensional transport correction is used.
No hidden fitted damping terms are introduced.

## Structural statement
Given a closure defect C_H and tolerance ε_C:
- if C_H ≤ ε_C, the configuration is admissible
- otherwise the logic must either reject the configuration or deterministically project it to a closure-admissible channel configuration

## Minimal correction principle
The preferred minimal correction is projection to the coherent diagonal channel manifold, using a deterministic reference phase.

## Metatime compatibility
This layer is compatible with the current minimal Metatime bootstrap because it preserves:
- explicit phase channels
- explicit closure defect
- deterministic evolution of admissibility decisions
- no hidden stochastic branch logic

## Falsification target
This module fails if:
- admissible configurations are altered without cause
- correction is non-deterministic for identical inputs
- correction worsens the closure defect
- anti-phase degeneracy is resolved by hidden or branch-specific conventions
