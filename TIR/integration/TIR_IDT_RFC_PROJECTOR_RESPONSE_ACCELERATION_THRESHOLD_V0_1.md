# TIR × IDT × RFC Projector-Response Acceleration Threshold v0.1

Status: RF_F22_PROJECTOR_ACTIVE_SOURCE_PASS / FROZEN_RESPONSE_DECELERATION_CONTROL_PASS / CONNECTION_SCALE_RESPONSE_ACCELERATION_THRESHOLD_EXACT_CONDITIONAL / TEMPORAL_U1_RESPONSE_BINDING_OPEN

Date: 2026-09-24

## 1. Parent source

RF-F22 gives the state-dependent interaction response on the projector surface

\[
\boxed{
D_{\mu\nu}
=
2\eta\widehat U_L f'(1)
\frac{q_\mu q_\nu}{\mu_\vartheta^2}
+
4\eta\widehat U_L f'(1)
\frac{R_{\mu\nu}}{\mu_\vartheta^2}
+
4\eta\widehat U_L f'(1)
S^{(\vartheta)}_{\mu\nu}.
}
\]

Here

- \(q_\mu\) is the gauge-covariant phase one-form;
- \(R_{\mu\nu}\) is the ABE connection metric response from RF-F20;
- \(S^{(\vartheta)}_{\mu\nu}\) is the independent phase-scale metric response from RF-F19;
- \(\eta\) is the exchange allocation;
- \(f'(1)\) is the physical projector slope.

This tensor is retained identically in both the fixed-reference and dynamic-\(\Lambda_0\) Einstein ledgers.

## 2. Homogeneous-isotropic normal phase projector

Take the local orthonormal normal-flow projector surface

\[
q_{\hat a}
=
(\mu_\vartheta,0,0,0),
\]

so

\[
-\frac{q^2}{\mu_\vartheta^2}=1.
\]

Take isotropic response tensors

\[
R_{\hat a\hat b}
=
\operatorname{diag}(R_0,R_s,R_s,R_s),
\]

\[
S^{(\vartheta)}_{\hat a\hat b}
=
\operatorname{diag}(S_0,S_s,S_s,S_s).
\]

Then

\[
\boxed{
D_{00}
=
2\eta\widehat U_L f'(1)
+
4\eta\widehat U_L f'(1)\frac{R_0}{\mu_\vartheta^2}
+
4\eta\widehat U_L f'(1)S_0,
}
\]

and

\[
\boxed{
D_{ss}
=
4\eta\widehat U_L f'(1)\frac{R_s}{\mu_\vartheta^2}
+
4\eta\widehat U_L f'(1)S_s.
}
\]

## 3. Active-source combination

The FLRW acceleration source is the isotropic combination

\[
D_{00}+3D_{ss}.
\]

Therefore

\[
\boxed{
D_{00}+3D_{ss}
=
2\eta\widehat U_L f'(1)
\left[
1
+
2\frac{R_0+3R_s}{\mu_\vartheta^2}
+
2(S_0+3S_s)
\right].
}
\]

Define

\[
\boxed{
\mathcal B_{\rm resp}
:=
1
+
2\frac{R_0+3R_s}{\mu_\vartheta^2}
+
2(S_0+3S_s).
}
\]

The projector contribution to the flat-FLRW acceleration equation is

\[
\boxed{
\Delta\!\left(\frac{a''}{a}\right)_D
=
-\frac{\kappa_E}{3}
\eta\widehat U_L f'(1)
\mathcal B_{\rm resp}.
}
\]

## 4. Acceleration threshold

On the positive interaction branch

\[
\eta>0,
\qquad
\widehat U_L>0,
\qquad
f'(1)>0,
\]

the projector response accelerates exactly when

\[
\boxed{
\mathcal B_{\rm resp}<0.
}
\]

Equivalently,

\[
\boxed{
\frac{R_0+3R_s}{\mu_\vartheta^2}
+
(S_0+3S_s)
<
-\frac12.
}
\]

This is the exact local response threshold.

## 5. Frozen-response null control

On the RF-F20/RF-F19 frozen-response surface

\[
R_{\mu\nu}=0,
\qquad
S^{(\vartheta)}_{\mu\nu}=0,
\]

one has

\[
\boxed{
\mathcal B_{\rm resp}=1.
}
\]

Therefore

\[
\boxed{
\Delta(a''/a)_D
=
-\frac{\kappa_E}{3}
\eta\widehat U_L f'(1)
<0
}
\]

on the positive branch.

Thus a metric-insensitive phase-clock projector is pressureless/decelerating and cannot generate dark-energy-like acceleration.

The acceleration effect requires a sufficiently negative off-shell connection and/or phase-scale metric response.

## 6. Standard normalization surface

RF-F17 uses the candidate normalization

\[
f'(1)=\frac12.
\]

At

\[
\eta=1,
\]

the acceleration correction becomes

\[
\boxed{
\Delta\!\left(\frac{a''}{a}\right)_D
=
-\frac{\kappa_E\widehat U_L}{6}
\left[
1
+
2\frac{R_0+3R_s}{\mu_\vartheta^2}
+
2(S_0+3S_s)
\right].
}
\]

The frozen-response limit reproduces the pressureless rank-one source

\[
D_{\mu\nu}
=
\widehat U_L
v_\mu^{(\vartheta)}
v_\nu^{(\vartheta)}.
\]

## 7. Relation to the RF-F15 constant-vacuum mechanism

The RF-F15 integration component

\[
\rho_C=K_0C_\Lambda
\]

is a constant metric-proportional vacuum component.

The RF-F22 projector response \(D_{\mu\nu}\) is a distinct state-dependent non-metric-proportional source.

Therefore the current acceleration ledger contains two separately typed mechanisms:

\[
\boxed{
\text{constant transport integration component}
}
\]

and

\[
\boxed{
\text{state-dependent connection/scale metric response}.
}
\]

They must not be identified or double counted.

## 8. Holonomy firewall

A closed-loop temporal/Berry/Euler holonomy does not by itself fix

\[
R_{\mu\nu}
\]

or

\[
S^{(\vartheta)}_{\mu\nu}.
\]

Thus the threshold above is an exact conditional test, not yet a physical prediction.

The remaining physical bridge is

\[
\boxed{
\text{temporal }U(1)\text{ realization}
\to
(R_{\mu\nu},S^{(\vartheta)}_{\mu\nu})
\to
\mathcal B_{\rm resp}
\to
\Delta(a''/a).
}
\]

## 9. Verdict

For a positive state-dependent interaction, the current RFC stack implies:

\[
\boxed{
\text{frozen phase projector}
\Rightarrow
\text{deceleration},
}
\]

while

\[
\boxed{
\text{acceleration}
\iff
\frac{R_0+3R_s}{\mu_\vartheta^2}
+
(S_0+3S_s)
<
-\frac12.
}
\]

The response threshold is exact conditional mathematics. The physical response tensors remain open inputs.

Reference validator:

TIR/validation/tir_idt_rfc_projector_response_acceleration_threshold_v0_1.py
