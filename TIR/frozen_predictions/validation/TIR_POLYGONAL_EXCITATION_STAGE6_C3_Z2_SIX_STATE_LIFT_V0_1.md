# TIR Polygonal Excitation — Stage 6: Pure Mathematical Test of the C3 × Z2 Six-State Lift v0.1

**Status:** `STAGE_6_PURE_MATHEMATICS_PASS`

## Scope

This stage tests only the abstract algebra implied by a three-state cyclic degree of freedom together with an independent binary sheet. It does not identify these states with any physical flavor, color, polarization, particle, or measured observable.

## 1. Three-state cyclic operator

Let

\[
P_3=\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{pmatrix},
\qquad P_3^3=I_3.
\]

The order of \(P_3\) is exactly three.

## 2. Binary sheet operator

Let

\[
X_2=\begin{pmatrix}
0&1\\
1&0
\end{pmatrix},
\qquad X_2^2=I_2.
\]

The order of \(X_2\) is exactly two.

## 3. Six-state lifted operator

Define the product-space operator

\[
G=P_3\otimes X_2
\]

on a six-dimensional state space.

Because the factors act on independent tensor components,

\[
G^k=P_3^k\otimes X_2^k.
\]

Therefore

\[
G^k=I_6
\]

if and only if

\[
3\mid k
\qquad\text{and}\qquad
2\mid k.
\]

The smallest positive solution is

\[
k=\operatorname{lcm}(3,2)=6.
\]

Hence

\[
\boxed{\operatorname{ord}(G)=6}.
\]

In particular,

\[
G^3=I_3\otimes X_2\neq I_6,
\]

while

\[
G^6=I_6.
\]

Thus after three steps the cyclic base state has returned but the binary sheet has flipped; after six steps the full lifted state returns.

## 4. Spectrum

The eigenvalues of \(P_3\) are

\[
1,\omega,\omega^2,
\qquad \omega=e^{2\pi i/3},
\]

and the eigenvalues of \(X_2\) are \(+1,-1\).

The eigenvalues of \(G\) are therefore

\[
\{\pm1,\pm\omega,\pm\omega^2\},
\]

which are exactly the six sixth roots of unity. Hence

\[
\boxed{\chi_G(\lambda)=\lambda^6-1}.
\]

This supplies an exact six-phase closure without numerical fitting.

## 5. Projection to the three-state base

Let

\[
\pi:\{0,1,2\}\times\{+,-\}\to\{0,1,2\}
\]

forget the binary sheet. Then the projected orbit has period three, while the lifted orbit has period six.

Therefore a three-cycle can coexist with a six-step identity closure without contradiction:

\[
\boxed{\text{projected period}=3,\qquad\text{lifted period}=6.}
\]

## 6. Comparison with the spinor lift already tested

The earlier TIR operator test gave, for the spin-1/2 lift of the tetrahedral \(2\pi/3\) rotation,

\[
U_3^3=-I,
\qquad
U_3^6=I.
\]

Stage 6 gives independently

\[
G^3=I_3\otimes X_2,
\qquad
G^6=I_6.
\]

These are different representations and are not identified as the same operator. What is established is the shared cyclic closure structure: a three-step return in the projected degree of freedom and a six-step return in the lifted state.

## 7. Important generalization boundary

For a generic product generator

\[
G_m=P_m\otimes X_2,
\]

its order is

\[
\operatorname{ord}(G_m)=\operatorname{lcm}(m,2).
\]

Thus

\[
\operatorname{ord}(G_m)=2m
\]

only when \(m\) is odd. For even \(m\), the order is \(m\).

This distinction is retained explicitly because the tensor-product binary-sheet construction and the SU(2) spinor lift are not generically identical constructions.

## 8. Verdict

The pure mathematical test passes:

1. a three-state cyclic operator has exact order 3;
2. an independent binary sheet has exact order 2;
3. their product generator has exact order 6;
4. the six eigenphases are precisely the sixth roots of unity;
5. projection erases the binary sheet and reduces the observable period from 6 to 3;
6. the resulting 3/6 closure pattern matches the group-order pattern found independently in the TIR spinor lift, without identifying the two representations.

No physical correspondence is promoted in this stage.
