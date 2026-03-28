# D-0010 — Effective White-Thread from a loose-thread bundle

## Status
`hypothesis`

## Depends on
- `DEF-0010`
- `DEF-0011`

## Goal
Derive the first normalized effective White-Thread amplitude from a finite bundle of primitive transport channels.

## Step 1 — Primitive family
For a fixed pair \((i,j)\), take a finite family of primitive amplitudes
\[
W_{ij}^{(a)} = W_{ij}[\gamma_{ij}^{(a)}],
\qquad a=1,\dots,M.
\]
Each primitive satisfies \(|W_{ij}^{(a)}|\le 1\) in the minimal abelian toy sector.

## Step 2 — Normalized nonnegative weights
Let \(\alpha_a\ge 0\) with
\[
\sum_{a=1}^{M} \alpha_a = 1.
\]
Define
\[
W_{ij}^{\mathrm{eff}} = \sum_{a=1}^{M} \alpha_a W_{ij}^{(a)}.
\]

## Step 3 — Reduction to the primitive case
If the bundle contains a single channel with weight one, then
\[
W_{ij}^{\mathrm{eff}} = W_{ij}^{(1)},
\]
so the effective object reduces to the primitive one.

## Step 4 — Magnitude bound
Using the triangle inequality,
\[
|W_{ij}^{\mathrm{eff}}|
= \left|\sum_a \alpha_a W_{ij}^{(a)}\right|
\le \sum_a \alpha_a |W_{ij}^{(a)}|
\le \sum_a \alpha_a = 1.
\]

## Result
The loose-thread bundle defines a first dressed White-Thread object
\[
W_{ij}^{\mathrm{eff}} = \sum_a \alpha_a W_{ij}^{(a)}
\]
that remains bounded and reduces correctly to the primitive case.

## Scope restriction
This derivation closes only the normalized convex aggregation law. It does not yet derive a dynamic path-selection rule or a full bundle dynamics.
