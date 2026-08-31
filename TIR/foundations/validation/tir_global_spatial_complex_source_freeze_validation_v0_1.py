#!/usr/bin/env python3
from __future__ import annotations

import json

from tir_global_3manifold_smooth_certificate_v0_1 import boundary_of_4_simplex
from tir_global_spatial_complex_input_contract_v0_1 import validate_input_dataset
from tir_global_spatial_complex_source_freeze_v0_1 import (
    CAPTURE_SCHEMA,
    SpatialComplexFreezeError,
    freeze_source_capture,
)


def make_capture(*, source_class="REFERENCE_CONTROL", receipt=None, reverse=False):
    tets = [tuple(str(v) for v in tet) for tet in boundary_of_4_simplex()]
    cells = [
        {"cell_id": f"tet-{index}", "vertices": list(tet)}
        for index, tet in enumerate(tets)
    ]
    if reverse:
        cells = [
            {"cell_id": item["cell_id"], "vertices": list(reversed(item["vertices"]))}
            for item in reversed(cells)
        ]
    source = {
        "source_id": "UNIT_TEST_SPATIAL_RELATIONAL_COMPLEX",
        "source_class": source_class,
        "immutable_ref": "unit-test-immutable-source-ref-v1",
    }
    if receipt is not None:
        source["capture_receipt_sha256"] = receipt
    return {
        "schema": CAPTURE_SCHEMA,
        "capture_id": "unit-test-global-spatial-complex",
        "source": source,
        "tetrahedral_cells": cells,
    }


def expect_rejected(capture):
    try:
        freeze_source_capture(capture)
    except SpatialComplexFreezeError:
        return True
    return False


def main():
    checks = []

    ref = freeze_source_capture(make_capture())
    ref_cert = validate_input_dataset(ref.dataset)
    checks.append({
        "name": "reference_source_freezes_and_passes_A5_without_promotion",
        "pass": ref_cert.manifold_certified
        and not ref.production_source_admitted
        and not ref_cert.promotion_eligible,
    })

    reordered = freeze_source_capture(make_capture(reverse=True))
    checks.append({
        "name": "freeze_is_invariant_to_cell_order_and_vertex_order",
        "pass": ref.capture_sha256 == reordered.capture_sha256
        and ref.dataset["incidence_sha256"] == reordered.dataset["incidence_sha256"],
    })

    missing_receipt = make_capture(source_class="PRODUCTION_SOURCE")
    checks.append({
        "name": "production_source_without_capture_receipt_is_rejected",
        "pass": expect_rejected(missing_receipt),
    })

    malformed_receipt = make_capture(source_class="PRODUCTION_SOURCE", receipt="abc")
    checks.append({
        "name": "malformed_production_capture_receipt_is_rejected",
        "pass": expect_rejected(malformed_receipt),
    })

    # In-memory execution-path control only. No production fixture is persisted.
    prod = freeze_source_capture(
        make_capture(source_class="PRODUCTION_SOURCE", receipt="a" * 64)
    )
    prod_cert = validate_input_dataset(prod.dataset)
    checks.append({
        "name": "production_path_requires_receipt_and_preserves_A5_gate",
        "pass": prod.production_source_admitted
        and prod_cert.production_input
        and prod_cert.manifold_certified
        and prod_cert.promotion_eligible,
    })

    duplicate_id = make_capture()
    duplicate_id["tetrahedral_cells"][1]["cell_id"] = duplicate_id["tetrahedral_cells"][0]["cell_id"]
    checks.append({
        "name": "duplicate_source_cell_id_is_rejected",
        "pass": expect_rejected(duplicate_id),
    })

    duplicate_tet = make_capture()
    duplicate_tet["tetrahedral_cells"][1]["vertices"] = list(
        duplicate_tet["tetrahedral_cells"][0]["vertices"]
    )
    checks.append({
        "name": "duplicate_tetrahedral_facet_is_rejected",
        "pass": expect_rejected(duplicate_tet),
    })

    passed = all(item["pass"] for item in checks)
    receipt = {
        "schema": "TIR_GLOBAL_SPATIAL_COMPLEX_SOURCE_FREEZE_VALIDATION_V0_1",
        "status": "PASS" if passed else "FAIL",
        "verdict": (
            "PASS_TIR_GSC1_SOURCE_FREEZE_ADAPTER_WITH_PRODUCTION_SOURCE_RECEIPT_REQUIRED"
            if passed
            else "FAIL_TIR_GSC1_SOURCE_FREEZE_ADAPTER"
        ),
        "checks": checks,
        "production_dataset_committed": False,
        "source_freeze_promotes_without_A5": False,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
