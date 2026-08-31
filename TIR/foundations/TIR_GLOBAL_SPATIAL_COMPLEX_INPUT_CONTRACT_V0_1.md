# TIR Global Spatial-Complex Input Contract v0.1

Status: `INPUT_CONTRACT_DEFINED / SOURCE_CAPTURE_FREEZE_DEFINED / A5_HANDOFF_FAIL_CLOSED / PRODUCTION_SPATIAL_COMPLEX_OPEN`

## Purpose

Gate A5 certifies a supplied closed tetrahedral complex as a combinatorial 3-manifold and then uses the standard three-dimensional smoothing bridge. The remaining GSC-1 dependency is the concrete global spatial incidence datum.

This contract gives that datum a machine-readable source capture, deterministic freeze stage, provenance surface and A5 handoff.

## Source capture and deterministic freeze

A source producer submits schema

`TIR_GLOBAL_RELATIONAL_COMPLEX_CAPTURE_V0_1`

with:

- a non-empty `capture_id`;
- source metadata `source_id`, `source_class` and `immutable_ref`;
- source class in `{PRODUCTION_SOURCE, REFERENCE_CONTROL, CANDIDATE_SOURCE}`;
- `capture_receipt_sha256` for `PRODUCTION_SOURCE`;
- a non-empty list of tetrahedral cells;
- one unique `cell_id` per source cell;
- exactly four distinct string vertex identifiers per cell.

The freeze adapter

`TIR/foundations/validation/tir_global_spatial_complex_source_freeze_v0_1.py`

canonicalizes vertex order inside each tetrahedron, canonicalizes source-cell order by `cell_id`, derives the global vertex set, rejects repeated source cells and repeated tetrahedral facets, and computes a source-capture SHA-256.

It then constructs the existing `TIR_GLOBAL_SPATIAL_COMPLEX_INPUT_V0_1` object and immediately invokes the GSC-1 input validator/A5 handoff. The frozen dataset carries both the source capture digest and the canonical incidence digest.

`PRODUCTION_SOURCE` admission requires a 64-hex capture receipt in the source capture. `REFERENCE_CONTROL` and `CANDIDATE_SOURCE` freeze to non-production datasets. The A5 manifold result remains an independent downstream condition.

## Dataset contract

A frozen dataset has schema `TIR_GLOBAL_SPATIAL_COMPLEX_INPUT_V0_1` and contains:

- a non-empty `dataset_id`;
- representation `closed_tetrahedral_complex`;
- an explicit boolean `production` inherited from the admitted source class;
- provenance fields `source` and `source_commit_or_digest` plus freeze metadata;
- a unique list of string vertex identifiers;
- a non-empty list of tetrahedra, each containing four distinct declared vertices;
- `incidence_sha256`, computed canonically from the vertex and tetrahedron incidence data.

Every declared vertex occurs in at least one tetrahedron. The contract validates identifiers, provenance, cell structure and digest agreement.

## Facet-list minimality audit

For a finite pure abstract simplicial 3-complex, the maximal simplices are tetrahedra. Their facet list determines every lower-dimensional simplex by downward closure:

\[
\boxed{\mathcal T\Longrightarrow(V,E,F,\mathcal T).}
\]

Therefore the tetrahedral facet incidence is the irreducible combinatorial content consumed by A5. The explicit `vertices` field in this contract is an integrity/provenance redundancy: validation requires it to agree exactly with the vertex set derived from the tetrahedra.

Aggregate counts carry less information than facet incidence. A deterministic control pair uses two eight-tetrahedron complexes with the same full f-vector

\[
\boxed{(f_0,f_1,f_2,f_3)=(6,14,16,8).}
\]

The positive member is a stellar subdivision of one tetrahedron in the boundary of the 4-simplex and remains an `S^3` triangulation. The second member has the same f-vector and A5 distinguishes it through triangular-face incidence.

Hence

\[
\boxed{f\text{-vector equality does not determine the A5 manifold certificate}.}
\]

The production witness may use any lossless encoding equivalent to the facet incidence table; the freeze adapter provides the canonical repository representation.

## A5 handoff

After structural and integrity validation, the tetrahedral incidence data are passed directly to the existing A5 certifier

`certify_closed_combinatorial_3manifold`.

The promotion condition is

```text
source_class = PRODUCTION_SOURCE
AND capture_receipt_sha256 valid
AND input_valid
AND integrity_valid
AND manifold_certified
```

Only then is `promotion_eligible=true`.

The standard boundary-of-the-4-simplex control remains a reference dataset with `source_class=REFERENCE_CONTROL` and `production=false`.

## Dependency result

```text
source-owned global relational complex capture
 -> deterministic tetrahedral facet freeze
 -> source-capture digest + canonical incidence digest
 -> GSC-1 input-contract / provenance gate
 -> A5 closed combinatorial 3-manifold certifier
 -> GSC-1 production spatial carrier eligibility
```

The current global spatial incidence dataset remains an open source-owned input.

## Falsification rules

The source-freeze gate validates source class, production receipt shape, unique cell identifiers, tetrahedral arity, unique facets and deterministic canonicalization. The input gate validates vertex/provenance/incidence integrity. A5 supplies the topological manifold verdict.

The facet-minimality control also verifies that aggregate simplex counts and full incidence remain separately typed evidence surfaces.

## Validation authority

Source capture schema:
`TIR/foundations/validation/TIR_GLOBAL_RELATIONAL_COMPLEX_CAPTURE_V0_1.schema.json`

Source freeze implementation:
`TIR/foundations/validation/tir_global_spatial_complex_source_freeze_v0_1.py`

Source freeze validation:
`TIR/foundations/validation/tir_global_spatial_complex_source_freeze_validation_v0_1.py`

Input implementation:
`TIR/foundations/validation/tir_global_spatial_complex_input_contract_v0_1.py`

Static contract receipt:
`TIR/foundations/validation/TIR_GLOBAL_SPATIAL_COMPLEX_INPUT_CONTRACT_V0_1.json`

Hosted workflow:
`.github/workflows/tir-global-spatial-complex-input-contract.yml`

Verdict target:
`PASS_TIR_GLOBAL_SPATIAL_COMPLEX_INPUT_CONTRACT_WITH_SOURCE_FREEZE_AND_PRODUCTION_INPUT_OPEN`.
