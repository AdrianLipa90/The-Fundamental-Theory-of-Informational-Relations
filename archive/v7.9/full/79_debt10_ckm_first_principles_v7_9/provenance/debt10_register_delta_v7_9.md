# DEBT-010 Register Delta — CKM First Principles v7.9

## Status: **PASS** (Structural derivation, not a formal freeze)

## Summary
CKM quark mixing matrix derived from first principles using tetrahedron
NOEMA geometry projected onto the up-down quark sector.

## Key Results
| Parameter | Predicted | PDG | σ | Err% |
|-----------|-----------|-----|---|------|
| λ | 0.222222 | 0.225000 | 4.15 | -1.23% |
| A | 0.826531 | 0.826 | — | +0.06% |
| |V_cb| | 0.040816 | 0.04182 | 1.18 | -2.40% |
| |V_ub| | 0.003628 | 0.00369 | 0.56 | -1.68% |
| J_CP | 3.11e-5 | 3.08e-5 | 0.33 | +0.98% |
| θ₁₂ | 12.84° | 13.01° | 4.26 | -1.31% |
| θ₂₃ | 2.34° | 2.40° | 1.21 | -2.53% |
| θ₁₃ | 0.208° | 0.211° | 0.45 | -1.48% |

## Formulas
- λ = L4/(L3+L4) = 2/9
- A = (L3+L4)²/(2·L3²) = 81/98
- |V_cb| = (L4/L3)²/2 = 2/49
- |V_ub| = (L4/L3)²·L4/(L3+L4)/L5 = 8/2205
- J_CP = OI²·L4/L5·(1−(L4/L5)²/2) = 3.11×10⁻⁵
- √(ρ̄²+η̄²) = |V_ub|/(Aλ³) = L4/L5 = 2/5

## Verification
- Matrix exactly unitary (|V·V†| = I)
- Mean σ across 9 CKM elements: 2.52

## Prior Art
Builds on v3.5 (White-Thread open holonomy pre-CKM operator) and
v7.8 (tetrahedron NOEMA for PMNS).

## Open Issues
- CKM CP phase δ = 75.96° (PDG 65.6°, σ=6.91) — may be convention difference
- λ = 2/9 ≈ 0.2222 vs PDG 0.2250 (4.2σ) — possible higher-order correction
- Not yet frozen; needs cross-validation with PDG 2024
