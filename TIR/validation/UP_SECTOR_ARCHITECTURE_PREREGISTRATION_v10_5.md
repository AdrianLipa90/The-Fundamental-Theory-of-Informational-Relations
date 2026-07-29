# Up-sector architecture preregistration v10.5

## Status

- **Artifact class:** preregistration and architecture freeze
- **Formula selected:** no
- **Mass benchmark performed:** no
- **Prospective observables named:** yes
- **Observable mapping:** refined by v10.6
- **Canonical promotion:** forbidden at this stage
- **Debt 9:** open

This artifact follows the v10.4 no-go theorem. A single common additive `B_up` cannot close the fixed v10.2 up-sector trace because it preserves the large residual separation between `u` and `c/t`. The next stage therefore freezes the only admissible architecture classes before another formula is written.

The v10.6 identifiability audit refines, but does not erase, this freeze. It separates a generation-invariant sector baseline from a generation-varying release operator and assigns a different prospective observable to each class.

## 1. Closed route

The architecture

\[
\ln\frac{m_{u_g}}{m_e}=B_{\rm up}+\Delta_{\rm up}(g)
\]

with one common `B_up` and the v10.2 relative trace held fixed is closed as insufficient. The proof is recorded in v10.4 and Appendix L.

No later module may reintroduce the same proposal under a new name or select a common shift by minimising the already known residuals.

## 2. Pre-existing structural distinction

Before v10.5, the repository already contained the sector labels:

- `charged_lepton_small_seed`;
- `light_quark_seed`;
- `heavy_quark_resonance`.

Within the up-type rows:

- `u` belongs to `light_quark_seed`;
- `c` and `t` belong to `heavy_quark_resonance`;
- the heavy-sector rows retain the source status `old_doc_bridge_ansatz_quarantined`.

These labels predate the v10.4 no-go result. They may enter a new structural candidate only with their provenance and quarantine status intact.

## 3. Allowed candidate class A: sector-invariant universal functional

A candidate may define

\[
B_i=F(Z_{s(i)}),
\]

where `Z_s` contains only coordinates invariant across generations inside the declared sector and **the same algebraic functional `F` is evaluated for every charged sector**.

Generation, `mode`, generation-specific Collatz release, generation-varying `v7`, or another particle-level coordinate is not allowed inside class A. A candidate using such a field is reclassified as class B before testing.

The generation-invariant feature bundle may contain previously declared mass-free coordinates such as:

\[
Z_s^{(0)}=
\bigl(
 p,q,p+1,
 c,Y,Q,\chi_H,
 A^{EB}_{\rm sector},
 R_{\rm Ram,sector}
\bigr),
\]

provided the selected value is genuinely common to the declared sector and its provenance is explicit.

The function may not contain a branch keyed by `u`, `c`, or `t`. A rule that happens to act only on the singleton `u` row is invalid unless the same functional produces auditable coordinates for the other charged sectors.

## 4. Allowed candidate class B: universal relative-release operator

A candidate may replace the v10.2 relative trace by

\[
\Delta_f(g)=D\bigl(Z_{f,g},Z_{f,a(g)}\bigr),
\]

provided the same operator `D` is applied to:

- charged leptons;
- down-type quarks;
- up-type quarks.

Class B may use generation-varying structural fields, including mode, Collatz release, Euler--Berry orientation and particle-level open holonomy, but it must use them by one universal algebraic rule.

An up-only release formula is not admissible. Generation order and all sign conventions must be fixed symbolically before any numerical mass comparison.

## 5. Finite candidate family

At most three formulas may survive symbolic derivation. If multiple formulas remain possible:

1. all must be retained;
2. none may be selected using the known charged-fermion masses;
3. all must be fingerprinted before the independent observable is inspected;
4. the prospective test must use a multiplicity-aware interpretation.

Creating a large formula catalogue and reporting only the best result is forbidden.

## 6. Cross-transfer gate

Every candidate must generate structural coordinates for all charged sectors, including at least one sector that did not motivate the candidate.

The gate fails when:

- the formula is effectively a singleton `u` correction;
- the formula contains a special case for the first up-type generation;
- the light/heavy distinction is invoked for up quarks but not evaluated wherever the same structural label or feature logic occurs elsewhere;
- a heavy-sector quarantine marker is silently removed.

Cross-transfer is a structural gate, not a numerical mass-fit gate.

## 7. Frozen source artifacts

The architecture freeze records the following GitHub blob identifiers:

| Source | Blob SHA |
|---|---|
| Euler–Berry action v1.6 | `c021ebfeffef7d700d2d843a9ea5eaed4fe7754d` |
| Ramanujan seed suppression v2.1 | `ab9e290a7bc9ba5596a170b9c060b1f2f73a40d7` |
| sector orientation v3.4 | `838b2606e004049bf58d86a18cf0f345799aaa73` |
| White-Thread open holonomy v3.5 | `9576ae22f783aa0a3c333b628aa4c21656ff75c3` |
| corrected representation features v1.0 | `536dd830666e8100c00b046b625ce0028e424558` |
| v10.2 prediction table, retrospective only | `b7563fd294e9a688dd276b954ffe56fd499c621e` |

The corrected v1.0 representation table must be used instead of the v0.7 status field, which displayed allowed transitions as blocked because of an already documented hypercharge-sign error.

The machine-readable manifest is:

`TIR/validation/results/up_sector_architecture_freeze_v10_5.json`

The original v10.5 manifest fingerprint remains a provenance marker for the initial freeze. The v10.6 result ledger records the corrected observable mapping.

## 8. Forbidden operations

The following remain forbidden:

- using the known `24.18` factor, its logarithm, or a nearby expression as a design target;
- a constant, phase, seed choice, sign, or exponent selected specifically for `u`;
- selecting formulas by the known charged-fermion residuals;
- removing Ramanujan because another term appears numerically better;
- importing PDG tables or archived fitted mass solvers into candidate construction;
- claiming the current mass table as a prospective holdout;
- silently promoting `old_doc_bridge_ansatz_quarantined` heavy rows;
- changing either named external observable after seeing an unfavourable result.

## 9. Prospective observables after v10.6

### Class A — sector-invariant baseline

The primary independent observable is frozen as:

> the direct charm-to-tau Higgs coupling ratio from the first public joint ATLAS/CMS likelihood or combination released after 2026-07-28 that reports direct charm and tau Higgs-coupling information without constructing the target from the current charged-fermion mass table.

Charm and tau occupy different declared sectors, so a genuine sector baseline does not cancel from `y_c/y_tau`.

### Class B — universal relative release

The primary independent observable is frozen as:

> the direct charm-to-top Higgs coupling ratio from the first public joint ATLAS/CMS likelihood or combination released after 2026-07-28 that reports direct charm and top Higgs-coupling information without constructing the target from the current quark-mass table.

Charm and top share `heavy_quark_resonance`, so any sector-invariant baseline cancels from `y_c/y_t`. This observable therefore tests only the generation-varying relative-release operator.

The frozen v10.2 class-B prediction is

\[
\left|\frac{y_c}{y_t}\right|_{v10.2}
=0.006345210526463283.
\]

For both classes, the prospective rule is:

- freeze the candidate prediction before opening the selected likelihood;
- compare it to the published 95% confidence region;
- record PASS only when the frozen prediction lies inside that region;
- otherwise record FAIL without modifying the candidate;
- if no qualifying joint result becomes available, no replacement observable is chosen post hoc and promotion remains unavailable.

## 10. Gates

### Technical gate

Deterministic execution, complete provenance, finite coordinates, stable fingerprints and reproduction from a clean checkout.

### No-hidden-fit gate

No observed mass or mixing input in the candidate, no residual scan, no particle-name branch and no more than three retained formulas.

### Structural gate

The formula belongs to candidate class A or B, passes cross-transfer, preserves declared sector labels, respects the v10.6 reclassification rule and retains heavy-sector quarantine.

### Prospective gate

The frozen prediction passes the observable assigned to its candidate class without refitting.

### Canonical gate

All four gates must pass. A retrospective improvement on the current mass table cannot substitute for the prospective gate.

## 11. Frozen conclusion

The next implementation must begin from this architecture freeze as refined by v10.6. It may derive a generation-invariant universal sector functional or a universal relative-release operator. It may not attempt another common additive up-sector baseline, mix the two candidate classes, or disguise a `u` correction as a new geometric constant.
