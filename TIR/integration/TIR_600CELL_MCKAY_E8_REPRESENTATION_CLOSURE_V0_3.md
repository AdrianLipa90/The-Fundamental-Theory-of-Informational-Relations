# TIR 600-cell / 2I McKay–E8 representation closure v0.3

Status: `CANDIDATE_ONLY`  
Physical binding: `OPEN`  
Runtime default: `OFF`  
Canon write authority: `FALSE`

## Scope

This note records an exact representation-theoretic explanation of the finite-rank pattern already observed numerically for sampled scalar harmonics on the 600-cell. It does **not** promote the 600-cell to a physical electron carrier, a Kaluza–Klein compactification, an event horizon, or an E8 gauge-unification model.

The geometric input is

\[
S^3\simeq SU(2),\qquad V_\ell=\operatorname{Sym}^{\ell}(\mathbb C^2),\qquad \dim V_\ell=\ell+1,
\]

with scalar harmonic multiplicity

\[
\dim\mathcal H_\ell(S^3)=(\ell+1)^2,
\qquad -\Delta_{S^3}=\ell(\ell+2).
\]

The 120 vertices of the 600-cell are used as the binary icosahedral group `2I` inside `SU(2)`. Restricting `V_ell` to `2I` is governed by the affine-E8 McKay graph.

## Stable irrep identifiers

Prime labels for the two 2D, 3D and 4D irreducibles vary between references. The executable validator therefore uses stable local IDs rather than treating any prime convention as canonical:

| local id | dimension |
|---|---:|
| `rho1` | 1 |
| `rho2a` | 2 |
| `rho3a` | 3 |
| `rho4a` | 4 |
| `rho5` | 5 |
| `rho6` | 6 |
| `rho4b` | 4 |
| `rho3b` | 3 |
| `rho2b` | 2 |

The McKay adjacency used by the validator is

```text
rho1 -- rho2a -- rho3a -- rho4a -- rho5 -- rho6 -- rho4b -- rho2b
                                                  |
                                                rho3b
```

and obeys the dimension balance at every vertex

\[
2d_\rho=\sum_{\sigma\sim\rho}d_\sigma.
\]

## Exact recurrence

Let `Q = rho2a` be the fundamental doublet. The `SU(2)` Clebsch–Gordan recurrence becomes, after restriction to `2I`,

\[
V_{\ell+1}=Q\otimes V_\ell-V_{\ell-1},
\qquad V_0=\rho_1,\quad V_1=\rho_{2a}.
\]

The executable validator performs representation-ring subtraction fail-closed; it never uses `Counter.__sub__`, because silent removal of negative multiplicities would hide an invalid recurrence.

The resulting low sectors are

\[
\begin{aligned}
V_0&=\rho_1,\\
V_1&=\rho_{2a},\\
V_2&=\rho_{3a},\\
V_3&=\rho_{4a},\\
V_4&=\rho_5,\\
V_5&=\rho_6,\\
V_6&=\rho_{4b}\oplus\rho_{3b},\\
V_7&=\rho_6\oplus\rho_{2b}.
\end{aligned}
\]

Thus `ell=6` is the first reducible restriction. This is a precise representation-theory statement; the project label `finite-resolution branching threshold` is permitted, whereas a physical event-horizon interpretation remains unvalidated.

## Coefficient-space ranks

For finite-group matrix coefficients, an irrep type `rho` contributes `dim(rho)^2` to the sampled coefficient space once it occurs. Therefore

\[
R_\ell=\sum_{\rho\subset V_\ell|_{2I}} d_\rho^2.
\]

For `ell=0..7` this gives

\[
(1,4,9,16,25,36,25,40).
\]

In particular,

\[
R_6=4^2+3^2=25,
\]

which exactly explains the independently computed numerical sampled-harmonic rank 25 at `ell=6`, rather than the continuum dimension 49.

Likewise,

\[
R_7=6^2+2^2=40,
\]

matching the independently computed numerical rank 40 at `ell=7`, rather than continuum dimension 64.

## Finite closure at ell=7

The cumulative rank is obtained from the union of irrep types encountered up to each level, so previously seen blocks are not counted twice. The sequence is

\[
(1,5,14,30,55,91,116,120).
\]

At `ell=7`, the `rho6` block was already present at `ell=5`; only the new terminal `rho2b` contributes

\[
2^2=4,
\]

so

\[
116+4=120.
\]

This is the regular/group-algebra closure

\[
\mathbb C[2I]\simeq\bigoplus_{\rho\in\widehat{2I}}\operatorname{End}(V_\rho),
\]

with

\[
|2I|=\sum_\rho d_\rho^2
=1^2+2^2+3^2+4^2+5^2+6^2+4^2+3^2+2^2
=120.
\]

Therefore the safe exact project statements are:

- `ell=6`: first irreducibility-breaking / finite-resolution branching threshold;
- `ell=7`: finite representation closure of the 120-dimensional `C[2I]` carrier.

## Relation to previous validators

This file complements, rather than replaces, `TIR/validation/tir_600cell_s3_rank_closure_candidate_v0_2.py`. That validator independently measures the sampled harmonic ranks from the 600-cell point set. The v0.3 validator derives the same `ell=6` and `ell=7` ranks from the finite-group representation ring. Agreement between these independent routes is the relevant closure test.

## Epistemic boundary

Exact within mathematics / representation theory:

- `S^3 ≅ SU(2)` harmonic representation dimensions;
- the `2I` McKay graph and recurrence encoded by the validator;
- the low-level branching sequence above;
- coefficient ranks 25 and 40 at `ell=6,7`;
- cumulative closure at 120 and the group-algebra sum-of-squares identity.

Still candidate / not promoted to physical fact:

- identification with physical electron orbitals;
- nonlinear soliton dynamics;
- physical compactification or Kaluza–Klein interpretation;
- an E8 physical-unification claim;
- any literal event-horizon/fractal-layer interpretation.
