# Master Plan

## Purpose
Convert this repository from a scaffold created by tarball unpacking into a rigorously organized, derivation-first public theory program.

## Current state
The repository already contains the correct top-level categories and an initial roadmap, but many core objects are still placeholders:
- axioms exist but formal statements are TODO
- definitions registry is largely empty
- constants have folders but placeholder derivations/code/tests
- core source modules are stubs
- tests are category placeholders, not object-level tests
- sectors are declared but not yet wired to inherited operators/constants

## Planning doctrine
All work must respect:
- single canonical public theory tree
- registry-first insertion
- no interpretation ahead of derivation
- no downstream Omega logic as source of truth here
- every step leaves explicit provenance and status

## Execution phases

### Phase 0 — Governance freeze
Goal: make the repository self-consistent before deriving new content.

Tasks:
1. Freeze canonical procedure in `AGENT.md`.
2. Normalize registries so every declared object has a matching path.
3. Add a definitions plan linking axioms -> definitions -> derivations -> modules.
4. Add missing publication/public-only hygiene controls (`.gitignore`, publication rules, artifact exclusions) if absent.

Exit criteria:
- AGENT procedure exists
- registry drift is identified
- every placeholder area has a declared owner phase

### Phase 1 — Foundations object graph
Goal: replace abstract scaffold with a real dependency skeleton.

Tasks:
1. Create canonical definitions entries for:
   - relation
   - potential
   - information
   - state
   - boundary
   - locality
   - attractor
   - holonomy
   - white thread
   - closure
2. Expand `definitions/registry.yaml` from empty placeholders into explicit records.
3. Link each definition to at least one axiom and one downstream derivation target.
4. Add equation / object IDs where missing.

Exit criteria:
- definitions registry is populated
- each core term has a canonical location
- dependency graph includes definitions layer explicitly

### Phase 2 — Minimal executable core
Goal: turn declared modules into real minimal modules.

Priority order:
1. initial_conditions
2. bloch
3. closure
4. holonomy
5. tau_solver
6. genesis

Tasks per module:
- write formal derivation note
- define interface
- implement minimal executable path
- add symbolic/numeric tests
- add falsification entry where needed
- register artifacts if generated

Exit criteria:
- each module has non-placeholder code
- each module has at least one passing canonical test
- each module is linked to assumptions and falsification criteria

### Phase 3 — Constants program
Goal: move constants from placeholder folders to explicit derivation program.

Priority constants:
1. I0
2. tau
3. kappa
4. Lambda0

Tasks:
- write exact role statements
- declare dependency path for each constant
- implement canonical code representation
- add tests for invariants / consistency
- mark epistemic status honestly

Exit criteria:
- constant registry contains explicit derivation/code/test links
- no constant folder remains a pure placeholder

### Phase 4 — Sector bootstrap
Goal: wire sectors to inherited theory objects rather than local invention.

Order:
1. neutrino
2. lepton
3. quark
4. hadron
5. cosmology

Tasks:
- define sector interface
- record imported constants/operators
- define minimal falsification targets
- attach whitepaper skeletons

Exit criteria:
- each sector declares what it consumes from foundations
- no sector invents local copies of canonical constants/operators

### Phase 5 — Export surface for Omega
Goal: define downstream contract without contaminating theory source of truth.

Tasks:
- define export manifests for constants/operators/constraints
- version export schema
- document import contract for Omega/demo repositories
- mark public stabilized vs provisional objects

Exit criteria:
- Omega-facing export layer is explicit
- downstream consumption does not rely on ad hoc copying

## First concrete sprint
The next concrete work items should be:
1. populate `definitions/registry.yaml`
2. create canonical definition files for the core ontology
3. add `.gitignore`
4. add publication/sanitization rules
5. replace placeholder tests in `tests/*` with real test files for initial conditions and closure
6. update dependency graph to include definitions layer

## Non-negotiable checks before any future "final" claim
- registries synchronized
- no placeholder presented as derived content
- no duplicate source-of-truth object
- tests present for changed executable modules
- falsification path declared
- downstream/public boundary respected
