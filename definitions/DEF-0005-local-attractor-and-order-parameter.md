# DEF-0005 — Local attractor and rotating order parameter

## Status
`defined`

## Depends on
- `AX-0002`
- `AX-0005`

## Objects defined here
1. `OBJ-LOCAL-ATTRACTOR-0001`
2. `OBJ-ORDER-PARAMETER-0001`
3. `OBJ-POLES-EQUATOR-0001`

## Local attractor
For each bounded or stabilized object \(O_i\), define a local attractor \(A_i\) together with a neighborhood \(U_i\) in which local relational flow is organized.

## Order parameter
On \(U_i\), define a complex order parameter
\[
\Psi_i(x) = \sqrt{\rho_i(x)}\,e^{i\theta_i(x)}.
\]
Here \(\rho_i\) is an effective local density and \(\theta_i\) is a phase field.

## Local axis, poles, and equator
If the local flow carries a nonzero angular-velocity vector \(\Omega_i \neq 0\), define the normalized axis
\[
n_i = \frac{\Omega_i}{\|\Omega_i\|}.
\]
This determines local poles and equator on the auxiliary unit sphere:
\[
P_i^{\pm} = \pm n_i,
\qquad
E_i = \{x\in S^2 : x\cdot n_i = 0\}.
\]

## Canonical role
This object bridges the minimal projective/Berry layer to rotating local flow around a local attractor.

## Scope restriction
Examples such as nucleus, planetary core, stellar core, or galactic compact center are interpretations of the same formal object class. They are not part of the definition itself.
