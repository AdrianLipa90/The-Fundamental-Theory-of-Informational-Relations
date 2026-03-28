# D-0013 — Spectral tau from effective White-Thread

## Status
`hypothesis`

## Depends on
- `DEF-0011`
- `DEF-0014`

## Goal
Construct a real symmetric coupling operator from effective White-Thread amplitudes and define tau modes as its spectrum.

## Step 1 — Effective transport input
Take the effective amplitudes \(W^{eff}_{ij}\). These are generally complex and encode transported phase information.

## Step 2 — Hermitian projection
Define
\[
A_{ij}=\frac{1}{2}\left(W^{eff}_{ij}+\overline{W^{eff}_{ji}}\right).
\]
This ensures that \(A\) is Hermitian. In the real symmetric toy sector it reduces to the real part of the effective transport.

## Step 3 — Global coupling matrix
Assemble the matrix
\[
A=\begin{pmatrix}
0 & A_{12} & A_{13}\\
A_{21} & 0 & A_{23}\\
A_{31} & A_{32} & 0
\end{pmatrix}
\]
with \(A_{ij}=A_{ji}\).

## Step 4 — Spectral modes
Define the tau modes by the eigenvalue problem
\[
A v_i = \tau_i v_i.
\]
Thus
\[
\tau_i = \lambda_i(A).
\]

## Step 5 — Registered toy polynomial
For the registered toy couplings
\[
A_{12}=0.74224129,\qquad A_{13}=0.5,\qquad A_{23}=0.3,
\]
the characteristic polynomial becomes
\[
-\lambda^3 + 0.8909211506872641\lambda + 0.222672387 = 0.
\]
Its numerical roots are
\[
\tau \approx (0.99893394,\ -0.60734102,\ -0.39159292).
\]

## Result
The first spectral bridge is therefore
\[
W^{eff}_{ij} \to A_{ij} \to \tau_i,
\]
with \(A\) built as the Hermitian projection of effective White-Thread transport and \(\tau_i\) obtained as spectral modes of the resulting coupling matrix.

## Scope restriction
This derivation does not yet identify flavor/color labels or a calibrated map from \(\tau_i\) to physical masses.
