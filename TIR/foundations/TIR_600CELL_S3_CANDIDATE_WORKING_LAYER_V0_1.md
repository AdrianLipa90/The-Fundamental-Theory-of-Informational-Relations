# TIR 600-cell / S^3 Candidate Working Layer v0.1

Status: `CANDIDATE / ACTIVE_WORKING_IMPLEMENTATION / PHYSICAL_BINDING_OPEN`

Date: 2026-09-11

## Candidate is a working state

Within TIR, `CANDIDATE` means an implementation/theorem surface is active for execution, validation, integration experiments and dependent candidate work. It does not mean unused, archived or failed.

Canonical status classes for this workstream:

```text
CANONICAL   = promoted and admitted to the canonical contract.
CANDIDATE   = active working implementation with explicit candidate provenance.
QUARANTINED = isolated from ordinary routing except diagnostics.
FAILED      = known failing route; retained only as evidence/diagnostics unless repaired under a new version.
```

Candidate results may feed other candidate-labelled surfaces. They may not silently satisfy a canonical gate.

## Finite S^3 carrier

Let `V_600` be the 120 unit vertices of the regular 600-cell in `S^3 subset R^4`, using the standard coordinate families

- 8 axial vertices `(±1,0,0,0)` and permutations,
- 16 vertices `(±1/2,±1/2,±1/2,±1/2)`,
- 96 even permutations of `(0,±1/2,±phi/2,±1/(2phi))`,

where `phi=(1+sqrt(5))/2`.

Join two vertices when their inner product is `phi/2`. The resulting vertex graph has

```text
vertices = 120
degree = 12
edges = 720
```

and adjacency spectrum with multiplicities

```text
12                         : 1
6 phi                      : 4
4 phi                      : 9
3                          : 16
0                          : 25
-2                         : 36
-3                         : 16
2(1-sqrt(5))               : 9
3(1-sqrt(5))               : 4
```

## Validated low S^3 angular sectors

For hyperspherical harmonics on `S^3`, the degree-ell eigenspace has multiplicity

`d_ell=(ell+1)^2`

and Laplacian eigenvalue

`lambda_ell=ell(ell+2)`.

The first six 600-cell adjacency sectors reproduce the multiplicities exactly:

```text
ell  multiplicity  A_600 eigenvalue  -Delta_S3
0    1             12                0
1    4             6 phi             3
2    9             4 phi             8
3    16            3                 15
4    25            0                 24
5    36            -2                35
```

Therefore TIR admits the following research operator as a working candidate on the explicitly validated subspace:

`L_600^(<=5) = sum_{ell=0}^5 ell(ell+2) Pi_ell`,

where `Pi_ell` is the spectral projector onto the corresponding adjacency eigenspace.

This is a mathematical/angular candidate. It is not by itself a physical atomic-orbital identification.

## Exact quadrature test

The validator enumerates all 1365 coordinate monomials of total degree `<=11` and compares the 120-point average to the normalized `S^3` moment. The observed maximum absolute error is at floating-point floor (`5.55e-17` in the reference execution).

At degree 12 the tested monomial `x_1^12` is no longer exact:

`<x_1^12>_600 - <x_1^12>_S3 = 1/4096`.

Accordingly the current working labels are:

```text
S3_600CELL_L0_L5_EXACT = CANDIDATE_VALIDATED
L6_SPECTRAL_QUADRATURE_HORIZON = CANDIDATE_OBSERVED_BOUNDARY
L7_FINITE_CLOSURE = CANDIDATE_RESEARCH_TARGET
PHYSICAL_ORBITAL_BINDING = OPEN
SOLITON_BINDING = OPEN / MODEL_ONLY
```

The `ell=6 -> ell=7` interpretation is deliberately not promoted by this document beyond the tested quadrature boundary. A separate rank/representation validator is required before `L7_FINITE_CLOSURE` can be promoted even within the candidate layer.

## Executability

Reference validator:

`TIR/validation/tir_600cell_s3_candidate_v0_1.py`

The working executable PhaseNav counterpart is maintained in the PNCS candidate branch as `candidate_600cell_s3_v01.py`. Candidate execution must preserve its status in receipts and fail closed outside the validated `ell<=5` sector.

## Promotion gates

Promotion from `CANDIDATE` requires, at minimum:

1. full repository regression PASS;
2. cross-repository byte/provenance reconciliation with PNCS;
3. explicit representation/rank tests for the proposed `ell=6/7` folding/closure;
4. non-regression against existing PhaseNav behaviour;
5. separate evidence for any physical orbital, soliton, Standard Model or spacetime interpretation.
