# Theory of Informational Relations Monograph — historical v12 migration ledger

**Historical snapshot:** 30 August 2026  
**Former working branch:** `feat/tir-monograph-v12-structural-skeleton`  
**Snapshot baseline:** `main@3f5a08ef04ec53c1a155263d23e8b10a96404370`  
**Promotion state:** `COMPLETED` — validated head `51ec12b5a00201296c8872cadde06bde03cf95d5` was integrated into `main` through PR #111

This file is retained as the historical v12 migration ledger. It is not the current branch-status surface; canonical public status follows `main`.

## Publication architecture

The v12 master is

`TIR/monograph/tir_monograph_v12.tex`.

The v11 master and its chapter/appendix tree remain historical provenance. Version 12 reorganizes publication order around the current dependency graph:

```text
primitive informational relations
-> emergent geometry
-> information / phase / flavour
-> particle and gauge sectors
-> extensions / tests / completion frontier
```

The structural skeleton compiles as a 21-chapter, five-part monograph plus four appendix groups.

## Canonical κ status

The canonical parent surface is

`TIR/foundations/TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md`.

It derives

\[
V_F\cong\mathbb C^3,
\qquad
\dim\mathfrak{su}(3)_F=8,
\qquad
N_{\rm mix}=3\times8=24,
\]

\[
\Delta\phi_{1/2}=\pi,
\qquad
\Phi_{\rm mix}=24\pi,
\qquad
H_2(1/2)=\ln2,
\]

hence

\[
\boxed{\kappa=\frac{\ln2}{24\pi}}.
\]

Publication ownership of the full derivation belongs to v12 Chapter 9. Other v12 occurrences are cross-references or downstream consequences. The structural validator is

`TIR/validation/tir_kappa_flavour_mixing_normalization_v0_1.py`.

The phase-rate consequence remains

\[
\boxed{
\Gamma_{\mathcal I}
=\kappa\omega
=\frac{\ln2}{12}f
},
\qquad
\omega=2\pi f,
\]

with operational measurement tracked as a separate `OPEN` gate.

## Completed v12 migration surfaces

### Chapters 8–10 — flavour carrier, κ, discrete labels

- three-flavour carrier is established before κ;
- κ has one publication owner;
- \(L_3\) uses only the finite orbit \(3\to10\to5\to16\to8\to4\to2\to1\);
- the quark-prime assignment has an exhaustive \(6!=720\) permutation audit;
- arithmetic constraints leave two assignments related by \(b\leftrightarrow t\); the typed monotone flavour-order rule selects the canonical assignment.

### Chapter 11 — coefficient forcing

The role/sign layer is validator-backed:

- role-slot bijection: `PASS`;
- identity is the unique role-preserving slot permutation;
- gradient orientation is scale-independent for positive source gain;
- consensus sign is unique when active source orientations agree.

The active frontier is extraction of \(|h|,|a|,|b|,|c|\) from four typed integer invariants.

### Chapter 12 — charged leptons and neutrinos

Charged-lepton formulas remain sector provenance while their current empirical verdicts are owned by Chapter 19.

A v12 diagnostic audit found a legacy neutrino formula/value mismatch: the printed absolute masses follow the reconstruction \(S_1=S_{\rm bare}+dS\), whereas the legacy text prints \(S_1=S_{\rm bare}+\kappa dS\). The legacy equation is therefore quarantined pending derivational repair.

### Chapter 13 — CKM/PMNS

The migration preserves the common three-flavour carrier and separates formula provenance from empirical verdicts. The PMNS reactor-angle tension is retained. The historical CKM magnitude-product \(J\) check is retained as a diagnostic proxy with its residual visible.

### Chapter 19 — Unified Evidence Matrix

Chapter 19 is the single v12 owner of current observable verdicts. It normalizes PDG-2026 V2, retained physical failures, and v12 migration diagnostics into

`(Claim Class, Timing, Verdict)`.

Consistency validator:

`TIR/validation/tir_v12_evidence_matrix_consistency_v0_1.py`

Receipt:

`TIR/validation/TIR_V12_EVIDENCE_MATRIX_CONSISTENCY_V0_1.json`

Current local receipt status: `PASS`, 30 typed rows.

## GREMLIN-assisted audit

GREMLIN is used as a constrained candidate/audit layer:

```text
OWL      provenance / evidence
SPIDER   dependency graph / relation mapping
MOLE     local derivation checks
HOUND    contradictions / counterexamples
ANT      exhaustive finite search
MANTIS   redundancy / duplicate ownership
BELZEBUB adversarial synthesis
```

Candidate promotion remains theorem/validator/evidence gated.

Findings already incorporated into v12 include:

- duplicate κ ownership;
- global-Collatz overreach around the finite \(L_3\) calculation;
- two-fold prime-label ambiguity before the typed ordering rule;
- charged-lepton current-table drift;
- neutrino formula/value mismatch;
- CKM historical proxy residual;
- stale κ provenance in live-facing ledgers;
- a cosmological arithmetic mismatch now routed to Chapter 18 audit.

## Active migration frontier

1. Chapter 14 — baryon/meson consolidation and provenance quarantine cleanup.
2. Chapter 15 — fresh hypercharge/anomaly chirality and sign-convention audit.
3. Chapter 16 — electroweak/Higgs structural-vs-precision separation.
4. Chapter 17 — strong-CP equation plus retained neutron-EDM failure.
5. Chapter 18 — cosmological arithmetic/unit reconstruction.
6. Chapters 20–21 — prospective programme and formal completion frontier.
7. Full GREMLIN MANTIS/HOUND redundancy and contradiction sweep.
8. Exact-head v12 LaTeX build, citation audit and publication preflight.

## Publication gate

A v12 publication candidate is promoted only after the exact feature head passes its structural validators, evidence-matrix audit, citation/reference checks, LaTeX build and PDF-integrity preflight. Historical workflow receipts remain attached to their original commits.
