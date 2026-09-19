# TIR CKM SU(3)_F Angle–Sine Generator Firewall v0.8

Status: `EXACT_ANGLE_SINE_DISTINCTION / NAIVE_CONNECTION_ADDITIVITY_NO_GO / NONLINEAR_ANGLE_LIFT_EXACT / PHYSICAL_READOUT_MAP_OPEN_POSTDICTIVE`

Date: 2026-09-14

## Scope

Stage 34 places CKM mixing on the family carrier
\[
V_F=R_{23}R_{13}(\delta)R_{12}\in SU(3)_F.
\]
The standard `12` block is parameterized by an angle `theta_12` through
\[
s_{12}=\sin\theta_{12},\qquad c_{12}=\cos\theta_{12}.
\]

v0.6 and v0.7 provide an exact operator readout
\[
s_{12}=b+a\kappa,
\qquad b=\frac29,\quad a=\frac27.
\]
This audit prevents a false shortcut: a Lie-algebra/connection generator is additive in its infinitesimal **angle/generator parameter**, not automatically in its sine coordinate.

## 1. Exact nonlinear angle lift

The group angle corresponding to the current sine coordinate is
\[
\boxed{\theta_{12}=\arcsin(b+a\kappa).}
\]
Relative to the rational base angle
\[
\theta_{12}^{(0)}=\arcsin b,
\]
the exact correction is
\[
\boxed{\Delta\theta=\arcsin(b+a\kappa)-\arcsin b.}
\]

At `kappa=0`,
\[
\left.\frac{d\Delta\theta}{d\kappa}\right|_{0}
=\frac{a}{\sqrt{1-b^2}}.
\]
Because
\[
1-b^2=1-\frac4{81}=\frac{77}{81},
\]
we obtain
\[
\boxed{
\left.\frac{d\Delta\theta}{d\kappa}\right|_{0}
=\frac{18}{7\sqrt{77}}
\neq\frac27=a.
}
\]
Thus `a*kappa` is not even the first-order correction to the SU(3)_F rotation angle.

## 2. Naive additive-angle route fails exactly

If one tried to identify the connection correction directly with `a*kappa`,
\[
\theta_{12}\stackrel{?}{=}\arcsin b+a\kappa,
\]
then the predicted sine would be
\[
\sin(\arcsin b+a\kappa),
\]
which is not equal to
\[
b+a\kappa
\]
for nonzero `kappa`.

Therefore a primitive Lie-algebra coproduct or an additive connection one-form cannot by itself prove the exact historical sine formula.  It can at most control the additive generator/angle law.  A separate map from the TIR connection/flow variable to the CKM sine readout must be derived.

## 3. Relation to v0.7

v0.7 proves conditionally that an independent tensor-product flow has the unique infinitesimal Kronecker-sum generator.  v0.8 sharpens the remaining physical debt:

1. prove that the TIR flavour dynamics is represented by such a connection flow;
2. derive the observable/readout map from that flow to `s_12`;
3. show that this map yields exactly `b+a*kappa`, or equivalently yields the nonlinear angle correction above.

The group-theoretic home `SU(3)_F` is already established by Stage 34, but it does not identify `s_12` with the additive Lie-algebra coordinate.

## 4. Proof firewall

Exact:

- `s_12=sin(theta_12)` in the standard CKM `R_12` block;
- `theta_12=asin(b+a*kappa)` if the current structural sine formula is used;
- `Delta theta=asin(b+a*kappa)-asin(b)`;
- the first-order coefficient `18/(7 sqrt(77))`;
- the failure of the naive exact angle ansatz `asin(b)+a*kappa`.

Open:

- deriving the angle/readout map from TIR connection or holonomy dynamics;
- deriving the exact nonlinear `Delta theta` independently of historical CKM development;
- prospective validation.

No physical or predictive promotion is made.

Validator:

`TIR/validation/tir_ckm_su3f_angle_sine_generator_firewall_v0_8.py`
