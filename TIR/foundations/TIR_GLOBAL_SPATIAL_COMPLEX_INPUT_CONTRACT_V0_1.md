# TIR Global Spatial-Complex Input Contract v0.1

Status: `INPUT_CONTRACT_DEFINED / A5_HANDOFF_FAIL_CLOSED / PRODUCTION_SPATIAL_COMPLEX_OPEN`

## Purpose

Gate A5 already certifies a supplied closed tetrahedral complex as a combinatorial 3-manifold and then uses the standard three-dimensional smoothing bridge. The remaining GSC-1 dependency is the concrete global spatial incidence datum.

This contract makes that datum machine-readable without selecting or inventing a global topology.

## Dataset contract

A supplied dataset has schema `TIR_GLOBAL_SPATIAL_COMPLEX_INPUT_V0_1` and contains:

- a non-empty `dataset_id`;
- representation `closed_tetrahedral_complex`;
- an explicit boolean `production`;
- provenance fields `source` and `source_commit_or_digest`;
- a unique list of string vertex identifiers;
- a non-empty list of tetrahedra, each containing four distinct declared vertices;
- `incidence_sha256`, computed canonically from the vertex and tetrahedron incidence data.

Every declared vertex must occur in at least one tetrahedron. The contract rejects undeclared vertices, duplicate vertex identifiers, malformed tetrahedra, missing provenance and digest mismatch.

## A5 handoff

After structural and integrity validation, the tetrahedral incidence data are passed directly to the existing A5 certifier

`certify_closed_combinatorial_3manifold`.

The promotion condition is

```text
production = true
AND input_valid
AND integrity_valid
AND manifold_certified
```

Only then is `promotion_eligible=true`.

The standard boundary-of-the-4-simplex control is retained solely as a reference dataset. It is frozen with `production=false`, so a reference `S^3` control cannot promote GSC-1.

## Dependency result

```text
TIR local regular tetrahedral cell
 + supplied global tetrahedral incidence dataset
 -> input-contract / provenance / digest gate
 -> A5 closed combinatorial 3-manifold certifier
 -> GSC-1 production spatial carrier eligibility
```

The current global spatial incidence dataset remains an open source-owned input.

## Falsification rules

The input gate fails closed on malformed identifiers, missing provenance, incidence digest mismatch, undeclared or unused vertices, malformed tetrahedra, or any structural input error. A structurally valid dataset may still receive `manifold_certified=false` from A5; the input contract never masks that result.

## Validation authority

Implementation:
`TIR/foundations/validation/tir_global_spatial_complex_input_contract_v0_1.py`

Static contract receipt:
`TIR/foundations/validation/TIR_GLOBAL_SPATIAL_COMPLEX_INPUT_CONTRACT_V0_1.json`

Hosted workflow:
`.github/workflows/tir-global-spatial-complex-input-contract.yml`

Verdict target:
`PASS_TIR_GLOBAL_SPATIAL_COMPLEX_INPUT_CONTRACT_WITH_PRODUCTION_INPUT_OPEN`.
