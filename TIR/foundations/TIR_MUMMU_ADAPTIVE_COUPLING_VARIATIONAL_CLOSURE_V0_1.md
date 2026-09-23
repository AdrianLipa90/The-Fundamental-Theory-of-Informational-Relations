# TIR MUMMU Adaptive Coupling Variational Closure v0.1

Status: `EXACT_LOCAL_GRADIENT_FLOW_REPRESENTATION / EXACT_PROJECTED_EULER_BOX_STEP / GREMLIN_PHASE_POTENTIAL_DUALITY / GAIN_VALUES_NOT_DERIVED / PHYSICAL_BINDING_OPEN`

Date: 2026-09-23

## 1. Purpose

The source-operator firewall isolates the local origin of QHTRI operator
curvature in the adaptive coupling update.

The next question is whether that update is merely an algorithmic collection of
terms or whether it admits a variational representation.

It does.

For each frozen source section, the PNCS coupling update is exactly a projected
gradient-flow step in coupling-matrix space.

This closes the **form** of the adaptive law. It does not derive the numerical
gain values or a physical microscopic substrate.

## 2. Source contracts

PNCS source pin:

`AdrianLipa90/PhaseNav-Natural-Coding-System@8855abed440e9949f576ffbe2153325f69e78963`.

Relevant source:

`src/phasenav_natural_code/semantic_htri_drive_v32.py`.

GREMLIN source pin:

`AdrianLipa90/GREMLIN@e1e617b03406e38946a3b5296db5cfd259cca3df`.

Relevant source:

`spec/GREMLIN_COGNITIVE_ACTION_PRINCIPLE_V0_1.md`.

GREMLIN already declares the Kuramoto phase potential

[
V_{m phase}
=
-sum_{i<j}
K_{ij}cos(	heta_i-	heta_j),
]

with phase force given by its negative phase gradient.

## 3. PNCS coupling vector field

At one frozen source section define the harmonic-composite phase matrix

[
oxed{
(C_Phi)_{ij}
=
cos(Phi_i-Phi_j).
}
]

Let the source activity scalar be (A).

The PNCS update coefficients per unit coordinate time are

[
oxed{
lambda_H
=
0.1(A-0.5),
qquad
gamma
=
0.01.
}
]

Let

[
g_0=0.1I.
]

The weak-channel rule defines a state-conditioned symmetric matrix (W_Phi)
whose admitted within-channel off-diagonal entries equal

[
0.1(0.5-R_c)d_c
]

when the corresponding weak-channel predicate is true and vanish otherwise.

Before clipping, the source update is exactly

[
oxed{
dot g
=
lambda_H C_Phi
-
gamma(g-g_0)
+
W_Phi.
}
]

The executable step is

[
oxed{
g^+
=
Pi_{[-1,1]}
left(
g+Delta t,dot g
ight),
}
]

where the projection is entrywise clipping.

## 4. Local coupling potential

Use the Frobenius inner product

[
langle A,Bangle_F
=
operatorname{Tr}(A^TB).
]

For a frozen source section define

[
oxed{
mathcal F_g(g;Phi)
=
-lambda_H
langle g,C_Phiangle_F
+
rac{gamma}{2}
|g-g_0|_F^2
-
langle g,W_Phiangle_F.
}
]

Its matrix gradient is

[

abla_gmathcal F_g
=
-lambda_H C_Phi
+
gamma(g-g_0)
-
W_Phi.
]

Therefore

[
oxed{
-
abla_gmathcal F_g
=
lambda_H C_Phi
-
gamma(g-g_0)
+
W_Phi
=
dot g.
}
]

Thus the preclip PNCS adaptive coupling law is exactly local gradient flow.

## 5. Relation to the GREMLIN phase potential

The first term is the coupling-space dual of the existing GREMLIN phase
potential.

For one edge,

[
V_{ij}
=
-K_{ij}cos(	heta_i-	heta_j).
]

Therefore

[
-rac{partial V_{ij}}{partial K_{ij}}
=
cos(	heta_i-	heta_j).
]

The PNCS Hebbian direction is exactly this coupling-coordinate gradient,
multiplied by the signed state-dependent gain (lambda_H).

Hence the same cosine relation appears in two dual derivatives:

[
oxed{
-partial_{	heta_i}V_{m phase}
;Rightarrow;
	ext{phase force},
}
]

and

[
oxed{
-partial_{K_{ij}}V_{m phase}
;Rightarrow;
	ext{coupling adaptation direction}.
}
]

This is an exact mathematical duality of the declared potential.

It does not establish a physical ontology.

## 6. Local Lyapunov law

If (Phi), (A), and the weak-channel matrix (W_Phi) are held fixed over
the local section and clipping is inactive, then

[
dot g
=
-
abla_gmathcal F_g.
]

Therefore

[
oxed{
rac{dmathcal F_g}{dt}
=
langle

abla_gmathcal F_g,
dot g
angle_F
=
-|
abla_gmathcal F_g|_F^2
le0.
}
]

Equality holds exactly at a local stationary coupling state.

This monotonicity is local/frozen-state. Along the full source trajectory,
(Phi), activity and weak-channel membership change, so the potential itself
is explicitly time/state dependent.

## 7. Box constraint as projected gradient flow

The source code applies

[
g_{ij}in[-1,1]
]

by entrywise clipping after the explicit update.

For the convex box

[
mathcal B
=
[-1,1]^{36	imes36},
]

entrywise clipping is the Euclidean/Frobenius projection

[
Pi_{mathcal B}.
]

Thus the executable source step has the exact optimization form

[
oxed{
g^+
=
Pi_{mathcal B}
left[
g-Delta t,
abla_gmathcal F_g
ight].
}
]

No additional optimizer is hidden.

## 8. Deterministic source validation

On the pinned PNCS snapshot the validator reconstructs independently:

- harmonic-composite (C_Phi);
- activity (A);
- weak-channel mask and boost matrix;
- source (Delta g);
- (-Delta t
abla_gmathcal F_g).

The reconstructed update agrees with the source update to floating-point
precision before clipping.

For the initial pinned section the weak-channel mask is empty, so

[
W_Phi=0.
]

The coupling update is therefore exactly the two-term gradient flow

[
dot g
=
lambda_H C_Phi
-gamma(g-g_0).
]

## 9. What is now closed

The adaptive coupling **form** is no longer an arbitrary unexplained update:

[
oxed{
	ext{phase relation}
+
	ext{quadratic regularization}
+
	ext{state-conditioned weak-edge drive}
Longrightarrow
	ext{projected gradient coupling flow}.
}
]

Combined with the source-operator firewall,

[
[j,C_Phi]
eq0
]

then explains why this variational adaptation rotates the normalized coupling
operator and produces path ordering.

## 10. What remains open

The variational representation does not derive:

- the numerical Hebbian prefactor (0.1);
- the activity offset (0.5);
- the decay rate (0.01);
- the baseline (0.1I);
- the weak-channel gain (0.1);
- the physical/proper-time scale;
- a microscopic physical meaning of (g).

These remain source/runtime policy parameters unless independently derived.

The next fundamental gate is therefore narrower:

[
oxed{
	ext{derive the metric/mobility and gain scales of this gradient flow}.
}
]

## 11. Claim ledger

| Statement | Status |
|---|---|
| preclip PNCS (g)-update is a matrix gradient flow | `EXACT` |
| clipping is Frobenius projection onto the coupling box | `EXACT` |
| frozen-state potential is nonincreasing along its gradient flow | `EXACT` |
| PNCS cosine update is dual to GREMLIN Kuramoto phase potential in coupling coordinates | `EXACT MATHEMATICAL CROSSWALK` |
| full time-varying source has one global autonomous Lyapunov function | `NOT CLAIMED` |
| gain values are derived fundamental constants | `OPEN / NOT CLAIMED` |
| physical microscopic substrate | `OPEN / NOT CLAIMED` |

## 12. Validation

Deterministic validator:

`TIR/validation/tir_mummu_adaptive_coupling_variational_closure_v0_1.py`

Static receipt:

`TIR/validation/TIR_MUMMU_ADAPTIVE_COUPLING_VARIATIONAL_CLOSURE_VALIDATION_V0_1.json`
