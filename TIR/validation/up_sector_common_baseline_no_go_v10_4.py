#!/usr/bin/env python3
"""Retrospective no-go audit for a common additive up-sector baseline.

This module does not propose a new mass formula. It proves a structural limit of
any extension of the form

    log(m_g / m_e) = B_up + Delta_up(g),  g in {u,c,t},

when the relative trace Delta_up(g) is held fixed at the v10.2 values. A common
B_up translates all logarithmic residuals by the same amount, so their pairwise
separations are invariant.

The audit is retrospective because the v10.2 validation masses and residuals
have already been inspected. It is not promotion-eligible.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path
from statistics import mean, median
from typing import Any, Dict, List

HERE = Path(__file__).resolve().parent
INPUT = HERE / "results" / "collatz_sector_holonomy_predictions_v10_2.csv"
OUT = HERE / "results"
UP_SLOTS = ("u", "c", "t")
REFERENCE_ENVELOPE = 0.254  # retrospective v10.2 non-u maximum |log error|


def read_rows(path: Path) -> List[Dict[str, str]]:
    """
    Read CSV records from a UTF-8-encoded file.
    
    Parameters:
    	path (Path): Path to the CSV file.
    
    Returns:
    	List[Dict[str, str]]: Rows represented as dictionaries keyed by CSV column names.
    """
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def residuals_from_v10_2() -> Dict[str, float]:
    """
    Load the v10.2 logarithmic residual for each required up-sector slot.
    
    Returns:
        Dict[str, float]: Mapping of up-sector slot names to their logarithmic residuals.
    
    Raises:
        RuntimeError: If a required up-sector slot is missing from the input data.
    """
    rows = read_rows(INPUT)
    by_slot = {row["fermion"]: row for row in rows}
    missing = [slot for slot in UP_SLOTS if slot not in by_slot]
    if missing:
        raise RuntimeError(f"Missing up-sector rows: {missing}")
    return {slot: float(by_slot[slot]["sector_log_error"]) for slot in UP_SLOTS}


def shifted_metrics(residuals: Dict[str, float], shift: float) -> Dict[str, Any]:
    """
    Compute absolute residual errors and aggregate multiplicative error metrics after applying a common logarithmic shift.
    
    Parameters:
        residuals (Dict[str, float]): Logarithmic residuals keyed by sector slot.
        shift (float): Common logarithmic shift applied to each residual.
    
    Returns:
        Dict[str, Any]: The applied shift, per-slot absolute logarithmic errors, and aggregate error metrics.
    """
    errors = {slot: abs(value + shift) for slot, value in residuals.items()}
    values = list(errors.values())
    return {
        "common_log_shift": shift,
        "absolute_log_errors": errors,
        "mean_absolute_log_error": mean(values),
        "median_absolute_log_error": median(values),
        "maximum_absolute_log_error": max(values),
        "geometric_mean_multiplicative_error": math.exp(mean(values)),
        "worst_case_multiplicative_error": math.exp(max(values)),
    }


def main() -> None:
    """Generate and persist the retrospective common-baseline no-go audit report."""
    residuals = residuals_from_v10_2()
    values = list(residuals.values())
    r_min = min(values)
    r_max = max(values)
    spread = r_max - r_min

    # Chebyshev/minimax translation of a finite set on the real line.
    minimax_shift = -(r_max + r_min) / 2.0
    minimax = shifted_metrics(residuals, minimax_shift)

    # Other translations are reported only as mathematical diagnostics.
    least_squares_shift = -mean(values)
    l1_shift = -median(values)

    # A common translation can put every residual inside [-eps,+eps] iff
    # max(r)-min(r) <= 2*eps. This is necessary and sufficient.
    minimum_uniform_tolerance = spread / 2.0
    reference_gate_possible = spread <= 2.0 * REFERENCE_ENVELOPE

    intervals = {
        slot: [
            -value - REFERENCE_ENVELOPE,
            -value + REFERENCE_ENVELOPE,
        ]
        for slot, value in residuals.items()
    }

    fingerprint_material = {
        "input_file": str(INPUT.relative_to(HERE.parent.parent)),
        "up_slots": UP_SLOTS,
        "residuals": residuals,
        "theorem": "common translation preserves pairwise residual differences",
        "reference_envelope": REFERENCE_ENVELOPE,
    }
    fingerprint = hashlib.sha256(
        json.dumps(fingerprint_material, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()

    result = {
        "schema": "TIR_UP_SECTOR_COMMON_BASELINE_NO_GO_V10_4",
        "module": "up_sector_common_baseline_no_go_v10_4",
        "methodological_status": "RETROSPECTIVE_MATHEMATICAL_NO_GO_AUDIT",
        "technical_status": "PASS",
        "substantive_status": "COMMON_ADDITIVE_BASELINE_CANNOT_CLOSE_V10_2_UP_SECTOR",
        "physical_mass_spectrum_status": "OPEN_NOT_CLOSED",
        "canon_allowed": False,
        "current_promotion": "DENY_CURRENT",
        "mass_derivation_claimed": False,
        "operator_fingerprint_sha256": fingerprint,
        "v10_2_up_sector_log_residuals": residuals,
        "residual_spread_invariant_under_common_shift": spread,
        "minimum_achievable_uniform_absolute_log_error": minimum_uniform_tolerance,
        "minimum_achievable_worst_case_multiplicative_error": math.exp(minimum_uniform_tolerance),
        "reference_non_u_envelope": REFERENCE_ENVELOPE,
        "reference_gate_possible_with_common_shift": reference_gate_possible,
        "reference_gate_shift_intervals": intervals,
        "minimax_common_shift": minimax,
        "least_squares_common_shift_diagnostic": shifted_metrics(residuals, least_squares_shift),
        "l1_common_shift_diagnostic": shifted_metrics(residuals, l1_shift),
        "theorem": {
            "statement": "For r'_g=r_g+B, all pairwise differences r'_g-r'_h equal r_g-r_h. A common B can satisfy |r'_g|<=epsilon for every g iff max(r)-min(r)<=2*epsilon.",
            "proof_class": "elementary translation invariance on the real line",
        },
        "conclusion": [
            "The v10.3 common-baseline-only architecture is insufficient for the fixed v10.2 relative trace.",
            "No choice of a single B_up can simultaneously retain the c/t absolute scale and remove the u offset.",
            "The next structural candidate must revise the up-sector relative architecture or derive a pre-existing light-up/heavy-up sector split; it may not introduce a u-specific residual correction.",
            "Any numerical comparison on the known charged-fermion table remains retrospective.",
        ],
    }

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "up_sector_common_baseline_no_go_v10_4.json").write_text(
        json.dumps(result, indent=2, sort_keys=True), encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
