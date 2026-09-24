# TIR Tetrahedral Antipodal 1+3 Split v0.1

Status: EXACT_CARRIER_DECOMPOSITION / PHYSICAL_TIME_SPACE_INTERPRETATION_CONDITIONAL  
Date: 2026-09-24

## 1. Input

Use the exact tetrahedral null frame and its antipodal partner

\[
E_- = P E_+,
\qquad
P=\operatorname{diag}(1,-1,-1,-1).
\]

Define the symmetric and antisymmetric layer combinations

\[
\boxed{
E_{\rm com}=\frac12(E_+ + E_-),
\qquad
E_{\rm diff}=\frac12(E_+ - E_-).
}
\]

## 2. Exact ranks

For the canonical tetrahedral frame,

\[
E_{\rm com}
=
\begin{pmatrix}
1&1&1&1\\
0&0&0&0\\
0&0&0&0\\
0&0&0&0
\end{pmatrix},
\]

so

\[
\boxed{\operatorname{rank}E_{\rm com}=1.}
\]

The differential channel is

\[
E_{\rm diff}
=
\begin{pmatrix}
0&0&0&0\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix},
\]

with

\[
\boxed{\operatorname{rank}E_{\rm diff}=3.}
\]

Therefore

\[
\boxed{4=1+3}
\]

is an exact consequence of the antipodal tetrahedral pairing.

Moreover,

\[
E_+=E_{\rm com}+E_{\rm diff},
\qquad
E_-=E_{\rm com}-E_{\rm diff}.
\]

No information is lost by the split.

## 3. Intrinsic formulation

Before choosing the rational chart, the positive elapsed-state lift of a tetrahedral Bloch direction is proportional to

\[
X_a^+ = (1,\mathbf n_a),
\qquad
X_a^- = (1,-\mathbf n_a).
\]

Then

\[
\frac{X_a^+ + X_a^-}{2}=(1,\mathbf 0)
\]

is identical for every tetrahedral label \(a\), while

\[
\frac{X_a^+ - X_a^-}{2}=(0,\mathbf n_a).
\]

The four differential vectors satisfy

\[
\sum_a\mathbf n_a=0
\]

and span the three-dimensional Bloch/Pauli coefficient space.

Thus the rank-one common channel and rank-three differential channel are not artifacts of the Hadamard chart.

## 4. Conditional spacetime reading

The existing TIR x IDT positive-cone theorem independently assigns the scalar elapsed coordinate to the identity component and the three Bloch coordinates to the Pauli components.

Under that already-admitted crosswalk, the exact decomposition becomes

\[
\boxed{
\text{common antipodal channel}
\leftrightarrow
1\text{ scalar/elapsed direction},
}
\]

\[
\boxed{
\text{differential antipodal channel}
\leftrightarrow
3\text{ Bloch/spatial relation directions}.
}
\]

This is a carrier theorem. The calibration of the scalar direction as physical time and the three differential directions as physical space remains subject to the existing TIR/IDT physical binding gates.

## 5. Exterior-square consequence

Applying the exterior square to the parity involution gives

\[
\Pi=C_2(P)=\operatorname{diag}(-I_3,+I_3).
\]

Hence the vector-level

\[
4=1+3
\]

decomposition induces the bivector-level

\[
\boxed{6=3+3}.
\]

The exact half-projectors

\[
\frac12(I\pm P)
\]

select the 1D/3D vector sectors, while

\[
\frac12(I\pm\Pi)
\]

select the complementary 3D/3D bivector sectors.

This gives a two-level hierarchy:

\[
\boxed{
4=1+3
\quad\xrightarrow{\Lambda^2}\quad
6=3+3.
}
\]

## 6. Moire/null reading

The two parent layers are nonzero, but their symmetric/antisymmetric overlays vanish identically on complementary subspaces.

Therefore the construction realizes an exact algebraic version of the project motif

\[
\text{nonzero layers}
\to
\text{relative overlay}
\to
\text{structured zero}.
\]

No literal optical material moire or gravitational field is claimed by this identity alone.

## 7. Promotion ledger

- antipodal half-sum rank = 1: PASS EXACT
- antipodal half-difference rank = 3: PASS EXACT
- exact reconstruction of both parent layers: PASS EXACT
- differential tetra directions sum to zero: PASS EXACT
- 4=1+3 carrier decomposition: PASS EXACT
- exterior-square 6=3+3 consequence: PASS EXACT
- scalar channel = calibrated physical time: CONDITIONAL / EXISTING IDT GATE
- three differential directions = universal physical space: CONDITIONAL / EXISTING TIR GATE
- constant split = gravity: FAIL / NOT IMPLIED
