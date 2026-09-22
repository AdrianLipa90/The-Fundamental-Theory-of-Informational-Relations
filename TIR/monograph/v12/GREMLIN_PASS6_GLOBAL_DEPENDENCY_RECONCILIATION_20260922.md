# GREMLIN Global Dependency Reconciliation — 2026-09-22

Status: `TIR_LOCAL_SURFACE_RECONCILED / WHITE_THREAD_INCLUDED / FPDG_REFRESH_REQUIRED / PENDING_FINAL_MERGE`

Source baseline: `main@611bc7687f0a2266a7cc6cc3010f9776dc03a391`

## Result

The dependency surface is refreshed after merging TIR PRs #169--#177.

```text
claims:       35 -> 60
local edges:  40 -> 84
promoted local DAG: acyclic
```

The reconciled surface now distinguishes formal closure, physical/production binding, frozen empirical verdicts, and candidate-only structures.

White-Thread is now first-class in the source export:

```text
TIR.HALF_SEAM.PHASE_FIBER
 + TIR.HOLONOMY.SEMANTIC_U1
 -> TIR.WHITE_THREAD.SPIN_LIFT
 -> TIR.WHITE_THREAD.LYAPUNOV
```

The spin-lift records the exact 2pi/4pi double-cover identities and half-seam two-sheet lift. The Lyapunov node records the exact conditional static-holonomy energy monotonicity and overdamped gauge-twisted Kuramoto gradient flow. Dynamic field/action closure and physical astrophysical interpretation remain open.

Other principal corrections retained:

- hypercharge relative uniqueness: derivationally closed on declared field content + TIR normalization;
- neutrino absolute-action source repair: derivationally closed; absolute physical mass remains open;
- coefficient selector no-go: closed diagnostic; transition-sensitive selector remains open;
- local RFC ADM/Einstein derivation: closed; global production carrier/coverage remains open;
- legacy FAIL/TENSION receipts remain attached to their frozen formulas only;
- 600-cell/McKay-E8 physical binding remains CANDIDATE_ONLY.

After this reconciliation reaches main, FPDG must refresh the exact TIR export lock and global graph before global impact analysis.
