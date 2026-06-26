#!/usr/bin/env python3
"""
Metatime Framework — Rigorous Free Parameter Audit v2
Computes every SM parameter from Metatime formulas and counts ALL degrees of freedom.
"""
import math

# ── Fundamental Constants ──────────────────────────────────────────────
κ = math.log(2) / (24 * math.pi)
L3, L4, L5 = 7, 2, 5
q = {'u':3, 'd':5, 's':7, 'c':11, 'b':13, 't':17}
E_P = 1.22089e22       # MeV
E_p = 938.272          # proton mass MeV

# ── Derived fine-structure constant ────────────────────────────────────
α_inv_metatime = (L3*L4)**2 - L3**2 - L4*L5 + L4**2 * κ  # ~137.037
α_metatime = 1/α_inv_metatime

# ── External inputs (NOT derived in Metatime) ──────────────────────────
α_fine = 1/137.035999084  # PDG reference only (Metatime-derived value used)
N_c = 3
Y_L = -0.5
CREWTHER = 2.4e-16  # e·cm per θ

# ── PDG 2024 ───────────────────────────────────────────────────────────
PDG = {
    'e':0.510998950, 'μ':105.658375, 'τ':1776.86,
    'p':938.272, 'n':939.565, 'Λ':1115.683, 'Σ+':1189.37,
    'Σ0':1192.642, 'Σ-':1197.45, 'Ξ0':1314.86, 'Ξ-':1321.71,
    'Δ++':1232.0, 'Σ*+':1382.8, 'Ξ*0':1531.8, 'Ω-':1672.45,
    'v':246.22, 'sin2θW':0.23122, 'MW':80.38, 'MZ':91.19, 'MH':125.25,
    'sinθ13':0.148, 'sin2θ12':0.307, 'sin2θ23':0.545, 'δCP':244.0,
    'λ':0.22500, 'Vub':0.00369, 'Vcb':0.04182, 'JCP':3.08e-5,
}

results = {}  # store computed values for cross-check

# ═══════════════════════════════════════════════════════════════════════
# 1. CHARGED LEPTONS
# ═══════════════════════════════════════════════════════════════════════
S_e  = 0.5 - 3*κ + κ/L3 - κ**2/2
R_eμ = 5*κ + 2*κ/L3 + (L3+1)*κ**2/2
R_μτ = 3*κ - κ/L3 - L3*κ**2/2
S_μ  = S_e - R_eμ
S_τ  = S_μ - R_μτ

me = E_P * math.exp(-S_e/κ)
mμ = E_P * math.exp(-S_μ/κ)
mτ = E_P * math.exp(-S_τ/κ)
results['leptons'] = {'me':me, 'mμ':mμ, 'mτ':mτ}

# Structural: S_e (4 terms: +½, -3κ, +κ/L3, -κ²/2), R_eμ (3 terms), R_μτ (3 terms)
# 4 + 3 + 3 = 10 signed coefficients without derivation
STRUCT_LEPTONS = 10

# ═══════════════════════════════════════════════════════════════════════
# 2. BARYON OCTET
# ═══════════════════════════════════════════════════════════════════════
α_oct = E_p * κ * (q['s']**2 - q['u']**2 - q['d']**2 + L3)
γ_oct = α_oct * L4 * (L3 - L4) / L3**2   # α · 10/49 = 38.73
β_oct = -α_oct * (L3**2 - 1) / L3**2     # -α · 48/49 = -185.90

# M₀ derived: M₀ = E_p·(1 − (s+u)·κ/L₃)  — NO free parameter
M0_oct = E_p * (1 - (q['s']+q['u'])*κ/L3)
oct_masses = {}
for name, Y, I, I2 in [
    ('p',  1, 0.5, 0.75), ('n',  1, 0.5, 0.75),
    ('Λ',  0, 0,   0),    ('Σ+', 0, 1,   2),
    ('Σ0', 0, 1,   2),    ('Σ-', 0, 1,   2),
    ('Ξ0',-1, 0.5, 0.75), ('Ξ-',-1, 0.5, 0.75)]:
    oct_masses[name] = M0_oct + α_oct + β_oct*Y + γ_oct*(I2 - Y**2/4)
results['octet'] = oct_masses

# Structural: α (4-element sum: s²-u²-d²+L3), β ratio, γ (2-element sum), GMO form assumed
# 4 + 1 + 1 + 1 (GMO) = 7
STRUCT_OCTET = 7
FREE_PARAMS_OCTET = 0  # M₀ derived

# ═══════════════════════════════════════════════════════════════════════
# 3. BARYON DECUPLET
# ═══════════════════════════════════════════════════════════════════════
α10 = E_p * κ * (L3**2 + L4**2 + L5**2 + L3 + L4 + L5 + L4) / L4
β10 = -E_p * κ * L3 * L5 / L4

# M₀' derived: M₀' = E_p·(1 + (s−u)·κ)  — NO free parameter
M0_dec = E_p * (1 + (q['s']-q['u'])*κ)
dec_masses = {}
for name, Y in [('Δ++',1), ('Σ*+',0), ('Ξ*0',-1), ('Ω-',-2)]:
    dec_masses[name] = M0_dec + α10 + β10*Y
results['decuplet'] = dec_masses

# Structural: α10 (7-term sum/L4), β10 (3-term product), equal-spacing rule assumed
STRUCT_DECUPLET = 6
FREE_PARAMS_DECUPLET = 0  # M₀' derived

# ═══════════════════════════════════════════════════════════════════════
# 4. NEUTRINO PMNS
# ═══════════════════════════════════════════════════════════════════════
e1, e2, e3 = L4/L3, L4/(L3+L4), 1/L3
e4, e5, e6 = (L4/L3)**2/2, (L4/L3)**2/2*(L3+L4+1), L4/L3+(L4/L3)**2

sinθ13 = e3          # 1/7
sin2θ12 = e2 + e1**2 # 2/9 + 4/49
sin2θ23 = 0.5 + L4/L3**2
δ_CP = 180 + 180*(e1 + e1**2)  # π*(1+e1+e1²) in degrees

# Mass sector
S_bare = (1 + L4/L3) / 2  # 9/14
A_face = (L4/L3)**2 / 2   # 2/49
dS = κ * A_face * (1 - κ)
S1 = S_bare + κ*dS
mass_ratios = [1, L4, L3+L4+1]  # [1,2,10]

# m_i = E_P * 10^6 * exp(-S_i/κ) gives eV with E_P in eV (×10⁶ converts MeV→eV)
E_P_eV = E_P * 1e6
m1_eV = E_P_eV * math.exp(-(S1 - κ*math.log(1))/κ)
m2_eV = E_P_eV * math.exp(-(S1 - κ*math.log(L4))/κ)
m3_eV = E_P_eV * math.exp(-(S1 - κ*math.log(L3+L4+1))/κ)
Δm21 = m2_eV**2 - m1_eV**2
Δm31 = m3_eV**2 - m1_eV**2
results['pmns'] = {'sinθ13':sinθ13, 'sin2θ12':sin2θ12, 'sin2θ23':sin2θ23,
                   'δ_CP':δ_CP, 'm1':m1_eV, 'm2':m2_eV, 'm3':m3_eV}

# Structural: e-mapping to angles (6 edges), S_bare, dS formula, mass ratios [1,2,10], E_P×10⁶ scaling
# 6 + 1 + 1 + 1 + 1 = 10, but red-team says 7
# (6 edges are tetrahedron geometry - might count as 1 choice total)
# Let me count: tetrahedron mapping (1 choice), S_bare (1), dS (1), mass ratios (1), E_P×10⁶ (1),
# ± derivation for sin²θ23 offset (1/2 + ...) (1), δ_CP π-offset (1)
STRUCT_PMNS = 7

# ═══════════════════════════════════════════════════════════════════════
# 5. CKM QUARK MIXING
# ═══════════════════════════════════════════════════════════════════════
λ_ckm = L4/(L3+L4) + (L4/L3)*κ
Vcb = (L4/L3)**2 / 2  # 2/49
Vub = (L4/L3)**2 * L4 / ((L3+L4) * L5)  # 8/2205
A_ckm = Vcb / λ_ckm**2
J_CP = κ**2 * (L4/L5) * (1 - (L4/L5)**2/2)

# δ from direct geometric angle: arccos(L4/L5)
δ_CKM = math.degrees(math.acos(L4/L5))
results['ckm'] = {'λ':λ_ckm, 'Vcb':Vcb, 'Vub':Vub, 'J_CP':J_CP, 'δ_CKM':δ_CKM}

# Structural: λ (2-term sum: 2/9 + 2κ/7), Vcb formula, Vub (5-constant product),
# J_CP (3-term), δ back-computed not derived
STRUCT_CKM = 5

# ═══════════════════════════════════════════════════════════════════════
# 6. GAUGE BOSONS + HIGGS
# ═══════════════════════════════════════════════════════════════════════
v = E_p * (L3**2*L5 + L3*L4 + L4)  # 938.272 * 261 = 244889 MeV
sin2θW = L4/(L3+L4) + κ

g_w = L4/L3 + L4/L5  # 24/35 = 0.68571 — tetrahedron edge sum

MW = g_w * v / 2 / 1000  # GeV
MZ = MW / math.sqrt(1 - sin2θW)  # GeV

# Higgs mass: M_H = v · κ · (L3² + L4 + L5)
L_sum = L3**2 + L4 + L5  # 49 + 2 + 5 = 56
MH = v * κ * L_sum / 1000  # GeV
results['gauge'] = {'v':v/1000, 'sin2θW':sin2θW, '1/α':α_inv_metatime, 'MW':MW, 'MZ':MZ, 'MH':MH}

# Structural: v factor 261 (3-term), sin²θW formula (2/9 + κ), 1/α formula (4+1 terms),
# g_w as L4/L3+L4/L5 (2-term sum), M_H as v·κ·(L3²+L4+L5) (3-term sum)
STRUCT_GAUGE = 6
EXT_GAUGE = 0  # α now derived from Metatime

# ═══════════════════════════════════════════════════════════════════════
# 7. STRONG CP
# ═══════════════════════════════════════════════════════════════════════
θ_QCD = κ * (L4/L3)**(L3 + L4 + L5)  # exponent = 14
d_n = θ_QCD * CREWTHER
results['strong_cp'] = {'θ':θ_QCD, 'dn':d_n}

# Structural: θ form (κ·(L4/L3)^b), exponent b=13, post-hoc rejection of c=11
STRUCT_STRONGCP = 3
EXT_STRONGCP = 1  # Crewther factor

# ═══════════════════════════════════════════════════════════════════════
# 8. ANOMALY CANCELLATION
# ═══════════════════════════════════════════════════════════════════════
Y_Q = q['s']/(L3*L4*N_c)  # 1/6
Y_uR = L4/N_c             # 2/3
Y_dR = -L4/(N_c*L4)       # -1/3
Y_eR = -(L3-L4)/L5        # -1

A1 = 2*Y_Q - Y_uR - Y_dR
A2 = 3*Y_Q + Y_L
A3 = (2*Y_Q**3 + Y_L**3) - (Y_uR**3 + Y_dR**3 + Y_eR**3)
A4 = 6*Y_Q + 2*Y_L
results['anomaly'] = {'A1':A1, 'A2':A2, 'A3':A3, 'A4':A4}

# Structural: Y assignments (4 formulas), mapping to L-constants
# External: N_c=3, Y(L)=-½
STRUCT_ANOMALY = 4
EXT_ANOMALY = 2  # N_c, Y(L)

# ═══════════════════════════════════════════════════════════════════════
# 9. DARK ENERGY
# ═══════════════════════════════════════════════════════════════════════
exp_D = L3 * L4**L5  # 7 * 32 = 224
ρ_Λ = (L4/L3)**exp_D
ρ14_meV = ρ_Λ**0.25 * 1000
results['dark_energy'] = {'ρ':ρ_Λ, 'ρ14_meV':ρ14_meV}

# Structural: exponent form L3·L4^L5, L4^L5=32 as "intention space dimension"
STRUCT_DE = 3

# ═══════════════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════════════
print("=" * 72)
print("  METATIME FORMULA LEDGER — EXACT FREE PARAMETER AUDIT")
print("=" * 72)
print(f"\n  Fundamental constants (fixed): κ={κ:.6g}, L₃={L3}, L₄={L4}, L₅={L5}")
print(f"  Quark primes: {q}")
print()

struct_tbl = [
    ("Charged leptons",    STRUCT_LEPTONS,    6),
    ("Baryon octet",       STRUCT_OCTET,      9),
    ("Baryon decuplet",    STRUCT_DECUPLET,   6),
    ("Neutrino PMNS",      STRUCT_PMNS,       7),
    ("CKM",                STRUCT_CKM,        7),
    ("Gauge bosons + Higgs", STRUCT_GAUGE,    5),
    ("Strong CP",          STRUCT_STRONGCP,   5),
    ("Dark energy",        STRUCT_DE,         5),
    ("Anomaly cancellation", STRUCT_ANOMALY,  8),
]

total_free = 0
total_ext_scale = 2
total_ext_input = 3  # N_c, Y(L), Crewther (α now derived)
total_structural_my = sum(r[1] for r in struct_tbl if isinstance(r[1], int))
total_structural_rt = sum(r[2] for r in struct_tbl if isinstance(r[2], int))

print(f"  {'─'*70}")
print(f"  {'FREE PARAMETERS':70s}")
print(f"  {'─'*70}")
print(f"  {'  All M₀ now derived from framework constants':50s} {0:>3d}")
print(f"  {'  Total free continuous parameters':50s} \033[1m{total_free:>3d}\033[0m")

print(f"\n  {'─'*70}")
print(f"  {'EXTERNAL SCALES':70s}")
print(f"  {'─'*70}")
print(f"  {'  E_P (Planck energy, MeV)':50s} {'1':>3s}")
print(f"  {'  E_proton (proton mass, MeV)':50s} {'1':>3s}")

print(f"\n  {'─'*70}")
print(f"  {'EXTERNAL INPUTS (not from Metatime)':70s}")
print(f"  {'─'*70}")
print(f"  {'  N_c=3 (number of colors)':50s} {'1':>3s}")
print(f"  {'  Y(L)=-½ (lepton hypercharge)':50s} {'1':>3s}")
print(f"  {'  Crewther factor 2.4e-16 (for d_n)':50s} {'1':>3s}")
print(f"  {'  (α now derived — see GAUGE section)':50s} {'0':>3s}")

print(f"\n  {'─'*70}")
print(f"  {'STRUCTURAL CHOICES':70s}")
print(f"  {'─'*70}")
print(f"  {'  Sector':40s} {'My count':>10s} {'Red-team':>10s}")
for sector, my_c, rt_c in struct_tbl:
    match = "✓" if isinstance(rt_c, int) and abs(my_c - rt_c) <= 1 else "?"
    print(f"  {match} {sector:38s} {my_c:>10d} {(rt_c if isinstance(rt_c, int) else 0):>10d}")

print(f"  {'─'*40} {'─'*10} {'─'*10}")
print(f"  {'  TOTAL structural choices':40s} {total_structural_my:>10d} {total_structural_rt:>10d}")

print(f"\n  {'─'*70}")
print(f"  {'GRAND ACCOUNTING':70s}")
print(f"  {'─'*70}")
print(f"  {'  Free continuous parameters':55s} {total_free:>3d}")
print(f"  {'  External scales':55s} {total_ext_scale:>3d}")
print(f"  {'  External inputs (non-Metatime)':55s} {total_ext_input:>3d}")
print(f"  {'  Structural choices (my audit)':55s} {total_structural_my:>3d}")
print(f"  {'  ─'*18} {'─'*3}")
print(f"  {'  ALL degrees of freedom':55s} {total_free+total_ext_scale+total_ext_input+total_structural_my:>3d}")

print(f"\n  {'─'*70}")
print(f"  {'COMPARISON: SELECTED PREDICTIONS':70s}")
print(f"  {'─'*70}")
checks = [
    ('m_e (MeV)', me, PDG.get('e')),
    ('m_μ (MeV)', mμ, PDG.get('μ')),
    ('m_τ (MeV)', mτ, PDG.get('τ')),
    ('1/α', α_inv_metatime, PDG.get('1/α', 137.035999084)),
    ('sin²θ₁₂', sin2θ12, PDG.get('sin2θ12')),
    ('sin²θ₂₃', sin2θ23, PDG.get('sin2θ23')),
    ('δ_CP (°)', δ_CP, PDG.get('δCP')),
    ('λ_CKM', λ_ckm, PDG.get('λ')),
    ('M_H (GeV)', MH, PDG.get('MH')),
    ('M_W (GeV)', MW, PDG.get('MW')),
    ('M_Z (GeV)', MZ, PDG.get('MZ')),
]
for name, val, pdg_val in checks:
    if pdg_val and pdg_val != 0:
        err = (val - pdg_val)/pdg_val*100
        σ = abs(err)/0.1
        print(f"  {name:20s} = {val:>12.6g}  (PDG {pdg_val:>12.6g})  {'⚠' if abs(err)>2 else '✓'}  {err:+.2f}%")

print(f"\n  {'─'*70}")
print(f"  {'CLAIM LEVEL ASSESSMENT':70s}")
print(f"  {'─'*70}")
print(f"  The framework now has zero continuous free parameters,")
print(f"  {total_ext_scale} external scales, {total_ext_input} external inputs,")
print(f"  and ~{total_structural_my} structural choices.")
print(f"  → Classification: L0-L1 ansatz (formula ledger / phenomenological fit)")
print(f"  → No sector reaches L3 (physical mechanism) or L4 (physical law)")
print("=" * 72)
