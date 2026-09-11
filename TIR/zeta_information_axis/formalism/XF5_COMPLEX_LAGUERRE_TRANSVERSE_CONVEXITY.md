# XF-5 — Complex Laguerre transverse-convexity closure

Status: **STANDARD equivalence / OPEN global convexity criterion**

Parent route: XF-4 Wiener–Laguerre scalar.

Primary theorem provenance:

- G. Csordas and R. S. Varga, *Necessary and sufficient conditions and the Riemann hypothesis*, Advances in Applied Mathematics 11 (1990), 328–357, DOI 10.1016/0196-8858(90)90013-O.
- G. Csordas and A. Escassut, *The Laguerre inequality and the distribution of zeros of entire functions*, Annales Mathématiques Blaise Pascal 12 (2005), 331–345, DOI 10.5802/ambp.210.

## 1. Standard Xi setting

Write

\[
\Xi(z)=\xi\!\left(\frac12+iz\right).
\]

The completed Xi function is a real entire function of order one. Its zeros are the images of the nontrivial zeta zeros. Since the classical zero-free regions place those zeros in

\[
0<\Re s<1,
\]

the corresponding Xi zeros lie in the horizontal strip

\[
|\Im z|<\frac12.
\]

Thus Xi belongs to the standard strip class used by the complex Laguerre criterion with strip parameter `A=1/2`.

Repository status:

- `xi_strip_class_s_half`: **STANDARD_PASS**.

## 2. XF-4 scalar

For

\[
z=x+iy,
\]

define

\[
Q_\Xi(x,y)
=
|\Xi'(z)|^2
-
\operatorname{Re}\!\left[
\Xi(z)\overline{\Xi''(z)}
\right].
\]

This is the same scalar exposed by XF-4.

## 3. Exact transverse-curvature identity

Let

\[
M(x,y)=|\Xi(x+iy)|^2.
\]

Because Xi is real entire,

\[
\overline{\Xi(x+iy)}=\Xi(x-iy).
\]

Using

\[
\partial_y\Xi(x+iy)=i\Xi'(x+iy),
\qquad
\partial_y^2\Xi(x+iy)=-\Xi''(x+iy),
\]

and the conjugate relations, direct differentiation gives

\[
\partial_y^2 M(x,y)
=
2|\Xi'(x+iy)|^2
-2\operatorname{Re}\!\left[
\Xi(x+iy)\overline{\Xi''(x+iy)}
\right].
\]

Therefore

\[
\boxed{
\partial_y^2|\Xi(x+iy)|^2
=2Q_\Xi(x,y).
}
\]

Repository status:

- `xi_transverse_curvature_equals_twice_laguerre_scalar`: **EXACT_PASS**.

## 4. Classical complex Laguerre criterion

Csordas–Escassut Theorem 2.4 records the complex Laguerre criterion for a real entire function `f` in the strip class `S(A)`:

\[
f\in\mathcal{LP}
\iff
|f'(z)|^2
\ge
\operatorname{Re}\!\left[f(z)\overline{f''(z)}\right]
\qquad
\forall z\in\mathbb C.
\]

The same paper states the geometric interpretation explicitly: the inequality is equivalent to convexity of

\[
|f(x+iy)|^2
\]

as a function of `y` for every fixed real `x`.

For Xi this yields

\[
\Xi\in\mathcal{LP}
\iff
Q_\Xi(x,y)\ge0
\quad\forall x,y\in\mathbb R
\]

and therefore, by the boxed identity,

\[
\boxed{
\Xi\in\mathcal{LP}
\iff
\partial_y^2|\Xi(x+iy)|^2\ge0
\quad\forall x,y\in\mathbb R.
}
\]

## 5. RH equivalence

For the Riemann Xi function,

\[
\mathrm{RH}
\iff
\Xi\in\mathcal{LP},
\]

because membership in the Laguerre–Pólya class is exactly the all-real-zero condition for this real entire function.

Combining this with the complex Laguerre criterion gives

\[
\boxed{
\mathrm{RH}
\iff
\forall x,y\in\mathbb R:\quad
\partial_y^2|\Xi(x+iy)|^2\ge0.
}
\]

Equivalently,

\[
\boxed{
\mathrm{RH}
\iff
\forall x,y\in\mathbb R:\quad
Q_\Xi(x,y)\ge0.
}
\]

The equivalence is classified **STANDARD**. The universally quantified premise is classified

`OPEN_RH_EQUIVALENT_CRITERION`.

## 6. Relation to XF-4

XF-4 uses the Dimitrov–Xu/Wiener route and yields

\[
\mathrm{RH}
\iff
Q_\Xi(x,y)>0
\quad
\forall x\in\mathbb R,
\quad0<|y|<\frac12.
\]

XF-5 supplies an independent classical theorem path:

\[
\mathrm{RH}
\iff
Q_\Xi(x,y)\ge0
\quad
\forall x,y\in\mathbb R.
\]

The difference between strict positivity and nonnegativity is material on the real axis. The complex Laguerre criterion permits equality there; for a Laguerre–Pólya function the real-axis Laguerre expression can vanish at a multiple real zero. The XF-4 open-strip criterion excludes `y=0` and uses strict positivity.

## 7. Executable interface

`src/critical_axis/correlation_kernel.py` exposes

```text
xi_transverse_modulus_curvature(x, y)
```

with

\[
\texttt{xi\_transverse\_modulus\_curvature}(x,y)
=2Q_\Xi(x,y).
\]

Regression tests independently compare this analytic expression with a direct second derivative in the transverse coordinate `y`.

Finite evaluations remain `NUMERICAL_DIAGNOSTIC`. The global sign criterion requires analytic control over both real variables.

## 8. XF-5 frontier

The research frontier is now the geometric inequality

\[
\boxed{
\partial_y^2|\Xi(x+iy)|^2\ge0
\quad
\text{for every }(x,y)\in\mathbb R^2.
}
\]

The useful next question is structural: identify a representation of the transverse curvature whose nonnegativity follows from an independently provable positivity, total-positivity, operator, or kernel property.
