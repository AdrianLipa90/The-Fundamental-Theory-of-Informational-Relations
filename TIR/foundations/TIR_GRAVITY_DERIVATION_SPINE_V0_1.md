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

For \(V=H(t)R\),

\[
\frac{D V}{Dt}
=
(\dot H+H^2)R
=
\frac{\ddot a}{a}R.
\]

Thus accelerated expansion can be represented as a flow/geometric mechanism rather than as a material object.

However, TIR has not yet derived the effective source or correction that forces the observed late-time sign and magnitude.

The remaining physical cosmology gate is

\[
\boxed{
{\rm source\!\!-\!bound\ event/spatial\ evolution}
\to
\partial_0 h_{ij},\,N,\,b^i
\xrightarrow{\rm RF\!\!-\!E9}
K_{ij}
\to
{\rm ADM\ constraints/evolution}
\to
\ddot a/a.
}
\]

The late-time acceleration mechanism still requires a derived physical source or geometric correction; the event-spatial contract closes the metric-rate handoff, not that cosmological source.

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

HOLONOMIC_LATE_TIME_ACCELERATION_SOURCE = OPEN

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
