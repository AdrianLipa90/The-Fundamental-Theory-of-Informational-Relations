# DEF-0006 — Nonlocal holonomic vortex in spacetime

## Status
`defined`

## Depends on
- `DEF-0002`
- `DEF-0003`
- `DEF-0005`

## Objects defined here
1. `OBJ-NONLOCAL-HOLO-VORTEX-0001`
2. `OBJ-CORIOLIS-0001`

## Effective phase-flow one-form
For the local order parameter around \(A_i\), define the effective phase-flow one-form
\[
u^{(i)}_\mu = \partial_\mu \theta_i - A^{(i)}_\mu,
\]
where \(A^{(i)}_\mu\) is the connection/transport sector associated with the local phase flow.

## Spacetime circulation
For a closed spacetime loop \(\mathcal C\), define the holonomic circulation
\[
\Gamma_i[\mathcal C] = \oint_{\mathcal C} u^{(i)}_\mu\,dx^\mu.
\]

## Nonlocal holonomic vortex
A nonlocal holonomic vortex is a closed spacetime-loop configuration around \(A_i\) for which
\[
\Gamma_i[\mathcal C] \neq 0.
\]
It is called nonlocal because the loop is not restricted to a single spatial slice.

## Coriolis-like term
For the spatial part \(u_i\) of the effective flow in a frame rotating with angular velocity \(\Omega_i\), define the Coriolis-like term
\[
F_{C,i} = -2\,\Omega_i \times u_i.
\]

## Canonical role
This object captures rotating spacetime phase flow around a local attractor while preserving the earlier projective, Berry, and closure structure.
