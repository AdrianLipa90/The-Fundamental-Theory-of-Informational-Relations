# XF-8A — Tilted autocorrelation / Bochner reduction

Status: `EXACT_AUTOCORRELATION_IDENTITY / POINTWISE_KERNEL_POSITIVITY_EXACT / POSITIVE_DEFINITENESS_GATE_OPEN_RH_EQUIVALENT`

Parent route: XF-8 differential Hermite–Biehler bridge.

## 1. Purpose

XF-8 reduces the Riemann-hypothesis localization problem to the strict upper-strip margin

\[
\Delta_D(x+iy)
=2\,\partial_y|\Xi(x+iy)|^2>0,
\qquad x\in\mathbb R,\quad 0<y<\frac12.
\]

This note rewrites that derivative as the Fourier transform of an explicit positive autocorrelation-derivative kernel. The resulting statement is exact, but the missing positive-definiteness property remains OPEN / RH-equivalent.

## 2. Even Xi kernel and exponential tilt

Let

\[
\Phi_e(u):=\Phi(|u|),\qquad u\in\mathbb R,
\]

where \(\Phi\) is the standard Riemann Xi kernel used in XF-1. Then

\[
\boxed{
\Xi(z)=\int_{-\infty}^{\infty}\Phi_e(u)e^{izu}\,du.
}
\]

For

\[
z=x+iy,
\]

define the tilted kernel

\[
\boxed{
f_y(u):=\Phi_e(u)e^{-yu}.}
\]

The super-exponential decay of the Riemann kernel makes this transform well defined for finite real \(y\), and

\[
\boxed{
\Xi(x+iy)=\int_{\mathbb R}f_y(u)e^{ixu}\,du.}
\]

## 3. Exact autocorrelation representation of the modulus

Define the symmetric autocorrelation

\[
C_y(t)
:=
\int_{\mathbb R}
 f_y\!\left(a+\frac t2\right)
 f_y\!\left(a-\frac t2\right)
\,da.
\]

Direct substitution gives

\[
C_y(t)
=
\int_{\mathbb R}
\Phi_e\!\left(a+\frac t2\right)
\Phi_e\!\left(a-\frac t2\right)
 e^{-2ya}\,da.
\]

By the autocorrelation/Fourier identity,

\[
\boxed{
|\Xi(x+iy)|^2
=
\int_{\mathbb R}C_y(t)e^{ixt}\,dt.
}
\]

No zero location is used in this identity.

## 4. Evenness in the autocorrelation coordinate

Set

\[
G(a,t)
:=
\Phi_e\!\left(a+\frac t2\right)
\Phi_e\!\left(a-\frac t2\right).
\]

Because \(\Phi_e\) is even,

\[
G(-a,t)=G(a,t),
\qquad
G(a,-t)=G(a,t).
\]

Therefore

\[
\boxed{
C_y(t)
=2\int_0^\infty G(a,t)\cosh(2ya)\,da.}
\]

In particular, for real \(t\), \(C_y(t)\) is real, even, and positive.

## 5. Exact transverse derivative kernel

Differentiate under the integral sign and define

\[
H_y(t)
:=\partial_y C_y(t).
\]

Then

\[
\boxed{
H_y(t)
=4\int_0^\infty
 a\,G(a,t)\sinh(2ya)\,da.}
\]

For \(y>0\), standard positivity of the Riemann Xi kernel implies

\[
\boxed{
H_y(t)>0
\qquad\text{for every real }t.}
\]

This is an exact pointwise positivity statement. It is not yet the RH-level Fourier-sign statement.

Differentiating the modulus representation gives

\[
\boxed{
\partial_y|\Xi(x+iy)|^2
=
\int_{\mathbb R}H_y(t)e^{ixt}\,dt
=2\int_0^\infty H_y(t)\cos(xt)\,dt.}
\]

Hence the XF-8 margin is

\[
\boxed{
\Delta_D(x+iy)
=2\widehat{H_y}(x),}
\]

with the Fourier convention used above.

## 6. Exact Bochner reduction

For fixed \(y>0\), \(H_y\) is real, even, continuous and integrable under the standard Xi-kernel decay. Therefore Bochner's theorem applies in the usual Fourier form.

The nonnegative-margin condition

\[
\partial_y|\Xi(x+iy)|^2\ge0
\qquad\forall x\in\mathbb R
\]

is equivalent to positive definiteness of \(H_y\):

\[
\boxed{
H_y\ \text{positive definite}
\iff
\widehat{H_y}(x)\ge0
\quad\forall x.}
\]

The strict XF-8 localization gate requires the stronger spectral statement

\[
\boxed{
\widehat{H_y}(x)>0
\qquad\forall x\in\mathbb R,\quad0<y<\frac12.}
\]

Because this strict condition is sufficient to exclude every off-axis nontrivial zero, its universal proof remains RH-level.

## 7. What this reduction gains

The previous two-dimensional core/tail formulation asks for cancellation control directly in the \((a,b)\) plane. XF-8A instead packages the same transverse derivative into one real even kernel \(H_y(t)\).

Two facts are now separated cleanly:

1. **EXACT:** \(H_y(t)>0\) pointwise for \(y>0\).
2. **OPEN / RH-EQUIVALENT:** \(H_y\) is positive definite with strictly positive Fourier transform throughout the critical-strip range.

Pointwise positivity alone does not imply positive definiteness, so no RH promotion follows from Section 5.

## 8. Slice-mixture sufficient route

The derivative kernel is a positive mixture

\[
H_y(t)
=
4\int_0^\infty
 a\sinh(2ya)
\underbrace{
\Phi_e\!\left(a+\frac t2\right)
\Phi_e\!\left(a-\frac t2\right)
}_{K_a(t)}
\,da.
\]

Thus a sufficient, but deliberately stronger, route would be:

\[
\boxed{
K_a(t)\ \text{positive definite for every }a>0
\Longrightarrow
H_y(t)\ \text{positive definite for every }y>0.}
\]

No such global slice theorem is asserted here. It is recorded only as an independently falsifiable sufficient route.

The slice transform

\[
\widehat{K_a}(x)
=
\int_{\mathbb R}
\Phi_e\!\left(a+\frac t2\right)
\Phi_e\!\left(a-\frac t2\right)
e^{ixt}\,dt
\]

is the natural object for testing this route. Failure of slice positivity would not invalidate XF-8A, because positive mixtures can remain positive definite even when individual slices are not.

## 9. Relation to the "horizon" picture

In the Xi coordinate

\[
z=x+iy,
\]

the critical line is the boundary \(y=0\), while

\[
0<|y|<\frac12
\]

is the image of the open critical strip away from that boundary.

XF-8 gives

\[
\Xi(z_0)=0
\Longrightarrow
\Theta_D(z_0)=-1=e^{i\pi}
\]

at every simple zero. XF-8A rewrites the required exclusion of interior zeros as the strict Fourier-positivity condition

\[
\boxed{
0<y<\frac12
\Longrightarrow
\widehat{H_y}(x)>0\quad\forall x.}
\]

So the "boundary" interpretation is mathematically precise only after this positivity gate is supplied; the gate is not derived from the geometric language itself.

## 10. Promotion ledger

- `XI_EVEN_KERNEL_FOURIER_REPRESENTATION`: `STANDARD`
- `TILTED_KERNEL_F_Y`: `EXACT_DEFINITION`
- `XI_MODULUS_AS_TILTED_AUTOCORRELATION_FOURIER_TRANSFORM`: `EXACT`
- `H_Y = D_Y C_Y`: `EXACT`
- `H_Y(t) > 0 FOR y>0`: `EXACT_FROM_STANDARD_KERNEL_POSITIVITY`
- `D_Y |Xi|^2 = FOURIER(H_Y)`: `EXACT`
- `H_Y POSITIVE_DEFINITE <-> FOURIER(H_Y) >= 0`: `STANDARD_BOCHNER_EQUIVALENCE`
- `STRICT_FOURIER_POSITIVITY_ON_0<y<1/2`: `OPEN / RH_EQUIVALENT`
- `ALL_SLICES_K_A_POSITIVE_DEFINITE`: `OPEN_SUFFICIENT_ROUTE`
- `RIEMANN_HYPOTHESIS`: `OPEN`

## 11. Next falsifiable target

Before attempting another global proof, test the stronger slice route independently:

\[
\widehat{K_a}(x)\stackrel{?}{\ge}0
\qquad\forall a>0,\ x\in\mathbb R.
\]

If a counterexample exists, discard the slice-wise route while retaining the exact positive-mixture representation for \(H_y\). If it survives aggressive numerical and analytic audit, seek an independent positive-definiteness theorem rather than inferring it from pointwise positivity.
