# Foundations Definitions

This folder stores canonical first-order definition files for the foundational ontology.

## Role
Objects here sit between axioms and derivations.
They must define what the object is, what it depends on, and where it is consumed downstream.

## Required file content
Each object file should contain:
- canonical ID
- role statement
- minimal formal definition
- upstream axioms
- downstream derivations/modules/tests
- epistemic status
- scope guard

## Maintenance rules
- Do not bypass this folder by introducing hidden theory objects in code.
- Do not declare imported sector objects here as native primitives unless re-derived.
- Keep file names aligned with `definitions/registry.yaml` paths.
- Every file here must remain short, structural, and canonical.

## Current priority objects
- relation
- potential
- boundary
- locality
- attractor
