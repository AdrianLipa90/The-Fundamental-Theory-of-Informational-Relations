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

## 11. Moire hyperlayer microscopic bridge

The additive candidate `TIR_MOIRE_HYPERLAYER_GRAVITY_BRIDGE_V0_1` supplies a lower-level representation candidate for the still-open microscopic-to-coframe gate:

\[
CP^1
\to (g_{FS},F_{Berry})
\to T_4\cup T_4^*
\to \text{paired triangular sheets}
\to \mathbb R^6\otimes\mathbb R^6
\to \mathcal M
\to e
\to \omega_{LC}
\to R.
\]

The 36D factorization is declared as a structured computational choice. It distinguishes the factorized subgroup \(SO(6)_L\times SO(6)_R\), with 30 generators, from unrestricted \(SO(36)\), with 630 plane-rotation generators.

The bridge also adds a strict pure-gauge firewall. A globally exact displacement and a smooth connection of the form \(U^{-1}dU\) do not by themselves generate physical curvature. The candidate only advances the gravity chain if the induced coframe/metric retains gauge-invariant non-flat content.

The associated project-local memory law is:

\[
\text{memory}=\text{persistent path-dependent relational transport},
\]

represented minimally by non-trivial holonomy classes after gauge quotient.

Current status:

- MOIRE_TWO_LAYER_IDENTITY = PASS_EXACT
- HYPERLAYER_6x6_FACTORIZATION = PASS_DEFINITION
- PURE_GAUGE_FIREWALL = PASS_EXACT
- MOIRE_TO_UNIQUE_PHYSICAL_COFRAME = OPEN
- UNIVERSE_MEMORY_AS_PHYSICAL_ONTOLOGY = OPEN
- MILLENNIUM_PROBLEM_CLOSURE = NOT_CLAIMED


## 12. Bivector-36 refinement of the microscopic gate

`TIR_BIVECTOR36_COFRAME_LIFT_V0_1` supplies a non-arbitrary representation target for the previously open 36D-to-coframe step:

\[
\mathcal M_{36}
\xrightarrow{\mathcal D}
B^{IJ}{}_{\mu\nu}
\xrightarrow{\text{simplicity/liftability}}
[e^I{}_{\mu}]
\to g_{\mu\nu}
\to \omega_{LC}
\to R.
\]

The exact exterior-square identities and validator close the algebraic **type** of the lift gate. They do not yet derive the physical decoder \(\mathcal D\), the source normalization, or Einstein dynamics from pre-geometric TIR data alone.

Current status additions:

- BIVECTOR_36_DIMENSIONAL_MATCH = PASS_EXACT
- COFRAME_TO_C2_EXTERIOR_SQUARE = PASS_EXACT
- WEDGE_PAIRING_LIFT_GATE = PASS_EXACT
- GENERIC_PERTURBED_6x6_REJECTION = PASS_VALIDATOR
- PLEBANSKI_SIMPLICITY_CROSSWALK = PASS_STANDARD
- MOIRE_OBSERVABLES_TO_B_FIELD = OPEN


## 13. Exact tetrahedral null-frame / Stella parity seed

The microscopic bridge now has an exact seed sector independent of anonymous legacy Phase36 coordinates.

Using the already-admitted positive elapsed-state lift,

\[
x_a^{(+)}=\frac{\ell_+}{2}(1,\mathbf n_a),
\]

for the four tetrahedral Bloch directions, the Gram determinant is

\[
\boxed{\det G=-\ell_+^8/27\neq0}.
\]

Thus the four canonical tetrahedral pure-state rays form a full-rank 4D null frame.

For the antipodal Stella layer

\[
x_a^{(-)}=\frac{\ell_-}{2}(1,-\mathbf n_a),
\]

one obtains exactly

\[
\boxed{
e_{-+}=E_-E_+^{-1}
=
q\,\operatorname{diag}(1,-1,-1,-1),
\qquad q=\ell_-/\ell_+.
}
\]

Therefore the ideal T / -T sector is a discrete spatial-parity operation multiplied by a positive conformal scale.

Its exterior-square image is

\[
\boxed{
C_2(e_{-+})
=
q^2\operatorname{diag}(-1,-1,-1,+1,+1,+1)
}
\]

in the basis \((01,02,03,23,31,12)\).

This closes a non-arbitrary **seed** route

\[
(T_4,-T_4,\ell_+,\ell_-)
\to
(E_+,E_-)
\to
e
\to
C_2(e),
\]

without selecting four coordinates from 36 and without hashing edge labels.

Firewall:

- constant parity is not gravity;
- constant conformal scaling is not gravity;
- the ideal Stella seed is too symmetric to span generic GR.

The next physical gate is the dynamics of local frame deformation,

\[
\boxed{
E_2(x)\neq q(x)P E_1(x),
\qquad
e(x)=E_2(x)E_1(x)^{-1},
}
\]

followed by the existing Levi-Civita/curvature and phenomenology gates.

Current status additions:

- TETRA_NULL_FRAME_RANK4 = PASS_EXACT
- STELLA_RELATIVE_PARITY_FRAME = PASS_EXACT
- STELLA_BIVECTOR_3PLUS3 = PASS_EXACT
- IDEAL_STELLA_SEED_TO_GENERIC_GRAVITY = FAIL_TOO_SYMMETRIC
- DYNAMICAL_FRAME_DEFORMATION_LAW = OPEN
