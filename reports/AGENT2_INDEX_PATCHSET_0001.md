# AGENT2 Index Patchset 0001

This file contains the intended normalized contents or required insertions for the current repository index files.

## Target 1 — `index.md`

### Required additions
- link to `INDEX.md`
- link to `AGENT2.md`
- link to `reports/AGENT2_AUDIT_0001.md`
- link to `reports/AGENT2_AUDIT_0002_INDEX_NORMALIZATION.md`
- link to `registries/agent2_scope_map.yaml`
- link to `registries/repo_holonomy.yaml`
- link to root indexes for `whitepapers`, `derivations`, `interfaces`, `axioms`

### Proposed normalized content
```md
# Canonical Index

This index is the navigation spine for the Foundations repository.

## Global workflow
Axiom -> Definition -> Derivation -> Implementation -> Test -> Status -> Interpretation

## Root cross-reference governance
- [Repository root map](INDEX.md)
- [AGENT2 scope](AGENT2.md)
- [AGENT2 audit 0001](reports/AGENT2_AUDIT_0001.md)
- [AGENT2 audit 0002](reports/AGENT2_AUDIT_0002_INDEX_NORMALIZATION.md)

## Sector map

### Whitepapers
- [Whitepapers root index](whitepapers/index.md)
- [Metatime sector index](whitepapers/metatime/index.md)
- [Metatime framework summary](whitepapers/metatime/metatime_framework_summary.md)

### Derivations
- [Derivations root index](derivations/index.md)
- [Metatime derivations index](derivations/metatime/index.md)
- [Manual spectrum solver](derivations/metatime/manual_spectrum_solver.md)

### Registries
- [Registry index](registries/index.md)
- [Repository holonomy map](registries/repo_holonomy.yaml)
- [AGENT2 scope map](registries/agent2_scope_map.yaml)
- [Pending index links queue](registries/agent2_pending_index_links.yaml)
- [Metatime epistemic status registry](registries/metatime_status.yaml)
- [Cross-reference map](registries/cross_reference_map.yaml)

### Interfaces
- [Interfaces root index](interfaces/index.md)
- [Metatime export interface](interfaces/metatime_exports.yaml)

### Axioms
- [Axioms root index](axioms/index.md)

## Cross-reference principle
Every imported object must appear in:
1. a local sector index,
2. the global index,
3. at least one registry entry describing epistemic status or export status.
```

## Target 2 — `whitepapers/index.md`

### Required addition
- link to `whitepapers/AGENT2.md`

### Minimal insertion
```md
## Local governance
- [AGENT2 scope](AGENT2.md)
```

## Target 3 — `whitepapers/metatime/index.md`

### Required addition
- link to `whitepapers/metatime/AGENT2.md`

### Minimal insertion
```md
- [AGENT2 local scope](AGENT2.md)
```

## Target 4 — `derivations/index.md`

### Required addition
- link to `derivations/AGENT2.md`

### Minimal insertion
```md
## Local governance
- [AGENT2 scope](AGENT2.md)
```

## Target 5 — `derivations/metatime/index.md`

### Required addition
- link to `derivations/metatime/AGENT2.md`

### Minimal insertion
```md
- [AGENT2 local scope](AGENT2.md)
```

## Target 6 — `registries/index.md`

### Required additions
- link to `registries/AGENT2.md`
- link to `registries/agent2_scope_map.yaml`
- link to `registries/agent2_pending_index_links.yaml`

### Minimal insertion
```md
## Local governance
- [AGENT2 scope](AGENT2.md)
- [AGENT2 scope map](agent2_scope_map.yaml)
- [Pending index links queue](agent2_pending_index_links.yaml)
```

## Target 7 — `interfaces/index.md`

### Required addition
- link to `interfaces/AGENT2.md`

### Minimal insertion
```md
## Local governance
- [AGENT2 scope](AGENT2.md)
```

## Target 8 — `axioms/index.md`

### Required addition
- link to `axioms/AGENT2.md`

### Minimal insertion
```md
## Local governance
- [AGENT2 scope](AGENT2.md)
```

## Status
Prepared on branch `Agent2-refresh` after confirming that the current connector still rejects direct updates to existing files without a supported model-facing SHA update path.
