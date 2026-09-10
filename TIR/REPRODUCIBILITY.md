# Reproducibility Guide — v12.1 synchronization

TIR uses separate reproducibility layers for structural derivations, numerical implementations, historical formula snapshots, empirical comparison, and publication assembly. A `PASS` is scoped to the exact layer and revision named by its receipt; no technical PASS silently promotes a physical observable.

## 1. Legacy formula reproducibility

```text
python3 TIR/run_audit.py --json
```

This retains the selected historical implementation subset under schema `TIR_SELECTED_LEGACY_REPRODUCIBILITY_V11_1`. Its result certifies reproducibility of that frozen subset only.

## 2. Canonical κ structural derivation

Canonical theorem surface:

```text
TIR/foundations/TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md
```

Validator:

```text
python3 TIR/validation/tir_kappa_flavour_mixing_normalization_v0_1.py
```

The structural chain is

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

## 3. Platonic L-constant closure

Canonical theorem:

```text
TIR/foundations/TIR_PLATONIC_L_CONSTANTS_CLOSURE_V0_1.md
```

Validator:

```text
python3 TIR/validation/tir_platonic_l_constants_closure_v0_1.py
```

The validator enumerates the five convex Platonic Schläfli pairs, constructs the relevant finite permutation groups and cosets, verifies

\[
[S_4:A_4]=2,
\qquad
[A_5:A_4]=5,
\]

and, conditional on the explicit TIR tetrahedral-root extension rule, obtains

\[
(L_3,L_4,L_5)=(7,2,5).
\]

The finite Collatz orbit of 3 and the twin-prime identities are retained as independent arithmetic crosschecks rather than derivation inputs. This validator has no physical-promotion authority.

## 4. κ phase-rate audit

```text
python3 TIR/validation/kappa_phase_rate_identity_v11_1.py
```

Conditional on the canonical normalization and the declared information-phase relation,

\[
\Gamma_{\mathcal I}=\kappa\omega=\frac{\ln2}{12}f.
\]

Operational calibration of a physical \(\Gamma_{\mathcal I}\) observable remains an open evidence gate.

## 5. Spatial GR theorem stack

The post-v12 geometry validators are run in dependency order:

```text
python3 TIR/foundations/validation/tir_cartan_continuum_refinement_v0_1.py
python3 TIR/foundations/validation/tir_zero_torsion_levi_civita_selection_v0_1.py
python3 TIR/foundations/validation/tir_leading_loop_locality_metric_jet_v0_1.py
python3 TIR/foundations/validation/tir_global_3manifold_smooth_certificate_v0_1.py
python3 TIR/foundations/validation/tir_global_spatial_complex_input_contract_v0_1.py
python3 TIR/foundations/validation/tir_interleaf_matching_field_input_contract_v0_1.py
```

The first three certify conditional/local structural results under their declared assumptions. The A5 certifier certifies a supplied combinatorial carrier. The final two commands certify input contracts and reference controls; they do **not** assert that production global spatial or inter-leaf datasets have been supplied.

## 6. v12 discrete-label and coefficient audits

```text
python3 TIR/validation/tir_v12_discrete_labels_audit_v0_1.py
python3 TIR/validation/tir_coefficient_role_orientation_forcing_v0_1.py
```

The discrete-label audit checks the finite Collatz orbit and all \(6!=720\) quark-prime permutations. The coefficient validator certifies role/orientation structure; extraction of the four coefficient magnitudes remains a separate open theorem.

## 7. v12 flavour-sector diagnostics

Chapter 12 carries a dedicated diagnostic receipt for the legacy neutrino absolute-action formula/value mismatch. Chapter 13 carries a flavour-mixing audit that preserves the PMNS reactor-angle tension and historical CKM diagnostics. These remain evidence inputs rather than current-status owners.

## 8. Unified Evidence Matrix audit

Current validator:

```text
python3 TIR/validation/tir_v12_evidence_matrix_consistency_v0_2.py
```

The publication owner for observable verdicts remains

```text
TIR/monograph/v12/chapters/ch19_unified_evidence_matrix.tex
```

The v0.2 audit checks the 32 normalized rows and retains charged-lepton precision failures, PMNS \(\theta_{13}\) tension, neutron-EDM failure, formula quarantines, hypercharge-source openness and standard anomaly-algebra PASS without conflating those statuses.

## 9. Current completion-frontier audit

The historical v12.0 DAG snapshot is retained in repository history. The v12.1 publication synchronization uses

```text
python3 TIR/validation/tir_v12_1_completion_frontier_dag_v0_2.py
```

The current DAG treats A2-A4 and the A5 certifier/input contracts according to their actual theorem/contract status, keeps production spatial/inter-leaf inputs open, and explicitly records `riemann_hypothesis_in_closure=false`.

## 10. Repository-to-monograph synchronization

```text
python3 TIR/validation/tir_v12_1_repository_sync_audit.py
```

This fail-closed audit verifies that the v12.1 master, Chapters 7, 10 and 21, Appendix E, current status and dependency export all point to the current theorem graph and preserve the physical-promotion firewall.

Audit ledger:

```text
TIR/monograph/v12/TIR_MONOGRAPH_V12_1_AUDIT_20260910.md
```

## 11. Source and appendix contracts

The integrated source contract is

```text
python3 TIR/validation/tir_v12_source_contract_v0_2.py
```

with v12.1 synchronization markers added on the correction branch. Appendices A-D remain bound to their frozen v12.0 hashes through

```text
python3 TIR/validation/tir_v12_appendix_integration_audit_v0_1.py
```

Appendix E is validated by the v12.1 repository-sync audit rather than being retroactively inserted into the A-D hash receipt.

## 12. Critical-axis firewall

The integrated critical-axis workflow must continue to establish

```text
"riemann_hypothesis_in_closure": false
```

for the current theorem graph. Exact transforms, equivalence reductions or conditional positive corridors do not convert an RH-equivalent global positivity/nondegeneracy premise into a proof.

## 13. Publication validation

The v12.1 branch build must run the structural validators above, the current evidence validator, the source/appendix/sync audits, and the LaTeX/PDF preflight on the same exact branch head. Required document checks include a successful two-pass build, no undefined references/citations, no duplicate labels, no fatal PDF-string warnings, `qpdf --check`, and no Type-3 fonts.

## Reviewer checklist

1. Run the canonical κ and Platonic-L structural validators.
2. Run the A2-A5 spatial stack and confirm production-input firewalls remain open where appropriate.
3. Run the discrete-label and coefficient-role validators.
4. Run the v12 flavour/hadron diagnostics and the v0.2 evidence matrix audit.
5. Run the v12.1 completion-frontier and repository-sync validators.
6. Inspect retained `FAIL`, `TENSION`, `OPEN`, and `QUARANTINED` rows in Chapter 19.
7. Compile `TIR/monograph/tir_monograph_v12.tex` on the exact correction head and run PDF preflight before any promotion to `main`.
