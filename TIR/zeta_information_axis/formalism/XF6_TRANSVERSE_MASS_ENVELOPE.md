# XF-6 — Transverse Mass Envelope and Positive-Core Gate

## Status

- Repository Xi-kernel normalization: **STANDARD**
- XF-5 correlated mass definition: **EXACT**
- XF-6 positive central curvature corridor: **EXACT**
- Log-concavity ⇒ transverse centre dominance: **EXACT_CONDITIONAL**
- Log-concavity ⇒ strict decay in `|b|`: **EXACT_CONDITIONAL**
- Certified curvature floor ⇒ Gaussian transverse envelope: **EXACT_CONDITIONAL**
- Gershon v2 global strict log-concavity of the Xi kernel: **EXTERNAL_PREPRINT_CLAIM**
- TP∞ / Laguerre–Pólya closure: **OPEN**
- Global positive-core versus oscillatory-tail domination: **OPEN_RH_EQUIVALENT_ROUTE**
- Riemann hypothesis: **OPEN**

## 1. XF-5 starting surface

XF-5 writes the Wiener–Laguerre scalar as

\[
Q_\Xi(x,y)
=
4\iint_{a>|b|} M(a,b)L_{x,y}(a,b)\,da\,db,
\]

with

\[
M(a,b)=\Phi(a+b)\Phi(a-b),
\]

and

\[
L_{x,y}(a,b)
=
a^2\cos(2xb)\cosh(2ya)
+b^2\cos(2xa)\cosh(2yb).
\]

The global sign condition

\[
Q_\Xi(x,y)>0,
\qquad x\in\mathbb R,
\qquad 0<|y|<\frac12,
\]

retains **OPEN_RH_EQUIVALENT_CRITERION** status.

## 2. Exact positive central corridor

For `x ≠ 0`, impose

\[
|b|\le r_+(x,a)
:=
\min\!\left(\frac a2,\frac{\pi}{8|x|}\right).
\]

Then

\[
|2xb|\le\frac\pi4,
\qquad
\cos(2xb)\ge\frac1{\sqrt2}.
\]

Because

\[
\cos(2xa)\ge -1
\]

and, for `|b|<a`,

\[
\cosh(2|y||b|)\le\cosh(2|y|a),
\]

we obtain

\[
\begin{aligned}
L_{x,y}(a,b)
&\ge
\frac{a^2}{\sqrt2}\cosh(2|y|a)
-b^2\cosh(2|y||b|)\\
&\ge
\left(\frac{a^2}{\sqrt2}-b^2\right)
\cosh(2|y|a).
\end{aligned}
\]

Inside `|b|≤a/2`,

\[
\frac{a^2}{\sqrt2}-b^2
\ge
a^2\left(\frac1{\sqrt2}-\frac14\right)>0.
\]

Therefore

\[
\boxed{
|b|\le r_+(x,a)
\Longrightarrow
L_{x,y}(a,b)>0
}
\]

for every real `x,y` with `x≠0`. At `x=0`,

\[
L_{0,y}(a,b)
=
a^2\cosh(2ya)+b^2\cosh(2yb)>0
\]

throughout the full interior cone `a>|b|`.

This positive-core statement has status **EXACT**.

## 3. Transverse mass geometry

Set

\[
f(u):=\log\Phi(u).
\]

Then

\[
\log M(a,b)=f(a+b)+f(a-b).
\]

The mass is even in `b`:

\[
M(a,b)=M(a,-b).
\]

Assume strict log-concavity on the relevant interval,

\[
f''(u)<0.
\]

Jensen's inequality at the midpoint gives

\[
\frac{f(a+b)+f(a-b)}2<f(a)
\qquad (b\neq0),
\]

hence

\[
\boxed{
M(a,b)<M(a,0)=\Phi(a)^2
\qquad (b\neq0).
}
\]

The transverse logarithmic slope is

\[
\partial_b\log M(a,b)
=f'(a+b)-f'(a-b).
\]

Strict concavity makes `f'` strictly decreasing, so for `b>0`,

\[
\boxed{
\partial_b\log M(a,b)<0.
}
\]

Thus each fixed-`a` mass slice is centred at `b=0` and strictly decreases with `|b|`, conditional on strict log-concavity.

## 4. Hessian transfer

Let

\[
c_+=f''(a+b),
\qquad
c_-=f''(a-b).
\]

Then

\[
\nabla^2\log M
=
\begin{pmatrix}
c_++c_- & c_+-c_-\\
c_+-c_- & c_++c_-
\end{pmatrix},
\]

whose eigenvalues are

\[
\boxed{2c_+,\qquad 2c_-}.
\]

Hence strict log-concavity of `Φ` transfers directly to strict log-concavity of the two-dimensional correlated mass surface `M` on the diagonal cone.

## 5. Gaussian slice envelope

Suppose a certified curvature floor is available on the complete symmetric interval

\[
[a-|b|,a+|b|],
\]

namely

\[
-f''(u)\ge\lambda>0.
\]

Define the symmetric logarithmic gap

\[
G(a,b)
:=
2f(a)-f(a+b)-f(a-b).
\]

Twice integrating the curvature gives

\[
G(a,b)
=
\int_0^{|b|}(|b|-t)
\left[-f''(a+t)-f''(a-t)\right]dt.
\]

Therefore

\[
G(a,b)\ge\lambda b^2,
\]

and since

\[
\frac{M(a,b)}{M(a,0)}=e^{-G(a,b)},
\]

we obtain the conditional Gaussian envelope

\[
\boxed{
M(a,b)
\le
M(a,0)e^{-\lambda b^2}.
}
\]

The implication from a certified curvature floor to this envelope has status **EXACT_CONDITIONAL**.

## 6. External TP₂ input and normalization firewall

Avi Gershon, *On the Log-Concavity of the Riemann Xi Kernel*, version 2, posted 29 June 2026, reports

\[
(\log\Phi_G)''(u)<0,
\qquad u\ge0,
\]

with computational and analytic arguments. The source is a preprint and is tracked here as **EXTERNAL_PREPRINT_CLAIM**.

The source's kernel normalization is

\[
\Phi_G(u)=2\Phi_{\mathrm{TIR}}(u).
\]

Positive constant scaling preserves

\[
(\log\Phi)'
\quad\text{and}\quad
(\log\Phi)'',
\]

so the TP₂/log-curvature statement is normalization-invariant. The correlated mass scales by a constant factor while the ratios

\[
\frac{M(a,b)}{M(a,0)}
\]

and all logarithmic derivatives remain invariant.

The same v2 source records TP₂ as a necessary level and leaves TP∞ / the full Laguerre–Pólya closure **OPEN**. XF-6 preserves that separation.

Reference:

- A. Gershon, *On the Log-Concavity of the Riemann Xi Kernel*, Preprints.org, v2, 29 June 2026, DOI: `10.20944/preprints202604.0159.v2`.

## 7. Positive-core / tail decomposition

Because both `M(a,b)` and `L_{x,y}(a,b)` are even in `b`,

\[
Q_\Xi(x,y)
=
8\int_0^\infty
\int_0^a
M(a,b)L_{x,y}(a,b)\,db\,da.
\]

For `x≠0`, split at `r_+(x,a)`:

\[
Q_\Xi
=8\int_0^\infty
\left[
\int_0^{r_+} ML\,db
+
\int_{r_+}^{a} ML\,db
\right]da.
\]

The first integral has an **EXACT** positive kernel lower bound. The second is the oscillatory tail. A certified transverse mass envelope supplies a quantitative mechanism for suppressing that tail.

The remaining global obligation can therefore be stated as

\[
\boxed{
\text{positive-core lower bound}
>
\text{absolute negative-tail bound}
}
\]

uniformly for every real `x` and every `0<|y|<1/2`.

This global domination statement has status **OPEN_RH_EQUIVALENT_ROUTE**.

## 8. XF-6 executable surface

`critical_axis.transverse_mass` exposes:

- `transverse_mass(a,b)`;
- `transverse_mass_ratio(a,b)`;
- `log_phi_slope(u)`;
- `log_phi_curvature(u)`;
- `transverse_log_mass_slope_b(a,b)`;
- `transverse_log_gap(a,b)`;
- `transverse_log_mass_hessian(a,b)`;
- `gaussian_mass_envelope(a,b,curvature_floor)`;
- `curvature_positive_corridor_radius(x,a)`;
- `theta_curvature_corridor_lower_bound(x,y,a,b)`;
- `theta_curvature_corridor_margin(x,y,a,b)`.

Finite-`Phi` derivatives are **NUMERICAL_DIAGNOSTIC**. The positive-corridor inequality and the conditional calculus implications are analytic statements.

## 9. Frontier

The next proof target is a certified, globally usable bound of the form

\[
\int_{r_+(x,a)}^a
M(a,b)\,|L^-_{x,y}(a,b)|\,db
<
\int_0^{r_+(x,a)}
M(a,b)L_{x,y}(a,b)\,db
\]

after integration in `a`, uniformly over the critical-strip `y` range.

Promising admissible tools are:

1. a rigorous lower-curvature certificate for `-\partial_u^2\log\Phi`;
2. Gaussian or stronger transverse tail bounds;
3. exact oscillatory-moment estimates preserving the `M·L` correlation;
4. interval-certified partition bounds for finite `a,x,y` blocks followed by analytic tails.

The global sign frontier and RH retain **OPEN** status.
