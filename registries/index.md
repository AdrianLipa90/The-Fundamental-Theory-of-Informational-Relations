# Registry Index

Registries store machine-readable truth about object status, export boundaries, and cross-reference topology.

## Root authority registries
- [Global index registry](global_index_registry.yaml)
- [Cross-reference map](cross_reference_map.yaml)

`global_index_registry.yaml` is the canonical machine-readable source of truth for root navigation authority.
`cross_reference_map.yaml` is the sector/object topology map.

## Local contents
- [Global index registry](global_index_registry.yaml)
- [Metatime epistemic status registry](metatime_status.yaml)
- [Cross-reference map](cross_reference_map.yaml)
- [Root governance index](../INDEX.md)
- [Global project index](../index.md)
- [Metatime whitepaper sector index](../whitepapers/metatime/index.md)
- [Metatime derivations index](../derivations/metatime/index.md)
- [Metatime export interface](../interfaces/metatime_exports.yaml)

## Canonical rule
If an object is not present in a registry, it is not canonical enough for downstream export.
