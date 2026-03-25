# T-0003 State / Phase Vectorization

Status: defined

## Scope
This document states the conceptual and structural role of the minimal vectorization operator that converts a projective two-level state into a deterministic finite real vector without invoking Fourier analysis.

## Object links
- Definitions: DEF-0004 state, DEF-0005 boundary, DEF-0006 locality
- Derivation: D-0003-state-vectorization
- Notebook: NB-0003-state-vectorization
- Source module: src/ciel_foundations/initial_conditions/vectorization.py
- Simulations: Simulations/code/ic/vectorization_demo.py, Simulations/results/ic/vectorization/

## Role of vectorization
The vectorization operator provides a deterministic, gauge-invariant finite representation of the minimal state needed for downstream closure and dynamics analysis.

It exists to answer:
1. How is a normalized projective state represented without arbitrary hidden coordinates?
2. Which representation is invariant under global phase?
3. How do we obtain finite real coordinates suitable for computation before any justified discretization or spectral analysis?

## Metatime compatibility
At this stage, no Fourier decomposition is used.
No modal expansion is introduced.
The operator remains finite, explicit, and chart-aware.

## Structural statement
For the minimal CP^1 realization, the preferred vectorization is the Bloch-sphere image of the projective state.

This representation is:
- finite
- deterministic
- invariant under global phase
- normalized
- directly computable from the state amplitudes

## Output forms
Primary output:
- Bloch vector n = (n_x, n_y, n_z)

Secondary chart output:
- angular chart (theta, phi)

## Non-arbitrariness rule
The vectorization map may not depend on arbitrary Fourier modes or undeclared discretization.

## Falsification target
This module fails if:
- global phase changes alter the vectorization result
- normalized states fail to map to unit Bloch norm
- the implementation depends on branch-specific hidden conventions
- chart extraction is inconsistent with the Bloch vector
