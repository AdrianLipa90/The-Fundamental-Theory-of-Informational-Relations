# DEF-0008 — Pairwise coupling kernel and tau-from-coupling generator

## Status
`defined` for the kernel, `hypothesis` for the tau generator

## Depends on
- `DEF-0002`
- `DEF-0003`

## Objects defined here
1. `OBJ-PAIRWISE-KERNEL-0001`
2. `OBJ-TAU-FROM-COUPLING-0001`

## Pairwise coupling kernel
For a finite family of relational cycles indexed by \(i,j\), define a symmetric nonnegative pairwise kernel
\[
A_{ij}=A_{ji}\ge 0,
\qquad
A_{ii}=0.
\]
A minimal toy realization may use
\[
A_{ij}=|W_{ij}|,
\]
while a phase-aware realization may be written schematically as
\[
A_{ij}=|W_{ij}|\,g(\gamma_i-\gamma_j,\Delta_H).
\]
The canonical role of \(A_{ij}\) is to summarize pairwise coupling strength without yet committing to a unique microphysical law.

## Graph objects
Define the row-sum strength and diagonal matrix
\[
d_i = \sum_j A_{ij},
\qquad
D = \operatorname{diag}(d_1,\dots,d_N).
\]
Define the graph Laplacian
\[
L_A = D-A.
\]

## Tau-from-coupling hypothesis
Let
\[
\xi_i = \ln \tau_i.
\]
The proposed generator is the constrained Laplacian system
\[
L_A\,\xi = \kappa(d-\bar d\,\mathbf 1),
\qquad
\bar d = \frac1N\sum_i d_i,
\qquad
\sum_i \xi_i = 0.
\]
Equivalently,
\[
\xi = \kappa L_A^{+}(d-\bar d\,\mathbf 1),
\]
with \(L_A^+\) the Moore--Penrose pseudoinverse \cite{penrose1955generalizedinverse}. Therefore
\[
\tau_i = \tau_*\exp\!\Big(\kappa\,[L_A^+(d-\bar d\,\mathbf 1)]_i\Big).
\]

## Canonical role
This object is the first explicit non-fit candidate generator of \(\tau_i\) from pairwise coupling data.

## Scope restriction
This definition does not yet prove that the Laplacian generator is the unique or final microphysical law for \(\tau_i\). It registers a concrete, testable hypothesis that can replace direct fitting as the first generator candidate.
