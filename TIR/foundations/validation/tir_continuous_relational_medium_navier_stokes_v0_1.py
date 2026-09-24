from __future__ import annotations

import json
import math

SCHEMA = "TIR_CONTINUOUS_RELATIONAL_MEDIUM_NAVIER_STOKES_VALIDATION_V0_1"


def hubble_continuity_control(H: float, rho: float) -> float:
    drho_dt = -3.0 * H * rho
    div_u = 3.0 * H
    return drho_dt + rho * div_u


def rigid_rotation_control(x: float, y: float, omega: float) -> dict[str, object]:
    adv = (-omega * omega * x, -omega * omega * y, 0.0)
    grad_pi = (omega * omega * x, omega * omega * y, 0.0)
    residual = tuple(a + p for a, p in zip(adv, grad_pi))
    return {
        "divergence": 0.0,
        "laplacian": (0.0, 0.0, 0.0),
        "vorticity": (0.0, 0.0, 2.0 * omega),
        "momentum_residual": residual,
    }


def validate() -> dict[str, object]:
    hubble_cases = [(0.1, 2.0), (-0.03, 5.0), (1.2, 0.7)]
    rigid_cases = [(1.0, 2.0, 0.5), (-3.0, 0.2, 2.0), (0.1, -0.4, 1.3)]

    hubble_residuals = [hubble_continuity_control(H, rho) for H, rho in hubble_cases]
    rigid = [rigid_rotation_control(x, y, omega) for x, y, omega in rigid_cases]

    tol = 1e-12
    hubble_pass = all(abs(value) <= tol for value in hubble_residuals)
    rigid_pass = all(
        abs(row["divergence"]) <= tol
        and all(abs(v) <= tol for v in row["laplacian"])
        and all(abs(v) <= tol for v in row["momentum_residual"])
        for row in rigid
    )

    return {
        "schema": SCHEMA,
        "status": "PASS_MATHEMATICAL_CONTROLS_ONLY" if hubble_pass and rigid_pass else "FAIL",
        "hubble_continuity": {
            "status": "PASS" if hubble_pass else "FAIL",
            "residuals": hubble_residuals,
        },
        "rigid_rotation_incompressible_ns": {
            "status": "PASS" if rigid_pass else "FAIL",
            "cases": rigid,
        },
        "physical_source_binding": "OPEN",
        "einstein_equals_navier_stokes_claim": False,
        "physical_material_fluid_claim": False,
        "canon_allowed": False,
    }


if __name__ == "__main__":
    print(json.dumps(validate(), indent=2, sort_keys=True))
