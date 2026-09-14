from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR = ROOT / "TIR" / "validation" / "tir_ckm_su3f_angle_sine_generator_firewall_v0_8.py"


def test_ckm_su3f_angle_sine_generator_firewall_v08() -> None:
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
    assert receipt["checks"]["angle_linear_coefficient_is_not_a"] is True
    assert receipt["checks"]["naive_additive_connection_angle_does_not_equal_additive_sine"] is True
    assert receipt["open"]["derive_angle_to_sine_readout_map_from_TIR"] is True
