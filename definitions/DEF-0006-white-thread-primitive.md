# DEF-0006 — White-thread primitive

## Status
`defined`

## Depends on
- `DEF-0002`
- `ASM-0002`

## Object defined here
- `OBJ-WHITE-THREAD-PRIMITIVE-0001`

## Definition
For a pair of states \((x_i,x_j)\) and an associated path phase \(\chi_{ij}\), define the minimal white-thread primitive by
\[
W_{ij}^{(0)} = e^{i\chi_{ij}}.
\]

## Meaning
This is the first executable pairwise transport object built over the Berry/phase layer.
It captures only phase transport and unit magnitude.

## Scope restriction
This primitive does not yet include nonabelian transport, path ordering, or a separate magnitude channel.
