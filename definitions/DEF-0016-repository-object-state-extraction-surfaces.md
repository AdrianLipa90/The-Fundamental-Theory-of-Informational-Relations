# DEF-0016 — Repository object-state extraction surfaces

## Status
`hypothesis`

## Depends on
- `DEF-0015`

## Objects defined here
1. `OBJ-FILE-LOCAL-FEATURES-0001`
2. `OBJ-REPOSITORY-OBJECT-STATE-CSV-0001`
3. `OBJ-REPOSITORY-COUPLINGS-CSV-0001`
4. `OBJ-REPOSITORY-OBJECT-STATE-EXTRACTOR-0001`

## Local-feature extraction
For each canonical file object in a repository working tree, extract the local feature set
\[
\mathcal L_i=(\text{path}_i,\text{type}_i,\text{layer}_i,\text{content\_hash}_i,\text{size}_i,\text{local\_mass}_i).
\]
The first canonical local-mass ansatz is:
- token count for text-like files,
- nonempty noncomment line count for Python source.

## Coupling extraction
Define the first repository coupling extraction rule by exact relative-path mention:
\[
C_{ij}>0
\quad\text{iff}\quad
\text{path}_j\text{ appears in the textual content of object }i.
\]
The resulting coupling export is the table
\[
\mathcal C = \{(i,j,\text{relation\_type}_{ij},C_{ij},\Delta\phi_{ij},m_{ij})\}.
\]

## Object-state export
Given local features and extracted couplings, construct for each object the fields required by `objects_state.schema.yaml`, including:
- `crossref_in`, `crossref_out`,
- `pressure`, `density`, `weight`, `frequency`,
- `state_vector`, `character`,
- `raw_energy`, `norm_energy`, `amplitude`, `phase`, `state_signature`, `seed`.

## Canonical role
This module is the first executable export surface that connects repository files to the energetic object-state formalism.

## Registered fixture trace
For the registered fixture demo with three files,
\[
|\mathcal O|=3,
\qquad
|\mathcal C|=3.
\]
The exported normalized object energies are approximately
\[
(0.51979107,\ 0.33359383,\ 0.14661509),
\]
which sum to one.

## Executable bindings
- solver: `src/ciel_foundations/solvers/repo_object_state_extractor.py`
- simulation: `Simulations/code/sim_repo_object_state_extraction.py`
- section: `LaTeX/sections/SEC-0013-repository-object-state-extraction.tex`
- appendix: `LaTeX/appendices/APP-0011-repository-object-state-extraction.tex`

## Artifact bindings
- objects export: `Simulations/results/ART-0010-repo-object-state-fixture-demo.csv`
- couplings export: `Simulations/results/ART-0011-repo-couplings-fixture-demo.csv`
- provenance: `provenance/ART-0010-provenance.yaml`, `provenance/ART-0011-provenance.yaml`
- falsification: `falsification/FM-0010-repository-object-state-extraction.yaml`

## Scope restriction
This module defines the first executable extraction surface only. It does not yet calibrate repository-global frequencies from git history by default, and the first coupling rule is still limited to exact path mentions.
