# TIR Monograph v12 — dependency-ordered content migration

Status: `CONTENT_MIGRATION / PROVENANCE_FIRST / VALIDATION_ACTIVE`

Baseline: `main@3f5a08ef04ec53c1a155263d23e8b10a96404370`

Working branch: `feat/tir-monograph-v12-structural-skeleton`

## Purpose

Version 12 reorganizes the long TIR monograph around the current dependency graph:

`primitive informational relations -> emergent geometry -> information/phase/flavour -> particle and gauge sectors -> extensions and tests`.

The v11 tree remains historical provenance while v12 owns the current dependency-ordered publication surface.

## Current migration state

All twenty-one v12 theory/evidence chapters now contain migrated substantive content. The migration has also introduced deterministic validators for newly reconciled theorem surfaces and has separated canonical formula ownership from publication verdict ownership.

The current foundational spine is

```text
0
-> POINT
-> FIRST DISTINCTION
-> {N,S}
-> 1/2
-> ln2
-> C^2
-> Herm_0(2) ~= R^3
-> Euclidean relational metric
-> regular tetrahedral Gram class
-> W_ij transport
-> SE(3) affine lift
-> discrete solder/torsion source
```

The flavour/information spine continues through

```text
C^3
-> SU(3)_F
-> dim su(3)=8
-> 3*8=24 mixing channels
-> half-turn phase pi
-> Phi_mix=24*pi
-> kappa=ln2/(24*pi)
```

The canonical kappa source is

`TIR/foundations/TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md`.

## Publication ownership

Version 12 uses three independent status axes documented in `STATUS_TAXONOMY.md`:

`(Claim Class, Timing, Verdict)`.

Sector chapters own formulas, derivations and provenance. Chapter 19, `Unified Evidence Matrix`, owns current observable-level publication verdicts.

## Geometry status

Chapters 4–7 now source-bind the local spatial construction through the affine two-level state carrier. The canonical endpoint relation is

`E_xy = 2(rho_y-rho_x) in Herm_0(2)`.

The Hilbert–Schmidt metric supplies the Euclidean quadratic form, full local `SO(3)` isotropy stabilizes rank three, and minimal finite full isotropy forces the regular tetrahedral Gram matrix. The spatial and qubit-SIC tetrahedra are closed at the orthogonal congruence-class level.

The transport chain then separates pure atlas cocycles from path-dependent connection transport and gives the exact discrete identity

`vec(T_xyz) = t_C = -c_xyz`

on the rotationally consistent triangular sector. The next geometry theorem is controlled refinement to Cartan torsion and curvature.

## Evidence and falsification state

The v12 evidence surface preserves compatible results, tensions, failures and quarantines as independent typed rows. Current retained examples include:

- CKM retrospective compatibility in the frozen PDG-2026 matrix;
- PMNS reactor-angle tension;
- charged-lepton precision failures;
- meson formula quarantines/failures;
- electroweak precision failures plus the common `R_EW` closure gate;
- the retained neutron-EDM physical failure;
- exact Standard Model local anomaly cancellations and the Witten doublet count;
- cosmological arithmetic/conversion quarantine pending the unit-complete scale bridge.

## Prospective programme

The active prospective contract is the frozen v10.7 three-candidate family with the orthogonal observables

`y_c/y_mu` and `y_c/y_t`.

The family, observable assignment and no-refit rule are frozen before their assigned qualifying future likelihoods are used for model selection.

## Completion frontier

Chapter 21 represents the remaining work as a directed acyclic graph rather than a flat list. Its current machine-readable receipt reports 23 resolved nodes: eight closed roots and fifteen open gates, with zero missing parents and zero cycles.

Principal downstream gates include:

1. discrete-to-continuum Cartan refinement;
2. zero-torsion spatial sector and TIR–IDT ADM join;
3. Einstein constraint/evolution closure;
4. coefficient magnitude forcing;
5. continuum gauge normalization and running;
6. common electroweak scheme/scale transport;
7. Higgs scalar-action binding;
8. holonomic strong-CP source theorem;
9. meson absolute-action baseline;
10. neutrino absolute-action repair;
11. cosmological dimensionful scale binding;
12. native Li/Weil positivity closure.

## Build surface

The v12 master is

`TIR/monograph/tir_monograph_v12.tex`.

The v11 master remains

`TIR/monograph/metatime_monograph.tex`.

The final promotion pass consists of source-contract validation, LaTeX compilation, citation/reference checks, PDF preflight and an exact-head workflow receipt. `main` remains unchanged by this branch until an explicit promotion decision.
