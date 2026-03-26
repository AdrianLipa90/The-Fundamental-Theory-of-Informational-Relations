# AGENT2.md

## Local role
AGENT2 maintains cross-reference integrity for the `reports/` layer.

## Scope
- ensure reports are indexed,
- ensure reports point back to registries or canonical indexes when they describe pending work,
- ensure reports do not become shadow sources of truth,
- ensure report findings are translatable into later canonical edits.

## Required local references
A report should link, when relevant, to:
1. the root AGENT2 scope,
2. the relevant registry queue,
3. the relevant canonical index or sector index it discusses.

## Failure conditions
- report exists with no index exposure,
- report contains normative structure changes with no registry trail,
- report silently supersedes canonical indexes.
