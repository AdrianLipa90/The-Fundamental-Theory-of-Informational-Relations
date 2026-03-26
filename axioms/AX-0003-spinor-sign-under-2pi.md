# AX-0003 — Spinor sign under 2π rotation

## Status
`axiom`

## Statement
The minimal spinorial sector changes sign under a full 2π rotation.

\[
\psi(\phi + 2\pi) = -\psi(\phi)
\]

## Purpose
This axiom freezes the minimal spin-1/2 structure before any richer sector algebra is introduced.

## Immediate consequences
1. The minimal spinorial lift is double-valued over orbital angle.
2. Berry phase accumulation along suitable closed cycles can reproduce the minus sign.
3. Any future algebraic layer must remain compatible with a spinorial, not purely vectorial, closure.

## Depends on
- `AX-0001`
- `AX-0002`

## Downstream links
- `DEF-0002`
- `DEF-0003`
- `D-0002`
- `IF-0001`

## Falsification target
Any minimal implementation that returns the same state after a 2π spinorial cycle without a minus sign violates this axiom.
