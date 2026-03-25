# Foundational Work Pattern

## Purpose
Define the canonical artifact structure for any theoretical module.

## Required artifact set (per module)
Each module must produce a linked set of artifacts:

1. THEORY
   - file: `T-xxxx-*.md`
   - content: conceptual structure, definitions usage, high-level explanation

2. DERIVATION
   - file: `D-xxxx-*.md`
   - content: strict formal derivation, equations, dependency path

3. CODE NOTEBOOK
   - file: `NB-xxxx-*.ipynb` or `.md`
   - content: executable or pseudo-executable realization

4. SIMULATION
   - directory: `simulations/code/xxxx/`
   - content: runnable scripts

5. RESULTS
   - directory: `simulations/results/xxxx/`
   - content: plots, outputs, artifacts

## Cross-reference requirement
Every artifact must link to:
- definitions (DEF-*)
- derivations (D-*)
- code modules (`src/*`)
- simulations and results

## Minimal closure condition
A module is not complete unless:
- theory exists
- derivation exists
- at least one executable path exists
- results are recorded

## Anti-patterns
- single markdown "idea" without derivation
- derivation without link to definitions
- code without reference to theory
- results without reproducible path
