# TIR MUMMU Activity-Controlled Operator-Curvature Bifurcation v0.1

Status: `EXACT_ACTIVITY_HYPERPLANE / EXACT_HEBBIAN_CURVATURE_SIGN_BIFURCATION / CONDITIONAL_BARYCENTRIC_INTERPRETATION / ACTIVITY_WEIGHTS_NOT_DERIVED / PHYSICAL_BINDING_OPEN`

Date: 2026-09-23

## 1. Purpose

The source-operator firewall gives the infinitesimal normalized-coupling rotation

[
[J,dot J]
=
rac{lambda_H}{ho^2}
[j,C_Phi]
]

when the weak-channel boost is inactive and the local normalized-decay direction
cancels.

This theorem resolves the source state dependence of

[
lambda_H.
]

## 2. Source activity law

PNCS declares

[
A
=
operatorname{clip}_{[0,1]}
left[
rac{
f_2+0.5f_4+0.3(1-f_3)
}{1.8}
ight].
]

Define the preclamp coordinate

[
widetilde A
=
rac{
10f_2+5f_4+3(1-f_3)
}{18}.
]

Then

[
A=operatorname{clip}_{[0,1]}(widetilde A).
]

The Hebbian gain is

[
oxed{
lambda_H
=
0.1left(A-rac12ight).
}
]

Therefore

[
oxed{
-rac1{20}
le
lambda_H
le
rac1{20}.
}
]

## 3. Exact sign hyperplane

Because clipping to ([0,1]) preserves which side of (1/2) a real number lies
on,

[
A>rac12
iff
widetilde A>rac12,
]

and similarly for equality and (<).

Hence

[
oxed{
A=rac12
iff
10f_2+5f_4+3(1-f_3)=9.
}
]

This is an exact affine hyperplane in the three source coordinates used by the
activity law.

The two half-spaces determine the Hebbian sign:

[
10f_2+5f_4+3(1-f_3)>9
Longrightarrow
lambda_H>0,
]

[
10f_2+5f_4+3(1-f_3)<9
Longrightarrow
lambda_H<0.
]

## 4. Conditional barycentric interpretation

If independently

[
f_2, f_4, 1-f_3in[0,1],
]

then

[
widetilde A
=
rac59f_2
+
rac5{18}f_4
+
rac16(1-f_3),
]

and the weights satisfy

[
rac59+rac5{18}+rac16=1.
]

Thus on a normalized flavor domain the preclamp activity is a convex/barycentric
average and already lies in ([0,1]).

However the current `DriveSnapshot` admission accepts finite flavor values and
does not globally establish that normalized domain.

Therefore:

[
oxed{
	ext{barycentric interpretation = conditional},
}
]

while the clipped activity law and sign hyperplane are exact source contracts.

## 5. Operator-curvature bifurcation

Let

[
j
]

be the pre-normalized symmetric zero-diagonal coupling matrix,

[
ho=ho(j)>0,
qquad
J=j/ho,
]

and define

[
(C_Phi)_{ij}
=
cos(Phi_i-Phi_j)
]

on the off-diagonal coupling sector.

When:

1. the weak-channel boost is inactive;
2. clipping is locally inactive;
3. the spectral-radius branch is differentiable,

the source-operator firewall gives

[
oxed{
[J,dot J]
=
rac{
0.1(A-rac12)
}{ho^2}
[j,C_Phi].
}
]

Therefore, whenever

[
[j,C_Phi]
eq0,
]

one has

[
oxed{
A=rac12
Longrightarrow
[J,dot J]=0,
}
]

while

[
oxed{
A
eqrac12
Longrightarrow
[J,dot J]
eq0.
}
]

Moreover crossing the hyperplane reverses the sign/orientation of the local
commutator:

[
lambda_Hmapsto-lambda_H.
]

Thus (A=1/2) is a genuine local operator-curvature bifurcation surface for the
Hebbian lane.

## 6. Norm law

The Frobenius magnitude is

[
oxed{
|[J,dot J]|_F
=
rac{
0.1|A-rac12|
}{ho^2}
|[j,C_Phi]|_F.
}
]

Define the coefficient-free geometric obstruction

[
Xi_Phi
=
rac{
|[j,C_Phi]|_F
}{
|j|_F|C_Phi|_F
}.
]

Then activity controls the rate while (Xi_Phi) controls whether a
directional obstruction exists at all.

This cleanly separates:

[
oxed{
	ext{geometry }[j,C_Phi]
}
]

from

[
oxed{
	ext{state-dependent signed rate }A-rac12.
}
]

## 7. Pinned source point

For the deterministic PNCS fixture,

[
(f_2,f_3,f_4)=(0.23,0.56,0.48),
]

so

[
A
=
rac{
0.23+0.5(0.48)+0.3(0.44)
}{1.8}
=
0.33444444444444443.
]

Hence

[
oxed{
lambda_H
=
-0.016555555555555556.
}
]

The pinned point lies strictly on the negative-Hebbian side of the bifurcation
surface.

## 8. What remains arbitrary

The exact source structure does not derive why the activity uses the relative
weights

[
oxed{
10:5:3.
}
]

Search of the current PNCS/GREMLIN/TIR source surfaces finds these weights as
runtime policy in the HTRI drive path, not as a separately derived invariant.

Likewise the overall (0.1) Hebbian scale remains an effective rate.

Thus this theorem derives the bifurcation geometry **given the source activity
map**, not the microscopic origin of that map.

## 9. Claim ledger

| Statement | Status |
|---|---|
| clipped activity formula | `EXACT SOURCE CONTRACT` |
| (lambda_Hin[-0.05,0.05]) | `EXACT` |
| sign boundary is (10f_2+5f_4+3(1-f_3)=9) | `EXACT` |
| normalized inputs make activity a convex combination | `EXACT CONDITIONAL` |
| global flavor admission guarantees normalized inputs | `REFUTED / NOT PRESENT` |
| (A=1/2) kills local Hebbian (J)-rotation under declared conditions | `EXACT CONDITIONAL` |
| crossing (A=1/2) reverses commutator orientation | `EXACT CONDITIONAL` |
| weights (10:5:3) are source-derived fundamental ratios | `OPEN / NOT FOUND` |
| physical meaning of flavor/activity coordinates | `OPEN / NOT CLAIMED` |

## 10. Validation

Deterministic validator:

`TIR/validation/tir_mummu_activity_operator_curvature_bifurcation_v0_1.py`

Static receipt:

`TIR/validation/TIR_MUMMU_ACTIVITY_OPERATOR_CURVATURE_BIFURCATION_VALIDATION_V0_1.json`
