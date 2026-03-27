# D-0004 — Local attractor axis, poles/equator, and Coriolis term

## Status
`derived`

## Depends on
- `AX-0005`
- `DEF-0005`
- `DEF-0006`

## Goal
Derive the local axis/poles/equator structure from a rotating local attractor neighborhood and recover the standard Coriolis-like term in the rotating frame.

## Step 1 — Local attractor and angular velocity
Take a bounded object \(O_i\) with local attractor \(A_i\) and a nonzero local angular-velocity vector \(\Omega_i\neq 0\).

## Step 2 — Distinguished axis
Normalize the angular-velocity vector:
\[
n_i = \frac{\Omega_i}{\|\Omega_i\|}.
\]
This defines a distinguished axis in the local auxiliary sphere.

## Step 3 — Poles and equator
The local poles are
\[
P_i^{\pm} = \pm n_i,
\]
and the equator is the orthogonal great circle
\[
E_i = \{x\in S^2 : x\cdot n_i = 0\}.
\]
Thus a nonzero local rotational axis implies poles and equator.

## Step 4 — Coriolis term
For a spatial local flow velocity \(u_i\) observed in the rotating frame with angular velocity \(\Omega_i\), standard rotating-frame kinematics yields
\[
F_{C,i} = -2\,\Omega_i \times u_i.
\]
If the spatial phase flow is represented by the spatial part of \(u^{(i)}_\mu\), the same term enters the effective hydrodynamic equation.

## Result
Local attractor + nonzero local rotation implies:
1. a distinguished axis,
2. poles and equator,
3. a Coriolis-like term in the rotating local flow.

## Scope restriction
This derivation establishes local rotating-flow structure. It does not yet derive a full white-thread or tau-from-coupling layer.
