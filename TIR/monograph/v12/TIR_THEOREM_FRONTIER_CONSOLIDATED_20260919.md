# TIR Theorem Frontier — consolidated 2026-09-19 snapshot

Status: `HISTORICAL_CONSOLIDATED_VIEW / CONTENT_PRESERVED / DOES_NOT_OVERRIDE_CURRENT_STATUS`

Source branch: `docs/theorem-chain-frontier-consolidation-20260919`

Imported into current main lineage: 2026-09-22.

This document preserves the unique three-block compression from the historical consolidation branch without replacing the newer, more complete `TIR/CURRENT_STATUS.md`, `TIR_COMPLETION_FRONTIER_V0_7.md`, or the expanded integration theorem chain.

## NEW — consolidated theorem frontier (2026-09-19)

The former Appendix-update stream is no longer the active status format. Its full pre-consolidation state remains in Git at `main@bc22bf7dc9e02b912656e2f229a8efee39c2bbc9` and blob `352a37bf7bf74e6d356b0bb5cd87666dafd99cdf`. The current status is compressed into the three blocks below.

### Representation closure

The periodic IDT carrier closes to \(C_3\); \(F_3\) is its exact character basis; the ordered temporal and active Stage-22/24 family \(C_3\) carriers have an exact order-preserving intertwiner. The current \(A_1\simeq\mathfrak{su}(2)\) weak carrier supplies its Weyl \(Z_2\), giving

\[
C_3\times Z_2\cong C_6,
\qquad
\dim(V_F\otimes V_W)=3\times2=6.
\]

Stage 21 independently supplies \(E_8\supset(E_6\times SU(3)_F)/Z_3\), and Stage 24 binds the ordered seed basis to the exceptional triplet. The \(C_3/F_3\) projective frames support the representation-level Bargmann structure. Orientation extensions \(D_3\cong S_3\), \(\mathbf3=\mathbf1\oplus\mathbf2\), the order-12 six-state dihedral extension, and the exact sixth-root \(C_6\) character spectrum are closed as finite representation results.

```text
REPRESENTATION_CROSSWALK                         = CLOSED
ORDERED_TEMPORAL_TO_FAMILY_C3_INTERTWINER       = CLOSED
A1_WEYL_Z2                                      = CLOSED
FAMILY_C3_X_WEAK_Z2_TO_C6                       = CLOSED
THREE_X_TWO_SIX_STATE_CARRIER                   = CLOSED
E8_FAMILY_MULTIPLICITY_3                        = PASS
F3_BARGMANN_REPRESENTATION_STRUCTURE            = CLOSED
FINITE_ORIENTATION_EXTENSIONS                   = CLOSED
PHYSICAL_FAMILY_GENERATION_BINDING              = OPEN
```

NEW: fractal-orbital Lorentz carrier. The hyperbolic orbital carrier now has an explicit representation bridge
\[
\mathfrak{su}(1,1)\cong\mathfrak{so}(2,1)\subset\mathfrak{so}(3,1),
\]
with \(q=\tanh(\chi/2)\) and \(\beta=2q/(1+q^2)=\tanh\chi\). This closes a representation crosswalk only; physical spacetime binding remains separately gated.

### Dynamics / geometry bridge

The structural chain

\[
\{E,O\}^*
\to PSL(2,\mathbb R)
\xrightarrow{\operatorname{Sym}^2}
SL(3,\mathbb R)
\]

is exact. Canonical Poincaré branch lengths and the signed log-Jacobian cocycle provide the branch-local geometric alphabet. The compact geometry side closes the \(3\oplus5\) decomposition and the \(N=5\) icosahedral five-carrier.

The Stage-65/66 selector is closed at

\[
\eta_*=-\frac{75(59+21\sqrt5)}{638},
\]

and the full Stage-66 \(C_3\) orbit Lie-generates \(\mathfrak{su}(3)_F\). Stopping depth modulo three closes the representation-level Collatz-to-temporal-\(C_3\) state index on the finite-stopping basin. The state-dependent signed-geometric \(SU(3)\) step and the branch-local Collatz–Poincaré rhythm have hosted mathematical/provenance PASS.

The terminal \(1\to4\to2\to1\) Collatz cycle supplies a validated nonidentity, non-coboundary, orientation-sensitive \(SU(3)\) loop candidate. It lies outside every conjugate spin-one \(SU(2)\) subgroup and defines a regular rank-two \(SU(3)\) conjugacy class. Physical interpretation remains separately gated.

```text
COLLATZ_TO_PSL2R_TO_SYM2_THREE_CARRIER          = CLOSED
POINCARE_BRANCH_GEOMETRIC_ALPHABET               = CLOSED
SU3_SO3_3_PLUS_5                                 = CLOSED
STAGE66_SELECTOR_ETA_STAR                        = CLOSED_SADDLE
STAGE66_C3_ORBIT_TO_FULL_SU3F                    = CLOSED
STOPPING_DEPTH_MOD3_TO_C3_STATE_INDEX            = CLOSED
SIGNED_GEOMETRIC_SU3_STEP                        = PASS_MATH_PROVENANCE
COLLATZ_POINCARE_BRANCH_RHYTHM                   = PASS_MATH_PROVENANCE
TERMINAL_NONFLAT_SU3_PATH_SOURCE                 = PASS_STRUCTURAL
```

NEW: orbital-flow gravity controls. Ordered non-collinear orbital boosts generate the expected Lorentz rotation commutator. With the candidate coframe
\[
e^0=c\,d\tau,\qquad e^i=dX^i-V_{\rm FO}^i d\tau,
\]
the profiles \(V=-\sqrt{2GM/R}\,\hat r\) and \(V=H(t)R\) reproduce exact Schwarzschild Painleve-Gullstrand and flat-FLRW physical-radius controls respectively. These are exact control identities, not yet a source derivation.

NEW: ADM flow constraint strengthening. For the already-admitted unit-lapse flat-slice flow coframe, stationary spherical vacuum ADM data satisfy
\[
\frac{d}{dr}(rV^2)=0,
\]
hence \(V^2=C/r\). Weak-field/ADM mass normalization gives \(C=2GM\). This upgrades the Schwarzschild Painleve-Gullstrand profile from inserted control to a conditional derivation downstream of the existing TIR ADM/Einstein gate. Microscopic source-to-coframe binding remains open.

NEW: native inter-leaf shift to rapidity. The existing TIR matching-field export \(b_{(0)}=\beta_t/c\) is exactly the flow-coordinate carrier up to the declared sign convention \(V=-cb_{(0)}\). Hence \(\chi=\operatorname{artanh}|b|\) on the subluminal chart and the Poincare radial coordinate follows without a new scale. In spherical symmetry the full metric gives \(m_{\rm MS}=rV^2/(2G)\), separating gauge-dependent shift representation from invariant mass content. Production \(\beta_{\rm match}\) remains open.

NEW: event-indexed metric-rate source bridge. IDT realized-event edges may be paired with TIR spatial snapshots under one source-owned realization receipt and calibrated clock. The finite estimator
\[
\Delta h_{ij}/\Delta x^0
\]
converges to \(\partial_0h_{ij}\) on a regular smooth refinement and is handed to the existing RFC RF-E9 operator. No competing \(K_{ij}\) is introduced. This removes a generic physical identity \(x_{\rm IDT}=\rho_{\rm TIR}\) from the minimum production premises.

NEW: information-scalar acceleration theorem. The RF-E12/RF-E13 flat-FLRW reduction gives \(a''/a=-\kappa_E(\rho+3p)/6\). On the locally Fisher-normalized information-scalar branch, \(U_I=\alpha_I\Xi_I/\kappa_E\) and \(\phi_I=\sqrt{2\Xi_I}\), hence
\[
\frac{a''}{a}\Big|_I=\frac{\alpha_I\Xi_I}{3}-\frac{\kappa_E}{6\Xi_I}(\Xi_I')^2.
\]
An additional bare cosmological constant is not required for this mechanism; the absolute \(\alpha_I\) scale remains physically open.

NEW: holonomy-stress no-go. The current RF-L3 action preserves \(\tau_R\) but is independent of it, so holonomy is presently a spectator in stress-energy. Further, \(C_h+D_h=1\) makes a same-stress C/D partition gravitationally \(\tau_R\)-independent. A holonomy-active completion therefore requires differential stress attribution, a derived holonomy-dependent action, a dynamical holonomy stress, or a genuinely topological/frozen contribution. The candidate \(\Lambda_D=\alpha_I\Xi_I\sin^2(\tau_R/2)\) is not promoted without the complementary C-channel/Bianchi ledger and persistence/stability closure.

NEW: temporal-U1 metric-response route. RF-E4 fixes pure homogeneous phase kinetic stress at w=+1, so the phase-kinetic sector is decelerating rather than dark-energy-like. RF-F20 supplies a genuinely non-bookkeeping correction \(\Delta T^{phase}_{\mu\nu}=4A^2R_{\mu\nu}\). In an isotropic orthonormal sector its acceleration correction is \(-2\kappa_EA^2(R_0+3R_s)/3\), so the correction accelerates iff \(R_0+3R_s<0\). Closed-loop holonomy does not determine the local off-shell metric response; the temporal-U(1)/holonomy to local Berry/Euler \(R_{\mu\nu}\) binding remains OPEN.

### Open physical binding / no-go ledger

The branch-local geometric rhythm is validated structurally, but the physical Hamiltonian identification

\[
\rho_s(k)=\rho_{\rm geo}(b_k)
\]

remains OPEN.

The source-derived common-target family transport

\[
W^F_{ij}=G_i^\dagger G_j
\]

is an exact \(SU(3)\) groupoid but a flat coboundary, so it cannot by itself source physical loop curvature. A non-flat terminal path source exists structurally; its binding to the physical family connection remains OPEN.

Stage 39 structural sector frames are present, but the physical A/B up/down assignment is OPEN. Stage 40 full CKM-shape failure remains retained without retuning.

```text
RHO_S_PHYSICAL_HAMILTONIAN_BINDING               = OPEN
PHYSICAL_NONFLAT_FAMILY_WIJ_BINDING              = OPEN
STAGE39_A_B_TO_PHYSICAL_UP_DOWN_ASSIGNMENT        = OPEN
STAGE40_FULL_CKM_SHAPE                            = FAIL_RETAINED

DIRECT_SPLIT_REAL_SYM2_TO_SU3F_SIMILARITY         = REFUTED
GENERATORWISE_POLAR_BRANCH_COMPACTIFICATION       = REFUTED_ORDER_BLIND
WORDWISE_POLAR_FACTOR_REPRESENTATION              = REFUTED
CONTINUOUS_PSL2R_TO_SU3F_REAL_LIE_LIFT            = REFUTED
SCALAR_QC_SEPARABLE_CP_SOURCE                     = REFUTED
ACTIVE_EQUATORIAL_QC_BARGMANN_PHASE               = ZERO
STATIC_SINGLE_OR_TWO_AXIS_BRANCH_MAPS             = REFUTED
COMMON_TARGET_WIJ_AS_NONFLAT_CP_SOURCE            = REFUTED
```

Still OPEN downstream: temporal-to-physical-family identification, dynamical compact-real-form selection, Higgs/hypercharge vacuum alignment, mass/Yukawa derivation, physical CKM/PMNS forcing, full particle-spectrum binding, temporal-to-spatial physical binding, and metric/source gravity binding.

NEW: gravity physical-binding firewall. The map \(B\omega\mathcal N/(AR\Lambda)\to\chi(x)\), the unique orbital recursion \(\to V_{\rm FO}\), and the field equation for \(V_{\rm FO}\) remain OPEN. Pure local Lorentz relabeling is explicitly rejected as a gravity source. Existing TIR Levi-Civita zero torsion and an optional teleparallel torsion representation refer to different connections and are not conflated. A dark-energy-like interpretation is only a mechanism claim if the derived dynamics yields \(\dot H_{\rm FO}+H_{\rm FO}^2>0\) without retuning.

NEW: event-spatial production frontier. The coordinate shift is not a fundamental observable target. Remaining gravity closure requires source-owned event-spatial snapshots with the same physical-realization receipt and clock identity, plus sufficient refinement/coverage for the continuum claim. Reference fixtures, NOEMA/PhaseNav runtime vectors and synthetic event graphs cannot satisfy this production gate.

```text
INFORMATION_SCALAR_ACCELERATION_CRITERION             = PASS_EXACT_LOCAL_CANONICAL
CURRENT_RFL3_HOLONOMY_STRESS_COUPLING                 = SPECTATOR_NO_GO
EQUAL_STRESS_C_D_PARTITION_HOLONOMY_EFFECT            = NO_GO
HOLONOMY_DIFFERENTIAL_STRESS_OR_ACTION_BINDING        = OPEN
COMPLEMENTARY_C_CHANNEL_BIANCHI_LEDGER                = OPEN
NONTRIVIAL_HOLONOMY_PERSISTENCE_OR_STABILITY          = OPEN
ABSOLUTE_ALPHA_I_NORMALIZATION                        = OPEN
```

Future small additions are written as `NEW:` under one of these three blocks. No further Appendix-letter sequence is active.



## NEW — 2026-09-24 continuation — vacuum integration / response / dimensional frontier

RF-F15 fixed-x transport carries the conserved integration coordinate \(C_\Lambda=|\omega|^4[v-(1-x)/2]\) and the exact conditional acceleration transition \(a''/a=\kappa_E(\rho_\Lambda-\rho_r)/3\). Its sign and magnitude remain boundary/physical inputs. RF-F22 supplies the distinct response threshold \((R_0+3R_s)/\mu_\vartheta^2+(S_0+3S_s)<-1/2\). Same-metric lapse reuse gives projector self-normalization and zero stress. Since \([C_\Lambda]=T^{-4}\) while winding/Chern/holonomy are dimensionless, topology alone cannot determine nonzero absolute \(C_\Lambda\); an independent \(\Omega_*\) is required.

```text
RF_F15_CONSTANT_VACUUM_TRANSPORT = PASS_EXACT_CONDITIONAL
RF_F22_PROJECTOR_RESPONSE_THRESHOLD = PASS_EXACT_CONDITIONAL
SAME_METRIC_LAPSE_PROJECTOR = SELF_NORMALIZED_ZERO_STRESS_NO_GO
EULER_SPIN_METRIC_RESPONSE = OPEN
C_LAMBDA_TOPOLOGICAL_ABSOLUTE_SCALE = NO_GO_WITHOUT_OMEGA_STAR
C_LAMBDA_OVER_OMEGA_STAR_4_TOPOLOGY = OPEN
```
