# TIR MUMMU Coefficient-Free Observed-Hydro CP1 Transport v0.1

Status: `EXACT_CONDITIONAL_CP1_PROJECTIVE_TRANSPORT / NUMERIC_PROJECTIVE_CONNECTION_WITNESS / EXACT_MINIMUM_NORM_HERMITIAN_LIFT / COMMUTING_DIAGONAL_SOURCE_LIFT_EXISTS / QHTRI_GRAPH_COEFFICIENTS_NOT_REQUIRED_FOR_DESCRIPTIVE_LIFT / NATIVE_CROSS_BINDING_OPEN / PHYSICAL_BINDING_OPEN`

Date: 2026-09-23

## 1. Purpose

The existing source-derived MUMMU witness used the PNCS QHTRI graph Hamiltonian

\[
H_{\rm QHTRI}
=
0.25,operatorname{diag}(widehatomega)
+
0.7,widehat g.
\]

Those coefficients are regression/reference defaults, not source-derived
invariants.

This theorem shows that a different model-level route to a full local (CP^1)
history exists using already implemented PNCS source components:

\[
\boxed{
\text{temporal observation amplitudes}
+
\text{hydrodynamic }T^{36}\text{ phase flow}.
}
\]

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

\[
p_k=|a_k|^2,
\]

while the hydrodynamic layer provides an ordered proper-time phase trajectory

\[
\taumapsto \theta_k(\tau).
\]

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

\[
q_j=p_L+p_R>0,
\]

\[
u_j
=
\frac{p_L-p_R}{p_L+p_R},
\]

and

\[
delta_j(\tau)
=
\theta_R(\tau)-\theta_L(\tau).
\]

The pair state is

\[
\boxed{
|psi_j(\tau)\rangle
=
\frac1{sqrt{q_j}}
\begin{pmatrix}
sqrt{p_L}e^{i\theta_L(\tau)}\
sqrt{p_R}e^{i\theta_R(\tau)}
end{pmatrix}.
}
\]

The corresponding Bloch vector is

\[
\boxed{
mathbf n_j
=
left(
r_jcosdelta_j,,
r_jsindelta_j,,
u_j
\right),
qquad
r_j=sqrt{1-u_j^2}.
}
\]

Because the observation probabilities are held fixed on the admitted trace,

\[
dot u_j=0.
\]

## 4. Exact phase-flow generator

For constant (u),

\[
partial_deltamathbf n
=
(-rsindelta,,
 rcosdelta,,
 0).
\]

Therefore

\[
\boxed{
\boldsymbol\Omega
=
mathbf n\timesdot{mathbf n}
=
dotdelta
left(
-u rcosdelta,,
-u rsindelta,,
r^2
\right).
}
\]

The local spin connection is

\[
\boxed{
mathcal A
=
-\frac{i}{2}
\boldsymbol\Omegacdot\boldsymbolsigma.
}
\]

No QHTRI graph-Hamiltonian coefficient enters this expression.

## 5. Exact horizontal/projective connection noncommutativity criterion

Let

\[
mathbf w(delta)
=
(-urcosdelta,,-ursindelta,,r^2).
\]

For two admitted sections,

\[
\boldsymbol\Omega_1
=
dotdelta_1mathbf w(delta_1),
qquad
\boldsymbol\Omega_2
=
dotdelta_2mathbf w(delta_2).
\]

Their vector cross product is

\[
\boxed{
mathbf w(delta_1)\timesmathbf w(delta_2)
=
\begin{pmatrix}
u r^3(sindelta_1-sindelta_2)\
u r^3(cosdelta_2-cosdelta_1)\
u^2r^2sin(delta_2-delta_1)
end{pmatrix}.
}
\]

Hence a sufficient and generic exact condition for noncommutation is

\[
\boxed{
0<|u|<1,
quad
dotdelta_1dotdelta_2
e0,
quad
delta_1
otequivdelta_2pmod{2pi}.
}
\]

Then

\[
\boxed{
[mathcal A(\tau_1),mathcal A(\tau_2)]

e0.
}
\]

Thus amplitude imbalance plus an evolving relative phase is sufficient for noncommutativity of the declared horizontal/projective connection. It is not sufficient to prove noncommutativity of the source Hamiltonian.

## 6. Why the two obvious shortcuts fail

### 6.1 Canonical dual-pair NOW translation

For `TemporalDualPairProjection36`,

\[
t_pm=NOWpmDelta,
\]

so

\[
u_pm
=
pm\frac{Delta}{lambda}.
\]

Therefore the pair phases depend on (Delta/lambda), not on the absolute
value of (NOW).

Hence

\[
\boxed{
\frac{partialdelta_{\rm dual}}{partial NOW}=0.
}
\]

Moving the observation origin alone does not create the required phase history
for the canonical inversion-dual pair.

### 6.2 Gaussian localization at fixed phase

A Gaussian observation changes pair probabilities and therefore (u), but its
weights are positive real numbers and do not change the pair phase difference.

At fixed (delta),

\[
mathbf n\timespartial_umathbf n
=
\frac1r
(sindelta,-cosdelta,0).
\]

All such generators are collinear as (u) changes.

Therefore

\[
\boxed{
\text{Gaussian localization alone is locally Abelian on one pair.}
}
\]

Both ingredients are required: an imbalanced pair and a changing relative phase.

## 7. Deterministic source-component witness

Use the deterministic temporal grid

\[
t_k=k-18,
qquad
k=0,ldots,35,
\]

with (lambda=4), equal-modulus pre-observation amplitudes and
Gaussian localization at

\[
NOW=0,
qquad
sigma=1.
\]

For pair (j=9), coordinates (18,19) correspond to times (0,1).

The post-observation pair imbalance is exactly

\[
\boxed{
u
=
\frac{1-e^{-1/2}}{1+e^{-1/2}}
=
\tanh\frac14
approx
0.2449186624.
}
\]

Initialize `PhaseFlowState36` from the same temporal phase projection and use
an admitted hydrodynamic gate

\[
\rho=1,
qquad

u_{\rm eff}=0,
qquad
gamma=0.05,
qquad
dt=0.01,
\]

with a unit drive on coordinate 18.

For the source equations in `hydro_time_v27.py`, the pair has nonzero
relative phase velocity after the first step.

At steps 50 and 100 the deterministic witness gives

\[
\boxed{
left|
\boldsymbol\Omega_{50}
\times
\boldsymbol\Omega_{100}
\right|
approx
5.44020445\times10^{-6}>0.
}
\]

The witness depends on the admitted hydrodynamic trajectory parameters, but not
on the QHTRI graph coefficients (0.25,0.7).

## 8. Canonical minimum-Frobenius Hermitian lift

A known normalized state trajectory also admits a coefficient-free operator
representation.

Let

\[
|Psi\rangle^dagger|Psi\rangle=1,
\]

and define

\[
|v\rangle
=
i|dotPsi\rangle.
\]

Normalization implies

\[
a
:=
langlePsi|v\rangle
inmathbb R.
\]

Define

\[
\boxed{
H_{min}
=
|v\ranglelanglePsi|
+
|Psi\ranglelangle v|
-
a|Psi\ranglelanglePsi|.
}
\]

Then

\[
H_{min}^dagger=H_{min},
\]

and

\[
\boxed{
H_{min}|Psi\rangle=|v\rangle
=
i|dotPsi\rangle.
}
\]

Therefore

\[
i|dotPsi\rangle
=
H_{min}|Psi\rangle.
\]

### Minimum-norm uniqueness

Choose a basis with (|Psi\rangle=e_1) and decompose

\[
|v\rangle
=
(a,w)^T.
\]

Every Hermitian solution of (H|Psi\rangle=v) has block form

\[
H
=
\begin{pmatrix}
a & w^dagger\
w & B
end{pmatrix},
qquad
B=B^dagger.
\]

Hence

\[
|H|_F^2
=
a^2+2|w|^2+|B|_F^2.
\]

The unique minimum occurs at

\[
B=0,
\]

which is exactly (H_{min}).

Thus

\[
\boxed{
H_{min}
=
operatorname*{argmin}_{H=H^dagger, HPsi=idotPsi}
|H|_F.
}
\]

This supplies a canonical operator representation of an already admitted
trajectory without inserting detuning/coupling mixture coefficients.

## 9. Predictive vs descriptive Hamiltonian

This distinction is mandatory.

The source-composed trajectory plus (H_{min}) answers:

\[
\text{“what Hermitian operator minimally represents this admitted motion?”}
\]

It does not answer:

\[
\text{“what operator predicts the motion before the trajectory is known?”}
\]

The first is now coefficient-free.

The second still requires a source actuation/dynamics law.

Therefore the (0.25,0.7) problem is removed from **descriptive MUMMU
transport**, but not automatically from predictive QHTRI dynamics.

## 10. Semantic-magnitude firewall

The PNCS semantic-magnitude gate proves that, at fixed content identity,
(phi), (omega), lane profile and source snapshot, varying

\[
Q_{BNA}=\frac{BN}{A_R}
\]

leaves all current HTRI/QHTRI numeric outputs unchanged, including (H).

Thus on the current source path

\[
\boxed{
\frac{partial H_{\rm QHTRI}}{partial Q_{BNA}}=0
}
\]

in the operational sense tested by that firewall.

Consequently (Q_{BNA}) cannot be used retroactively to justify the current
QHTRI graph coefficients.

## 11. Native integration frontier

The missing native object is now narrower than a new Hamiltonian law.

A future PNCS receipt may bind:

\[
\boxed{
(
\text{TemporalObservationReceipt},
\text{shared }T^{36}\text{ basis},
\text{HydrodynamicTrace}
)
longrightarrow
\text{ObservedHydroWaveTrace}.
}
\]

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
| generic horizontal/projective connection noncommutativity criterion above | `EXACT` |
| canonical dual-pair NOW translation changes pair phase | `REFUTED` |
| Gaussian localization alone is non-Abelian | `REFUTED` |
| pinned observed+hydro composition has nonzero horizontal/projective witness | `NUMERIC PASS` |\n| same fixed-modulus source phase law admits commuting diagonal Hamiltonians | `EXACT` |
| (H_{min}) is the unique minimum-Frobenius Hermitian trajectory lift | `EXACT` |
| route requires QHTRI graph defaults (0.25,0.7) | `REFUTED FOR DESCRIPTIVE TRANSPORT` |
| native PNCS observation→hydro wave-trace receipt exists | `NOT FOUND / OPEN` |
| physical neutrino/gravity realization | `OPEN / NOT CLAIMED` |

## 13. Validation

Deterministic validator:

`TIR/validation/tir_mummu_coefficient_free_observed_hydro_cp1_v0_1.py`

Static receipt:

`TIR/validation/TIR_MUMMU_COEFFICIENT_FREE_OBSERVED_HYDRO_CP1_VALIDATION_V0_1.json`


## 14. Geometric versus dynamical noncommutativity firewall

The coefficient-free source-composed lane has an exact operator split recorded
in

`TIR/foundations/TIR_MUMMU_GEOMETRIC_NONABELIAN_DYNAMICAL_ABELIAN_SPLIT_V0_1.md`.

With frozen pair amplitudes and hydrodynamic phase velocities,

\[
H_{\rm phase}
=
-operatorname{diag}(v_L,v_R)
=
-\frac{v_L+v_R}{2}I
+
\frac{dotdelta}{2}sigma_z.
\]

Therefore all time-separated dynamical phase Hamiltonians commute:

\[
\boxed{
[H_{\rm phase}(\tau_1),H_{\rm phase}(\tau_2)]=0.
}
\]

The projective horizontal generator is instead

\[
\boxed{
Omega
=
h-(ncdot h)n,
qquad
h=(0,0,dotdelta),
}
\]

and can rotate with the moving Bloch state.  Hence the same bound trajectory can
have

\[
\boxed{
[mathcal A_{\rm geom}(\tau_1),mathcal A_{\rm geom}(\tau_2)]
e0.
}
\]

The coefficient-free witness is therefore a statement about non-Abelian
**projective/horizontal geometry**, not by itself evidence of a non-Abelian
dynamical interaction Hamiltonian.


## 15. 36D commuting diagonal source-lift restatement

For the fixed-probability observed-hydro construction,

\[
psi_k(\tau)
=
sqrt{p_k}e^{i\theta_k(\tau)},
\]

the exact Hamiltonian

\[
\boxed{
H_D(\tau)
=
-operatorname{diag}
(dot\theta_1,ldots,dot\theta_{36})
}
\]

satisfies

\[
idotpsi=H_Dpsi.
\]

Because every (H_D(\tau)) is diagonal,

\[
\boxed{
[H_D(\tau_1),H_D(\tau_2)]=0.
}
\]

Therefore the nonzero
(Omega(\tau_1)\timesOmega(\tau_2)) reported above is specifically a
horizontal/projective connection witness.

The direct source-operator criterion is separated in

`TIR/foundations/TIR_MUMMU_SOURCE_OPERATOR_NONABELIANITY_FIREWALL_V0_1.md`.

This preserves the coefficient-free descriptive (H_{min}) theorem while
preventing a chosen trajectory lift from being mistaken for a predictive source
Hamiltonian.
