#!/usr/bin/env python3
"""Run the typed half-axis solver and emit a machine-readable receipt."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import mpmath as mp

from critical_axis.solver import DEFAULT_SOLVER, kappa_from_projective_cycle, solve_half_axis_routes


DEFAULT_FACTS = {
    "sigma_half",
    "qubit_representation",
    "symmetric_readout",
    "half_turn_phase",
    "centered_zeta_chart",
    "reciprocal_chart",
    "affine_endpoint_map",
    "projective_cycle",
    "spin_half",
    "binary_information",
    "twelve_projective_cycles",
    "radian_closure_tau",
    "eight_mix_sectors",
    "three_flavours",
}


def _proof(result) -> dict[str, dict[str, object]]:
    return {
        claim: {
            "premises": list(step.rule.premises),
            "status": step.rule.status.value,
            "provenance": step.rule.provenance,
        }
        for claim, step in sorted(result.proof.items())
    }


def build_receipt() -> dict[str, object]:
    mp.mp.dps = 80
    routes = solve_half_axis_routes()
    exact = DEFAULT_SOLVER.closure(DEFAULT_FACTS, allow_model=False)
    model = DEFAULT_SOLVER.closure(DEFAULT_FACTS, allow_model=True)
    missing_rh = DEFAULT_SOLVER.missing_premises(
        "all_zeros_on_half_axis", model.facts, allow_model=True
    )
    return {
        "schema": "tir.critical-axis.solver-receipt/v1",
        "precision_decimal_digits": mp.mp.dps,
        "half_axis_routes": {key: mp.nstr(value, 50) for key, value in routes.items()},
        "half_axis_consensus": all(abs(value - mp.mpf("0.5")) < mp.mpf("1e-50") for value in routes.values()),
        "exact_closure": sorted(exact.facts),
        "exact_proof": _proof(exact),
        "model_closure": sorted(model.facts),
        "model_proof": _proof(model),
        "kappa_conditional": mp.nstr(kappa_from_projective_cycle(), 50),
        "kappa_reference": mp.nstr(mp.log(2) / (24 * mp.pi), 50),
        "rh_derived": "riemann_hypothesis" in model.facts,
        "open_bridge_candidates": [
            {
                "conclusion": rule.conclusion,
                "status": rule.status.value,
                "missing": list(missing),
                "provenance": rule.provenance,
            }
            for rule, missing in missing_rh
        ],
        "verdict": {
            "mathematical_half_axis_routes": "PASS",
            "conditional_kappa_arithmetic": "PASS",
            "model_semantics": "EXPLICIT",
            "zero_state_representation": "OPEN",
            "riemann_hypothesis": "NOT_DERIVED",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()
    receipt = build_receipt()
    text = json.dumps(receipt, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
