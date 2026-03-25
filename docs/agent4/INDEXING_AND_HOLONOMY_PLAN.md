# AGENT4 — Indexing and Cross-Reference Holonomy Plan

## Repository role
This repository is the first-principles / foundations layer for CIEL. It is upstream to Omega-facing runtime and demo surfaces.

## AGENT4 immediate mission
AGENT4 does not begin with runtime migration. It begins with internal epistemic closure of the repository graph.

Priority order:
1. inventory existing objects
2. distinguish real content from placeholders
3. identify native vs coupled vs export-facing objects
4. establish index authority
5. build internal cross-reference holonomy
6. define validator conditions
7. only then prepare export mappings downstream

## Object classes to use initially
- `native` — first-principles object owned by this repository
- `coupled_omega_facing` — object in this repo that is structurally coupled to Omega-facing layers
- `export_ready` — stabilized object suitable for downstream consumption
- `mirrored` — object mirrored from another context and requiring provenance/status care
- `placeholder` — structural slot without derived content
- `imported` — imported text/object not yet canonically stabilized

## Minimal object record requirements
Each indexed object should eventually have:
- stable ID
- name
- layer
- status
- class
- upstream links
- downstream links
- path
- tests
- implementations
- provenance
- export readiness marker

## Immediate AGENT4 work packages
### Package A — inventory seed
Map currently visible layers and sectors.

### Package B — index authority
Clarify the role of global index, layer indexes, and machine-readable registry.

### Package C — cross-reference holonomy
Record at least the following relation types:
- `upstream`
- `downstream`
- `couples_to`
- `exports_to`
- `mirrors`
- `surface_for`

### Package D — validator requirements
Prepare a validator spec that can later reject:
- code without upstream formal object
- placeholder presented as canonical content
- export-ready object lacking test or provenance
- missing upstream/downstream links

## Current caution
If `systems/CIEL_OMEGA_COMPLETE_SYSTEM` appears inside this repository tree, AGENT4 should treat it first as a possible coupling sector, not automatically as a contradiction of repository scope. Classification comes before migration decisions.

## Deliverable rule
AGENT4 should prefer small, index-oriented artifacts first:
- plans
- registry seeds
- mapping tables
- validator notes
- cross-reference manifests

Not large uncontrolled code moves.
