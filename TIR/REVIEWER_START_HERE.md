# Reviewer Orientation — Theory of Informational Relations v12.1

## Review scope

The audited publication master remains

`TIR/monograph/tir_monograph_v12.tex`

and is compiled as **Version 12.1 Audited Repository Synchronization — 10 September 2026**. The v12.0 migration state and earlier source tree remain historical provenance.

Read the current dependency order as

```text
primitive informational relations
-> emergent geometry
-> information / phase / flavour
-> particle and gauge sectors
-> extensions / evidence / falsification
```

## Canonical structural primitives

- \(\kappa=\ln2/(24\pi)\): TIR-internal derived normalization with explicit flavour-mixing and half-turn parents;
- \((L_3,L_4,L_5)=(7,2,5)\): exact TIR-internal structural consequence of the explicit Platonic tetrahedral-root extension rule, with Collatz/twin-prime arithmetic retained as an independent crosscheck;
- \((u,d,s,c,b,t)=(3,5,7,11,13,17)\): typed prime-label assignment with exhaustive permutation audit;
- external anchors, scales and conversion conventions are tracked separately from internal structural quantities.

Canonical sources:

`TIR/foundations/TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md`

`TIR/foundations/TIR_PLATONIC_L_CONSTANTS_CLOSURE_V0_1.md`

## Current geometry state

Do not use the v12.0 phrase “next Cartan gate” as current status. The active repository has:

```text
Gate A   discrete solder/torsion source               PASS
Gate A2  Cartan torsion/curvature refinement          PASS, conditional local/refining theorem
Gate A3  T^a=0 / Levi-Civita selection                PASS on admitted endpoint-compatible sector
Gate A4  leading-loop second metric-jet selection     PASS under the TIR Leading Refinement Rule
Gate A5  global 3-manifold certifier                  IMPLEMENTED
         production global spatial-complex input      OPEN
         production inter-leaf matching field         OPEN
```

The theorem/production-input distinction is mandatory. Reference-control or certifier PASS does not imply that the actual global TIR spatial complex or inter-leaf field has been supplied.

## Read evidence through three axes

Every publication result is read as

`(Claim Class, Timing, Verdict)`

with the canonical taxonomy in

`TIR/monograph/v12/STATUS_TAXONOMY.md`.

The current observable-evidence owner is

`TIR/monograph/v12/chapters/ch19_unified_evidence_matrix.tex`.

Its normalized machine audit is

`TIR/validation/tir_v12_evidence_matrix_consistency_v0_2.py`.

New theorem or software PASS states do not overwrite existing physical `FAIL`, `TENSION`, `OPEN` or `QUARANTINED` rows.

## High-value current review targets

1. **κ parent chain:** verify the three-flavour carrier, eight-dimensional mixing algebra, 24-channel incidence count, half-turn phase and binary-information numerator.
2. **Platonic L closure:** verify the five Schläfli pairs, \([S_4:A_4]=2\), \([A_5:A_4]=5\), and the explicit TIR disjoint-union closure rule; keep physical interpretation separate.
3. **Spatial A2-A5 stack:** verify every theorem assumption and the production-input firewall.
4. **Coefficient magnitudes:** role/orientation are typed; \(|h|,|a|,|b|,|c|\) extraction remains open.
5. **Particle-sector evidence:** retain the neutrino absolute-action quarantine, PMNS reactor-angle tension, hadron provenance states, electroweak precision failures/tensions, meson formula failures and frozen nEDM failure.
6. **Global inputs:** require source-owned frozen spatial incidence and inter-leaf matching data before global spacetime promotion.
7. **Critical axis:** confirm `riemann_hypothesis_in_closure=false`; RH-equivalent positivity/nondegeneracy conditions remain open, not proved.
8. **Prospective evidence:** confirm formula hashes, observables, decision rules and no-refit contracts before unblinding.

## GREMLIN-assisted review discipline

GREMLIN remains a constrained candidate/audit layer. Candidate generation, dependency search or adversarial synthesis is not canonical promotion. Promotion requires a separately identified theorem, validator or evidence gate.

## Quick reproducibility checks

```text
python3 TIR/validation/tir_kappa_flavour_mixing_normalization_v0_1.py
python3 TIR/validation/tir_platonic_l_constants_closure_v0_1.py
python3 TIR/foundations/validation/tir_cartan_continuum_refinement_v0_1.py
python3 TIR/foundations/validation/tir_zero_torsion_levi_civita_selection_v0_1.py
python3 TIR/foundations/validation/tir_leading_loop_locality_metric_jet_v0_1.py
python3 TIR/foundations/validation/tir_global_3manifold_smooth_certificate_v0_1.py
python3 TIR/validation/tir_v12_evidence_matrix_consistency_v0_2.py
python3 TIR/validation/tir_v12_1_completion_frontier_dag_v0_2.py
python3 TIR/validation/tir_v12_source_contract_v0_3.py
python3 TIR/validation/tir_v12_1_repository_sync_audit.py
```

Appendices A-D retain their frozen v12.0 integrity gate. Appendix E is the explicit v12.1 repository-state synchronization layer.

## Publication boundary

A green exact-head build certifies source synchronization, named validators and PDF integrity on that commit. It is not external experimental validation and does not merge or promote the correction branch by itself.
