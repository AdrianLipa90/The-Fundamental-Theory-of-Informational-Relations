# v7.3 — Meson Pair-State Freeze (DEBT-009)

q-qbar vortex-antivortex pair in the W_ij BEC supercondensate.
Dual operator: spectral zeta (pseudoscalar) + W_ij eigenvalue (vector).

## Sector A: Pseudoscalars (JP=0⁻)

```
ΔS/OI = π/ζ(2) = 6/π ≈ 1.90986   if r₃(p·q) = 0  (n ≡ 7 mod 8)
       = ζ(2)-1 = π²/6-1 ≈ 0.64493  if r₃(p·q) > 0  (n ≢ 7 mod 8)

E = E_proton · exp(-ΔS/OI)

E_proton = 938.27209 MeV
```

| Meson | qqbar | n | r₃ | Formula | Predicted | Reference | Error |
|-------|-------|---|----|---------|-----------|-----------|-------|
| π+  | ud | 15 | 0   | 6/π   | 138.96 | 139.57 | -0.44% |
| K+  | us | 21 | >0  | ζ(2)-1 | 492.31 | 493.68 | -0.28% |
| K0  | ds | 35 | >0  | ζ(2)-1 | 492.31 | 497.61 | -1.07% |
| η   | ss | 49 | >0  | ζ(2)-1 | 492.31 | 547.86 | -10.1% |

η needs SU(3) mixing correction (η-η' octet-singlet mixing).

## Sector B: Vectors (JP=1⁻)

```
E = E_0 · exp(-λ_k) · exp(-2·OI)

E_0 = 1037.9 MeV  (zero-mode λ=0)
exp(-2·OI) = 0.9818  (Bogoliubov correction)
λ_k ∈ spec(W_ij 24×24) from SU(3) J_KJ
```

| Meson | λ | E_pred | E_ref | Error |
|-------|---|--------|-------|-------|
| φ(1020) | 0.000 | 1019.0 | 1019.46 | -0.05% |
| K*(892) | 0.121 | 902.9 | 891.67 | +1.26% |
| η/ρ/ω   | 0.528 | 601.0 | 547.86 | +9.70% |

## Open: Heavy Mesons

| Meson | qqbar | Predicted (zeta) | Predicted (W_ij) | Reference |
|-------|-------|-----------------|-------------------|-----------|
| D+(1870) | cd | 139 γ | 2499 (λ=-0.897) | 1869.66 |
| B+(5279) | ub | 139 γ | 6270 (λ=-1.817) | 5279.34 |

Neither operator alone matches. Hypothesis: heavy quark core creates
different W_ij cavity via QCD screening length.

Status: `PASS_MESON_PAIR_STATE_OPERATOR_FROZEN`
Substantive: `LIGHT_MESON_SUB_PERCENT_HEAVY_MESON_SCALE_OPEN`
canon_allowed: false
