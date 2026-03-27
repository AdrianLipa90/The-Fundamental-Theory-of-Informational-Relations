# D-0003 — Regular tetrahedron on \(S^2\)

## Status
`derived`

## Depends on
- `AX-0002`
- `DEF-0004`

## Goal
Derive the minimal noncoplanar frame inscribed in the unit sphere and show why it naturally yields three relative directions / phases after removal of one global redundancy.

## Step 1 — Vertex constraints
Let \(v_0,v_1,v_2,v_3 \in \mathbb R^3\) satisfy:
\[
\|v_i\|=1,
\qquad
v_i\cdot v_j = c \text{ for } i\neq j.
\]
For a regular tetrahedron, all off-diagonal inner products are equal.

## Step 2 — Impose zero centroid
Demand symmetric centering:
\[
\sum_{i=0}^3 v_i = 0.
\]
Then
\[
0 = \left\|\sum_{i=0}^3 v_i\right\|^2 = \sum_{i=0}^3 \|v_i\|^2 + 2\sum_{i<j} v_i\cdot v_j.
\]
Because there are four unit vectors and six off-diagonal pairs,
\[
0 = 4 + 12c.
\]
Thus
\[
c = -\frac13.
\]
Hence
\[
v_i \cdot v_j =
\begin{cases}
1 & i=j \\
-\frac13 & i\neq j.
\end{cases}
\]

## Step 3 — Minimal 3D simplex
A tetrahedron is a 3-simplex, so it is the minimal noncoplanar simplex and therefore the first minimal volume-supporting extension beyond a purely surface triangle.

## Step 4 — Relative redundancy count
A tetrahedron has four vertices. If one global reference is removed, the number of independent relative directions is
\[
4-1=3.
\]
This same count applies to phases assigned at the vertices after removal of global \(U(1)\).

## Step 5 — Relative phase triple
Assign phases \(\phi_i\in U(1)\). Quotienting by a global phase leaves three independent phase differences, e.g.
\[
\gamma_1=\phi_1-\phi_0,
\qquad
\gamma_2=\phi_2-\phi_0,
\qquad
\gamma_3=\phi_3-\phi_0.
\]
These become the natural minimal triple for later closure constructions.

## Result
The regular tetrahedron inscribed in \(S^2\) is the minimal nontrivial spatial frame that:
1. is noncoplanar,
2. has symmetric centroid zero,
3. yields three independent relative directions / phase channels after removal of one global redundancy.

## Scope restriction
This derivation supports the geometry of a minimal relational 3D frame. It does not by itself prove a full physical theory of all occurrences of the number 3.
