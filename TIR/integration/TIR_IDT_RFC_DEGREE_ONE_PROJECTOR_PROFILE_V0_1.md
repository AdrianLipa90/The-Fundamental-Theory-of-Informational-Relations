# TIR × IDT × RFC Degree-One Projector-Profile Selection v0.1

Status: UNIQUE_SQRT_PROFILE_UNDER_Q_DEGREE_ONE_HOMOGENEITY / RF_F17_NORMALIZATION_AND_SLOPE_RECOVERED / CONNECTION_HESSIAN_ZERO_EXACT / LOCAL_CARTAN_ELIMINATION_EXACT / HOMOGENEITY_PHYSICAL_BINDING_CONDITIONAL

Date: 2026-09-24

## 1. Purpose

RF-F17 leaves the physical projector profile

\[
f(C)
\]

open while requiring

\[
f(1)=1
\]

and using the dust-normalized slope

\[
f'(1)=\frac12.
\]

The projector-profile identifiability gate proves that these two local conditions do not determine the torsion-eliminated action.

RF-F13 independently establishes a degree-one Hamiltonian/source surface for the relational generator.

This gate asks a narrower compatibility question:

> If the state-dependent projector interaction is required to be positively homogeneous of degree one in the phase-clock one-form \(q\), at fixed independent calibration scale \(\mu_\vartheta\), is \(f(C)\) uniquely selected?

The answer is yes.

This is conditional on importing that degree-one requirement into the RF-F17 interaction sector. RF-F13 does not by itself force that import.

## 2. Projector scaling

Use

\[
\boxed{
C[q]
=
-\frac{g^{-1}(q,q)}{\mu_\vartheta^2}.
}
\]

On a fixed timelike orientation branch and for

\[
\lambda>0,
\]

scale

\[
q\mapsto\lambda q
\]

while holding

\[
g,\qquad
\mu_\vartheta
\]

fixed.

Then

\[
\boxed{
C[\lambda q]
=
\lambda^2C[q].
}
\]

## 3. Degree-one compatibility condition

Require the projector factor itself to carry one power of the phase-clock rate:

\[
\boxed{
f(C[\lambda q])
=
\lambda f(C[q]).
}
\]

Equivalently,

\[
\boxed{
f(\lambda^2 C)
=
\lambda f(C)
}
\]

for every

\[
C>0,\qquad \lambda>0.
\]

The physical projector normalization remains

\[
\boxed{f(1)=1.}
\]

## 4. Uniqueness theorem

Set

\[
C=1.
\]

Then

\[
f(\lambda^2)=\lambda.
\]

For an arbitrary

\[
x>0,
\]

choose

\[
\lambda=\sqrt x.
\]

Therefore

\[
\boxed{
f(x)=\sqrt x.
}
\]

Hence the unique positive degree-one-compatible normalized projector profile is

\[
\boxed{
f(C)=\sqrt C.
}
\]

No differentiability assumption beyond that needed by RF-F17 is required for this uniqueness on the positive domain.

## 5. RF-F17 normalization roundtrip

For

\[
f(C)=\sqrt C,
\]

one has

\[
\boxed{
f(1)=1,
}
\]

\[
\boxed{
f'(1)=\frac12,
}
\]

and

\[
\boxed{
f''(1)=-\frac14.
}
\]

Thus the RF-F17 dust-normalized slope is not an additional parameter on this conditional branch.

It follows from degree-one homogeneity plus \(f(1)=1\).

## 6. Connection-Hessian cancellation

The projector-profile identifiability gate gives

\[
\mathcal L''_{int,*}
=
\eta\widehat U_L
\frac{s_E^2}{\mu_\vartheta^2}
\left[
f''(1)
+
\frac12f'(1)
\right].
\]

For the square-root profile,

\[
f''(1)
+
\frac12f'(1)
=
-\frac14+\frac14
=
0.
\]

Therefore

\[
\boxed{
\mathcal L''_{int,*}=0.
}
\]

The interaction has zero local Euler-connection Hessian on the projector surface.

## 7. Exact fixed-orientation linearization

On the one-axis local control,

\[
q_0(h)
=
Q+\frac{s_E}{2}h.
\]

Since

\[
C(h)
=
\frac{q_0(h)^2}{\mu_\vartheta^2},
\]

the square-root profile is

\[
f(C(h))
=
\frac{|q_0(h)|}{\mu_\vartheta}.
\]

On a fixed-sign branch

\[
\varsigma_q
:=
\operatorname{sgn}q_0
\]

with no zero crossing,

\[
\boxed{
f(C(h))
=
\varsigma_q
\frac{
Q+\frac{s_E}{2}h
}{
\mu_\vartheta
}.
}
\]

Therefore the interaction is exactly affine in the Euler connection amplitude:

\[
\boxed{
\mathcal L_{int}
=
\eta\widehat U_L
\varsigma_q
\frac{
Q+\frac{s_E}{2}h
}{
\mu_\vartheta
}.
}
\]

The vanishing Hessian is exact throughout one fixed-sign patch, not only at one Taylor point.

## 8. Exact local Cartan elimination

Define

\[
\boxed{
\sigma_E
=
\varsigma_q
\frac{
\eta\widehat U_Ls_E
}{
\mu_\vartheta
}.
}
\]

This equals the earlier spin-current amplitude because

\[
2f'(1)=1.
\]

The local constant-source reduced connection action is

\[
\boxed{
\Delta\mathcal L(h)
=
-\frac{h^2}{4\kappa_E}
+
\frac{\sigma_E}{2}h.
}
\]

Stationarity gives

\[
-\frac{h}{2\kappa_E}
+
\frac{\sigma_E}{2}
=
0,
\]

hence

\[
\boxed{
h
=
\kappa_E\sigma_E.
}
\]

This is exactly the Cartan torsion amplitude derived independently from the sourced Cartan equation.

## 9. Exact eliminated local action

Substituting

\[
h=\kappa_E\sigma_E
\]

gives

\[
\boxed{
\Delta\mathcal L_{\rm eff}^{\sqrt C}
=
\frac{\kappa_E\sigma_E^2}{4}.
}
\]

Equivalently,

\[
\boxed{
\Delta\mathcal L_{\rm eff}^{\sqrt C}
=
\frac{
\kappa_E\eta^2\widehat U_L^2s_E^2
}{
4\mu_\vartheta^2
}.
}
\]

The orientation sign drops out quadratically.

There is no affine-control denominator

\[
1-\gamma_E
\]

on this degree-one branch.

## 10. Zero-crossing firewall

The profile

\[
f(C)=\sqrt C
\]

is smooth for

\[
C>0,
\]

but the fixed-sign representation

\[
|q_0|/\mu_\vartheta
\]

is nondifferentiable at

\[
q_0=0.
\]

The present theorem therefore applies on the already-admitted nonzero fixed-orientation phase-clock branch.

Crossing the zero-rate surface requires a separate branch-transition prescription.

## 11. What this does and does not close

Closed conditionally:

\[
\boxed{
\text{degree-one in }q
+
f(1)=1
\Rightarrow
f(C)=\sqrt C.
}
\]

This also fixes

\[
f'(1)=1/2,
\qquad
f''(1)=-1/4,
\]

and gives exact local algebraic elimination of the Euler torsion amplitude.

Still open:

1. whether the RF-F17 physical interaction must obey the RF-F13-compatible degree-one \(q\)-homogeneity condition;
2. the internal-axis to spacetime-tetrad solder;
3. the coarse-grained tetrahedral spin/torsion statistics;
4. full metric variation of the eliminated action;
5. the effective equation of state and acceleration sign.

## 12. Verdict

The previous arbitrary profile direction is reduced to a single physical yes/no gate:

\[
\boxed{
\text{Does RF-F17 inherit degree-one phase-rate homogeneity?}
}
\]

If yes,

\[
\boxed{
f(C)=\sqrt C
}
\]

is unique and the local Euler–Cartan sector is algebraically closed.

If no, the projector-profile identifiability no-go remains active.

Reference validator:

TIR/validation/tir_idt_rfc_degree_one_projector_profile_v0_1.py
