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

## Facet-list minimality audit

For a finite pure abstract simplicial 3-complex, the maximal simplices are tetrahedra. Their facet list determines every lower-dimensional simplex by downward closure:

\[
\boxed{\mathcal T\Longrightarrow(V,E,F,\mathcal T).}
\]

Therefore the tetrahedral facet incidence is the irreducible combinatorial content consumed by A5. The explicit `vertices` field in this contract is an integrity/provenance redundancy: validation requires it to agree exactly with the vertex set derived from the tetrahedra.

Aggregate counts cannot replace facet incidence. A deterministic control pair uses two eight-tetrahedron complexes with the same full f-vector

\[
\boxed{(f_0,f_1,f_2,f_3)=(6,14,16,8).}
\]

The positive member is a stellar subdivision of one tetrahedron in the boundary of the 4-simplex and remains an `S^3` triangulation. The negative member has the same f-vector but A5 rejects it because several triangular faces have incidence one or three instead of two.

Hence

\[
\boxed{f\text{-vector equality does not determine the A5 manifold certificate}.}
\]

The production witness may use any lossless encoding equivalent to the facet incidence table, but a summary invariant that discards incidence is insufficient for GSC-1 promotion.

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

The input gate fails closed on malformed identifiers, missing provenance, incidence digest mismatch, undeclared or unused vertices, malformed tetrahedra, or any structural input error. A structurally valid dataset may still receive `manifold_certified=false` from A5; the input contract preserves that result.

The minimality control additionally rejects replacement of the facet incidence witness by aggregate simplex counts.

## Validation authority

Implementation:
`TIR/foundations/validation/tir_global_spatial_complex_input_contract_v0_1.py`

Static contract receipt:
`TIR/foundations/validation/TIR_GLOBAL_SPATIAL_COMPLEX_INPUT_CONTRACT_V0_1.json`

Hosted workflow:
`.github/workflows/tir-global-spatial-complex-input-contract.yml`

Verdict target:
`PASS_TIR_GLOBAL_SPATIAL_COMPLEX_INPUT_CONTRACT_WITH_PRODUCTION_INPUT_OPEN`.
