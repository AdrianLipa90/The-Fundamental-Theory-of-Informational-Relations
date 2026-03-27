# DEF-0011 — Loose-thread bundle and effective White-Thread

## Status
`hypothesis`

## Depends on
- `DEF-0010`

## Objects defined here
1. `OBJ-LOOSE-THREAD-BUNDLE-0001`
2. `OBJ-EFFECTIVE-WHITE-THREAD-0001`

## Loose-thread bundle
For a fixed ordered pair \((i,j)\), define a finite family of admissible auxiliary transport paths
\[
\mathcal L_{ij} = \{\gamma_{ij}^{(a)}\}_{a=1}^{M}
\]
with associated primitive White-Thread amplitudes
\[
W_{ij}^{(a)} = W_{ij}[\gamma_{ij}^{(a)}].
\]
These are called the loose-thread bundle for the pair \((i,j)\).

## Effective White-Thread
Given nonnegative weights \(\alpha_a\ge 0\) satisfying
\[
\sum_{a=1}^{M} \alpha_a = 1,
\]
define the effective White-Thread amplitude by
\[
W_{ij}^{\mathrm{eff}} = \sum_{a=1}^{M} \alpha_a W_{ij}^{(a)}.
\]

## Canonical role
This object is the first dressed extension beyond the single-path primitive. It models a controlled aggregation of auxiliary transport channels without yet introducing a full non-abelian or dynamically reweighted bundle law.

## Immediate bound
If each primitive amplitude satisfies \(|W_{ij}^{(a)}|\le 1\), then
\[
|W_{ij}^{\mathrm{eff}}|\le 1
\]
by convexity and the triangle inequality.

## Scope restriction
This definition does not yet specify how the weights \(\alpha_a\) are generated dynamically. It only registers the first normalized aggregation law for loose-thread bundles.
