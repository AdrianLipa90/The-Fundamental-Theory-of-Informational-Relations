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

## Scope
Included now:
- axioms
- state-space definitions
- derivations
- constants registry
- solver modules
- simulations and artifact tracking
- whitepapers and LaTeX sections
- bibliography and cross-reference infrastructure
- operational modes (external formalisms mapped into CIEL operational roles)
- assumptions, decisions, falsification criteria, interfaces, provenance, benchmarks

Excluded for now:
- Omega runtime
- CQCL runtime integration
- memory/agent layers
- UI/persona/prompt infrastructure

## Source of truth
Source of truth is stored in:
- Markdown / TeX for formal and explanatory text
- YAML for registries, interfaces, assumptions, provenance, and cross-reference maps
- Python for executable realization

PDF files are generated artifacts, not source of truth.
# The-Fundamental-Theory-of-Informational-Relations
