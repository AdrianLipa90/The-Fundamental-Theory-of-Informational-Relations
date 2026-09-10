# The Fundamental Theory of Informational Relations

https://www.researchgate.net/publication/408131825_Metatime_A_Low-Parameter_Ansatz_for_Standard_Model_Parameters_from_Geometric_Phase_Information_Theory

**Author:** Adrian Lipa — Independent Researcher, Doncaster, United Kingdom  
**Current audited monograph revision:** TIR v12.1 repository synchronization  
**Audit baseline:** `main@0f63c823961a58770de22d14b5f53e2bfa38a9b3`  
**Validated source head:** `b19d1becd7ed59263d2c78483b617bc4ef83bd3e`  
**Main promotion:** PR `#128` -> `main@3a31da6ebeded16d4f48345de62c974870f76694`  
**Publication status:** dependency-ordered research programme with mathematical, implementation, production-input and empirical gates tracked separately

## Overview

The **Fundamental Theory of Informational Relations (TIR)** is a research programme that develops a dependency-ordered relation between primitive informational structure, quantum/projective geometry, spatial transport, flavour structure, particle-sector relations and falsifiable empirical tests.

The active dependency spine is summarized as

```text
0
-> POINT
-> FIRST DISTINCTION
-> {N,S}
-> 1/2
-> ln2
-> C^2
-> Herm_0(2) ~= R^3
-> Euclidean relational geometry
-> tetrahedral closure
-> connection / holonomy / SE(3) / solder / torsion
-> A2 Cartan refinement
-> A3 zero-torsion / Levi-Civita sector
-> A4 leading-loop metric-jet selection
-> A5 global 3-manifold certifier
-> production global spatial + inter-leaf inputs
-> global spacetime / ADM / Einstein-system frontier
```

Historical v11 and v12.0 publication sources remain versioned provenance.

## Canonical κ normalization

The current internal TIR normalization surface gives

\[
\boxed{\kappa=\frac{\ln2}{24\pi}}
\]

from the declared three-flavour mixing carrier

\[
V_F\cong\mathbb C^3,
\qquad
U_F\in SU(3)_F,
\qquad
\dim_{\mathbb R}\mathfrak{su}(3)_F=8,
\]

with

\[
N_{\rm mix}=3(3^2-1)=24,
\qquad
\Delta\phi_{1/2}=\pi,
\qquad
H_2(1/2)=\ln2.
\]

Canonical source:

`TIR/foundations/TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md`

Validator:

`TIR/validation/tir_kappa_flavour_mixing_normalization_v0_1.py`

The exact conditional phase-rate consequence is

\[
\boxed{\Gamma_{\mathcal I}=\kappa\omega=\frac{\ln2}{12}f},
\qquad
\omega=2\pi f.
\]

Physical instrumentation of this quantity remains a separate open gate.

## Platonic L-constant closure

The convex Platonic classification contains exactly

\[
\{3,3\},\{3,4\},\{3,5\},\{4,3\},\{5,3\},
\]

so its index alphabet is \(\{3,4,5\}\). The triangular branch has rotational groups \(A_4,S_4,A_5\) with orders \(12,24,60\). With the tetrahedral rotational group as common root,

\[
\boxed{[S_4:A_4]=2},
\qquad
\boxed{[A_5:A_4]=5}.
\]

TIR defines the complete non-self-dual extension carrier

\[
X_3^{\rm closure}=S_4/A_4\sqcup A_5/A_4,
\]

hence

\[
\boxed{L_4=2,\qquad L_5=5,\qquad L_3=7},
\]

or

\[
\boxed{(L_3,L_4,L_5)=(7,2,5)}.
\]

This is an exact TIR-internal structural consequence conditional on the explicit root-extension rule. The pre-existing Collatz/twin-prime route remains an independent arithmetic crosscheck. The finite-group result alone is not a physical law.

Canonical source:

`TIR/foundations/TIR_PLATONIC_L_CONSTANTS_CLOSURE_V0_1.md`

Validator:

`TIR/validation/tir_platonic_l_constants_closure_v0_1.py`

## Emergent geometry and current GR stack

The local binary-state carrier supplies

\[
\mathcal A_2=\frac12 I+\operatorname{Herm}_0(2),
\qquad
\operatorname{Herm}_0(2)\cong\mathbb R^3,
\]

with invariant metric

\[
\langle A,B\rangle=\frac12\operatorname{Tr}(AB).
\]

The finite isotropic branch reaches the regular tetrahedral Gram class. Typed connection transport is

\[
W_{ij}^{WT}\in U(1),
\qquad
W_{ij}^{X}\in SU(2),
\qquad
W_{ij}^{c}\in SU(3),
\]

and the spatial affine lift is

\[
G_{ij}^{\nabla}=(R_{ij},\mathbf e_{ij})\in SE(3),
\qquad
R_{ij}=\operatorname{Ad}(W_{ij}^{X}).
\]

The discrete torsion source satisfies

\[
\mathcal T_{xyz}=-\mathcal C_{xyz}.
\]

Current theorem status:

```text
Gate A   discrete solder/torsion source             PASS
Gate A2  Cartan torsion/curvature refinement        PASS, conditional local/refining theorem
Gate A3  T^a=0 and Levi-Civita selection            PASS on admitted endpoint-compatible sector
Gate A4  leading-loop second metric-jet carrier     PASS under TIR Leading Refinement Rule
Gate A5  global 3-manifold certifier                IMPLEMENTED
         production global spatial complex          OPEN INPUT
         production inter-leaf matching field       OPEN INPUT
```

Canonical post-v12 sources include

`TIR/foundations/TIR_CARTAN_CONTINUUM_REFINEMENT_V0_1.md`

`TIR/foundations/TIR_ZERO_TORSION_LEVI_CIVITA_SELECTION_V0_1.md`

`TIR/foundations/TIR_LEADING_LOOP_LOCALITY_METRIC_JET_V0_1.md`

`TIR/foundations/TIR_GLOBAL_3MANIFOLD_SMOOTH_CERTIFICATE_V0_1.md`

`TIR/foundations/TIR_GLOBAL_SPATIAL_COMPLEX_INPUT_CONTRACT_V0_1.md`

`TIR/foundations/TIR_INTERLEAF_MATCHING_FIELD_INPUT_CONTRACT_V0_1.md`

The A5 certifier and input-contract PASS states do not imply that the actual production TIR incidence data have been supplied.

## Collatz–Fubini–Study relational phase

The merged mathematical interface includes

\[
q(Cn)=2q(n)\pmod1,
\qquad
\zeta_C(Cn)=\zeta_C(n)^2,
\]

and types an explicit projective phase coordinate on a TIR relation. Projective \(2\pi\) and optional spinorial \(4\pi\) carriers remain distinct. Physical identification with elapsed time, energy, mass, interaction strength, spectroscopy, chemistry or gravity remains open.

Source:

`TIR/integration/TIR_COLLATZ_FS_RELATIONAL_PHASE_INTERFACE_V0_1.md`

## Evidence architecture

Publication status uses

```text
(Claim Class, Timing, Verdict)
```

from

`TIR/monograph/v12/STATUS_TAXONOMY.md`.

Chapter 19, **Unified Evidence Matrix**, is the current observable-level evidence owner. The normalized machine audit is

`TIR/validation/tir_v12_evidence_matrix_consistency_v0_2.py`.

Current retained states include CKM retrospective compatibility, PMNS reactor-angle tension, charged-lepton precision failures, hadron and meson provenance/formula quarantines, electroweak precision failures/tensions, the frozen neutron-EDM physical failure and cosmological arithmetic/unit quarantine. A technical theorem or software PASS is never substituted for an empirical PASS.

## Current Standard-Model frontier

The active structural tasks are

```text
coefficient magnitude extraction
W_ij -> continuum gauge connection/curvature normalization
hypercharge source/uniqueness theorem
scheme/scale-defined quark mass map
common electroweak R_EW(mu,scheme) transport
Higgs scalar/action binding
neutrino absolute-action repair
meson absolute-action baseline
strong-CP holonomic/topological source theorem
cosmological dimensionful scale/rho_crit binding
```

The current reconciliation ledger is

`TIR/standard_model/TIR_SM_RECONCILIATION_LEDGER_V0_1.md`.

## Secret-of-a-Half / critical-axis boundary

The critical-axis stack contains exact identities, equivalence reductions and conditional positive corridors, but global strict-positivity/nondegeneracy premises remain open. The integrated solver contract explicitly requires

```text
"riemann_hypothesis_in_closure": false
```

so the Riemann hypothesis remains open. RH-equivalent criteria are not reported as a proof.

## Prospective programme

The frozen v10.7 separable candidate family retains its two orthogonal observables, future-data gate and no-refit/no-substitution rule. Its later evidence is downstream of the frozen formulas, never an upstream fitting parent.

## Monograph and audit surfaces

Current master:

`TIR/monograph/tir_monograph_v12.tex`

Current audited synchronization:

`TIR/monograph/v12/TIR_MONOGRAPH_V12_1_AUDIT_20260910.md`

Current sync manifest:

`TIR/monograph/v12/MONOGRAPH_SYNC_V12_1.yaml`

Current source/sync/frontier validators:

```text
TIR/validation/tir_v12_source_contract_v0_3.py
TIR/validation/tir_v12_1_repository_sync_audit.py
TIR/validation/tir_v12_1_completion_frontier_dag_v0_2.py
```

Appendices A-D preserve the v12.0 frozen provenance hashes. Appendix E records post-v12 repository synchronization.

## Repository map

```text
TIR/
├── foundations/
├── integration/
├── interfaces/
├── standard_model/
├── validation/
├── zeta_information_axis/
├── subrepos/
│   └── the-space-of-geometry/
└── monograph/
    ├── tir_monograph_v12.tex
    ├── v12/
    │   ├── STATUS_TAXONOMY.md
    │   ├── MIGRATION_MANIFEST.yaml
    │   ├── MONOGRAPH_SYNC_V12_1.yaml
    │   ├── chapters/
    │   └── appendices/
    └── metatime_monograph.tex
```

## Research and publication policy

The repository preserves source provenance and version identity; retrospective and prospective evidence remain separate; failed gates stay visible; scheme- and scale-dependent quantities require explicit conventions; GREMLIN is candidate/audit infrastructure rather than promotion authority; and publication promotion requires exact-head deterministic validation plus PDF preflight. TIR v12.1 has now been promoted to `main` through PR #128 after the exact source head passed the full validation/build/preflight suite. This repository promotion does not change any physical `OPEN`, `TENSION`, `FAIL` or `QUARANTINED` verdict.

## Citation

Until a DOI-backed v12.1 release is deposited, cite the repository and exact Git commit used.

```bibtex
@misc{Lipa2026TIR,
  author       = {Adrian Lipa},
  title        = {Theory of Informational Relations: Foundations, Emergent Geometry, and Phenomenological Tests},
  year         = {2026},
  howpublished = {The Fundamental Theory of Informational Relations repository},
  url          = {https://github.com/AdrianLipa90/The-Fundamental-Theory-of-Informational-Relations},
  note         = {Audited v12.1 repository synchronization; cite the exact Git commit used}
}
```
