# D-0014 — Normalized object state from raw energy

## Status
`hypothesis`

## Depends on
- `DEF-0015`

## Goal
Construct normalized amplitudes, phases, and local object states from raw repository-object energy.

## Step 1 — Raw energy inputs
For each object \(i\), evaluate the raw energy functional
\[
E_i^{raw}=F(\rho_i,p_i,w_i,\nu_i,\vec s_i,\chi_i,\mathcal N_i).
\]
In the first linear ansatz,
\[
E_i^{raw}=\alpha_1\rho_i+\alpha_2 p_i+\alpha_3 w_i+\alpha_4\nu_i+\alpha_5\|\vec s_i\|_2+\alpha_6\delta(\chi_i)+\alpha_7\|\mathcal N_i\|.
\]

## Step 2 — Normalized energy
Normalize across the full object ensemble:
\[
\widetilde E_i = \frac{E_i^{raw}}{\sum_j E_j^{raw}}.
\]
Hence
\[
\sum_i \widetilde E_i = 1.
\]

## Step 3 — Amplitude
Define the amplitude by
\[
A_i=\sqrt{\widetilde E_i},
\]
so that
\[
\sum_i A_i^2 = 1.
\]

## Step 4 — Phase from topological seed
Let the seed be
\[
s_i = H(\text{content}_i,\text{path}_i,\rho_i,p_i,w_i,\nu_i,\vec s_i,\chi_i,\mathcal N_i),
\]
then map it to phase:
\[
\phi_i = 2\pi\,\mathrm{frac}(g(s_i)).
\]

## Step 5 — Local state
The resulting local object state is
\[
\psi_i=A_i e^{i\phi_i}.
\]
The full repository-object state is then
\[
\Psi=(\psi_1,\psi_2,\dots,\psi_N),
\qquad
\sum_i |\psi_i|^2=1.
\]

## Registered toy trace
For the registered toy objects with raw energies
\[
E^{raw}=(2.0,3.0,5.0),
\]
we obtain
\[
\widetilde E=(0.2,0.3,0.5),
\qquad
A\approx (0.44721360,0.54772256,0.70710678).
\]
For phases generated from registered toy seeds,
\[
\phi\approx(5.37242597,\ 0.80247601,\ 5.95338902).
\]
Thus
\[
\psi_1\approx 0.27508520-0.35261961i,
\quad
\psi_2\approx 0.38061860+0.39380677i,
\quad
\psi_3\approx 0.66950784-0.22861838i.
\]

## Result
The object-state layer is the normalized energetic state
\[
E_i^{raw}\to \widetilde E_i \to A_i,\phi_i \to \psi_i.
\]

## Scope restriction
This derivation closes the first normalization pipeline only. It does not yet identify calibrated object flavors/colors or the final learned energy coefficients.
