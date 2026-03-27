# CIEL Foundations Orchestrator

## Purpose
This file is the human-readable orchestration layer for the canonical foundations repository.

## Active module groups
### Core piko chain
- `DEF-0001..0007`
- `D-0001..0006`
- core interfaces and solvers

### Tau / kernel / White-Thread / action chain
- `DEF-0008` + `D-0007` + `IF-0006`
- `DEF-0009` + `D-0008` + `IF-0007`
- `DEF-0010` + `D-0009` + `IF-0008`
- `DEF-0011` + `D-0010` + `IF-0009`
- `DEF-0012` + `D-0011` + `IF-0010`
- `DEF-0013` + `D-0012` + `IF-0011`
- bundle support: `AUDIT_SCHEMA.yaml`, `SEMANTIC_ACTION_REFERENCE_CARD.md`

## Routing policy
1. Start from `README.md`, `INDEX.md`, or `index.md`.
2. Enter the target object through its registry or interface.
3. Follow the dependency DAG upstream before touching downstream code.
4. Treat bibliography as support for attribution and context, not as automatic epistemic upgrade.

## Immediate open targets
- semantic metric law
- truth potential runtime operator
- reduction threshold operator
- semantic mass / orbital embedding operator
- local time-owning and winding operators
