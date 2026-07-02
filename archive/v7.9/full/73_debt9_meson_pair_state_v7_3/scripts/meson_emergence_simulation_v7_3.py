#!/usr/bin/env python3
"""DEBT-009 meson pair-state emergent simulation on Poincaré disk.

Tests hypothesis: meson action offset ΔS = OI * f(p,q) where f(p,q)
emerges from Kuramoto evolution of q-qbar oscillator pair with
prime-weighted coupling on the Poincaré disk geometry.

Target values from observation (to be verified emergent):
  - pion (u=3,d=5):  ΔS/OI ≈ 6/π  = 1.90986
  - kaon  (u=3,s=7): ΔS/OI ≈ ζ(2)-1 = π²/6-1 = 0.64493

Boundary conditions:
  - ω_q = OI × prime_1  (natural frequency from quark identity)
  - ω_qbar = OI × prime_2
  - W_ij = exp(-OI × L3 × |ln(p_i)-ln(p_j)|²)  (v5.9 style)
  - Initial phase Δφ₀ from prime geometry
"""

from __future__ import annotations
import math, json, sys, csv
from pathlib import Path

import numpy as np

# ── Metatime constants ──────────────────────────────────────────────────
OI = math.log(2.0) / (24.0 * math.pi)
L3 = 7.0

# Quark prime identity
QUARK_PRIME = {'u': 3, 'd': 5, 's': 7, 'c': 11, 'b': 13, 't': 17}

# ── Meson states to simulate ────────────────────────────────────────────
MESONS = {
    'pion+':   {'q': 'u', 'qbar': 'd', 'target': 6.0/math.pi},
    'kaon+':   {'q': 'u', 'qbar': 's', 'target': math.pi**2/6.0 - 1.0},
    'D+':      {'q': 'c', 'qbar': 'd', 'target': None},
    'B+':      {'q': 'u', 'qbar': 'b', 'target': None},
}

def meson_n(q, qbar):
    return QUARK_PRIME[q] * QUARK_PRIME[qbar]

def meson_omega(q, qbar):
    """Natural frequencies from quark prime identity.
    Flavor asymmetry → frequency splitting → eccentric orbit."""
    p = QUARK_PRIME[q]
    qp = QUARK_PRIME[qbar]
    # Asymmetric frequencies produce elliptical orbits on Poincaré disk
    omega_q = OI * p
    omega_qbar = OI * qp
    return np.array([omega_q, omega_qbar], dtype=np.float64)


def wij_meson(q, qbar):
    """Coupling between q and qbar.
    Uses v5.9 wij_pair formula — the geometric link through prime log-space."""
    p = QUARK_PRIME[q]
    qp = QUARK_PRIME[qbar]
    diff = (math.log(p) - math.log(qp))**2
    w = math.exp(-OI * L3 * diff)
    # Antiquark orientation: open link → enhancement
    w_annihilation = w * math.exp(OI * L3)
    return w_annihilation


def initial_phase_gap(q, qbar):
    """Initial phase gap from prime ratio.
    On Poincaré disk: Δφ₀ = π × |p-q|/(p+q)  (mass ratio as angular separation).
    This creates an eccentric elliptical orbit from the start."""
    p = QUARK_PRIME[q]
    qp = QUARK_PRIME[qbar]
    asymmetry = abs(p - qp) / (p + qp)
    # Phase gap: 0 = sync (no binding), π = antisync (max binding energy)
    return math.pi * asymmetry
    # Note: not using symmetry collapse yet — that's what the simulation tests


def integrate_kuramoto_pair(omega, w, phi0, steps=50000, dt=OI):
    """Integrate Kuramoto for a 2-oscillator q-qbar pair.
    Returns full trajectory for ZPE analysis."""
    N = len(omega)
    phi = np.array(phi0, dtype=np.float64)
    trajectory = []
    
    for i in range(steps):
        diff = phi[1] - phi[0]
        coupling = w * np.sin(diff) / N
        
        dphi = np.array([
            omega[0] + coupling,
            omega[1] - coupling,  # opposite sign for symmetric pair
        ])
        phi = (phi + dt * dphi) % (2.0 * np.pi)
        
        if i % 10 == 0:  # subsample
            zpe = w * (1.0 - np.cos(diff)) / (N * (N-1) * 2.0)
            trajectory.append({
                'step': i,
                'phi_0': float(phi[0]),
                'phi_1': float(phi[1]),
                'diff': float(diff),
                'zpe': float(zpe),
                'sync_r': float(np.abs(np.exp(1j*phi).mean())),
            })
    
    return trajectory


def action_offset_from_zpe(trajectory, omega, w):
    """Extract emergent action offset ΔS/OI from the ZPE profile.
    
    The perihelion overload in the Poincaré disk corresponds to the
    MAXIMUM ZPE during one orbital cycle. This maps to ΔS.
    """
    zpes = [t['zpe'] for t in trajectory[100:]]  # skip transient
    diffs = [t['diff'] for t in trajectory[100:]]
    
    # ZPE peak = perihelion overload
    zpe_max = max(zpes)
    zpe_mean = sum(zpes) / len(zpes)
    
    # The action offset is the accumulated ZPE stress
    # Normalized by OI to give ΔS/OI
    # This is the key emergent quantity
    delta_s_over_oi = zpe_max / OI  # hypothesis: peak stress = action offset
    
    return {
        'delta_s_over_oi_peak': delta_s_over_oi,
        'delta_s_over_oi_mean': zpe_mean / OI,
        'zpe_max': zpe_max,
        'zpe_mean': zpe_mean,
    }


def perihelion_overload_analysis(trajectory):
    """Analyze phase orbit for perihelion overload signature.
    
    On the Poincaré disk, the pair follows an elliptical orbit.
    At perihelion (closest approach in phase space → min |Δφ|),
    the hyperbolic curvature peaks, producing the overload."""
    diffs = [abs(t['diff']) for t in trajectory[100:]]
    phases = [t['phi_0'] for t in trajectory[100:]]
    
    # Find perihelion events: points where |Δφ| is minimized
    # These are "closest approach" in phase space
    min_diff = min(diffs)
    max_diff = max(diffs)
    
    # The overload ratio: how much the peak curvature exceeds mean
    overload_ratio = max_diff / max(min_diff, 1e-9)
    
    return {
        'min_phase_gap': min_diff,
        'max_phase_gap': max_diff,
        'overload_ratio': overload_ratio,
    }


def run_simulation(name, q, qbar, target=None, steps=50000):
    print(f"\n{'='*60}")
    print(f"  Meson: {name}  ({q}-{qbar}bar)")
    print(f"{'='*60}")
    
    n = meson_n(q, qbar)
    print(f"  Prime product n = {n} = {QUARK_PRIME[q]}×{QUARK_PRIME[qbar]}")
    print(f"  σ(n) = {sum(d for d in range(1, n+1) if n % d == 0)}")
    
    omega = meson_omega(q, qbar)
    w = wij_meson(q, qbar)
    phi0 = [0.0, initial_phase_gap(q, qbar)]
    
    print(f"  ω_q = {omega[0]:.6f}, ω_qbar = {omega[1]:.6f}")
    print(f"  Δω = {abs(omega[1]-omega[0]):.6f} = {abs(omega[1]-omega[0])/OI:.4f} × OI")
    print(f"  W_ij(coupling) = {w:.6f}")
    print(f"  Δφ₀ = {phi0[1]:.4f} rad = {phi0[1]/math.pi:.4f} × π")
    
    # Run Kuramoto integration
    traj = integrate_kuramoto_pair(omega, w, phi0, steps=steps, dt=OI)
    
    # Extract emergent action offset
    emergent = action_offset_from_zpe(traj, omega, w)
    overload = perihelion_overload_analysis(traj)
    
    print(f"\n  --- Emergent results ---")
    print(f"  ΔS/OI (peak ZPE / OI) = {emergent['delta_s_over_oi_peak']:.6f}")
    print(f"  ΔS/OI (mean ZPE / OI) = {emergent['delta_s_over_oi_mean']:.6f}")
    print(f"  ZPE peak = {emergent['zpe_max']:.6e}")
    print(f"  ZPE mean = {emergent['zpe_mean']:.6e}")
    print(f"  Perihelion overload ratio = {overload['overload_ratio']:.4f}")
    print(f"  Min phase gap = {overload['min_phase_gap']:.4f}")
    print(f"  Max phase gap = {overload['max_phase_gap']:.4f}")
    
    if target is not None:
        print(f"\n  Target ΔS/OI = {target:.6f}")
        error = abs(emergent['delta_s_over_oi_peak'] - target) / target * 100
        print(f"  Error = {error:.4f}%")
        print(f"  MATCH" if error < 2.0 else f"  MISMATCH (error > 2%)")
    
    return {
        'name': name,
        'composition': f"{q}{qbar}bar",
        'n': n,
        'omega_q': float(omega[0]),
        'omega_qbar': float(omega[1]),
        'omega_asymmetry': float(abs(omega[1]-omega[0])/OI),
        'w_coupling': w,
        'initial_gap_rad': phi0[1],
        'delta_s_oi_emergent': emergent['delta_s_over_oi_peak'],
        'delta_s_oi_mean': emergent['delta_s_over_oi_mean'],
        'zpe_peak': emergent['zpe_max'],
        'zpe_mean': emergent['zpe_mean'],
        'overload_ratio': overload['overload_ratio'],
        'target': target,
        'target_error_pct': abs(emergent['delta_s_over_oi_peak'] - target) / target * 100 if target else None,
    }


def main():
    results = []
    for name, spec in MESONS.items():
        r = run_simulation(name, spec['q'], spec['qbar'], spec['target'], steps=50000)
        results.append(r)
    
    # Summary table
    print(f"\n\n{'='*60}")
    print(f"  SUMMARY: Meson pair-state emergence")
    print(f"{'='*60}")
    print(f"  {'Meson':<10} {'ΔS/OI_em':>10} {'ΔS/OI_target':>13} {'err%':>8} {'ζ(n)':>10} {'ω_asym':>10}")
    print(f"  {'-'*60}")
    
    for r in results:
        zeta_val = ""
        if r['name'] == 'pion+':
            zeta_val = "π/ζ(2)=6/π"
        elif r['name'] == 'kaon+':
            zeta_val = "ζ(2)-1"
        target_s = f"{r['target']:.6f}" if r['target'] else "N/A"
        err_s = f"{r['target_error_pct']:.2f}%" if r['target_error_pct'] else "N/A"
        print(f"  {r['name']:<10} {r['delta_s_oi_emergent']:>10.6f} {target_s:>13} {err_s:>8} {zeta_val:>10} {r['omega_asymmetry']:>10.4f}")
    
    # Save results
    out = Path(__file__).resolve().parent / '../results/meson_emergence_simulation_v7_3.json'
    # Actually create in metatime directory
    metatime_root = Path('/tmp/ciel_metatime/METATIME_STANDARD_MODEL_DERIVATION_MERGED_REPO_v7_0_E_MU_RELEASE_REFINEMENT_GATE_NO_NESTED_ZIPS')
    out73 = metatime_root / '73_debt9_meson_pair_state_v7_3/results/meson_emergence_simulation_v7_3.json'
    out73.parent.mkdir(parents=True, exist_ok=True)
    out73.write_text(json.dumps(results, indent=2))
    print(f"\n  Results saved to {out73}")


if __name__ == '__main__':
    main()
