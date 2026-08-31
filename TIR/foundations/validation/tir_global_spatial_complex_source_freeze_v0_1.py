#!/usr/bin/env python3
"""Freeze a source-owned relational tetrahedral complex into the TIR GSC1 input contract."""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from typing import Any

from tir_global_spatial_complex_input_contract_v0_1 import (
    SpatialComplexInputError,
    build_input_dataset,
    validate_input_dataset,
)

CAPTURE_SCHEMA = "TIR_GLOBAL_RELATIONAL_COMPLEX_CAPTURE_V0_1"
HEX64 = re.compile(r"^[0-9a-f]{64}$")


class SpatialComplexFreezeError(ValueError):
    """Raised when a source capture cannot be admitted to the GSC1 freeze surface."""


@dataclass(frozen=True)
class FrozenSpatialComplex:
    dataset: dict[str, Any]
    capture_sha256: str
    cell_count: int
    vertex_count: int
    production_source_admitted: bool


def _canonical(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _sha256(obj: Any) -> str:
    return hashlib.sha256(_canonical(obj)).hexdigest()


def _require_string(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise SpatialComplexFreezeError(f"{name} must be a non-empty string")
    return value.strip()


def _validate_source(source: Any) -> tuple[str, str, bool, str | None]:
    if not isinstance(source, dict):
        raise SpatialComplexFreezeError("source must be an object")

    source_id = _require_string(source.get("source_id"), "source.source_id")
    immutable_ref = _require_string(source.get("immutable_ref"), "source.immutable_ref")
    source_class = _require_string(source.get("source_class"), "source.source_class")
    if source_class not in {"PRODUCTION_SOURCE", "REFERENCE_CONTROL", "CANDIDATE_SOURCE"}:
        raise SpatialComplexFreezeError("unsupported source.source_class")

    receipt = source.get("capture_receipt_sha256")
    if receipt is not None:
        receipt = _require_string(receipt, "source.capture_receipt_sha256")
        if HEX64.fullmatch(receipt) is None:
            raise SpatialComplexFreezeError("source.capture_receipt_sha256 must be 64 lowercase hex characters")

    production = source_class == "PRODUCTION_SOURCE"
    if production and receipt is None:
        raise SpatialComplexFreezeError("PRODUCTION_SOURCE requires capture_receipt_sha256")

    return source_id, immutable_ref, production, receipt


def freeze_source_capture(capture: dict[str, Any]) -> FrozenSpatialComplex:
    if not isinstance(capture, dict):
        raise SpatialComplexFreezeError("capture must be an object")
    if capture.get("schema") != CAPTURE_SCHEMA:
        raise SpatialComplexFreezeError(f"capture schema must equal {CAPTURE_SCHEMA}")

    capture_id = _require_string(capture.get("capture_id"), "capture_id")
    source_id, immutable_ref, production, receipt = _validate_source(capture.get("source"))

    raw_cells = capture.get("tetrahedral_cells")
    if not isinstance(raw_cells, list) or not raw_cells:
        raise SpatialComplexFreezeError("tetrahedral_cells must be a non-empty list")

    cell_ids: set[str] = set()
    tetrahedra: list[tuple[str, str, str, str]] = []
    canonical_cells: list[dict[str, Any]] = []
    seen_tetrahedra: set[tuple[str, str, str, str]] = set()

    for index, raw_cell in enumerate(raw_cells):
        if not isinstance(raw_cell, dict):
            raise SpatialComplexFreezeError(f"tetrahedral_cells[{index}] must be an object")
        cell_id = _require_string(raw_cell.get("cell_id"), f"tetrahedral_cells[{index}].cell_id")
        if cell_id in cell_ids:
            raise SpatialComplexFreezeError(f"duplicate cell_id: {cell_id}")
        cell_ids.add(cell_id)

        raw_vertices = raw_cell.get("vertices")
        if not isinstance(raw_vertices, list) or len(raw_vertices) != 4:
            raise SpatialComplexFreezeError(f"tetrahedral_cells[{index}].vertices must contain four ids")
        vertices = tuple(_require_string(v, f"tetrahedral_cells[{index}].vertex") for v in raw_vertices)
        if len(set(vertices)) != 4:
            raise SpatialComplexFreezeError(f"tetrahedral_cells[{index}] repeats a vertex")
        tet = tuple(sorted(vertices))
        if tet in seen_tetrahedra:
            raise SpatialComplexFreezeError(f"duplicate tetrahedral facet: {tet}")
        seen_tetrahedra.add(tet)
        tetrahedra.append(tet)
        canonical_cells.append({"cell_id": cell_id, "vertices": list(tet)})

    vertices = sorted({v for tet in tetrahedra for v in tet})
    frozen_capture_payload = {
        "schema": CAPTURE_SCHEMA,
        "capture_id": capture_id,
        "source": capture["source"],
        "tetrahedral_cells": sorted(canonical_cells, key=lambda item: item["cell_id"]),
    }
    capture_sha = _sha256(frozen_capture_payload)

    dataset = build_input_dataset(
        dataset_id=capture_id,
        vertices=vertices,
        tetrahedra=tetrahedra,
        source=source_id,
        source_commit_or_digest=immutable_ref,
        production=production,
    )
    dataset["provenance"]["source_class"] = capture["source"]["source_class"]
    dataset["provenance"]["capture_sha256"] = capture_sha
    if receipt is not None:
        dataset["provenance"]["capture_receipt_sha256"] = receipt
    dataset["provenance"]["source_cell_count"] = len(tetrahedra)

    # Run the existing GSC1 contract immediately so the adapter cannot emit an
    # unchecked production-shaped object.
    validate_input_dataset(dataset)

    return FrozenSpatialComplex(
        dataset=dataset,
        capture_sha256=capture_sha,
        cell_count=len(tetrahedra),
        vertex_count=len(vertices),
        production_source_admitted=production,
    )


def freeze_json_text(raw: str) -> FrozenSpatialComplex:
    try:
        capture = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SpatialComplexFreezeError(f"invalid JSON: {exc}") from exc
    return freeze_source_capture(capture)
