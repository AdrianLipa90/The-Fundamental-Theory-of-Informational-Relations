# TIR Tetrahedral Null-Frame / Stella Parity Bridge v0.1

Status: EXACT_LOCAL_FRAME_BRIDGE / DISCRETE_Z2_SECTOR / PHYSICAL_DYNAMICS_OPEN
Date: 2026-09-24

## 1. Upstream inputs

Use the already-derived tetrahedral Bloch frame

\[
\mathbf n_a\cdot\mathbf n_b=
\begin{cases}
1,&a=b,\\
-1/3,&a\neq b,
\end{cases}
\qquad
\sum_a\mathbf n_a=0,
\]

and the TIR x IDT positive elapsed-state lift

\[
X=\ell\rho,
\qquad
x^0=\ell/2,
\qquad
\mathbf x=(\ell/2)\mathbf n.
\]

For a pure tetrahedral state define the four lifted event rays

\[
\boxed{
x_a^{(+)}
=
\frac{\ell_+}{2}
(1,\mathbf n_a)
}.
\]

With Minkowski metric \(\eta=\operatorname{diag}(1,-1,-1,-1)\),

\[
x_a^{(+)}\cdot x_a^{(+)}=0,
\]

and for \(a\neq b\),

\[
\boxed{
x_a^{(+)}\cdot x_b^{(+)}
=
\frac{\ell_+^2}{3}.
}
\]

Thus the four tetrahedral pure-state rays are null but mutually non-orthogonal.

## 2. Exact full-rank theorem

The Gram matrix is

\[
G_{ab}
=
\begin{cases}
0,&a=b,\\
\ell^2/3,&a\neq b.
\end{cases}
\]

Its eigenvalues are

\[
\ell^2,
\qquad
-\ell^2/3
\quad\text{(threefold)},
\]

so

\[
\boxed{
\det G=-\frac{\ell^8}{27}\neq0
}
\qquad(\ell>0).
\]

Therefore the four lifted tetrahedral rays form a full-rank local 4D frame.

This is stronger than the dimension count \(1+3=4\): the four canonical tetrahedral rays themselves span the carrier.

## 3. Antipodal Stella layer

The Bloch orthocomplement sends

\[
\mathbf n_a\mapsto-\mathbf n_a.
\]

Define the antipodal layer

\[
x_a^{(-)}
=
\frac{\ell_-}{2}
(1,-\mathbf n_a).
\]

Let \(E_+\) and \(E_-\) be the 4x4 matrices whose columns are the four lifted rays. Put

\[
q:=\frac{\ell_-}{\ell_+}>0
\]

and

\[
P=\operatorname{diag}(1,-1,-1,-1).
\]

Then column by column

\[
E_-=qPE_+,
\]

hence, because \(E_+\) is invertible,

\[
\boxed{
e_{-+}:=E_-E_+^{-1}=qP.
}
\]

No coordinate selection, hash, fit or 36-to-4 projection is required.

For equal elapsed scale \(q=1\),

\[
\boxed{
e_{-+}=P
}
\]

is exactly spatial parity.

## 4. Metric action

Because

\[
P^T\eta P=\eta,
\]

the relative frame satisfies

\[
\boxed{
e_{-+}^T\eta e_{-+}
=
q^2\eta.
}
\]

Thus the exact tetrahedron-to-antitetrahedron relation is:

- a discrete orientation-reversing \(Z_2\) parity sector;
- multiplied, when the two elapsed scales differ, by a positive conformal scale \(q\).

Its determinant is

\[
\boxed{
\det e_{-+}=-q^4.
}
\]

For constant \(q\), this does not generate curvature. It is a global parity/conformal frame relation.

## 5. Exact bivector / 36D image

Use the ordered pair basis

\[
(01,02,03,23,31,12).
\]

The exterior-square image is

\[
C_2(e_{-+})
=
\Lambda^2 e_{-+}.
\]

For the Stella parity bridge,

\[
\boxed{
C_2(e_{-+})
=
q^2
\operatorname{diag}
(-1,-1,-1,+1,+1,+1).
}
\]

Therefore the 6D bivector carrier splits exactly into

\[
\boxed{
3\oplus3
}
\]

with:

- the three time-space channels \((01,02,03)\) reversing sign;
- the three space-space channels \((23,31,12)\) preserving sign.

This is an exact exterior-algebra consequence of parity, not a fitted 3+3 decomposition.

The 6x6 operator has 36 coefficient slots, though this highly symmetric Stella sector occupies only a sparse/discrete subset of that space.

## 6. Wedge pairing and orientation

With

\[
J=
\begin{pmatrix}
0&I_3\\
I_3&0
\end{pmatrix},
\]

the exterior-square identity gives

\[
\boxed{
C_2(e)^TJC_2(e)
=
\det(e)J
=
-q^4J.
}
\]

Also

\[
\boxed{
\det C_2(e)
=
\det(e)^3
=
-q^{12}.
}
\]

The sign reversal of the wedge pairing is the expected orientation reversal.

## 7. Relation to self-dual / anti-self-dual sectors

An orientation-reversing 4D frame transformation reverses the Hodge orientation. Consequently it exchanges the two chiral two-form sectors:

- in Euclidean signature, the real \(\star=\pm1\) sectors;
- in Lorentzian signature, after complexification, the \(\star=\pm i\) sectors.

This is a standard geometric crosswalk. The wedge-pairing matrix \(J\) must not be silently identified with the Lorentzian Hodge operator.

## 8. What this closes

The previous chain

\[
\mathcal M_{36}
\to
B
\to
e
\]

contained an open question about a non-arbitrary 4D frame target.

For the exact tetrahedral/Stella sector the chain is now direct:

\[
\boxed{
(T_4,-T_4,\ell_+,\ell_-)
\to
(E_+,E_-)
\to
e_{-+}=qP
\to
C_2(e_{-+}).
}
\]

So the **ideal antipodal seed sector** needs no arbitrary decoder.

## 9. What remains open

The exact seed is too symmetric to be full gravity.

If every local pair remains exactly \(qP\), the metric is only conformally Minkowski:

\[
g=q^2\eta.
\]

A spatially varying \(q(x)\) can produce a conformally curved scalar sector, but this does not span generic GR metrics.

To obtain the full local geometric sector, TIR needs deformed local frames

\[
E_2(x)\neq q(x)PE_1(x),
\]

with

\[
\boxed{
e(x)=E_2(x)E_1(x)^{-1}\in GL(4).
}
\]

Then

\[
C_2(e(x))\in CO(3,3)
\]

at the local exterior-square level, and the already-defined simplicity/liftability and curvature gates apply.

The remaining physical problem is therefore no longer "how to choose 4 coordinates from 36", but:

\[
\boxed{
\text{what TIR dynamics deforms the exact tetrahedral null frame into }E(x)?
}
\]

## 10. Moire interpretation firewall

The exact antipodal relation is a discrete parity/conformal relation, not yet a moire interference field.

A genuine moire/gravity mechanism requires position-dependent relative frame data, e.g.

\[
e(x)=E_2(x)E_1(x)^{-1},
\]

whose nontrivial spatial variation survives the gauge/integrability tests.

Constant parity or constant conformal rescaling is not gravity.

## 11. Promotion ledger

- tetrahedral pure-state rays are null: PASS EXACT
- tetrahedral null-frame Gram determinant \(-\ell^8/27\): PASS EXACT
- tetrahedral lifted frame rank = 4: PASS EXACT
- Stella antipodal relative frame \(e=qP\): PASS EXACT
- equal-scale case is spatial parity: PASS EXACT
- metric relation \(e^T\eta e=q^2\eta\): PASS EXACT
- bivector image \(q^2\operatorname{diag}(-I_3,+I_3)\): PASS EXACT
- wedge pairing reverses orientation: PASS EXACT
- ideal Stella sector alone gives generic gravity: FAIL / TOO SYMMETRIC
- varying conformal factor gives full GR: FAIL / INSUFFICIENT IN GENERAL
- deformed frame pair can define general local \(GL(4)\) relative coframe: PASS ALGEBRAIC
- TIR dynamics generating physical frame deformations: OPEN
- Einstein/Newton/PPN binding: OPEN
