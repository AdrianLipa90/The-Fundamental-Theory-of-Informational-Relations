# Reports Index

This folder stores audit, inspection, and normalization reports generated during repository maintenance.

## Canonical role
Reports are support-layer artifacts. They do not define theory truth, but they may define:
- audit findings,
- pending normalization work,
- migration notes,
- cross-reference repair queues.

## Current reports
- [AGENT2 audit 0001](AGENT2_AUDIT_0001.md)
- [AGENT2 audit 0002 — index normalization](AGENT2_AUDIT_0002_INDEX_NORMALIZATION.md)
- [AGENT2 audit 0003 — topology gaps](AGENT2_AUDIT_0003_TOPOLOGY_GAPS.md)
- [AGENT2 index patchset 0001](AGENT2_INDEX_PATCHSET_0001.md)

## Cross-references
- [Root AGENT2 scope](../AGENT2.md)
- [Registries index](../registries/index.md)
- [AGENT2 scope map](../registries/agent2_scope_map.yaml)
- [Pending index links queue](../registries/agent2_pending_index_links.yaml)
- [Topology gap queue](../registries/agent2_topology_gap_queue.yaml)

## Rule
A report may describe repository state, but it must not silently replace:
- a registry entry,
- a canonical index,
- a formal derivation,
- an interface contract.
