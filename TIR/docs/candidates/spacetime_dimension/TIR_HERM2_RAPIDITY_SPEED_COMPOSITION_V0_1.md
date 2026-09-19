# TIR Herm(2) Rapidity and Speed Composition v0.1

Status: CANDIDATE_ONLY / EXACT_RAPIDITY_COMPOSITION / INVARIANT_NULL_SLOPE / SPEED_BOUND_AFTER_CLOCK_CALIBRATION / PHYSICAL_CLOCK_BINDING_CONDITIONAL / CANON_ALLOWED_FALSE

Date: 2026-09-19

## 1. Parent theorem

Herm(2) Lorentz Covariance v0.1 gives the boost

\[
x^{0\prime}
=
x^0\cosh\chi
+
z\sinh\chi,
\]

\[
z'
=
z\cosh\chi
+
x^0\sinh\chi.
\]

Here \(x^0\) is the scalar Hermitian coordinate and has the same dimension as the spatial coefficients.

## 2. Dimensionless velocity

For a directed worldline segment with \(dx^0>0\), define the dimensionless slope

\[
\boxed{
u:=\frac{dz}{dx^0}.
}
\]

The causal cone condition

\[
(dx^0)^2-dz^2\ge0
\]

implies

\[
\boxed{|u|\le1.}
\]

Strictly timelike motion gives

\[
|u|<1,
\]

while null motion gives

\[
|u|=1.
\]

Thus the cone itself supplies a distinguished limiting slope before any physical unit calibration.

## 3. Boost action on slope

Differentiating the boost gives

\[
dx^{0\prime}
=
\cosh\chi\,dx^0
+
\sinh\chi\,dz,
\]

\[
dz'
=
\sinh\chi\,dx^0
+
\cosh\chi\,dz.
\]

Therefore

\[
u'
=
\frac{dz'}{dx^{0\prime}}
=
\frac{\sinh\chi+\cosh\chi\,u}
{\cosh\chi+\sinh\chi\,u}.
\]

Define

\[
\boxed{
\beta:=\tanh\chi.
}
\]

Dividing numerator and denominator by \(\cosh\chi\) gives

\[
\boxed{
u'
=
\frac{u+\beta}{1+\beta u}.
}
\]

Since finite real \(\chi\) satisfies

\[
|\tanh\chi|<1,
\]

every finite boost parameter lies inside the causal speed interval.

## 4. Null slopes are invariant

For

\[
u=+1,
\]

\[
u'
=
\frac{1+\beta}{1+\beta}
=
1.
\]

For

\[
u=-1,
\]

\[
u'
=
\frac{-1+\beta}{1-\beta}
=
-1.
\]

Hence

\[
\boxed{
u=\pm1
}
\]

are fixed points of every collinear proper boost.

The causal boundary is therefore an invariant limiting slope.

## 5. Timelike interval is preserved

For

\[
|u|<1
\]

and

\[
|\beta|<1,
\]

one has

\[
1-(u')^2
=
\frac{(1-u^2)(1-\beta^2)}
{(1+\beta u)^2}.
\]

Therefore

\[
\boxed{
|u|<1
\Longrightarrow
|u'|<1.
}
\]

The boost cannot push a timelike slope through the null boundary.

## 6. Additivity of rapidity

The spinor boost matrix is

\[
B_z(\chi)
=
\begin{pmatrix}
e^{\chi/2}&0\\
0&e^{-\chi/2}
\end{pmatrix}.
\]

Therefore

\[
B_z(\chi_1)B_z(\chi_2)
=
B_z(\chi_1+\chi_2).
\]

Thus

\[
\boxed{
\chi_{12}
=
\chi_1+\chi_2.
}
\]

Rapidity is the additive composition coordinate of collinear boosts.

## 7. Einstein composition from rapidity

Let

\[
\beta_1=\tanh\chi_1,
\qquad
\beta_2=\tanh\chi_2.
\]

Then

\[
\beta_{12}
=
\tanh(\chi_1+\chi_2).
\]

Using the hyperbolic tangent addition law,

\[
\boxed{
\beta_{12}
=
\frac{\beta_1+\beta_2}
{1+\beta_1\beta_2}.
}
\]

Thus the nonlinear velocity-composition law is the image of ordinary addition in rapidity.

## 8. Gamma factor

From

\[
\beta=\tanh\chi
\]

follows

\[
\cosh\chi
=
\frac{1}{\sqrt{1-\beta^2}}
\]

and

\[
\sinh\chi
=
\frac{\beta}{\sqrt{1-\beta^2}}.
\]

Define

\[
\boxed{
\gamma
=
\frac{1}{\sqrt{1-\beta^2}}.
}
\]

Then the boost becomes

\[
\boxed{
x^{0\prime}
=
\gamma(x^0+\beta z),
}
\]

\[
\boxed{
z'
=
\gamma(z+\beta x^0).
}
\]

The familiar Lorentz gamma factor is therefore a reparameterization of the spinor rapidity.

## 9. Physical clock calibration

The mathematics above uses the length-valued scalar coordinate \(x^0\).

If the remaining physical clock gate is admitted,

\[
\boxed{
x^0=ct,
}
\]

then

\[
u
=
\frac{dz}{c\,dt}
=
\frac{v}{c}.
\]

Therefore

\[
\boxed{
\beta=\frac{v}{c}.
}
\]

The cone bound becomes

\[
\boxed{
|v|\le c.
}
\]

For massive/timelike motion,

\[
\boxed{
|v|<c.
}
\]

For null motion,

\[
\boxed{
|v|=c.
}
\]

The dimensionful Einstein composition law is then

\[
\boxed{
v_{12}
=
\frac{v_1+v_2}
{1+v_1v_2/c^2}.
}
\]

Thus \(c\) enters only when the abstract unit null slope is calibrated to physical time.

## 10. Main theorem

### Theorem — rapidity and causal speed composition

Assume Herm(2) Lorentz Covariance v0.1.

Then:

1. causal worldline slopes satisfy \(|u|\le1\);
2. finite collinear boosts are parameterized by \(\beta=\tanh\chi\) with \(|\beta|<1\);
3. slope transformation is
   \[
   u'=\frac{u+\beta}{1+\beta u};
   \]
4. null slopes \(u=\pm1\) are invariant;
5. timelike slopes remain inside \((-1,1)\);
6. rapidities add linearly;
7. the induced boost-velocity parameter composes by
   \[
   \beta_{12}
   =
   \frac{\beta_1+\beta_2}{1+\beta_1\beta_2};
   \]
8. after the separate physical calibration \(x^0=ct\), this becomes the standard relativistic speed bound and Einstein velocity-addition law.

## 11. Evidence boundary

Exact mathematics:

- causal unit slope bound;
- invariant null slopes;
- timelike-domain invariance;
- rapidity additivity;
- hyperbolic tangent composition;
- Lorentz gamma relation.

Still conditional physically:

- \(x^0=ct\) is the calibrated physical clock binding;
- \(v=dz/dt\) is the corresponding measured physical velocity.

No independent measurement of \(c\) is derived here. The theorem shows that once the temporal coordinate is calibrated by \(x^0=ct\), the same scale is necessarily the invariant causal speed.
