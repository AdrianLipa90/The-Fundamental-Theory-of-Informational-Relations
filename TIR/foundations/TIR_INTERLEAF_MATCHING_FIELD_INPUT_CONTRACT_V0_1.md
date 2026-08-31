# TIR Inter-Leaf Matching-Field Input Contract v0.1

Status: `SOURCE_INPUT_CONTRACT_DEFINED / GSC3A_HANDOFF_INTEGRITY_GATE / RFE8_X0_SCALE_EXPORT / PRODUCTION_MATCHING_FIELD_OPEN`

Date: 2026-08-31

## 1. Purpose

The TIR spatial-temporal closure interface exports an inter-leaf identification field `beta_match`. RFC GSC3A derives the exact shared-clock matching-field law and RFC GSC3B binds the same matching direction to RF-E8/RF-E9 ADM kinematics.

This contract defines the source-owned machine-readable TIR packet consumed by those RFC gates. It stores actual inter-leaf matching data, provenance, temporal-coordinate convention and an integrity digest.

The theorem authority remains split by repository role:

```text
TIR  -> source matching-field data and provenance
RFC  -> GSC3A overlap/soldering theorem and GSC3B ADM crosslink
FPDG -> noncanonical/canonical dependency federation according to promotion state
```

## 2. Input schema

A dataset has schema

`TIR_INTERLEAF_MATCHING_FIELD_INPUT_V0_1`

and contains:

- non-empty `dataset_id`;
- boolean `production`;
- source provenance `source` and `source_commit_or_digest`;
- temporal-coordinate convention `t` or `x0`;
- positive conversion scale `c_scale` with declared binding `x0=c*t`;
- a non-empty list of patches with unique `patch_id` and three-component `beta_match`;
- directed overlap data `(source,target,A,v)` with `A` a finite `3x3` spatial Jacobian and `v` a finite three-vector temporal drift;
- `payload_sha256` over the canonical coordinate, patch and overlap payload.

## 3. GSC3A handoff integrity

For every declared overlap

\[
x_q=f_{qp}(t,x_p),
\qquad
A_{qp}=D_xf_{qp},
\qquad
v_{qp}=\partial_t f_{qp},
\]

RFC GSC3A proves the matching-field compatibility relation

\[
\boxed{\beta_q=A_{qp}\beta_p-v_{qp}.}
\]

The TIR input contract mirrors this equation only as a handoff-integrity check. A packet that violates the relation is rejected before RFC consumption.

The theorem status and physical interpretation of the relation remain owned by RFC GSC3A.

## 4. RF-E8 temporal-coordinate export

RF-E8 fixes

\[
\boxed{x^0=ct}
\]

and consumes the dimensionless shift `b_(0)^i` in

\[
\vartheta^a=e^a{}_i(dx^i+b_{(0)}^i dx^0).
\]

For a TIR packet expressed in coordinate time `t`, the exact conversion is

\[
\boxed{b_{(0)}^i=\frac{\beta_{(t)}^i}{c}}
\]

and

\[
\boxed{v_{(0)}^i=\frac{v_{(t)}^i}{c}}.
\]

For an input packet already expressed in `x0`, the conversion factor is one.

The validator emits a normalized handoff packet

`TIR_TO_RFC_RFE8_SHIFT_HANDOFF_V0_1`

with `coordinate=x0`.

## 5. Digest and provenance gate

The canonical hash covers:

```text
temporal coordinate kind
c_scale
sorted patch IDs + beta_match vectors
sorted directed overlaps + A + v
```

The provenance fields remain outside the mathematical payload hash and separately identify the source artifact or commit/digest that produced the packet.

A digest mismatch is a hard integrity failure.

## 6. Production semantics

The reference controls are frozen with

`production=false`.

They validate only the contract implementation and conversion rules.

A source-owned physical dataset may set

`production=true`

only when its patch values and overlaps are obtained from the admitted TIR inter-leaf realization and carry the corresponding provenance.

For a structurally valid production packet the contract returns

`promotion_eligible=true`.

Downstream RFC promotion still requires GSC3A/GSC3B and RF-E25 to consume the same realization. Therefore TIR eligibility is a source handoff status rather than a standalone spacetime promotion.

## 7. Falsification rules

The contract fails closed on:

1. malformed or duplicated patch identifiers;
2. non-finite matching vectors, Jacobians or temporal drifts;
3. an overlap referencing an unknown patch;
4. duplicate directed overlaps;
5. unsupported temporal-coordinate convention;
6. non-positive `c_scale`;
7. a matching-field handoff residual above tolerance;
8. missing provenance;
9. canonical payload digest mismatch.

## 8. Dependency result

```text
TIR spatial-temporal interface beta_match
 + source-owned inter-leaf patch data
 -> TIR input/provenance/digest contract
 -> normalized x0 shift packet
 -> RFC GSC3A matching-field soldering
 -> RFC GSC3B RF-E8/RF-E9 kinematic crosslink
 -> RFC RF-E25 production shared spacetime atlas
```

The current source-owned production matching-field dataset remains an open input.

## 9. Claim ledger

| Statement | Status |
|---|---|
| input schema and payload digest | `EXACT EXECUTABLE CONTRACT` |
| `beta_q=A beta_p-v` handoff check | `MIRROR OF RFC GSC3A EXACT THEOREM` |
| `b_x0=beta_t/c` | `EXACT COORDINATE SCALE` |
| `v_x0=v_t/c` | `EXACT COORDINATE SCALE` |
| normalized RF-E8 packet export | `EXACT EXECUTABLE HANDOFF` |
| reference control | `REFERENCE VALIDATION` |
| production TIR inter-leaf matching dataset | `OPEN INPUT` |

## 10. Validation authority

Implementation:

`TIR/foundations/validation/tir_interleaf_matching_field_input_contract_v0_1.py`

Hosted workflow:

`.github/workflows/tir-interleaf-matching-field-input-contract.yml`

Static receipt:

`TIR/foundations/validation/TIR_INTERLEAF_MATCHING_FIELD_INPUT_CONTRACT_V0_1.json`

Verdict target:

`PASS_TIR_INTERLEAF_MATCHING_FIELD_INPUT_CONTRACT_WITH_PRODUCTION_INPUT_OPEN`.
