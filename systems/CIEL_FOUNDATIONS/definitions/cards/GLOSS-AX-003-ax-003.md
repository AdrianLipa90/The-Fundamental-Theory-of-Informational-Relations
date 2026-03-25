# AX-003 - Primitive Relational Preference and Ordered Phase Motion

| field | value |
|---|---|
| stable_id | `GLOSS-AX-003` |
| canonical_id | `axiom.ax-003` |
| card_type | `axiom` |
| class | `axiom` |
| subclass | `phase_rotation` |
| status | `axiom` |
| certainty_scope | `internal_frozen_axiom` |
| units | `n/a` |
| value | `nonzero primitive relational preference => ordered phase motion => primitive local rotational dynamics` |

## Description
Once locality exists, any nonzero primitive relational preference breaks exact isotropy and induces ordered phase motion. On the minimal local projective sphere this appears first as rotational phase dynamics around a local axis.

## Formal definition
```text
ε ≠ 0 => Vφ ≠ 0 => primitive local rotational dynamics on CP^1
```

## Tags
`type:axiom`, `domain:foundations`, `status:axiom`, `role:relation`, `role:phase`, `role:rotation`, `role:spin`, `layer:foundations`, `bind:registry`, `math:phase_flow`

## Relational couplings
- `depends_on -> axiom.ax-001`
- `depends_on -> axiom.ax-002`
- `depends_on -> canonical_postulate.p7_symmetry_breaking_rotation`
- `depends_on -> canonical_postulate.p8_attractor_vortex`
- `supports -> state.ordered_phase_motion`
- `supports -> state.local_axis`
- `supports -> dynamics.primitive_rotation`

## Cross references
- `systems/CIEL_FOUNDATIONS/axioms/AX-003-relational-spectrum.md`
- `systems/CIEL_FOUNDATIONS/axioms/AX-001-projective-state.md`
- `systems/CIEL_FOUNDATIONS/axioms/AX-002-closure.md`
- `POSTULATES_CANON_PL_EN.md`

## Source-of-truth anchors
- `systems/CIEL_FOUNDATIONS/axioms/AX-003-relational-spectrum.md`
- `systems/CIEL_FOUNDATIONS/axioms/registry.yaml`

## Notes
This card establishes primitive spin-like dynamics only in the pre-quantized sense of ordered local rotation. Half-integer closure, Berry transport, and spectral identity are later layers.