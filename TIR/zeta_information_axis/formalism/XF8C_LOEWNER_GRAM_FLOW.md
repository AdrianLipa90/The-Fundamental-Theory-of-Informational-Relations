# XF-8C — Translation-Gram Loewner flow

Status: `EXACT_GRAM_IDENTITY / NONSTRICT_MARGIN_SUFFICES / RH_EQUIVALENT_LOEWNER_GATE / RH_OPEN`

Parent routes: XF-8 differential Hermite–Biehler bridge, XF-8A tilted-autocorrelation reduction, XF-8B Cayley–Schur/Pick gate.

## 1. Purpose

XF-8A writes

\[
\partial_y|\Xi(x+iy)|^2=\widehat{H_y}(x),
\]

where

\[
H_y(t)=\partial_y C_y(t)
\]

and \(C_y\) is the autocorrelation of the exponentially tilted Xi kernel. The previous formulation emphasized the stronger strict condition

\[
\widehat{H_y}(x)>0.
\]

XF-8C sharpens the gate: **strict positivity is not required**. Global nonnegativity already excludes every off-axis zero because the modulus is nonnegative and Xi is a nonzero entire function.

It then rewrites positive definiteness of \(H_y\) as monotonicity, in Loewner order, of a canonical family of finite translation-Gram matrices.

## 2. Tilted kernel and autocorrelation

Let

\[
\Phi_e(u)=\Phi(|u|),
\qquad
f_y(u)=\Phi_e(u)e^{-yu}.
\]

Define

\[
C_y(t)
:=
\int_{\mathbb R}f_y(u+t)f_y(u)\,du.
\]

This is equivalent to the centered XF-8A formula after the change of variable \(u=a-t/2\).

The Fourier identity is

\[
\boxed{
|\Xi(x+iy)|^2
=\widehat{C_y}(x).
}
\]

Because \(C_y\) is an autocorrelation, it is positive definite for every real \(y\) for which the tilted kernel is square integrable; the super-exponential Xi-kernel decay supplies this for every finite \(y\).

## 3. Exact translation-Gram identity

Choose any finite set of real translations

\[
T=(t_1,\ldots,t_n)
\]

and define

\[
\boxed{
G_y(T)_{jk}:=C_y(t_j-t_k).
}
\]

For arbitrary coefficients \(c_1,\ldots,c_n\in\mathbb C\),

\[
\begin{aligned}
\sum_{j,k}c_j\overline{c_k}C_y(t_j-t_k)
&=
\int_{\mathbb R}
\left|\sum_j c_j f_y(u+t_j)\right|^2du\\
&\ge0.
\end{aligned}
\]

Hence

\[
\boxed{G_y(T)\succeq0}
\]

for every finite translation set. This positivity is unconditional and is simply the Gram structure of translated tilted kernels.

## 4. Derivative Gram matrix

Differentiate entrywise in \(y\). Since

\[
H_y(t)=\partial_y C_y(t),
\]

we have

\[
\boxed{
\dot G_y(T)_{jk}=H_y(t_j-t_k).
}
\]

Therefore, for every fixed finite translation set,

\[
\boxed{
H_y\text{ is positive definite}
\iff
\dot G_y(T)\succeq0\ \text{for every }T.
}
\]

Equivalently,

\[
\boxed{
G_{y_2}(T)\succeq G_{y_1}(T)
\qquad(y_2\ge y_1)
}
\]

for every finite translation set if and only if the derivative kernel is positive definite throughout the interval. Thus the remaining spectral sign problem is a **Loewner-monotonicity problem for a family of correlation Gram matrices**.

## 5. Non-strict transverse monotonicity already excludes interior zeros

Set

\[
M_x(y):=|\Xi(x+iy)|^2\ge0.
\]

Assume only

\[
\boxed{
\partial_yM_x(y)\ge0
\qquad
\forall x\in\mathbb R,
\quad0<y<\frac12.
}
\]

Suppose there were an off-axis nontrivial zero

\[
\Xi(x_0+iy_0)=0,
\qquad0<y_0<\frac12.
\]

Then

\[
M_{x_0}(y_0)=0.
\]

Since \(M_{x_0}\ge0\) and is nondecreasing on \([0,y_0]\),

\[
0\le M_{x_0}(y)\le M_{x_0}(y_0)=0
\]

for every \(0\le y\le y_0\). Hence

\[
M_{x_0}(y)=0
\]

on a nontrivial interval, so \(\Xi\) vanishes on a line segment. By the identity theorem for entire functions this would force

\[
\Xi\equiv0,
\]

which is false.

Therefore

\[
\boxed{
\partial_y|\Xi(x+iy)|^2\ge0
\text{ on }0<y<\frac12
\Longrightarrow
\mathrm{RH}.
}
\]

The lower half-strip follows by Schwarz symmetry.

## 6. Converse under RH

Under RH, Xi belongs to the Laguerre–Pólya class. The standard complex Laguerre criterion used in XF-5 gives

\[
Q_\Xi(x,y)\ge0
\qquad\forall x,y\in\mathbb R.
\]

Since

\[
\partial_y^2|\Xi(x+iy)|^2=2Q_\Xi(x,y)
\]

and the modulus is even in \(y\),

\[
\partial_y|\Xi(x)|^2=0.
\]

Consequently

\[
\partial_y|\Xi(x+iy)|^2\ge0
\qquad(y>0).
\]

Combining both directions gives the sharpened equivalence

\[
\boxed{
\mathrm{RH}
\iff
\partial_y|\Xi(x+iy)|^2\ge0
\quad
\forall x\in\mathbb R,
\ 0<y<\frac12.
}
\]

Strict positivity is a stronger property than required for zero exclusion.

## 7. Bochner / Loewner equivalence

XF-8A gives

\[
\partial_y|\Xi(x+iy)|^2=\widehat{H_y}(x).
\]

For each fixed \(y\), Bochner's theorem gives

\[
H_y\text{ positive definite}
\iff
\widehat{H_y}(x)\ge0\quad\forall x.
\]

Therefore the surviving RH gate can be written exactly as

\[
\boxed{
\mathrm{RH}
\iff
H_y\text{ is positive definite for every }0<y<\frac12
}
\]

or equivalently

\[
\boxed{
\mathrm{RH}
\iff
G_y(T)\text{ is Loewner-nondecreasing in }y
\text{ for every finite translation set }T.
}
\]

This is a global, correlation-preserving formulation. It does not decompose the Xi cancellation into independently positive local blocks.

## 8. Finite Gram hierarchy

The Loewner gate can be resolved by matrix size.

### n = 1

The one-point derivative Gram condition is simply

\[
H_y(0)\ge0,
\]

which is already exact and in fact strict for \(y>0\) from the positive XF-8A integral.

### n = 2

For translations \(0,t\),

\[
\dot G_y
=
\begin{pmatrix}
H_y(0)&H_y(t)\\
H_y(t)&H_y(0)
\end{pmatrix}.
\]

Because XF-8A gives \(H_y(t)>0\), the two-point PSD gate reduces to

\[
\boxed{H_y(t)\le H_y(0).}
\]

A sufficient condition is global log-concavity of the even Xi kernel. Indeed, midpoint log-concavity gives

\[
\Phi_e\!\left(a+\frac t2\right)
\Phi_e\!\left(a-\frac t2\right)
\le
\Phi_e(a)^2,
\]

and integration against the positive weight \(4a\sinh(2ya)\) yields

\[
H_y(t)\le H_y(0).
\]

This implication is classified `EXACT_CONDITIONAL_ON_GLOBAL_EVEN_LOG_CONCAVITY`. It does not promote any external preprint claim to a theorem and does not address higher Gram sizes.

### n >= 3

The remaining principal minors contain genuinely multi-translation correlations. Pairwise control is insufficient in general for positive semidefiniteness of every finite Gram matrix. Thus TP2/log-concavity can at most close the two-point layer; the full RH gate requires the entire finite-Gram hierarchy or an operator theorem that closes all matrix sizes at once.

## 9. Horizon interpretation

The critical line is the boundary \(y=0\). The open region

\[
0<y<\frac12
\]

is the potential off-axis sector.

XF-8C replaces the stronger demand of strictly increasing spectral mass with the exact minimal statement:

\[
\boxed{
\text{the translation-correlation Gram geometry must never decrease as one moves away from }y=0.
}
\]

If that Loewner flow holds, an interior zero cannot appear because doing so would force the nonnegative scalar mode \(|\Xi(x+iy)|^2\) to collapse to zero after being nondecreasing from the boundary. The only alternative would be a continuum of zeros, forbidden for nonzero entire Xi.

## 10. Promotion ledger

- `C_Y_IS_AUTOCORRELATION`: `EXACT`
- `G_Y_TRANSLATION_GRAM_PSD`: `EXACT`
- `D_Y G_Y = H_Y_GRAM`: `EXACT`
- `H_Y_PD <-> G_Y_LOEWNER_NONDECREASING`: `EXACT`
- `NONNEGATIVE_TRANSVERSE_DERIVATIVE_EXCLUDES_INTERIOR_ZERO`: `EXACT`
- `RH <-> NONNEGATIVE_TRANSVERSE_DERIVATIVE_ON_OPEN_HALF_STRIP`: `STANDARD_INPUTS + EXACT_DERIVATION`
- `RH <-> H_Y_PD_FOR_ALL_0<Y<1/2`: `STANDARD_BOCHNER + EXACT_DERIVATION`
- `RH <-> ALL_TRANSLATION_GRAMS_LOEWNER_NONDECREASING`: `EXACT_REFORMULATION`
- `GLOBAL_EVEN_LOG_CONCAVITY -> N2_DERIVATIVE_GRAM_PSD`: `EXACT_CONDITIONAL`
- `N_GE_3_GRAM_HIERARCHY`: `OPEN / RH_EQUIVALENT_IN_THE_LIMIT`
- `RIEMANN_HYPOTHESIS`: `OPEN`

## 11. Next proof target

The next admissible target is no longer strict Fourier positivity. It is the weaker matrix inequality

\[
\boxed{
\dot G_y(T)\succeq0
\qquad
\forall T,\quad0<y<\frac12.
}
\]

A decisive route would be an operator factorization of the form

\[
\dot G_y(T)=B_y(T)^*B_y(T)
\]

valid for arbitrary finite translation sets, derived directly from the Xi/theta kernel without assuming real Xi zeros. Such a factorization would close all Gram levels simultaneously. Until then, RH remains OPEN.
