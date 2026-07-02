# v7.1 — Sealed Charged-Lepton Reconstruction Benchmark (after e→μ refinement)

This module re-runs the sealed charged-lepton reconstruction benchmark after the v7.0 `e→μ` release refinement gate replaced the older v6.2 frozen gate.

Frozen pipeline:

- `S_e` from v6.7: `1/2 - 3·OI + OI/L3 - OI²/2`
- `R_e_mu` from v7.0: `5·OI + 2·OI/L3 + ((L3+1)/2)·OI²`
- `R_mu_tau` from v6.8: `3·OI - OI/L3 - (L3/2)·OI²`
- `E_i = E_Planck · exp(-S_i / OI)`

Measured particle masses are scoring-only and not used as derivation inputs.

Status: `SEALED_CHARGED_LEPTON_RECONSTRUCTION_BENCHMARK_INSTALLED_V7_1`. Mean absolute error: 0.478% (down from 3.44% in v6.9).
