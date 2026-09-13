# XF-8A — Tilted autocorrelation / Bochner reduction

Status: `EXACT_AUTOCORRELATION_IDENTITY / POINTWISE_KERNEL_POSITIVITY_EXACT / SLICE_PD_ROUTE_FAIL_NUMERICAL / POSITIVE_DEFINITENESS_GATE_OPEN_RH_EQUIVALENT`

Parent route: XF-8 differential Hermite–Biehler bridge.

## 1. Purpose

XF-8 reduces critical-axis localization to

\[
\Delta_D(x+iy)
=2\,\partial_y|\Xi(x+iy)|^2>0,
\qquad x\in\mathbb R,\quad0<y<\frac12.
\]

XF-8A rewrites that derivative as the Fourier transform of an explicit positive autocorrelation-derivative kernel. The exact reduction survives, while a deliberately stronger slice-by-slice positive-definiteness route is now rejected by a reproducible numerical counterexample.

## 2. Even Xi kernel and exponential tilt

Let

\[
\Phi_e(u):=\Phi(|u|),
\]

where \(\Phi\) is the standard Riemann Xi kernel. Then

\[
\boxed{
\Xi(z)=\int_{\mathbb R}\Phi_e(u)e^{izu}\,du.}
\]

For \(z=x+iy\), define

\[
\boxed{f_y(u):=\Phi_e(u)e^{-yu}.}
\]

The super-exponential Xi-kernel decay gives

\[
\boxed{
\Xi(x+iy)=\int_{\mathbb R}f_y(u)e^{ixu}\,du.}
\]

## 3. Exact autocorrelation representation

Define

\[
C_y(t)
:=
\int_{\mathbb R}
 f_y\!\left(a+\frac t2\right)
 f_y\!\left(a-\frac t2\right)
\,da.
\]

Hence

\[
C_y(t)
=
\int_{\mathbb R}
\Phi_e\!\left(a+\frac t2\right)
\Phi_e\!\left(a-\frac t2\right)
 e^{-2ya}\,da.
\]

The autocorrelation/Fourier identity gives

\[
\boxed{
|\Xi(x+iy)|^2
=
\int_{\mathbb R}C_y(t)e^{ixt}\,dt.}
\]

No zero-location assumption enters this identity.

## 4. Exact transverse derivative kernel

Set

\[
G(a,t)
:=
\Phi_e\!\left(a+\frac t2\right)
\Phi_e\!\left(a-\frac t2\right).
\]

Evenness of \(\Phi_e\) gives

\[
G(-a,t)=G(a,t),
\qquad
G(a,-t)=G(a,t),
\]

and therefore

\[
C_y(t)
=2\int_0^\infty G(a,t)\cosh(2ya)\,da.
\]

Define

\[
H_y(t):=\partial_y C_y(t).
\]

Then

\[
\boxed{
H_y(t)
=4\int_0^\infty
 a\,G(a,t)\sinh(2ya)\,da.}
\]

For \(y>0\), standard positivity of the Xi kernel implies

\[
\boxed{H_y(t)>0\qquad\forall t\in\mathbb R.}
\]

This is pointwise positivity only.

Differentiating the modulus representation yields

\[
\boxed{
\partial_y|\Xi(x+iy)|^2
=
\int_{\mathbb R}H_y(t)e^{ixt}\,dt
=2\int_0^\infty H_y(t)\cos(xt)\,dt.}
\]

Thus

\[
\boxed{
\Delta_D(x+iy)=2\widehat{H_y}(x).}
\]

## 5. Bochner reduction

For fixed \(y>0\), \(H_y\) is real, even, continuous and integrable under the standard Xi-kernel decay. Bochner's theorem gives

\[
\boxed{
H_y\ \text{positive definite}
\iff
\widehat{H_y}(x)\ge0
\quad\forall x.}
\]

The strict localization gate is

\[
\boxed{
\widehat{H_y}(x)>0
\qquad\forall x\in\mathbb R,\quad0<y<\frac12.}
\]

This remains OPEN / RH-equivalent. Pointwise positivity of \(H_y(t)\) does not imply positive definiteness.

## 6. Positive slice mixture

The derivative kernel is a positive mixture

\[
H_y(t)
=
4\int_0^\infty
 a\sinh(2ya)
K_a(t)
\,da,
\]

where

\[
\boxed{
K_a(t)
:=
\Phi_e\!\left(a+\frac t2\right)
\Phi_e\!\left(a-\frac t2\right).}
\]

A stronger sufficient route would have been

\[
K_a\ \text{positive definite for every }a>0
\Longrightarrow
H_y\ \text{positive definite for every }y>0.
\]

That stronger route is falsifiable through

\[
\widehat{K_a}(x)
=
\int_{\mathbb R}K_a(t)e^{ixt}\,dt.
\]

## 7. Slice route counterexample

The finite Xi-kernel evaluator now exposes `xi_autocorrelation_slice_transform` with explicit kernel-series and integration cutoffs.

At

\[
\boxed{a=0.1,\qquad x=12}
\]

using

- 50 decimal digit working precision in the regression test,
- 12 Xi-kernel series terms,
- symmetric transform cutoff \(|t|\le4\),

the numerical slice transform is negative, with a stable value near

\[
\boxed{
\widehat{K_{0.1}}(12)
\approx-4.28258\times10^{-5}.}
\]

The regression test requires only

\[
\widehat{K_{0.1}}(12)<-10^{-5},
\]

leaving substantial separation from zero.

Verdict:

\[
\boxed{
\texttt{ALL\_SLICES\_K\_A\_POSITIVE\_DEFINITE = FAIL\_NUMERICAL\_COUNTEREXAMPLE}.}
\]

This rejects only the stronger slice-by-slice sufficient route. It does **not** reject positive definiteness of the integrated kernel \(H_y\), because a positive weighted mixture can have a Fourier transform with a different sign structure from individual slices.

A rigorous interval/error-bound certificate for this finite numerical witness remains an optional validation upgrade; the exact XF-8A identities do not depend on the witness.

## 8. Consequence for the proof search

The proof target cannot be reduced to independent positivity of every \(K_a\) slice. The correlation in the positive mixture over \(a\) is essential.

The surviving exact target is therefore

\[
\boxed{
H_y(t)
=4\int_0^\infty a\sinh(2ya)K_a(t)\,da
\quad\text{is positive definite for }0<y<\frac12.}
\]

Equivalently,

\[
\boxed{
\widehat{H_y}(x)>0
\qquad\forall x\in\mathbb R,\ 0<y<\frac12.}
\]

This is the same strict differential-Hermite–Biehler gate from XF-8, now expressed as a one-dimensional positive-definiteness problem.

## 9. Relation to the horizon picture

In the Xi coordinate

\[
z=x+iy,
\]

the critical line is the boundary \(y=0\), and

\[
0<|y|<\frac12
\]

is the image of the open critical strip away from that boundary.

XF-8 gives, at every simple zero,

\[
\Xi(z_0)=0
\Longrightarrow
\Theta_D(z_0)=-1=e^{i\pi}.
\]

XF-8A says that exclusion of an interior zero is equivalent to maintaining a strict positive spectral margin for the integrated derivative kernel. Thus the boundary language becomes operational only through the positive-definiteness gate; geometry alone does not supply it.

## 10. Promotion ledger

- `XI_EVEN_KERNEL_FOURIER_REPRESENTATION`: `STANDARD`
- `TILTED_KERNEL_F_Y`: `EXACT_DEFINITION`
- `XI_MODULUS_AS_TILTED_AUTOCORRELATION_FOURIER_TRANSFORM`: `EXACT`
- `H_Y = D_Y C_Y`: `EXACT`
- `H_Y(t) > 0 FOR y>0`: `EXACT_FROM_STANDARD_KERNEL_POSITIVITY`
- `D_Y |Xi|^2 = FOURIER(H_Y)`: `EXACT`
- `H_Y POSITIVE_DEFINITE <-> FOURIER(H_Y) >= 0`: `STANDARD_BOCHNER_EQUIVALENCE`
- `STRICT_FOURIER_POSITIVITY_ON_0<y<1/2`: `OPEN / RH_EQUIVALENT`
- `ALL_SLICES_K_A_POSITIVE_DEFINITE`: `FAIL_NUMERICAL_COUNTEREXAMPLE`
- `SLICE_COUNTEREXAMPLE_INTERVAL_CERTIFICATE`: `OPEN_VALIDATION_UPGRADE`
- `RIEMANN_HYPOTHESIS`: `OPEN`

## 11. Next target

The next admissible route must retain the \(a\)-integration before imposing a Fourier-sign condition. Candidate directions are:

1. prove positive definiteness of the full weighted mixture \(H_y\) directly;
2. find a Gram/operator representation of \(H_y\) that survives the signed slice spectrum;
3. combine the XF-6/XF-7 signed core-tail estimates before Fourier transformation;
4. derive a variation-diminishing or total-positivity property for the integrated kernel rather than for each slice.

No RH promotion is made.
