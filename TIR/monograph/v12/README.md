# TIR Monograph v12 — structural skeleton

Status: `STRUCTURAL_ONLY / EQUATION_PRESERVING / PROVENANCE_FIRST`

Baseline: `main@3f5a08ef04ec53c1a155263d23e8b10a96404370`

Working branch: `feat/tir-monograph-v12-structural-skeleton`

## Purpose

Version 12 reorganizes the long TIR monograph around the current dependency graph rather than the historical order in which phenomenological sectors were developed.

The narrative spine is:

`primitive informational relations -> emergent geometry -> information/phase/flavour -> particle and gauge sectors -> extensions and tests`.

## First-pass invariants

1. The v11 source tree remains intact and continues to provide historical provenance.
2. This pass changes document architecture, chapter ownership and status semantics only; equation-bearing source material is not rewritten here.
3. Every v12 chapter is a wrapper with an explicit source-integration map.
4. Legacy material is migrated only after its source path and claim provenance are recorded in `MIGRATION_MANIFEST.yaml`.
5. The canonical kappa derivation is owned by Chapter 9 and sourced from `TIR/foundations/TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md`; other occurrences become cross-references during the content-migration pass.
6. The canonical publication status is represented by three independent axes documented in `STATUS_TAXONOMY.md`.
7. `main` is not modified by this branch.

## v12 title

**Theory of Informational Relations**  
**Foundations, Emergent Geometry, and Phenomenological Tests**

`Metatime` remains a named programme/layer inside the wider TIR architecture.

## Build surface

The structural master is:

`TIR/monograph/tir_monograph_v12.tex`

The v11 master remains:

`TIR/monograph/metatime_monograph.tex`

## Next pass after skeleton review

The next pass is mechanical content migration and reconciliation:

1. move equation-bearing material into the declared wrapper chapter;
2. preserve source provenance and labels;
3. replace repeated derivations with canonical cross-references;
4. reconcile legacy status terms into the three-axis taxonomy;
5. compile and run source/claim audits before any publication promotion.
