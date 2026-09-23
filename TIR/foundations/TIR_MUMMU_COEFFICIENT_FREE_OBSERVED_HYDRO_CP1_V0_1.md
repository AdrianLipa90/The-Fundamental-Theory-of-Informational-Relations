# TIR MUMMU Coefficient-Free Observed-Hydro CP1 Transport v0.1

Status: `EXACT_CONDITIONAL_CP1_TRANSPORT / NUMERIC_SOURCE_COMPONENT_WITNESS / EXACT_MINIMUM_NORM_HERMITIAN_LIFT / QHTRI_GRAPH_COEFFICIENTS_NOT_REQUIRED / NATIVE_CROSS_BINDING_OPEN / PHYSICAL_BINDING_OPEN`

Date: 2026-09-23

## 1. Purpose

The existing source-derived MUMMU witness used the PNCS QHTRI graph Hamiltonian

[
H_{m QHTRI}
=
0.25,operatorname{diag}(widehatomega)
+
0.7,widehat g.
]

Those coefficients are regression/reference defaults, not source-derived
invariants.

This theorem shows that a different model-level route to a full local (CP^1)
history exists using already implemented PNCS source components:

[
oxed{
	ext{temporal observation amplitudes}
+
	ext{hydrodynamic }T^{36}	ext{ phase flow}.
}
]

The route does not use the QHTRI graph Hamiltonian or its (0.25,0.7)
coefficients.

## 2. Source components

PNCS source pin:

`AdrianLipa90/PhaseNav-Natural-Coding-System@8855abed440e9949f576ffbe2153325f69e78963`.

Relevant contracts:

- `src/phasenav_natural_code/temporal_geometry_v02.py`;
- `spec/experimental/PNCS_TEMPORAL_GEOMETRY_V0_2.md`;
- `src/phasenav_natural_code/hydro_time_v27.py`;
- `spec/PNCS_HYDRODYNAMIC_PROPER_TIME_V0_27.md`.

The temporal geometry contract explicitly maps
`TemporalPhaseProjection36.theta` into the existing
`PhaseFlowState36` coordinate semantics.

The observation layer provides normalized probabilities

[
p_k=|a_k|^2,
]

while the hydrodynamic layer provides an ordered proper-time phase trajectory

[
	aumapsto 	heta_k(	au).
]

There is not yet one native PNCS receipt binding an observation post-state to a
hydrodynamic trace.  That composition is therefore conditional in TIR.

## 3. Receipt-bound pair state

Assume:

1. one admitted temporal observation post-state supplies fixed probabilities
   (p_k);
2. one admitted hydrodynamic trace uses the same (T^{36}) coordinate basis;
3. the phase-flow initial section equals the temporal projection section carried
   by that observation state.

For pair (j), with coordinates (L=2j), (R=2j+1), define

[
q_j=p_L+p_R>0,
]

[
u_j
=
rac{p_L-p_R}{p_L+p_R},
]

and

[
delta_j(	au)
=
	heta_R(	au)-	heta_L(	au).
]

The pair state is

[
oxed{
|psi_j(	au)angle
=
rac1{sqrt{q_j}}
egin{pmatrix}
sqrt{p_L}e^{i	heta_L(	au)}\
sqrt{p_R}e^{i	heta_R(	au)}
end{pmatrix}.
}
]

The corresponding Bloch vector is

[
oxed{
mathbf n_j
=
left(
r_jcosdelta_j,,
r_jsindelta_j,,
u_j
ight),
qquad
r_j=sqrt{1-u_j^2}.
}
]

Because the observation probabilities are held fixed on the admitted trace,

[
dot u_j=0.
]

## 4. Exact phase-flow generator

For constant (u),

[
partial_deltamathbf n
=
(-rsindelta,,
 rcosdelta,,
 0).
]

Therefore

[
oxed{
oldsymbolOmega
=
mathbf n	imesdot{mathbf n}
=
dotdelta
left(
-u rcosdelta,,
-u rsindelta,,
r^2
ight).
}
]

The local spin connection is

[
oxed{
mathcal A
=
-rac{i}{2}
oldsymbolOmegacdotoldsymbolsigma.
}
]

No QHTRI graph-Hamiltonian coefficient enters this expression.

## 5. Exact non-Abelian criterion

Let

[
mathbf w(delta)
=
(-urcosdelta,,-ursindelta,,r^2).
]

For two admitted sections,

[
oldsymbolOmega_1
=
dotdelta_1mathbf w(delta_1),
qquad
oldsymbolOmega_2
=
dotdelta_2mathbf w(delta_2).
]

Their vector cross product is

[
oxed{
mathbf w(delta_1)	imesmathbf w(delta_2)
=
egin{pmatrix}
u r^3(sindelta_1-sindelta_2)\
u r^3(cosdelta_2-cosdelta_1)\
u^2r^2sin(delta_2-delta_1)
end{pmatrix}.
}
]

Hence a sufficient and generic exact condition for noncommutation is

[
oxed{
0<|u|<1,
quad
dotdelta_1dotdelta_2
e0,
quad
delta_1
otequivdelta_2pmod{2pi}.
}
]

Then

[
oxed{
[mathcal A(	au_1),mathcal A(	au_2)]

e0.
}
]

Thus amplitude imbalance plus an evolving relative phase is sufficient for local
non-Abelian transport.

## 6. Why the two obvious shortcuts fail

### 6.1 Canonical dual-pair NOW translation

For `TemporalDualPairProjection36`,

[
t_pm=NOWpmDelta,
]

so

[
u_pm
=
pmrac{Delta}{lambda}.
]

Therefore the pair phases depend on (Delta/lambda), not on the absolute
value of (NOW).

Hence

[
oxed{
rac{partialdelta_{m dual}}{partial NOW}=0.
}
]

Moving the observation origin alone does not create the required phase history
for the canonical inversion-dual pair.

### 6.2 Gaussian localization at fixed phase

A Gaussian observation changes pair probabilities and therefore (u), but its
weights are positive real numbers and do not change the pair phase difference.

At fixed (delta),

[
mathbf n	imespartial_umathbf n
=
rac1r
(sindelta,-cosdelta,0).
]

All such generators are collinear as (u) changes.

Therefore

[
oxed{
	ext{Gaussian localization alone is locally Abelian on one pair.}
}
]

Both ingredients are required: an imbalanced pair and a changing relative phase.

## 7. Deterministic source-component witness

Use the deterministic temporal grid

[
t_k=k-18,
qquad
k=0,ldots,35,
]

with (lambda=4), equal-modulus pre-observation amplitudes and
Gaussian localization at

[
NOW=0,
qquad
sigma=1.
]

For pair (j=9), coordinates (18,19) correspond to times (0,1).

The post-observation pair imbalance is exactly

[
oxed{
u
=
rac{1-e^{-1/2}}{1+e^{-1/2}}
=
	anhrac14
approx
0.2449186624.
}
]

Initialize `PhaseFlowState36` from the same temporal phase projection and use
an admitted hydrodynamic gate

[
ho=1,
qquad

u_{m eff}=0,
qquad
gamma=0.05,
qquad
dt=0.01,
]

with a unit drive on coordinate 18.

For the source equations in `hydro_time_v27.py`, the pair has nonzero
relative phase velocity after the first step.

At steps 50 and 100 the deterministic witness gives

[
oxed{
left|
oldsymbolOmega_{50}
	imes
oldsymbolOmega_{100}
ight|
approx
5.44020445	imes10^{-6}>0.
}
]

The witness depends on the admitted hydrodynamic trajectory parameters, but not
on the QHTRI graph coefficients (0.25,0.7).

## 8. Canonical minimum-Frobenius Hermitian lift

A known normalized state trajectory also admits a coefficient-free operator
representation.

Let

[
|Psiangle^dagger|Psiangle=1,
]

and define

[
|vangle
=
i|dotPsiangle.
]

Normalization implies

[
a
:=
langlePsi|vangle
inmathbb R.
]

Define

[
oxed{
H_{min}
=
|vanglelanglePsi|
+
|Psianglelangle v|
-
a|PsianglelanglePsi|.
}
]

Then

[
H_{min}^dagger=H_{min},
]

and

[
oxed{
H_{min}|Psiangle=|vangle
=
i|dotPsiangle.
}
]

Therefore

[
i|dotPsiangle
=
H_{min}|Psiangle.
]

### Minimum-norm uniqueness

Choose a basis with (|Psiangle=e_1) and decompose

[
|vangle
=
(a,w)^T.
]

Every Hermitian solution of (H|Psiangle=v) has block form

[
H
=
egin{pmatrix}
a & w^dagger\
w & B
end{pmatrix},
qquad
B=B^dagger.
]

Hence

[
|H|_F^2
=
a^2+2|w|^2+|B|_F^2.
]

The unique minimum occurs at

[
B=0,
]

which is exactly (H_{min}).

Thus

[
oxed{
H_{min}
=
operatorname*{argmin}_{H=H^dagger, HPsi=idotPsi}
|H|_F.
}
]

This supplies a canonical operator representation of an already admitted
trajectory without inserting detuning/coupling mixture coefficients.

## 9. Predictive vs descriptive Hamiltonian

This distinction is mandatory.

The source-composed trajectory plus (H_{min}) answers:

[
	ext{“what Hermitian operator minimally represents this admitted motion?”}
]

It does not answer:

[
	ext{“what operator predicts the motion before the trajectory is known?”}
]

The first is now coefficient-free.

The second still requires a source actuation/dynamics law.

Therefore the (0.25,0.7) problem is removed from **descriptive MUMMU
transport**, but not automatically from predictive QHTRI dynamics.

## 10. Semantic-magnitude firewall

The PNCS semantic-magnitude gate proves that, at fixed content identity,
(phi), (omega), lane profile and source snapshot, varying

[
Q_{BNA}=rac{BN}{A_R}
]

leaves all current HTRI/QHTRI numeric outputs unchanged, including (H).

Thus on the current source path

[
oxed{
rac{partial H_{m QHTRI}}{partial Q_{BNA}}=0
}
]

in the operational sense tested by that firewall.

Consequently (Q_{BNA}) cannot be used retroactively to justify the current
QHTRI graph coefficients.

## 11. Native integration frontier

The missing native object is now narrower than a new Hamiltonian law.

A future PNCS receipt may bind:

[
oxed{
(
	ext{TemporalObservationReceipt},
	ext{shared }T^{36}	ext{ basis},
	ext{HydrodynamicTrace}
)
longrightarrow
	ext{ObservedHydroWaveTrace}.
}
]

It must prove:

- common (T^{36}) basis identity;
- initial phase equality;
- ordered hydrodynamic step lineage;
- fixed or explicitly evolved amplitude policy;
- proper-time lineage;
- no silent use of QHTRI graph coefficients.

Until such a native object exists, the composition remains a TIR
source-compatible candidate.

## 12. Claim ledger

| Statement | Status |
|---|---|
| temporal projection is compatible with PhaseFlowState36 semantics | `EXACT IMPORTED` |
| Gaussian observation supplies normalized amplitude imbalance | `EXACT IMPORTED` |
| hydrodynamic trace supplies ordered proper-time phase evolution | `EXACT IMPORTED` |
| fixed-imbalance phase-flow CP1 formula | `EXACT` |
| generic non-Abelian criterion above | `EXACT` |
| canonical dual-pair NOW translation changes pair phase | `REFUTED` |
| Gaussian localization alone is non-Abelian | `REFUTED` |
| pinned observed+hydro composition has nonzero local witness | `NUMERIC PASS` |
| (H_{min}) is the unique minimum-Frobenius Hermitian trajectory lift | `EXACT` |
| route requires QHTRI graph defaults (0.25,0.7) | `REFUTED FOR DESCRIPTIVE TRANSPORT` |
| native PNCS observation→hydro wave-trace receipt exists | `NOT FOUND / OPEN` |
| physical neutrino/gravity realization | `OPEN / NOT CLAIMED` |

## 13. Validation

Deterministic validator:

`TIR/validation/tir_mummu_coefficient_free_observed_hydro_cp1_v0_1.py`

Static receipt:

`TIR/validation/TIR_MUMMU_COEFFICIENT_FREE_OBSERVED_HYDRO_CP1_VALIDATION_V0_1.json`
