#!/usr/bin/env python3
"""Deterministic audit for TIR Half-Seam Phase Fiber v0.1."""
from __future__ import annotations

import json
import math


def state(u: float, phi: float) -> tuple[complex, complex]:
    return (math.sqrt(1.0 - u) + 0j, math.sqrt(u) * complex(math.cos(phi), math.sin(phi)))


def probabilities(psi: tuple[complex, complex]) -> tuple[float, float]:
    return (abs(psi[0]) ** 2, abs(psi[1]) ** 2)


def bloch(u: float, phi: float) -> tuple[float, float, float]:
    rxy = 2.0 * math.sqrt(u * (1.0 - u))
    return (rxy * math.cos(phi), rxy * math.sin(phi), 1.0 - 2.0 * u)


def norm3(v: tuple[float, float, float]) -> float:
    return math.sqrt(sum(x * x for x in v))


def half_fiber_certificate() -> dict[str, object]:
    rows = []
    passed = True
    for phi in (0.0, math.pi / 7.0, math.pi / 2.0, math.pi, 11.0 * math.pi / 6.0):
        psi = state(0.5, phi)
        p_n, p_s = probabilities(psi)
        r = bloch(0.5, phi)
        row_pass = (
            math.isclose(p_n, 0.5, rel_tol=0.0, abs_tol=1e-15)
            and math.isclose(p_s, 0.5, rel_tol=0.0, abs_tol=1e-15)
            and math.isclose(norm3(r), 1.0, rel_tol=0.0, abs_tol=1e-15)
            and math.isclose(r[2], 0.0, rel_tol=0.0, abs_tol=1e-15)
        )
        passed &= row_pass
        rows.append({
            "phi": phi,
            "probabilities": [p_n, p_s],
            "bloch": list(r),
            "bloch_norm": norm3(r),
            "equator": math.isclose(r[2], 0.0, rel_tol=0.0, abs_tol=1e-15),
            "pass": row_pass,
        })
    return {
        "fiber": "U(1) ~= S1 over probability base (1/2,1/2)",
        "rows": rows,
        "pass": passed,
    }


def global_phase_equivalent(a: tuple[complex, complex], b: tuple[complex, complex], tol: float = 1e-12) -> bool:
    # Find a nonzero component and compare with one global unit-modulus factor.
    factor = None
    for av, bv in zip(a, b):
        if abs(bv) > tol:
            factor = av / bv
            break
    if factor is None:
        return False
    if not math.isclose(abs(factor), 1.0, rel_tol=0.0, abs_tol=tol):
        return False
    return all(abs(av - factor * bv) <= tol for av, bv in zip(a, b))


def exchange_certificate() -> dict[str, object]:
    rows = []
    passed = True
    for phi in (0.0, 0.3, math.pi / 2.0, math.pi, 1.7 * math.pi):
        psi = state(0.5, phi)
        exchanged = (psi[1], psi[0])
        target = state(0.5, (-phi) % (2.0 * math.pi))
        equivalent = global_phase_equivalent(exchanged, target)
        passed &= equivalent
        rows.append({"phi": phi, "projectively_maps_to_minus_phi": equivalent})
    fixed_phases = [0.0, math.pi]
    fixed_ok = all(
        global_phase_equivalent((state(0.5, phi)[1], state(0.5, phi)[0]), state(0.5, phi))
        for phi in fixed_phases
    )
    return {
        "action": "phi -> -phi mod 2pi",
        "rows": rows,
        "fixed_phases": ["0", "pi"],
        "fixed_phase_check": fixed_ok,
        "pass": passed and fixed_ok,
    }


def full_bloch_norm_certificate() -> dict[str, object]:
    rows = []
    passed = True
    for u in (0.0, 0.1, 0.25, 0.5, 0.8, 1.0):
        for phi in (0.0, 0.9, 2.2):
            r = bloch(u, phi)
            row_pass = math.isclose(norm3(r), 1.0, rel_tol=0.0, abs_tol=2e-15)
            passed &= row_pass
            rows.append({"u": u, "phi": phi, "norm": norm3(r), "pass": row_pass})
    return {"rows": rows, "pass": passed}


def phase_closure_certificate() -> dict[str, object]:
    rows = []
    passed = True
    for n in (1, 2, 3, 4, 5, 8, 12):
        phi = 2.0 * math.pi / n
        z = complex(math.cos(phi), math.sin(phi))
        zn = z**n
        row_pass = abs(zn - (1.0 + 0.0j)) <= 2e-14
        passed &= row_pass
        rows.append({
            "n": n,
            "phi": phi,
            "z_pow_n": [zn.real, zn.imag],
            "pass": row_pass,
        })
    return {"rows": rows, "pass": passed}


def build_receipt() -> dict[str, object]:
    blocks = {
        "half_fiber": half_fiber_certificate(),
        "pole_exchange": exchange_certificate(),
        "bloch_unit_sphere": full_bloch_norm_certificate(),
        "phase_closure": phase_closure_certificate(),
    }
    passed = all(block["pass"] for block in blocks.values())
    return {
        "schema": "TIR_HALF_SEAM_PHASE_FIBER_V0_1",
        "scope": "TIR_EXACT_GEOMETRIC_LIFT_AUDIT",
        "base": "binary probability half-seam u=1/2",
        "fiber": "relative phase U(1) ~= S1",
        "bloch_image": "equator z=0",
        "next_gate": "HALF_FIBER_PHASE_RATE_SELECTION",
        "blocks": blocks,
        "technical_status": "PASS" if passed else "FAIL",
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
