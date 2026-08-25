# TIR Polygonal Excitation — Stage 13: Exact Geometry–Spectrum Identity

Status: `STAGE_13_GEOMETRY_SPECTRUM_IDENTITY_PASS`

Scope: exact geometric and spectral relation for the finite spherical sequence N=3,4,5.

## 1. Objects

Let X_N be the V_N x 3 matrix whose rows are the unit-sphere vertex vectors of the regular triangular closure {3,N}. Let A_N be its unweighted edge adjacency matrix.

Every vertex has exactly N neighbours. For adjacent vertices v_i and v_j, Stage 1 gives the common inner product

\[
v_i\cdot v_j=c_N,
\qquad
c_N=\frac{\cos(2\pi/N)}{1-\cos(2\pi/N)}.
\]

## 2. Symmetry lemma

For a fixed vertex v_i, the N neighbouring vertices form a regular ring around its axis. Their vector sum is therefore axis-aligned:

\[
\sum_{j\sim i}v_j=\alpha_N v_i.
\]

Taking the inner product with v_i gives

\[
\alpha_N
=\sum_{j\sim i}v_i\cdot v_j
=Nc_N.
\]

Hence, row by row,

\[
A_NX_N=Nc_NX_N.
\]

Therefore

\[
\boxed{
\frac{A_N}{N}X_N=c_NX_N
}.
\]

The three Euclidean coordinate columns of X_N span a three-dimensional eigenspace of the normalized adjacency/exchange matrix H_N=A_N/N.

## 3. N=3

For the tetrahedron,

\[
c_3=-\frac13.
\]

The normalized adjacency spectrum is

\[
\operatorname{spec}(A_3/3)=\{1,(-1/3)^{\times3}\}.
\]

Thus the complete three-dimensional nontrivial eigenspace is exactly the geometric coordinate space.

## 4. N=4

For the octahedron,

\[
\boxed{c_4=0}.
\]

Stage 12 gives

\[
\operatorname{spec}(A_4/4)=\{1,(-1/2)^{\times2},0^{\times3}\}.
\]

Therefore

\[
\boxed{(A_4/4)X_4=0}.
\]

The geometric coordinate representation is exactly the three-dimensional zero eigenspace.

## 5. N=5

For the icosahedron,

\[
\boxed{c_5=\frac1{\sqrt5}}.
\]

Stage 12 gives

\[
\operatorname{spec}(A_5/5)
=
\{1,(1/\sqrt5)^{\times3},(-1/\sqrt5)^{\times3},(-1/5)^{\times5}\}.
\]

Therefore

\[
\boxed{
(A_5/5)X_5=\frac1{\sqrt5}X_5
}.
\]

The Stage 1 local latitude is exactly the positive threefold global exchange eigenvalue.

## 6. Computational audit

The audit reconstructs the tetrahedral, octahedral, and icosahedral coordinates, infers edges from the unique minimum pair distance, and evaluates

\[
R_N=\left\|\frac{A_N}{N}X_N-c_NX_N\right\|_\infty.
\]

Measured residuals:

\[
R_3=5.55\times10^{-17},
\qquad
R_4=6.12\times10^{-17},
\qquad
R_5=5.55\times10^{-17}.
\]

In every case the coordinate matrix has rank three and c_N has spectral multiplicity three.

## 7. Verdict

`STAGE_13_GEOMETRY_SPECTRUM_IDENTITY_PASS`

This identity supplies a parameter-free geometric exchange eigenspace for N=4 and N=5. The later QHTRI gate can therefore consume H_N=A_N/N as a frozen geometric operator rather than introduce fitted coupling weights.