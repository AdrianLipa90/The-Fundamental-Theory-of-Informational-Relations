#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from tir_global_spatial_complex_input_contract_v0_1 import validate_input_dataset
from tir_global_spatial_complex_source_freeze_v0_1 import (
    SpatialComplexFreezeError,
    freeze_json_text,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Freeze a source-owned relational tetrahedral complex into the TIR GSC1 contract."
    )
    parser.add_argument("capture", type=Path)
    parser.add_argument("--dataset-out", type=Path, required=True)
    parser.add_argument("--certificate-out", type=Path, required=True)
    args = parser.parse_args()

    try:
        frozen = freeze_json_text(args.capture.read_text(encoding="utf-8"))
        certificate = validate_input_dataset(frozen.dataset)
    except (OSError, SpatialComplexFreezeError, ValueError) as exc:
        error = {
            "schema": "TIR_GSC1_SOURCE_FREEZE_CLI_RESULT_V0_1",
            "status": "FAIL",
            "error": str(exc),
            "promotion_authority": False,
        }
        args.certificate_out.write_text(
            json.dumps(error, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        return 2

    args.dataset_out.write_text(
        json.dumps(frozen.dataset, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    result = {
        "schema": "TIR_GSC1_SOURCE_FREEZE_CLI_RESULT_V0_1",
        "status": "PASS",
        "capture_sha256": frozen.capture_sha256,
        "cell_count": frozen.cell_count,
        "vertex_count": frozen.vertex_count,
        "production_source_admitted": frozen.production_source_admitted,
        "certificate": asdict(certificate),
        "production_promoted": False,
        "promotion_authority": False,
        "note": "promotion_eligible is an input-gate result; repository canon promotion is a separate action",
    }
    args.certificate_out.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    return 0 if certificate.manifold_certified else 3


if __name__ == "__main__":
    raise SystemExit(main())
