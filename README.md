# CIEL Foundations

CIEL Foundations is a fresh, standalone first-principles project. It is **not** the Omega runtime and it does **not** inherit source-of-truth status from prior tarballs. Its purpose is to derive the minimal ontology, geometry, closure law, coupling structure, constants, and sector maps that Omega may later consume **only through exported constants, operators, and constraints**.

## Primary rule
Every object in the project must have four synchronized representations:
1. ontology / role
2. mathematical definition or derivation
3. executable code
4. epistemic status and tests

No formula without code. No code without formula. No interpretation without an upstream formal object.

## Canonical workflow
Axiom -> Definition -> Derivation -> Implementation -> Test -> Status -> Interpretation

## Quick navigation
### Root entrypoints
- `INDEX.md`
- `index.md`
- `GLOSSARY.md`
- `systems/CIEL_FOUNDATIONS/ORCHESTRATOR.md`
- `registries/global_index_registry.yaml`
- `registries/global_cross_reference_map.yaml`
- `registries/agent_authority_registry.yaml`
- `bibliography/README.md`
- `AUDIT_SCHEMA.yaml`
- `SEMANTIC_ACTION_REFERENCE_CARD.md`
- `schemas/objects_state.schema.yaml`
- `schemas/couplings.schema.yaml`

## Current active foundations modules
### Core piko chain
- `DEF-0001..0007`
- `D-0001..0006`
- `IF-0001`, `IF-0002`, `IF-0004`, `IF-0005`

### Tau / kernel / White-Thread / action stack
- `DEF-0008` — pairwise coupling kernel and tau-from-coupling generator
- `DEF-0009` — phase-aware kernel composition
- `DEF-0010` — White-Thread U(1) primitive
- `DEF-0011` — loose-thread bundle and effective White-Thread
- `DEF-0012` — dynamic path weights from semantic action
- `DEF-0013` — semantic action measurement operators
- `DEF-0014` — Hermitian coupling projection and spectral tau modes
- `DEF-0015` — object-state energy functional
- `DEF-0016` — repository object-state extraction surfaces
- `D-0007`, `D-0008`, `D-0009`, `D-0010`, `D-0011`, `D-0012`, `D-0013`, `D-0014`, `D-0015`
- `IF-0006`, `IF-0007`, `IF-0008`, `IF-0009`, `IF-0010`, `IF-0011`, `IF-0012`, `IF-0013`, `IF-0014`

## Paper layer now includes
- `SEC-0005` tau from coupling
- `SEC-0006` phase-aware kernel composition
- `SEC-0007` White-Thread primitive
- `SEC-0008` effective White-Thread
- `SEC-0009` dynamic path weights
- `SEC-0010` semantic action measurement operators
- `SEC-0011` spectral tau from White-Thread
- `SEC-0012` object-state energy functional
- `SEC-0013` repository object-state extraction
- `APP-0005`..`APP-0011`

## Scope
Included now:
- axioms
- definitions
- derivations
- solver modules
- simulations and artifact tracking
- whitepapers and LaTeX sections
- bibliography and cross-reference infrastructure
- falsification, provenance, interfaces
- audit schema and semantic action reference card
- glossary support
- object-state and coupling schemas
- executable repository extraction surfaces

Excluded for now:
- Omega runtime
- CQCL integration
- persona/UI/prompt layers

## Source of truth
Source of truth is stored in Markdown/TeX, YAML registries/interfaces/provenance, and Python implementation files. PDF files are generated artifacts, not source of truth.

## Global cross-reference principle
Repository-wide navigation should behave like a global organizational coupling graph:
\[
W_{ij}^{Global}: \text{object}_i \leftrightarrow \text{object}_j
\]
implemented through hyperlinks, registries, dependency DAGs, interfaces, tests, simulations, artifacts, provenance, and bibliography.

# The-Fundamental-Theory-of-Informational-Relations
