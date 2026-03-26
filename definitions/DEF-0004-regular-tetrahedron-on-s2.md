# DEF-0004 — Regular tetrahedron on \(S^2\)

## Status
`defined`

## Depends on
- `AX-0002`

## Objects defined here
1. `OBJ-TETRAHEDRON-0001`
2. `OBJ-RELATIVE-PHASE-TRIPLE-0001`

## Definition
A regular tetrahedron inscribed in the unit sphere \(S^2\) is a set of four unit vectors
\[
T_4 = \{v_0,v_1,v_2,v_3\} \subset S^2
\]
with pairwise inner products
\[
v_i \cdot v_j =
\begin{cases}
1 & i=j \\
-\frac{1}{3} & i\neq j
\end{cases}
\]
and zero centroid
\[
\sum_{i=0}^3 v_i = 0.
\]

## Relative phase triple
If phases \(\phi_i \in U(1)\) are assigned to tetrahedral vertices, then after quotienting by global phase one may use the three relative phases
\[
\gamma_1 = \phi_1 - \phi_0,
\qquad
\gamma_2 = \phi_2 - \phi_0,
\qquad
\gamma_3 = \phi_3 - \phi_0.
\]

## Canonical role
This object is the minimal noncoplanar spatial frame candidate extending the minimal CP1/Bloch layer toward relational 3D structure.

## Scope restriction
The tetrahedron is a geometric extension object. It does **not** yet imply a full physical derivation of all instances of the number 3.
