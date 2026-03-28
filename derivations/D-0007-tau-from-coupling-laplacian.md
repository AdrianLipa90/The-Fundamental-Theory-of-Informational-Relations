# D-0007 — Tau from coupling via a Laplacian generator

## Status
`hypothesis`

## Depends on
- `DEF-0008`

## Goal
Derive a positive relational generator for \(\tau_i\) from pairwise coupling data \(A_{ij}\) without taking fitted \(\tau_i\) values as primary input.

## Step 1 — Pairwise kernel and strengths
Given a symmetric nonnegative kernel \(A_{ij}\), define
\[
d_i = \sum_j A_{ij},
\qquad
D = \operatorname{diag}(d_1,\dots,d_N),
\qquad
L_A = D-A.
\]
This is the standard graph Laplacian construction in weighted form \cite{chung1997spectralgraph,fiedler1973algebraicconnectivity}.

## Step 2 — Logarithmic tau variables
To guarantee positivity of \(\tau_i\), write
\[
\xi_i = \ln \tau_i.
\]
Then any real solution \(\xi_i\) yields \(\tau_i>0\).

## Step 3 — Variational functional
Consider the energy functional
\[
\mathcal E[\xi]
=
\frac12\sum_{i,j} A_{ij}(\xi_i-\xi_j)^2
-
\kappa\sum_i(d_i-\bar d)\xi_i,
\qquad
\bar d = \frac1N\sum_i d_i,
\]
with gauge constraint
\[
\sum_i \xi_i = 0.
\]

## Step 4 — Stationary condition
Taking the variation with respect to \(\xi_i\) gives
\[
\sum_j A_{ij}(\xi_i-\xi_j)=\kappa(d_i-\bar d).
\]
In matrix form this is
\[
L_A\xi = \kappa(d-\bar d\,\mathbf 1).
\]

## Step 5 — Pseudoinverse solution
Since the Laplacian has a null direction along the constant vector, impose the gauge constraint and solve with the Moore--Penrose pseudoinverse \cite{penrose1955generalizedinverse}:
\[
\xi = \kappa L_A^{+}(d-\bar d\,\mathbf 1).
\]
Hence
\[
\tau_i = \tau_*\exp\!\Big(\kappa\,[L_A^+(d-\bar d\,\mathbf 1)]_i\Big).
\]

## Result
This yields a relational, positive, non-fit candidate generator
\[
\tau_i = f(A_{ij})
\]
with explicit dependence on the pairwise coupling kernel through its Laplacian geometry.

## Scope restriction
This derivation establishes a concrete candidate generator. It does not prove uniqueness, nor does it yet fix the final microphysical form of \(A_{ij}\).
