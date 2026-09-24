# TIR Differential Frame/Curvature Compatibility Gate v0.1

Status: CANDIDATE_DIFFERENTIAL_GATE / EXACT_NEGATIVE_CONTROL / EXACT_CURVED_CONTROL / PHYSICAL_SOURCE_FIELD_OPEN  
Date: 2026-09-24

## 1. Purpose

The pointwise representation theorem

\[
\operatorname{Mat}_6
=
\mathfrak{co}(3,3)_{16}
\oplus
\mathcal K(V)_{20}
\]

does not by itself prove gravity.

The 16-dimensional sector can be interpreted locally as the exterior-square image of a frame generator,

\[
X_{\rm frame}=\rho(H),
\qquad
H\in\mathfrak{gl}(4),
\]

while the 20-dimensional sector determines an algebraic-curvature bilinear

\[
S_{\rm alg}=JQ.
\]

Physical Levi-Civita curvature requires an additional differential compatibility condition.

## 2. Differential compatibility operator

Let a spacetime-dependent frame/coframe field be reconstructed or supplied as

\[
e=e(x).
\]

It determines

\[
g_{\mu\nu}
=
\eta_{IJ}e^I{}_{\mu}e^J{}_{\nu},
\]

the Levi-Civita connection

\[
\Gamma[g],
\]

and the Riemann tensor

\[
R_{\rm LC}[e].
\]

Write the corresponding curvature bilinear on the six 2-form channels as

\[
S_{\rm LC}(e).
\]

Define the differential compatibility residual

\[
\boxed{
\mathcal C[e,Q]
=
S_{\rm alg}[Q]
-
S_{\rm LC}[e].
}
\]

The physical promotion gate is

\[
\boxed{
\mathcal C[e,Q]=0
}
\]

modulo the declared basis, signature, units and gauge conventions.

Pointwise algebraic Bianchi is necessary but not sufficient.

## 3. Exact negative control: constant tetra relation field

Take the exact canonical tetrahedral edge-transport overlap matrix

\[
X_{\Delta}
=
\frac13
\begin{pmatrix}
-1&2&2&1&2&0\\
2&-1&2&0&1&2\\
2&2&-1&2&0&1\\
1&0&2&-1&0&0\\
2&1&0&0&-1&0\\
0&2&1&0&0&-1
\end{pmatrix}.
\]

Its exact split gives

\[
X_{\Delta}
=
X_{\rm frame}
+
Q_{\rm alg},
\]

with

\[
\|Q_{\rm alg}\|_F^2
=
\frac{10}{3}.
\]

If this relation operator is taken to be constant in a simply connected local chart, then the reconstructed local frame generator is constant. Hence a constant coframe representative gives

\[
de=0,
\qquad
\omega_{\rm LC}=0,
\qquad
R_{\rm LC}=0.
\]

But

\[
S_{\rm alg}=JQ_{\rm alg}\ne0.
\]

Therefore

\[
\boxed{
\mathcal C\ne0
}
\]

and the constant tetrahedral relation witness fails the physical curvature gate.

This is an intended negative control, not a failure of the pointwise algebra.

It proves that the static tetrahedral overlap matrix cannot be promoted directly to physical spacetime curvature.

## 4. Exact curved positive control

Use the local Euclidean product metric

\[
S^2\times\mathbb R^2
\]

in stereographic coordinates,

\[
e^0=\Omega\,dx,
\qquad
e^1=\Omega\,dy,
\qquad
e^2=dz,
\qquad
e^3=dw,
\]

with

\[
\boxed{
\Omega(x,y)=\frac{2}{1+x^2+y^2}.
}
\]

Thus

\[
g
=
\Omega^2(dx^2+dy^2)
+
dz^2+dw^2.
\]

At the chart origin,

\[
\Omega(0,0)=2.
\]

Direct symbolic Levi-Civita calculation gives, in the coordinate basis,

\[
R_{0101}=16,
\]

and after conversion to the orthonormal coframe,

\[
\boxed{
R_{\hat0\hat1\hat0\hat1}=1.
}
\]

All independent curvature channels involving the flat \(z,w\) directions vanish.

Hence the bivector curvature bilinear in the basis

\[
(01,02,03,23,31,12)
\]

is

\[
\boxed{
S_{\rm LC}
=
\operatorname{diag}(1,0,0,0,0,0).
}
\]

Set

\[
Q_{\rm LC}=J S_{\rm LC}.
\]

At the same point the frame generator may be represented by

\[
H_0
=
\operatorname{diag}(\ln2,\ln2,0,0),
\]

whose exterior-square differential is

\[
\rho(H_0)
=
\operatorname{diag}
(2\ln2,\ln2,\ln2,0,\ln2,\ln2).
\]

Construct the synthetic exact control

\[
X_{\rm ctrl}
=
\rho(H_0)+Q_{\rm LC}.
\]

The 36=16+20 projector recovers exactly:

\[
X_{\rm frame}=\rho(H_0),
\qquad
Q=Q_{\rm LC},
\]

and therefore

\[
\boxed{
\mathcal C(0)=0.
}
\]

This shows that the representation split can encode a frame and its actual Levi-Civita algebraic curvature consistently when the differential field is supplied correctly.

It does not show that TIR/moire dynamics generates this field.

## 5. Consequence for moire gravity

The corrected physical chain is

\[
\boxed{
\text{moire/relational field }X(x)
\to
\big(H(x),Q(x)\big)
\to
e[H](x)
\to
R_{\rm LC}[e](x)
\stackrel{?}{=}
JQ(x).
}
\]

A constant relative layer displacement cannot pass unless the 20D curvature sector also vanishes locally or nontrivial global/topological data enter through a separately admitted connection.

Thus physical gravity requires spatial/temporal variation, non-integrable gluing, or another source of nontrivial connection curvature.

## 6. Relation to existing TIR gates

This gate does not define a second gravitational connection.

It reuses the existing TIR hierarchy:

- Cartan refinement;
- zero-torsion Levi-Civita selection;
- leading-loop metric-jet gate;
- event-spatial metric-rate / RF-E9 route where applicable;
- existing Einstein/ADM sector.

The new object is only a compatibility test between the independent 20D algebraic-curvature channel and curvature already owned by the admitted geometric connection.

## 7. Promotion ledger

- pointwise 36=16+20 split: PASS EXACT
- algebraic Bianchi in 20D sector: PASS EXACT
- constant tetra witness has nonzero Q: PASS EXACT
- constant local frame has R_LC=0: PASS STANDARD/EXACT CONTROL
- constant tetra witness differential compatibility: FAIL EXACT
- S2 x R2 stereographic R_hat0101=1 at origin: PASS EXACT
- synthetic curved frame+curvature reconstruction: PASS EXACT CONTROL
- moire dynamics -> spacetime-dependent compatible X(x): OPEN
- production physical source field: OPEN
- Newton coupling / units: OPEN
- PPN/lensing/GW validation: OPEN
- Millennium/Clay closure: NOT CLAIMED
