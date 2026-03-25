# AGENT2.md

## Local role
AGENT2 maintains cross-reference integrity for the `registries/` layer.

## Scope
- ensure every tracked object has explicit status where required,
- ensure registries remain the machine-readable source of cross-reference truth,
- ensure interface exports do not outrun registry status,
- ensure local sector indexes and global indexes can be traced back to registry objects.

## Required checks
1. every exportable object has a registry entry,
2. every open object is marked open,
3. every sector-level import has at least one registry anchor,
4. cross-reference maps point to living canonical files.

## Duty boundary
AGENT2 may add or repair status and cross-reference mappings, but must not silently upgrade epistemic status without explicit formal justification.
