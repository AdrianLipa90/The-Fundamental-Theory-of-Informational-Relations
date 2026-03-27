# ASM-0002 — Unit-weight white-thread toy model

## Status
`explicit`

## Scope
Minimal white-thread primitive.

## Assumption
In the first executable white-thread layer, a pairwise path between two states is represented by a single phase-carrying transport channel with unit weight.

Formally, for a path phase \(\chi_{ij}\),
\[
W_{ij}^{(0)} = e^{i\chi_{ij}}.
\]

## Why this is an assumption
This is only the minimal primitive. It does not yet include:
- path ordering,
- nonabelian transport,
- magnitude/phase decomposition beyond unit magnitude,
- or the full downstream pairwise correction layer.
