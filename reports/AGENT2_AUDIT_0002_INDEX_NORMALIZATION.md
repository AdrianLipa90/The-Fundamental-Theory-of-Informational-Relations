# AGENT2 Audit 0002 — Index Normalization

## Scope
This report records the next required normalization step for repository cross-reference topology.

## Confirmed current state
The following canonical navigation files exist on branch `Agent2`:
- `INDEX.md`
- `index.md`
- `whitepapers/index.md`
- `whitepapers/metatime/index.md`
- `derivations/index.md`
- `derivations/metatime/index.md`
- `registries/index.md`
- `interfaces/index.md`
- `axioms/index.md`

The following AGENT2 scope files exist:
- `AGENT2.md`
- `whitepapers/AGENT2.md`
- `whitepapers/metatime/AGENT2.md`
- `derivations/AGENT2.md`
- `derivations/metatime/AGENT2.md`
- `registries/AGENT2.md`
- `interfaces/AGENT2.md`
- `axioms/AGENT2.md`

The following AGENT2 cross-reference artifacts exist:
- `reports/AGENT2_AUDIT_0001.md`
- `registries/agent2_scope_map.yaml`
- `registries/repo_holonomy.yaml`

## Finding
The AGENT2 scope files and audit artifacts are canonical but not yet fully exposed from the main navigation spines. They are therefore not orphaned in storage, but they remain underexposed in active navigation.

## Required normalization

### Root-level normalization
`index.md` should link to:
- `INDEX.md`
- `AGENT2.md`
- `reports/AGENT2_AUDIT_0001.md`
- `reports/AGENT2_AUDIT_0002_INDEX_NORMALIZATION.md`
- `registries/agent2_scope_map.yaml`
- `registries/repo_holonomy.yaml`
- `whitepapers/index.md`
- `derivations/index.md`
- `interfaces/index.md`
- `axioms/index.md`

### Layer-level normalization
Each layer index should link its own `AGENT2.md`:
- `whitepapers/index.md` -> `AGENT2.md`
- `derivations/index.md` -> `AGENT2.md`
- `registries/index.md` -> `AGENT2.md`
- `interfaces/index.md` -> `AGENT2.md`
- `axioms/index.md` -> `AGENT2.md`

### Sector-level normalization
Metatime sector indexes should link local scope files:
- `whitepapers/metatime/index.md` -> `AGENT2.md`
- `derivations/metatime/index.md` -> `AGENT2.md`

## Constraint encountered
Current connector behavior reliably supports creation of new files but does not yet expose a stable update path for existing index files through the currently available model-facing operations.

## AGENT2 interpretation
The repository is structurally ahead of its active navigators. The next successful edit operation against existing index files should apply the normalization targets above before further sector expansion.

## Status
Prepared and queued for execution.
