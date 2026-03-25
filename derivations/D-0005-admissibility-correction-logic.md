# D-0005 Admissibility / Correction Logic (Strict Derivation)

Status: draft-strict

## Dependencies
- D-0002 closure operator
- D-0004 state-to-phase-channels
- DEF-0009 closure

## Goal
Define a deterministic admissibility and correction rule acting on the minimal channel vector Γ = (γ_1, γ_2).

## Step 1 — Closure input
Let

Γ = (γ_1, γ_2)

and compute

Δ_H(Γ) = exp(i γ_1) + exp(i γ_2)

R_H(Γ) = |Δ_H(Γ)|^2 / 4

C_H(Γ) = 1 - R_H(Γ)

## Step 2 — Admissibility threshold
Fix tolerance ε_C ≥ 0.

Admissible if

C_H(Γ) ≤ ε_C

## Step 3 — Cases
Case A: admissible

If C_H(Γ) ≤ ε_C, return Γ unchanged.

Case B: non-admissible

If C_H(Γ) > ε_C, apply either reject or correction logic.

## Step 4 — Minimal deterministic correction manifold
At the minimal CP^1 layer, define the coherent diagonal manifold

M_diag = { (γ, γ) : γ ∈ ℝ mod 2π }

This is the set of perfectly coherent two-channel states under the minimal closure operator.

## Step 5 — Reference phase
For a non-admissible Γ = (γ_1, γ_2), define the phasor sum

Δ_H = exp(i γ_1) + exp(i γ_2)

If |Δ_H| > 0, define the reference phase

gamma_ref = arg(Δ_H)

If |Δ_H| = 0 (anti-phase degeneracy), define the deterministic fallback

gamma_ref = γ_1

## Step 6 — Projection correction
Define corrected channels

Π_corr(Γ) = (gamma_ref, gamma_ref)

Then

C_H(Π_corr(Γ)) = 0

## Step 7 — Decision function
Define the admissibility / correction operator A_C by

A_C(Γ; ε_C, mode) =
- Γ, if C_H(Γ) ≤ ε_C
- reject, if C_H(Γ) > ε_C and mode = reject
- Π_corr(Γ), if C_H(Γ) > ε_C and mode = correct

## Step 8 — Monotonicity
For mode = correct,

C_H(A_C(Γ; ε_C, correct)) ≤ C_H(Γ)

and under the chosen projection rule,

C_H(A_C(Γ; ε_C, correct)) = 0

## Notes
- This is the minimal deterministic correction rule.
- It does not claim physical uniqueness beyond the current foundational layer.
- Higher-dimensional or white-thread-aware correction rules belong to later derivations.
