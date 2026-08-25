#!/usr/bin/env python3
"""Stage 40 — retrospective comparison of the frozen Stage 39 candidate.

This stage reads the already frozen Stage 39 receipt and the archived v7.9r1
CKM result.  It performs no retuning and selects no preferred sector assignment.
All discrepancies are retained.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[2]
STAGE39 = ROOT / "results" / "TIR_POLYGONAL_STAGE39_TWO_OPERATOR_FAMILY_CANDIDATE_RECEIPT_V0_1.json"
CKM = REPO / "archive" / "v7.9" / "full" / "79_debt10_ckm_first_principles_v7_9" / "results" / "ckm_v7_9r1.json"
OUT = ROOT / "results"

ORDER = ["Vud", "Vus", "Vub", "Vcd", "Vcs", "Vcb", "Vtd", "Vts", "Vtb"]


def as_matrix(records):
    d = {r["element"]: float(r["predicted"]) for r in records}
    return np.array(
        [[d["Vud"], d["Vus"], d["Vub"]],
         [d["Vcd"], d["Vcs"], d["Vcb"]],
         [d["Vtd"], d["Vts"], d["Vtb"]]],
        dtype=float,
    )


def score(label, block, target, J_target):
    V = np.array(block["abs_relative_matrix"], dtype=float)
    delta = np.abs(V - target)
    key = {
        "Vus": (0, 1),
        "Vub": (0, 2),
        "Vcb": (1, 2),
        "Vtd": (2, 0),
        "Vts": (2, 1),
    }
    ratios = {
        name: float(V[i, j] / target[i, j])
        for name, (i, j) in key.items()
    }
    J_abs = abs(float(block["J_family"]))
    return {
        "assignment": label,
        "max_abs_matrix_difference": float(np.max(delta)),
        "mean_abs_matrix_difference": float(np.mean(delta)),
        "frobenius_difference": float(np.linalg.norm(delta)),
        "key_element_ratios_candidate_over_reference": ratios,
        "J_abs": J_abs,
        "J_reference": J_target,
        "J_abs_ratio_candidate_over_reference": float(J_abs / J_target),
        "full_ckm_shape_pass": False,
    }


def main():
    stage39 = json.loads(STAGE39.read_text(encoding="utf-8"))
    ckm = json.loads(CKM.read_text(encoding="utf-8"))
    target = as_matrix(ckm["ckm_magnitudes"])
    J_target = float(ckm["cp_violation"]["J_CP"])

    primary = stage39["outputs"]["primary_cN"]
    scores = [
        score("u=a_d=b", primary["u=a_d=b"], target, J_target),
        score("u=b_d=a", primary["u=b_d=a"], target, J_target),
    ]

    receipt = {
        "schema": "TIR_POLYGONAL_STAGE40_STAGE39_CKM_RETROSPECTIVE_V0_1",
        "status": "STAGE_40_FULL_CKM_SHAPE_FAIL__MECHANISM_RETAINED",
        "comparison_type": "RETROSPECTIVE_DIAGNOSTIC",
        "stage39_mutated": False,
        "retuning_performed": False,
        "assignment_selected_by_fit": False,
        "reference_schema": ckm["schema"],
        "reference_fingerprint": ckm.get("fingerprint_sha256"),
        "scores": scores,
        "failure_drivers": [
            "Cabibbo-like Vus magnitude strongly underproduced",
            "Vub magnitude strongly overproduced",
            "Vtd magnitude overproduced",
            "J magnitude below archived structural CKM value",
        ],
        "retained_results": [
            "unitary relative family transformation",
            "hierarchical near-identity magnitude matrix",
            "non-zero rephasing-invariant family CP measure",
            "parameter-free Stage 39 freeze",
        ],
    }
    path = OUT / "TIR_POLYGONAL_STAGE40_STAGE39_CKM_RETROSPECTIVE_RECEIPT_V0_1.json"
    path.write_text(json.dumps(receipt, indent=2), encoding="utf-8")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
