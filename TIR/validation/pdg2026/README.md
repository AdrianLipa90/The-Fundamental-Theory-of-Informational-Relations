# PDG 2026 validation freeze

Status: `PDG2026_VALIDATION_FREEZE_V1`

Base commit: `2b985536210477676c0bb3fbfd338b8edde88832`  
Freeze date: `2026-08-15`  
Branch: `pdg2026-validation-addendum-v1`

## Purpose

This directory records the first validation-aware TIR/Metatime cross-check against the 2026 Review of Particle Physics. It explicitly separates numerical compatibility, precision-level tension/failure, provenance limitations, internal formula failures, and quantities not yet testable.

The audit is **not** a global validation of TIR and is **not** a global falsification of the framework. Failed results are intentionally retained.

## Current headline status

- CKM: strongest current numerical compatibility; postdictive.
- Neutrinos: mixed; solar sector compatible, `sin² theta13` under tension.
- Charged leptons: internally reproducible action arithmetic, but precision-level failure.
- Baryon decuplet: retained as a useful candidate cross-check.
- Baryon octet: retrospective-refinement provenance caveat.
- Pseudoscalar mesons: pion/kaon printed equations fail their own arithmetic and are quarantined.
- Electroweak/Higgs: current printed relations fail precision-level tests or require scheme/running/radiative structure.
- Quark masses: not scoreable until the mass map declares renormalization scheme and scale.

## Freeze rule

A future claim intended as prospective evidence must publish before opening the comparison data:

1. formula/version identifier and source hash;
2. declared external inputs;
3. observables used during construction;
4. frozen numerical prediction;
5. no-retuning rule after unblinding;
6. retained FAIL/TENSION result if the test fails.

## Files

- `TIR_PDG2026_VALIDATION_MATRIX_V1.md` — observable-level validation ledger.
- `../../monograph/chapters/ch32_pdg2026_validation_addendum.tex` — integrated monograph addendum.

Reference: F. Takahashi et al. (Particle Data Group), *Review of Particle Physics*, Int. J. Mod. Phys. A 41, 2630011 (2026), DOI `10.1142/S0217751X26300115`.
