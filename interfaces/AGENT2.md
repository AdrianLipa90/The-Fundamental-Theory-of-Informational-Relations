# AGENT2.md

## Local role
AGENT2 maintains cross-reference integrity for the `interfaces/` layer.

## Scope
- ensure every exported object has a live registry reference,
- ensure every exported object has at least one explanatory or derivational backlink,
- ensure constraints explicitly block export of open objects,
- ensure interface files remain downstream-only and do not become hidden theory sources.

## Required local references
Each interface file should be able to trace to:
1. a registry entry,
2. a derivation or whitepaper context,
3. the global index.

## Failure conditions
- exported object with no registry anchor,
- exported object with no explanatory context,
- interface status stronger than registry status.
