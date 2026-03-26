# ADR-0001 — Index Authority and Root Navigation

## Status
Accepted on branch `Agent7`.

## Context
The repository currently has two root navigation files:
- `INDEX.md`
- `index.md`

Both are useful, but without an explicit authority split they create parallel-entrypoint risk.

The repository also contains:
- `registries/index.md`
- `registries/cross_reference_map.yaml`
- `docs/agent4/index_registry_seed.yaml`

These provide partial topology and early registry thinking, but do not yet define a canonical, machine-readable root-navigation authority.

## Decision
The repository will use a three-layer index authority model:

1. `INDEX.md`
   - role: human-readable root governance and repository map
   - purpose: explain repository role, canonical workflow, and layer responsibilities

2. `index.md`
   - role: human-readable global navigation spine for currently indexed sectors and imported object entrypoints
   - purpose: expose sector entrypoints and immediate theory-facing navigation

3. `registries/global_index_registry.yaml`
   - role: machine-readable authority layer for root navigation and object-index policy
   - purpose: define root-index roles, status vocabulary, relation vocabulary, and tracked root objects

`registries/cross_reference_map.yaml` remains the sector/object topology map, not the source of truth for root index authority.

## Consequences
- root navigation duplication is converted into an explicit dual-role architecture rather than silent overlap
- future layer indexes should link upward to `INDEX.md` and be representable in `registries/global_index_registry.yaml`
- machine-readable registry authority moves from agent-local notes toward canonical repository placement
- normalization of existing links becomes a follow-up edit, not an ambiguous policy question

## Follow-up tasks
1. update `INDEX.md` to mention `index.md` and `registries/global_index_registry.yaml`
2. update `index.md` to point back to `INDEX.md` and the canonical registry
3. update `registries/index.md` to expose the new registry explicitly
4. extend the registry with more root and layer objects as indexing progresses
