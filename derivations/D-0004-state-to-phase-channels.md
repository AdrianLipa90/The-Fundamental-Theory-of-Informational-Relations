# D-0004 State to Phase Channels (Strict Derivation)

Status: draft-strict

## Dependencies
- D-0002 closure operator
- D-0003 state vectorization
- DEF-0004 state
- DEF-0009 closure

## Goal
Construct a deterministic minimal channel-extraction operator that maps a projective two-level state to a finite angular channel vector suitable for the minimal closure operator.

## Step 1 — Projective input
Let

ψ = (a, b)^T ∈ C^2,   |a|^2 + |b|^2 = 1

with projective equivalence

ψ ~ e^{iα} ψ.

## Step 2 — Bloch vectorization
From D-0003 define

n = (n_x, n_y, n_z)

with

n_x = 2 Re(a conj(b))

n_y = 2 Im(a conj(b))

n_z = |a|^2 - |b|^2

and

n_x^2 + n_y^2 + n_z^2 = 1.

## Step 3 — Angular chart extraction
Define the Bloch chart coordinates

theta = arccos(n_z)

phi = atan2(n_y, n_x)

with the standard pole caveat when |n_z| = 1.

## Step 4 — Minimal channel set
Define the minimal finite channel vector

Γ(ψ) = (γ_1, γ_2)

by

γ_1 = theta

gamma_2 = phi

That is,

Γ(ψ) = (theta, phi).

## Step 5 — Determinism and gauge invariance
Because θ and φ are extracted from the Bloch vector n, and n is invariant under the global phase transformation ψ -> e^{iα} ψ, the extracted channel vector Γ(ψ) is gauge-invariant up to the standard chart convention at the poles.

## Step 6 — Closure bridge
The closure operator of D-0002 acts on the finite channel set:

C_H(Γ(ψ))

Thus, at this minimal level,

the state-dependent closure defect is

C_H(ψ) := C_H(Γ(ψ)).

## Step 7 — Pole handling
At the poles, φ is not structurally determined by the state.
Therefore define the convention:

if |n_z| = 1, set phi = 0 and record pole_chart = True.

This does not alter the Bloch vector and maintains deterministic output.

## Step 8 — Output
Return
- channel vector Γ(ψ) = (theta, phi)
- pole metadata
- closure-ready representation

## Notes
- No Fourier decomposition is used.
- No white-thread terms are included.
- This is the minimal state-to-closure bridge for CP^1.
