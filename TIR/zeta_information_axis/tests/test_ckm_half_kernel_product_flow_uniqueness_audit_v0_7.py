from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR = ROOT / "TIR" / "validation" / "tir_ckm_half_kernel_product_flow_uniqueness_audit_v0_7.py"


def test_ckm_half_kernel_product_flow_uniqueness_audit_v07() -> None:
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
    assert receipt["zero_trace_correlated_direction"]["normalized_trace"] == "0"
    assert receipt["checks"]["scalar_readout_does_not_identify_operator"] is True
    assert receipt["checks"]["monoidal_generator_is_P_plus_kappa_Q_at_first_order"] is True
    assert receipt["open"]["derive_monoidal_independence_from_TIR_connection_or_information_flow"] is True
