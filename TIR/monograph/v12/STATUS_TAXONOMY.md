# TIR Monograph v12 — canonical status taxonomy

Status: `V12_PUBLICATION_TAXONOMY`

The publication status of a claim or observable is the ordered triple

`(Claim Class, Timing, Verdict)`.

The three axes are independent. A numerical result can therefore carry its provenance, data timing and empirical/formal verdict without overloading one label.

## Axis 1 — Claim Class

| Class | Meaning |
|---|---|
| `A` | Established mathematical identity or external experimental result supported by standard sources. |
| `B` | TIR structural law, model identification, or internally derived structural quantity with explicit upstream TIR dependencies. |
| `C` | Retrospective phenomenological assignment developed with access to some or all target values. |
| `D` | Diagnostic result, retained failure, falsification witness, or restricted no-go theorem. |
| `E` | Prospectively frozen prediction with a declared observable and no-refit rule. |
| `F` | External anchor, measured scale, convention, or conversion input supplied to a construction. |

This axis is inherited from the v11 publication frontmatter and `TIR/CLAIM_HIERARCHY.md`.

## Axis 2 — Timing

Allowed values:

- `RETROSPECTIVE`
- `PROSPECTIVE`
- `EXTERNAL`
- `--` when timing is not an applicable dimension of the claim.

The dash is an empty value for this axis, not an additional claim class.

## Axis 3 — Verdict

| Verdict | Meaning |
|---|---|
| `PASS` | The declared theorem, validator or empirical gate is satisfied at the cited source/commit and under the stated observable definition. |
| `COMPATIBLE` | Empirical comparison is compatible at the declared precision, but the row is not a theorem-level PASS. |
| `TENSION` | A visible discrepancy remains and is retained as part of the evidence record. |
| `FAIL` | The declared gate is not satisfied under its frozen definition. |
| `OPEN` | The derivation, migration, empirical gate or theorem is still unresolved. |
| `QUARANTINED` | The formula or claim is isolated from promotion pending a specified repair or provenance closure. |

## Legacy normalization map

### `TIR/STRUCTURAL_CHOICES.md`

| Legacy type | v12 Claim Class | Additional provenance |
|---|---|---|
| `A` | `A` | established source |
| `D_TIR` | `B` | internal derivation parents required |
| `P` | `B` | structural-law provenance required |
| `S` | `B` | discrete selection alternatives must be recorded |
| `R` | `C` | `Timing=RETROSPECTIVE` |
| `F` | `F` | `Timing=EXTERNAL` |
| `E` | `E` | `Timing=PROSPECTIVE` |
| `D` | `D` | diagnostic/failure/no-go provenance required |

### v11 Chapter 30 status vocabulary

| Legacy term | v12 normalization |
|---|---|
| `structural` | `Class=B`, timing `--`, verdict from theorem/validation state |
| `postdiction` | `Class=C`, `Timing=RETROSPECTIVE`, verdict `COMPATIBLE`, `TENSION` or `FAIL` |
| `tension` | class from provenance, `Timing=RETROSPECTIVE`, `Verdict=TENSION` |
| `precision fail` | `Class=D`, `Timing=RETROSPECTIVE`, `Verdict=FAIL` |
| `formula quarantined` | `Class=D`, timing from provenance, `Verdict=QUARANTINED` |
| `prospective` | `Class=E`, `Timing=PROSPECTIVE`, verdict from frozen gate |

## Publication invariant

Every promoted v12 result must name all three axes and must preserve the source path or external citation that determines them. A PASS is scoped to the exact theorem surface, observable definition and tested revision.
