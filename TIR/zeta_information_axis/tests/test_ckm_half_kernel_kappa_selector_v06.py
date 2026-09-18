from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR = ROOT / "TIR/validation/tir_ckm_half_kernel_kappa_selector_candidate_v0_6.py"


def test_ckm_half_kernel_kappa_selector_v06_receipt() -> None:
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR)],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    receipt = json.loads(proc.stdout)
    assert receipt["status"] == "PASS"
    assert receipt["physical_promotion"] is False
    assert receipt["uses_observed_ckm_to_select_structure"] is False
    assert receipt["packet_compression"]["bulk_dimension"] == 9
    assert receipt["packet_compression"]["boundary_dimension"] == 7
    assert receipt["product_generator"]["bulk_coefficient"] == "2/9"
    assert receipt["product_generator"]["boundary_coefficient"] == "2/7"
    assert receipt["product_generator"]["normalized_trace"] == "b + kappa*a"
    assert receipt["inverse_ladder"]["xi_cross_midpoint"] == "7/2"
    assert receipt["open"]["derive_product_flow_as_unique_physical_ckm_generator"] is True
    assert receipt["open"]["promote_refined_lambda_as_first_principles_prediction"] is True
    assert all(receipt["checks"].values())
