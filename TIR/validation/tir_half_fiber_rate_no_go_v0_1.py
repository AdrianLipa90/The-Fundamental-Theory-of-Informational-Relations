#!/usr/bin/env python3
"""Deterministic audit for TIR Half-Fiber Phase-Rate No-Go v0.1."""
from __future__ import annotations

import json
import math


def probabilities(omega: float, tau: float, phi0: float = 0.37) -> tuple[float, float]:
    phase = phi0 + omega * tau
    alpha = 1.0 / math.sqrt(2.0)
    beta = alpha * complex(math.cos(phase), math.sin(phase))
    return (abs(alpha) ** 2, abs(beta) ** 2)


def rate_family_certificate() -> dict[str, object]:
    rows = []
    passed = True
    for omega in (-7.0, -1.0, 0.0, 0.5, 3.0, 11.0):
        for tau in (0.0, 0.2, 1.0, 4.5):
            p_n, p_s = probabilities(omega, tau)
            row_pass = (
                math.isclose(p_n, 0.5, rel_tol=0.0, abs_tol=1e-15)
                and math.isclose(p_s, 0.5, rel_tol=0.0, abs_tol=1e-15)
            )
            passed &= row_pass
            rows.append({"omega": omega, "tau": tau, "p_N": p_n, "p_S": p_s, "pass": row_pass})
    return {"rows": rows, "pass": passed}


def reparameterization_certificate() -> dict[str, object]:
    rows = []
    passed = True
    for omega, tau, scale in ((3.0, 2.0, 5.0), (-4.0, 1.5, 2.0), (0.75, 7.0, 0.25)):
        tau_prime = scale * tau
        omega_prime = omega / scale
        phase_a = omega * tau
        phase_b = omega_prime * tau_prime
        row_pass = math.isclose(phase_a, phase_b, rel_tol=0.0, abs_tol=1e-15)
        passed &= row_pass
        rows.append({
            "omega": omega,
            "tau": tau,
            "scale": scale,
            "omega_prime": omega_prime,
            "tau_prime": tau_prime,
            "phase_original": phase_a,
            "phase_rescaled": phase_b,
            "pass": row_pass,
        })
    return {"rows": rows, "pass": passed}


def kappa_rate_certificate() -> dict[str, object]:
    kappa = math.log(2.0) / (24.0 * math.pi)
    rows = []
    passed = True
    for f in (0.0, 1.0, 7.83, 12.0, 60.0):
        omega = 2.0 * math.pi * f
        gamma_a = kappa * omega
        gamma_b = (math.log(2.0) / 12.0) * f
        row_pass = math.isclose(gamma_a, gamma_b, rel_tol=1e-14, abs_tol=1e-15)
        passed &= row_pass
        rows.append({
            "f": f,
            "omega": omega,
            "Gamma_from_kappa_omega": gamma_a,
            "Gamma_closed": gamma_b,
            "pass": row_pass,
        })
    return {"kappa": kappa, "rows": rows, "pass": passed}


def build_receipt() -> dict[str, object]:
    blocks = {
        "rate_family_preserves_half_probabilities": rate_family_certificate(),
        "positive_parameter_rescaling_degeneracy": reparameterization_certificate(),
        "existing_kappa_rate_identity": kappa_rate_certificate(),
    }
    passed = all(block["pass"] for block in blocks.values())
    return {
        "schema": "TIR_HALF_FIBER_RATE_NO_GO_V0_1",
        "scope": "TIR_EXACT_CONDITIONAL_UNDERDETERMINATION_AUDIT",
        "result": "STATIC_HALF_FIBER_DOES_NOT_SELECT_UNIQUE_ABSOLUTE_PHASE_RATE",
        "free_coordinate": "omega",
        "crosslink_boundary": "temporal/dynamical normalization required for absolute rate",
        "next_gate": "DIMENSIONLESS_PHASE_RATE_RATIO_FROM_TIR_INVARIANTS",
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
