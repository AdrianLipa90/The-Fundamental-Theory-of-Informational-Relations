#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import importlib.util

ROOT = Path(__file__).resolve().parents[2]
FRONTIER = ROOT / "TIR/TIR_COMPLETION_FRONTIER_V0_7.md"
HYPER = ROOT / "TIR/validation/tir_hypercharge_source_uniqueness_v0_1.py"


def load_hyper():
    spec = importlib.util.spec_from_file_location("hyper", HYPER)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def validate():
    h = load_hyper()
    h.validate()
    text = FRONTIER.read_text(encoding="utf-8")
    assert "HYPERCHARGE_SOURCE_UNIQUENESS = CLOSED_CONDITIONAL_ON_DECLARED_FIELD_CONTENT_AND_TIR_NORMALIZATION_ANCHOR" in text
    assert "CONTINUUM_GAUGE_NORMALIZATION = OPEN" in text
    assert "COEFFICIENT_FREE_TRANSITION_TO_PARENT_SELECTION = OPEN" in text
    assert "PRODUCTION_GLOBAL_SPATIAL_COMPLEX_INPUT = OPEN" in text
    assert "PRODUCTION_INTERLEAF_MATCHING_FIELD_INPUT = OPEN" in text
    assert "RIEMANN_HYPOTHESIS = OPEN" in text
    assert "riemann_hypothesis_in_closure = false" in text
    assert "5=L4+L3" in text and "2+7=9" in text


if __name__ == "__main__":
    validate()
    print("schema=TIR_COMPLETION_FRONTIER_V0_7_VALIDATION")
    print("status=PASS")
    print("hypercharge_source_uniqueness_closed_conditional=true")
    print("continuum_gauge_normalization_remains_open=true")
    print("coefficient_transition_parent_selection_remains_open=true")
    print("production_inputs_remain_open=true")
    print("riemann_hypothesis_in_closure=false")
