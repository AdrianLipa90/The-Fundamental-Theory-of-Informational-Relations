# TIR Foundation Proof Source Registry v0.1

Status: `SOURCE_FIRST_PROVENANCE_REGISTRY`

Purpose: prevent the failure mode “not present in the current summary file -> treated as absent from TIR.” Every foundational claim is first searched across active foundations, integration surfaces, validators, monograph sources and archived formal/debt modules.

| Claim / edge | Canonical source or strongest existing source | Source status | Active TIR status |
|---|---|---|---|
| absolute nothing cannot be realized as existing | `TIR_CANONICAL_DERIVATION_SPINE_V0_1.md` | definitional contradiction | CANONICAL |
| minimum object is a point | historical A1 + canonical singleton/0D minimality proof in spine | legacy statement, now derivationally typed | CANONICAL |
| minimum nontrivial structure is relation | zero-axiom relational foundation + canonical spine | TIR structural typing | CANONICAL |
| nontrivial relation -> two orientation roles | first-distinction theorem + canonical spine | exact conditional on non-self-collapse | CANONICAL |
| exchange invariance -> 1/2 | `TIR_FIRST_DISTINCTION_THEOREM_V0_2.md` | exact | CANONICAL |
| 1/2 -> ln2 | first-distinction theorem / half-seam | exact Shannon identity | CANONICAL |
| relational phase coordinate -> U(1) ~= S1 | `TIR_RELATIONAL_PHASE_LAGRANGIAN_CORE_V0_1.md` | standard phase quotient + exact gauge-covariant Lagrangian identity | CANONICAL |
| 1/2 -> coherent S1 half-fibre | `TIR_HALF_SEAM_PHASE_FIBER_V0_1.md` | exact downstream crosscheck on two-state carrier | CANONICAL CROSSCHECK |
| relational phase Lagrangian with chi in U(1) | archived Hilbert--Kähler phase Hamiltonian | formal source, algebra exact once carrier admitted | PROMOTED SOURCE |
| CP1 ~= S2 and FS metric | `TIR_LAGRANGIAN_BLOCH_SELECTION_V0_1.md` + archived Hilbert--Kähler provenance + v12 ch03 | standard projective/Kähler geometry | CANONICAL |
| Berry curvature and Chern number 1 | archived Hilbert--Kähler note | standard geometry | CANONICAL |
| Euler/Berry nontrivial sign -> minimal spin 1/2 | archive module v2.4 | FORMAL_SYMBOLIC_PASS | PROMOTED SOURCE |
| 2pi -> -I, 4pi -> +I | White-Thread spin-lift | exact spin-lift identities | CANONICAL |
| spin 1/2 -> two polar eigenstates | Hilbert--Kähler note / standard Pauli representation | exact representation theory | CANONICAL |
| S1 phase fibre + two polar endpoints -> S2 | `TIR_LAGRANGIAN_BLOCH_SELECTION_V0_1.md` | standard suspension topology + exact Bloch map | CANONICAL |
| Bloch sphere -> Herm_0(2) ~= R3 | v12 ch03/ch04, relational-generator foundation | exact linear algebra | CANONICAL |
| affine relation is state difference up to scale | Space-of-Geometry naturality theorems | exact conditional + one TIR inheritance gate | CANONICAL DOWNSTREAM |
| tetrahedral minimal isotropic frame | TIR minimal tetrahedral-cell theorem | exact conditional | CANONICAL DOWNSTREAM |
| kappa = ln2/(24pi) | flavour-mixing normalization + information-spinor crosswalk | TIR-internal derived normalization on declared carrier | CANONICAL |
| alternative 24pi Collatz/parity/spin closure | archived Step 4 Berry--Euler note | independent historical normalization route; includes explicit lifted-identity postulate | CROSSCHECK ONLY |

## Promotion policy

1. A current-file omission is **not** a theory gap.
2. A candidate gap must first be searched across the full repository tree, including `archive/`.
3. Archived mathematics can be promoted only with its original status preserved.
4. A formal-symbolic PASS is not silently relabelled as empirical validation.
5. A legacy postulate is not silently called a theorem; if TIR can now derive it, the new derivation must be written explicitly.
6. Duplicate mathematical surfaces are linked by provenance rather than rewritten destructively.

## Current foundation reconciliation

The key source-order correction is:

```text
do not use:
  SO(3) -> S2 -> CP1 -> quantum -> SO(3)

use:
  relation -> polar roles {N,S}
  half-seam -> U(1) ~= S1
  S1 + {N,S} -> suspension(S1) ~= S2
  S2 -> CP1 / Fubini-Study / Berry
  Berry hemisphere + Euler sign -> spin 1/2
  spin polar pair == relational polar pair
  SU(2)/{+/-I} ~= SO(3) only downstream
```

This prevents the earlier circularity while reusing mathematics already present in TIR.
