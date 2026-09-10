# TIR Monograph v12.1 — audited dependency-ordered publication surface

Status: `V12_0_BASELINE_PRESERVED / V12_1_REPOSITORY_SYNC_ACTIVE / PROVENANCE_FIRST / VALIDATION_ACTIVE`

Audit baseline: `main@0f63c823961a58770de22d14b5f53e2bfa38a9b3`

Correction branch: `fix/tir-monograph-v12-1-sync-20260910`

Historical v12.0 integration baseline remains the 30 August 2026 content-migration publication surface. Version 12.1 synchronizes that architecture with later merged theorem and validation work without promoting unresolved physical claims.

## Purpose

The monograph is organized in dependency order:

`primitive informational relations -> emergent geometry -> information/phase/flavour -> particle and gauge sectors -> extensions and tests`.

All twenty-one main chapters remain substantive. Appendix E is the v12.1 repository-state synchronization layer; Appendices A-D remain frozen v12.0 provenance surfaces.

## Current foundational spine

```text
0
-> POINT
-> FIRST DISTINCTION
-> {N,S}
-> 1/2
-> ln2
-> C^2
-> Herm_0(2) ~= R^3
-> Euclidean relational metric
-> regular tetrahedral Gram class
-> W_ij transport
-> SE(3) affine lift
-> discrete solder/torsion source
-> Gate A2 Cartan refinement              [conditional local PASS]
-> Gate A3 T^a=0 / Levi-Civita             [admitted-sector PASS]
-> Gate A4 leading-loop metric jet <= 2    [LRR PASS]
-> Gate A5 3-manifold certifier            [implemented]
-> production global spatial complex       [OPEN INPUT]
```

The global-spacetime line additionally requires the production inter-leaf matching field, followed by TIR-IDT-RFC spacetime/ADM admission and the downstream Einstein-system gates.

## Information, flavour and L-constant state

The canonical information normalization remains

```text
C^3
-> SU(3)_F
-> dim su(3)=8
-> 3*8=24 mixing channels
-> half-turn phase pi
-> Phi_mix=24*pi
-> kappa=ln2/(24*pi)
```

Canonical source:

`TIR/foundations/TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md`.

The discrete structural constants now also have the independent Platonic finite-group closure

```text
A4 subset S4 -> [S4:A4] = 2 = L4
A4 subset A5 -> [A5:A4] = 5 = L5
S4/A4 disjoint-union A5/A4 -> cardinality 7 = L3
```

conditional on the explicit TIR tetrahedral-root extension rule. The Collatz/twin-prime path is retained as an independent arithmetic crosscheck. Canonical source:

`TIR/foundations/TIR_PLATONIC_L_CONSTANTS_CLOSURE_V0_1.md`.

## Evidence and falsification invariant

Version 12.1 preserves the existing `(Claim Class, Timing, Verdict)` taxonomy. The current evidence owner remains Chapter 19. In particular, repository theorem/contract PASS states do not overwrite charged-lepton precision failures, PMNS reactor-angle tension, electroweak/fine-structure/Higgs precision failures or tensions, pion/kaon formula failures, provenance quarantines, or the frozen strong-CP-to-neutron-EDM failure.

## Current open frontier

The current open problems are named gates rather than a frozen count:

- production global spatial-complex input and A5 certification on that exact dataset;
- production inter-leaf matching-field input;
- global TIR-IDT-RFC spacetime/ADM admission and Einstein constraint/evolution closure;
- coefficient magnitude extraction;
- continuum gauge normalization/running and hypercharge source uniqueness;
- common electroweak scheme/scale transport and Higgs scalar/action binding;
- scheme/scale-defined quark mass map;
- neutrino absolute-action repair and meson absolute-action baseline;
- holonomic/topological strong-CP source theorem;
- unit-complete cosmological scale/critical-density binding;
- physical binding of the Collatz-Fubini-Study relational phase;
- native Li/Weil positivity and globally quantified critical-axis nondegeneracy/strict-positivity conditions; the Riemann hypothesis remains open.

## Prospective programme

The frozen v10.7 three-candidate family and its orthogonal observables retain their no-refit evidence contract. A later qualifying dataset may score that frozen family; it does not retroactively become a parent of the structural derivations.

## Build surface

The master remains

`TIR/monograph/tir_monograph_v12.tex`

but its document metadata identify the compiled revision as **Version 12.1 Audited Repository Synchronization -- 10 September 2026**.

The repository-to-publication audit is

`TIR/monograph/v12/TIR_MONOGRAPH_V12_1_AUDIT_20260910.md`.

The current synchronization validators are

`TIR/validation/tir_v12_1_repository_sync_audit.py`

and

`TIR/validation/tir_v12_1_completion_frontier_dag_v0_2.py`.

The v12.0 migration manifest remains preserved as historical provenance; the v12.1 sync manifest records only the later correction layer.

## Promotion boundary

A green build means source synchronization, deterministic validation and PDF preflight passed on the exact branch head. It does not alter physical `OPEN`, `TENSION`, `FAIL` or `QUARANTINED` verdicts. Promotion of this corrected monograph to `main` is a separate explicit repository action.
