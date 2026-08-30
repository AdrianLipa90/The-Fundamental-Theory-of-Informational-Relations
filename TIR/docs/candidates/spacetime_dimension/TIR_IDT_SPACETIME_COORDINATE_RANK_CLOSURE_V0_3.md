# TIR × IDT Spacetime Coordinate-Rank Closure v0.3

Status: **CANDIDATE / EXACT LOCAL-RANK THEOREM**

This note sharpens `TEMPORAL_TRACE_BINDING_CANONICAL_LIFT_V0_2`.

## 1. Canonical coordinates

For an IDT positive elapsed scale \(\ell>0\) and a TIR qubit state

\[
\rho
=
\frac12
\left(
I+r_x\sigma_x+r_y\sigma_y+r_z\sigma_z
\right),
\qquad
|\mathbf r|<1,
\]

the canonical trace-recovery lift is

\[
X=\ell\rho.
\]

Write

\[
X=x^0I+x^1\sigma_x+x^2\sigma_y+x^3\sigma_z.
\]

Then

\[
\boxed{x^0=\frac{\ell}{2}},
\qquad
\boxed{x^i=\frac{\ell}{2}r_i}.
\]

## 2. Jacobian rank theorem

Define

\[
F:
(\ell,r_x,r_y,r_z)
\mapsto
(x^0,x^1,x^2,x^3).
\]

Its Jacobian is

\[
J_F=
\frac12
\begin{pmatrix}
1&0&0&0\\
r_x&\ell&0&0\\
r_y&0&\ell&0\\
r_z&0&0&\ell
\end{pmatrix}.
\]

Therefore

\[
\boxed{
\det J_F=\frac{\ell^3}{16}.
}
\]

For every admitted positive elapsed scale,

\[
\ell>0
\Longrightarrow
\det J_F>0.
\]

Hence

\[
\boxed{
\operatorname{rank}J_F=4.
}
\]

The IDT scalar scale and the three TIR affine/Bloch coordinates are therefore
locally independent coordinates on the lifted carrier.

This is stronger than the dimension count \(1+3=4\): the actual canonical lift
has full local differential rank.

## 3. Exact inverse in the timelike interior

For \(x^0>0\),

\[
\boxed{
\ell=2x^0,
\qquad
r_i=\frac{x^i}{x^0}.
}
\]

The Bloch interior condition

\[
|\mathbf r|<1
\]

is equivalent to

\[
(x^0)^2-|\mathbf x|^2>0,
\qquad
x^0>0.
\]

Thus

\[
\boxed{
\mathbb R_{>0}\times B^3
\cong
\{x:(x^0)^2-|\mathbf x|^2>0,\ x^0>0\}
}
\]

by an explicit smooth bijection with smooth inverse.

So the product of:
- one positive IDT elapsed coordinate, and
- the three-dimensional TIR normalized-state affine interior

is exactly a four-real-dimensional open cone.

## 4. Boundary rank

For a pure state,

\[
|\mathbf r|=1.
\]

The pure-state direction belongs to \(S^2\), so the boundary parameter space is

\[
\mathbb R_{>0}\times S^2,
\]

with real dimension

\[
\boxed{1+2=3}.
\]

Under the lift,

\[
\det X=0.
\]

Thus the boundary of the four-dimensional positive cone has the expected
three-dimensional null-cone hypersurface rank.

## 5. Group completion

The positive cone itself is not a vector space, but

\[
\operatorname{span}_{\mathbb R}\operatorname{Herm}_+(2)
=
\operatorname{Herm}(2).
\]

Therefore differences of lifted events generate the full tangent/relational
carrier with

\[
\boxed{\dim_{\mathbb R}=4}.
\]

## 6. Minimality inside the primitive two-level observable carrier

The primitive observable carrier has basis

\[
\{I,\sigma_x,\sigma_y,\sigma_z\}.
\]

There is no fifth linearly independent Hermitian \(2\times2\) generator.

Therefore, under the explicit minimality rule that spacetime-base directions
must arise as independent local translation directions of the admitted primitive
Hermitian carrier,

\[
\boxed{D_{\min}=4}.
\]

Any fifth or higher base dimension requires enlarging the primitive carrier or
adding a separately derived translation generator. Gauge, flavour, phase and
PhaseNav fibre coordinates do not alter this count by themselves.

## 7. Remaining physical statement

The mathematics now proves:

\[
\boxed{
(\ell,\rho)\mapsto X=\ell\rho
}
\]

is a full-rank four-dimensional local carrier construction.

The remaining physics gate is narrower:

\[
\boxed{
\ell=c\,t
\text{ from IDT/RFC clock calibration is the event-scale input of this lift}.
}
\]

IDT 01AD already gives the zero-shift temporal coframe

\[
\mathcal E^0=N_Rc\,dt
=c\,d\hat\tau.
\]

Therefore the next bridge should compare the integrated/local coframe scale
directly with \(\operatorname{Tr}X\), without assuming a four-dimensional base.

## 8. Status

| Statement | Status |
|---|---|
| canonical trace-normalized lift | EXACT |
| Jacobian determinant \(\ell^3/16\) | EXACT |
| interior local rank = 4 | EXACT |
| pure boundary dimension = 3 | EXACT |
| interior is future determinant cone | STANDARD / EXACT ALGEBRA |
| full Hermitian group completion dimension = 4 | EXACT |
| minimality within `Herm(2)` | EXACT |
| physical IDT clock scale = event trace scale | OPEN BINDING |
| physical spacetime interpretation | CONDITIONAL |
