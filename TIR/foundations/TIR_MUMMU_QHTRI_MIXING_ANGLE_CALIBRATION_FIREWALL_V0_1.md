# TIR MUMMU QHTRI Mixing-Angle Calibration and Actuation Firewall v0.1

Status: `EXACT_SCALE_INVARIANT_TRAJECTORY_SHAPE_OBSERVABLES / PINNED_FIXTURE_MONOTONE_ANGLE_CALIBRATION / FUNDAMENTAL_ACTUATION_BINDING_OPEN`

Date: 2026-09-23

## 1. Purpose

The coefficient-identifiability theorem reduces

[
H=aD+bJ
]

to

[
H
=
s
left(
coschi,widehat D
+
sinchi,widehat J
ight).
]

The overall scale (s) is a unitary time-rescaling parameter.  The remaining
dimensionless degree of freedom is the mixing angle (chi).

This theorem separates two questions:

1. can (chi) be calibrated from the **shape** of a model trajectory without
   knowing (s)?
2. is that calibration a fundamental source law?

The answer is:

[
oxed{
	ext{trajectory-shape calibration: YES at model level}
}
]

but

[
oxed{
	ext{fundamental actuation law: OPEN}.
}
]

## 2. GREMLIN provenance firewall

GREMLIN source:

`AdrianLipa90/GREMLIN@e1e617b03406e38946a3b5296db5cfd259cca3df`.

The development roadmap states that the semantic carrier factor

[
Q_{BNA}=rac{BN}{AR}
]

must obtain an explicit actuation law before it controls coupling, drive
magnitude or Hamiltonian parameters.

Therefore no MUMMU/TIR derivation is permitted to assign (chi) from
(Q_{BNA}), semantic mass, or another same-role variable without an independent
typed actuation receipt.

This matches the existing GREMLIN identifiability policy: factorization is not
promotion.

## 3. Exact scale laws

At a fixed local state, under

[
Hmapsto sH,
qquad
s>0,
]

the Schrödinger derivatives scale as

[
dotpsimapsto sdotpsi,
qquad
ddotpsimapsto s^2ddotpsi.
]

Hence for one local (CP^1) pair:

[
dot umapsto sdot u,
]

[
dot{mathbf n}mapsto sdot{mathbf n},
]

[
oldsymbolOmega
=
mathbf n	imesdot{mathbf n}
mapsto
soldsymbolOmega,
]

[
dot{oldsymbolOmega}
mapsto
s^2dot{oldsymbolOmega}.
]

Therefore

[
mathcal W
=
left|
oldsymbolOmega
	imes
dot{oldsymbolOmega}
ight|
mapsto
s^3mathcal W.
]

## 4. Scale-free local shape invariants

Define

[
oxed{
R_1
=
rac{|oldsymbolOmega|}
{|dot u|}
}
]

when (dot u
eq0), and

[
oxed{
R_2
=
rac{mathcal W}
{|oldsymbolOmega|^3}
}
]

when (|oldsymbolOmega|
eq0).

Then

[
oxed{
R_1(sH)=R_1(H),
qquad
R_2(sH)=R_2(H).
}
]

Thus the pair

[
oxed{
mathcal C(chi)
=
(R_1(chi),R_2(chi))
}
]

depends on trajectory shape but not on the unknown overall Hamiltonian scale.

This supplies a model-level route for identifying (chi) from local trajectory
geometry before fixing the absolute clock scale.

## 5. Pinned PNCS fixture

Use the same deterministic source fixture as the QHTRI pair-dynamics witness,
with Hilbert-Schmidt normalized basis

[
widehat D,
qquad
widehat J.
]

For the current source-default mixing angle

[
chi_{m default}
approx
34.180416^circ,
]

pair (j=0) gives, at the initial section,

[
dot u_0
approx
-5.8759260	imes10^{-3},
]

[
|Omega_0|
approx
1.6223975	imes10^{-2},
]

[
mathcal W_0
approx
1.5145529	imes10^{-4}
]

for the normalized (s=1) Hamiltonian.

Hence

[
oxed{
R_1(chi_{m default})
approx
2.76109241,
}
]

and

[
oxed{
R_2(chi_{m default})
approx
35.46603785.
}
]

## 6. Numerical angle-identifiability probe

On the pinned source fixture, scan the open interval

[
0<chi<racpi2.
]

The deterministic probe finds:

[
oxed{
R_1(chi)
	ext{ strictly decreases over the sampled interval},
}
]

while

[
oxed{
R_2(chi)
	ext{ strictly increases over the sampled interval}.
}
]

Therefore either one is numerically invertible on this pinned branch away from
its singular endpoint.

The ordered pair ((R_1,R_2)) provides a redundant calibration check.

This is a fixture-level deterministic result, not a universal theorem for all
admitted (D,J,psi).

## 7. Important distinction: calibration is not derivation

Suppose a trajectory receipt provides measured/model-observed

[
R_1^{m obs},R_2^{m obs}.
]

One may then solve

[
mathcal C(chi)
=
(R_1^{m obs},R_2^{m obs})
]

for (chi) within the admitted model branch.

That procedure answers:

[
	ext{“which }chi	ext{ generated this trajectory shape?”}
]

It does **not** answer:

[
	ext{“why does Nature choose this }chi	ext{?”}
]

The latter requires an independent source/actuation law or empirical
calibration.

## 8. Exact remaining actuation gate

The missing promotion object is typed as

[
oxed{
mathcal A_{m source}
:
	ext{independent source/actuation receipt}
longrightarrow
chi.
}
]

A valid implementation must:

1. cite an independent source quantity;
2. provide a dimensional/normalization law;
3. produce the same (chi) across independent realizations within declared
   uncertainty;
4. fail closed when the source receipt is absent;
5. not infer (chi) by fitting the same observable later used as validation.

Until then:

[
oxed{
chi
=
	ext{model-calibratable but not fundamental-source-derived}.
}
]

## 9. Consequence for GREMLIN minimal-action routing

GREMLIN may use the trajectory-shape invariants to:

- detect coefficient drift;
- compare candidate Hamiltonian profiles;
- recover (chi) from a known trajectory;
- flag incompatible actuation receipts.

It may not promote a preferred (chi) merely because one candidate minimizes,
maximizes, or aesthetically simplifies an internally chosen score.

Any such score must itself have independent authority.

## 10. Claim ledger

| Statement | Status |
|---|---|
| (dot u) scales as (s) | `EXACT` |
| (|Omega|) scales as (s) | `EXACT` |
| (mathcal W) scales as (s^3) | `EXACT` |
| (R_1,R_2) are scale invariant | `EXACT` |
| pinned-fixture (R_1) is monotone decreasing | `NUMERIC PASS` |
| pinned-fixture (R_2) is monotone increasing | `NUMERIC PASS` |
| (chi) can be calibrated from pinned trajectory shape | `MODEL-LEVEL PASS` |
| trajectory calibration makes (chi) fundamental | `REFUTED` |
| current GREMLIN source supplies explicit Hamiltonian actuation law | `OPEN / NOT FOUND` |

## 11. Validation

Deterministic validator:

`TIR/validation/tir_mummu_qhtri_mixing_angle_calibration_v0_1.py`

Static receipt:

`TIR/validation/TIR_MUMMU_QHTRI_MIXING_ANGLE_CALIBRATION_VALIDATION_V0_1.json`
