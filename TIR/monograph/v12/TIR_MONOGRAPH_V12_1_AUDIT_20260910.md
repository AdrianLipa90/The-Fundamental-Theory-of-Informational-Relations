# TIR Monograph v12.1 Repository-to-Publication Audit

Date: 2026-09-10
Baseline: `main@0f63c823961a58770de22d14b5f53e2bfa38a9b3`
Scope: active TIR publication/theorem/validation surfaces. Historical `archive/` trees are provenance only and are not promoted by this audit.

Status: `AUDIT_COMPLETE / CORRECTION_BRANCH_ACTIVE / MAIN_UNCHANGED`

## 1. Audit rule

The monograph is synchronized only from theorem surfaces, current status/evidence ledgers, deterministic validators, and merged repository history. A repository implementation PASS is not converted into an external physical PASS. Existing `FAIL`, `TENSION`, `OPEN`, and `QUARANTINED` verdicts are retained unless an explicit source theorem or evidence receipt supersedes them.

## 2. Confirmed monograph drift

The v12 publication baseline predates substantial merged TIR work. The following active surfaces were not fully represented in the v12 text:

1. Gate A2: conditional Cartan torsion/curvature refinement from the discrete solder/holonomy carrier.
2. Gate A3: endpoint-compatible zero-torsion selection and Levi-Civita uniqueness on a regular refining family.
3. Gate A4: leading-loop locality / metric-jet selection, with the leading GR carrier bounded to second metric-jet order under the TIR Leading Refinement Rule.
4. Gate A5: executable combinatorial 3-manifold certifier plus the standard Moise smoothing bridge; actual production TIR incidence data remain open.
5. GSC-1: global spatial-complex source/freeze/input contract; production spatial-complex data remain open.
6. Inter-leaf matching-field input contract; production `beta_match` data remain open.
7. Collatz-Fubini-Study relational-phase interface; the mathematical interface is present while physical time/energy/spectroscopy/gravity binding remains open.
8. Platonic L-constant closure: `(L3,L4,L5)=(7,2,5)` is now an exact TIR-internal structural consequence of the explicit tetrahedral-root extension rule, with the older Collatz/twin-prime route retained as an independent arithmetic crosscheck.
9. Critical-axis stack: several exact reductions and conditional positive corridors exist, but RH-equivalent global strict-positivity/nondegeneracy premises and RH itself remain open; the integrated audit explicitly requires `riemann_hypothesis_in_closure=false`.
10. Repository status surfaces drifted after feature merges: `CURRENT_STATUS.md`, `DEPENDENCY_EXPORT.json`, v12 README/manifests and reproducibility references require synchronization.

## 3. Corrections required in the monograph

### Chapter 7

Replace the old statement that Cartan refinement is merely the next theorem. Record Gate A2-A5 in dependency order and preserve the precise firewall:

`local/refining theorem PASS != production global relational-complex PASS`.

### Chapter 10

Retain the finite Collatz/twin-prime provenance but add the independent Platonic finite-group derivation:

`[S4:A4]=2`, `[A5:A4]=5`, and the explicit TIR root-extension carrier `S4/A4 disjoint-union A5/A4`, of cardinality seven.

The physical interpretation of this closure remains a separate open binding.

### Chapter 21

Replace the stale `23 nodes / 8 roots / 15 open gates` snapshot with a current frontier that distinguishes closed theorem/contract nodes from unresolved production inputs and physical/dynamical gates.

### Cross-framework/current-state appendix

Add a v12.1 appendix rather than rewriting the frozen v12 Appendix A-D provenance. The appendix must record post-v12 theorem surfaces, current open problems, retained empirical failures/tensions, and the critical-axis firewall.

### Front matter and build metadata

Mark the compiled artifact as `Version 12.1 Audited Repository Synchronization -- 10 September 2026`, while retaining v12.0 as the historical migration baseline.

## 4. Current open-problem register

### Global geometry and spacetime

- `PRODUCTION_GLOBAL_SPATIAL_COMPLEX_INPUT`: source/freeze/certifier machinery exists; the actual frozen production incidence complex is absent.
- `PRODUCTION_INTERLEAF_MATCHING_FIELD_INPUT`: the executable handoff contract exists; the source-owned production matching field is absent.
- `GLOBAL_TIR_IDT_RFC_SPACETIME_JOIN`: requires compatible global spatial and temporal/inter-leaf data and downstream RFC admission.
- `EINSTEIN_CONSTRAINT_EVOLUTION_CLOSURE`: downstream of the global spacetime join and RFC normalization/action gates.

### Information/phase physical binding

- `COLLATZ_FS_PHYSICAL_BINDING`: no validated rule yet maps the projective phase itinerary to elapsed time, energy, mass, transition strength, spectroscopy or gravity.
- `PHASE_CLOCK_INSTRUMENT_BINDING`: dimensionless projective geometry still requires an independently calibrated dimensionful/operational bridge where physical claims are made.
- `PLATONIC_L_PHYSICAL_INTERPRETATION`: the integer closure is internally exact; a physical identification beyond that theorem is not established by the finite-group result.

### Standard Model / particle sectors

- `COEFFICIENT_MAGNITUDE_EXTRACTION`: role and orientation are typed; the integer magnitudes `|h|,|a|,|b|,|c|` remain to be forced without target-value leakage.
- `CONTINUUM_GAUGE_NORMALIZATION`: derive `W_ij -> A_mu -> F_mn -> S_YM` with normalized coupling/running.
- `HYPERCHARGE_SOURCE_UNIQUENESS`: current arithmetic reproduces the conventional assignments, but the source/uniqueness theorem remains open.
- `ELECTROWEAK_SCHEME_SCALE_CLOSURE`: derive a common `R_EW(mu,scheme)` rather than observable-specific retuning.
- `HIGGS_SCALAR_ACTION_BINDING`: derive the scalar-sector structural combination/action rather than fit a mass target.
- `NEUTRINO_ABSOLUTE_ACTION_REPAIR`: the legacy printed absolute-action equation remains quarantined.
- `MESON_ABSOLUTE_ACTION_BASELINE`: pion/kaon legacy exponentials fail their own printed numerical values and require a source-derived absolute baseline.
- `STRONG_CP_HOLONOMIC_SOURCE`: the frozen legacy map remains upstream of a retained nEDM physical FAIL; any replacement must be re-derived from the holonomy/topological sector.
- `QUARK_MASS_MAP`: prime labels exist, but a scheme/scale-defined physical mass map remains open.
- `COSMOLOGY_DIMENSIONFUL_SCALE_BINDING`: the dimensionless arithmetic requires a unit-complete `rho_crit`/scale bridge.

### Retained empirical failures/tensions

These are not to be silently repaired by label changes:

- charged-lepton precision relations: `FAIL`;
- PMNS reactor angle `sin^2(theta13)=1/49`: `TENSION`;
- fine-structure, W, Z and Higgs frozen precision relations: `FAIL`/precision tension as recorded by Chapter 19;
- neutron EDM from the frozen strong-CP mapping: `FAIL` by approximately 2.96x against the manuscript bound;
- pion and kaon printed legacy exponentials: `FAIL`;
- baryon octet, eta/eta-prime, heavy/vector meson and selected cosmology surfaces retain provenance/quarantine states.

### Critical axis / Secret-of-a-Half interface

- native `Li/Weil` positivity is open;
- global strict transverse positivity / convexity conditions remain `OPEN_RH_EQUIVALENT_CRITERION`;
- global kernel nondegeneracy and equivalent bridge premises remain open;
- RH remains open and must not appear in the theorem closure;
- failed raw de Branges/other negative-control candidates remain retained as diagnostics rather than erased.

### Prospective evidence

- the frozen v10.7 candidate family remains pending its declared qualifying future likelihood/evidence gate under the no-refit rule.

## 5. Repository corrections on this branch

This audit authorizes only branch-level synchronization. `main` is not changed by this audit branch.

Planned synchronized surfaces:

- `TIR/CURRENT_STATUS.md`;
- `DEPENDENCY_EXPORT.json`;
- `TIR/REPRODUCIBILITY.md` and stale evidence-validator references;
- `TIR/monograph/tir_monograph_v12.tex` and front matter;
- v12 Chapter 7, Chapter 10 and Chapter 21;
- new v12.1 Appendix E;
- v12.1 repository-sync validator;
- compile workflow validator stack.

## 6. Promotion boundary

A successful monograph build establishes only:

`SOURCE_SYNC_PASS + VALIDATOR_PASS + LATEX/PDF_PREFLIGHT_PASS`.

It does not change any physical `OPEN`, `TENSION`, `FAIL`, or `QUARANTINED` verdict. Main promotion requires separate explicit authority after review of the compiled artifact.
