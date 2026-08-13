#!/usr/bin/env python3
"""
Collatz quarter-power mass-scaling audit v10.1.

Purpose
-------
Test a predeclared Collatz-derived quarter-power operator inside the existing
one-anchor / Ramanujan mass-scaling path without changing particle labels,
structural actions, seed pairs, or non-anchor validation masses.

The operator trace is frozen before validation masses are loaded:

    X_i = A_e / A_i
    Phi_alpha(X_i) = X_i ** alpha
    log(m_i / m_e) =
        [Phi_alpha(X_i) - 1] / (L3 * kappa)
        + [R_i - R_e] / kappa

where:
- A_i is the archived EB structural action (mass-free input),
- R_i is the archived mandatory Ramanujan release coordinate,
- kappa = ln(2)/(24*pi),
- L3 = 7,
- m_e is the sole observed mass anchor,
- all other masses are validation targets only.

The value alpha=3/4 is not fitted. It is fixed from the asymptotic geometric
mean of the accelerated odd Collatz multiplier. A post-hoc alpha scan is
reported separately and is explicitly barred from operator promotion.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path
from statistics import mean, median
from typing import Any, Dict, Iterable, List

REPO_ROOT = Path(__file__).resolve().parents[2]
ARCHIVE_ROOT = REPO_ROOT / "archive" / "v7.9" / "full"
OUT = Path(__file__).resolve().parent / "results"

EB_ACTION_CSV = (
    ARCHIVE_ROOT
    / "14_debt3_debt6_zeta_polar_eb_action_v1_6"
    / "results"
    / "charged_fermion_eb_action_debt6_v1_6.csv"
)
RAMANUJAN_CSV = (
    ARCHIVE_ROOT
    / "19_debt5_ramanujan_seed_suppression_v2_1"
    / "results"
    / "ramanujan_seed_suppression_table_v2_1.csv"
)
TARGET_CSV = (
    ARCHIVE_ROOT
    / "10_standard_model_derivation_stages"
    / "02_metatime_sm_mass_vectorization_v0_1"
    / "mass_action_validation_targets.csv"
)

KAPPA = math.log(2.0) / (24.0 * math.pi)
L3 = 7
ANCHOR = "e"
RESIDUE_BITS = 18

# Fixed comparators. These are declared before any target masses are read.
FIXED_EXPONENTS = {
    "SURFACE_2_OVER_3": 2.0 / 3.0,
    "COLLATZ_3_OVER_4": 3.0 / 4.0,
    "LINEAR_1": 1.0,
    "INVERSE_CLOSURE_4_OVER_3": 4.0 / 3.0,
}


def read_csv(path: Path) -> List[Dict[str, str]]:
    """
    Read a CSV file and return its rows as dictionaries keyed by column name.
    
    Parameters:
        path (Path): Path to the CSV file.
    
    Returns:
        List[Dict[str, str]]: The parsed CSV rows.
    
    Raises:
        FileNotFoundError: If the CSV file does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def pair_key(row: Dict[str, str]) -> str:
    """
    Build a seed-pair key from a row's numeric seed values.
    
    Parameters:
    	row (Dict[str, str]): A row containing `seed_p` and `seed_q` values.
    
    Returns:
    	str: The integer-formatted seed pair joined by a hyphen.
    """
    return f"{int(float(row['seed_p']))}-{int(float(row['seed_q']))}"


def v2(n: int) -> int:
    """
    Compute the exponent of 2 in the prime factorization of a positive integer.
    
    Parameters:
        n (int): The positive integer to evaluate.
    
    Returns:
        int: The number of times 2 divides `n`.
    
    Raises:
        ValueError: If `n` is less than or equal to zero.
    """
    if n <= 0:
        raise ValueError("v2 is defined here only for positive integers")
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return count


def collatz_residue_audit(bits: int = RESIDUE_BITS) -> Dict[str, float]:
    """
    Audit the 2-adic valuations of 3n + 1 for odd residues below 2**bits.
    
    Parameters:
        bits (int): Number of residue bits to enumerate; must be at least 4.
    
    Returns:
        Dict[str, float]: Audit statistics including the empirical and asymptotic
            scaling factors, their absolute error, the mean valuation, and the
            maximum observed valuation.
    """
    if bits < 4:
        raise ValueError("bits must be >= 4")
    valuations = [v2(3 * n + 1) for n in range(1, 2**bits, 2)]
    mean_a = mean(valuations)
    rho_empirical = math.exp(math.log(3.0) - mean_a * math.log(2.0))
    rho_asymptotic = 3.0 / 4.0
    return {
        "residue_bits": bits,
        "odd_residue_count": len(valuations),
        "mean_v2_3n_plus_1": mean_a,
        "rho_empirical": rho_empirical,
        "rho_asymptotic": rho_asymptotic,
        "absolute_rho_error": abs(rho_empirical - rho_asymptotic),
        "max_v2_seen": max(valuations),
    }


def structural_rows() -> List[Dict[str, Any]]:
    """
    Merge mass-free structural inputs from the archived action and Ramanujan tables.
    
    Returns:
    	List[Dict[str, Any]]: Structural records containing the fermion metadata,
    	seed pair, action values, and an indicator that observed mass was not used.
    
    Raises:
    	RuntimeError: If a seed pair has no matching Ramanujan record or the electron
    	structural anchor is missing.
    """
    eb_rows = read_csv(EB_ACTION_CSV)
    ram_rows = read_csv(RAMANUJAN_CSV)
    ram_by_pair = {pair_key(row): row for row in ram_rows}

    merged: List[Dict[str, Any]] = []
    for row in eb_rows:
        pair = pair_key(row)
        if pair not in ram_by_pair:
            raise RuntimeError(f"Missing Ramanujan row for seed pair {pair}")
        ram = ram_by_pair[pair]
        merged.append(
            {
                "fermion": row["fermion"],
                "class": row["class"],
                "generation": int(row["generation"]),
                "seed_pair": pair,
                "eb_action_kappa": float(row["eb_action_kappa_v16"]),
                "ramanujan_scaled_action": float(
                    ram["ramanujan_scaled_action"]
                ),
                "uses_observed_mass_as_operator_input": False,
            }
        )
    if not any(row["fermion"] == ANCHOR for row in merged):
        raise RuntimeError("Electron structural anchor row is missing")
    return merged


def freeze_operator_trace(rows: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Freeze fixed-exponent operator traces from mass-free structural rows.
    
    Parameters:
        rows (List[Dict[str, Any]]): Structural rows, including the anchor row.
    
    Returns:
        Dict[str, Any]: A SHA-256 fingerprint and the per-variant operator trace records.
    """
    anchor = next(row for row in rows if row["fermion"] == ANCHOR)
    a_anchor = anchor["eb_action_kappa"]
    r_anchor = anchor["ramanujan_scaled_action"]

    traces: List[Dict[str, Any]] = []
    for name, alpha in FIXED_EXPONENTS.items():
        for row in rows:
            inverse_action_ratio = a_anchor / row["eb_action_kappa"]
            scaled_coordinate = inverse_action_ratio**alpha
            ramanujan_release = row["ramanujan_scaled_action"] - r_anchor
            log_mass_ratio_trace = (
                (scaled_coordinate - 1.0) / (L3 * KAPPA)
                + ramanujan_release / KAPPA
            )
            traces.append(
                {
                    "variant": name,
                    "alpha": alpha,
                    "fermion": row["fermion"],
                    "class": row["class"],
                    "generation": row["generation"],
                    "seed_pair": row["seed_pair"],
                    "inverse_eb_action_ratio_Ae_over_Ai": (
                        inverse_action_ratio
                    ),
                    "scaled_coordinate": scaled_coordinate,
                    "ramanujan_release": ramanujan_release,
                    "log_mass_ratio_trace": log_mass_ratio_trace,
                    "observed_mass_used": False,
                }
            )

    fingerprint_material = {
        "kappa": KAPPA,
        "L3": L3,
        "anchor_slot": ANCHOR,
        "fixed_exponents": FIXED_EXPONENTS,
        "traces": traces,
    }
    fingerprint = hashlib.sha256(
        json.dumps(
            fingerprint_material,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()
    return {
        "operator_trace_sha256": fingerprint,
        "traces": traces,
    }


def class_order_pass(predictions: List[Dict[str, Any]], family: str) -> bool:
    """
    Determine whether predicted masses increase strictly by generation within a particle family.
    
    Parameters:
        predictions (List[Dict[str, Any]]): Prediction records containing class, generation, and predicted mass fields.
        family (str): Particle family to evaluate.
    
    Returns:
        bool: `true` if predicted masses strictly increase by generation, `false` otherwise.
    """
    rows = sorted(
        (row for row in predictions if row["class"] == family),
        key=lambda row: row["generation"],
    )
    masses = [row["mass_pred_GeV"] for row in rows]
    return all(masses[i] < masses[i + 1] for i in range(len(masses) - 1))


def summarize_variant(
    name: str,
    predictions: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    Summarize prediction errors and generation-order checks for an operator variant.
    
    Parameters:
    	name (str): Name of the operator variant.
    	predictions (List[Dict[str, Any]]): Prediction records, including anchor and non-anchor entries.
    
    Returns:
    	Dict[str, Any]: Error metrics and class-order validation results for the variant.
    """
    non_anchor = [row for row in predictions if not row["is_anchor"]]
    absolute_log_errors = [row["abs_log_error"] for row in non_anchor]
    return {
        "variant": name,
        "non_anchor_count": len(non_anchor),
        "mean_abs_log_error": mean(absolute_log_errors),
        "median_abs_log_error": median(absolute_log_errors),
        "max_abs_log_error": max(absolute_log_errors),
        "geometric_mean_multiplicative_error": math.exp(
            mean(absolute_log_errors)
        ),
        "charged_lepton_order_pass": class_order_pass(
            predictions, "charged_lepton"
        ),
        "down_quark_order_pass": class_order_pass(
            predictions, "down_quark"
        ),
        "up_quark_order_pass": class_order_pass(predictions, "up_quark"),
    }


def benchmark(frozen: Dict[str, Any]) -> Dict[str, Any]:
    """
    Benchmark fixed operator variants against validation masses and report diagnostic metrics and gating results.
    
    Parameters:
        frozen (Dict[str, Any]): Fingerprinted operator trace data containing per-fermion predictions.
    
    Returns:
        Dict[str, Any]: Validation predictions, per-variant summaries, post-hoc alpha diagnostics, and quarter-power gate results.
    
    Raises:
        RuntimeError: If the anchor mass or a mass required by an operator trace is missing.
    """
    target_rows = read_csv(TARGET_CSV)
    targets = {row["fermion"]: float(row["mass_GeV"]) for row in target_rows}
    if ANCHOR not in targets:
        raise RuntimeError("Electron mass anchor missing from target table")
    electron_mass = targets[ANCHOR]

    predictions_by_variant: Dict[str, List[Dict[str, Any]]] = {}
    for trace in frozen["traces"]:
        slot = trace["fermion"]
        if slot not in targets:
            raise RuntimeError(f"Missing validation mass for {slot}")
        mass_pred = electron_mass * math.exp(trace["log_mass_ratio_trace"])
        log_error = math.log(mass_pred / targets[slot])
        prediction = {
            **trace,
            "mass_pred_GeV": mass_pred,
            "target_mass_GeV_validation_only": targets[slot],
            "log_error": log_error,
            "abs_log_error": abs(log_error),
            "is_anchor": slot == ANCHOR,
            "observed_mass_used": slot == ANCHOR,
        }
        predictions_by_variant.setdefault(trace["variant"], []).append(
            prediction
        )

    summaries = {
        name: summarize_variant(name, rows)
        for name, rows in predictions_by_variant.items()
    }

    # Post-hoc diagnostic only. It uses validation masses and is tainted for
    # model selection; it may not replace the predeclared alpha=3/4 operator.
    scan_rows: List[Dict[str, float]] = []
    structural = structural_rows()
    anchor_struct = next(row for row in structural if row["fermion"] == ANCHOR)
    a_anchor = anchor_struct["eb_action_kappa"]
    r_anchor = anchor_struct["ramanujan_scaled_action"]
    for step in range(261):
        alpha = 0.2 + 0.005 * step
        errors: List[float] = []
        for row in structural:
            if row["fermion"] == ANCHOR:
                continue
            x = a_anchor / row["eb_action_kappa"]
            log_ratio = (
                (x**alpha - 1.0) / (L3 * KAPPA)
                + (row["ramanujan_scaled_action"] - r_anchor) / KAPPA
            )
            pred = electron_mass * math.exp(log_ratio)
            errors.append(abs(math.log(pred / targets[row["fermion"]])))
        scan_rows.append(
            {
                "alpha": alpha,
                "mean_abs_log_error": mean(errors),
                "median_abs_log_error": median(errors),
                "max_abs_log_error": max(errors),
            }
        )
    best_mean = min(scan_rows, key=lambda row: row["mean_abs_log_error"])

    quarter = summaries["COLLATZ_3_OVER_4"]
    comparator_rows = [
        summaries[name]
        for name in FIXED_EXPONENTS
        if name != "COLLATZ_3_OVER_4"
    ]
    quarter_beats_all_fixed = all(
        quarter["mean_abs_log_error"] < row["mean_abs_log_error"]
        and quarter["median_abs_log_error"] < row["median_abs_log_error"]
        and quarter["max_abs_log_error"] < row["max_abs_log_error"]
        for row in comparator_rows
    )
    all_order_pass = all(
        quarter[key]
        for key in (
            "charged_lepton_order_pass",
            "down_quark_order_pass",
            "up_quark_order_pass",
        )
    )

    # Physical closure is intentionally strict. A useful comparative signal
    # is not a successful particle-mass derivation.
    physical_closure_pass = (
        quarter["mean_abs_log_error"] < 0.10
        and quarter["max_abs_log_error"] < 0.20
    )

    return {
        "electron_mass_anchor_GeV": electron_mass,
        "non_anchor_validation_slots": sorted(
            slot for slot in targets if slot != ANCHOR
        ),
        "summaries": summaries,
        "predictions_by_variant": predictions_by_variant,
        "posthoc_alpha_scan": {
            "status": "DIAGNOSTIC_ONLY_TAINTED_FOR_MODEL_SELECTION",
            "range": [0.2, 1.5],
            "step": 0.005,
            "best_mean_abs_log_error": best_mean,
            "predeclared_alpha": 0.75,
        },
        "quarter_power_gate": {
            "beats_all_fixed_comparators_on_mean_median_and_max": (
                quarter_beats_all_fixed
            ),
            "all_generation_order_checks_pass": all_order_pass,
            "physical_closure_pass": physical_closure_pass,
            "promotion_to_canonical_mass_law": False,
            "status": (
                "COMPARATIVE_SIGNAL_PASS_PHYSICAL_FAIL"
                if quarter_beats_all_fixed
                and all_order_pass
                and not physical_closure_pass
                else "FAIL_NO_PROMOTION"
            ),
        },
    }


def flatten_predictions(
    predictions_by_variant: Dict[str, List[Dict[str, Any]]]
) -> Iterable[Dict[str, Any]]:
    """
    Yield prediction records for each fixed exponent variant.
    
    Parameters:
        predictions_by_variant (Dict[str, List[Dict[str, Any]]]): Prediction records grouped by variant name.
    
    Returns:
        Iterable[Dict[str, Any]]: Prediction records ordered by the variants in `FIXED_EXPONENTS`.
    """
    for variant in FIXED_EXPONENTS:
        yield from predictions_by_variant[variant]


def main() -> None:
    """
    Run the Collatz quarter-power mass-scaling audit and write its JSON and CSV reports.
    
    The audit evaluates the residue scaling, freezes mass-free operator traces, benchmarks
    the fixed exponent variants, and records status information without permitting
    promotion to a canonical mass law.
    """
    residue = collatz_residue_audit()
    structural = structural_rows()
    frozen = freeze_operator_trace(structural)
    benchmark_result = benchmark(frozen)

    residue_pass = residue["absolute_rho_error"] < 1.0e-4
    result = {
        "schema": "METATIME_COLLATZ_QUARTER_POWER_MASS_AUDIT_V10_1",
        "status": (
            "TECHNICAL_PASS_COMPARATIVE_SIGNAL_PHYSICAL_FAIL"
            if residue_pass
            and benchmark_result["quarter_power_gate"]["status"]
            == "COMPARATIVE_SIGNAL_PASS_PHYSICAL_FAIL"
            else "FAIL_NO_PROMOTION"
        ),
        "technical_status": "PASS" if residue_pass else "FAIL",
        "physical_status": "FAIL_OPEN_NOT_CLOSED",
        "canon_allowed": False,
        "current_promotion": "DENY_CURRENT",
        "mass_prediction_claimed": False,
        "operator_hypothesis": (
            "Apply the Collatz quarter-power to the inverse mass-free EB "
            "action ratio before the fixed L3/kappa release map."
        ),
        "logical_status": {
            "collatz_rho_3_over_4": (
                "DERIVED_AS_ASYMPTOTIC_GEOMETRIC_MEAN_MULTIPLIER"
            ),
            "rho_used_as_scaling_exponent": (
                "EXPLICIT_BRIDGE_HYPOTHESIS_NOT_A_THEOREM"
            ),
            "ramanujan_layer": "MANDATORY_FIXED_NON_FIT_TERM",
        },
        "collatz_residue_audit": residue,
        "operator_trace_sha256": frozen["operator_trace_sha256"],
        "fixed_exponents": FIXED_EXPONENTS,
        "benchmark": benchmark_result,
        "input_policy": {
            "operator_inputs": [
                str(EB_ACTION_CSV.relative_to(REPO_ROOT)),
                str(RAMANUJAN_CSV.relative_to(REPO_ROOT)),
            ],
            "single_observed_mass_anchor": ANCHOR,
            "validation_targets_only": str(TARGET_CSV.relative_to(REPO_ROOT)),
            "posthoc_alpha_scan_allowed_for_promotion": False,
        },
    }

    OUT.mkdir(parents=True, exist_ok=True)
    json_path = OUT / "collatz_quarter_power_mass_audit_v10_1.json"
    csv_path = OUT / "collatz_quarter_power_predictions_v10_1.csv"
    json_path.write_text(
        json.dumps(result, indent=2, sort_keys=True), encoding="utf-8"
    )

    rows = list(
        flatten_predictions(benchmark_result["predictions_by_variant"])
    )
    with csv_path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(
        json.dumps(
            {
                "status": result["status"],
                "technical_status": result["technical_status"],
                "physical_status": result["physical_status"],
                "rho_empirical": residue["rho_empirical"],
                "rho_asymptotic": residue["rho_asymptotic"],
                "operator_trace_sha256": frozen["operator_trace_sha256"],
                "quarter_power_gate": benchmark_result[
                    "quarter_power_gate"
                ],
                "summaries": benchmark_result["summaries"],
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
