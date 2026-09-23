# TIR MUMMU Adaptive Gain Stability Selection No-Go v0.1

Status: `EXACT_FROZEN_EULER_STABILITY_INTERVAL / EXACT_PROJECTED_NONEXPANSIVE_BOUND / CURRENT_DECAY_GAIN_DEEPLY_INTERIOR / STABILITY_DOES_NOT_SELECT_NUMERIC_GAIN / PHYSICAL_RATE_OPEN`

Date: 2026-09-23

## 1. Purpose

The adaptive coupling law now has an exact local projected-gradient form, but
its numerical gains remain source policy values.

This theorem tests whether numerical stability or local Lyapunov descent can
uniquely select the current decay rate

[
d=0.01.
]

They cannot.

## 2. Frozen unconstrained flow

For a frozen phase matrix (C_Phi), no weak-channel term and scalar effective
coefficients (h,d), write

[
dot g
=
hC_Phi-d(g-g_0),
qquad d>0.
]

The unconstrained stationary point is

[
g_*
=
g_0+rac{h}{d}C_Phi.
]

Define

[
e=g-g_*.
]

Then

[
oxed{
dot e=-d e.
}
]

## 3. Explicit Euler update

With step (Delta t>0),

[
g_{n+1}
=
g_n+Delta t
left[
hC_Phi-d(g_n-g_0)
ight].
]

Subtracting (g_*),

[
oxed{
e_{n+1}
=
(1-dDelta t)e_n.
}
]

Therefore convergence requires

[
|1-dDelta t|<1,
]

equivalently

[
oxed{
0<dDelta t<2.
}
]

If one additionally requires no sign reversal/overshoot,

[
oxed{
0<dDelta tle1.
}
]

Neither condition selects one numerical value of (d).

## 4. Exact local Lyapunov descent condition

For the frozen quadratic potential, after completing the square,

[
mathcal F_{HD}(g)
=
rac{d}{2mu}|g-g_*|_F^2+mathrm{const}
]

for any admitted scalar mobility representation.

Under explicit Euler,

[
mathcal F_{n+1}-mathcal F_*
=
(1-dDelta t)^2
(mathcal F_n-mathcal F_*).
]

Hence strict discrete Lyapunov descent is again equivalent to

[
oxed{
0<dDelta t<2.
}
]

Stability and quadratic-energy descent give the same interval, not a unique
gain.

## 5. Box projection

The actual source performs the projection

[
Pi_{mathcal B},
qquad
mathcal B=[-1,1]^{36	imes36}.
]

Euclidean/Frobenius projection onto a closed convex set is nonexpansive:

[
oxed{
|Pi_{mathcal B}(X)-Pi_{mathcal B}(Y)|_F
le
|X-Y|_F.
}
]

Therefore clipping cannot convert the broad admissible interval into a unique
decay gain.

It can change the constrained fixed point and active-set dynamics, but it does
not identify (d).

## 6. Current PNCS margin

The PNCS source uses

[
d=0.01,
qquad
Delta t=0.01.
]

Thus

[
oxed{
dDelta t=10^{-4}.
}
]

The strict Euler upper boundary is

[
dDelta t=2.
]

Therefore the current value sits at

[
oxed{
rac{10^{-4}}{2}
=
5	imes10^{-5}
}
]

of the upper stability boundary.

Equivalently the upper stable decay rate for this step is

[
oxed{
d_{max}
=
rac{2}{Delta t}
=
200,
}
]

so the current (d=0.01) is a factor

[
oxed{
20000
}
]

below that boundary.

For the no-overshoot condition,

[
dle100,
]

still leaving a factor (10000) margin.

## 7. Hebbian coefficient

The frozen linear Hebbian term (hC_Phi) changes the equilibrium location

[
g_*
=
g_0+(h/d)C_Phi
]

but not the Hessian of the frozen quadratic potential.

Therefore the local unconstrained Euler stability condition does not constrain
(h) separately.

The box projection bounds the executed state even when the unconstrained
stationary point lies outside the box.

Thus stability cannot derive the current Hebbian prefactor either.

## 8. Weak-channel coefficient

For a frozen weak-channel linear potential, the local vector field has zero
Hessian.

Its numerical gain changes displacement per step but is not selected by a
quadratic curvature stability condition.

The box projection again provides bounded execution without identifying the
gain.

## 9. Consequence

The current gain values cannot be justified merely by saying that they are
required for numerical stability.

The exact status is

[
oxed{
	ext{stability}
Longrightarrow
	ext{admissible interval},
}
]

not

[
oxed{
	ext{stability}
Longrightarrow
	ext{unique gain}.
}
]

Selecting a particular effective rate requires an independent clock, response
time, empirical target, microscopic action scale, or other source receipt.

## 10. Claim ledger

| Statement | Status |
|---|---|
| frozen error map is (e_{n+1}=(1-dDelta t)e_n) | `EXACT` |
| Euler convergence iff (0<dDelta t<2) | `EXACT` |
| no-overshoot interval is (0<dDelta tle1) | `EXACT` |
| projected box map is nonexpansive | `EXACT STANDARD RESULT` |
| current (d=0.01) is forced by stability at (dt=0.01) | `REFUTED` |
| frozen local stability uniquely fixes Hebbian gain | `REFUTED` |
| weak-channel gain is fixed by quadratic stability | `REFUTED` |
| physical response-time/gain scale | `OPEN` |

## 11. Validation

Deterministic validator:

`TIR/validation/tir_mummu_adaptive_gain_stability_selection_nogo_v0_1.py`

Static receipt:

`TIR/validation/TIR_MUMMU_ADAPTIVE_GAIN_STABILITY_SELECTION_NOGO_VALIDATION_V0_1.json`
