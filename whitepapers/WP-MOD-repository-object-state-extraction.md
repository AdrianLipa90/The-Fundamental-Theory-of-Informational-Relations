# WP-MOD — Repository object-state extraction surfaces

## Status
`defined`

## Scope
This whitepaper records the first executable export surface from a repository tree to `objects_state.csv` and `couplings.csv`.

## Theory highlights
- canonical files are discovered from the working tree
- exact relative-path mentions define the first coupling surface
- local and nonlocal features are lifted into the energetic object-state functional
- the export layer produces schema-conforming object and coupling tables

## Source files
- `definitions/DEF-0016-repository-object-state-extraction-surfaces.md`
- `derivations/D-0015-repository-object-state-extraction-from-canonical-files.md`
- `interfaces/IF-0014-repository-object-state-extraction.yaml`

## Code bindings
- `src/ciel_foundations/solvers/repo_object_state_extractor.py`
- `tests/test_repo_object_state_extractor.py`
- `Simulations/code/sim_repo_object_state_extraction.py`

## Epistemic note
This closes the first executable extraction surface only. The first coupling rule is still limited to exact path mentions, and frequency defaults remain uncalibrated unless extended downstream.
