# WP-MOD — Tau from coupling via a Laplacian generator

## Status
`defined`

## Scope
This whitepaper records the first explicit non-fit candidate generator of \(\tau_i\) from pairwise coupling data \(A_{ij}\).

## 1. Theory chapter
### 1.1 Pairwise kernel
A symmetric nonnegative pairwise coupling kernel \(A_{ij}\) is introduced as the first explicit summary of relational coupling strength.

### 1.2 Laplacian generator
From \(A_{ij}\) one constructs the weighted graph Laplacian
\[
L_A = D-A,
\qquad d_i = \sum_j A_{ij}.
\]

### 1.3 Logarithmic tau variables
To guarantee positivity, one sets \(\xi_i = \ln\tau_i\) and solves the gauge-fixed linear system
\[
L_A\xi = \kappa(d-\bar d\,\mathbf 1),
\qquad \sum_i \xi_i = 0.
\]

### 1.4 Pseudoinverse solution
The resulting candidate generator is
\[
\tau_i = \tau_*\exp\!\Big(\kappa [L_A^+(d-\bar d\,\mathbf 1)]_i\Big),
\]
using the Moore--Penrose pseudoinverse \cite{penrose1955generalizedinverse}. Graph-Laplacian context is anchored in weighted spectral graph theory \cite{chung1997spectralgraph,fiedler1973algebraicconnectivity}.

## 2. Source files
- `definitions/DEF-0008-pairwise-coupling-kernel.md`
- `derivations/D-0007-tau-from-coupling-laplacian.md`
- `interfaces/IF-0006-tau-from-coupling.yaml`

## 3. Code bindings
- `src/ciel_foundations/solvers/tau_from_coupling_solver.py`
- `tests/test_tau_from_coupling.py`
- `Simulations/code/sim_tau_from_coupling.py`

## 4. Epistemic note
This module is a registered hypothesis, not yet a final derived microphysical law for \(\tau_i\).
