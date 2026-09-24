# TIR Tetrahedral Null-Frame / Bivector Moire Bridge v0.1

Status: CANDIDATE_FOUNDATIONAL_BRIDGE / EXACT_CARRIER_GEOMETRY / PHYSICAL_DYNAMICS_OPEN  
Date: 2026-09-24

## 1. Purpose

This bridge closes the previously open question of how the tetrahedral Bloch/SIC carrier can produce a non-arbitrary six-edge bivector carrier without hashing edge labels into the legacy PhaseNav 36-vector.

The construction uses the already-admitted TIR x IDT positive elapsed-state lift

\[
X=\ell\rho,
\qquad
\rho=\frac12(I+\mathbf n\cdot\boldsymbol\sigma),
\]

together with the four regular tetrahedral Bloch directions.

The result is an exact four-null-vector frame, an exact six-bivector edge frame, and an exact 6x6 relative operator for the antipodal layer.

It does **not** claim that constant antipodal parity is gravity.

## 2. Tetrahedral null frame

Choose the unnormalized tetrahedral signs

\[
v_0=(1,1,1),\quad
v_1=(1,-1,-1),\quad
v_2=(-1,1,-1),\quad
v_3=(-1,-1,1).
\]

The normalized Bloch directions are

\[
\mathbf n_a=\frac{v_a}{\sqrt3}.
\]

The standard positive-cone lift gives future null rays proportional to

\[
(1,\mathbf n_a).
\]

Use the rational spatially-rescaled chart

\[
(1,\mathbf n_a)
\mapsto
(1,v_a),
\]

whose metric is

\[
G_T=\operatorname{diag}\left(1,-\frac13,-\frac13,-\frac13\right).
\]

The four columns form

\[
\boxed{
E_+=
\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&1&-1\\
1&-1&-1&1
\end{pmatrix}.
}
\]

This is the order-four Hadamard matrix. Exactly,

\[
E_+E_+^T=4I_4,
\qquad
\det E_+=-16,
\qquad
E_+^{-1}=\frac14E_+^T.
\]

Therefore the four lifted tetrahedral rays are linearly independent and form a full local four-dimensional frame.

Their Gram matrix under \(G_T\) is

\[
E_+^T G_T E_+
=
\begin{pmatrix}
0&4/3&4/3&4/3\\
4/3&0&4/3&4/3\\
4/3&4/3&0&4/3\\
4/3&4/3&4/3&0
\end{pmatrix}.
\]

Each column is null and every distinct pair has the same positive Lorentzian inner product.

## 3. Antipodal layer

Bloch orthocomplement sends

\[
\mathbf n\mapsto-\mathbf n.
\]

In the rational chart this is the parity matrix

\[
\boxed{
P=\operatorname{diag}(1,-1,-1,-1).
}
\]

Hence

\[
\boxed{
E_-=PE_+.
}
\]

The relative four-dimensional frame is therefore exactly

\[
\boxed{
E_-E_+^{-1}=P.
}
\]

This contains no fitted parameter.

The antipodal pair reverses spatial orientation:

\[
\det E_- = +16,
\qquad
\det P=-1.
\]

## 4. Six tetrahedral edges as a bivector frame

A four-frame induces its six two-form/edge directions through the exterior square.

Define

\[
B_+=C_2(E_+)=\Lambda^2E_+,
\qquad
B_-=C_2(E_-).
\]

The six columns correspond exactly to the six unordered tetrahedral vertex pairs

\[
(01,02,03,23,31,12).
\]

Because \(E_+\) is invertible, \(B_+\) is invertible and

\[
\boxed{
\det B_+=(\det E_+)^3=-4096.
}
\]

Thus the six tetrahedral edges are not merely six labels: after the null-frame lift they form a complete basis of \(\Lambda^2\) of the four-dimensional carrier.

Functoriality gives

\[
\boxed{
B_-=C_2(P)B_+.
}
\]

## 5. Exact 3+3 antipodal bivector split

In the ordered basis

\[
(01,02,03,23,31,12),
\]

the induced parity operator is

\[
\boxed{
\Pi=C_2(P)
=
\operatorname{diag}(-1,-1,-1,+1,+1,+1).
}
\]

Therefore

\[
\Pi^2=I_6
\]

and the exact half-projectors are

\[
\boxed{
Q_+=\frac12(I_6+\Pi),
\qquad
Q_-=\frac12(I_6-\Pi).
}
\]

Each has rank three.

The equal overlay and half-difference of the two antipodal bivector layers satisfy

\[
\boxed{
\frac{B_++B_-}{2}=Q_+B_+,
}
\]

\[
\boxed{
\frac{B_+-B_-}{2}=Q_-B_+.
}
\]

Thus the paired layers produce exact sector-selective cancellation:

- the half-sum removes the \(\Pi=-1\) three-sector;
- the half-difference removes the \(\Pi=+1\) three-sector.

This is an exact algebraic moire/null mechanism: nonzero parent layers can overlay to zero on an entire three-dimensional subspace.

This parity split is distinct from the Euclidean Hodge self-dual/anti-self-dual split. Both are 3+3 involutive decompositions, but they must not be identified without an explicit bridge.

## 6. Natural 36D relative carrier

Two six-bivector frames have a natural relative operator

\[
\boxed{
M_{36}=B_2B_1^{-1}\in\operatorname{End}(\Lambda^2V).
}
\]

For frames related by a four-dimensional map

\[
E_2=eE_1,
\]

one has exactly

\[
\boxed{
M_{36}=C_2(e).
}
\]

Therefore the 36 coefficients arise without selecting four coordinates from 36 and without mapping tetrahedral labels into the legacy PhaseNav ID space.

This gives a clean interpretation branch:

\[
\boxed{
36=\dim\operatorname{End}(\Lambda^2\mathbb R^4)=6\times6.
}
\]

In this branch the 36 coordinates are representation coefficients of a relative four-dimensional frame transformation, not 36 independent spacetime dimensions.

The broader PhaseNav 36D program may retain other typed 36D carriers; this theorem does not identify them automatically.

## 7. Geometric deformation and the 20-dimensional defect

For a general local four-frame deformation

\[
E_2(x)=e(x)E_1(x),
\qquad
e(x)\in GL(4),
\]

the bivector relation is automatically in the exterior-square image

\[
M_{36}(x)=C_2(e(x)).
\]

Infinitesimally, the geometric tangent sector is

\[
\mathfrak{gl}(4)\cong\mathfrak{co}(3,3),
\]

with dimension 16. The previously derived decomposition

\[
\operatorname{Mat}_6
=
\mathfrak{co}(3,3)\oplus\mathcal Q
\]

therefore reads

\[
\boxed{36=16+20}.
\]

The 20-dimensional \(\mathcal Q\) sector measures failure of a generic raw 6x6 perturbation to be the local exterior-square image of a four-frame deformation.

This is a simplicity/geometric defect, not discarded information.

## 8. Gravity firewall

For the exact undeformed antipodal pair,

\[
e=P
\]

is constant. Therefore it supplies a flat background relation, not gravitational curvature.

Gravity requires a spacetime-dependent admitted frame field

\[
e=e(x)
\]

whose induced metric

\[
g_{\mu\nu}
=
\eta_{IJ}e^I{}_{\mu}e^J{}_{\nu}
\]

has gauge-invariant nonzero curvature and is not merely a global coordinate Jacobian or local Lorentz gauge transformation of a flat metric.

The candidate chain becomes

\[
\boxed{
\text{tetra SIC + positive elapsed lift}
\to
E(x)
\to
B(x)=C_2(E(x))
\to
M_{36}(x)
\to
e(x)
\to
g(x)
\to
\omega_{LC}
\to
R[g].
}
\]

The carrier is now derived. The physical dynamics that determine \(e(x)\), its normalization, and its coupling to matter remain open.

## 9. PhaseNav firewall

The canonical legacy PhaseNav state

\[
(\phi_0,\ldots,\phi_{35})
\]

is **not** retroactively identified with this bivector carrier.

The tetra-null-frame branch constructs its 36 coefficients from

\[
C_2(E_2E_1^{-1})
\]

or an explicitly typed equivalent.

A row-major reshape of legacy Phase36 remains computational only.

## 10. Promotion ledger

- tetra Bloch directions -> four null lifted rays: PASS EXACT
- four null rays linearly independent: PASS EXACT
- rational Hadamard frame E+: PASS EXACT
- det E+ = -16: PASS EXACT
- antipodal layer E- = P E+: PASS EXACT
- relative frame E- E+^-1 = P: PASS EXACT
- six edge bivectors form full Lambda^2 basis: PASS EXACT
- det C2(E+) = det(E+)^3 = -4096: PASS EXACT
- bivector parity Pi = diag(-I3,+I3): PASS EXACT
- Q± = (I±Pi)/2 rank 3: PASS EXACT
- half-sum/half-difference sector cancellation: PASS EXACT
- natural 6x6 relative bivector carrier: PASS EXACT
- arbitrary legacy Phase36 -> this carrier: NOT DERIVED / FORBIDDEN
- constant antipodal pair -> gravity: FAIL / FLAT BACKGROUND
- spacetime-varying frame dynamics from TIR source laws: OPEN
- Newton constant/source normalization: OPEN
- Einstein dynamics and phenomenology: OPEN
