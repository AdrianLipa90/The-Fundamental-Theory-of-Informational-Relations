# DEF-0015 — Object-state energy functional

## Status
`hypothesis`

## Depends on
- `DEF-0012`
- `DEF-0014`

## Objects defined here
1. `OBJ-OBJECT-STATE-0001`
2. `OBJ-RAW-ENERGY-FUNCTIONAL-0001`
3. `OBJ-NORMALIZED-ENERGY-AMPLITUDE-0001`
4. `OBJ-OBJECT-PHASE-0001`
5. `OBJ-OBJECT-SEED-TOPOLOGICAL-0001`

## Object state
Each canonical repository object is described by the state tuple
\[
\mathcal F_i=(\rho_i,\; p_i,\; w_i,\; \nu_i,\; A_i,\; \vec s_i,\; \chi_i,\; \mathcal N_i).
\]
Here:
- \(\rho_i\): information density,
- \(p_i\): relational pressure,
- \(w_i\): ontological weight,
- \(\nu_i\): activation/change frequency,
- \(A_i\): normalized amplitude,
- \(\vec s_i\): state vector,
- \(\chi_i\): quality character/class,
- \(\mathcal N_i\): nonlocal neighborhood data.

## Raw energy functional
Define the raw object energy by
\[
E_i^{raw}=F(\rho_i,p_i,w_i,\nu_i,\vec s_i,\chi_i,\mathcal N_i).
\]
The first canonical linear ansatz is
\[
E_i^{raw}=\alpha_1\rho_i+\alpha_2 p_i+\alpha_3 w_i+\alpha_4\nu_i+\alpha_5\|\vec s_i\|_2+\alpha_6\delta(\chi_i)+\alpha_7\|\mathcal N_i\|,
\]
with nonnegative coefficients \(\alpha_k\ge 0\).

## Natural normalization
Define the normalized energy by
\[
\widetilde E_i = \frac{E_i^{raw}}{\sum_j E_j^{raw}},
\qquad
\sum_i \widetilde E_i = 1.
\]
Then define the object amplitude
\[
A_i = \sqrt{\widetilde E_i},
\qquad
\sum_i A_i^2 = 1.
\]

## Object phase and local state
Let the topological seed be
\[
s_i = H(\text{content}_i,\text{path}_i,\rho_i,p_i,w_i,\nu_i,\vec s_i,\chi_i,\mathcal N_i).
\]
Map it to phase via
\[
\phi_i = 2\pi\,\mathrm{frac}(g(s_i)).
\]
Then the local state is
\[
\psi_i = A_i e^{i\phi_i}.
\]

## Canonical role
This object is the first explicit energetic state model for repository objects. It upgrades seeds from local identifiers to topological state signatures coupled to normalization, amplitude, and phase.

## Scope restriction
This module defines the first canonical ansatz only. It does not yet fix the calibrated form of \(F\), the final state-vector basis, or the definitive classification map for \(\chi_i\).
