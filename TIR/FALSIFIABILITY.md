# Falsifiability and Decision Criteria — v12 synchronization

A TIR falsification gate is defined by a frozen formula, an operational observable, a comparison convention, a decision rule, and an explicit no-refit policy. Version 12 records result state with the independent triple

`(Claim Class, Timing, Verdict)`

from `TIR/monograph/v12/STATUS_TAXONOMY.md`.

## 1. Current retained failures and tensions

| Observable | Active TIR value / relation | Comparison used by publication | v12 verdict |
|---|---:|---:|---|
| neutron EDM | \(d_n=5.3299\times10^{-26}\,e\,\mathrm{cm}\) | \(|d_n|<1.8\times10^{-26}\,e\,\mathrm{cm}\) manuscript bound | **FAIL** — factor \(\approx2.96\) high |
| \(M_W\) relation | \(83.96\,\mathrm{GeV}\) in frozen 2026 matrix | \(80.3625\pm0.0077\,\mathrm{GeV}\) | **FAIL** at precision level |
| \(M_Z\) relation | \(95.77\,\mathrm{GeV}\) in frozen 2026 matrix | \(91.1879\pm0.0020\,\mathrm{GeV}\) | **FAIL** at precision level |
| PMNS \(\sin^2\theta_{13}=1/49\) | \(0.02041\) | selected 2026 global fits \(\sim0.02195\)--\(0.02230\) | **TENSION** |
| isolated Collatz quarter-power mass trace | frozen v10.1 trace | geometric-mean multiplicative error \(\approx9.967\) | **OPEN diagnostic** |

Technical reproducibility and physical verdict are independent axes. A technically exact calculation can therefore carry an empirical `FAIL` verdict.

## 2. Strong-CP / neutron-EDM gate

The frozen reviewed assignment is

\[
\theta_{\rm QCD}
=\kappa\left(\frac27\right)^{14}
\approx2.2208\times10^{-10}.
\]

With the fixed hadronic conversion coefficient used by the publication snapshot,

\[
\boxed{
 d_n\approx5.3299\times10^{-26}\,e\,\mathrm{cm}
}.
\]

Against the manuscript bound

\[
1.8\times10^{-26}\,e\,\mathrm{cm},
\]

the frozen physical gate has verdict `FAIL`. A revised exponent, conversion, cancellation mechanism, or source map constitutes a new version and receives a new evidence record.

## 3. Canonical κ provenance and phase-rate gate

The current structural parent chain is

\[
\frac12
\longrightarrow
\ln2,
\qquad
V_F\cong\mathbb C^3,
\qquad
\dim\mathfrak{su}(3)_F=8,
\]

\[
N_{\rm mix}=3\times8=24,
\qquad
\Delta\phi_{1/2}=\pi,
\qquad
\Phi_{\rm mix}=24\pi,
\]

and therefore

\[
\boxed{
\kappa=\frac{\ln2}{24\pi}
}.
\]

Canonical theorem surface:

`TIR/foundations/TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md`

Canonical validator:

`TIR/validation/tir_kappa_flavour_mixing_normalization_v0_1.py`

The normalization is classified as a **TIR-internal derived structural normalization** with explicit flavour-mixing and half-turn parents.

With

\[
\omega=2\pi f,
\qquad
d\mathcal I=\kappa\,d\phi,
\]

the downstream identity is

\[
\boxed{
\Gamma_{\mathcal I}
=\kappa\omega
=\frac{\ln2}{12}f
}.
\]

Current classification:

| Component | v12 status |
|---|---|
| \(\kappa=\ln2/(24\pi)\) | Class B / `--` / structural validator `PASS` |
| \(\omega=2\pi f\) | Class A / standard definition |
| \(d\mathcal I=\kappa d\phi\) | Class B / TIR information-phase relation |
| \(\Gamma_{\mathcal I}=(\ln2/12)f\) | exact conditional identity |
| operational surface-refresh observable | Class B / `--` / `OPEN` |

Empirical promotion of the final row requires a frozen instrument-level observable, independent frequency measurement, units/calibration, uncertainty propagation, acceptance rule, and no-refit protocol.

## 4. TIR ↔ Secret-of-a-Half boundary

The DHSE-001 Stage-M finite counterexample fixes a useful theorem boundary:
reciprocal self-duality by itself supplies set symmetry, while dynamical extremality requires an additional positive/variational mechanism. TIR promotion of a self-dual extremum therefore names that additional parent explicitly.

## 5. Prospectively frozen component

The v10.7 separable candidate family remains a prospectively frozen TIR component. Its evidence contract contains:

- a finite frozen candidate set;
- two orthogonal target observables;
- a post-freeze data gate;
- a no-refit/no-substitution rule.

A failed candidate remains in the evidence history; a newly introduced formula receives a new experiment/version identity.

## 6. Framework-level falsification conditions

A submodel is revised or rejected when a frozen gate establishes one of the following:

1. a claimed exact derivation contains a mathematical error or an untyped assumption;
2. an implementation receipt fails to reproduce its declared formal result;
3. a prospective physical observable violates its frozen acceptance rule;
4. an independence claim is contradicted by target-value or external-anchor provenance;
5. a universal relation fails in a new sector under the same frozen operator and conventions;
6. a claimed unique structural choice has multiple surviving alternatives and lacks a selection theorem;
7. a self-duality extremality claim lacks the additional mechanism required by the finite counterexample;
8. an agreed comparison protocol selects a simpler model with superior prospective likelihood and lower effective complexity.

## 7. v12 evidence owner

Current observable verdicts are owned by

`TIR/monograph/v12/chapters/ch19_unified_evidence_matrix.tex`

with machine-checkable consistency in

`TIR/validation/tir_v12_evidence_matrix_consistency_v0_1.py`.

Historical sector tables remain provenance snapshots.

## 8. Invariant

\[
\boxed{
\text{falsifiability}
=
\text{frozen claim}
+
\text{operational observable}
+
\text{decision rule}
+
\text{versioned no-refit policy}
}
\]
