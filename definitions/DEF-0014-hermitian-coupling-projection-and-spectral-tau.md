# DEF-0014 — Hermitian coupling projection and spectral tau modes

## Status
`hypothesis`

## Depends on
- `DEF-0011`
- `DEF-0012`

## Objects defined here
1. `OBJ-HERMITIAN-COUPLING-PROJECTION-0001`
2. `OBJ-SPECTRAL-TAU-MODES-0001`

## Hermitian coupling projection
Given effective White-Thread amplitudes \(W^{eff}_{ij}\in\mathbb C\), define the Hermitian pairwise coupling projection
\[
A_{ij} = \frac{1}{2}\left(W^{eff}_{ij}+\overline{W^{eff}_{ji}}\right).
\]
In the symmetric toy sector with \(W^{eff}_{ji}=\overline{W^{eff}_{ij}}\), this reduces to
\[
A_{ij}=\Re(W^{eff}_{ij}).
\]

## Spectral tau modes
Given a real symmetric coupling matrix \(A\), define the spectral tau modes by
\[
\tau_i = \lambda_i(A),
\]
where \(\lambda_i\) are the eigenvalues of \(A\).

## Canonical role
This object is the first explicit bridge from effective White-Thread transport to a global coupling operator and then to spectral relational timescales.

## Registered numeric trace
For the registered effective White-Thread toy value
\[
W^{eff}_{12}\approx 0.74224129 + 0.12412309 i,
\]
the Hermitian projection gives
\[
A_{12}=\Re(W^{eff}_{12})\approx 0.74224129.
\]
For the registered symmetric toy matrix
\[
A=\begin{pmatrix}
0 & 0.74224129 & 0.5\\
0.74224129 & 0 & 0.3\\
0.5 & 0.3 & 0
\end{pmatrix},
\]
the characteristic polynomial is
\[
-\lambda^3 + 0.8909211506872641\lambda + 0.222672387 = 0,
\]
with spectral tau modes
\[
\tau \approx (0.99893394,\ -0.60734102,\ -0.39159292).
\]

## Executable bindings
- solver: `src/ciel_foundations/solvers/spectral_tau_from_white_thread_solver.py`
- simulation: `Simulations/code/sim_spectral_tau_from_white_thread.py`
- section: `LaTeX/sections/SEC-0011-spectral-tau-from-white-thread.tex`
- appendix: `LaTeX/appendices/APP-0009-spectral-tau-from-white-thread.tex`

## Artifact bindings
- result: `Simulations/results/ART-0008-spectral-tau-from-white-thread-demo.csv`
- provenance: `provenance/ART-0008-provenance.yaml`
- falsification: `falsification/FM-0008-spectral-tau-from-white-thread.yaml`

## Scope restriction
This module closes only the first spectral bridge from effective transport to relational timescales. It does not yet identify physical flavor/color sectors or calibrated fermion masses.
