# TIR Gravity Derivation Spine v0.1

Status: STRUCTURAL_GRAVITY_DERIVATION_ASSEMBLED / LOCAL_GR_DYNAMICS_CONDITIONAL_CLOSED / PRODUCTION_PHYSICAL_REALIZATION_OPEN

Date: 2026-09-24

## 1. Purpose

This file is the single dependency spine for the current TIR gravity derivation. It does not create a new physical claim. It assembles the already-existing TIR geometry chain and the 2026-09-24 flow/orbital extensions into one auditable sequence.

## 2. Dependency spine

\[
0
\to P
\to {\rm FIRST\ DISTINCTION}
\to \{N,S\}
\to \frac12
\to \ln2
\to \mathbb C^2
\]

\[
\to {\rm Herm}_0(2)\cong\mathbb R^3
\to h_{ij}
\to {\rm tetrahedral\ relational\ carrier}
\]

\[
\to {\rm typed\ connection}
\to SE(3)\ {\rm affine\ lift}
\to {\rm discrete\ solder/torsion}
\]

\[
\to {\rm Cartan\ refinement}
\to T^a,\Omega^a{}_b
\to {\rm Levi\!-\!Civita\ GR\ sector}
\]

\[
\to
(\Sigma_\Theta,h_{ij},N_\Theta,K_{ij},\beta^i_{\rm match})
\to
g_{\mu\nu}
\]

\[
\to
b^i_{(0)}=\beta^i_{(t)}/c
\to
V^i=-cb^i_{(0)}
\to
\chi=\operatorname{artanh}|b|
\to
q=\tanh(\chi/2)
\]

\[
\to
{\rm ADM\ constraints}
\to
{\rm local\ Einstein\ sector}.
\]

For stationary spherical vacuum on the unit-lapse flat-slice branch,

\[
\frac{d}{dr}(rV^2)=0
\to
V^2=\frac Cr.
\]

Mass normalization gives

\[
C=2GM,
\qquad
V^2=\frac{2GM}{r}.
\]

The invariant spherical content is

\[
\boxed{
m_{\rm MS}=\frac{rV^2}{2G}
}
\]

so vacuum is equivalently \(dm_{\rm MS}/dr=0\).

## 3. What is now derived exactly or conditionally

### Exact / already closed structural pieces

- primitive TIR spatial carrier and rank-three geometry;
- discrete solder/torsion source object;
- Cartan torsion/curvature refinement under the declared smooth-refinement assumptions;
- zero-torsion Levi-Civita selection on the admitted endpoint-compatible sector;
- ADM metric reconstruction from spatial metric, lapse and matching shift;
- x0 shift conversion \(b=\beta_t/c\);
- flow-sign conversion \(V=-cb\);
- subluminal rapidity map \(\chi=\operatorname{artanh}|b|\);
- Poincare radial map \(q=\tanh(\chi/2)\);
- spherical Misner--Sharp crosswalk \(m_{\rm MS}=rV^2/(2G)\).

### Conditional dynamical closure

Using the already-admitted local ADM/Einstein gate:

- stationary spherical vacuum derives \(V^2=C/r\);
- asymptotic mass normalization gives \(C=2GM\);
- the resulting metric is Schwarzschild in Painleve--Gullstrand form;
- flat-FLRW flow \(V=HR\) reproduces the standard Hamiltonian constraint.

## 4. What is not required

The historical project-source expression

\[
\frac{B\omega N}{AR}(\phi+\kappa)
\]

is not required as a premise of the gravity derivation spine.

It may remain a separate wave/amplitude/dynamical candidate, but gravity kinematics already has a native TIR carrier through the inter-leaf shift.

This prevents an undefined historical symbol or dimensional ambiguity from becoming a hidden premise of the gravity derivation.

## 5. Gauge and representation firewall

The following are distinct:

1. the ADM shift \(b^i\), which is slicing/coordinate dependent;
2. the flow representation \(V^i=-cb^i\);
3. rapidity/Poincare coordinates \((\chi,q)\), which encode the same chosen representation;
4. invariant spacetime content such as curvature or, in spherical symmetry, \(m_{\rm MS}\).

Therefore

\[
b\neq0
\]

is not by itself a physical gravity claim.

The physical statement belongs to the full metric/coframe plus its invariant geometry.

Likewise, the Levi-Civita and teleparallel descriptions use different connections:

\[
T^a(\omega_{\rm LC})=0,
\qquad
R^a{}_b(\omega_{\rm TP})=0
\]

may both describe equivalent metric dynamics without assigning contradictory torsion to one connection.

## 6. Continuous transport extension

The companion file

TIR_CONTINUOUS_RELATIONAL_MEDIUM_NAVIER_STOKES_CROSSWALK_V0_1

shows that a persistent continuum transport field admits continuity, material derivative, vorticity and Navier--Stokes-form sectors under explicit assumptions.

This is a transport crosswalk only.

The forbidden claim remains

\[
{\rm Einstein\ equations}\equiv{\rm Navier\!-\!Stokes\ equations}.
\]

## 7. Cosmological mechanism boundary

For flat FLRW, the existing RF-E12/RF-E13 ADM parents imply

\[
\boxed{\frac{a''}{a}=-\frac{\kappa_E}{6}(\rho+3p)}
\]

in the length-valued temporal coordinate x^0=ct. Hence the event-derived metric rate does not itself generate acceleration; the admitted source must supply rho+3p<0 or the geometric operator must be changed.

The existing canonical information-scalar action supplies such a negative-pressure mechanism without requiring an additional bare Lambda. On the RF-L3/RF-L4A local chart,

\[
U_I=\frac{\alpha_I}{\kappa_E}\Xi_I,\qquad \phi_I=\sqrt{2\Xi_I},
\]

and therefore

\[
\boxed{\frac{a''}{a}\Big|_I=\frac{\alpha_I\Xi_I}{3}-\frac{\kappa_E}{6\Xi_I}(\Xi_I')^2.}
\]

The local acceleration criterion is

\[
\boxed{\left|\partial_0\ln\Xi_I\right|<\sqrt{2\alpha_I/\kappa_E}.}
\]

The potential may be kept inside the scalar stress tensor or moved to the dynamic-Lambda side as Lambda_I=alpha_I Xi_I; these are exactly equivalent bookkeeping choices and must not be added together.

The present IDT/RFC holonomy bridge does not yet make tau_R a gravity source: RF-L3 has partial U_I / partial tau_R = 0. Moreover, the exact partition C_h+D_h=1 cannot affect total stress when C and D have the same gravitational stress type. Thus the current holonomy route has a genuine no-go.

A minimal holonomy-active candidate is Lambda_D=alpha_I Xi_I sin^2(tau_R/2), but only if a source-owned differential stress attribution is derived and the complementary C channel receives a conservation-compatible Bianchi ledger. If tau_R is instead treated as a naive local positive-kinetic scalar in U_D proportional to sin^2(tau_R/2), the maximal D_h=1 point at tau_R=pi is a potential maximum, not a stable minimum. A topologically frozen nonlocal holonomy sector remains a separate open possibility.

Canonical gate:

TIR/integration/TIR_IDT_RFC_INFORMATION_HOLONOMY_COSMOLOGICAL_ACCELERATION_V0_1.md

## 8. Current blocker

The source contracts and assemblers exist, but the repository explicitly records:

- production global spatial capture: OPEN INPUT;
- production inter-leaf matching capture: OPEN INPUT;
- production beta_match: OPEN INPUT;
- same-realization production bundle: no admitted production instance.

Therefore the next fundamental gate cannot be closed by algebraic relabeling or by synthetic NOEMA/PhaseNav state.

It requires a source-owned production event-spatial realization with one clock/realization lineage and sufficient refinement coverage. The coordinate matching field remains a representation input for nonzero-shift gauges; it is not the fundamental observable target.

## 9. Claim status

GRAVITY_STRUCTURAL_DERIVATION_SPINE = ASSEMBLED

LOCAL_CARTAN_TO_GR_CHAIN = CLOSED_ON_DECLARED_ASSUMPTIONS

INTERLEAF_SHIFT_TO_FLOW_RAPIDITY = CLOSED_EXACT_KINEMATIC

SPHERICAL_VACUUM_RIVER_PROFILE = DERIVED_CONDITIONAL

SPHERICAL_FLOW_TO_MISNER_SHARP_MASS = CLOSED_EXACT

CONTINUOUS_TRANSPORT_CROSSWALK = PASS_CONDITIONAL

PRODUCTION_PHYSICAL_REALIZATION = OPEN_INPUT

FUNDAMENTAL_DYNAMICS_TO_BETA_MATCH = NOT_FUNDAMENTAL_TARGET / SHIFT_GAUGE_REPRESENTATION

EVENT_SPATIAL_METRIC_RATE_SOURCE_CONTRACT = PASS_EXECUTABLE / PRODUCTION_INPUT_OPEN

RF_E9_EXTRINSIC_CURVATURE_OPERATOR = REUSED_EXISTING_RFC_GATE

HOLONOMIC_LATE_TIME_ACCELERATION_SOURCE = OPEN / CURRENT_ACTION_SPECTATOR_NO_GO / RF_F20_LOCAL_CONNECTION_RESPONSE_ROUTE_IDENTIFIED

RF_E4_PHASE_KINETIC_COSMOLOGY = EXACT_W_PLUS_ONE_DECELERATING

RF_F20_CONNECTION_METRIC_RESPONSE_COSMOLOGY = PASS_EXACT_CONDITIONAL_SIGN_TEST

TEMPORAL_U1_TO_LOCAL_ABE_RESPONSE_BINDING = OPEN

FULL_PHYSICAL_GRAVITY_DERIVED_FROM_MICROSCOPIC_TIR_SOURCE = NOT_YET_CLOSED

## 10. Canonical files

- TIR_UNIVERSAL_LOOP_TORSION_SOURCE_BINDING_V0_1
- TIR_CARTAN_CONTINUUM_REFINEMENT_V0_1
- TIR_CARTAN_REFINEMENT_CURVATURE_TORSION_SEPARATION_V0_1
- TIR_ZERO_TORSION_LEVI_CIVITA_SELECTION_V0_1
- TIR_SPATIAL_TEMPORAL_CLOSURE_INTERFACE_V0_1
- TIR_INTERLEAF_MATCHING_FIELD_INPUT_CONTRACT_V0_1
- TIR_FRACTAL_ORBITAL_INFORMATIONAL_HOLONOMIC_GRAVITY_V0_1
- TIR_FLOW_COFRAME_ADM_CONSTRAINT_GRAVITY_V0_1
- TIR_INTERLEAF_SHIFT_ORBITAL_RAPIDITY_MASS_BRIDGE_V0_1
- TIR_CONTINUOUS_RELATIONAL_MEDIUM_NAVIER_STOKES_CROSSWALK_V0_1
- TIR_IDT_EXTRINSIC_CURVATURE_SOURCE_BRIDGE_V0_1
- TIR_IDT_EVENT_SPATIAL_STATE_BINDING_V0_1


## 11. Event-indexed source completion

The preferred production source path is now

\[
\boxed{\text{IDT event clock}+\text{TIR spatial snapshot}+\text{same realization/receipt/clock}\to\frac{\Delta h}{\Delta x^0}\to\partial_0h\xrightarrow{\rm RF\!-!E9}K_{ij}.}
\]

This path reuses RFC RF-E9 and avoids treating either the ADM shift or an abstract equality \(x_{\rm IDT}=\rho_{\rm TIR}\) as a physical premise.

The remaining blocker is empirical/source-level:

\[
\boxed{\text{production event-spatial realization + refinement coverage}.}
\]


## 10. 2026-09-24 acceleration mechanism closure refinement

The current source stack now separates three non-equivalent acceleration routes:

1. RF-F15 constant vacuum integration component: rho_C=K0 C_Lambda, with exact fixed-x transition rho_C>rho_r but open magnitude/sign.
2. RF-L2 information-scalar potential: exact negative-pressure action route when potential dominates kinetic stress; absolute scale remains open.
3. RF-F22 state-dependent projector/connection response: genuinely non-metric-proportional candidate source, with exact local threshold

\[
\frac{R_0+3R_s}{\mu_\vartheta^2}+(S_0+3S_s)<-\frac12
\]

on the positive interaction branch.

The current frozen/internal realization does not satisfy route 3: AB and fixed-map Berry response may be held metric-independent, RF-F19 has an exact S_vartheta=0 independent-variation branch, and no current source derives a nonzero Euler/spin metric functional. Reusing the same ADM lapse inside the projector calibration during the same metric variation recovers the RF-F18 self-normalization no-go and gives zero projector stress.

Finally, C_Lambda has dimension T^-4. Dimensionless holonomy/topological data cannot determine its nonzero magnitude without an independently derived frequency scale Omega_*; at most they may fix C_Lambda/Omega_*^4.

PROJECTOR_RESPONSE_THRESHOLD = PASS_EXACT_CONDITIONAL

SAME_METRIC_LAPSE_PROJECTOR = ZERO_STRESS_NO_GO

C_LAMBDA_TOPOLOGICAL_ABSOLUTE_MAGNITUDE = DIMENSIONAL_NO_GO_WITHOUT_OMEGA_STAR

PHYSICAL_EULER_OR_SCALE_METRIC_RESPONSE = OPEN

PHYSICAL_OMEGA_STAR_SCALE = OPEN
