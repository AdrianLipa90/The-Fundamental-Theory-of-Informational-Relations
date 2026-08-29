# TIR Standard-Model Reconciliation Ledger v0.1

Status: `CURRENT_BRANCH_RECONCILIATION_2026_08_29`

This ledger reconciles the active monograph sources with the PDG-2026 addendum and the later TIR structural modules. It separates structural derivation, numerical comparison, provenance and the exact next closure operation.

## 1. Gauge skeleton and holonomy

Status: `STRUCTURAL_CARRIER_PASS__DYNAMICAL_NORMALIZATION_ACTIVE`

The internal bundle decomposition supports

\[
G_{SM}=SU(3)_c\times SU(2)_L\times U(1)_Y,
\]

while the holonomic colour layer uses

\[
W_{ij}^{c}\in SU(3),
\qquad
W_{ji}^{c}=(W_{ij}^{c})^\dagger,
\]

and

\[
U_{012}=W_{01}^{c}W_{12}^{c}W_{20}^{c}.
\]

The common `W_ij` typing is now recorded in

`TIR/foundations/TIR_WIJ_HOLONOMY_CROSSWALK_V0_1.md`.

Next closure operation:

\[
W_{ij}
\to A_\mu
\to F_{\mu\nu}
\to S_{YM}
\to\text{normalized gauge coupling/running}.
\]

## 2. CKM

Status: `STRONG_POSTDICTION_COMPATIBILITY__STRUCTURAL_PHASE_SURVIVES_2026_AUDIT`

The PDG-2026 addendum records all nine printed CKM magnitudes within about `1.71 sigma` of the selected reference fits, with mean absolute pull about `1.09 sigma`. The phase

\[
\delta_{CKM}=\arccos(2/5)=66.42^\circ
\]

and the structural Jarlskog value remain close to the selected 2026 reference snapshot.

Next closure operation: bind the full CKM matrix to the same coefficient-free holonomic/orientation forcing theorem used by the mass/flavour sector.

## 3. PMNS

Status: `MIXED_2026_COMPATIBILITY__REACTOR_ANGLE_TENSION`

The active chapter already carries the 2026 correction. The structural values for the solar sector remain close to the selected reference region; the reactor prediction

\[
\sin^2\theta_{13}=\frac1{49}\approx0.02041
\]

is the main explicit tension in the current frozen map.

Next closure operation: derive the correction, if any, from the already-existing flavour/holonomy dynamics rather than from a numerical retuning of the edge ratio.

## 4. Weak angle

Status: `STRUCTURAL_RELATION_FROZEN__SCHEME_SCALE_MAP_REQUIRED`

The frozen relation is

\[
\sin^2\theta_W^{(0)}=\frac29+\kappa.
\]

The active chapter now types precision transport as

\[
\sin^2\theta_W^{(0)}
\xrightarrow{\mathcal R_W(\mu,\mathrm{scheme})}
\sin^2\theta_W(\mu,\mathrm{scheme}).
\]

Next closure operation: derive `R_W` jointly with the electroweak running map.

## 5. Fine structure

Status: `LOW_RELATIVE_RESIDUAL__PRECISION_PROMOTION_REQUIRES_OBSERVABLE_SCALE_BINDING`

The current structural relation remains

\[
\alpha^{-1}_{TIR}
=(L_3L_4)^2-L_3^2-L_4L_5+L_4^2\kappa.
\]

The active monograph already carries the PDG-2026 precision correction. The next task is to identify the exact renormalized observable and scale to which the structural quantity maps.

## 6. W and Z

Status: `TREE_LEVEL_STRUCTURAL_MAP_FROZEN__PRECISION_FAIL__RG_CLOSURE_ACTIVE`

The frozen tree-level map is

\[
g_0=\frac{L_4}{L_3}+\frac{L_4}{L_5}=\frac{24}{35},
\]

\[
M_W^{(0)}=\frac{g_0v_0}{2},
\qquad
M_Z^{(0)}=\frac{M_W^{(0)}}{\cos\theta_W^{(0)}}.
\]

The active precision target is now

\[
\boxed{
(g_0,\theta_W^{(0)},v_0)
\xrightarrow{\mathcal R_{EW}(\mu,\mathrm{scheme})}
(g(\mu),\theta_W(\mu),v(\mu))
\to(M_W^{pole},M_Z^{pole}).
}
\]

No observable-specific scalar repair is part of the active path.

## 7. Higgs

Status: `RETROSPECTIVE_STRUCTURAL_RELATION__FIELD_THEORETIC_BINDING_ACTIVE`

The active relation is

\[
M_H=v\kappa(L_3^2+L_4+L_5).
\]

The numerical value is close in fractional terms but the relation was revised after the target was known. Its next promotion step is not another numerical correction: it is a derivation of the combination

\[
L_3^2+L_4+L_5
\]

from the scalar-sector geometry/action already present in the framework.

## 8. Charged leptons and quarks

Status: `STRUCTURAL_ROUTING_PRESENT__PHYSICAL_BINDING_THEOREM_ACTIVE`

The intrinsic recovered coefficient state is

\[
(h,a,b,c)\in\mathbb Z^4.
\]

Slot-role routing is structurally implemented, and directed/relational orientation operators exist. The remaining closure target is now stated as a forcing theorem:

\[
\boxed{
\text{coefficient-free state + framework grammar}
\Longrightarrow
(h,a,b,c)\text{ assignment up to finite declared degeneracy}.
}
\]

Observed masses and Yukawa values are excluded from the parent side of this theorem.

## 9. Pseudoscalar mesons

Status: `PRINTED_EXPONENTIAL_MAP_QUARANTINED__ABSOLUTE_ACTION_BASELINE_REQUIRED`

The active chapter already records that the printed pion and kaon exponential equations do not numerically produce the displayed masses. The correct next task is to derive the absolute action baseline from the same holonomy/action framework, then reevaluate the meson map from frozen inputs.

## 10. Strong CP / neutron EDM

Status: `FROZEN_V11_RELATION_PHYSICAL_FAIL__NEW_HOLONOMIC_DERIVATION_REQUIRED_FOR_REPLACEMENT`

The current monograph relation

\[
\theta_{QCD}=\kappa\left(\frac{L_4}{L_3}\right)^{14}
\]

with the frozen hadronic conversion produces the retained nEDM failure receipt. This receipt remains part of the version history.

The replacement axis, if the theory supplies one, must originate upstream from the now-explicit non-Abelian loop/holonomy sector:

\[
W_{ij}^{c}
\to U_\gamma
\to\text{topological CP phase/sector invariant}
\to\theta_{QCD}
\to d_n.
\]

This keeps the next strong-CP formula tied to a structural source rather than to a post-comparison exponent change.

## 11. Current closure order inside SM

```text
1. coefficient forcing theorem
2. W_ij -> continuum connection / curvature normalization
3. electroweak R_EW and R_W scheme/scale maps
4. Higgs scalar-sector binding
5. strong-CP holonomic phase derivation
6. meson absolute-action baseline
7. rerun one deterministic 2026 sector matrix
```

The statistical summary is a maintenance layer after these structural maps are frozen.