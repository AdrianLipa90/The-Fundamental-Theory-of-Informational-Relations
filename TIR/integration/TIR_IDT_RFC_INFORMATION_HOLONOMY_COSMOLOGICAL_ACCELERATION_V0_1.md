# TIR × IDT × RFC Information-Holonomy Cosmological Acceleration Gate v0.1

Status: RF_E13_FLAT_FLRW_ACCELERATION_PASS / INFORMATION_SCALAR_ACCELERATION_CRITERION_EXACT_LOCAL / BARE_LAMBDA_NOT_REQUIRED_ON_INFORMATION_SCALAR_ACTION_ROUTE / CURRENT_HOLONOMY_SPECTATOR_NO_GO / EQUAL_STRESS_HOLONOMY_PARTITION_NO_GO / HOLONOMY_D_CHANNEL_DIFFERENTIAL_STRESS_ATTRIBUTION_CANDIDATE / ABSOLUTE_ALPHA_AND_HOLONOMY_PERSISTENCE_OPEN

Date: 2026-09-24

## 1. Purpose

This gate asks the narrow cosmological question left by the current gravity spine:

\[
\boxed{
\text{Can the already admitted TIR/IDT/RFC source dynamics produce }
\ddot a>0
\text{ without inserting an independent bare cosmological constant?}
}
\]

The answer splits into two distinct results.

First, the existing RFC canonical information-scalar action already permits accelerated FLRW evolution when its potential dominates its kinetic term. A separate bare \(\Lambda\) is not mathematically required for that mechanism.

Second, the currently admitted temporal holonomy coordinate \(\tau_R\) is preserved by the RF-L3 scalar reconstruction but is not present in the scalar potential. Therefore the current action does not derive dark-energy-like acceleration from holonomy itself.

This gate records both the positive acceleration theorem and the holonomy no-go.

## 2. Pinned parent equations

RFC RF-E9 fixes

\[
\boxed{
K_{ij}=-\frac12\mathcal L_nh_{ij}.
}
\]

RFC RF-E12 supplies the base Hamiltonian constraint

\[
\boxed{
{}^{(3)}R+K^2-K_{ij}K^{ij}
=2\kappa_E\rho.
}
\]

RFC RF-E13 supplies

\[
\boxed{
(\partial_0-\mathcal L_b)h_{ij}=-2NK_{ij}
}
\]

and

\[
\boxed{
(\partial_0-\mathcal L_b)K_{ij}
=
-D_iD_jN
+N\left({}^{(3)}R_{ij}+KK_{ij}-2K_{ik}K^k{}_j\right)
+N\kappa_E\left[
\frac12h_{ij}(S-\rho)-S_{ij}
\right].
}
\]

The RFC temporal coordinate is

\[
x^0=ct.
\]

RF-L2 supplies a canonical scalar action and RF-L3/RF-L4A supply

\[
\boxed{
U_I=\frac{\alpha_I}{\kappa_E}\Xi_I,
\qquad
\phi_I=\sqrt{2\Xi_I}
}
\]

on the local zero-baseline Fisher-normalized information chart.

IDT 01K supplies

\[
\boxed{
\Xi_I
=
\frac{\mathcal J_\pi}{a_{FS}}
\left(\frac{\omega}{c}\right)^2
}
\]

on a constant-rate projective cell.

IDT 01L/01L2 preserve the oriented temporal holonomy

\[
\boxed{
\tau_R=\operatorname{wrap}_\pi\Phi_T(C),
\qquad
h_R=e^{i\tau_R}.
}
\]

## 3. Flat-FLRW reduction of RF-E12/RF-E13

Take the flat homogeneous/isotropic sector

\[
N=1,
\qquad
b^i=0,
\qquad
h_{ij}=a(x^0)^2\delta_{ij},
\qquad
{}^{(3)}R_{ij}=0.
\]

Define

\[
\boxed{
H_0:=\frac{a'}a,
\qquad
{}'=\partial_0.
}
\]

RF-E9 gives

\[
\boxed{
K_{ij}=-H_0h_{ij},
\qquad
K=-3H_0.
}
\]

For a perfect-fluid source,

\[
S_{ij}=ph_{ij},
\qquad
S=3p.
\]

RF-E12 then gives

\[
\boxed{
3H_0^2=\kappa_E\rho.
}
\]

Substitution into RF-E13 gives

\[
\boxed{
H_0'=-\frac{\kappa_E}{2}(\rho+p).
}
\]

Therefore

\[
\frac{a''}{a}
=H_0'+H_0^2
\]

becomes

\[
\boxed{
\frac{a''}{a}
=
-\frac{\kappa_E}{6}(\rho+3p).
}
\]

In physical time \(t\), because \(x^0=ct\),

\[
\boxed{
\frac{\ddot a}{a}
=
-\frac{\kappa_Ec^2}{6}(\rho+3p).
}
\]

Thus acceleration requires

\[
\boxed{\rho+3p<0}
\]

on the base Einstein branch.

The event-derived metric rate does not by itself imply acceleration. It supplies the geometric evolution data that the source equations must satisfy.

## 4. Canonical information-scalar acceleration theorem

For a homogeneous canonical information field on the local RF-L2/RF-L4A chart, write derivatives with respect to \(x^0\):

\[
K_I=\frac12(\phi_I')^2,
\]

\[
\boxed{
\rho_I
=
\frac12(\phi_I')^2+U_I,
\qquad
p_I
=
\frac12(\phi_I')^2-U_I.
}
\]

Hence

\[
\rho_I+3p_I
=
2(\phi_I')^2-2U_I.
\]

The RF-E13 acceleration equation gives

\[
\boxed{
\frac{a''}{a}\Big|_I
=
\frac{\kappa_E}{3}
\left(
U_I-(\phi_I')^2
\right).
}
\]

Using

\[
\phi_I=\sqrt{2\Xi_I},
\]

one has

\[
(\phi_I')^2
=
\frac{(\Xi_I')^2}{2\Xi_I}.
\]

Using

\[
U_I=\frac{\alpha_I}{\kappa_E}\Xi_I,
\]

the acceleration becomes

\[
\boxed{
\frac{a''}{a}\Big|_I
=
\frac{\alpha_I\Xi_I}{3}
-
\frac{\kappa_E}{6\Xi_I}(\Xi_I')^2.
}
\]

For \(\Xi_I>0\) and \(\alpha_I>0\),

\[
\boxed{
\frac{a''}{a}>0
\iff
\left|
\partial_0\ln\Xi_I
\right|
<
\sqrt{\frac{2\alpha_I}{\kappa_E}}.
}
\]

Since RF-L4A gives

\[
m_I^2=\frac{\alpha_I}{\kappa_E},
\]

the same condition is

\[
\boxed{
\left|\partial_0\ln\Xi_I\right|
<
\sqrt2\,m_I.
}
\]

In physical time,

\[
\boxed{
\left|\partial_t\ln\Xi_I\right|
<
\sqrt2\,c\,m_I.
}
\]

This is a local dynamical acceleration criterion. It is not yet an absolute prediction because the physical normalization of \(m_I\), equivalently \(\alpha_I\), remains open.

## 5. No bare Lambda required, but no double counting allowed

The RF-L2 scalar admits two algebraically equivalent bookkeeping representations.

### Representation A — full scalar stress on the source side

Use

\[
T_{\mu\nu}^{I}
=
T_{\mu\nu}^{kin}
-U_Ig_{\mu\nu}
\]

with no information-sector \(\Lambda_I\) inserted separately on the geometric side.

### Representation B — dynamic-Lambda split

Move the potential term to the geometric side:

\[
\boxed{
\Lambda_I=\kappa_EU_I=\alpha_I\Xi_I
}
\]

and leave only the scalar kinetic tensor in the displayed matter ledger.

For FLRW,

\[
-\frac{\kappa_E}{6}
\left[
(K_I+U_I)+3(K_I-U_I)
\right]
\]

equals exactly

\[
-\frac{\kappa_E}{6}(K_I+3K_I)
+
\frac{\Lambda_I}{3}.
\]

Therefore

\[
\boxed{
\text{full scalar representation}
=
\text{dynamic-Lambda representation}.
}
\]

The same \(U_I\) must never be counted simultaneously in \(T_{\mu\nu}\) and in \(\Lambda_Ig_{\mu\nu}\).

The acceleration mechanism therefore does not require an additional bare \(\Lambda\), but it does require the already-open physical normalization and realization of the information scalar.

## 6. Phase-clock form of the acceleration criterion

IDT 01K gives

\[
\Xi_I
=
\frac{\mathcal J_\pi}{a_{FS}}
\left(\frac{\omega}{c}\right)^2.
\]

Hence

\[
\boxed{
\partial_t\ln\Xi_I
=
\partial_t\ln\mathcal J_\pi
-
\partial_t\ln a_{FS}
+
2\partial_t\ln|\omega|.
}
\]

For constant dimensionless projective area,

\[
\boxed{
\partial_t\ln\Xi_I
=
\frac{\dot{\mathcal J}_\pi}{\mathcal J_\pi}
+
2\frac{\dot\omega}{\omega}.
}
\]

Therefore the information-sector acceleration gate can be tested directly from information redistribution, projective area evolution and phase-rate evolution.

RF-L5 states that if an independently admitted physical phase-clock spectral line satisfies

\[
\omega_t^{(KG)}=|\omega_{phase}|,
\]

then

\[
m_I^2=\left(\frac{\omega_{phase}}{c}\right)^2
\]

and the sign condition becomes

\[
\boxed{
\left|\partial_t\ln\Xi_I\right|
<
\sqrt2\,|\omega_{phase}|.
}
\]

This last reduction is conditional on an independent spectral identification.

If the same phase observable is used both to construct \(\Xi_I\) and to calibrate \(m_I\) without an independent receipt, the comparison is circular and cannot be promoted as a prediction.

## 7. Event-snapshot acceleration estimator

The event-spatial source contract already supplies source-bound spatial metrics.

For an isotropic FLRW snapshot,

\[
\det h=a^6.
\]

Define

\[
\boxed{
y:=\ln a
=
\frac16\ln\det h.
}
\]

Then

\[
\boxed{
\frac{a''}{a}
=
y''+(y')^2.
}
\]

For three equally spaced event snapshots in \(x^0\),

\[
x^0_{n-1},
\quad
x^0_n,
\quad
x^0_{n+1},
\]

define

\[
y_n=\frac16\ln\det h_n.
\]

The centered source estimator is

\[
\boxed{
y'_n
\approx
\frac{y_{n+1}-y_{n-1}}{2\Delta x^0},
}
\]

\[
\boxed{
y''_n
\approx
\frac{y_{n+1}-2y_n+y_{n-1}}{(\Delta x^0)^2},
}
\]

and therefore

\[
\boxed{
\mathcal A_n^{event}
=
\frac{y_{n+1}-2y_n+y_{n-1}}{(\Delta x^0)^2}
+
\left(
\frac{y_{n+1}-y_{n-1}}{2\Delta x^0}
\right)^2.
}
\]

On a smooth event refinement this is second-order accurate.

The physical-time acceleration is

\[
\boxed{
\frac{\ddot a}{a}
=
c^2\mathcal A^{event}.
}
\]

This provides a source-model-independent observable side of the test.

## 8. Current holonomy spectator no-go

The current RF-L3 / IDT 01L2 action bridge is

\[
\boxed{
(\Xi_I,\tau_R)
\longmapsto
(\Lambda_{ref}+\alpha_I\Xi_I,\tau_R)
\longmapsto
(U_I,\tau_R).
}
\]

Therefore

\[
\boxed{
U_I=U_I(\Xi_I),
\qquad
\frac{\partial U_I}{\partial\tau_R}=0.
}
\]

The temporal holonomy is preserved as an oriented coordinate but is a spectator in the current scalar stress-energy.

Consequently,

\[
\boxed{
\text{current RF-L3 action does not derive dark-energy acceleration from }\tau_R.
}
\]

This is a no-go for the present action, not a no-go for every possible holonomy-active completion.

## 9. Equal-stress partition no-go

IDT 01L defines

\[
\boxed{
C_h=\cos^2\frac{\tau_R}{2},
\qquad
D_h=\sin^2\frac{\tau_R}{2},
\qquad
C_h+D_h=1.
}
\]

If the information potential is merely partitioned as

\[
U_C=U_IC_h,
\qquad
U_D=U_ID_h
\]

and both channels carry the same gravitational stress type, then

\[
\boxed{
U_C+U_D
=
U_I(C_h+D_h)
=
U_I.
}
\]

Hence all \(\tau_R\)-dependence cancels from the total potential.

Therefore naming \(D_h\) a dark channel does not create dark energy.

A gravitational holonomy effect requires at least one of:

1. different physical stress attribution for the two channels;
2. an independently derived \(\tau_R\)-dependent action term;
3. a dynamical holonomy field with its own kinetic/geometric stress;
4. a topologically frozen sector whose global contribution is not reducible to an equal local partition.

## 10. Minimal no-new-relative-coefficient holonomy-active candidate

On the already-admitted joint-information action surface RF-S8 gives

\[
\boxed{
\alpha_{clk}=\alpha_I=\alpha_J.
}
\]

Thus no additional relative clock/information coupling is required on that conditional surface.

If the existing \(D_h\) channel is independently shown to carry metric-proportional vacuum stress while its complementary channel receives its own conservation-compatible stress ledger, the minimal candidate is

\[
\boxed{
\Lambda_D
=
\alpha_I\Xi_I D_h
=
\alpha_I\Xi_I
\sin^2\frac{\tau_R}{2}.
}
\]

Equivalently,

\[
\boxed{
U_D
=
\frac{\alpha_I}{\kappa_E}\Xi_I
\sin^2\frac{\tau_R}{2}.
}
\]

This introduces no new relative dimensionless coefficient beyond the already present \(\alpha_I\).

However, the physical stress attribution is not derived by the partition identity itself. The complementary \(C_h\) ledger must also be specified so that energy-momentum conservation and the Bianchi identity remain closed.

The candidate is therefore not promoted.

## 11. Persistence/stability obstruction for the naive dynamical holonomy potential

Suppose, only as a diagnostic, that \(\tau_R\) is promoted to a local canonical coordinate and the candidate potential contains

\[
U_D(\tau_R)=U_I\sin^2\frac{\tau_R}{2}
\]

with \(U_I>0\) held fixed.

Then

\[
\frac{\partial U_D}{\partial\tau_R}
=
\frac{U_I}{2}\sin\tau_R
\]

and

\[
\boxed{
\frac{\partial^2U_D}{\partial\tau_R^2}
=
\frac{U_I}{2}\cos\tau_R.
}
\]

At

\[
\tau_R=0,
\]

the \(D\) fraction is zero and the coordinate curvature is positive.

At

\[
\tau_R=\pi,
\]

the \(D\) fraction is maximal,

\[
D_h=1,
\]

but

\[
\boxed{
\frac{\partial^2U_D}{\partial\tau_R^2}
=
-\frac{U_I}{2}<0.
}
\]

Thus the maximal nontrivial \(D\)-sector is a potential maximum in the naive positive-kinetic local scalar realization.

This does not exclude a topologically frozen global holonomy sector, because a global Wilson-loop/holonomy coordinate need not be a freely variable local scalar. It does exclude claiming local dynamical stability from the simple single-cosine partition alone.

## 12. Exact versus candidate status

### Exact / conditional-exact on admitted parents

- flat-FLRW reduction of RF-E12/RF-E13;
- acceleration equation \(a''/a=-\kappa_E(\rho+3p)/6\);
- canonical information-scalar acceleration formula;
- \(\Xi_I\) logarithmic rate identity;
- equality of full-scalar and dynamic-Lambda bookkeeping;
- second-order event-snapshot acceleration estimator;
- current RF-L3 holonomy spectator result;
- \(C_h+D_h=1\) equal-stress partition no-go;
- coordinate Hessian classification of the naive \(D_h\) potential.

### Candidate / open physical binding

- absolute \(\alpha_I\) or \(m_I\) normalization;
- independent KG/phase spectral identification;
- production event-spatial cosmology realization;
- physical differential stress attribution of \(C_h\) and \(D_h\);
- conservation-compatible complementary-channel ledger;
- dynamical or topological persistence of nontrivial holonomy;
- observational late-time acceleration fit and perturbation/growth tests.

## 13. Current verdict

The present project supports the following precise statement:

\[
\boxed{
\text{An information-scalar potential can source accelerated expansion without an additional bare }\Lambda.
}
\]

It does not yet support

\[
\boxed{
\text{temporal holonomy itself is the physical dark-energy source}.
}
\]

To make that stronger statement, the smallest remaining gate is

\[
\boxed{
\text{holonomy}
\to
\text{differential stress attribution or derived holonomy-active action}
\to
T_{\mu\nu}^{hol}
}
\]

with Bianchi closure, stability/persistence and independent physical normalization.

Reference validator:

TIR/validation/tir_idt_rfc_information_holonomy_cosmological_acceleration_v0_1.py
