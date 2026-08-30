# XF-4 — Wiener–Laguerre scalar form of the correlation-kernel criterion

Status: **STANDARD equivalence / OPEN global positivity criterion**

Parent route: XF-3, Dimitrov–Xu correlation-kernel density criterion.

Primary source: D. K. Dimitrov and Y. Xu, *Wronskians of Fourier and Laplace Transforms*, Trans. Amer. Math. Soc. 369 (2017), arXiv:1606.05011.

## 1. Input objects

Use the standard even Riemann kernel `Phi` and the completed real-entire Xi function in the Fourier convention

\[
\Xi(z)=\int_{\mathbb R}\Phi(t)e^{-izt}\,dt.
\]

For the Dimitrov–Xu second correlation kernel,

\[
\nu_2(t)=\int_{\mathbb R}(t-2s)^2\Phi(t-s)\Phi(s)\,ds,
\]

and for

\[
0<|y|<\frac12,
\]

define

\[
\Phi_{2,y}(t)=\cosh(ty)\,\nu_2(t).
\]

Dimitrov–Xu Theorem 1.1 gives the external STANDARD equivalence

\[
\mathrm{RH}
\iff
\forall\,0<|y|<\frac12:\quad
\overline{\operatorname{span}\mathcal T(\Phi_{2,y})}^{L^1(\mathbb R)}
=L^1(\mathbb R).
\]

## 2. The scalar

For real `x` and admissible `y`, define

\[
\boxed{
Q_\Xi(x,y)
:=
|\Xi'(x+iy)|^2
-
\operatorname{Re}\!\left[
\Xi(x+iy)\overline{\Xi''(x+iy)}
\right].
}
\]

Writing

\[
\Xi(x+iy)=\phi(x,y)+i\psi(x,y),
\]

the Cauchy–Riemann relations give the classical Jensen/Laguerre identity

\[
Q_\Xi(x,y)
=
\phi_x(x,y)^2-\phi(x,y)\phi_{xx}(x,y)
+
\psi_x(x,y)^2-\psi(x,y)\psi_{xx}(x,y).
\]

With the second Wronskian

\[
W_2(f;x)=f(x)f''(x)-f'(x)^2,
\]

this is

\[
Q_\Xi(x,y)
=-W_2(\phi(\cdot,y);x)-W_2(\psi(\cdot,y);x).
\]

## 3. Fourier identity

Dimitrov–Xu Theorem 1.3 / Theorem 2.5 identifies the Wronskians with Fourier transforms of the corresponding correlation kernels. Their Section 3 then combines the real and imaginary parts to obtain

\[
W_2(\phi(\cdot,y);x)+W_2(\psi(\cdot,y);x)
=
-\mathcal F\!\left[\cosh(\cdot y)\nu_2\right](x).
\]

Therefore

\[
\boxed{
Q_\Xi(x,y)=\mathcal F[\Phi_{2,y}](x).
}
\]

Repository status:

- `phi2y_fourier_equals_xi_wiener_laguerre_scalar`: **STANDARD_PASS**.

## 4. Wiener reduction

For each fixed admissible `y`, `Phi_{2,y}` belongs to the class used by the Dimitrov–Xu theorem. Wiener's `L^1` translation theorem gives

\[
\overline{\operatorname{span}\mathcal T(\Phi_{2,y})}^{L^1}=L^1
\iff
\mathcal F[\Phi_{2,y}](x)\neq0
\quad\forall x\in\mathbb R.
\]

Using the boxed Fourier identity,

\[
\text{translation density}
\iff
Q_\Xi(x,y)\neq0
\quad\forall x\in\mathbb R.
\]

The same Dimitrov–Xu argument establishes strict positivity at the origin for every admissible nonzero `y`:

\[
Q_\Xi(0,y)>0.
\]

Since `Q_Xi(·,y)` is a continuous real-valued function on the real axis, global nonvanishing fixes its sign. Hence

\[
Q_\Xi(x,y)\neq0\ \forall x
\iff
Q_\Xi(x,y)>0\ \forall x.
\]

Thus for every fixed `0<|y|<1/2`,

\[
\boxed{
\overline{\operatorname{span}\mathcal T(\Phi_{2,y})}^{L^1}=L^1
\iff
Q_\Xi(x,y)>0\quad\forall x\in\mathbb R.
}
\]

Combining this with Dimitrov–Xu Theorem 1.1 yields the sharpened scalar criterion

\[
\boxed{
\mathrm{RH}
\iff
\forall\,y\in\left(-\frac12,\frac12\right)\setminus\{0\}
\ \forall x\in\mathbb R:\quad
Q_\Xi(x,y)>0.
}
\]

The equivalence is classified **STANDARD**. The universally quantified strict-positivity premise is classified

`OPEN_RH_EQUIVALENT_CRITERION`.

## 5. Executable interface

`src/critical_axis/correlation_kernel.py` exposes

```text
xi_wiener_laguerre_scalar(x, y)
```

with a fail-closed domain guard

\[
0<|y|<\frac12.
\]

Finite evaluations are classified `NUMERICAL_DIAGNOSTIC`. Promotion of the global claim requires an analytic argument carrying both universal quantifiers.

The regression suite checks:

1. `y -> -y` symmetry at reference points;
2. strict positivity at `x=0` for several admissible `y` values;
3. fail-closed behavior at `y=0` and `|y|>=1/2`;
4. solver separation between the STANDARD Fourier identity and the OPEN global positivity condition.

## 6. Falsification surface

The criterion has a direct falsification surface. A certified pair

\[
(x_*,y_*),\qquad x_*\in\mathbb R,\quad0<|y_*|<\frac12,
\]

with

\[
Q_\Xi(x_*,y_*)\le0
\]

would force, by continuity and `Q_Xi(0,y_*)>0`, a real zero of the Fourier transform of `Phi_{2,y_*}`. That would break the Wiener density condition at that `y_*`.

Floating-point scans are discovery instruments. A theorem-level falsification requires certified error control or exact analysis.

## 7. XF-4 frontier

The new frontier is the single global inequality

\[
\boxed{
Q_\Xi(x,y)>0
\quad
\text{for every }x\in\mathbb R,
\quad0<|y|<\frac12.
}
\]

This form replaces an infinite-dimensional density statement by a pointwise scalar sign problem while preserving exact equivalence. The next research step is to seek a structural representation of `Q_Xi` whose positivity can be certified globally without importing RH as a premise.
