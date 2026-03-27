# ASM-0001 — Thresholded active closure toy model

## Status
`explicit`

## Scope
Active closure regulator for the minimal CP1/Berry/spin layer.

## Assumption
For the minimal executable layer, admissibility is tested through the closure magnitude
\[
R_H = |\Delta_H|^2
\]
with a finite threshold \(\rho_c\).

Accepted states satisfy
\[
R_H \le \rho_c,
\]
and rejected states satisfy
\[
R_H > \rho_c.
\]

## Why this is an assumption
The repository has not yet frozen whether exact closure \(\Delta_H=0\) or nonzero residual defect is the final foundational law. Therefore the thresholded regulator is a toy executable assumption, not the final canonical closure theorem.
