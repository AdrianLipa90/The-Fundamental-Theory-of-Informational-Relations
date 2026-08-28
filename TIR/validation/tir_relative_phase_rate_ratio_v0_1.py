#!/usr/bin/env python3
"""Deterministic audit for TIR Relative Phase-Rate Ratio v0.1."""
from __future__ import annotations

import json
import math


def closure_ratio_certificate() -> dict[str, object]:
    rows = []
    passed = True
    for m_i, m_j in ((1, 1), (1, 2), (2, 3), (5, 2), (-3, 4), (7, -5)):
        delta_i = 2.0 * math.pi * m_i
        delta_j = 2.0 * math.pi * m_j
        ratio_phase = delta_i / delta_j
        ratio_winding = m_i / m_j
        row_pass = math.isclose(ratio_phase, ratio_winding, rel_tol=1e-15, abs_tol=1e-15)
        passed &= row_pass
        rows.append({
            "m_i": m_i,
            "m_j": m_j,
            "phase_ratio": ratio_phase,
            "winding_ratio": ratio_winding,
            "pass": row_pass,
        })
    return {"rows": rows, "pass": passed}


def reparameterization_certificate() -> dict[str, object]:
    rows = []
    passed = True
    for m_i, m_j, duration, scale in (
        (2, 3, 1.25, 7.0),
        (5, 2, 4.0, 0.25),
        (-3, 4, 2.5, 3.0),
    ):
        avg_i = (2.0 * math.pi * m_i) / duration
        avg_j = (2.0 * math.pi * m_j) / duration
        duration_prime = scale * duration
        avg_i_prime = avg_i / scale
        avg_j_prime = avg_j / scale
        ratio_a = avg_i / avg_j
        ratio_b = avg_i_prime / avg_j_prime
        target = m_i / m_j
        row_pass = (
            math.isclose(ratio_a, target, rel_tol=1e-15, abs_tol=1e-15)
            and math.isclose(ratio_b, target, rel_tol=1e-15, abs_tol=1e-15)
        )
        passed &= row_pass
        rows.append({
            "m_i": m_i,
            "m_j": m_j,
            "duration": duration,
            "scale": scale,
            "ratio_original": ratio_a,
            "ratio_rescaled": ratio_b,
            "target": target,
            "pass": row_pass,
        })
    return {"rows": rows, "pass": passed}


def information_rate_ratio_certificate() -> dict[str, object]:
    kappa = math.log(2.0) / (24.0 * math.pi)
    rows = []
    passed = True
    for m_i, m_j, duration in ((1, 2, 3.0), (3, 5, 0.75), (7, 4, 11.0)):
        omega_i = (2.0 * math.pi * m_i) / duration
        omega_j = (2.0 * math.pi * m_j) / duration
        gamma_i = kappa * omega_i
        gamma_j = kappa * omega_j
        ratio = gamma_i / gamma_j
        target = m_i / m_j
        row_pass = math.isclose(ratio, target, rel_tol=1e-15, abs_tol=1e-15)
        passed &= row_pass
        rows.append({
            "m_i": m_i,
            "m_j": m_j,
            "information_rate_ratio": ratio,
            "target": target,
            "pass": row_pass,
        })
    return {"kappa": kappa, "rows": rows, "pass": passed}


def build_receipt() -> dict[str, object]:
    blocks = {
        "common_cycle_closure_ratio": closure_ratio_certificate(),
        "common_positive_reparameterization_invariance": reparameterization_certificate(),
        "common_kappa_information_rate_ratio": information_rate_ratio_certificate(),
    }
    passed = all(block["pass"] for block in blocks.values())
    return {
        "schema": "TIR_RELATIVE_PHASE_RATE_RATIO_V0_1",
        "scope": "TIR_COMMON_CYCLE_DIMENSIONLESS_RELATIVE_RATE_AUDIT",
        "result": "COMMON_CYCLE_AVERAGE_RELATIVE_PHASE_RATE_RATIO_EQUALS_WINDING_RATIO",
        "absolute_rate_scale": "FREE",
        "pointwise_rate_ratio": "OPEN_WITHOUT_SYNCHRONIZATION_LAW",
        "next_gate": "RELATIONAL_PHASE_SYNCHRONIZATION_LAW",
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
