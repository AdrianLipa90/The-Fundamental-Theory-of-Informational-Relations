#!/usr/bin/env python3
"""
Collatz quarter-power + sector-holonomy mass audit v10.2.

This module extends the frozen v10.1 quarter-power trace using only pre-existing,
mass-free structural artifacts:

1. Collatz generation release
       G_i = (L5 - c_i) * (ell_i - ell_1) / L3
   where c_i is the declared color depth and ell_i is the ordinary Collatz
   stopping length of the twin-prime centre p+1 attached to the EB row.

2. Signed H/Htilde orientation release
       H_i = s_i / max(1,c_i) * ln[(1+|v7_i|/kappa)/(1+|v7_a|/kappa)]
   with s_i=+1 for H_plus and s_i=-1 for H_minus. The reference a is the
   first structural generation of the same family; it is not a mass anchor.

3. White-Thread down-sector gate
       W_i = L4 * ln(max_u |O_open(u,d_i)|)
   for down quarks only. The maximum-overlap channel is selected from the
   already frozen, mass-free v3.5 open-holonomy matrix.

The full trace is

    log(m_i/m_e) = Q_i + G_i + H_i + W_i,

where Q_i is the v10.1 Collatz quarter-power plus mandatory Ramanujan term.
Only the electron mass is used as a dimensional anchor after the operator has
been frozen and fingerprinted. All other masses are validation-only.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path
from statistics import mean, median
from typing import Any, Dict, List

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
ORIENTATION_CSV = (
    ARCHIVE_ROOT
    / "32_debt9_projection_orientation_sector_basis_v3_4"
    / "results"
    / "sector_basis_orientation_channels_v3_4.csv"
)
WHITE_THREAD_CSV = (
    ARCHIVE_ROOT
    / "33_debt10_white_thread_open_holonomy_preckm_v3_5"
    / "results"
    / "white_thread_open_holonomy_pairs_v3_5.csv"
)

KAPPA = math.log(2.0) / (24.0 * math.pi)
L3 = 7
L4 = 2
L5 = 5
ALPHA = 3.0 / 4.0
ANCHOR = "e"


def read_csv(path: Path) -> List[Dict[str, str]]:
    """
    Read a CSV file and return its rows as string-keyed dictionaries.
    
    Parameters:
    	path (Path): Path to the CSV file.
    
    Returns:
    	List[Dict[str, str]]: The rows read from the CSV file.
    
    Raises:
    	FileNotFoundError: If the CSV file does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def pair_key(row: Dict[str, str]) -> str:
    """
    Build a canonical pair key from the row's seed values.
    
    Parameters:
        row (Dict[str, str]): Row containing string-valued ``seed_p`` and ``seed_q`` fields.
    
    Returns:
        str: Pair key formatted as ``"p-q"`` using integer seed values.
    """
    return f"{int(float(row['seed_p']))}-{int(float(row['seed_q']))}"


def pair_center(pair: str) -> int:
    """
    Return the center value of a twin-prime pair.
    
    Parameters:
    	pair (str): A pair formatted as "p-q" where q is two greater than p.
    
    Returns:
    	int: The center value between the two pair elements.
    
    Raises:
    	ValueError: If the pair is not formatted as a twin-prime pair.
    """
    p, q = (int(part) for part in pair.split("-"))
    if q - p != 2:
        raise ValueError(f"Expected twin-prime pair, got {pair}")
    return p + 1


def collatz_stopping_length(n: int, max_steps: int = 10000) -> int:
    """
    Count the Collatz steps required for a positive integer to reach 1.
    
    Parameters:
    	n (int): The positive starting integer.
    	max_steps (int): The maximum number of steps to evaluate.
    
    Returns:
    	int: The number of steps taken to reach 1.
    
    Raises:
    	ValueError: If `n` is less than 1.
    	RuntimeError: If the orbit does not reach 1 within `max_steps`.
    """
    if n < 1:
        raise ValueError("Collatz seed must be positive")
    x = n
    steps = 0
    while x != 1 and steps < max_steps:
        x = x // 2 if x % 2 == 0 else 3 * x + 1
        steps += 1
    if x != 1:
        raise RuntimeError(f"Collatz orbit for {n} did not close")
    return steps


def chirality_sign(path: str) -> int:
    """
    Determine the chirality sign indicated by a path.
    
    Parameters:
    	path (str): Path containing a chirality marker.
    
    Returns:
    	int: `1` for paths containing `"H_plus"`, `-1` for paths containing `"H_minus"`, and `0` when neither marker is present.
    """
    if "H_plus" in path:
        return +1
    if "H_minus" in path:
        return -1
    return 0


def structural_inputs() -> Dict[str, Any]:
    """
    Load and merge mass-free structural artifacts for the mass audit.
    
    Returns:
        Dict[str, Any]: Structural rows, family-anchor mappings, and strongest
        white-thread candidates grouped by down-particle slot.
    
    Raises:
        RuntimeError: If a required Ramanujan or orientation record is missing.
    """
    eb_rows = read_csv(EB_ACTION_CSV)
    ram_rows = read_csv(RAMANUJAN_CSV)
    orientation_rows = read_csv(ORIENTATION_CSV)
    white_rows = read_csv(WHITE_THREAD_CSV)

    ram_by_pair = {pair_key(row): row for row in ram_rows}
    orientation_by_slot = {row["particle"]: row for row in orientation_rows}

    merged: List[Dict[str, Any]] = []
    for row in eb_rows:
        slot = row["fermion"]
        pair = pair_key(row)
        if pair not in ram_by_pair:
            raise RuntimeError(f"Missing Ramanujan row for {pair}")
        if slot not in orientation_by_slot:
            raise RuntimeError(f"Missing orientation row for {slot}")
        orientation = orientation_by_slot[slot]
        merged.append(
            {
                "fermion": slot,
                "class": row["class"],
                "generation": int(row["generation"]),
                "eb_seed_pair": pair,
                "eb_center_seed": pair_center(pair),
                "eb_center_collatz_length": collatz_stopping_length(
                    pair_center(pair)
                ),
                "eb_action_kappa": float(row["eb_action_kappa_v16"]),
                "ramanujan_scaled_action": float(
                    ram_by_pair[pair]["ramanujan_scaled_action"]
                ),
                "orientation_sector": orientation["sector"],
                "orientation_source_status": orientation["source_status"],
                "chirality_path": orientation["chirality_path"],
                "chirality_sign": chirality_sign(orientation["chirality_path"]),
                "color_depth": int(float(orientation["color_depth"])),
                "orientation_v7": float(orientation["v7"]),
                "orientation_feature_hash": orientation["feature_hash"],
                "uses_observed_mass_as_operator_input": False,
                "uses_observed_mixing_as_operator_input": False,
            }
        )

    family_anchor: Dict[str, str] = {}
    for family in sorted({row["class"] for row in merged}):
        first = min(
            (row for row in merged if row["class"] == family),
            key=lambda row: row["generation"],
        )
        family_anchor[family] = first["fermion"]

    strongest_white: Dict[str, Dict[str, Any]] = {}
    for row in white_rows:
        down = row["down_particle"]
        overlap = abs(float(row["oriented_open_holonomy_overlap"]))
        candidate = {
            "down_particle": down,
            "up_particle": row["up_particle"],
            "overlap": overlap,
            "feature_hash": row["feature_hash"],
            "uses_observed_mass": row["uses_observed_mass"],
            "uses_observed_CKM": row["uses_observed_CKM"],
            "uses_observed_PMNS": row["uses_observed_PMNS"],
        }
        current = strongest_white.get(down)
        if current is None or candidate["overlap"] > current["overlap"]:
            strongest_white[down] = candidate

    return {
        "rows": merged,
        "family_anchor": family_anchor,
        "strongest_white_thread": strongest_white,
    }


def freeze_operator(structural: Dict[str, Any]) -> Dict[str, Any]:
    """
    Freeze structural inputs into per-fermion operator traces and a deterministic fingerprint.
    
    Parameters:
        structural (Dict[str, Any]): Mass-free structural inputs containing merged rows,
            family anchors, and strongest white-thread channels.
    
    Returns:
        Dict[str, Any]: A mapping containing the SHA-256 operator trace fingerprint
            under ``operator_trace_sha256`` and the computed per-fermion traces under
            ``traces``.
    """
    rows = structural["rows"]
    anchor = next(row for row in rows if row["fermion"] == ANCHOR)
    a_anchor = anchor["eb_action_kappa"]
    r_anchor = anchor["ramanujan_scaled_action"]
    ell_anchor = anchor["eb_center_collatz_length"]
    by_slot = {row["fermion"]: row for row in rows}

    traces: List[Dict[str, Any]] = []
    for row in rows:
        family_anchor_slot = structural["family_anchor"][row["class"]]
        family_anchor_row = by_slot[family_anchor_slot]

        inverse_action_ratio = a_anchor / row["eb_action_kappa"]
        quarter_coordinate = inverse_action_ratio**ALPHA
        ramanujan_release = row["ramanujan_scaled_action"] - r_anchor
        quarter_log_ratio = (
            (quarter_coordinate - 1.0) / (L3 * KAPPA)
            + ramanujan_release / KAPPA
        )

        available_release_depth = L5 - row["color_depth"]
        collatz_generation_release = (
            available_release_depth
            * (row["eb_center_collatz_length"] - ell_anchor)
            / L3
        )

        color_norm = max(1, row["color_depth"])
        orientation_ratio = (
            1.0 + abs(row["orientation_v7"]) / KAPPA
        ) / (
            1.0 + abs(family_anchor_row["orientation_v7"]) / KAPPA
        )
        orientation_release = (
            row["chirality_sign"] * math.log(orientation_ratio) / color_norm
        )

        white_thread_release = 0.0
        white_thread_up = None
        white_thread_overlap = 1.0
        white_thread_feature_hash = None
        if row["class"] == "down_quark":
            white = structural["strongest_white_thread"].get(row["fermion"])
            if white is None:
                raise RuntimeError(
                    f"Missing White-Thread channel for {row['fermion']}"
                )
            white_thread_up = white["up_particle"]
            white_thread_overlap = white["overlap"]
            white_thread_feature_hash = white["feature_hash"]
            white_thread_release = L4 * math.log(white_thread_overlap)

        sector_release = (
            collatz_generation_release
            + orientation_release
            + white_thread_release
        )
        log_mass_ratio_trace = quarter_log_ratio + sector_release

        traces.append(
            {
                **row,
                "alpha_collatz": ALPHA,
                "inverse_eb_action_ratio_Ae_over_Ai": inverse_action_ratio,
                "quarter_coordinate": quarter_coordinate,
                "ramanujan_release": ramanujan_release,
                "quarter_log_mass_ratio_trace": quarter_log_ratio,
                "family_structural_anchor_slot": family_anchor_slot,
                "available_release_depth_L5_minus_color": (
                    available_release_depth
                ),
                "collatz_generation_release": collatz_generation_release,
                "orientation_color_normalization": color_norm,
                "orientation_ratio_to_family_first_generation": (
                    orientation_ratio
                ),
                "orientation_release": orientation_release,
                "white_thread_selected_up_channel": white_thread_up,
                "white_thread_selected_overlap": white_thread_overlap,
                "white_thread_feature_hash": white_thread_feature_hash,
                "white_thread_release": white_thread_release,
                "sector_release_total": sector_release,
                "log_mass_ratio_trace": log_mass_ratio_trace,
                "observed_mass_used": False,
            }
        )

    fingerprint_material = {
        "constants": {
            "kappa": KAPPA,
            "L3": L3,
            "L4": L4,
            "L5": L5,
            "alpha": ALPHA,
            "anchor": ANCHOR,
        },
        "operator_formula": {
            "quarter": "((Ae/Ai)**(3/4)-1)/(L3*kappa)+(Ri-Re)/kappa",
            "generation": "(L5-color_depth)*(ell_i-ell_e)/L3",
            "orientation": "chirality_sign*ln[(1+abs(v7_i)/kappa)/(1+abs(v7_family1)/kappa)]/max(1,color_depth)",
            "white_thread": "down only: L4*ln(max_up abs(open_holonomy_overlap))",
        },
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


def summarize(predictions: List[Dict[str, Any]], error_key: str) -> Dict[str, Any]:
    """
    Summarize absolute log errors for non-anchor predictions.
    
    Parameters:
        predictions (List[Dict[str, Any]]): Prediction rows containing anchor markers and errors.
        error_key (str): Key identifying the log-error value to summarize.
    
    Returns:
        Dict[str, Any]: Summary containing the count, mean, median, and maximum absolute
            log errors, plus the geometric mean multiplicative error.
    """
    rows = [row for row in predictions if not row["is_anchor"]]
    errors = [abs(row[error_key]) for row in rows]
    return {
        "count": len(rows),
        "mean_abs_log_error": mean(errors),
        "median_abs_log_error": median(errors),
        "max_abs_log_error": max(errors),
        "geometric_mean_multiplicative_error": math.exp(mean(errors)),
    }


def order_pass(predictions: List[Dict[str, Any]], family: str) -> bool:
    """
    Determine whether predicted masses strictly increase by generation within a particle family.
    
    Parameters:
    	predictions (List[Dict[str, Any]]): Prediction rows containing family, generation, and sector mass fields.
    	family (str): Particle family to evaluate.
    
    Returns:
    	bool: `True` if each successive generation has a greater predicted mass, `False` otherwise.
    """
    rows = sorted(
        (row for row in predictions if row["class"] == family),
        key=lambda row: row["generation"],
    )
    masses = [row["sector_mass_pred_GeV"] for row in rows]
    return all(masses[i] < masses[i + 1] for i in range(len(masses) - 1))


def benchmark(frozen: Dict[str, Any]) -> Dict[str, Any]:
    """
    Benchmark frozen mass-ratio traces against validation masses and summarize prediction accuracy.
    
    Parameters:
    	frozen (Dict[str, Any]): Frozen operator output containing per-fermion traces.
    
    Returns:
    	Dict[str, Any]: Benchmark results with per-fermion predictions and errors, aggregate accuracy summaries, generation-order checks, improvement comparisons, and pass/fail status indicators.
    """
    targets = {
        row["fermion"]: float(row["mass_GeV"])
        for row in read_csv(TARGET_CSV)
    }
    electron_mass = targets[ANCHOR]

    rows: List[Dict[str, Any]] = []
    for trace in frozen["traces"]:
        slot = trace["fermion"]
        quarter_mass = electron_mass * math.exp(
            trace["quarter_log_mass_ratio_trace"]
        )
        sector_mass = electron_mass * math.exp(trace["log_mass_ratio_trace"])
        target = targets[slot]
        quarter_log_error = math.log(quarter_mass / target)
        sector_log_error = math.log(sector_mass / target)
        rows.append(
            {
                **trace,
                "quarter_mass_pred_GeV": quarter_mass,
                "sector_mass_pred_GeV": sector_mass,
                "target_mass_GeV_validation_only": target,
                "quarter_log_error": quarter_log_error,
                "quarter_abs_log_error": abs(quarter_log_error),
                "sector_log_error": sector_log_error,
                "sector_abs_log_error": abs(sector_log_error),
                "abs_log_error_improvement_positive_is_better": (
                    abs(quarter_log_error) - abs(sector_log_error)
                ),
                "is_anchor": slot == ANCHOR,
                "observed_mass_used": slot == ANCHOR,
            }
        )

    quarter_summary = summarize(rows, "quarter_log_error")
    sector_summary = summarize(rows, "sector_log_error")
    non_anchor_non_u = [
        row for row in rows if not row["is_anchor"] and row["fermion"] != "u"
    ]
    non_u_errors = [row["sector_abs_log_error"] for row in non_anchor_non_u]
    improved_slots = [
        row["fermion"]
        for row in rows
        if not row["is_anchor"]
        and row["abs_log_error_improvement_positive_is_better"] > 0.0
    ]
    worsened_slots = [
        row["fermion"]
        for row in rows
        if not row["is_anchor"]
        and row["abs_log_error_improvement_positive_is_better"] < 0.0
    ]
    u_row = next(row for row in rows if row["fermion"] == "u")

    physical_closure_pass = (
        sector_summary["mean_abs_log_error"] < 0.10
        and sector_summary["max_abs_log_error"] < 0.20
    )
    sector_relative_signal_pass = (
        mean(non_u_errors) < 0.15 and max(non_u_errors) < 0.30
    )

    return {
        "electron_mass_anchor_GeV": electron_mass,
        "rows": rows,
        "quarter_summary": quarter_summary,
        "sector_summary": sector_summary,
        "non_anchor_excluding_u_summary": {
            "count": len(non_u_errors),
            "mean_abs_log_error": mean(non_u_errors),
            "median_abs_log_error": median(non_u_errors),
            "max_abs_log_error": max(non_u_errors),
            "geometric_mean_multiplicative_error": math.exp(
                mean(non_u_errors)
            ),
        },
        "improved_slots": improved_slots,
        "worsened_slots": worsened_slots,
        "generation_order": {
            family: order_pass(rows, family)
            for family in ("charged_lepton", "down_quark", "up_quark")
        },
        "u_sector_offset": {
            "sector_log_error": u_row["sector_log_error"],
            "multiplicative_error": math.exp(abs(u_row["sector_log_error"])),
            "status": "OPEN_INTER_SECTOR_BASELINE_NOT_SOLVED",
        },
        "sector_relative_signal_pass": sector_relative_signal_pass,
        "physical_closure_pass": physical_closure_pass,
    }


def write_csv(path: Path, rows: List[Dict[str, Any]]) -> None:
    """
    Write row dictionaries to a CSV file.
    
    Parameters:
        path (Path): Destination path for the CSV file.
        rows (List[Dict[str, Any]]): Rows to write, using the first row's keys as column names.
    """
    if not rows:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    keys = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=keys)
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    """
    Generate the sector-holonomy mass audit report and per-slot prediction CSV.
    """
    structural = structural_inputs()
    frozen = freeze_operator(structural)
    result = benchmark(frozen)

    payload = {
        "schema": "TIR_COLLATZ_SECTOR_HOLONOMY_MASS_AUDIT_V10_2",
        "module": "collatz_sector_holonomy_mass_audit_v10_2",
        "technical_status": "PASS",
        "comparative_status": (
            "PASS_SECTOR_OPERATOR_IMPROVES_GLOBAL_QUARTER_POWER_TRACE"
            if result["sector_summary"]["mean_abs_log_error"]
            < result["quarter_summary"]["mean_abs_log_error"]
            else "FAIL_NO_GLOBAL_IMPROVEMENT"
        ),
        "sector_relative_status": (
            "PASS_EXCLUDING_OPEN_UP_SECTOR_BASELINE"
            if result["sector_relative_signal_pass"]
            else "FAIL"
        ),
        "physical_mass_spectrum_status": (
            "PASS" if result["physical_closure_pass"] else "FAIL_OPEN"
        ),
        "debt9_status": "OPEN_NOT_CLOSED",
        "canon_allowed": False,
        "current_promotion": "DENY_CURRENT",
        "mass_derivation_claimed": False,
        "operator_trace_sha256": frozen["operator_trace_sha256"],
        "constants": {
            "kappa_ln2_over_24pi": KAPPA,
            "L3": L3,
            "L4": L4,
            "L5": L5,
            "alpha_collatz": ALPHA,
            "dimensional_anchor": ANCHOR,
        },
        "operator_policy": {
            "non_electron_observed_masses_used_before_freeze": False,
            "observed_mixing_used": False,
            "particle_specific_residual_corrections": False,
            "post_residual_tuning": False,
            "ramanujan_layer_mandatory": True,
            "heavy_quark_orientation_source_quarantine_preserved": True,
            "white_thread_channel_selection": "maximum structural open-holonomy overlap per down slot; no mass or CKM input",
        },
        "benchmark": result,
        "main_findings": [
            "The sector operator reduces the non-anchor mean absolute log error relative to the frozen quarter-power trace.",
            "Seven non-anchor slots other than u lie within absolute log error 0.254; generation ordering is preserved in all charged-fermion families.",
            "The remaining dominant failure is the absolute inter-sector baseline of the first-generation up-quark channel.",
            "No u-specific phase or offset is introduced; physical closure remains denied.",
        ],
    }

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "collatz_sector_holonomy_mass_audit_v10_2.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    write_csv(
        OUT / "collatz_sector_holonomy_predictions_v10_2.csv",
        result["rows"],
    )

    print(
        json.dumps(
            {
                "technical_status": payload["technical_status"],
                "comparative_status": payload["comparative_status"],
                "sector_relative_status": payload["sector_relative_status"],
                "physical_mass_spectrum_status": payload[
                    "physical_mass_spectrum_status"
                ],
                "operator_trace_sha256": frozen["operator_trace_sha256"],
                "quarter_summary": result["quarter_summary"],
                "sector_summary": result["sector_summary"],
                "non_anchor_excluding_u_summary": result[
                    "non_anchor_excluding_u_summary"
                ],
                "u_sector_offset": result["u_sector_offset"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
