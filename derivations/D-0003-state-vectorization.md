# D-0003 State / Phase Vectorization (Strict Derivation)

Status: draft-strict

## Dependencies
- DEF-0004 state

## Goal
Construct a deterministic finite real vectorization of the minimal projective two-level state without using Fourier decomposition.

## Step 1 — State representative
Let the normalized state representative be

ψ = (a, b)^T ∈ C^2

with normalization

|a|^2 + |b|^2 = 1.

Projective equivalence identifies

ψ ~ e^{iα} ψ.

## Step 2 — Outer-product invariance
Define the rank-one projector

ρ = |ψ><ψ|

Then ρ is invariant under

ψ -> e^{iα} ψ.

Hence any function of ρ is gauge-invariant with respect to global phase.

## Step 3 — Pauli expectation coordinates
Let σ_x, σ_y, σ_z be the Pauli matrices.
Define

n_i = Tr(ρ σ_i),   i ∈ {x,y,z}.

Explicitly,

n_x = 2 Re(a* conj(b))

n_y = 2 Im(a* conj(b))

n_z = |a|^2 - |b|^2

## Step 4 — Unit-sphere property
For a normalized pure state,

n_x^2 + n_y^2 + n_z^2 = 1.

Thus the vector

n = (n_x, n_y, n_z)

lies on S^2 and gives the Bloch representation of the projective state.

## Step 5 — Angular chart
For n on S^2, define

theta = arccos(n_z)

phi = atan2(n_y, n_x)

with chart caveat at the poles.

## Step 6 — Deterministic vectorization map
Define the vectorization operator

G(ψ) = (n_x, n_y, n_z)

and optional chart extraction

G_ang(ψ) = (theta, phi)

## Step 7 — No Fourier rule
No Fourier or modal decomposition is introduced at this stage because no justified discretization or basis expansion has yet been declared.

## Step 8 — Output
Return
- Bloch vector n
- optional chart (theta, phi)
- metadata for chart singularity handling if needed

## Notes
- The Bloch vector is the primary canonical finite vectorization.
- Angular extraction is downstream of the Bloch vector, not the source of truth.
- Phase-channel extraction for closure remains a separate downstream operator.
