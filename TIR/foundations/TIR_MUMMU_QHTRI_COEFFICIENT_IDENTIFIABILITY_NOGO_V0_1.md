# TIR MUMMU QHTRI Coefficient Identifiability No-Go v0.1

Status: `EXACT_HILBERT_SCHMIDT_ORTHOGONALITY / EXACT_SCALE_TIME_REPARAMETRIZATION / EXACT_QUADRATIC_SELECTION_NO_GO / DEFAULT_COEFFICIENTS_NOT_DERIVED / NEUTRAL_EQUAL_HS_BENCHMARK_ONLY`

Date: 2026-09-23

## 1. Purpose

The source-derived QHTRI pair-dynamics witness currently uses the PNCS Hamiltonian

[
H
=
aD+bJ,
]

with source defaults

[
a=0.25,
qquad
b=0.7.
]

Here

[
D=operatorname{diag}(widehatomega)
]

is the standardized detuning operator and

[
J=widehat g
]

is the symmetrized zero-diagonal coupling matrix normalized by spectral radius.

This theorem determines what is and is not fixed by the source geometry before
those coefficients are interpreted as fundamental.

## 2. Provenance result

Source pin:

`AdrianLipa90/PhaseNav-Natural-Coding-System@8855abed440e9949f576ffbe2153325f69e78963`.

Relevant contracts:

- `src/phasenav_natural_code/semantic_htri_drive_v32.py`;
- `spec/PNCS_SEMANTIC_HTRI_INPUT_ADMISSION_V0_1.md`.

The implementation declares

`coupling_strength: float = 0.7`

and

`detuning_strength: float = 0.25`

as function defaults.

The admission contract explicitly allows arbitrary exact finite real values for
both parameters before Hamiltonian construction.

The commit that introduced the file,

`bfe21eaa3e5c0d5e33dc2e449c88c6bd0e10cf52`,

already contains these defaults and no preceding derivation of them.

Therefore:

[
oxed{
0.25, 0.7
	ext{ are source-contract defaults, not source-derived invariants.}
}
]

## 3. Exact Hilbert-Schmidt orthogonality

The detuning operator (D) is diagonal.

The coupling normalization sets

[
J_{ii}=0
]

exactly.

Hence

[
oxed{
langle D,Jangle_{m HS}
=
operatorname{Tr}(D^dagger J)
=
operatorname{Tr}(DJ)
=
0.
}
]

This statement does not depend on the deterministic fixture.

Since the standardized detuning vector has unit variance over (N=36),

[
sum_{k=1}^{36}widehatomega_k^2=36,
]

so

[
oxed{
|D|_F=6.
}
]

For any admitted nonzero coupling graph define

[
j_F:=|J|_F>0.
]

## 4. Canonical coefficient coordinates

Define the Hilbert-Schmidt normalized basis

[
widehat D=rac{D}{|D|_F},
qquad
widehat J=rac{J}{|J|_F}.
]

Then

[
operatorname{Tr}(widehat D^2)=1,
qquad
operatorname{Tr}(widehat J^2)=1,
qquad
operatorname{Tr}(widehat Dwidehat J)=0.
]

Write

[
A=a|D|_F,
qquad
B=b|J|_F.
]

The Hamiltonian becomes

[
H=Awidehat D+Bwidehat J.
]

Introduce

[
oxed{
s=sqrt{A^2+B^2},
qquad
chi=operatorname{atan2}(B,A).
}
]

Thus

[
oxed{
H
=
s
left(
coschi,widehat D
+
sinchi,widehat J
ight).
}
]

The original two coefficients are therefore separated into:

- one overall scale (s);
- one dimensionless mixing angle (chi).

## 5. Overall scale is a time reparameterization

For a fixed normalized generator

[
K_chi
=
coschi,widehat D
+
sinchi,widehat J,
]

the unitary is

[
U_{s,chi}(t)
=
e^{-istK_chi}.
]

Therefore

[
oxed{
U_{s,chi}(t)
=
U_{1,chi}(st).
}
]

So, before an external/proper-time calibration fixes the absolute rate, changing
(s) only changes the parameterization speed along the same unitary orbit.

The projective orbit shape is selected by (chi), not by (s).

## 6. Quadratic minimum-action no-go

By Hilbert-Schmidt orthonormality,

[
egin{aligned}
operatorname{Tr}(H^2)
&=
s^2
operatorname{Tr}
left[
(coschi,widehat D+sinchi,widehat J)^2
ight]
\
&=
s^2
(cos^2chi+sin^2chi)
\
&=
s^2.
end{aligned}
]

Hence

[
oxed{
operatorname{Tr}(H^2)
	ext{ is independent of }chi.
}
]

Therefore any coefficient-selection rule based only on a quadratic norm/action
of this orthonormalized two-generator sector cannot determine the mixing angle.

In particular:

[
oxed{
	ext{“choose }a,b	ext{ by minimizing }operatorname{Tr}(H^2)	ext{”}
}
]

is mathematically incapable of selecting the ratio (b/a) at fixed scale.

A higher-order invariant, an external physical calibration, a source-derived
symmetry, or an explicit operational objective is required.

## 7. Pinned deterministic fixture

For the deterministic PNCS cosine-coupling fixture used by the existing MUMMU
source witness,

[
|D|_F=6,
qquad
|J|_F
approx
1.4552137502179978.
]

The source defaults therefore correspond in the orthonormal basis to

[
A
=
0.25	imes6
=
1.5,
]

[
B
=
0.7	imes1.4552137502179978
approx
1.0186496251525985.
]

Hence

[
oxed{
s
approx
1.8131869894810986,
}
]

and

[
oxed{
chi_{m default}
approx
0.5965608027914262 {m rad}
approx
34.180416^circ.
}
]

The raw coefficient ratio (0.7/0.25=2.8) is therefore not itself an
invariant measure of the relative Hamiltonian contribution because the two
basis operators have different norms.

## 8. Fixture-specific non-Abelian witness scan

Normalize (s=1) and scan

[
H(chi)
=
coschi,widehat D
+
sinchi,widehat J
]

against the already-defined local source witness

[
mathcal W_0(chi)
=
left|
oldsymbolOmega_0
	imes
dot{oldsymbolOmega}_0
ight|.
]

For the pinned deterministic fixture, the maximum occurs numerically near

[
oxed{
chi_{mathcal W}
approx43.065^circ.
}
]

The source default angle gives approximately

[
oxed{
rac{
mathcal W_0(chi_{m default})
}{
max_chimathcal W_0(chi)
}
approx
0.9531.
}
]

This is an interesting fixture-level observation, but it is not a derivation of
the source defaults.  Maximizing (mathcal W) is itself an additional
objective and is not promoted here.

## 9. Neutral equal-HS benchmark

A coefficient-free **benchmark convention** may be defined by equal contribution
in the orthonormal Hilbert-Schmidt basis:

[
oxed{
H_{m eq}
=
rac1{sqrt2}
(widehat D+widehat J),
}
]

corresponding to

[
chi=racpi4.
]

In raw coefficient coordinates this is

[
rac{b}{a}
=
rac{|D|_F}{|J|_F}.
]

For the pinned fixture,

[
rac ba
approx
4.123100.
]

This is not a fundamental prediction.  It is a transparent neutral benchmark
with no arbitrary preference between two orthonormal generator directions.

## 10. Correct status of the QHTRI coefficients

The current status is

[
oxed{
s: 	ext{time-scale parameter until externally calibrated},
}
]

[
oxed{
chi: 	ext{one remaining dimensionless model parameter}.
}
]

The values (0.25,0.7) remain valid regression/reference defaults for PNCS, but
must not be used downstream as if derived by TIR geometry.

## 11. Claim ledger

| Statement | Status |
|---|---|
| (D) and (J) are Hilbert-Schmidt orthogonal | `EXACT` |
| (|D|_F=6) for standardized 36-vector | `EXACT` |
| two raw coefficients reduce to scale (s) and angle (chi) | `EXACT` |
| overall scale rescales unitary time | `EXACT` |
| quadratic HS action selects (chi) | `FAIL / NO-GO` |
| PNCS source derives (0.25,0.7) | `NOT FOUND / REFUTED AS CURRENT PROVENANCE CLAIM` |
| equal-HS (chi=pi/4) is a neutral benchmark | `CONVENTION` |
| current default is near fixture-specific (mathcal W) maximum | `NUMERIC OBSERVATION` |
| current default is therefore fundamental | `NOT CLAIMED` |

## 12. Validation

Deterministic validator:

`TIR/validation/tir_mummu_qhtri_coefficient_identifiability_v0_1.py`

Static receipt:

`TIR/validation/TIR_MUMMU_QHTRI_COEFFICIENT_IDENTIFIABILITY_VALIDATION_V0_1.json`
