# D-0005 — Spacetime holonomic circulation and nonlocal vortex criterion

## Status
`derived`

## Depends on
- `DEF-0002`
- `DEF-0003`
- `DEF-0006`

## Goal
Derive a gauge/global-phase-invariant circulation criterion for nonlocal holonomic vortices in spacetime.

## Step 1 — Effective phase-flow one-form
Start with
\[
u_\mu = \partial_\mu \theta - A_\mu.
\]

## Step 2 — Gauge/global-phase invariance
Under a local phase shift
\[
\theta \mapsto \theta + \chi,
\qquad
A_\mu \mapsto A_\mu + \partial_\mu \chi,
\]
we obtain
\[
u_\mu \mapsto \partial_\mu(\theta+\chi) - (A_\mu + \partial_\mu \chi) = \partial_\mu \theta - A_\mu = u_\mu.
\]
Hence \(u_\mu\) is invariant under the compensated phase/connection shift.

## Step 3 — Closed spacetime loop
For a closed spacetime loop \(\mathcal C\), define
\[
\Gamma[\mathcal C] = \oint_{\mathcal C} u_\mu\,dx^\mu.
\]
Because \(u_\mu\) is gauge-invariant in Step 2, \(\Gamma[\mathcal C]\) is also gauge-invariant.

## Step 4 — Nonlocal holonomic vortex criterion
A nonlocal holonomic vortex is present whenever a closed spacetime loop around the local attractor satisfies
\[
\Gamma[\mathcal C] \neq 0.
\]
The object is nonlocal because the loop need not lie on a single time slice.

## Result
The holonomic circulation criterion for a spacetime loop is gauge/global-phase invariant and supplies the minimal criterion for a nonlocal holonomic vortex.
