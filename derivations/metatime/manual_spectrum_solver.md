# Manual Spectrum Solver

## Scope
This document records the manually reproducible solving path imported from the uploaded January 2026 Metatime PDFs.

## 1. Emergent eigenvalues
The imported material uses family-wise seeded dynamics to define discrete spectrum values for:
- charged leptons,
- light quarks,
- heavy quarks,
- neutrinos.

The solver boundary in this repository is:
1. family seed choice,
2. discrete orbit rule,
3. selected eigenvalue table,
4. downstream mass formula assignment.

## 2. Topological fingerprint
Each particle is represented by a fingerprint of the form:
- eigenvalue,
- Berry phase,
- intention correction or unit correction,
- optional pairwise coherence role.

### Minimal imported facts
- all fermions are assigned a fermionic Berry phase in the toy `S^2` picture,
- the intention operator is treated as a universal small coupling,
- the light-quark sector requires nontrivial correction factors,
- neutrinos require pairwise white-thread factors.

## 3. Charged-lepton closure
Imported charged-lepton closure uses a Vandermonde / polynomial fit over the selected eigenvalues.

### Status boundary
- reproduces the charged-lepton anchors exactly,
- is fitted by construction,
- remains useful as a sector-local closure relation,
- is not yet promoted here to a first-principles derivation.

## 4. Light-quark closure
Imported light-quark masses use a base power law multiplied by intention corrections.

### Status boundary
- base scaling is structural,
- correction coefficients are effectively fitted to match the physical masses,
- the `d`-quark suppression is interpreted topologically but not yet derived from explicit geometry in this repository.

## 5. Heavy-quark closure
Imported heavy-quark masses use a two-parameter power law.

### Status boundary
- compact and predictive relative to the number of targets,
- still based on fitted constants,
- exportable only as a calibrated sector map, not as a closed derivation.

## 6. Neutrino sector
The imported neutrino solver path contains:
- a base model from eigenvalues and exponent choice,
- a calibration scale fixed by one observed splitting,
- pairwise white-thread factors required to recover the other splitting(s).

### Status boundary
- spectrum ordering and calibration machinery are defined,
- pairwise coherence remains open at first-principles level,
- any imported `F_ij` used for closure must be tagged fitted unless geometry later derives it.

## 7. CP and cosmology-facing derived quantities
The imported derivation set also supplies:
- a DUNE-target CP resonance window near `0.63 GeV`,
- a dynamic `Λ_0(z)` concept,
- a staged falsification programme.

## 8. Immediate next derivation tasks
1. derive `W_ij` on explicit geometry,
2. derive `F_ij` instead of fitting them,
3. fold QCD running into the light-quark sector,
4. separate truly derived constants from calibrated constants in code.

## Cross-references
- [Derivations index](index.md)
- [Metatime framework summary](../../whitepapers/metatime/metatime_framework_summary.md)
- [Metatime epistemic status registry](../../registries/metatime_status.yaml)
- [Metatime export interface](../../interfaces/metatime_exports.yaml)
