# Project Charter

## Mission
Establish the first-principles foundation of CIEL as a reproducible research program in which every module, operator, constant, and sector is explicitly defined, derived, implemented, tested, and tracked.

## Deliverables
1. Frozen axiomatic basis
2. Dependency graph from axioms to sectors
3. Generator of constants from arithmetic + geometry + closure
4. Core solver modules with tests
5. Whitepapers and LaTeX sections built from the canonical source tree
6. Artifact registry with hashes and provenance
7. Falsification matrix for every major module

## Non-goals
- patching legacy runtime tarballs
- building UX or agent wrappers
- using interpretation as evidence
- hiding fitted inputs inside derived objects

## Hard constraints
- Each module must declare its assumptions and interface.
- Each constant must have a registry record and its own folder.
- Each simulation must register code, results, environment, constants used, and linked theory nodes.
- Each external formalism or analogy must be recorded in `operational_modes/` as an operational interpretation with limits.

## Success condition
A reader must be able to answer, for any object in the project:
- What is it?
- Where is it defined?
- What does it depend on?
- How is it computed?
- What would falsify it?
- Which artifacts instantiate it?
