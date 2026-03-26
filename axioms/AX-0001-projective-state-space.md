# AX-0001 — Projective state space

## Status
`axiom`

## Statement
Physical states are rays in a complex Hilbert space, not raw vectors.

\[
\text{state} = [\psi] \in \mathbb{P}(\mathcal H)
\]

where two vectors represent the same physical state iff they differ by a nonzero complex scalar.

## Purpose
This removes global phase redundancy and fixes the minimal ontological level on which later geometry, closure, and transport are defined.

## Immediate consequences
1. Any physical quantity must descend from ray space, not depend on a representative vector.
2. A minimal two-level reduction lives on \(\mathbb{CP}^1\).
3. Berry transport and spin structure are downstream objects over projective state space.

## Depends on
None. Foundational axiom.

## Downstream links
- `AX-0002`
- `DEF-0001`
- `D-0001`
- `IF-0001`

## Falsification target
Any implementation that depends on global phase of a representative vector violates this axiom.
