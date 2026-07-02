# Structural-Choice Audit

Every input, constant, and formula choice in Metatime, classified by type.

## Legend
| Type | Label | Description |
|------|-------|-------------|
| P | Postulate | Framework principle, not derived |
| M | Mathematical identity | Proven from prior mathematics |
| E_phys | Physical external input | Measured constant (non-SM) |
| E_SM | SM external input | Taken from Standard Model |
| S | Structural selection | Discrete choice among alternatives |
| R | Retrospective fit | Selected to match known data |
| H | Hypothesis | Open/falsifiable prediction |

## Master Table

### Fundamental constants
| Symbol | Value | Type | Notes |
|--------|-------|------|-------|
| κ = ln2/(24π) | 0.00919315 | P | Information constant; binary outcome·A₄·Berry half-cycle |
| L₃ | 7 | P | Integer from CP³ Kähler dimension? |
| L₄ | 2 | P | Twin-prime gap? Tetrahedron edge? |
| L₅ | 5 | P | Larger twin prime; tetrahedron face? |

### Quark prime assignments
| Symbol | Value | Type | Notes |
|--------|-------|------|-------|
| q(u) | 3 | S | First odd prime |
| q(d) | 5 | S | Second odd prime |
| q(s) | 7 | S | Third odd prime (= L₃) |
| q(c) | 11 | S | Fifth prime (4 skipped?) |
| q(b) | 13 | S | Sixth prime |
| q(t) | 17 | S | Seventh prime |

Alternative prime mappings not tested. The leap from L₃=7 to q(c)=11 skips prime 7→11 without derivation. Structural choice count: 6.

### External scales & inputs
| Symbol | Value | Type | Source |
|--------|-------|------|--------|
| E_P | 1.22089e22 MeV | E_phys | Planck energy |
| E_proton | 938.272 MeV | E_phys | Proton mass |
| N_c | 3 | E_SM | Number of colors |
| Y_L | −½ | E_SM | Lepton hypercharge |
| Crewther C | 2.4×10⁻¹⁶ e·cm/θ | E_phys | nEDM conversion factor |

### Charged leptons
| Choice | Type | Count |
|--------|------|-------|
| S_e structure: ½ − 3κ + κ/L₃ − κ²/2 | S | 4 signed terms |
| R_eμ: 5κ + 2κ/L₃ + (L₃+1)κ²/2 | S | 3 terms |
| R_μτ: 3κ − κ/L₃ − L₃κ²/2 | S | 3 terms |
| Exponential decay: m_i = E_P·exp(−S_i/κ) | P | Form postulate |
| **Total structural** | | **10** |

### Baryon octet
| Choice | Type | Count |
|--------|------|-------|
| α formula: E_p·κ·(s² − u² − d² + L₃) | S | 4-term sum |
| β ratio: −α·(L₃²−1)/L₃² | S | 1 ratio |
| γ ratio: α·L₄·(L₃−L₄)/L₃² | S | 2-factor product |
| GMO form assumed | S | 1 structural assumption |
| M₀ derived: E_p·(1 − (s+u)·κ/L₃) | M | Derived from Λ mass |
| **Total structural** | | **7** |

### Baryon decuplet
| Choice | Type | Count |
|--------|------|-------|
| α₁₀: E_p·κ·(L₃²+L₄²+L₅²+L₃+L₄+L₅+L₄)/L₄ | S | 7-term sum/L₄ |
| β₁₀: −E_p·κ·L₃·L₅/L₄ | S | 3-factor product |
| Equal-spacing rule | S | 1 structural assumption |
| M₀' derived: E_p·(1 + (s−u)·κ) | M | Derived from Δ mass |
| **Total structural** | | **6** |

### Neutrino PMNS
| Choice | Type | Count |
|--------|------|-------|
| Tetrahedron edge → PMNS mapping | S | 1 assignment |
| S_bare = (1+L₄/L₃)/2 | S | 1 formula |
| dS = κ·A_face·(1−κ) | S | 1 formula |
| Mass ratios [1, L₄, L₃+L₄+1] | S | 1 selection |
| E_P·10⁶ eV scaling | S | 1 conversion |
| sin²θ₂₃ ½+ offset | S | 1 offset |
| δ_CP 180°+ offset | S | 1 offset |
| **Total structural** | | **7** |

### CKM
| Choice | Type | Count |
|--------|------|-------|
| λ = L₄/(L₃+L₄) + (L₄/L₃)·κ | S | 2-term sum |
| V_cb = (L₄/L₃)²/2 | S | 1 formula |
| V_ub = (L₄/L₃)²·L₄/((L₃+L₄)·L₅) | S | 5-constant product |
| J_CP = κ²·(L₄/L₅)·(1 − (L₄/L₅)²/2) | S | 3-factor |
| δ_CKM = arccos(L₄/L₅) | S | 1 back-computation |
| **Total structural** | | **5** |

### Gauge bosons + Higgs
| Choice | Type | Count |
|--------|------|-------|
| VEV v = E_p·(L₃²·L₅ + L₃·L₄ + L₄) | S | 3-term sum = 261 |
| sin²θ_W = L₄/(L₃+L₄) + κ | S | 2-term |
| 1/α = (L₃L₄)² − L₃² − L₄L₅ + L₄²κ | S | 4-term |
| g_w = L₄/L₃ + L₄/L₅ | S | 2-term |
| M_H = v·κ·(L₃²+L₄+L₅) | S | 3-term |
| **Total structural** | | **5** |

### Strong CP
| Choice | Type | Count |
|--------|------|-------|
| θ_QCD = κ·(L₄/L₃)^b | S | Form choice |
| Exponent b = L₃+L₄+L₅ = 14 | S | Exponent selection |
| Post-hoc rejection of c=11 | R | Alternative not justified |
| + Crewther factor (external) | E_phys | 1 |
| **Total structural** | | **3** |

### Anomaly cancellation
| Choice | Type | Count |
|--------|------|-------|
| Y_Q = q(s)/(L₃·L₄·N_c) = 1/6 | M | Derived if you accept L-constants |
| Y_uR = L₄/N_c = 2/3 | M | Ditto |
| Y_dR = −L₄/(N_c·L₄) = −1/3 | M | Ditto |
| Y_eR = −(L₃−L₄)/L₅ = −1 | M | Ditto |
| + External: N_c, Y(L) | E_SM | 2 |
| **Total structural** | | **4** |

### Dark energy
| Choice | Type | Count |
|--------|------|-------|
| ρ_Λ = (L₄/L₃)^(L₃·L₄^L₅) | S | Form + exponent |
| L₄^L₅ = 32 as "intention space dimension" | S | Interpretation |
| **Total structural** | | **3** |

## Grand Total

| Category | Count |
|----------|-------|
| Free continuous parameters | 0 |
| External physical scales | 2 |
| External SM inputs | 3 |
| Structural choices (P + S) | ~50 |
| **Total degrees of freedom** | **55** |
