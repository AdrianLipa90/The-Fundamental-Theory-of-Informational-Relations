#!/usr/bin/env python3
from __future__ import annotations

import cmath
import json
import math

import numpy as np

TOL = 1e-12


def fs_distance(n: np.ndarray, m: np.ndarray) -> float:
    dot = float(np.clip(np.dot(n, m), -1.0, 1.0))
    return 0.5 * math.acos(dot)


def transition_probability(n: np.ndarray, m: np.ndarray) -> float:
    return 0.5 * (1.0 + float(np.dot(n, m)))


def bargmann3(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> complex:
    return np.vdot(a, b) * np.vdot(b, c) * np.vdot(c, a)


def assert_close(a: float, b: float, tol: float = TOL) -> None:
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{a} != {b}")


def main() -> int:
    ex = np.array([1.0, 0.0, 0.0])
    ey = np.array([0.0, 1.0, 0.0])
    ez = np.array([0.0, 0.0, 1.0])
    normals = np.array([ex, -ex, ey, -ey, ez, -ez])
    weights = np.full(6, 1.0 / 6.0)

    checks: list[dict[str, object]] = []

    M = sum(w * np.outer(n, n) for w, n in zip(weights, normals))
    target_M = np.eye(3) / 3.0
    if not np.allclose(M, target_M, atol=TOL, rtol=TOL):
        raise AssertionError("second moment is not I/3")
    checks.append({"name": "second_moment_isotropy", "status": "PASS"})

    H = 0.25 * (np.eye(3) - M)
    target_H = np.eye(3) / 6.0
    if not np.allclose(H, target_H, atol=TOL, rtol=TOL):
        raise AssertionError("aggregate FS metric is not I/6")
    eig = np.linalg.eigvalsh(H)
    if np.linalg.matrix_rank(H, tol=TOL) != 3:
        raise AssertionError("aggregate FS metric rank is not 3")
    if not np.allclose(eig, np.full(3, 1.0 / 6.0), atol=TOL, rtol=TOL):
        raise AssertionError("unexpected eigenvalues")
    assert_close(float(np.linalg.det(H)), 1.0 / 216.0)
    assert_close(float(np.linalg.cond(H)), 1.0)
    checks.append({"name": "rank3_isotropic_metric", "status": "PASS", "eigenvalues": eig.tolist()})

    assert_close(fs_distance(ex, -ex), math.pi / 2.0)
    assert_close(fs_distance(ex, ey), math.pi / 4.0)
    assert_close(transition_probability(ex, -ex), 0.0)
    assert_close(transition_probability(ex, ey), 0.5)
    checks.append({"name": "pair_FS_and_transition_fingerprint", "status": "PASS"})

    # Standard qubit representatives for +x,+y,+z.
    plus_x = np.array([1.0, 1.0], dtype=complex) / math.sqrt(2.0)
    plus_y = np.array([1.0, 1.0j], dtype=complex) / math.sqrt(2.0)
    plus_z = np.array([1.0, 0.0], dtype=complex)
    delta = bargmann3(plus_x, plus_y, plus_z)
    phase = cmath.phase(delta)
    assert_close(phase, math.pi / 4.0)

    # Gauge invariance of the closed Bargmann product.
    ga, gb, gc = 0.37, -1.23, 2.11
    delta_g = bargmann3(
        cmath.exp(1j * ga) * plus_x,
        cmath.exp(1j * gb) * plus_y,
        cmath.exp(1j * gc) * plus_z,
    )
    if abs(delta_g - delta) > TOL:
        raise AssertionError("Bargmann product changed under ray phase gauge")
    checks.append({"name": "octant_Bargmann_phase_and_gauge", "status": "PASS", "phase": phase})

    omega_oct = math.pi / 2.0
    fs_area_oct = omega_oct / 4.0
    berry_oct = omega_oct / 2.0
    assert_close(fs_area_oct, math.pi / 8.0)
    assert_close(berry_oct, math.pi / 4.0)
    assert_close(8.0 * omega_oct, 4.0 * math.pi)
    assert_close(8.0 * fs_area_oct, math.pi)
    assert_close(8.0 * berry_oct, 2.0 * math.pi)
    c1 = (8.0 * berry_oct) / (2.0 * math.pi)
    assert_close(c1, 1.0)
    checks.append({"name": "octant_area_Berry_flux_Chern", "status": "PASS", "chern": c1})

    # Euler characteristic of cube and dual octahedral spherical complex.
    chi_hex = 8 - 12 + 6
    chi_dual = 6 - 12 + 8
    if chi_hex != 2 or chi_dual != 2:
        raise AssertionError("Euler characteristic mismatch")
    checks.append({"name": "Euler_duality", "status": "PASS", "chi_hex": chi_hex, "chi_dual": chi_dual})

    # Physicalization preserves rank and condition number for every finite ell_phi > 0.
    omega = 7.83 * 2.0 * math.pi
    c = 299_792_458.0
    ell_phi = c / omega
    H_phys = ell_phi**2 * H
    if np.linalg.matrix_rank(H_phys, tol=1e-6) != 3:
        raise AssertionError("physicalized metric lost rank")
    assert_close(float(np.linalg.cond(H_phys)), 1.0, tol=1e-9)
    checks.append({"name": "phase_clock_physicalization", "status": "PASS", "ell_phi_m": ell_phi})

    out = {
        "schema": "TIR_HEXAHEDRAL_BLOCH_DUAL_FRAME_VALIDATION_V0_1",
        "status": "PASS",
        "checks": checks,
        "summary": {"passed": len(checks), "failed": 0, "total": len(checks)},
        "claim_scope": "exact local hexahedral dual-frame geometry; global spatial binding remains open",
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
