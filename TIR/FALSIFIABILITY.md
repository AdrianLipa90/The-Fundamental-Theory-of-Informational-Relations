# Falsifiability and Decision Criteria — v12.1 synchronization

A TIR falsification gate is defined by a frozen formula, an operational observable, a comparison convention, a decision rule, and an explicit no-refit policy. Version 12.1 retains the independent status triple

`(Claim Class, Timing, Verdict)`

from `TIR/monograph/v12/STATUS_TAXONOMY.md`. Mathematical theorem status, software reproducibility and physical evidence remain separate axes.

## 1. Current retained failures and tensions

| Observable | Active TIR value / relation | Comparison used by publication | verdict |
|---|---:|---:|---|
| neutron EDM | \(d_n=5.3299\times10^{-26}\,e\,\mathrm{cm}\) | \(|d_n|<1.8\times10^{-26}\,e\,\mathrm{cm}\) manuscript bound | **FAIL** — factor \(\approx2.96\) high |
| \(M_W\) relation | \(83.96\,\mathrm{GeV}\) in frozen 2026 matrix | \(80.3625\pm0.0077\,\mathrm{GeV}\) | **FAIL** at precision level |
| \(M_Z\) relation | \(95.77\,\mathrm{GeV}\) in frozen 2026 matrix | \(91.1879\pm0.0020\,\mathrm{GeV}\) | **FAIL** at precision level |
| PMNS \(\sin^2\theta_{13}=1/49\) | \(0.02041\) | selected 2026 global fits \(\sim0.02195\)--\(0.02230\) | **TENSION** |
| isolated Collatz quarter-power mass trace | frozen v10.1 trace | geometric-mean multiplicative error \(\approx9.967\) | **OPEN diagnostic** |

Technical reproducibility and physical verdict are independent. A structurally exact or computationally reproducible calculation may still carry an empirical `FAIL`.

## 2. Strong-CP / neutron-EDM gate

The frozen reviewed assignment is

\[
\theta_{\rm QCD}
=\kappa\left(\frac27\right)^{14}
\approx2.2208\times10^{-10}.
\]

With the fixed hadronic conversion coefficient used by the publication snapshot,

\[
\boxed{d_n\approx5.3299\times10^{-26}\,e\,\mathrm{cm}}.
\]

Against the manuscript bound \(1.8\times10^{-26}\,e\,\mathrm{cm}\), the frozen physical gate is `FAIL`. A revised exponent, conversion, cancellation mechanism or source map is a new version and receives a new evidence record. The current replacement target is an upstream holonomic/topological source theorem, not numerical retuning of this failed row.

## 3. Canonical structural normalizations

The current information-normalization chain gives

\[
\boxed{\kappa=\frac{\ln2}{24\pi}}
\]

from the declared three-flavour mixing and half-turn parents. Canonical theorem and validator:

`TIR/foundations/TIR_KAPPA_FLAVOUR_MIXING_NORMALIZATION_V0_1.md`

`TIR/validation/tir_kappa_flavour_mixing_normalization_v0_1.py`

The discrete L-constants now also have the independent finite-group closure

\[
[S_4:A_4]=2=L_4,
\qquad
[A_5:A_4]=5=L_5,
\]

and, under the explicit TIR root-extension rule,

\[
L_3=|S_4/A_4\sqcup A_5/A_4|=7.
\]

Canonical theorem and validator:

`TIR/foundations/TIR_PLATONIC_L_CONSTANTS_CLOSURE_V0_1.md`

`TIR/validation/tir_platonic_l_constants_closure_v0_1.py`

This exact internal structural closure has no automatic physical-promotion authority.

## 4. Information-phase observable gate

With

\[
\omega=2\pi f,
\qquad
d\mathcal I=\kappa\,d\phi,
\]

the downstream identity is

\[
\boxed{\Gamma_{\mathcal I}=\kappa\omega=\frac{\ln2}{12}f}.
\]

Operational promotion of a physical \(\Gamma_{\mathcal I}\) requires an instrument-level observable, independent frequency measurement, units/calibration, uncertainty propagation, acceptance rule and no-refit protocol.

The Collatz--Fubini--Study relational-phase interface is similarly mathematical/interface-level until a separately validated physical binding to time, energy, mass, transition rates, spectroscopy or gravity exists.

## 5. TIR ↔ Secret-of-a-Half / critical-axis boundary

The local half-axis and negative-inverse identities do not by themselves prove a global dynamical extremum or the Riemann hypothesis. The active critical-axis stack contains exact reductions and conditional positive corridors, while globally quantified strict-positivity/nondegeneracy premises remain open. The integrated solver contract requires

`riemann_hypothesis_in_closure = false`.

Thus RH-equivalent positivity criteria remain falsifiable open gates rather than completed theorems.

## 6. Prospectively frozen component

The v10.7 separable candidate family remains prospectively frozen. Its evidence contract contains a finite candidate set, two orthogonal target observables, a post-freeze data gate and a no-refit/no-substitution rule. A failed candidate remains in evidence history; a new formula receives a new experiment/version identity.

## 7. Framework-level falsification conditions

A submodel is revised or rejected when a frozen gate establishes one of the following:

1. a claimed exact derivation contains a mathematical error or an untyped assumption;
2. an implementation receipt fails to reproduce its declared formal result;
3. a prospective physical observable violates its frozen acceptance rule;
4. an independence claim is contradicted by target-value or external-anchor provenance;
5. a universal relation fails in a new sector under the same frozen operator and conventions;
6. a claimed unique structural choice has multiple surviving alternatives and lacks a selection theorem;
7. a self-duality/extremality claim lacks the additional mechanism required by its counterexamples;
8. a production-input theorem is promoted using only a reference-control dataset;
9. an agreed comparison protocol selects a simpler model with superior prospective likelihood and lower effective complexity.

## 8. Current evidence owner

Current observable verdicts are owned by

`TIR/monograph/v12/chapters/ch19_unified_evidence_matrix.tex`

with machine-checkable consistency in

`TIR/validation/tir_v12_evidence_matrix_consistency_v0_2.py`.

Historical sector tables remain provenance snapshots. The v12.1 repository synchronization does not rescore Chapter 19 merely because new structural theorems were merged.

## 9. Invariant

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

and

\[
\boxed{
\text{technical/theorem PASS}\not\Rightarrow\text{physical PASS}.
}
\]
