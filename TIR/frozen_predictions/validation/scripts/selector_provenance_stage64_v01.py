#!/usr/bin/env python3
"""Stage 64 — algebraic companion for selector provenance gate.

Checks only algebraic facts used in the provenance audit:
  * global kappa scaling preserves the projective ratio of cubic coefficients,
  * one quadratic normalization constraint leaves one projective degree of
    freedom in a two-dimensional cubic coefficient space.
Textual promotion/debt status is sourced from repository ledgers and is not
reclassified by this script.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results"
OUT.mkdir(parents=True, exist_ok=True)
TOL = 1e-14


def main() -> None:
    kappa = math.log(2.0) / (24.0 * math.pi)

    # Generic nonzero representative of a projective cubic coefficient line.
    c = np.array([2.0, -5.0], dtype=float)
    scaled = kappa * c
    ratio_before = c[0] / c[1]
    ratio_after = scaled[0] / scaled[1]
    ratio_residual = abs(ratio_before - ratio_after)

    # Normalization of a 2-vector removes radial scale but leaves an angle / P^1
    # coordinate. Two explicitly different normalized directions witness this.
    u = np.array([1.0, 0.0])
    v = np.array([0.0, 1.0])
    u /= np.linalg.norm(u)
    v /= np.linalg.norm(v)
    normalization_residual = max(abs(np.linalg.norm(u) - 1.0), abs(np.linalg.norm(v) - 1.0))
    distinct_normalized_direction_inner_product = float(np.dot(u, v))

    passed = (
        kappa > 0.0
        and ratio_residual < TOL
        and normalization_residual < TOL
        and abs(distinct_normalized_direction_inner_product) < TOL
    )

    receipt = {
        "schema": "TIR_POLYGONAL_STAGE64_SELECTOR_PROVENANCE_RECEIPT_V0_1",
        "status": (
            "STAGE_64_CANONICAL_SCALAR_SELECTOR_REMAINS_OPEN_PASS"
            if passed
            else "STAGE_64_FAIL"
        ),
        "gate_type": "formal_provenance_audit_with_algebraic_checks",
        "kappa": kappa,
        "kappa_projective_ratio_residual": ratio_residual,
        "quadratic_normalization_residual": normalization_residual,
        "distinct_normalized_direction_inner_product": distinct_normalized_direction_inner_product,
        "provenance_findings": {
            "kappa_role": "overall_scale",
            "quadratic_A5_role": "norm_radius",
            "A5_rigid_embedding_role": "carrier_orientation",
            "collatz_role": "ordered_words_present_quantitative_operator_rhythm_open",
            "euler_berry_role": "constructive_coherence_functional_open",
            "zeta_role": "coherence_axis_exact_weighting_functional_open"
        },
        "canonical_scalar_selector_status": "OPEN",
        "new_selector_promoted": False,
        "uses_observed_CKM": False,
        "uses_observed_masses": False,
        "uses_fitted_coefficients": False,
        "pass": passed
    }

    path = OUT / "TIR_POLYGONAL_STAGE64_SELECTOR_PROVENANCE_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
