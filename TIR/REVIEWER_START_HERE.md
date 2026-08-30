# Reviewer Orientation — Theory of Informational Relations v12

## Review scope

The current review branch reorganizes the TIR monograph around its dependency graph:

```text
primitive informational relations
-> emergent geometry
-> information / phase / flavour
-> particle and gauge sectors
-> extensions / evidence / falsification
```

The v11 source tree is preserved as historical provenance. The v12 publication master is

`TIR/monograph/tir_monograph_v12.tex`.

## Canonical structural primitives used by the current monograph

- \(\kappa=\ln2/(24\pi)\): TIR-internal derived structural normalization with explicit flavour-mixing and half-turn parents;
- \((L_3,L_4,L_5)=(7,2,5)\): discrete structural labels with v12 provenance audit;
- \((u,d,s,c,b,t)=(3,5,7,11,13,17)\): typed prime-label assignment with exhaustive permutation audit;
- declared external anchors and conversion inputs tracked independently from internal structural quantities.

The canonical κ surface is

`TIR/foundations/TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md`.

It records

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

The downstream phase-rate identity is

\[
\boxed{
\Gamma_{\mathcal I}=\kappa\omega=\frac{\ln2}{12}f
},
\qquad
\omega=2\pi f.
\]

Its algebraic status and the operational measurement gate are tracked independently.

## Read evidence through three axes

Every promoted v12 result is read as

`(Claim Class, Timing, Verdict)`.

Claim Class:

- `A`: established mathematical identity or external experimental result;
- `B`: TIR structural law, model identification, or internally derived structural quantity;
- `C`: retrospective phenomenological assignment;
- `D`: diagnostic result, retained failure, falsification witness, or restricted no-go theorem;
- `E`: prospectively frozen prediction;
- `F`: external anchor, measured scale, convention, or conversion input.

Timing:

`RETROSPECTIVE / PROSPECTIVE / EXTERNAL / --`

Verdict:

`PASS / COMPATIBLE / TENSION / FAIL / OPEN / QUARANTINED`

The canonical vocabulary is maintained in

`TIR/monograph/v12/STATUS_TAXONOMY.md`.

## Current evidence owner

The single v12 owner of current observable verdicts is

`TIR/monograph/v12/chapters/ch19_unified_evidence_matrix.tex`.

Sector chapters own equations and derivation provenance. Historical Ch.30, Ch.32 and earlier sector tables remain versioned evidence snapshots.

The frozen PDG-2026 comparison surface is

`TIR/validation/pdg2026/TIR_PDG2026_VALIDATION_MATRIX_V2.md`.

## High-value current review targets

1. **κ parent chain.** Verify the three-flavour carrier, eight-dimensional mixing algebra, 24-channel incidence count, half-turn phase and binary-information numerator independently.
2. **Discrete labels.** Verify the finite Collatz orbit used for \(L_3\) and the exhaustive 720-permutation prime-label audit.
3. **Coefficient forcing.** Verify role-slot identity, sign/orientation forcing, and the still-active four typed magnitude-extraction gates.
4. **Neutrino absolute-action diagnostic.** Inspect the v12 formula/value reconstruction receipt for legacy Ch.17.
5. **Flavour mixing.** Inspect the preserved PMNS reactor-angle tension and the historical CKM \(J\)-proxy residual.
6. **Hadronic provenance.** Separate baryon retrospective refinement from candidate compatibility and verify meson formula arithmetic before promotion.
7. **Gauge/anomaly algebra.** Audit chirality and sign conventions before assigning a v12 formal verdict.
8. **Electroweak precision.** Preserve renormalization scheme/scale dependence and the frozen precision failures in Chapter 19.
9. **Strong-CP gate.** Retain the neutron-EDM physical `FAIL` attached to its frozen conversion map.
10. **Cosmology.** Re-evaluate the legacy power and unit conversion before restoring an empirical compatibility verdict.
11. **Prospective evidence.** Confirm formula hashes, observables, decision rules and no-refit contracts before unblinding.

## GREMLIN-assisted review discipline

GREMLIN is used as a constrained candidate/audit layer:

```text
OWL    -> provenance and evidence
SPIDER -> dependency graph / relation mapping
MOLE   -> local derivation checks
HOUND  -> contradictions and counterexamples
ANT    -> exhaustive finite search
MANTIS -> redundancy and duplicate ownership
BELZEBUB -> adversarial synthesis of surviving candidates
```

GREMLIN outputs enter the repository as candidates or diagnostics. Canonical promotion remains theorem/validator/evidence gated.

## Quick reproducibility checks

```text
python3 TIR/validation/tir_kappa_flavour_mixing_normalization_v0_1.py
python3 TIR/validation/kappa_phase_rate_identity_v11_1.py
python3 TIR/validation/tir_coefficient_role_orientation_forcing_v0_1.py
python3 TIR/validation/tir_v12_evidence_matrix_consistency_v0_1.py
```

The v11 historical source contract remains available through

```text
python3 TIR/validation/review_source_contract_v11_1.py
```

## Publication boundary

Publication promotion requires exact-head validation of the v12 master, its claim/status receipts, citations, references and PDF integrity. Workflow evidence is attached to the exact commit that produced it.
