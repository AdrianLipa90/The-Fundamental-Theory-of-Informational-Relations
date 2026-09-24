# TIR MUMMU Coupling Mobility-Gain Identifiability No-Go v0.1

Status: `EXACT_MOBILITY_POTENTIAL_SCALE_GAUGE / EXACT_RUNTIME_PRODUCT_IDENTIFIABILITY / EXACT_FROZEN_EQUILIBRIUM_RATIO / PROPER_TIME_DOES_NOT_SPLIT_MOBILITY_FROM_POTENTIAL_NORMALIZATION / PHYSICAL_MOBILITY_OPEN`

Date: 2026-09-23

## 1. Purpose

The adaptive-coupling variational closure gives the frozen Hebbian+decay flow

[
dot g
=
h,C_Phi
-
d,(g-g_0),
]

with the current PNCS runtime values

[
h=0.1(A-0.5),
qquad
d=0.01.
]

The remaining question is whether these observed flow coefficients uniquely
determine a coupling-space mobility and a potential normalization.

They do not.

This theorem isolates the exact non-identifiability.

## 2. General mobility form

Let the coupling-space gradient flow be

[
oxed{
dot g
=
-mu,
abla_gmathcal F
}
]

with positive scalar mobility

[
mu>0
]

and local potential

[
oxed{
mathcal F(g;Phi)
=
-alphalangle g,C_Phiangle_F
+
rac{eta}{2}|g-g_0|_F^2.
}
]

Then

[

abla_gmathcal F
=
-alpha C_Phi
+
eta(g-g_0),
]

hence

[
oxed{
dot g
=
mualpha,C_Phi
-
mueta,(g-g_0).
}
]

Define the observable/runtime coefficients

[
oxed{
h:=mualpha,
qquad
d:=mueta.
}
]

Therefore the trajectory determines the products ((h,d)), not the three
factors ((mu,alpha,eta)).

## 3. Exact gauge degeneracy

For any

[
c>0,
]

define

[
mu'=cmu,
qquad
alpha'=rac{alpha}{c},
qquad
eta'=rac{eta}{c}.
]

Then

[
mu'alpha'=mualpha=h,
]

and

[
mu'eta'=mueta=d.
]

Therefore

[
oxed{
dot g(mu',alpha',eta')
=
dot g(mu,alpha,eta)
}
]

for every admitted (g) and (C_Phi).

Thus

[
oxed{
(mu,alpha,eta)
sim
(cmu,alpha/c,eta/c)
}
]

is an exact one-parameter identifiability gauge.

No observation of this gradient flow alone can break it.

## 4. What is identifiable

If (C_Phi) and (g-g_0) are linearly independent as matrices at an admitted
section, then the two runtime coefficients (h,d) can in principle be
identified from the local tangent

[
dot g=hC_Phi-d(g-g_0).
]

Their ratio is

[
oxed{
rac{h}{d}
=
rac{alpha}{eta}.
}
]

This ratio is independent of the scalar mobility (mu).

For the current PNCS law,

[
oxed{
rac{h}{d}
=
10(A-0.5).
}
]

For the pinned source activity

[
A
=
0.33444444444444443,
]

one gets

[
oxed{
rac{h}{d}
=
-1.6555555555555557.
}
]

## 5. Frozen unconstrained stationary point

For frozen (C_Phi), no weak-channel term and no active box constraint, the
stationary point satisfies

[
0
=
hC_Phi-d(g_*-g_0).
]

Hence

[
oxed{
g_*
=
g_0
+
rac{h}{d}C_Phi
=
g_0
+
rac{alpha}{eta}C_Phi.
}
]

Again the stationary geometry depends on the potential ratio
(alpha/eta), not on mobility.

For the pinned activity,

[
g_*
=
g_0
-
1.6555555555,C_Phi.
]

Because this unconstrained candidate can exceed the declared box
([-1,1]), the actual bounded long-time problem is a projected/constrained
flow rather than this unconstrained stationary formula.

No claim is made here about its global attractor.

## 6. A second time-scale degeneracy before clock binding

If only the unparameterized coupling-space path is observed, then

[
(h,d)
mapsto
(s h,s d),
qquad
tmapsto t/s,
]

traverses the same frozen gradient-flow orbit at a different rate.

Thus before an independent clock binding:

[
oxed{
	ext{orbit shape}
Rightarrow
h/d,
}
]

while the common rate remains clock-gauge-like.

A typed coordinate/proper-time receipt can calibrate that common rate.

## 7. Why proper time does not solve the mobility split

Suppose an independent receipt fixes

[
d	au=q,dt,
qquad q>0.
]

Then

[
rac{dg}{d	au}
=
rac1q
left[
hC_Phi-d(g-g_0)
ight].
]

Sufficient trajectory data can therefore calibrate the proper-time rates

[
h/q,qquad d/q
]

and, when (q) is independently known, recover (h,d).

But even exact knowledge of (h,d) leaves

[
h=mualpha,
qquad
d=mueta
]

with the gauge

[
(mu,alpha,eta)
sim
(cmu,alpha/c,eta/c).
]

Therefore

[
oxed{
	ext{proper-time binding fixes flow rate but not mobility/potential factorization}.
}
]

## 8. Weak-channel sector

For a frozen weak-channel drive

[
W_Phi
]

with potential

[
mathcal F_W=-zetalangle g,widetilde W_Phiangle_F,
]

the same issue occurs:

[
dot g_W
=
muzeta,widetilde W_Phi.
]

Only the product

[
muzeta
]

is dynamically identifiable unless mobility is independently fixed.

Thus adding the weak-channel term does not break the mobility-normalization
degeneracy.

## 9. Consequence for the current PNCS numbers

The existing runtime values

[
0.1,qquad0.01,qquad0.1
]

can be interpreted exactly as **effective flow coefficients** in the current
coordinate-time convention.

They are not, from the present source evidence, separately identified as:

- a mobility;
- an energy/action normalization;
- a physical damping coefficient;
- a microscopic coupling constant.

Assigning any of those roles requires an independent metric/mobility or
physical-action receipt.

## 10. Minimal closure object

The missing object can now be typed narrowly as a positive coupling-space
metric or mobility operator

[
oxed{
mathsf M_g
:
T_g^*mathcal G
	o
T_gmathcal G,
qquad
mathsf M_g>0,
}
]

such that

[
oxed{
dot g
=
-mathsf M_g
abla_gmathcal F.
}
]

For the present implementation,

[
mathsf M_g=mu I
]

is an admissible scalar candidate, but its normalization is not source-derived.

A nontrivial (mathsf M_g) must be independently specified and then tested
against the source update; it must not be inferred by absorbing arbitrary
potential coefficients.

## 11. Claim ledger

| Statement | Status |
|---|---|
| runtime flow identifies (h=mualpha), (d=mueta) | `EXACT` |
| ((mu,alpha,eta)	o(cmu,alpha/c,eta/c)) leaves flow invariant | `EXACT` |
| (h/d=alpha/eta) is mobility independent | `EXACT` |
| frozen unconstrained (g_*=g_0+(h/d)C_Phi) | `EXACT CONDITIONAL` |
| unparameterized orbit fixes common rate | `REFUTED` |
| independent proper time can calibrate (h,d) | `EXACT CONDITIONAL` |
| proper time uniquely splits mobility from potential normalization | `REFUTED` |
| current numeric gains uniquely determine a microscopic mobility | `REFUTED` |
| source-derived coupling-space mobility/metric exists | `OPEN / NOT FOUND` |

## 12. Validation

Deterministic validator:

`TIR/validation/tir_mummu_coupling_mobility_gain_identifiability_nogo_v0_1.py`

Static receipt:

`TIR/validation/TIR_MUMMU_COUPLING_MOBILITY_GAIN_IDENTIFIABILITY_NOGO_VALIDATION_V0_1.json`


## 13. Stability does not select the effective rate

The effective decay coefficient itself is not selected uniquely by local
numerical stability.

See:

`TIR_MUMMU_ADAPTIVE_GAIN_STABILITY_SELECTION_NOGO_V0_1.md`.

For the frozen explicit-Euler flow,

[
e_{n+1}
=
(1-dDelta t)e_n,
]

so strict convergence and quadratic Lyapunov descent require only

[
oxed{
0<dDelta t<2.
}
]

At the source values

[
d=0.01,qquadDelta t=0.01,
]

one has

[
dDelta t=10^{-4},
]

which is (20000) times below the upper stability boundary in (d).

Thus neither the mobility/potential factorization nor the effective decay rate
is fixed by stability. An independent response-time, clock or microscopic scale
is required for numerical gain selection.
