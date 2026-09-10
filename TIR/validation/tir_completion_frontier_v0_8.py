#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
F = ROOT / "TIR/TIR_COMPLETION_FRONTIER_V0_8.md"


def validate():
    t = F.read_text(encoding="utf-8")
    required = [
        "NEUTRINO_ABSOLUTE_ACTION_REPAIR = CLOSED_SOURCE_CONFLICT",
        "NEUTRINO_ABSOLUTE_MASS_PHYSICAL_VALIDATION = OPEN",
        "HYPERCHARGE_SOURCE_UNIQUENESS = CLOSED_CONDITIONAL_ON_DECLARED_FIELD_CONTENT_AND_TIR_NORMALIZATION_ANCHOR",
        "CONTINUUM_GAUGE_NORMALIZATION = OPEN_SEPARATE_GATE",
        "COEFFICIENT_FREE_TRANSITION_TO_PARENT_SELECTION = OPEN",
        "PRODUCTION_GLOBAL_SPATIAL_COMPLEX_INPUT = OPEN",
        "PRODUCTION_INTERLEAF_MATCHING_FIELD_INPUT = OPEN",
        "RIEMANN_HYPOTHESIS = OPEN",
        "riemann_hypothesis_in_closure = false",
    ]
    assert all(x in t for x in required)
    assert "S_1=S_{\\rm bare}+dS" in t


if __name__ == "__main__":
    validate()
    print("schema=TIR_COMPLETION_FRONTIER_V0_8_VALIDATION")
    print("status=PASS")
    print("neutrino_action_source_repair_closed=true")
    print("neutrino_absolute_mass_physical_validation_open=true")
    print("hypercharge_source_uniqueness_closed_conditional=true")
    print("coefficient_parent_selection_open=true")
    print("riemann_hypothesis_in_closure=false")
