# AGENT2.md

## Local role
AGENT2 maintains cross-reference integrity for `derivations/metatime/`.

## Scope
- keep the manual solver linked to the Metatime whitepaper summary,
- keep derivation-local claims synchronized with `metatime_status.yaml`,
- ensure open pairwise objects like `W_ij` and `F_ij` are not represented as fully derived,
- ensure downstream exports reflect actual epistemic status.

## Required local references
- `index.md`
- `manual_spectrum_solver.md`
- `../../whitepapers/metatime/metatime_framework_summary.md`
- `../../registries/metatime_status.yaml`
- `../../interfaces/metatime_exports.yaml`

## Failure conditions
- derivation text outruns registry status,
- fitted closures are described as first-principles results,
- export interfaces point to objects unsupported by derivation-local context.
