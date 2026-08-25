#!/usr/bin/env python3
"""Stage 9: QHTRI 36D computational gate for C3 x Z2 / polynomial-Poincare structure.

Scope:
- pure computational mathematics,
- no atomic observables,
- no PDG inputs,
- six-state active sector embedded isometrically in 36D QHTRI state space.

The active generator is (j,s)->(j+1 mod 3,1-s). A Hermitian H6 is
constructed spectrally so exp(-i H6)=G6. H6 is then embedded as the
leading 6x6 block of H36.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np

TOL = 1e-12

def build_generator() -> np.ndarray:
    G = np.zeros((6, 6), dtype=np.complex128)
    for j in range(3):
        for s in range(2):
            q = 2*j + s
            q2 = 2*((j+1) % 3) + (1-s)
            G[q2, q] = 1.0
    return G

def hermitian_log_generator(G: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    order = [0]
    q = 0
    for _ in range(5):
        q = int(np.argmax(np.abs(G[:, q])))
        order.append(q)
    S = np.eye(6, dtype=np.complex128)[:, order]
    C = S.conj().T @ G @ S
    F = np.zeros((6, 6), dtype=np.complex128)
    m = np.arange(6)
    for k in range(6):
        F[:, k] = np.exp(-2j*np.pi*k*m/6)/np.sqrt(6)
    eig = np.diag(F.conj().T @ C @ F)
    h = -np.angle(eig)
    V = S @ F
    H = V @ np.diag(h) @ V.conj().T
    U = V @ np.diag(np.exp(-1j*h)) @ V.conj().T
    return H, U

def projected_distribution(psi: np.ndarray) -> np.ndarray:
    p = np.abs(psi[:6])**2
    return np.array([p[2*j] + p[2*j+1] for j in range(3)])

def run() -> dict:
    G = build_generator()
    H6, U6 = hermitian_log_generator(G)
    H36 = np.zeros((36,36), dtype=np.complex128)
    H36[:6,:6] = H6
    U36 = np.eye(36, dtype=np.complex128)
    U36[:6,:6] = U6

    psi0 = np.zeros(36, dtype=np.complex128)
    psi0[0] = 1.0
    psi3 = np.linalg.matrix_power(U36, 3) @ psi0
    psi6 = np.linalg.matrix_power(U36, 6) @ psi0

    radii = [0.25, 0.5, 0.75, 0.95]
    poly_max = {str(r): 0.0 for r in radii}
    trajectory = []
    psi = psi0.copy()
    for step in range(7):
        q = int(np.argmax(np.abs(psi[:6])**2))
        j, sheet = divmod(q, 2)
        trajectory.append({
            "step": step,
            "basis_index": q,
            "projected_C3_index": j,
            "sheet": sheet,
            "norm": float(np.vdot(psi, psi).real),
        })
        for r in radii:
            z = r*np.exp(2j*np.pi*j/3)
            poly_max[str(r)] = max(poly_max[str(r)], float(abs(z**3-r**3)))
        psi = U36 @ psi

    geom = []
    for N in range(3, 11):
        ctheta = np.cos(2*np.pi/N)
        c = ctheta/(1-ctheta)
        if abs(c) <= 1 + 1e-14:
            rb = math.sqrt(max(0.0, 1-c*c))
            status = "DEGENERATE" if rb < TOL else "NONDEGENERATE"
        else:
            rb = None
            status = "OUTSIDE_BLOCH_SPHERE"
        geom.append({"N": N, "c": float(c),
                     "base_radius": None if rb is None else float(rb),
                     "status": status})

    target = np.zeros(7, dtype=np.complex128)
    target[0], target[-1] = 1.0, -1.0
    char_err = float(np.max(np.abs(np.poly(G)-target)))
    root_err = float(max(abs(x**6-1) for x in np.linalg.eigvals(G)))

    gates = {
        "H36_hermiticity_error": float(np.max(np.abs(H36-H36.conj().T))),
        "U36_unitarity_error": float(np.max(np.abs(U36.conj().T@U36-np.eye(36)))),
        "single_step_generator_error": float(np.max(np.abs(U36[:6,:6]-G))),
        "projected_period_3_error": float(np.max(np.abs(
            projected_distribution(psi3)-projected_distribution(psi0)))),
        "lifted_period_3_state_error_expected_nonzero": float(np.max(np.abs(psi3-psi0))),
        "lifted_period_6_state_error": float(np.max(np.abs(psi6-psi0))),
        "characteristic_polynomial_lambda6_minus_1_error": char_err,
        "eigenvalue_sixth_root_residual": root_err,
        "poincare_polynomial_residual_max_by_radius": poly_max,
        "generator_power_identity_errors": {
            str(k): float(np.max(np.abs(np.linalg.matrix_power(G,k)-np.eye(6))))
            for k in range(1,7)
        },
    }

    passed = (
        gates["H36_hermiticity_error"] < TOL
        and gates["U36_unitarity_error"] < TOL
        and gates["single_step_generator_error"] < TOL
        and gates["projected_period_3_error"] < TOL
        and gates["lifted_period_3_state_error_expected_nonzero"] > 0.5
        and gates["lifted_period_6_state_error"] < TOL
        and char_err < TOL
        and root_err < TOL
        and max(poly_max.values()) < TOL
        and geom[3]["N"] == 6 and geom[3]["status"] == "DEGENERATE"
    )
    return {
        "schema": "TIR-QHTRI-POLYGONAL/0.1",
        "stage": "9",
        "scope": "pure computational mathematics; no atomic/PDG inputs",
        "dimension": 36,
        "active_sector_dimension": 6,
        "generator": "C3 x Z2 six-state lift",
        "radii_sweep": radii,
        "gates": gates,
        "trajectory": trajectory,
        "equal_edge_polygon_geometry": geom,
        "verdict": "PASS" if passed else "FAIL",
    }

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    result = run()
    text = json.dumps(result, indent=2)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if result["verdict"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
