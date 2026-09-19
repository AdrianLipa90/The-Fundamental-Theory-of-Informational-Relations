# TIR Physical-Realization Source Bundle v0.2

Status: `EXECUTABLE_SOURCE_BUNDLE_CERTIFIER / SAME_REALIZATION_GATE_CLOSED / PRODUCTION_SOURCE_CAPTURES_OPEN / CANON_ALLOWED_FALSE`

Date: 2026-09-19

## 1. Purpose

This source contract records the already-merged executable composition between the TIR global spatial capture and the TIR inter-leaf matching capture.

The implementation authority is

`TIR/foundations/validation/tir_production_realization_binding_v0_2.py`.

The bundle does not infer or fabricate a physical realization. It certifies that independently source-owned production captures refer to one and the same declared physical realization.

## 2. Bundle schema

The outer object has schema

`TIR_PHYSICAL_REALIZATION_SOURCE_BUNDLE_V0_2`

and contains exactly two typed source surfaces:

```text
spatial_capture : TIR_GLOBAL_RELATIONAL_COMPLEX_CAPTURE_V0_2
matching_input  : TIR_INTERLEAF_MATCHING_FIELD_INPUT_V0_2
```

Both inner captures must carry:

```text
physical_realization_id
physical_realization_receipt_sha256
```

The realization receipt is a 64-character lowercase SHA-256 digest.

## 3. Spatial capture requirements

The spatial v0.2 capture extends the existing GSC-1 source capture and is passed through the existing source-freeze and A5 input/certification path.

Promotion review eligibility requires both:

```text
production_source_admitted = true
manifold_certified         = true
```

The bundle does not replace the existing GSC-1/A5 source contract.

## 4. Matching capture requirements

The matching v0.2 input extends the existing inter-leaf matching-field input contract and therefore retains:

- source provenance;
- temporal coordinate kind `t` or `x0`;
- positive `c_scale` with `x0=c*t`;
- non-empty unique patch identifiers;
- finite three-component `beta_match` values;
- directed overlap data `(source,target,A,v)`;
- the exact handoff-integrity relation
  [
  \beta_q=A_{qp}\beta_p-v_{qp};
  ]
- canonical payload SHA-256;
- normalized RF-E8 shift export.

Promotion review eligibility requires the underlying matching packet to be a genuine production input and to pass the handoff contract.

## 5. Same-realization gate

The bundle requires simultaneously

[
oxed{
mathrm{spatial.physical_realization_id}
=
mathrm{matching.physical_realization_id}
}
]

and

[
oxed{
mathrm{spatial.physical_realization_receipt_sha256}
=
mathrm{matching.physical_realization_receipt_sha256}
}.
]

The executable certificate reports four fail-closed blockers:

```text
TIR_GSC1_PRODUCTION_SPATIAL_CAPTURE
TIR_INTERLEAF_PRODUCTION_MATCHING_CAPTURE
SAME_PHYSICAL_REALIZATION_ID
SAME_PHYSICAL_REALIZATION_RECEIPT
```

The bundle is promotion-review eligible only when none of these blockers remains.

## 6. PNCS / synthetic identity firewall

Identifiers beginning with

`pncs:realization36:`

are explicitly rejected as physical-realization identifiers.

Phase36/PNCS/Terminal36D runtime states may be used for candidate audit, diagnostics or synthetic validation, but they cannot substitute for a source-declared physical-realization receipt.

## 7. Evidence and canon boundary

The deterministic evidence wrapper is

`tir_production_realization_evidence_v0_2.py`.

The deterministic bundle-receipt wrapper is

`tir_production_realization_receipt_v0_2.py`.

Both retain

`physical_production_claim=false`

and the bundle certificate retains

`canon_allowed=false`.

Therefore an executable PASS of the assembler is not a physical-production claim.

## 8. Current production state

Repository audit on 2026-09-19 found no production instance of either v0.2 capture schema and no production bundle instance on `main`.

Current state:

```text
bundle assembler                         CLOSED / EXECUTABLE
production spatial capture              OPEN INPUT
production inter-leaf matching capture  OPEN INPUT
same-realization ID/receipt gate         DEFINED / NO PRODUCTION INSTANCE
physical production claim               FALSE
canon_allowed                            FALSE
```

## 9. Downstream handoff

The production dependency line is

```text
TIR production spatial capture
 + TIR production matching capture
 + same physical realization ID
 + same physical realization receipt
 -> TIR physical-realization source bundle v0.2
 -> RFC GSC3A clock-transverse matching-flow soldering
 -> RFC GSC4A / RF-E25 production shared-spacetime path
```

RFC remains responsible for its own clock, lapse, coframe, overlap and production-atlas gates.
