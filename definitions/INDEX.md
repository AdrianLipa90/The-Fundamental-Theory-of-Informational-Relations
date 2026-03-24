# Definitions Index

This index organizes the canonical definitions layer.

## Role
Definitions are the bridge between axioms and derivations.
No executable theory object should bypass this layer.

## What belongs here
- canonical object names
- symbols
- formal role statements
- dependency links to axioms
- downstream targets in derivations/code/tests
- epistemic status

## Current state
`definitions/registry.yaml` exists but is still mostly empty.
This means the structural layer exists, but canonical object indexing is not yet complete.

## Required core objects to index first
- relation
- information
- potential
- state
- boundary
- locality
- identity
- attractor
- closure
- holonomy
- white thread
- spectrum

## Required outputs of this layer
For each object, the repository must ultimately expose:
1. ontology / role
2. formal definition
3. dependency path
4. executable implementation target
5. tests / falsification target
6. status

## Immediate next step
Populate `definitions/registry.yaml` and add per-object definition files before expanding derivation/code complexity.
