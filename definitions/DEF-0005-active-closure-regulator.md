# DEF-0005 — Active closure regulator

## Status
`defined`

## Depends on
- `DEF-0003`
- `ASM-0001`

## Object defined here
- `OBJ-ACTIVE-CLOSURE-0001`

## Definition
Given the closure defect
\[
\Delta_H = \sum_k e^{i\phi_k},
\qquad
R_H = |\Delta_H|^2,
\]
define a thresholded active closure regulator
\[
\mathcal C_{\rho_c}(\{\phi_k\}) =
\begin{cases}
\mathrm{accept} & R_H \le \rho_c, \\
\mathrm{rollback} & R_H > \rho_c.
\end{cases}
\]

## Meaning
This turns the closure functional into an active admissibility regulator for minimal executable dynamics.

## Scope restriction
This is a toy executable regulator only. It does not yet claim the final foundational form of the closure law.
