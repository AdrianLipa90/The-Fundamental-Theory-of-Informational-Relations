# D-0006 — White-thread primitive

## Status
`derived`

## Depends on
- `DEF-0002`
- `DEF-0006`
- `ASM-0002`

## Goal
Define the first executable pairwise transport object built on the Berry/phase layer.

## Step 1 — Phase-carrying path variable
Associate to a pair of states \((x_i,x_j)\) a path phase \(\chi_{ij}\).

## Step 2 — Minimal transport channel
Under the unit-weight toy assumption, define
\[
W_{ij}^{(0)} = e^{i\chi_{ij}}.
\]

## Step 3 — Interpretation
This is the smallest nontrivial pairwise transport object:
- it carries phase,
- it has unit magnitude,
- it is compatible with the Berry/closure layer,
- and it leaves nonabelian and magnitude extensions for later modules.

## Result
The white-thread primitive is the first executable pairwise transport object over the minimal CP1/Berry foundations layer.

## Scope restriction
This derivation does not yet provide path ordering, nonabelian transport, or the full downstream pairwise correction layer.
