# D-0008 — Kernel composition from holonomy, phase alignment, and closure

## Status
`hypothesis`

## Depends on
- `DEF-0002`
- `DEF-0003`
- `DEF-0008`
- `DEF-0009`

## Goal
Show that a phase-aware pairwise kernel built from holonomy magnitude, phase alignment, and closure defect is positive, symmetric, and compatible with the tau-from-coupling generator.

## Step 1 — Holonomy magnitude
Take the nonnegative pairwise magnitude
\[
|W_{ij}|\ge 0.
\]
This supplies the basic pairwise coupling amplitude.

## Step 2 — Phase alignment
Define
\[
g_{\mathrm{phase}}(\delta\gamma_{ij};\lambda)
=
\exp\!\big[-\lambda(1-\cos\delta\gamma_{ij})\big].
\]
Because \(\cos(\gamma_i-\gamma_j)=\cos(\gamma_j-\gamma_i)\), this factor is symmetric under exchange of indices.

## Step 3 — Closure weight
Define
\[
g_{\mathrm{closure}}(R_H;\mu)=\exp(-\mu R_H).
\]
Since \(R_H\ge 0\), the weight is positive and decreases monotonically as closure defect grows.

## Step 4 — Product kernel
Form the product
\[
A_{ij}=|W_{ij}|\,g_{\mathrm{phase}}(\delta\gamma_{ij};\lambda)\,g_{\mathrm{closure}}(R_H;\mu).
\]
Each factor is nonnegative; the phase factor is symmetric and the closure factor is scalar. Therefore the resulting kernel is nonnegative and symmetric whenever \(|W_{ij}|=|W_{ji}|\).

## Step 5 — Compatibility with tau generator
Since the tau-from-coupling hypothesis in `D-0007` requires a symmetric nonnegative kernel as input, the product kernel above is admissible as a candidate upstream constructor of \(A_{ij}\).

## Result
The composition
\[
A_{ij}=|W_{ij}|\,g_{\mathrm{phase}}\,g_{\mathrm{closure}}
\]
is a coherent first hypothesis for converting already-registered piko objects into a kernel suitable for the \(\tau_i=f(A_{ij})\) generator.
