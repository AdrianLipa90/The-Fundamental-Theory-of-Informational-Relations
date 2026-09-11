# TIR Standard-Model Reconciliation Ledger v0.2

Status: `COEFFICIENT_PARENT_EVALUATION_CLOSED / TRANSITION_SELECTOR_AND_DYNAMICS_ACTIVE`

Date: 2026-09-10

Supersedes the v0.1 status view while preserving every historical empirical verdict and source receipt.

## 1. Coefficient branch

The generator remains

\[
G(h,a,b,c)=\frac h2+a\kappa+b\frac{\kappa}{L_3}+c\frac{\kappa^2}{2}.
\]

Role identity and source-sign forcing remain typed by

`TIR/foundations/TIR_COEFFICIENT_ROLE_ORIENTATION_FORCING_V0_1.md`.

A source audit establishes that the historical charged-lepton lineage already declares magnitude-parent packets. Using only the closed upstream values

\[
N_F=3,\qquad (L_3,L_4,L_5)=(7,2,5),
\]

the packet valuations are uniquely

\[
M(P_e)=(1,3,1,1),
\]

\[
M(P_{e\mu})=(0,5,2,8),
\]

\[
M(P_{\mu\tau})=(0,3,1,7).
\]

Status: `COEFFICIENT_MAGNITUDE_PARENT_EVALUATION = CLOSED_EXACT`.

Canonical source:

`TIR/foundations/TIR_COEFFICIENT_MAGNITUDE_PARENT_EVALUATION_V0_1.md`.

The current atomic operator does not yet map coefficient-free transition data to a unique parent packet. The exact identifiability audit proves that role routing and orientation alone are insufficient and that an additional transition-sensitive invariant is required.

Status: `COEFFICIENT_TRANSITION_PARENT_SELECTOR = OPEN`.

Canonical non-identifiability source:

`TIR/foundations/TIR_COEFFICIENT_TRANSITION_SELECTOR_IDENTIFIABILITY_V0_1.md`.

No mass, Yukawa target, recovered tuple or tuple-generated runtime envelope is admitted as a selector parent.

## 2. Gauge skeleton and continuum normalization

The internal carrier remains

\[
G_{SM}=SU(3)_c\times SU(2)_L\times U(1)_Y,
\]

with typed links including

\[
W_{ij}^{c}\in SU(3),\qquad W_{ji}^{c}=(W_{ij}^{c})^\dagger.
\]

The unresolved normalization chain remains

\[
W_{ij}\to A_\mu\to F_{\mu\nu}\to S_{YM}
\to\text{normalized coupling/running}.
\]

Status: `CONTINUUM_GAUGE_NORMALIZATION = OPEN`.

## 3. CKM and PMNS

The v12.1 evidence owner remains Chapter 19. No coefficient-parent bookkeeping change modifies the empirical classification.

CKM retains its retrospective compatibility status under the frozen formula family. PMNS retains the reactor-angle tension associated with

\[
\sin^2\theta_{13}=\frac1{49}.
\]

Any future correction must be derived from upstream flavour/holonomy dynamics rather than target residuals.

## 4. Electroweak scheme/scale closure

The frozen tree-level relations remain historical structural inputs. The required precision bridge is one common map

\[
(g_0,\theta_W^{(0)},v_0)
\xrightarrow{\mathcal R_{EW}(\mu,\mathrm{scheme})}
(g(\mu),\theta_W(\mu),v(\mu))
\to(M_W^{pole},M_Z^{pole}).
\]

Status: `ELECTROWEAK_SCHEME_SCALE_CLOSURE = OPEN`.

The current W/Z precision failures and weak-angle/fine-structure tensions are not erased by this open map.

## 5. Hypercharge and quark map

The conventional one-generation anomaly arithmetic passes, but the source/uniqueness theorem for hypercharge remains open.

Status: `HYPERCHARGE_SOURCE_UNIQUENESS = OPEN`.

The prime-label layer and Platonic L closure do not by themselves produce a scheme- and scale-defined physical quark-mass map. Any coefficient contribution required by that map is downstream of the open transition-parent selector.

Status: `QUARK_MASS_MAP = OPEN`.

## 6. Higgs

The active structural expression remains retrospective and requires an upstream scalar/action derivation rather than numerical repair against the measured mass.

Status: `HIGGS_SCALAR_ACTION_BINDING = OPEN`.

It is downstream of electroweak normalization and, where a discrete coefficient packet is used, of the transition-parent selector.

## 7. Strong CP / neutron EDM

The frozen legacy relation retains its physical neutron-EDM failure. A replacement must originate from the colour holonomy/topological sector:

\[
W_{ij}^{c}\to U_\gamma
\to\text{topological CP invariant}
\to\theta_{QCD}\to d_n.
\]

Status: `STRONG_CP_HOLONOMIC_SOURCE = OPEN`.

No change in this ledger overwrites the frozen nEDM `FAIL`.

## 8. Mesons

The printed pion and kaon exponential maps remain failed legacy formulas. The structural repair target is a source-derived absolute action baseline, with any coefficient packet selected upstream rather than inferred from the observed mass.

Status: `MESON_ABSOLUTE_ACTION_BASELINE = OPEN`.

## 9. Neutrinos

The historical printed double-κ action and the values it accompanied are inconsistent. The v12 diagnostic reconstruction identifies the historical calculation path but does not constitute a new upstream action theorem.

Status: `NEUTRINO_ABSOLUTE_ACTION_REPAIR = OPEN`.

The retrospective mass-splitting compatibility remains distinct from absolute-action closure.

## 10. Cosmology

The remaining task is a dimensionally complete bridge from dimensionless TIR structure to a declared physical scale and critical density:

\[
(L_3,L_4,L_5)
\to r_\Lambda
\to M_\star^4
\to\rho_\Lambda
\to\rho_{crit}
\to\Omega_\Lambda.
\]

Status: `COSMOLOGY_DIMENSIONFUL_SCALE_BINDING = OPEN`.

Historical quarantined arithmetic/unit statements remain quarantined.

## 11. Current Standard-Model closure order

The current dependency-aware order is

```text
1. COEFFICIENT_TRANSITION_PARENT_SELECTOR
2. CONTINUUM_GAUGE_NORMALIZATION
3. HYPERCHARGE_SOURCE_UNIQUENESS and QUARK_MASS_MAP
4. ELECTROWEAK_SCHEME_SCALE_CLOSURE
5. HIGGS_SCALAR_ACTION_BINDING
6. STRONG_CP_HOLONOMIC_SOURCE
7. MESON_ABSOLUTE_ACTION_BASELINE
8. NEUTRINO_ABSOLUTE_ACTION_REPAIR
9. COSMOLOGY_DIMENSIONFUL_SCALE_BINDING
10. rerun the unified evidence matrix only after the relevant structural maps are frozen
```

The coefficient magnitude-parent evaluator is no longer listed as an open arithmetic task. The transition-parent selector is the remaining non-circular coefficient theorem.

## 12. Evidence firewall

The following statuses remain owned by the evidence layer until a separately versioned predictive construction is frozen and tested:

```text
charged leptons precision       FAIL
PMNS reactor angle              TENSION
legacy W/Z precision            FAIL
legacy pion/kaon formulas       FAIL
legacy strong-CP -> nEDM        FAIL
selected provenance/unit rows   QUARANTINED
```

A structural or software PASS cannot promote these rows.
