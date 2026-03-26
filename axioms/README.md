# Axioms

This folder stores the frozen primitive commitments of the repository.

## Role
Axioms are the highest-order canonical objects in this repository.
They license downstream definitions, derivations, implementations, and tests.
Nothing downstream may silently override them.

## Required maintenance rules
- Keep all axiom IDs stable once published.
- Record legacy IDs when namespace migration occurs.
- Do not add explanatory interpretation as if it were an axiom.
- When a new axiom is proposed, register it before using it anywhere else.
- Every downstream reference must resolve to a canonical axiom ID.

## Canonical namespace policy
The preferred namespace for this repository is:
- `AX-FND-0001`
- `AX-FND-0002`
- ...

Legacy aliases may exist during migration, but only as compatibility markers.

## Required contents
- `registry.yaml` as the canonical axiom registry
- optional mapping/bridge files for namespace normalization
- one file per formal axiom when the folder is fully populated

## Completion standard
This folder is complete only when:
1. every axiom has a stable canonical ID,
2. all downstream layers reference the same namespace,
3. no undocumented legacy alias remains active.
