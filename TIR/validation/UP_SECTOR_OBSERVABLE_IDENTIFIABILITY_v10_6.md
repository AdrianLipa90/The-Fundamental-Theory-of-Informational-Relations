# Up-sector prospective-observable identifiability v10.6

## Status

- **Technical status:** PASS
- **Artifact class:** architecture and observable-mapping correction
- **Formula selected:** no
- **Mass benchmark performed:** no
- **Observed future likelihood inspected:** no
- **Debt 9:** open
- **Canonical promotion:** denied

This artifact refines the v10.5 architecture freeze. It does not add another mass formula. It asks whether the prospective observable assigned to each candidate class is mathematically capable of identifying that class.

## 1. Architecture classes after v10.5

The two admissible classes are now separated more sharply.

### Class A — sector-invariant baseline

A class-A term has the form

\[
B_i=B_{s(i)},
\]

where `s(i)` is a declared sector and the input coordinates are invariant across generations inside that sector.

A functional that uses `mode`, generation number, generation-varying `v7`, or another within-sector varying coordinate is not a pure baseline. It is reclassified as class B before testing.

### Class B — universal generation release

A class-B term has the form

\[
\Delta_f(g)=D\!\left(Z_{f,g},Z_{f,a(g)}\right),
\]

where the same algebraic operator `D` is applied to charged leptons, down-type quarks, and up-type quarks.

## 2. Cancellation theorem

The frozen v3.4 orientation layer assigns both charm and top to

`heavy_quark_resonance`.

For a sector-invariant baseline,

\[
\ln y_c=B_{\rm heavy}+\Delta_c,
\qquad
\ln y_t=B_{\rm heavy}+\Delta_t.
\]

Therefore

\[
\boxed{
\ln\frac{y_c}{y_t}
=
\Delta_c-\Delta_t
}
\]

and the heavy-sector baseline cancels exactly.

This means that a direct measurement of `y_c/y_t` cannot identify a pure class-A baseline. It can test only a generation-varying class-B release operator.

## 3. Corrected prospective-observable mapping

### Class A

The primary prospective observable is frozen as:

> the first qualifying post-2026-07-28 joint ATLAS/CMS likelihood or combination that reports direct charm and tau Higgs-coupling information and permits a charm-to-tau coupling ratio without reconstructing the target from the charged-fermion mass table.

Charm belongs to `heavy_quark_resonance`, while tau belongs to `charged_lepton_small_seed`. A genuine sector baseline therefore does not cancel from

\[
\frac{y_c}{y_\tau}.
\]

The candidate prediction must be frozen before opening the selected likelihood. PASS requires the frozen prediction to lie inside the published 95% confidence region. Otherwise the result is retained as FAIL.

### Class B

The primary prospective observable remains:

> the first qualifying post-2026-07-28 joint ATLAS/CMS likelihood or combination that reports direct charm and top Higgs-coupling information.

The frozen retrospective v10.2 structural prediction is

\[
\boxed{
\left|\frac{y_c}{y_t}\right|_{v10.2}
=0.006345210526463283
}
\]

because

\[
\ln\frac{y_c}{y_t}
=
7.899965155203114-12.96002015366969.
\]

This value is frozen before the future likelihood is inspected. A future match would be an independent test of the relative-release trace, not a retrospective validation of a sector baseline.

## 4. Reclassification rule

A proposed class-A candidate is automatically moved to class B when it uses any coordinate that varies between `c` and `t`, including:

- generation or mode;
- generation-specific Collatz release;
- generation-varying Euler--Berry orientation;
- generation-varying `v7`;
- any particle-level open-holonomy coordinate.

This prevents a generation correction from being disguised as an absolute sector baseline.

## 5. Source correction retained

The earlier v0.7 representation CSV displayed allowed chiral transitions as `blocked` because of a sign error in the hypercharge residual. The repository already corrected this in v1.0 using

\[
-Y_L+Y_H+Y_R=0.
\]

Future candidate construction must use the corrected v1.0 representation table, not the erroneous v0.7 status field.

Corrected source:

`archive/v7.9/full/10_standard_model_derivation_stages/11_metatime_sm_full_action_seed_arbitration_v1_0/results/representation_features_corrected_v1_0.csv`

## 6. Integrity rules

- no new mass formula is selected in v10.6;
- no future Higgs likelihood has been opened for this test;
- the known charged-fermion table remains retrospective;
- no observable may be swapped after seeing its result;
- class A and class B must be tested by observables sensitive to their own parameters;
- Ramanujan continuity and heavy-sector quarantine remain mandatory;
- canonical promotion remains denied until the appropriate prospective gate passes.

## 7. Execution

```bash
python TIR/validation/up_sector_observable_identifiability_v10_6.py
```

Output:

- `TIR/validation/results/up_sector_observable_identifiability_v10_6.json`

Fingerprint:

`baa956fb41a1867f3f6c51435a1bdc0e41167091ec0c4a24d61206a4b60a9614`
