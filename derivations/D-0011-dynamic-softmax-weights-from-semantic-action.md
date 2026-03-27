# D-0011 — Dynamic softmax weights from semantic action

## Status
`hypothesis`

## Depends on
- `DEF-0011`
- `DEF-0012`

## Goal
Derive a normalized action-based weighting rule for loose-thread bundles and connect it to the effective White-Thread amplitude.

## Step 1 — Semantic action per path
For each path \(\gamma^{(a)}\), assign an action
\[
\mathcal S_a = \mathcal S(\gamma^{(a)}).
\]
The action summarizes path length, phase cost, relational defect, and truth penalty.

## Step 2 — Exponential weighting
Define
\[
\widetilde\alpha_a = e^{-\sigma \mathcal S_a},
\qquad \sigma\ge 0.
\]
These raw weights are nonnegative.

## Step 3 — Normalization
Normalize them by
\[
\alpha_a = \frac{\widetilde\alpha_a}{\sum_b \widetilde\alpha_b} = \frac{e^{-\sigma \mathcal S_a}}{\sum_b e^{-\sigma \mathcal S_b}}.
\]
Hence
\[
\alpha_a\ge 0,
\qquad
\sum_a \alpha_a = 1.
\]

## Step 4 — Effective White-Thread
Insert the dynamic weights into the loose-thread aggregation law:
\[
W_{ij}^{\mathrm{eff}} = \sum_a \alpha_a W_{ij}^{(a)}.
\]
This yields a first action-driven effective White-Thread object.

## Step 5 — Ordering property
If \(\sigma>0\) and \(\mathcal S_a < \mathcal S_b\), then
\[
\alpha_a > \alpha_b.
\]
Thus lower-action paths are dynamically favored.

## Result
The dynamic weights
\[
\alpha_a = \frac{e^{-\sigma \mathcal S_a}}{\sum_b e^{-\sigma \mathcal S_b}}
\]
provide the first non-arbitrary weighting law for loose-thread bundles and close the immediate gap between path cost and the effective White-Thread amplitude.
