# Metatime Archive Timeline

## Version History

### v7.0 (2026-06) — Baseline
First merged repo with charged lepton (e, μ, τ) refinement and release gate. All modules 1–41 in structural hierarchy. No nested zips.

### v7.8 (2026-06-26±) — Full freeze + slim paper
| Directory | Contents |
|-----------|----------|
| `v7.8/full/` | Complete repo (1501 files): all modules, scripts, schemas, lineages |
| `v7.8/slim/` | Paper-only: `metatime_paper.tex`, `metatime_paper_v7_9.pdf`, `CURRENT_STATUS.md` |

**Key changes**: M₀ derived for baryon octet (eliminates 1 free param), M₀' derived for decuplet, β/γ from J-KJ eigenvalues, GMO formula standardized, δ·S_dq removed.

### v7.9 (2026-06-27±) — Gauge bosons + CKM + strong CP + dark energy
| Directory | Contents |
|-----------|----------|
| `v7.9/full/` | Complete repo (1686 files): all modules plus gauge/CKM/CP/DE additions |
| `v7.9/slim/` | Paper + summary + status |

**Key changes**: CKM quark mixing (DEBT-010), gauge bosons + Higgs VEV (DEBT-015), strong CP θ_QCD (DEBT-016), anomaly cancellation (DEBT-017), dark energy D_Λ (DEBT-018), formal proofs P1–P11.

### v7.9r1 (2026-06-27) — CKM refinement
| Directory | Contents |
|-----------|----------|
| `v7.9r1/slim/` | Paper + summary + status |

**Key changes**: CKM A corrected from structural formula (81/98 = 0.82653) to A = V_cb/λ² (0.80733). Mean σ improves from 1.2 to 0.78.

### v10_final (2026-06-28±) — Alpha derived, final external input eliminated
| Directory | Contents |
|-----------|----------|
| `v10_final/slim/` | Final paper + all code |

**Key changes**: 1/α = (L₃·L₄)² − L₃² − L₄·L₅ + L₄²·κ = 137.037 (error +0.0006%). Replaces old 1/α = 9/(7κ) = 139.86. External inputs reduced from 4 to 3.

## Structural Audit (per Milligan Stage 2 Review)
- 0 continuous free parameters
- 2 external scales (E_P, E_proton)
- 3 external inputs (N_c, Y_L, Crewther factor)
- ~50 structural choices (see `/TIR/metatime_audit.py`)

## Integrity
Original zips with SHA-256 in `originals/`.
