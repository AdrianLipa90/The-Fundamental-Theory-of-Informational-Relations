# XF-8 — Differential Hermite–Biehler bridge

Status: `EXACT_DIFFERENTIAL_IDENTITY / RH_EQUIVALENT_GLOBAL_MARGIN / PI_BOUNDARY_PHASE_EXACT_AT_SIMPLE_ZERO / INTEGRATED_KERNEL_REDUCTION_EXACT / RH_OPEN`

Parent routes: XF-1 canonical Xi-kernel branches, XF-5 transverse convexity, XF-6 transverse mass envelope, XF-7 Laguerre hierarchy.

## 1. Real entire Xi coordinate

Use

\[
\Xi(z)=\xi\!\left(\frac12+i z\right).
\]

Then \(\Xi\) is a real entire function,

\[
\Xi^{\#}(z):=\overline{\Xi(\overline z)}=\Xi(z),
\]

and the critical line in the original \(s\)-plane is the real \(z\)-axis.

## 2. Canonical differential pair

Define

\[
\boxed{E_D(z):=\Xi(z)+i\Xi'(z)},
\qquad
\boxed{E_D^{\#}(z)=\Xi(z)-i\Xi'(z)}.
\]

Hence

\[
\boxed{
\Xi(z)=\frac12\left(E_D(z)+E_D^{\#}(z)\right).
}
\]

Unlike XF-2, this is not a constant real mixing of the raw half-kernel branches. It is an operator-derived transform of Xi.

## 3. Exact Hermite–Biehler margin identity

For \(z=x+iy\), let

\[
M_\Xi(x,y):=|\Xi(x+iy)|^2.
\]

Direct algebra and analyticity give

\[
\begin{aligned}
\Delta_D(z)
&:=|E_D(z)|^2-|E_D^{\#}(z)|^2\\
&=4\,\operatorname{Im}\!\left(\Xi(z)\overline{\Xi'(z)}\right)\\
&=2\,\partial_y M_\Xi(x,y).
\end{aligned}
\]

Since \(M_\Xi(x,y)\) is even in \(y\), \(\partial_yM_\Xi(x,0)=0\). XF-5 established

\[
\partial_y^2M_\Xi(x,y)=2Q_\Xi(x,y),
\]

therefore

\[
\boxed{
\Delta_D(x+iy)
=4\int_0^y Q_\Xi(x,v)\,dv.
}
\]

This exact identity is the main XF-5 -> XF-8 bridge.

## 4. Euler phase at an Xi zero

Where \(E_D(z)\neq0\), define

\[
\Theta_D(z):=\frac{E_D^{\#}(z)}{E_D(z)}.
\]

If \(z_0\) is a simple Xi zero, then

\[
E_D(z_0)=i\Xi'(z_0),
\qquad
E_D^{\#}(z_0)=-i\Xi'(z_0),
\]

so

\[
\boxed{
\Theta_D(z_0)=-1=e^{i\pi}.
}
\]

Thus the \(\pi\) antiphase is an exact consequence of zerohood in this representation; it is not inserted by assuming \(\Re s=1/2\).

For a zero of multiplicity \(m>1\), both differential branches share \((z-z_0)^{m-1}\). After cancelling that common local factor, the quotient tends to \(-1\). No simplicity claim is promoted.

## 5. Half-plane localization condition

The antiphase alone does not localize the zero. A hypothetical off-real simple zero also gives \(\Theta_D=-1\).

If

\[
\boxed{
|E_D(z)|>|E_D^{\#}(z)|
\qquad \Im z>0,
}
\]

then \(|\Theta_D(z)|<1\) in the upper half-plane, so the unit-modulus value \(-1\) cannot occur there. Schwarz symmetry excludes the lower half-plane. All Xi zeros are then real.

Equivalently, it is sufficient to prove

\[
\boxed{
\partial_y|\Xi(x+iy)|^2>0
\qquad y>0.
}
\]

Since nontrivial zeta zeros already lie in the critical strip, RH only needs the corresponding strip-local condition

\[
\boxed{
\Delta_D(x+iy)>0
\qquad x\in\mathbb R,\quad0<y<\frac12.
}
\]

## 6. Relation to XF-5

XF-5 gives the standard equivalence

\[
\mathrm{RH}
\iff
Q_\Xi(x,y)\ge0
\quad\forall x,y\in\mathbb R.
\]

Since

\[
\Delta_D(x+iy)=4\int_0^yQ_\Xi(x,v)\,dv,
\]

pointwise XF-5 positivity is stronger in form than the integrated sign needed by XF-8.

Conversely, strict positivity of \(\Delta_D\) throughout the upper critical strip excludes every off-axis nontrivial zero immediately, because at any Xi zero \(\Delta_D=0\).

Thus the strip-local strict differential margin is an RH-equivalent target. It is a reformulation, not a proof of the missing sign.

## 7. Weyl/Herglotz reformulation

Away from Xi zeros define

\[
\boxed{
m_\Xi(z):=-\frac{\Xi'(z)}{\Xi(z)}.}
\]

Then

\[
\boxed{
\Delta_D(z)
=4|\Xi(z)|^2\operatorname{Im}m_\Xi(z).
}
\]

Therefore the strict differential margin is equivalent, away from zeros, to

\[
\boxed{
\operatorname{Im}m_\Xi(z)>0
\qquad \Im z>0.
}
\]

In other words, the missing global statement can be posed as a Herglotz/Nevanlinna property for the canonical Xi logarithmic derivative. If that property is established independently, an off-real Xi zero is impossible because \(m_\Xi\) would have a pole inside its Herglotz domain.

Under RH, the real-zero canonical product gives the familiar Poisson-sign form for the logarithmic derivative, so the Herglotz property follows. Hence this is again an RH-equivalent operator reformulation, not an independent proof.

## 8. Exact integrated XF-6 kernel

XF-6 writes

\[
Q_\Xi(x,y)
=4\iint_{a>|b|}M(a,b)L_{x,y}(a,b)\,da\,db,
\]

where

\[
M(a,b)=\Phi(a+b)\Phi(a-b)
\]

and

\[
L_{x,y}(a,b)
=a^2\cos(2xb)\cosh(2ya)
+b^2\cos(2xa)\cosh(2yb).
\]

Integrating exactly in the transverse variable gives

\[
\boxed{
\Delta_D(x+iy)
=8\iint_{a>|b|}M(a,b)K_{x,y}(a,b)\,da\,db,
}
\]

with

\[
\boxed{
K_{x,y}(a,b)
=a\cos(2xb)\sinh(2ya)
+b\cos(2xa)\sinh(2yb).
}
\]

This removes one power of \(a\) and \(b\) relative to the pointwise-curvature kernel and replaces \(\cosh\) by its integrated \(\sinh\) weight.

### Positive integrated corridor

For \(x\neq0\), define

\[
r_D(x,a)
:=
\min\!\left(\frac{a}{\sqrt2},\frac{\pi}{8|x|}\right).
\]

If \(|b|\le r_D\), then \(\cos(2xb)\ge1/\sqrt2\). For \(y>0\), \(|b|<a\) also gives

\[
|b|\sinh(2y|b|)
<\frac{a}{\sqrt2}\sinh(2ya).
\]

Using \(\cos(2xa)\ge-1\),

\[
\boxed{
|b|\le r_D(x,a)
\Longrightarrow
K_{x,y}(a,b)>0.
}
\]

At \(x=0\), both terms are positive throughout \(a>|b|\) for \(y>0\).

The integrated positive corridor is therefore exact and is wider in its geometric \(a\)-constraint than the earlier \(a/2\) XF-6 pointwise-curvature corridor.

## 9. Signed longitudinal tail bound

XF-7 already controls the \(b\)-oscillatory sector by integration by parts when the transverse mass decreases in \(|b|\).

For the remaining longitudinal sector, fix \(b>0\) and regard \(M(a,b)\) as a function of \(a\ge b\). Standard positivity and radial decrease of \(\Phi\) imply

\[
\partial_aM(a,b)\le0,
\qquad
M(a,b)\to0\quad(a\to\infty).
\]

A second integration-by-parts estimate therefore gives, for \(x\neq0\),

\[
\boxed{
\left|
\int_b^\infty M(a,b)\cos(2xa)\,da
\right|
\le
\frac{M(b,b)}{|x|}
=
\frac{\Phi(2b)\Phi(0)}{|x|}.
}
\]

Thus both oscillatory directions now have explicit signed \(1/|x|\) control without replacing the phase by an absolute value before integration.

This does not yet prove the global integrated margin. The remaining task is a uniform comparison between the exact positive integrated core and the two signed tails.

## 10. Promotion ledger

- `E_D = Xi + i Xi'`: `EXACT`
- `E_D# = Xi - i Xi'`: `EXACT`
- `Xi = (E_D + E_D#)/2`: `EXACT`
- `DELTA_D = 2 d_y |Xi|^2`: `EXACT`
- `DELTA_D = 4 integral_0^y Q_Xi dv`: `EXACT`
- `SIMPLE_XI_ZERO -> THETA_D = -1 = exp(i*pi)`: `EXACT`
- `MULTIPLE_ZERO -> REDUCED_LOCAL_QUOTIENT_LIMIT = -1`: `EXACT_LOCAL`
- `DELTA_D = 4 |Xi|^2 Im(m_Xi)`: `EXACT_AWAY_FROM_ZEROS`
- `INTEGRATED_XF6_KERNEL_K`: `EXACT`
- `INTEGRATED_POSITIVE_CORRIDOR`: `EXACT`
- `LONGITUDINAL_SIGNED_1_OVER_X_BOUND`: `EXACT_FROM_STANDARD_KERNEL_MONOTONICITY`
- `GLOBAL_STRICT_DIFFERENTIAL_HB_MARGIN`: `OPEN / RH_EQUIVALENT`
- `GLOBAL_INTEGRATED_CORE_TAIL_DOMINATION`: `OPEN_SUFFICIENT_ROUTE`
- `RIEMANN_HYPOTHESIS`: `OPEN`

## 11. Next proof target

The next noncircular target is no longer the pointwise inequality \(Q_\Xi>0\). It is the weaker but sufficient integrated statement

\[
\boxed{
\int_0^yQ_\Xi(x,v)\,dv>0
\qquad
x\in\mathbb R,
\quad0<y<\frac12.
}
\]

The exact positive integrated corridor and the two signed oscillatory \(1/|x|\) estimates provide the next comparison surface. RH remains OPEN until that uniform domination is actually proved.
