#!/usr/bin/env python3
"""Prospective-observable identifiability audit v10.6.

This module refines the v10.5 architecture freeze.  It proves that a
sector-invariant baseline common to charm and top cancels from y_c/y_t, so the
charm-to-top ratio can test only a generation-varying relative-release
operator.  A cross-sector charm-to-tau ratio is therefore frozen for the
sector-baseline candidate class.

No observed Higgs-coupling likelihood is loaded.  No new mass formula is
selected.  The v10.2 charm-to-top structural prediction is merely frozen for a
future independent likelihood.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
from pathlib import Path
from typing import Any, Dict, List

REPO_ROOT = Path(__file__).resolve().parents[2]
ARCHIVE_ROOT = REPO_ROOT / "archive" / "v7.9" / "full"
OUT = Path(__file__).resolve().parent / "results"

ORIENTATION_CSV = (
    ARCHIVE_ROOT
    / "32_debt9_projection_orientation_sector_basis_v3_4"
    / "results"
    / "sector_basis_orientation_channels_v3_4.csv"
)
V10_2_PREDICTIONS = (
    Path(__file__).resolve().parent
    / "results"
    / "collatz_sector_holonomy_predictions_v10_2.csv"
)


def read_csv(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def canonical_sha256(obj: Any) -> str:
    encoded = json.dumps(
        obj,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def main() -> None:
    orientation = {row["particle"]: row for row in read_csv(ORIENTATION_CSV)}
    predictions = {
        row["fermion"]: row for row in read_csv(V10_2_PREDICTIONS)
    }

    required = {"c", "t", "tau"}
    missing_orientation = required - orientation.keys()
    missing_predictions = {"c", "t"} - predictions.keys()
    if missing_orientation:
        raise RuntimeError(
            f"Missing orientation rows: {sorted(missing_orientation)}"
        )
    if missing_predictions:
        raise RuntimeError(
            f"Missing v10.2 prediction rows: {sorted(missing_predictions)}"
        )

    c_sector = orientation["c"]["sector"]
    t_sector = orientation["t"]["sector"]
    tau_sector = orientation["tau"]["sector"]

    c_log = float(predictions["c"]["log_mass_ratio_trace"])
    t_log = float(predictions["t"]["log_mass_ratio_trace"])
    frozen_ct_ratio = math.exp(c_log - t_log)

    same_ct_sector = c_sector == t_sector
    tau_is_cross_sector = tau_sector != c_sector
    if not same_ct_sector:
        raise RuntimeError(
            "v10.6 theorem requires c and t to share the declared sector"
        )
    if not tau_is_cross_sector:
        raise RuntimeError(
            "v10.6 cross-sector observable requires tau to differ from c"
        )

    fingerprint_material = {
        "architecture_rule": {
            "class_A": "sector_invariant_baseline_only",
            "class_B": "generation_varying_relative_release_only",
        },
        "sector_labels": {
            "c": c_sector,
            "t": t_sector,
            "tau": tau_sector,
        },
        "prospective_observables": {
            "class_A": "direct_charm_to_tau_Higgs_coupling_ratio",
            "class_B": "direct_charm_to_top_Higgs_coupling_ratio",
        },
        "v10_2_frozen_ct_prediction": frozen_ct_ratio,
    }
    fingerprint = canonical_sha256(fingerprint_material)

    payload = {
        "schema": "TIR_UP_SECTOR_OBSERVABLE_IDENTIFIABILITY_V10_6",
        "module": "up_sector_observable_identifiability_v10_6",
        "technical_status": "PASS",
        "methodological_status": "ARCHITECTURE_AND_OBSERVABLE_MAPPING_CORRECTION",
        "formula_selected": False,
        "mass_benchmark_performed": False,
        "observed_higgs_likelihood_loaded": False,
        "debt9_status": "OPEN_NOT_CLOSED",
        "canon_allowed": False,
        "current_promotion": "DENY_CURRENT",
        "operator_fingerprint_sha256": fingerprint,
        "sector_labels": {
            "c": c_sector,
            "t": t_sector,
            "tau": tau_sector,
        },
        "theorem": {
            "statement": (
                "For a sector-invariant baseline B_s with s(c)=s(t), "
                "log(y_c/y_t)=[B_s+Delta_c]-[B_s+Delta_t]="
                "Delta_c-Delta_t; therefore y_c/y_t is insensitive to B_s."
            ),
            "c_and_t_share_sector": same_ct_sector,
            "tau_is_cross_sector_from_c": tau_is_cross_sector,
        },
        "architecture_refinement": {
            "class_A": {
                "name": "SECTOR_INVARIANT_BASELINE",
                "rule": (
                    "May use only coordinates invariant across generations "
                    "inside a declared sector. Generation-varying coordinates "
                    "must be assigned to class B."
                ),
                "primary_prospective_observable": (
                    "first qualifying post-2026-07-28 joint ATLAS/CMS "
                    "direct charm-to-tau Higgs-coupling likelihood"
                ),
                "reason": (
                    "c and tau occupy different declared sectors, so a "
                    "sector baseline does not cancel from y_c/y_tau."
                ),
            },
            "class_B": {
                "name": "UNIVERSAL_GENERATION_RELEASE",
                "rule": (
                    "May use generation-varying structural coordinates, but "
                    "the same algebraic operator must be applied across all "
                    "charged-fermion families."
                ),
                "primary_prospective_observable": (
                    "first qualifying post-2026-07-28 joint ATLAS/CMS "
                    "direct charm-to-top Higgs-coupling likelihood"
                ),
                "frozen_v10_2_prediction_yc_over_yt": frozen_ct_ratio,
            },
        },
        "reclassification_rule": (
            "Any proposed class-A functional that uses mode, generation, "
            "generation-varying v7, or another within-sector varying field "
            "is reclassified as class B before testing."
        ),
        "source_policy": {
            "orientation_blob_sha": "838b2606e004049bf58d86a18cf0f345799aaa73",
            "v10_2_prediction_blob_sha": "b7563fd294e9a688dd276b954ffe56fd499c621e",
            "non_electron_mass_used_to_select_formula": False,
            "future_likelihood_value_inspected": False,
        },
    }

    OUT.mkdir(parents=True, exist_ok=True)
    output = OUT / "up_sector_observable_identifiability_v10_6.json"
    output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
