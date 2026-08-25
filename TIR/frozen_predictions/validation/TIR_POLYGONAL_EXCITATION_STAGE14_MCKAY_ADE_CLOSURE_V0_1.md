# TIR Polygonal Excitation — Stage 14: McKay ADE Closure of the N=3,4,5 Spinor Sequence

Status: `STAGE_14_MCKAY_ADE_CLOSURE_PASS`

Scope: pure mathematics of finite SU(2) subgroups, binary polyhedral groups, and affine ADE correspondence.

## 1. Input from Stage 11

The spinor double covers of the finite spherical rotational groups are

\[
N=3:\quad 2T,
\qquad
N=4:\quad 2O,
\qquad
N=5:\quad 2I,
\]

with orders

\[
24,\qquad48,\qquad120.
\]

## 2. McKay correspondence

For a finite subgroup G of SU(2), construct a graph whose vertices are irreducible representations \(\rho_i\). Let V be the defining two-dimensional representation of SU(2). The edge multiplicities are defined by

\[
V\otimes\rho_i
=\bigoplus_j a_{ij}\rho_j.
\]

The resulting McKay graph for the three binary polyhedral groups is the affine exceptional Dynkin sequence

\[
\boxed{
2T\leftrightarrow\widetilde E_6,
\qquad
2O\leftrightarrow\widetilde E_7,
\qquad
2I\leftrightarrow\widetilde E_8.
}
\]

Thus the geometric N sequence induces

\[
\boxed{
N=3\to\widetilde E_6,
\qquad
N=4\to\widetilde E_7,
\qquad
N=5\to\widetilde E_8.
}
\]

## 3. Dimension-vector identity

Let

\[
d_i=\dim\rho_i.
\]

Taking dimensions of the McKay tensor-product rule gives

\[
2d_i=\sum_j a_{ij}d_j.
\]

Hence, if A is the affine Dynkin adjacency matrix,

\[
\boxed{Ad=2d},
\]

or equivalently for the affine Cartan matrix C=2I-A,

\[
\boxed{Cd=0}.
\]

The representation-dimension vector is therefore the positive affine null vector.

## 4. Binary tetrahedral / affine E6

A dimension vector is

\[
d_{E_6}=(3,2,2,2,1,1,1).
\]

It satisfies

\[
A_{\widetilde E_6}d_{E_6}=2d_{E_6}
\]

and

\[
\sum_i d_i^2
=9+3\cdot4+3\cdot1
=24
=|2T|.
\]

## 5. Binary octahedral / affine E7

A dimension vector is

\[
d_{E_7}=(4,3,2,1,3,2,1,2).
\]

It satisfies

\[
A_{\widetilde E_7}d_{E_7}=2d_{E_7}
\]

and

\[
\boxed{\sum_i d_i^2=48=|2O|}.
\]

Thus the N=4 octahedral spinor closure lands exactly on the affine E7 McKay graph.

## 6. Binary icosahedral / affine E8

A dimension vector is

\[
d_{E_8}=(6,5,4,3,2,1,4,2,3).
\]

It satisfies

\[
A_{\widetilde E_8}d_{E_8}=2d_{E_8}
\]

and

\[
\boxed{\sum_i d_i^2=120=|2I|}.
\]

Thus the N=5 icosahedral spinor closure lands exactly on the affine E8 McKay graph.

## 7. Computational audit

The audit constructs explicit affine-E6, affine-E7, and affine-E8 adjacency matrices in node orders adapted to their positive dimension vectors and verifies:

1. the binary group orders 24,48,120;
2. the exact integer equation Ad=2d;
3. the identity \(\sum_i d_i^2=|G|\);
4. a numerical zero eigenvalue of C=2I-A.

The integer residual is exactly zero in all three cases. The smallest affine-Cartan eigenvalues are of floating-point order 10^-16.

## 8. Verdict

`STAGE_14_MCKAY_ADE_CLOSURE_PASS`

The Stage 14 result is a mathematical closure of the N=3,4,5 spinor sequence into the exceptional affine ADE sequence. Physical assignments are reserved for a later preregistered gate.