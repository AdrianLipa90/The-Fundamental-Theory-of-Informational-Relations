# XF-6 — Differential Hermite–Biehler bridge

Status: `EXACT_DIFFERENTIAL_IDENTITY / RH_EQUIVALENT_GLOBAL_MARGIN / PI_BOUNDARY_PHASE_EXACT_AT_SIMPLE_ZERO / RH_OPEN`

Parent routes: XF-1 canonical Xi-kernel branches, XF-5 transverse convexity.

## 1. Real entire Xi coordinate

Use

\[
\Xi(z)=\xi\!\left(\frac12+i z\right).
\]

Then \(\Xi\) is a real entire function:

\[
\Xi^{\#}(z):=\overline{\Xi(\overline z)}=\Xi(z).
\]

The critical line in the original \(s\)-plane is the real \(z\)-axis.

## 2. Canonical differential pair

Define

\[
\boxed{E_D(z):=\Xi(z)+i\Xi'(z)}
\]

and therefore

\[
\boxed{E_D^{\#}(z)=\Xi(z)-i\Xi'(z)}.
\]

The symmetric reconstruction is exact:

\[
\boxed{
\Xi(z)=\frac12\left(E_D(z)+E_D^{\#}(z)\right).
}
\]

Unlike XF-2, this candidate is not a constant real mixing of the raw half-kernel branches.  It is an operator-derived transform of the completed Xi function.

## 3. Exact Hermite–Biehler margin identity

For \(z=x+iy\), let

\[
M(x,y):=|\Xi(x+iy)|^2.
\]

Direct algebra gives

\[
\begin{aligned}
\Delta_D(z)
&:=|E_D(z)|^2-|E_D^{\#}(z)|^2\\
&=4\,\operatorname{Im}\!\left(\Xi(z)\overline{\Xi'(z)}\right).
\end{aligned}
\]

Analyticity gives

\[
\partial_y M(x,y)
=2\,\operatorname{Im}\!\left(\Xi(z)\overline{\Xi'(z)}\right),
\]

hence

\[
\boxed{
\Delta_D(x+iy)=2\,\partial_y|\Xi(x+iy)|^2.
}
\]

Because \(M(x,y)\) is even in \(y\),

\[
\partial_yM(x,0)=0.
\]

XF-5 established the exact curvature identity

\[
\partial_y^2M(x,y)=2Q_\Xi(x,y),
\]

so integration from the real axis yields

\[
\boxed{
\Delta_D(x+iy)
=4\int_0^y Q_\Xi(x,v)\,dv.
}
\]

This is an exact bridge between the Hermite–Biehler margin and the XF-5 Laguerre curvature.

## 4. Euler phase at an Xi zero

Where \(E_D(z)\neq0\), define

\[
\Theta_D(z):=\frac{E_D^{\#}(z)}{E_D(z)}.
\]

If \(z_0\) is a simple Xi zero, then \(\Xi(z_0)=0\) and \(\Xi'(z_0)\neq0\), so

\[
E_D(z_0)=i\Xi'(z_0),
\qquad
E_D^{\#}(z_0)=-i\Xi'(z_0).
\]

Therefore

\[
\boxed{
\Theta_D(z_0)=-1=e^{i\pi}.
}
\]

Thus the Euler antiphase is not inserted as a critical-line assumption in this differential representation: it is an exact consequence of zerohood for every simple Xi zero.

For a multiple zero of multiplicity \(m>1\), both \(E_D\) and \(E_D^{\#}\) share the factor \((z-z_0)^{m-1}\).  After cancelling that common local factor, the quotient tends to \(-1\) as \(z\to z_0\).  No simplicity claim is promoted.

## 5. Why the antiphase alone still does not prove RH

The equation

\[
\Theta_D(z_0)=-1
\]

holds at a hypothetical off-real simple Xi zero as well.  The missing localization condition is a half-plane modulus ordering.

If

\[
\boxed{
|E_D(z)|>|E_D^{\#}(z)|
\qquad \Im z>0,
}
\]

then

\[
|\Theta_D(z)|<1
\qquad \Im z>0.
\]

Hence \(\Theta_D=-1\), which has unit modulus, cannot occur inside the upper half-plane.  Schwarz symmetry excludes the lower half-plane.  All Xi zeros are then real, which is RH.

Equivalently, by the exact margin identity, it is sufficient to prove

\[
\boxed{
\partial_y|\Xi(x+iy)|^2>0
\qquad y>0,
}
\]

for every real \(x\).

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

global XF-5 nonnegativity forces a nonnegative differential Hermite–Biehler margin in the upper half-plane.  Under the real-zero/Laguerre–Pólya representation of Xi, the margin is strictly positive for \(y>0\) because the logarithmic derivative is a sum of strictly negative imaginary Poisson terms contributed by the real zeros.

Conversely, strict positivity of \(\Delta_D\) throughout \(\Im z>0\) excludes every nonreal Xi zero immediately, since at any Xi zero the margin equals zero.

Thus the global strict differential margin is an RH-equivalent criterion.  This is a reformulation, not a proof of the missing sign.

## 7. What has changed relative to the older conditional theorem

The old conditional two-state theorem treated a \(\pi\) relative zero phase as an assumption.  XF-1 already replaced the representation debt by a canonical two-branch Xi-kernel identity.  XF-6 further shows that an operator-derived Xi representation carries the boundary antiphase

\[
-1=e^{i\pi}
\]

exactly at every simple zero, without inserting \(\Re s=1/2\) in advance.

The remaining RH-level debt is therefore not "derive the phase \(\pi\)".  It is:

\[
\boxed{
\text{prove the global half-plane modulus ordering / integrated curvature sign.}
}
\]

## 8. Promotion ledger

- `E_D = Xi + i Xi'`: `EXACT`
- `E_D# = Xi - i Xi'`: `EXACT`
- `Xi = (E_D + E_D#)/2`: `EXACT`
- `DELTA_D = 2 d_y |Xi|^2`: `EXACT`
- `DELTA_D = 4 integral_0^y Q_Xi dv`: `EXACT`
- `SIMPLE_XI_ZERO -> THETA_D = -1 = exp(i*pi)`: `EXACT`
- `MULTIPLE_ZERO -> REDUCED_LOCAL_QUOTIENT_LIMIT = -1`: `EXACT_LOCAL`
- `GLOBAL_STRICT_DIFFERENTIAL_HB_MARGIN`: `OPEN / RH_EQUIVALENT`
- `RIEMANN_HYPOTHESIS`: `OPEN`

## 9. Next proof target

The next noncircular target is a theorem proving

\[
\int_0^y Q_\Xi(x,v)\,dv>0
\qquad\forall x\in\mathbb R,\ y>0,
\]

from an independently positive kernel/operator representation, without assuming real Xi zeros.  This target is weaker in form than pointwise XF-5 curvature positivity, but still strong enough to exclude off-axis zeros through the differential Hermite–Biehler quotient.
