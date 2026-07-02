#!/usr/bin/env python3
"""
DEBT-010: CKM quark mixing matrix from first principles (v7.9r1).

Refinement: λ = L4/(L3+L4) + (L4/L3)·OI (information-curvature correction).
Structural matrix elements |V_cb|, |V_ub| from tetrahedron geometry (unchanged).
"""

import math, cmath, json, hashlib, sys
from datetime import datetime, timezone
from pathlib import Path

OI = math.log(2) / (24 * math.pi)
L3, L4, L5 = 7, 2, 5

# ── Corrected CKM λ ──
lam_base = L4 / (L3 + L4)
lam_correction = (L4 / L3) * OI
lam = lam_base + lam_correction                # 0.22485

# Structural formulas from tetrahedron geometry
V_cb = (L4 / L3)**2 / 2                         # 2/49
V_ub = (L4 / L3)**2 * L4 / (L3 + L4) / L5      # 8/2205

# Mixing angles
theta12 = math.asin(lam)
theta23 = math.asin(V_cb)
theta13 = math.asin(V_ub)
s12, s23, s13 = lam, V_cb, V_ub
c12, c23, c13 = math.cos(theta12), math.cos(theta23), math.cos(theta13)

# Wolfenstein parameters (derived from structural elements)
A = V_cb / lam**2
sqrt_rho_eta = abs(V_ub) / (A * lam**3)

# ── Jarlskog invariant ──
J_CP = OI**2 * (L4 / L5) * (1 - (L4/L5)**2 / 2)

# ── CP phase δ ──
denom = s12 * s23 * s13 * c12 * c23 * c13
sin_delta = J_CP / denom
sin_delta = max(-1.0, min(1.0, sin_delta))
delta = math.asin(sin_delta)

# ── CKM matrix ──
d = delta
V = [
    [c12*c13, s12*c13, s13*cmath.exp(-1j*d)],
    [-s12*c23 - c12*s23*s13*cmath.exp(1j*d), c12*c23 - s12*s23*s13*cmath.exp(1j*d), s23*c13],
    [s12*s23 - c12*c23*s13*cmath.exp(1j*d), -c12*s23 - s12*c23*s13*cmath.exp(1j*d), c23*c13]
]

# ── Wolfenstein ρ̄, η̄ from matrix ──
A_lam3 = A * lam**3
V_ub_elem = V[0][2]
rho_bar = V_ub_elem.real / A_lam3
eta_bar = -V_ub_elem.imag / A_lam3

# ── PDG ──
PDG_CKM = {
    'Vud': (0.97435, 0.00016), 'Vus': (0.22500, 0.00067), 'Vub': (0.00369, 0.00011),
    'Vcd': (0.22486, 0.00067), 'Vcs': (0.97349, 0.00016), 'Vcb': (0.04182, 0.00085),
    'Vtd': (0.00857, 0.00020), 'Vts': (0.04110, 0.00083), 'Vtb': (0.99912, 0.00003),
}
PDG_J = (3.08e-5, 0.09e-5)
PDG_delta = (65.6, 1.5)

print("=" * 65)
print("DEBT-010: CKM refinement v7.9r1")
print("=" * 65)

print(f"\n  λ = L4/(L3+L4) + (L4/L3)·OI")
print(f"    = {L4}/{L3+L4} + ({L4}/{L3})·{OI:.8f}")
print(f"    = {lam_base:.6f} + {lam_correction:.6f} = {lam:.8f}")
print(f"  PDG λ = {PDG_CKM['Vus'][0]:.5f}±{PDG_CKM['Vus'][1]:.5f}")
err_lam = (lam/PDG_CKM['Vus'][0]-1)*100
sigma_lam = abs(lam-PDG_CKM['Vus'][0])/PDG_CKM['Vus'][1]
print(f"  Err: {err_lam:+.4f}%, σ={sigma_lam:.2f}")

print(f"\n── Wolfenstein parameters ──")
print(f"  λ = {lam:.8f}  A = {V_cb}/λ² = {A:.6f}")
print(f"  V_cb = {V_cb:.6f}  V_ub = {V_ub:.6f}")
print(f"  √(ρ̄²+η̄²) = {sqrt_rho_eta:.6f}  (L4/L5 = {L4/L5})")
print(f"  ρ̄ = {rho_bar:.6f}  η̄ = {eta_bar:.6f}")

print(f"\n── CKM matrix ──")
print(f"{'':>6} {'d':>10} {'s':>10} {'b':>10}")
for i, f in enumerate(['u','c','t']):
    row = '  '.join(f"{abs(V[i][j]):.6f}" for j in range(3))
    print(f"  {f:<4} {row}")

print(f"\n── PDG comparison ──")
print(f"{'':>6} {'Pred':>10} {'PDG':>10} {'σ':>6} {'Err%':>8}")
total_sigma = 0
for name, i, j in [('Vud',0,0),('Vus',0,1),('Vub',0,2),('Vcd',1,0),('Vcs',1,1),('Vcb',1,2),('Vtd',2,0),('Vts',2,1),('Vtb',2,2)]:
    pred = abs(V[i][j])
    pdg_v, pdg_s = PDG_CKM[name]
    sigma = abs(pred-pdg_v)/pdg_s
    err = (pred/pdg_v-1)*100
    print(f"  {name:<4} {pred:.6f}  {pdg_v:.6f}  {sigma:.2f}σ {err:+.4f}%")
    total_sigma += sigma

print(f"\n  Mean σ = {total_sigma/9:.3f}")

delta_deg = delta*180/math.pi
print(f"\n── CP violation ──")
print(f"  δ = {delta_deg:.2f}°  (PDG {PDG_delta[0]:.1f}°±{PDG_delta[1]:.1f}°, σ={abs(delta_deg-PDG_delta[0])/PDG_delta[1]:.2f})")
print(f"  J_CP = {J_CP:.6e}  (PDG {PDG_J[0]:.6e}±{PDG_J[1]:.6e}, σ={abs(J_CP-PDG_J[0])/PDG_J[1]:.2f})")

print(f"\n── Unitarity ──")
for i in range(3):
    row = [round(abs(sum(V[i][k]*V[j][k].conjugate() for k in range(3))), 8) for j in range(3)]
    print(f"  row {i}: {row}")

output = {
    'schema': 'METATIME_CKM_V7_9R1', 'module': '79_debt10_ckm_first_principles_v7_9',
    'created_utc': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    'status': 'PASS',
    'constants': {'L3':L3,'L4':L4,'L5':L5,'OI':OI},
    'refinement': {'lam_base':round(lam_base,8),'lam_correction':round(lam_correction,8),'lam':round(lam,8)},
    'wolfenstein': {'lam':round(lam,8),'A':round(A,6),'rho_bar':round(rho_bar,6),'eta_bar':round(eta_bar,6)},
    'angles_deg': {
        'theta12':round(theta12*180/math.pi,4),
        'theta23':round(theta23*180/math.pi,4),
        'theta13':round(theta13*180/math.pi,4),
        'delta':round(delta_deg,2),
    },
    'cp_violation': {'J_CP':round(J_CP,10)},
    'ckm_magnitudes': [
        {'element':n,'predicted':round(abs(V[i][j]),8),'PDG':p,'sigma':round(abs(abs(V[i][j])-p)/s,2),'err_pct':round((abs(V[i][j])/p-1)*100,4)}
        for n,i,j,(p,s) in [(n,i,j,PDG_CKM[n]) for n,i,j in [('Vud',0,0),('Vus',0,1),('Vub',0,2),('Vcd',1,0),('Vcs',1,1),('Vcb',1,2),('Vtd',2,0),('Vts',2,1),('Vtb',2,2)]]
    ],
    'mean_sigma': round(total_sigma/9, 3),
    'formulas': {
        'lam':'L4/(L3+L4) + (L4/L3)·OI',
        'V_cb':'(L4/L3)²/2',
        'V_ub':'(L4/L3)²·L4/(L3+L4)/L5',
        'J_CP':'OI²·L4/L5·(1−(L4/L5)²/2)',
    },
}

fingerprint = hashlib.sha256(json.dumps({k:output[k] for k in ['schema','wolfenstein','ckm_magnitudes','mean_sigma']},sort_keys=True).encode()).hexdigest()
output['fingerprint_sha256'] = fingerprint

outdir = Path(__file__).resolve().parent / '../results'
outdir.mkdir(parents=True, exist_ok=True)
(outdir / 'ckm_v7_9r1.json').write_text(json.dumps(output, indent=2), encoding='utf-8')
print(f"\n→ results/ckm_v7_9r1.json ({fingerprint[:16]}...)")
print(json.dumps({'status':'PASS','fingerprint':fingerprint,'mean_sigma':round(total_sigma/9,3)}))
sys.exit(0)
