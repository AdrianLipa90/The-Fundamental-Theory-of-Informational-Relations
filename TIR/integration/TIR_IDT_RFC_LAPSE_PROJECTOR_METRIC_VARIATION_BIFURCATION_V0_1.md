# TIR × IDT × RFC Lapse–Projector Metric-Variation Bifurcation v0.1

Status: INDEPENDENT_CALIBRATION_BRANCH_RECOVERS_RF_F18_RF_F19 / SAME_METRIC_LAPSE_SELF_NORMALIZATION_NO_GO / PROJECTOR_STRESS_VANISHES_ON_SAME_METRIC_COMMON_RATE_BRANCH / DARK_ENERGY_FROM_LAPSE_REIDENTIFICATION_DENIED

Date: 2026-09-24

## 1. Purpose

RF-F18 requires the phase-scale calibration \(\mu_\vartheta\) to be independent during metric variation. It proves that self-normalizing the projector by the same metric norm makes

\[
\mathcal C_\vartheta\equiv1
\]

off shell and therefore gives

\[
\delta_g\mathcal C_\vartheta=0.
\]

RF-F19 later supplies an independently evaluated rotor/lapse calibration

\[
\mu_\vartheta
=
\frac{|r_t^{rot}|}{N_Rc}.
\]

RFC RF-E8 also uses \(N_R\) as the ADM lapse in the block metric.

This gate separates two logically distinct variational choices.

## 2. Branch A — independent upstream calibration

RF-F18/RF-F19 promotion uses

\[
\boxed{
\left.
\frac{\partial\mu_\vartheta}{\partial g^{\mu\nu}}
\right|_{\rm metric\ variation}
=0.
}
\]

Equivalently,

\[
\boxed{
S_{\mu\nu}^{(\vartheta)}=0.
}
\]

This means the independently evaluated rotor/lapse data are held fixed while the local spacetime metric is varied.

On the frozen one-form branch,

\[
R_{\mu\nu}=0,
\]

the projector derivative is

\[
\boxed{
\frac{\partial\mathcal C_\vartheta}{\partial g^{\mu\nu}}
=
-\frac{q_\mu q_\nu}{\mu_\vartheta^2}.
}
\]

Hence the RF-F17/RF-F18 interaction produces the pressureless rank-one source

\[
\boxed{
T^U_{\mu\nu}
=
2\widehat U_L f'(1)
v_\mu^{(\vartheta)}
v_\nu^{(\vartheta)}
}
\]

at \(\eta=1\).

For positive \(\widehat U_L f'(1)\), this branch is decelerating in FLRW.

## 3. Branch B — same-metric ADM lapse reconstruction

Suppose instead that the same \(N_R\) appearing in the calibration is reconstructed from the metric being varied.

RF-E8 gives exactly

\[
\boxed{
g^{00}=-\frac1{N_R^2},
}
\]

hence

\[
\boxed{
N_R=(-g^{00})^{-1/2}.
}
\]

Take zero shift locally for clarity and hold the coordinate rotor rate \(r_t^{rot}\) fixed.

Then

\[
\mu_\vartheta
=
\frac{|r_t^{rot}|}{N_Rc}
\]

is no longer metric-independent.

For the inverse-metric variation,

\[
\boxed{
\frac{\partial\ln N_R}{\partial g^{00}}
=
-\frac1{2g^{00}}
=
\frac{N_R^2}{2}.
}
\]

Thus

\[
\boxed{
S^{N}_{00}
=
\frac{N_R^2}{2},
}
\]

while fixed \(r_t^{rot}\) gives

\[
S^{rot}_{00}=0.
\]

RF-F19 therefore gives

\[
\boxed{
S^{(\vartheta)}_{00}
=
-S^N_{00}
=
-\frac{N_R^2}{2}.
}
\]

## 4. Exact cancellation on the common-rate pure-normal surface

On the pure-normal common-rate surface,

\[
\mathcal C_\vartheta=1.
\]

Using

\[
-g^{00}\frac{q_0^2}{\mu_\vartheta^2}=1
\]

and

\[
g^{00}=-\frac1{N_R^2},
\]

one gets

\[
\boxed{
\frac{q_0^2}{\mu_\vartheta^2}
=
N_R^2.
}
\]

With frozen connection response \(R_{\mu\nu}=0\), the RF-F19 full derivative is

\[
\frac{\partial\mathcal C_\vartheta}{\partial g^{00}}
=
-\frac{q_0^2}{\mu_\vartheta^2}
-
2\mathcal C_\vartheta S^{(\vartheta)}_{00}.
\]

Substitution yields

\[
\boxed{
\frac{\partial\mathcal C_\vartheta}{\partial g^{00}}
=
-N_R^2
+
N_R^2
=
0.
}
\]

The spatial components vanish on the pure-normal same-metric branch as well.

Therefore

\[
\boxed{
\frac{\partial\mathcal C_\vartheta}{\partial g^{\mu\nu}}
=0.
}
\]

## 5. Projector stress no-go

RF-F17 gives

\[
T^U_{\mu\nu}
=
-2\eta\widehat U_L f'(1)
\frac{\partial\mathcal C_\vartheta}{\partial g^{\mu\nu}}
\]

on the projector surface.

Hence on the same-metric lapse/common-rate/frozen-connection branch,

\[
\boxed{
T^U_{\mu\nu}=0.
}
\]

This is exactly the RF-F18 self-normalization no-go, expressed through the RFC ADM lapse identity.

Therefore one may not obtain a new gravitational source by:

1. defining \(\mu_\vartheta\) through \(N_R\);
2. identifying that \(N_R\) with the same lapse extracted from \(g^{00}\);
3. varying \(g^{00}\);
4. while still treating \(\mu_\vartheta\) as an independent calibration.

Those assumptions are mutually incompatible.

## 6. Variational bifurcation

The two valid branches are:

### A. Independent calibration branch

\[
\boxed{
\delta_g\mu_\vartheta=0.
}
\]

Then the projector can have nonzero stress, but its frozen-response part is rank-one/decelerating.

### B. Same-metric self-normalized branch

\[
\boxed{
\mu_\vartheta\propto(-g^{00})^{1/2}
}
\]

on the pure-normal common-rate surface.

Then

\[
\boxed{
\delta_g\mathcal C_\vartheta=0
}
\]

and the projector interaction stress vanishes.

There is no third branch obtained by mixing the two variational rules.

## 7. Consequence for the acceleration frontier

The phase-clock lapse alone does not generate a dark-energy-like projector stress.

On the independent branch, acceleration still requires the previously derived response threshold

\[
\boxed{
\frac{R_0+3R_s}{\mu_\vartheta^2}
+
(S_0+3S_s)
<
-\frac12
}
\]

from additional physical metric response.

On the same-metric self-normalized branch, the projector source is zero before this interpretation can be made.

Thus any nonzero accelerating projector source must come from a genuinely independent metric-sensitive physical adapter rather than from reusing the same lapse normalization.

## 8. Verdict

\[
\boxed{
\text{ADM lapse reidentification}
\neq
\text{new dark-energy source}.
}
\]

More strongly,

\[
\boxed{
\text{same-metric lapse calibration}
\Rightarrow
\text{projector self-normalization}
\Rightarrow
T^U_{\mu\nu}=0
}
\]

on the pure-normal common-rate frozen-connection branch.

Reference validator:

TIR/validation/tir_idt_rfc_lapse_projector_metric_variation_bifurcation_v0_1.py
