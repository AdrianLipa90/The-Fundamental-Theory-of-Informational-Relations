# D-0006 Minimal Dynamics / Update Step (Strict Derivation)

Status: draft-strict

## Dependencies
- D-0002 closure operator
- D-0005 admissibility / correction logic
- DEF-0009 closure

## Goal
Define a deterministic one-step update operator acting on the minimal channel vector Γ = (γ_1, γ_2).

## Step 1 — State and increment
Let

Γ_n = (γ_1, γ_2)

be the current channel state.
Let

V_n = (ν_1, ν_2)

be the declared increment vector.
Let dt > 0.

## Step 2 — Proposed step
Define the proposed update

Γ_prop = Γ_n + dt V_n

with angles interpreted modulo 2π.

## Step 3 — Closure evaluation
Compute

C_in = C_H(Γ_n)

C_prop = C_H(Γ_prop)

using D-0002.

## Step 4 — Acceptance modes
Define three minimal modes.

### Mode A — accept_if_nonworsening
Accept Γ_prop if

C_prop ≤ C_in

otherwise rollback to Γ_n.

### Mode B — rollback
Accept Γ_prop only if

C_prop ≤ ε_C

otherwise rollback to Γ_n.

### Mode C — correct
Accept Γ_prop if admissible.
If not admissible, apply correction logic from D-0005 to Γ_prop.

## Step 5 — Update operator
Define the update operator U by

Γ_{n+1} = U(Γ_n, V_n, dt; mode, ε_C)

where
- in Mode A: Γ_{n+1} = Γ_prop if C_prop ≤ C_in, else Γ_n
- in Mode B: Γ_{n+1} = Γ_prop if C_prop ≤ ε_C, else Γ_n
- in Mode C: Γ_{n+1} = Γ_prop if C_prop ≤ ε_C, else A_C(Γ_prop; ε_C, correct)

## Step 6 — Monotonicity under rollback-enabled logic
For Mode A and Mode B, rollback guarantees

C_H(Γ_{n+1}) ≤ max(C_in, ε_C)

and specifically in Mode A,

C_H(Γ_{n+1}) ≤ C_in.

## Step 7 — Determinism
For fixed inputs

(Γ_n, V_n, dt, mode, ε_C)

the output Γ_{n+1} is unique.

## Notes
- This is the minimal deterministic step law.
- It does not yet include a generator derived from Hamiltonian, Berry curvature, or white-thread coupling.
- It is intended as the first admissibility-aware dynamical shell for the CP^1 foundations layer.
