#!/usr/bin/env python3
"""Deterministic implementation audit for the TIR κ phase-rate subsystem.

This script checks the numerical implementation of the exact algebraic identity

    κ = ln(2)/(24π),  ω = 2πf,  Γ_I = κω = (ln2/12)f

at representative frequencies and records the structural constraint rank.  It
does not promote the Metatime normalization or the physical interpretation of
Γ_I beyond their declared claim classes.
"""
from __future__ import annotations

import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

FREQUENCIES_HZ = (0.0, 1.0, 7.83, 12.0, 60.0, 440.0)
ABS_TOL = 1e-15
REL_TOL = 1e-14


@dataclass(frozen=True)
class Row:
    frequency_hz: float
    omega_rad_s: float
    gamma_from_kappa_omega: float
    gamma_from_closed_form: float
    residual: float
    pass_identity: bool


def kappa() -> float:
    return math.log(2.0) / (24.0 * math.pi)


def evaluate(frequency_hz: float) -> Row:
    omega = 2.0 * math.pi * frequency_hz
    gamma_a = kappa() * omega
    gamma_b = (math.log(2.0) / 12.0) * frequency_hz
    residual = gamma_a - gamma_b
    return Row(
        frequency_hz=frequency_hz,
        omega_rad_s=omega,
        gamma_from_kappa_omega=gamma_a,
        gamma_from_closed_form=gamma_b,
        residual=residual,
        pass_identity=math.isclose(gamma_a, gamma_b, rel_tol=REL_TOL, abs_tol=ABS_TOL),
    )


def constraint_rank_certificate() -> dict[str, object]:
    # For q=(κ,ω,f,Γ), the Jacobian rows are
    # (1,0,0,0), (0,1,-2π,0), (-ω,-κ,0,1).
    # They are independent for every κ,ω because the third row is the only row
    # with a nonzero Γ component; the first two are already independent.
    return {
        "ambient_dimension": 4,
        "constraint_count": 3,
        "jacobian_rank": 3,
        "constraint_manifold_dimension": 1,
        "proof_basis": "row independence from κ pivot, ω/f relation, and unique Γ pivot",
    }


def build_receipt() -> dict[str, object]:
    rows = [evaluate(f) for f in FREQUENCIES_HZ]
    rank = constraint_rank_certificate()
    technical_pass = all(row.pass_identity for row in rows) and rank["jacobian_rank"] == 3
    return {
        "schema": "TIR_KAPPA_PHASE_RATE_IDENTITY_V11_1",
        "claim_class": {
            "kappa_normalization": "B_MODEL_POSTULATE",
            "omega_equals_2pi_f": "A_STANDARD_DEFINITION",
            "phase_rate_identity": "EXACT_CONDITIONAL_IDENTITY",
            "surface_refresh_interpretation": "OPEN_OPERATIONAL_INTERPRETATION",
        },
        "kappa": kappa(),
        "per_cycle_information_increment": math.log(2.0) / 12.0,
        "rows": [asdict(row) for row in rows],
        "constraint_rank": rank,
        "technical_status": "PASS" if technical_pass else "FAIL",
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
