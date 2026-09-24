# TIR Herm(2) -> Bivector-36 Frame/Curvature Split v0.1

Status: CANDIDATE_INTEGRATION / EXACT_REPRESENTATION_THEOREM / EXACT_TETRA_EDGE_WITNESS / PHYSICAL_CURVATURE_BINDING_OPEN  
Date: 2026-09-24

## 1. Architectural correction

The current TIR main branch already contains an earlier four-dimensional event carrier:

\[
X=\ell\rho\in\operatorname{Herm}(2),
\qquad
X=x^0I+x^i\sigma_i,
\]

with the exact local-rank theorem

\[
\det J_F=\frac{\ell^3}{16}>0
\]

for \(\ell>0\), and the standard determinant form

\[
\det X=(x^0)^2-|\mathbf x|^2.
\]

The same carrier already admits the standard action

\[
X\mapsto AXA^\dagger,
\qquad
A\in SL(2,\mathbb C),
\]

with

\[
SL(2,\mathbb C)/\{\pm I\}\cong SO^+(1,3).
\]

Therefore the role of the moire/36D layer is corrected:

\[
\boxed{
\text{Herm(2) supplies the local 3+1 base;}
\quad
36D is a derived bivector/area/response carrier over that base.
}
\]

The old question "how does 36D choose four coordinates?" is no longer the preferred physical architecture.

## 2. Why 36 appears after 4D

For a four-dimensional real vector space \(V\),

\[
\dim\Lambda^2V=6,
\qquad
\dim\operatorname{End}(\Lambda^2V)=36.
\]

Choose an orientation and the pair basis

\[
(01,02,03,23,31,12).
\]

The wedge product defines the split pairing

\[
J=
\begin{pmatrix}
0&I_3\\
I_3&0
\end{pmatrix}.
\]

Thus a real \(6\times6\) relation matrix is naturally an endomorphism of the six bivector channels of an already-established 4D carrier.

## 3. Exact 36 = 16 + 20 decomposition

For \(X\in\operatorname{End}(\Lambda^2V)\), define

\[
\Theta_J(X)=JX^TJ,
\]

\[
X_{\rm so}=\frac12(X-\Theta_JX),
\qquad
\alpha=\frac{\operatorname{tr}X}{6},
\]

\[
\boxed{
X_{\rm frame}=X_{\rm so}+\alpha I_6,
}
\]

and

\[
\boxed{
Q=X-X_{\rm frame}.
}
\]

Then exactly

\[
X_{\rm frame}^TJ+JX_{\rm frame}=2\alpha J,
\]

so

\[
X_{\rm frame}\in\mathfrak{co}(3,3)
\cong\mathfrak{gl}(4)
\]

at the Lie-algebra representation level.

The complementary sector obeys

\[
JQ=Q^TJ,
\qquad
\operatorname{tr}Q=0.
\]

The projection ranks are exactly

\[
\boxed{
36=16+20.
}
\]

## 4. The 20-dimensional sector is algebraic curvature, not garbage

Define the bilinear form

\[
S=JQ.
\]

Because \(JQ=Q^TJ\),

\[
S=S^T.
\]

In four dimensions, a symmetric bilinear form on \(\Lambda^2V\) represents a pair-symmetric four-index tensor. The first algebraic Bianchi map is the natural alternation

\[
\operatorname{Sym}^2(\Lambda^2V^*)\to\Lambda^4V^*.
\]

Since \(\dim\operatorname{Sym}^2(\Lambda^2V^*)=21\) and \(\dim\Lambda^4V^*=1\), its kernel has dimension 20.

In the chosen basis, the sole independent Bianchi scalar is

\[
S_{01,23}+S_{02,31}+S_{03,12}.
\]

But

\[
\boxed{
\operatorname{tr}Q
=
2\big(
S_{01,23}+S_{02,31}+S_{03,12}
\big).
}
\]

Hence \(\operatorname{tr}Q=0\) is exactly the four-dimensional algebraic Bianchi condition in this representation.

Therefore

\[
\boxed{
\mathcal Q_{20}
\cong
\mathcal K(V),
}
\]

where \(\mathcal K(V)\) is the 20-dimensional space of algebraic Riemann curvature tensors.

This corrects the earlier provisional name "simplicity defect". A nonzero \(Q\) is not automatically a failure. It is a pointwise **algebraic-curvature candidate**.

## 5. Differential gravity firewall

The representation theorem above is pointwise algebra.

A genuine Levi-Civita curvature field must additionally satisfy the differential/geometric chain

\[
e(x)
\to
\omega_{LC}[e](x)
\to
R[\omega_{LC}](x)
\]

and its differential identities.

Therefore an arbitrary projected \(Q(x)\) is **not** automatically the physical curvature of \(X_{\rm frame}(x)\).

The physical promotion gate is

\[
\boxed{
Q(x)
\stackrel{?}{=}
R\big[\omega_{LC}(e[X_{\rm frame}])\big](x)
}
\]

up to the declared representation maps, units and gauge conventions.

This is stronger than a dimension match and remains OPEN.

## 6. Exact tetrahedral edge-transport witness

TIR already defines, for a regular \(n\)-simplex,

\[
U_{ij}
=
\frac{I+\Sigma_i\Sigma_j}{\sqrt{2(1+c)}},
\qquad
c=-\frac1n.
\]

For the tetrahedral case \(n=3\),

\[
\boxed{
U_{ij}=\sqrt{\frac34}\,(I+\Sigma_i\Sigma_j).
}
\]

Use the six oriented edge labels

\[
\mathcal E=(01,02,03,23,31,12).
\]

For the oppositely oriented companion sheet, use

\[
U^-_{ij}=U_{ji}=U_{ij}^\dagger.
\]

Define the coefficient-free normalized Hilbert--Schmidt overlap

\[
\boxed{
X_{ab}
=
\frac14\operatorname{Tr}
\left[
(U^+_a)^\dagger U^-_b
\right].
}
\]

The exact matrix is

\[
\boxed{
X=
\frac13
\begin{pmatrix}
-1&2&2&1&2&0\\
2&-1&2&0&1&2\\
2&2&-1&2&0&1\\
1&0&2&-1&0&0\\
2&1&0&0&-1&0\\
0&2&1&0&0&-1
\end{pmatrix}.
}
\]

No PhaseNav ID, label hash or fitted coefficient enters this witness.

## 7. Phase-only decoder falsified on the canonical witness

The previously preregistered relation law

\[
\arg X_{ab}
\]

fails closed on this canonical construction because

\[
\boxed{12/36}
\]

entries of \(X\) vanish exactly.

The phase of an exact zero is undefined.

Therefore

\[
\boxed{
\text{TETRA_EDGE_PAIR_PHASE_ONLY_DECODER = FAIL}
}
\]

for the canonical edge-transport witness.

The full signed Hilbert--Schmidt overlap remains well-defined and is the correct raw observable for this witness.

## 8. Exact half split of the canonical tetra relation matrix

Apply the exact decomposition of Section 3:

\[
X=X_{\rm frame}+Q_{\rm curv}.
\]

With the Frobenius norm,

\[
\|X\|_F^2=\frac{20}{3},
\]

while

\[
\boxed{
\|X_{\rm frame}\|_F^2
=
\frac{10}{3},
}
\]

and

\[
\boxed{
\|Q_{\rm curv}\|_F^2
=
\frac{10}{3}.
}
\]

Thus

\[
\boxed{
\frac{\|X_{\rm frame}\|_F^2}{\|X\|_F^2}
=
\frac{\|Q_{\rm curv}\|_F^2}{\|X\|_F^2}
=
\frac12.
}
\]

This is an exact property of the canonical tetrahedral edge-transport overlap construction and the declared wedge-pairing decomposition.

It is not claimed to be a universal law of Nature.

## 9. Relation to moire

The corrected architecture is

\[
\boxed{
\operatorname{Herm}(2)_{3+1}
\to
\Lambda^2
\to
\operatorname{End}(\Lambda^2)_{36}
\to
\big(
\mathfrak{gl}(4)_{16},
\mathcal K(V)_{20}
\big).
}
\]

A moire/hyperlayer relation operator can therefore be read as carrying, pointwise:

- a frame/deformation channel;
- an algebraic-curvature channel.

Interference zeros remain relational nulls; they do not erase the parent layers.

The remaining physical task is no longer "extract 4D from 36D". It is:

\[
\boxed{
\text{derive the physical relation operator }X(x)
\text{ and prove differential compatibility between its 16- and 20-sectors.}
}
\]

## 10. PhaseNav firewall

Canonical legacy PhaseNav \(\phi_0,\ldots,\phi_{35}\) is not natively this tetrahedral \(6\times6\) operator.

The exact tetrahedral witness above is built from source-derived simplex/Clifford edge transports, not by row-major reshaping of legacy Phase36.

Legacy Phase36 may be used only as a separate computational/fibre representation unless a source-derived intertwiner is proved.

## 11. Promotion ledger

- Herm(2) local 4D carrier: REUSE EXISTING EXACT CANDIDATE GATE
- Herm(2) Lorentz covariance: REUSE EXISTING EXACT CANDIDATE GATE
- dim End(Lambda2 R4)=36: PASS EXACT
- Mat6 = co(3,3) + Q20: PASS EXACT
- co(3,3) ~= gl(4) Lie representation: PASS STANDARD/EXACT CROSSWALK
- Q20 -> symmetric pair tensor: PASS EXACT
- tr(Q)=0 <-> 4D algebraic Bianchi scalar: PASS EXACT
- Q20 ~= algebraic curvature tensors: PASS EXACT/STANDARD
- canonical tetra edge overlap matrix: PASS EXACT
- canonical phase-only decoder: FAIL (12 exact zeros)
- exact Frobenius energy split 1/2 + 1/2: PASS EXACT FOR WITNESS
- Q(x) = physical Levi-Civita curvature of frame sector: OPEN
- physical normalization / G: OPEN
- production spacetime realization: OPEN
- Clay/Millennium closure: NOT CLAIMED


## 12. Tetrahedral S4 covariance of the six-axis basis

The six oriented representatives

\[
(01,02,03,23,31,12)
\]

are the two-element index pairs of four tetrahedral labels.

Every vertex permutation \(p\in S_4\) induces a signed permutation matrix \(C_2(p)\) on this six-dimensional pair space, with

\[
\boxed{
C_2(p)^TJC_2(p)
=
\operatorname{sgn}(p)J.
}
\]

Thus:

- the 12 even permutations preserve the oriented wedge pairing;
- the 12 odd permutations reverse its overall orientation;
- the involution \(\Theta_J(X)=JX^TJ\) is unchanged by the global sign \(J\mapsto-J\);
- the frame/curvature decomposition is therefore compatible with tetrahedral relabeling.

This is an exact covariance statement about the index carrier. It does not identify tetrahedral labels with physical spacetime coordinates.


## 13. Exact criterion for the half/half norm split

Because \(\Theta_J\) is an orthogonal involution for the Frobenius pairing, write

\[
A=\frac12(X-\Theta_JX),
\qquad
B=\frac12(X+\Theta_JX),
\qquad
\alpha=\frac{\operatorname{tr}X}{6}.
\]

Then

\[
X_{\rm frame}=A+\alpha I,
\qquad
Q=B-\alpha I,
\]

with all relevant summands mutually orthogonal. Therefore

\[
\boxed{
\|X_{\rm frame}\|_F^2
-
\|Q\|_F^2
=
-\langle X,\Theta_JX\rangle_F
+
\frac{(\operatorname{tr}X)^2}{3}.
}
\]

Hence the two sectors carry exactly equal Frobenius norm if and only if

\[
\boxed{
\langle X,\Theta_JX\rangle_F
=
\frac{(\operatorname{tr}X)^2}{3}.
}
\]

For the canonical tetrahedral overlap witness,

\[
\operatorname{tr}X=-2,
\qquad
\langle X,\Theta_JX\rangle_F=\frac43,
\]

so the exact \(1/2+1/2\) split is forced by this identity rather than being a numerical accident.

## 14. Exact barycentric 1+3 frame generator

Applying the inverse exterior-square Lie map to the canonical tetrahedral frame sector gives

\[
\boxed{
H_\Delta
=
\frac13\mathbf 1\mathbf 1^T
-
\frac12 I_4.
}
\]

Equivalently,

\[
H_\Delta=
\begin{pmatrix}
-1/6&1/3&1/3&1/3\\
1/3&-1/6&1/3&1/3\\
1/3&1/3&-1/6&1/3\\
1/3&1/3&1/3&-1/6
\end{pmatrix}.
\]

The vertex permutation representation therefore splits exactly as

\[
\mathbb R^4
=
\operatorname{span}(1,1,1,1)
\oplus
\{v:\sum_i v_i=0\},
\]

with dimensions

\[
\boxed{4=1+3}
\]

and eigenvalues

\[
\boxed{
\lambda_{\rm bary}=\frac56,
\qquad
\lambda_{\rm std}=-\frac12
\quad\text{(multiplicity 3)}.
}
\]

This is the standard trivial-plus-standard decomposition of the tetrahedral vertex representation under \(S_4\).

TIR already has an independent \(1+3\) Herm(2) event carrier \(I\oplus\operatorname{span}(\sigma_x,\sigma_y,\sigma_z)\). The two decompositions are representation-compatible, but physical identification of the barycentric scalar with clock time and the standard three-space with measured spatial directions remains a separate binding gate.
