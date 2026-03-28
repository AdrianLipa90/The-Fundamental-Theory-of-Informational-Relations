# D-0012 — Semantic action assembled from measurement operators

## Status
`hypothesis`

## Depends on
- `DEF-0012`
- `DEF-0013`

## Goal
Show that the action-based loose-thread weighting law can be written entirely in terms of explicit measurement operators.

## Step 1 — Component operators
Take the nonnegative trajectory operators
\[
\widehat L[\gamma],\qquad \widehat{\Delta\phi}[\gamma],\qquad \widehat D_{rel}[\gamma],\qquad \widehat\Pi_{truth}^{struct}[\gamma].
\]
Each returns a scalar cost for the same admissible path \(\gamma\).

## Step 2 — Linear assembly
For nonnegative coefficients \(\alpha,\beta,\kappa,\mu\ge 0\), define
\[
\mathcal S_{online}[\gamma] = \alpha\widehat L[\gamma] + \beta\widehat{\Delta\phi}[\gamma] + \kappa\widehat D_{rel}[\gamma] + \mu\widehat\Pi_{truth}^{struct}[\gamma].
\]
This is the online semantic action.

## Step 3 — Full action with audit term
When a completed artifact is available, extend the online action by
\[
\mathcal S_{full} = \mathcal S_{online} + \nu\widehat\Pi_{truth}^{audit},
\qquad \nu\ge 0.
\]
This separates trajectory dynamics from post-hoc artifact auditing.

## Step 4 — Insertion into the dynamic weighting law
For a loose-thread bundle \(\{\gamma^{(a)}\}\), define
\[
\alpha_a = \frac{e^{-\sigma \mathcal S(\gamma^{(a)})}}{\sum_b e^{-\sigma \mathcal S(\gamma^{(b)})}},
\qquad \sigma\ge 0.
\]
Then the effective White-Thread becomes
\[
W_{ij}^{eff} = \sum_a \alpha_a W_{ij}^{(a)}.
\]

## Result
The action-driven bundle law is no longer symbolic only. It is assembled from explicit trajectory and audit measurement operators.

## Scope restriction
This derivation closes the assembly law only. It does not yet derive the final semantic metric, the final truth potential, or the calibrated coefficient set.
