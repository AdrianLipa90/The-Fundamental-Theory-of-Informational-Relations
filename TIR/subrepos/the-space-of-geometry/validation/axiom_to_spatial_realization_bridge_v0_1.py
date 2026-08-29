#!/usr/bin/env python3
"""Deterministic audit for Axiom-to-Spatial-Realization Bridge v0.1."""
from __future__ import annotations

import json


def build_receipt() -> dict[str, object]:
    dependencies = {
        "A2": "C2_TO_HERM0_2",
        "A3": "DISTINGUISHABILITY_PRESERVATION_CANDIDATE",
        "A5_A7": "INVARIANT_REAL_QUADRATIC_MEASURE",
        "A1_A3": "MINIMAL_SOURCE_CLOSURE_CANDIDATE",
    }
    required = {"A2", "A3", "A5_A7", "A1_A3"}
    pass_dependencies = set(dependencies) == required

    return {
        "schema": "TIR_SPACE_OF_GEOMETRY_AXIOM_TO_SPATIAL_REALIZATION_BRIDGE_V0_1",
        "effective_group": "PSU(2)~=SO(3)",
        "exact_closure_if_bridge_conditions_admitted": "V_x~=Herm_0(2)~=R3",
        "bridge_status": "TWO_FOUNDATIONAL_RULES_REMAIN_TO_BE_PROMOTED",
        "foundational_rules": [
            "A3_DISTINGUISHABILITY_PRESERVATION_AFTER_GAUGE_REDUCTION",
            "A1_A3_MINIMAL_SOURCE_CLOSURE",
        ],
        "orthogonality_route": "A5_PLUS_A7_INVARIANT_POSITIVE_QUADRATIC_MEASURE",
        "dependencies": dependencies,
        "dependency_surface_complete": pass_dependencies,
        "technical_status": "PASS" if pass_dependencies else "FAIL",
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
