# DEF-0003 — Closure functional

## Status
`defined`

## Depends on
- `AX-0003`
- `DEF-0002`

## Object defined here
- `OBJ-CLOSURE-FUNCTIONAL-0001`

## Definition
Given a finite family of transported phases \(\{\phi_k\}\), define the closure functional:
\[
\Delta_H = \sum_k e^{i\phi_k}.
\]

Associated defect magnitude:
\[
R_H = |\Delta_H|^2.
\]

## Meaning
\(\Delta_H\) is a compact summary of phase closure defect. It partitions candidate cycles or transported phase families into more coherent and less coherent classes.

## Scope restriction
This definition does **not** yet freeze whether the canonical admissibility condition is:
- exact closure \(\Delta_H = 0\), or
- nonzero residual defect \(\Delta_H = \varepsilon \neq 0\).

That choice belongs to the derivation layer and later falsification.

## Canonical role
This is the first registered closure object used by:
- minimal toy simulations,
- acceptance/rollback logic,
- later Euler/Berry/holonomy interaction.

## Falsification target
A closure implementation that is inconsistent under phase-periodicity or basic complex-sum invariance violates this definition.
