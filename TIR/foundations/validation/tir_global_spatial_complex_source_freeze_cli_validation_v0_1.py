#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from freeze_global_spatial_complex import main as freeze_cli_main
from tir_global_3manifold_smooth_certificate_v0_1 import boundary_of_4_simplex
from tir_global_spatial_complex_source_freeze_v0_1 import CAPTURE_SCHEMA


def make_reference_capture():
    return {
        "schema": CAPTURE_SCHEMA,
        "capture_id": "cli-reference-global-spatial-complex",
        "source": {
            "source_id": "CLI_REFERENCE_SOURCE",
            "source_class": "REFERENCE_CONTROL",
            "immutable_ref": "CLI_REFERENCE_IMMUTABLE_REF",
        },
        "tetrahedral_cells": [
            {
                "cell_id": f"tet-{index}",
                "vertices": [str(v) for v in tet],
            }
            for index, tet in enumerate(boundary_of_4_simplex())
        ],
    }


def main():
    with tempfile.TemporaryDirectory() as tmpdir:
        root = Path(tmpdir)
        capture_path = root / "capture.json"
        dataset_path = root / "dataset.json"
        certificate_path = root / "certificate.json"
        capture_path.write_text(
            json.dumps(make_reference_capture(), indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

        code = freeze_cli_main([
            str(capture_path),
            "--dataset-out", str(dataset_path),
            "--certificate-out", str(certificate_path),
        ])
        dataset = json.loads(dataset_path.read_text(encoding="utf-8"))
        result = json.loads(certificate_path.read_text(encoding="utf-8"))

        checks = [
            code == 0,
            result["status"] == "PASS",
            result["production_promoted"] is False,
            result["promotion_authority"] is False,
            result["production_source_admitted"] is False,
            result["certificate"]["manifold_certified"] is True,
            result["certificate"]["promotion_eligible"] is False,
            dataset["production"] is False,
            len(dataset["tetrahedra"]) == 5,
        ]

    receipt = {
        "schema": "TIR_GSC1_SOURCE_FREEZE_CLI_VALIDATION_V0_1",
        "status": "PASS" if all(checks) else "FAIL",
        "checks": len(checks),
        "passed": sum(bool(x) for x in checks),
        "production_fixture_persisted": False,
        "promotion_authority": False,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if not all(checks):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
