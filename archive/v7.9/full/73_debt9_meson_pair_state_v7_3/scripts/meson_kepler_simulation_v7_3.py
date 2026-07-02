#!/usr/bin/env python3
"""DEBT-009 meson emergence simulation — Poincaré disk Kepler dynamics.

Instead of first-order Kuramoto (which phase-locks symmetric pairs),
this uses the CIEL Kepler engine: two bodies (q, qbar) on the Poincaré
disk with semantic mass M_sem derived from quark primes, interacting
through hyperbolic geometry.

The pair follows an elliptical orbit. At perihelion (closest approach
in Poincaré metric), the hyperbolic curvature peaks — this is the
"przeciążenie przy peryhelium" (perihelion overload) that determines
the meson action offset ΔS.

Physics:
  - Position: (ρ_i, φ_i) on Poincaré disk
  - Semantic mass from prime: M_sem = p × OI / L3
  - Potential: V(ρ) = -W_ij / ρ  (coupling as effective gravity)
  - Eccentricity ε from prime asymmetry: ε = |p-q|/(p+q)
  - Overload = integrated ZPE excess over circular orbit at same a
"""

from __future__ import annotations
import math, json
from pathlib import Path

import numpy as np

# ── Metatime constants ──────────────────────────────────────────────────
OI = math.log(2.0) / (24.0 * math.pi)
L3 = 7.0
QUARK_PRIME = {'u': 3, 'd': 5, 's': 7, 'c': 11, 'b': 13, 't': 17}

# ── Mesons ──────────────────────────────────────────────────────────────
MESONS = {
    'pion+':   {'q': 'u', 'qbar': 'd', 'target': 6.0/math.pi},
    'kaon+':   {'q': 'u', 'qbar': 's', 'target': math.pi**2/6.0 - 1.0},
    'D+':      {'q': 'c', 'qbar': 'd', 'target': None},
    'B+':      {'q': 'u', 'qbar': 'b', 'target': None},
}

# ── Poincaré disk geometry ──────────────────────────────────────────────

def hyperbolic_distance(r1, phi1, r2, phi2):
    """Distance on Poincaré disk between points (r,phi)."""
    r1 = min(r1, 0.9999)
    r2 = min(r2, 0.9999)
    num = r1**2 + r2**2 - 2.0 * r1 * r2 * math.cos(phi2 - phi1)
    arg = 1.0 + 2.0 * num / max(1e-12, (1.0 - r1**2) * (1.0 - r2**2))
    return math.acosh(max(1.0, arg))

def poincare_radius(theta):
    """Map polar angle θ to Poincaré radius ρ."""
    return math.tanh(math.tan(max(0.0, min(theta, math.pi/2 - 1e-9))/2.0))


def integrate_meson_pair(p, qp, steps=100000, dt=OI/10.0):
    """Integrate q-qbar orbit on Poincaré disk with semantic inertia.
    
    Two-body problem in hyperbolic geometry.
    Each body has semantic mass M_i = p_i × OI / L3.
    They orbit their common center of mass under potential V = -W/ρ.
    
    Returns trajectory with positions, velocities, ZPE, curvature."""
    
    M_q = p * OI / L3
    M_qbar = qp * OI / L3
    M_tot = M_q + M_qbar
    mu = M_q * M_qbar / M_tot  # reduced mass
    
    # W_ij coupling (v5.9 style)
    diff_log = (math.log(p) - math.log(qp))**2
    W_base = math.exp(-OI * L3 * diff_log)
    W = W_base * math.exp(OI * L3)  # q-qbar enhancement
    
    # Orbital parameters from primes
    eccentricity = abs(p - qp) / (p + qp)
    a = 0.3 + OI * (p + qp) / 4.0   # semi-major axis scales with primes
    
    # Perihelion distance
    r_min = a * (1.0 - eccentricity)
    r_max = a * (1.0 + eccentricity)
    
    # Initial positions at perihelion (closest approach)
    rho_q = a * M_qbar / M_tot * (1.0 - eccentricity)
    rho_qbar = a * M_q / M_tot * (1.0 - eccentricity)
    
    # Orbital angular velocity at perihelion (Kepler II)
    v_orbital = math.sqrt(W / (mu * a)) * math.sqrt((1.0 + eccentricity) / (1.0 - eccentricity))
    
    phi_q = 0.0
    phi_qbar = math.pi  # opposite sides initially
    
    dphi_q = v_orbital / max(rho_q, 1e-9)
    dphi_qbar = -v_orbital / max(rho_qbar, 1e-9)
    drho_q = 0.0
    drho_qbar = 0.0
    
    trajectory = []
    
    for i in range(steps):
        # Current distance between q and qbar on Poincaré disk
        d_hyper = hyperbolic_distance(rho_q, phi_q, rho_qbar, phi_qbar)
        
        # Gravitational-like potential (W_ij creates the binding)
        sep = max(d_hyper, 1e-6)
        F = W / (sep * sep)
        
        # Direction vector in Poincaré coordinates
        dx = rho_qbar * math.cos(phi_qbar) - rho_q * math.cos(phi_q)
        dy = rho_qbar * math.sin(phi_qbar) - rho_q * math.sin(phi_q)
        dist = math.hypot(dx, dy)
        if dist < 1e-9: continue
        fx, fy = dx/dist, dy/dist
        
        # Forces in polar coordinates for q
        ax = F * fx / M_q
        ay = F * fy / M_q
        
        # Convert to polar acceleration for q
        cos_phi = math.cos(phi_q)
        sin_phi = math.sin(phi_q)
        a_radial = ax * cos_phi + ay * sin_phi
        a_angular = (-ax * sin_phi + ay * cos_phi) / max(rho_q, 1e-9)
        
        # Radial EOM with centrifugal + hyperbolic curvature correction
        # Hyperbolic curvature factor: K_h = 1/(1-rho²)²  (peaks at boundary)
        K_h_q = 1.0 / (1.0 - rho_q**2)**2
        K_h_qbar = 1.0 / (1.0 - rho_qbar**2)**2
        
        # Curvature-modified centrifugal force
        centri_q = rho_q * dphi_q**2 * K_h_q
        centri_qbar = rho_qbar * dphi_qbar**2 * K_h_qbar
        
        # Damping (environmental: small, just for stability)
        eta = OI * 10.0
        
        # Update radial velocity and position (q)
        drho_q += (a_radial + centri_q - eta * drho_q) * dt / (1.0 + eta * dt)
        rho_q = max(0.001, min(0.999, rho_q + drho_q * dt))
        
        # Update angular velocity and position (q)
        dphi_q += (a_angular - eta * dphi_q) * dt / (1.0 + eta * dt)
        phi_q = (phi_q + dphi_q * dt) % (2.0 * math.pi)
        
        # Forces for qbar (equal and opposite)
        ax_qbar = -F * fx / M_qbar
        ay_qbar = -F * fy / M_qbar
        a_radial_qbar = ax_qbar * math.cos(phi_qbar) + ay_qbar * math.sin(phi_qbar)
        a_angular_qbar = (-ax_qbar * math.sin(phi_qbar) + ay_qbar * math.cos(phi_qbar)) / max(rho_qbar, 1e-9)
        
        drho_qbar += (a_radial_qbar + centri_qbar - eta * drho_qbar) * dt / (1.0 + eta * dt)
        rho_qbar = max(0.001, min(0.999, rho_qbar + drho_qbar * dt))
        
        dphi_qbar += (a_angular_qbar - eta * dphi_qbar) * dt / (1.0 + eta * dt)
        phi_qbar = (phi_qbar + dphi_qbar * dt) % (2.0 * math.pi)
        
        # ── Measurements ──
        # ZPE from phase gap
        delta_phi = abs(phi_qbar - phi_q)
        zpe = W * (1.0 - math.cos(delta_phi)) / 4.0  # Kuramoto ZPE
        
        # Hyperbolic curvature overload at current positions
        curvature_q = 1.0 / (1.0 - rho_q**2)
        curvature_qbar = 1.0 / (1.0 - rho_qbar**2)
        total_curvature = curvature_q + curvature_qbar
        
        # Integrated ZPE (running sum)
        if i % 50 == 0:
            trajectory.append({
                'step': i,
                'rho_q': rho_q, 'rho_qbar': rho_qbar,
                'phi_q': phi_q, 'phi_qbar': phi_qbar,
                'd_hyperbolic': d_hyper,
                'zpe': zpe,
                'curvature_q': curvature_q,
                'curvature_qbar': curvature_qbar,
                'total_curvature': total_curvature,
                'sep_euclidean': dist,
            })
    
    return trajectory


def analyze_trajectory(traj):
    """Extract emergent action offset ΔS from trajectory.
    
    The perihelion overload = excess ZPE × hyperbolic curvature,
    integrated over one orbital cycle.
    """
    # Skip transient
    steady = traj[len(traj)//4:]
    
    zpes = [t['zpe'] for t in steady]
    curves = [t['total_curvature'] for t in steady]
    d_hyper = [t['d_hyperbolic'] for t in steady]
    
    # Mean and peak ZPE
    zpe_mean = sum(zpes) / len(zpes)
    zpe_max = max(zpes)
    zpe_min = min(zpes)
    
    # Curvature-weighted overload: the hyperbolic geometry amplifies ZPE
    # at perihelion where curvature is highest
    overloads = [z * c for z, c in zip(zpes, curves)]
    overload_mean = sum(overloads) / len(overloads)
    overload_max = max(overloads)
    
    # The action offset ΔS/OI = exponentially scaled overload
    # (hypothesis: the accumulated hyperbolic stress maps to action)
    delta_s_oi_from_overload = overload_mean / OI
    
    # Alternative: peak ZPE normalized by hyperbolic distance
    if min(d_hyper) > 0:
        perihelion_zpe = max([z for z, d in zip(zpes, d_hyper) 
                             if d < sum(d_hyper)/len(d_hyper) * 0.5])
        delta_s_oi_from_peak = perihelion_zpe / OI
    else:
        delta_s_oi_from_peak = zpe_max / OI
    
    return {
        'delta_s_oi_overload': delta_s_oi_from_overload,
        'delta_s_oi_peak_zpe': delta_s_oi_from_peak,
        'zpe_mean': zpe_mean,
        'zpe_max': zpe_max,
        'zpe_min': zpe_min,
        'overload_mean': overload_mean,
        'overload_max': overload_max,
        'curvature_mean': sum(curves)/len(curves),
        'd_hyperbolic_mean': sum(d_hyper)/len(d_hyper),
    }


def run_simulation(name, q, qbar, target=None):
    print(f"\n{'='*60}")
    print(f"  Meson: {name}  ({q}-{qbar}bar)")
    print(f"{'='*60}")
    
    p = QUARK_PRIME[q]
    qp = QUARK_PRIME[qbar]
    
    print(f"  Primes: p_q={p}, p_qbar={qp}")
    print(f"  n = {p*qp}, σ(n) = {sum(d for d in range(1, p*qp+1) if p*qp % d == 0)}")
    print(f"  Mass asymmetry: |{p}-{qp}|/({p}+{qp}) = {abs(p-qp)/(p+qp):.4f}")
    
    traj = integrate_meson_pair(p, qp, steps=150000, dt=OI/10.0)
    emergent = analyze_trajectory(traj)
    
    # Derive the four candidate formulas for ΔS/OI
    # and compare with the target
    candidates = {
        'sigma_n_over_n': (sum(d for d in range(1, p*qp+1) if p*qp % d == 0)) / (p*qp),
        'sigma_n2_over_n2': (sum(d**2 for d in range(1, p*qp+1) if p*qp % d == 0)) / (p*qp)**2,
        '6_over_pi': 6.0/math.pi,
        'zeta2_minus_1': math.pi**2/6.0 - 1.0,
        'abs_p2_minus_q2_over_L3': abs(p**2 - qp**2) / L3,
        'ln_p_over_q_squared': (math.log(p/qp))**2 * L3,
        'sigma_n_over_n_minus_1_times_L3': (sum(d for d in range(1, p*qp+1) if p*qp % d == 0)/(p*qp) - 1) * L3,
    }
    
    print(f"\n  --- Emergent ---")
    print(f"  ΔS/OI (overload)  = {emergent['delta_s_oi_overload']:.6f}")
    print(f"  ΔS/OI (peak ZPE)  = {emergent['delta_s_oi_peak_zpe']:.6f}")
    print(f"  ZPE range: [{emergent['zpe_min']:.6e}, {emergent['zpe_max']:.6e}]")
    print(f"  Mean curvature: {emergent['curvature_mean']:.4f}")
    print(f"  Mean hyperbolic distance: {emergent['d_hyperbolic_mean']:.4f}")
    
    print(f"\n  --- Candidate formulas ---")
    for k, v in candidates.items():
        print(f"  {k:>30s} = {v:.6f}")
    
    if target is not None:
        print(f"\n  TARGET ΔS/OI = {target:.6f}")
        print(f"  Error (overload):  {abs(emergent['delta_s_oi_overload']-target)/target*100:.2f}%")
        print(f"  Error (peak ZPE):  {abs(emergent['delta_s_oi_peak_zpe']-target)/target*100:.2f}%")
        
        # Check which candidate matches
        for k, v in candidates.items():
            err = abs(v - target)/target*100
            if err < 5.0:
                print(f"  ✓ {k} matches target! (error {err:.2f}%)")
    
    return {
        'name': name,
        'primes': (p, qp),
        'n': p*qp,
        'sigma_n': sum(d for d in range(1, p*qp+1) if p*qp % d == 0),
        'mass_asymmetry': abs(p-qp)/(p+qp),
        'emergent': emergent,
        'candidates': candidates,
        'target': target,
    }


def main():
    all_results = []
    for name, spec in MESONS.items():
        r = run_simulation(name, spec['q'], spec['qbar'], spec['target'])
        all_results.append(r)
    
    # Summary
    print(f"\n\n{'='*70}")
    print(f"  SUMMARY: Meson emergence on Poincaré disk")
    print(f"{'='*70}")
    print(f"  {'Meson':<10} {'ΔS/OI_ovld':>11} {'ΔS/OI_peak':>11} {'target':>11} {'err%_ovld':>9} {'asym':>7}")
    print(f"  {'-'*70}")
    for r in all_results:
        tgt = r['target']
        if tgt:
            e = r['emergent']
            err_ovld = abs(e['delta_s_oi_overload'] - tgt)/tgt*100
            print(f"  {r['name']:<10} {e['delta_s_oi_overload']:>11.6f} {e['delta_s_oi_peak_zpe']:>11.6f} {tgt:>11.6f} {err_ovld:>8.2f}% {r['mass_asymmetry']:>7.4f}")
        else:
            print(f"  {r['name']:<10} {r['emergent']['delta_s_oi_overload']:>11.6f} {r['emergent']['delta_s_oi_peak_zpe']:>11.6f} {'N/A':>11} {'N/A':>9} {r['mass_asymmetry']:>7.4f}")
    
    # Save
    metatime = Path('/tmp/ciel_metatime/METATIME_STANDARD_MODEL_DERIVATION_MERGED_REPO_v7_0_E_MU_RELEASE_REFINEMENT_GATE_NO_NESTED_ZIPS/73_debt9_meson_pair_state_v7_3/results')
    metatime.mkdir(parents=True, exist_ok=True)
    (metatime / 'meson_kepler_simulation_v7_3.json').write_text(json.dumps(all_results, indent=2))
    print(f"\n  → saved to results/meson_kepler_simulation_v7_3.json")


if __name__ == '__main__':
    main()
