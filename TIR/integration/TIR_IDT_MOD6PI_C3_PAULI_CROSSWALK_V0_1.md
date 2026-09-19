# TIR–IDT Mod-6pi C3 / Pauli Representation Crosswalk v0.1

Status: `REPRESENTATION_CROSSWALK_CLOSED / PHYSICAL_SECTOR_BINDING_OPEN`

Date: 2026-09-19

## Scope

This integration note reconciles three already-existing mathematical surfaces:

1. IDT half-frame temporal gluing and its (6pi) three-frame sector;
2. the TIR local generator carrier (operatorname{Herm}_0(2)congmathbb R^3) with Pauli basis;
3. the TIR (C_3) character basis (F_3) used in the family-space branch.

The new result is a representation crosswalk. It does not identify temporal, spatial, and flavour sectors as the same physical degree of freedom.

## 1. IDT periodic three-frame quotient

IDT 02J/02JB gives the open-cut (N=3) support path

[
|1|12|23|3|
]

with path complex (P_4).

Under the explicit periodic phase condition

[
ThetasimTheta+6pi,
]

the endpoints are identified,

[
v_0sim v_3,
]

and therefore

[
oxed{P_4/(v_0sim v_3)cong C_3.}
]

The ordered frame carrier has the cyclic shift

[
P_3=
egin{pmatrix}
0&0&1\
1&0&0\
0&1&0
end{pmatrix},
qquad
P_3^3=I.
]

## 2. Exact character crosswalk

The TIR Stage-38 character matrix is

[
F_3=rac1{sqrt3}
egin{pmatrix}
1&1&1\
1&omega&omega^2\
1&omega^2&omega
end{pmatrix},
qquad
omega=e^{2pi i/3}.
]

For the IDT cyclic shift,

[
oxed{
F_3^dagger P_3F_3
=
operatorname{diag}(1,omega^2,omega).
}
]

Thus the IDT periodic triad and the TIR Stage-38 family calculation use the same abstract (C_3) character decomposition.

This closes the representation-theoretic bridge only. It does not prove that the temporal carrier is the physical flavour carrier.

## 3. Exact Pauli crosswalk

TIR already establishes

[
operatorname{Herm}_0(2)
=
operatorname{span}_{mathbb R}{sigma_x,sigma_y,sigma_z}
congmathbb R^3
]

with Hilbert-Schmidt metric

[
langle A,Bangle=rac12operatorname{Tr}(AB).
]

Let the IDT ordered frame basis be (e_1,e_2,e_3). Define

[
iota(e_1)=sigma_x,qquad
iota(e_2)=sigma_y,qquad
iota(e_3)=sigma_z.
]

Because the Pauli basis is Hilbert-Schmidt orthonormal, (iota) is an isometric real vector-space isomorphism.

Now define

[
U_3=
exp!left[
-rac{ipi}{3}
rac{sigma_x+sigma_y+sigma_z}{sqrt3}
ight]in SU(2).
]

Direct calculation gives

[
U_3sigma_xU_3^dagger=sigma_y,qquad
U_3sigma_yU_3^dagger=sigma_z,qquad
U_3sigma_zU_3^dagger=sigma_x.
]

Hence

[
oxed{
iotacirc P_3
=
operatorname{Ad}_{U_3}circiota.
}
]

The IDT (C_3) frame action and the TIR cyclic Pauli action are therefore exactly equivariantly isomorphic.

The lift also satisfies

[
U_3^3=-I,qquad U_3^6=I,
]

whereas the adjoint action has order three. This is the standard (SU(2)	o SO(3)) double-cover structure and must not be conflated with the separate numerical value of the IDT (6pi) phase budget.

## 4. Consequence for the completion frontier

The earlier seam

[
{1,2,3}_{6pi}
stackrel{?}{longrightarrow}
{sigma_x,sigma_y,sigma_z}
]

should no longer be classified as wholly open.

Its corrected status is

[
oxed{
	ext{PERIODIC TRIAD}
	o
C_3
	o
	ext{PAULI EQUIVARIANT REPRESENTATION}
quad	ext{CLOSED}.
}
]

The remaining stronger claim

[
	ext{IDT temporal triad}
equiv
	ext{physical TIR spatial tangent carrier}
]

remains open and requires an explicit physical sector-binding theorem.

Likewise,

[
C_3	o F_3
]

is exact, but

[
	ext{IDT temporal }C_3
equiv
	ext{physical flavour }C_3
]

remains open.

## 5. Relation to existing TIR CP work

The crosswalk explains why the same (C_3/F_3) algebra can appear both in the temporal modular carrier and in the TIR family-space CP calculations.

It does **not** by itself promote the Stage-38 mathematical CP result to a temporal origin theorem for CKM CP violation. Such a promotion still requires a source-owned sector map that binds the temporal carrier to the quark-family operators without importing fitted or observed mixing data.

## 6. Validation

Deterministic validator:

`TIR/validation/tir_idt_mod6pi_c3_pauli_crosswalk_v0_1.py`

Parents:

- IDT: `formalism/02JN_modular_cyclic_c3_pauli_bridge.md`;
- TIR: `TIR/validation/tir_relational_generator_space_v0_1.py`;
- TIR Stage-38: `TIR/frozen_predictions/validation/scripts/c3_character_basis_cp_stage38_v01.py`.

Promotion boundary:

`REPRESENTATION_CROSSWALK_CLOSED / TEMPORAL_SPATIAL_PHYSICAL_BINDING_OPEN / TEMPORAL_FLAVOUR_PHYSICAL_BINDING_OPEN`.


---

## 7. Consolidated theorem frontier — NEW 2026-09-19

The append-only Appendix-letter stream is retired as the active presentation layer. The detailed derivations remain preserved in Git provenance at pre-consolidation `main@bc22bf7dc9e02b912656e2f229a8efee39c2bbc9`; the pre-consolidation blob of this file is `1081c2a2e8b6474e4aa013fed2f22ab219b5a411`.

The former Appendix A–BA material is compressed below into three theorem-chain blocks. Appendix AA is therefore cancelled as an active document unit; later AC–BA entries are also absorbed here rather than continued as further appendices. Historical labels remain provenance locators only.

### 7.1 Representation closure

The exact representation chain is now:

\[
P_4/(v_0\sim v_3)\cong C_3,
\qquad
F_3^\dagger P_3F_3=\operatorname{diag}(1,\omega^2,\omega),
\qquad
\omega=e^{2\pi i/3}.
\]

The ordered temporal \(C_3\) carrier and the active Stage-22/24 ordered family \(C_3\) carrier admit the exact order-preserving equivariant intertwiner. At label level the free cyclic anchor is removed by the independently checked source order.

The current weak carrier supplies

\[
A_1\simeq\mathfrak{su}(2),
\qquad
W(A_1)\cong Z_2,
\]

and therefore

\[
C_3\times Z_2\cong C_6,
\qquad
\dim(V_F\otimes V_W)=3\times2=6.
\]

All normalized \(A_1\) Cartan axes lie in one \(SU(2)\) conjugacy class, so the weak Weyl exchange is covariant under axis reorientation rather than requiring an absolute pre-breaking external axis.

Independently, Stage 21 supplies the multiplicity-three parent

\[
E_8\supset(E_6\times SU(3)_F)/Z_3,
\]

and Stage 24 binds the ordered seed basis to the exceptional triplet. This remains distinct from color \(SU(3)_C\).

The \(C_3\) label frame and its \(F_3\) character frame provide a nontrivial projective/Bargmann quadrilateral at representation level. This shows that the current family representation can carry a gauge-invariant projective phase structure; it does not identify that structure with observed CKM or PMNS data.

NEW: orientation reflection extends the family \(C_3\) to the non-Abelian \(D_3\cong S_3\), with real family representation

\[
\mathbf3_{\mathbb R}\cong\mathbf1\oplus\mathbf2.
\]

The commuting family×weak six-cycle is instead the Abelian \(C_6\). Adding orientation reflection extends that six-state carrier to the dihedral group of order \(12\); \(F_3\otimes F_2\) diagonalizes the \(C_6\) rotation into the exact sixth-root character spectrum. These finite-group closures are representation statements, not particle-spectrum identifications.

Current representation statuses:

```text
PERIODIC_6PI_C3                                      = CLOSED
C3_TO_F3_CHARACTER_FRAME                            = CLOSED
C3_TO_ACTIVE_STAGE22_24_ORDERED_FAMILY_CARRIER      = CLOSED
ORDER_PRESERVING_LABEL_INTERTWINER                   = CLOSED
A1_WEYL_Z2                                           = CLOSED
A1_CARTAN_AXIS_SU2_CONJUGACY_CLASS                   = CLOSED
FAMILY_C3_X_WEAK_Z2_TO_C6                            = CLOSED
THREE_X_TWO_SIX_STATE_CARRIER                        = CLOSED
STAGE21_E8_FAMILY_MULTIPLICITY_3                     = PASS
STAGE24_SEED_TO_E8_TRIPLET_INTERTWINER               = PASS
F3_JARLSKOG_MATH_TRANSFER                            = CLOSED
SU3F_LIE_DIMENSION_TRANSFER                          = CLOSED
C3_F3_PROJECTIVE_BARGMANN_STRUCTURE                  = CLOSED_REPRESENTATION_LEVEL
D3_ORIENTATION_EXTENSION_AND_3_EQ_1_PLUS_2           = CLOSED
C6_TO_ORDER12_DIHEDRAL_EXTENSION                     = CLOSED
PHYSICAL_FAMILY_GENERATION_IDENTIFICATION             = OPEN
PHYSICAL_CKM_PMNS_BINDING                             = OPEN
```

### 7.2 Dynamics / geometry bridge

The exact Collatz branch grammar now has the structural chain

\[
\{E,O\}^*
\longrightarrow
PSL(2,\mathbb R)
\xrightarrow{\operatorname{Sym}^2}
SL(3,\mathbb R),
\]

so the two-symbol branch dynamics has an exact three-component split-real carrier. The canonical Poincaré translation lengths of the normalized branch generators and the signed log-Jacobian cocycle give an exact branch-local geometric alphabet.

The compact geometry side supplies the symmetric-pair decomposition

\[
\mathfrak{su}(3)
=
\mathfrak{so}(3)\oplus\mathfrak p_5,
\qquad
\dim\mathfrak p_5=5,
\]

hence the current \(3\oplus5\) architecture: the spin-one three-carrier plus the five-dimensional \(SU(3)/SO(3)\) tangent complement. The \(N=5\) icosahedral realization provides the irreducible five-dimensional quadrupole carrier. This is a representation/tangent decomposition, not a claim of five physical spatial dimensions.

The Stage-65/66 stationary cubic selector is closed at its declared saddle:

\[
\boxed{
\eta_*
=
-\frac{75(59+21\sqrt5)}{638}
}.
\]

Its \(C_3\) orbit supplies three Stage-66 generators whose full orbit Lie-generates

\[
\operatorname{Lie}\langle iA_0,iA_1,iA_2\rangle
=
\mathfrak{su}(3)_F,
\qquad
\dim_{\mathbb R}=8.
\]

NEW: the finite-stopping Collatz basin has an exact temporal-\(C_3\) state index from stopping depth modulo three. This closes the representation-level state-to-orbit index and selects a state-dependent Stage-66 generator. The frozen signed-geometric \(SU(3)\) step built from that index and the branch sign passed hosted mathematical/provenance validation; every three consecutive \(C_3\) axes recover full eight-dimensional Lie accessibility.

NEW: the Collatz–Poincaré branch-rhythm candidate has passed hosted mathematical/provenance validation as a branch-local geometric rhythm. The physical Hamiltonian identification remains separate.

NEW: the actual terminal Collatz cycle

\[
1\to4\to2\to1,
\qquad
(O,E,E),
\]

produces a validated nonidentity \(SU(3)\) loop candidate. It is non-coboundary/path-nonseparable, basepoint-covariant, orientation-sensitive, outside every conjugate spin-one \(SU(2)\) subgroup, and a regular rank-two \(SU(3)\) conjugacy class with maximal-torus centralizer \(U(1)\times U(1)\). Orientation reversal gives the inverse loop and a distinct inner-conjugacy class; complex conjugation maps to the reverse-loop class. These are structural group-theoretic results only.

Current bridge statuses:

```text
COLLATZ_BRANCH_WORDS                                 = EXACT
BRANCH_WORD_TO_PSL2R                                 = CLOSED
PSL2R_TO_SYM2_THREE_CARRIER                          = CLOSED
POINCARE_BRANCH_TRANSLATION_LENGTH_ALPHABET           = CLOSED
SIGNED_LOG_JACOBIAN_COCYCLE                           = CLOSED
SU3_SO3_3_PLUS_5_DECOMPOSITION                        = CLOSED
N5_ICOSAHEDRAL_FIVE_CARRIER                           = CLOSED
STAGE66_STATIONARY_SELECTOR_ETA_STAR                  = CLOSED_SADDLE
STAGE66_C3_ORBIT_GENERATES_SU3F                       = CLOSED
STOPPING_DEPTH_MOD3_TO_TEMPORAL_C3_INDEX              = CLOSED_ON_FINITE_STOPPING_BASIN
STATE_DEPENDENT_SIGNED_GEOMETRIC_SU3_STEP             = PASS_MATH_PROVENANCE
BRANCH_LOCAL_COLLATZ_POINCARE_RHYTHM                  = PASS_MATH_PROVENANCE
TERMINAL_COLLATZ_NONFLAT_SU3_LOOP                     = PASS_RETROSPECTIVE_STRUCTURAL
TERMINAL_LOOP_NONCOBOUNDARY_PATH_SOURCE               = PASS
TERMINAL_LOOP_ORIENTATION_CLASS_STRUCTURE             = CLOSED_STRUCTURAL
```

### 7.3 Open physical binding / no-go ledger

The current frontier is no longer “missing mathematics everywhere.” Several candidate carriers and source-derived structures exist, but their physical identification remains gated.

For the rhythm variable, distinguish the validated mathematical candidate from the physical Hamiltonian binding:

\[
\rho_{\rm geo}(b_k)
\quad\text{is structurally available, while}\quad
\boxed{\rho_s(k)=\rho_{\rm geo}(b_k)}
\]

remains an OPEN physical/uniqueness identification.

For family transport, the source-derived common-target scaffold

\[
W^F_{ij}=G_i^\dagger G_j
\]

is an exact \(SU(3)\) groupoid, but it is a flat coboundary:

\[
W^F_{12}W^F_{23}W^F_{31}=I.
\]

It therefore cannot by itself source nonzero loop curvature or a physical CP phase. Separately, the terminal Collatz loop supplies a validated non-flat, non-coboundary path source. The remaining gate is the binding of that source to the physical family connection.

Stage 39 supplies two structural sector eigenframes. Their physical A/B assignment remains OPEN: the current coefficient-orientation theorem does not define the required up/down sector parameters, and the \(q_C\) sign correlation is not an admissible substitute. Stage 40 full CKM-shape failure remains retained without retuning.

The principal no-go results are:

```text
RAW_QC_AS_UNIFORM_MOD6PI_C3_CLOCK                     = REFUTED
ORDINARY_CENTER_COLLATZ_AS_STAGE24_C3_CYCLE            = REFUTED
ORDINARY_PRODUCT_SEED_COLLATZ_AS_STAGE24_C3_CYCLE      = REFUTED
DIRECT_SYM2_SPLIT_REAL_TO_SU3F_FIXED_SIMILARITY         = REFUTED
GENERATORWISE_POLAR_COMPACTIFICATION_AS_BRANCH_MAP      = REFUTED_ORDER_BLIND
WORDWISE_POLAR_FACTOR_AS_GROUP_REPRESENTATION           = REFUTED
NONTRIVIAL_CONTINUOUS_PSL2R_TO_SU3F_REAL_LIE_LIFT       = REFUTED
SCALAR_QC_SEPARABLE_PHASE_AS_CP_SOURCE                  = REFUTED
ACTIVE_EQUATORIAL_QC_BARGMANN_PHASE                     = ZERO
STATIC_SINGLE_AXIS_BRANCH_TO_FAMILY_MAP                 = REFUTED
STATIC_TWO_AXIS_EO_TO_STAGE66_ORBIT_MAP                 = REFUTED
STAGE52_SPIN1_BRIDGE_ALONE_AS_FULL_DC_FAMILY_PAIR       = INSUFFICIENT
COMMON_TARGET_WIJ_COBBOUNDARY_AS_NONFLAT_CP_SOURCE      = REFUTED
STAGE40_FULL_CKM_SHAPE                                  = FAIL_RETAINED
```

The principal OPEN physical bindings are:

```text
RHO_S_PHYSICAL_HAMILTONIAN_IDENTIFICATION               = OPEN
TERMINAL_PATH_SOURCE_TO_PHYSICAL_FAMILY_CONNECTION      = OPEN
STAGE39_STRUCTURAL_A_B_TO_PHYSICAL_UP_DOWN_ASSIGNMENT   = OPEN
TEMPORAL_C3_TO_PHYSICAL_FAMILY_GENERATION_INDEX          = OPEN
DYNAMICAL_COMPACT_REAL_FORM_SELECTION                    = OPEN
HIGGS_AND_HYPERCHARGE_VACUUM_ALIGNMENT                  = OPEN
MASS_AND_YUKAWA_DERIVATION                              = OPEN
PHYSICAL_CKM_PMNS_PARAMETER_FORCING                      = OPEN
FULL_PARTICLE_SPECTRUM_BINDING                          = OPEN
TEMPORAL_TO_SPATIAL_PHYSICAL_BINDING                     = OPEN
METRIC_SOURCE_GRAVITY_BINDING                            = OPEN
```

The orientation-sensitive terminal \(SU(3)\) loop is not, by itself, identified with physical CP, CKM, PMNS, charge conjugation, parity, or matter–antimatter asymmetry. Those interpretations remain outside the current theorem closure.

Future incremental results must be written as ordinary `NEW:` entries under one of these three blocks. No new Appendix-letter sequence is to be created. A later consolidation may promote a `NEW:` entry into the main theorem chain once its dependencies and status are stable.
