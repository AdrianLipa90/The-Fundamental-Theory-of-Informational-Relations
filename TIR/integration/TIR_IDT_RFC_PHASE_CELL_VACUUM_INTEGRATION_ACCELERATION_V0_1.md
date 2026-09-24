# TIR × IDT × RFC Phase-Cell Vacuum-Integration Acceleration Gate v0.1

Status: RF_F15_FIXED_X_VACUUM_INTEGRATION_CONSTANT_PASS / CONSERVED_C_LAMBDA_TRANSPORT_COORDINATE_PASS / FLRW_ACCELERATION_TRANSITION_EXACT_CONDITIONAL / NO_BARE_LAMBDA_INSERTION_REQUIRED_ON_TRANSPORT_ROUTE / C_LAMBDA_PHYSICAL_OR_TOPOLOGICAL_ORIGIN_OPEN / MULTICOMPONENT_COSMOLOGY_OPEN

Date: 2026-09-24

## 1. Purpose

This gate asks whether the already-derived microscopic ↔ phase-cell transport law can generate a vacuum-like contribution and an accelerated FLRW phase without inserting an independent bare cosmological constant by hand.

The relevant RFC parents are RF-F12, RF-F15 and RF-F16.

RF-F15 gives, on the fixed spatial-ratio branch,

\[
x:=\frac{k^2}{\omega^2}=\mathrm{constant},
\]

\[
\boxed{
v(\omega)
=
\frac{1-x}{2}
+
\frac{C_\Lambda}{\omega^4},
}
\]

with

\[
K=K_0\omega^4.
\]

Therefore

\[
\boxed{
\rho
=
\rho_r+\rho_\Lambda,
\qquad
p
=
\frac13\rho_r-\rho_\Lambda,
}
\]

where

\[
\boxed{
\rho_r
=
\frac{3+x}{2}K_0\omega^4,
}
\]

and

\[
\boxed{
\rho_\Lambda
=
K_0C_\Lambda
=
\mathrm{constant}.
}
\]

RF-F16 places this constant component into the common-action vacuum ledger and shows that it can be absorbed into the renormalized reference cosmological coordinate without changing the geometry.

## 2. Conserved transport coordinate

Starting from the fixed-\(x\) RF-F15 transport equation

\[
\boxed{
\frac{dv}{d\ln|\omega|}
+4v
=
2(1-x),
}
\]

define

\[
\boxed{
C_\Lambda
:=
|\omega|^4
\left[
v-\frac{1-x}{2}
\right].
}
\]

Differentiate with respect to \(\ln|\omega|\):

\[
\frac{dC_\Lambda}{d\ln|\omega|}
=
|\omega|^4
\left[
4\left(v-\frac{1-x}{2}\right)
+
\frac{dv}{d\ln|\omega|}
\right].
\]

Using the transport equation,

\[
\boxed{
\frac{dC_\Lambda}{d\ln|\omega|}=0.
}
\]

Thus \(C_\Lambda\) is an exact conserved coordinate of the fixed-\(x\) transport family.

It is not, at this gate, identified with temporal holonomy, a topological invariant or a fundamental constant. It is an integration/boundary datum of the transport equation.

## 3. Acceleration equation

For a flat FLRW source,

\[
\boxed{
\frac{a''}{a}
=
-\frac{\kappa_E}{6}(\rho+3p)
}
\]

in the RFC length-valued temporal coordinate \(x^0=ct\).

For the RF-F15 fixed-\(x\) decomposition,

\[
\rho+3p
=
(\rho_r+\rho_\Lambda)
+
3\left(\frac13\rho_r-\rho_\Lambda\right),
\]

hence

\[
\boxed{
\rho+3p
=
2(\rho_r-\rho_\Lambda).
}
\]

Therefore

\[
\boxed{
\frac{a''}{a}
=
\frac{\kappa_E}{3}
(\rho_\Lambda-\rho_r).
}
\]

The source accelerates exactly when

\[
\boxed{
\rho_\Lambda>\rho_r.
}
\]

Substituting the RF-F15 expressions gives

\[
\boxed{
C_\Lambda
>
\frac{3+x}{2}\omega^4.
}
\]

A positive \(C_\Lambda\) is required for a late vacuum-dominated accelerating phase in this two-component fixed-\(x\) family.

## 4. Exact transition phase rate

At the acceleration transition,

\[
\rho_\Lambda=\rho_r.
\]

Therefore

\[
K_0C_\Lambda
=
\frac{3+x}{2}K_0\omega_{\rm acc}^4,
\]

so, for \(C_\Lambda>0\),

\[
\boxed{
\omega_{\rm acc}^4
=
\frac{2C_\Lambda}{3+x}.
}
\]

Hence

\[
\boxed{
|\omega_{\rm acc}|
=
\left(
\frac{2C_\Lambda}{3+x}
\right)^{1/4}.
}
\]

RF-F12 gives

\[
\boxed{
a|\omega|=Q_a=\mathrm{constant}
}
\]

on the homogeneous-isotropic fixed-orientation branch. Therefore

\[
\boxed{
a_{\rm acc}
=
Q_a
\left(
\frac{3+x}{2C_\Lambda}
\right)^{1/4}.
}
\]

This is an exact transition relation on the admitted fixed-\(x\), phase-cell, FLRW branch.

It is not yet a numerical prediction because \(C_\Lambda\), \(Q_a\) and the physical realization of the branch remain promotion inputs.

## 5. Effective equation of state

Define the ratio

\[
r_\Lambda
:=
\frac{\rho_\Lambda}{\rho_r}.
\]

Then

\[
\boxed{
w_{\rm eff}
=
\frac{p}{\rho}
=
\frac{\frac13-r_\Lambda}{1+r_\Lambda}.
}
\]

The limits are

\[
r_\Lambda\to0
\Longrightarrow
w_{\rm eff}\to\frac13,
\]

\[
r_\Lambda=1
\Longrightarrow
w_{\rm eff}=-\frac13,
\]

\[
r_\Lambda\to\infty
\Longrightarrow
w_{\rm eff}\to-1.
\]

Thus the same exact fixed-\(x\) transport family interpolates from radiation-like behavior to a vacuum-like late-time limit as \(|\omega|\) decreases.

This is a transport mechanism, not an additional particle species.

## 6. Scale-factor form

RF-F12 gives

\[
|\omega|\propto a^{-1}.
\]

Hence

\[
\boxed{
\rho_r\propto a^{-4},
}
\]

while

\[
\boxed{
\rho_\Lambda=\mathrm{constant}.
}
\]

Therefore

\[
\boxed{
r_\Lambda\propto a^4.
}
\]

For a reference epoch \(a_0\),

\[
\boxed{
r_\Lambda(a)
=
r_{\Lambda,0}
\left(\frac{a}{a_0}\right)^4.
}
\]

The acceleration threshold \(r_\Lambda=1\) occurs at

\[
\boxed{
\frac{a_{\rm acc}}{a_0}
=
r_{\Lambda,0}^{-1/4}.
}
\]

If one sets \(a_0=1\), the corresponding purely kinematic redshift expression is

\[
\boxed{
1+z_{\rm acc}
=
r_{\Lambda,0}^{1/4}.
}
\]

This is only the fixed-\(x\) radiation+vacuum family. It must not be compared directly with observed late-time acceleration without adding the independently admitted matter/dust source ledger.

## 7. Matter-added conditional corollary

If an independently action-derived pressureless component \(\rho_d\) is added to the total Einstein source, then

\[
\rho_{\rm tot}
=
\rho_d+\rho_r+\rho_\Lambda,
\]

\[
p_{\rm tot}
=
\frac13\rho_r-\rho_\Lambda.
\]

The acceleration equation becomes

\[
\boxed{
\frac{a''}{a}
=
-\frac{\kappa_E}{6}
\left(
\rho_d+2\rho_r-2\rho_\Lambda
\right).
}
\]

Hence

\[
\boxed{
\ddot a>0
\iff
2\rho_\Lambda
>
\rho_d+2\rho_r.
}
\]

This composition is exact once the source sectors are independently admitted. The common microscopic/multispecies transport realization remains open.

## 8. Relation to RF-F16 common action

RF-F16 defines

\[
\boxed{
\rho_C=K_0C_\Lambda
}
\]

and

\[
\boxed{
\Lambda_*
=
\Lambda_{\rm ref}
+
\kappa_E(\rho_C+U_0).
}
\]

Therefore the RF-F15 integration constant is already action-compatible as a constant vacuum component.

A constant repartition

\[
\rho_C\mapsto\rho_C+\delta,
\qquad
U_L\mapsto U_L-\delta
\]

leaves the geometry invariant.

Thus the physically meaningful quantity is the complete constant-vacuum ledger, not a label attached to one algebraic term.

## 9. No-arbitrary-Lambda statement and its limit

The fixed-\(x\) transport equation generates a constant vacuum-density component as its integration constant. Therefore one does not need to insert an additional independent \(\Lambda\)-term into the transport equation to obtain the vacuum-like branch.

However,

\[
\boxed{
\text{generation of the functional form}
\neq
\text{prediction of its magnitude}.
}
\]

The value and sign of \(C_\Lambda\) are not fixed by RF-F15/F16.

A stronger first-principles claim requires an independent boundary/topological/dynamical theorem fixing

\[
\boxed{
C_\Lambda.
}
\]

## 10. Holonomy frontier

No existing repository receipt identifies

\[
C_\Lambda
\]

with

\[
\tau_R,
\qquad
\oint\mathcal A,
\qquad
\int\mathcal F,
\]

or another topological/holonomic invariant.

The next non-circular question is therefore:

\[
\boxed{
\text{Can }C_\Lambda
\text{ be derived from an independently conserved holonomy/topology/boundary charge?}
}
\]

Until such a theorem is supplied, \(C_\Lambda\) remains a conserved transport integration coordinate rather than a holonomy-derived constant.

## 11. Current verdict

Exact on the admitted RF-F12/F15/F16 parents:

\[
\boxed{
\text{phase-cell transport}
\to
C_\Lambda
\to
\rho_\Lambda=\mathrm{const}
\to
\text{radiation/vacuum interpolation}
\to
\text{acceleration when }\rho_\Lambda>\rho_r.
}
\]

Open:

\[
\boxed{
\text{first-principles value/sign of }C_\Lambda
}
\]

and its possible holonomic/topological origin.

Reference validator:

TIR/validation/tir_idt_rfc_phase_cell_vacuum_integration_acceleration_v0_1.py
