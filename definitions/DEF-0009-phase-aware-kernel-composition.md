# DEF-0009 — Phase-aware composition of the pairwise coupling kernel

## Status
`hypothesis`

## Depends on
- `DEF-0002`
- `DEF-0003`
- `DEF-0008`

## Objects defined here
1. `OBJ-PHASE-AWARE-KERNEL-0001`
2. `OBJ-PHASE-ALIGNMENT-0001`
3. `OBJ-CLOSURE-WEIGHT-0001`

## Goal
Refine the abstract pairwise kernel \(A_{ij}\) into an explicit phase-aware composition built from pairwise holonomy magnitude, phase alignment, and closure defect.

## Phase alignment factor
For a relative phase difference
\[
\delta\gamma_{ij} = \gamma_i - \gamma_j,
\]
define the phase-alignment weight
\[
g_{\mathrm{phase}}(\delta\gamma_{ij};\lambda)
=
\exp\!\big[-\lambda(1-\cos\delta\gamma_{ij})\big],
\qquad \lambda\ge 0.
\]
This factor is maximal for aligned phases and remains symmetric under \(i\leftrightarrow j\).

## Closure weight
For a closure-defect magnitude
\[
R_H = |\Delta_H|^2,
\]
define the closure weight
\[
g_{\mathrm{closure}}(R_H;\mu)=\exp(-\mu R_H),
\qquad \mu\ge 0.
\]
This penalizes configurations with large closure defect.

## Phase-aware kernel
Given a pairwise holonomy magnitude \(|W_{ij}|\), define the phase-aware kernel candidate
\[
A_{ij}
=
|W_{ij}|\,g_{\mathrm{phase}}(\delta\gamma_{ij};\lambda)\,g_{\mathrm{closure}}(R_H;\mu).
\]

## Canonical role
This object is the first explicit candidate answer to the question of how the abstract pairwise kernel \(A_{ij}\) should be composed from already-registered piko objects.

## Scope restriction
This definition does not yet prove that this is the unique or final composition law. It registers a concrete, testable hypothesis that refines the more abstract kernel in `DEF-0008`.
