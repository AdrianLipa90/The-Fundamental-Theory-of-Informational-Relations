#!/usr/bin/env python3
"""Fail-closed source contract for TIR inter-leaf matching-field data.

The contract owns source provenance, coordinate typing and lossless patch/overlap
payload integrity.  It mirrors the finite RF-GSC3A matching-field overlap relation
for cross-repository handoff compatibility; theorem authority remains in RFC.
"""
from __future__ import annotations

import hashlib
import json
import math
from dataclasses import asdict, dataclass
from typing import Any

SCHEMA = "TIR_INTERLEAF_MATCHING_FIELD_INPUT_V0_1"


class InterleafMatchingInputError(ValueError):
    pass


@dataclass(frozen=True)
class InterleafMatchingInputCertificate:
    input_valid: bool
    integrity_valid: bool
    handoff_compatible: bool
    production_input: bool
    promotion_eligible: bool
    dataset_id: str
    payload_sha256: str
    temporal_coordinate_kind: str
    patch_count: int
    overlap_count: int
    max_matching_residual: float
    rfe8_shift_packet: dict[str, Any]


def _string(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise InterleafMatchingInputError(f"{name} must be a non-empty string")
    return value.strip()


def _finite(value: Any, name: str) -> float:
    if isinstance(value, bool):
        raise InterleafMatchingInputError(f"{name} must be a finite number")
    out = float(value)
    if not math.isfinite(out):
        raise InterleafMatchingInputError(f"{name} must be a finite number")
    return out


def _vec3(value: Any, name: str) -> tuple[float, float, float]:
    if not isinstance(value, (list, tuple)) or len(value) != 3:
        raise InterleafMatchingInputError(f"{name} must contain three numbers")
    return tuple(_finite(x, name) for x in value)  # type: ignore[return-value]


def _mat3(value: Any, name: str) -> tuple[tuple[float, float, float], ...]:
    if not isinstance(value, (list, tuple)) or len(value) != 3:
        raise InterleafMatchingInputError(f"{name} must be 3x3")
    rows = tuple(_vec3(row, f"{name} row") for row in value)
    return rows


def _matvec(a, v):
    return tuple(sum(a[i][k] * v[k] for k in range(3)) for i in range(3))


def _sub(a, b):
    return tuple(a[i] - b[i] for i in range(3))


def _max_residual(a, b):
    return max(abs(a[i] - b[i]) for i in range(3))


def _canonical_payload(*, temporal_coordinate_kind, c_scale, patches, overlaps):
    return {
        "temporal_coordinate_kind": temporal_coordinate_kind,
        "c_scale": c_scale,
        "patches": sorted(
            [
                {"patch_id": patch["patch_id"], "beta_match": list(patch["beta_match"])}
                for patch in patches
            ],
            key=lambda item: item["patch_id"],
        ),
        "overlaps": sorted(
            [
                {
                    "source": overlap["source"],
                    "target": overlap["target"],
                    "spatial_jacobian": [list(row) for row in overlap["spatial_jacobian"]],
                    "time_drift": list(overlap["time_drift"]),
                }
                for overlap in overlaps
            ],
            key=lambda item: (item["source"], item["target"]),
        ),
    }


def payload_sha256(*, temporal_coordinate_kind, c_scale, patches, overlaps):
    payload = _canonical_payload(
        temporal_coordinate_kind=temporal_coordinate_kind,
        c_scale=c_scale,
        patches=patches,
        overlaps=overlaps,
    )
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def build_input_dataset(
    *,
    dataset_id,
    patches,
    overlaps,
    source,
    source_commit_or_digest,
    production,
    temporal_coordinate_kind="t",
    c_scale=299792458.0,
):
    kind = _string(temporal_coordinate_kind, "temporal_coordinate_kind")
    if kind not in {"t", "x0"}:
        raise InterleafMatchingInputError("temporal_coordinate_kind must be t or x0")
    c_value = _finite(c_scale, "c_scale")
    if c_value <= 0.0:
        raise InterleafMatchingInputError("c_scale must be positive")
    normalized_patches = [
        {"patch_id": _string(patch["patch_id"], "patch_id"), "beta_match": _vec3(patch["beta_match"], "beta_match")}
        for patch in patches
    ]
    normalized_overlaps = [
        {
            "source": _string(overlap["source"], "overlap.source"),
            "target": _string(overlap["target"], "overlap.target"),
            "spatial_jacobian": _mat3(overlap["spatial_jacobian"], "spatial_jacobian"),
            "time_drift": _vec3(overlap["time_drift"], "time_drift"),
        }
        for overlap in overlaps
    ]
    digest = payload_sha256(
        temporal_coordinate_kind=kind,
        c_scale=c_value,
        patches=normalized_patches,
        overlaps=normalized_overlaps,
    )
    return {
        "schema": SCHEMA,
        "dataset_id": dataset_id,
        "production": bool(production),
        "provenance": {
            "source": source,
            "source_commit_or_digest": source_commit_or_digest,
        },
        "temporal_coordinate": {
            "kind": kind,
            "x0_binding": "x0=c*t",
            "c_scale": c_value,
        },
        "patches": [
            {"patch_id": patch["patch_id"], "beta_match": list(patch["beta_match"])}
            for patch in normalized_patches
        ],
        "overlaps": [
            {
                "source": overlap["source"],
                "target": overlap["target"],
                "spatial_jacobian": [list(row) for row in overlap["spatial_jacobian"]],
                "time_drift": list(overlap["time_drift"]),
            }
            for overlap in normalized_overlaps
        ],
        "payload_sha256": digest,
    }


def validate_input_dataset(data, *, atol=1.0e-12):
    if not isinstance(data, dict):
        raise InterleafMatchingInputError("dataset must be a JSON object")
    if data.get("schema") != SCHEMA:
        raise InterleafMatchingInputError(f"schema must equal {SCHEMA}")
    dataset_id = _string(data.get("dataset_id"), "dataset_id")
    if type(data.get("production")) is not bool:
        raise InterleafMatchingInputError("production must be a boolean")
    provenance = data.get("provenance")
    if not isinstance(provenance, dict):
        raise InterleafMatchingInputError("provenance must be an object")
    _string(provenance.get("source"), "provenance.source")
    _string(provenance.get("source_commit_or_digest"), "provenance.source_commit_or_digest")

    coordinate = data.get("temporal_coordinate")
    if not isinstance(coordinate, dict):
        raise InterleafMatchingInputError("temporal_coordinate must be an object")
    kind = _string(coordinate.get("kind"), "temporal_coordinate.kind")
    if kind not in {"t", "x0"}:
        raise InterleafMatchingInputError("temporal_coordinate.kind must be t or x0")
    if coordinate.get("x0_binding") != "x0=c*t":
        raise InterleafMatchingInputError("temporal_coordinate.x0_binding must equal x0=c*t")
    c_scale = _finite(coordinate.get("c_scale"), "temporal_coordinate.c_scale")
    if c_scale <= 0.0:
        raise InterleafMatchingInputError("temporal_coordinate.c_scale must be positive")

    raw_patches = data.get("patches")
    if not isinstance(raw_patches, list) or not raw_patches:
        raise InterleafMatchingInputError("patches must be a non-empty list")
    patches = []
    for raw in raw_patches:
        if not isinstance(raw, dict):
            raise InterleafMatchingInputError("patch entries must be objects")
        patches.append({
            "patch_id": _string(raw.get("patch_id"), "patch_id"),
            "beta_match": _vec3(raw.get("beta_match"), "beta_match"),
        })
    patch_ids = [patch["patch_id"] for patch in patches]
    if len(set(patch_ids)) != len(patch_ids):
        raise InterleafMatchingInputError("patch ids must be unique")
    patch_map = {patch["patch_id"]: patch["beta_match"] for patch in patches}

    raw_overlaps = data.get("overlaps")
    if not isinstance(raw_overlaps, list):
        raise InterleafMatchingInputError("overlaps must be a list")
    overlaps = []
    keys = set()
    max_residual = 0.0
    for raw in raw_overlaps:
        if not isinstance(raw, dict):
            raise InterleafMatchingInputError("overlap entries must be objects")
        source = _string(raw.get("source"), "overlap.source")
        target = _string(raw.get("target"), "overlap.target")
        if source == target:
            raise InterleafMatchingInputError("overlap must connect distinct patches")
        if source not in patch_map or target not in patch_map:
            raise InterleafMatchingInputError("overlap references an unknown patch")
        key = (source, target)
        if key in keys:
            raise InterleafMatchingInputError("duplicate directed overlap")
        keys.add(key)
        overlap = {
            "source": source,
            "target": target,
            "spatial_jacobian": _mat3(raw.get("spatial_jacobian"), "spatial_jacobian"),
            "time_drift": _vec3(raw.get("time_drift"), "time_drift"),
        }
        overlaps.append(overlap)
        expected = _sub(_matvec(overlap["spatial_jacobian"], patch_map[source]), overlap["time_drift"])
        residual = _max_residual(expected, patch_map[target])
        max_residual = max(max_residual, residual)
        if residual > atol:
            raise InterleafMatchingInputError(
                f"GSC3A handoff relation beta_target=A beta_source-v failed on {key}; residual={residual:.17g}"
            )

    supplied_digest = _string(data.get("payload_sha256"), "payload_sha256")
    computed_digest = payload_sha256(
        temporal_coordinate_kind=kind,
        c_scale=c_scale,
        patches=patches,
        overlaps=overlaps,
    )
    if supplied_digest != computed_digest:
        raise InterleafMatchingInputError(
            f"payload_sha256 mismatch: supplied={supplied_digest}, computed={computed_digest}"
        )

    divisor = c_scale if kind == "t" else 1.0
    rfe8_patches = [
        {
            "patch_id": patch["patch_id"],
            "b_x0": [value / divisor for value in patch["beta_match"]],
        }
        for patch in patches
    ]
    rfe8_overlaps = [
        {
            "source": overlap["source"],
            "target": overlap["target"],
            "spatial_jacobian": [list(row) for row in overlap["spatial_jacobian"]],
            "time_drift_x0": [value / divisor for value in overlap["time_drift"]],
        }
        for overlap in overlaps
    ]
    packet = {
        "schema": "TIR_TO_RFC_RFE8_SHIFT_HANDOFF_V0_1",
        "source_dataset_id": dataset_id,
        "coordinate": "x0",
        "x0_binding": "x0=c*t",
        "patches": rfe8_patches,
        "overlaps": rfe8_overlaps,
    }

    production = data["production"]
    return InterleafMatchingInputCertificate(
        input_valid=True,
        integrity_valid=True,
        handoff_compatible=True,
        production_input=production,
        promotion_eligible=production,
        dataset_id=dataset_id,
        payload_sha256=computed_digest,
        temporal_coordinate_kind=kind,
        patch_count=len(patches),
        overlap_count=len(overlaps),
        max_matching_residual=max_residual,
        rfe8_shift_packet=packet,
    )


def reference_dataset(*, production=False, c_scale=10.0):
    patches = [
        {"patch_id": "A", "beta_match": [3.0, -2.0, 5.0]},
        {"patch_id": "B", "beta_match": [2.5, -1.0, 3.0]},
    ]
    overlaps = [
        {
            "source": "A",
            "target": "B",
            "spatial_jacobian": [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]],
            "time_drift": [0.5, -1.0, 2.0],
        }
    ]
    return build_input_dataset(
        dataset_id="reference-interleaf-matching-field",
        patches=patches,
        overlaps=overlaps,
        source="TIR inter-leaf matching reference control",
        source_commit_or_digest="REFERENCE_CONTROL_NOT_PRODUCTION",
        production=production,
        temporal_coordinate_kind="t",
        c_scale=c_scale,
    )


def run_reference_controls():
    data = reference_dataset(production=False, c_scale=10.0)
    cert = validate_input_dataset(data)
    assert cert.input_valid and cert.integrity_valid and cert.handoff_compatible
    assert cert.production_input is False and cert.promotion_eligible is False
    assert cert.max_matching_residual == 0.0
    patches = {row["patch_id"]: row["b_x0"] for row in cert.rfe8_shift_packet["patches"]}
    assert patches["A"] == [0.3, -0.2, 0.5]
    assert patches["B"] == [0.25, -0.1, 0.3]
    drift = cert.rfe8_shift_packet["overlaps"][0]["time_drift_x0"]
    assert drift == [0.05, -0.1, 0.2]

    corrupted = json.loads(json.dumps(data))
    corrupted["patches"][1]["beta_match"][0] += 0.25
    corrupted["payload_sha256"] = payload_sha256(
        temporal_coordinate_kind="t",
        c_scale=10.0,
        patches=[{"patch_id": p["patch_id"], "beta_match": tuple(p["beta_match"])} for p in corrupted["patches"]],
        overlaps=[{
            "source": o["source"],
            "target": o["target"],
            "spatial_jacobian": tuple(tuple(row) for row in o["spatial_jacobian"]),
            "time_drift": tuple(o["time_drift"]),
        } for o in corrupted["overlaps"]],
    )
    try:
        validate_input_dataset(corrupted)
    except InterleafMatchingInputError as exc:
        assert "handoff relation" in str(exc)
    else:
        raise AssertionError("inconsistent matching field must fail closed")

    bad_digest = json.loads(json.dumps(data))
    bad_digest["payload_sha256"] = "0" * 64
    try:
        validate_input_dataset(bad_digest)
    except InterleafMatchingInputError as exc:
        assert "payload_sha256 mismatch" in str(exc)
    else:
        raise AssertionError("digest mismatch must fail closed")

    return {
        "schema": "TIR_INTERLEAF_MATCHING_FIELD_INPUT_CONTRACT_REFERENCE_RECEIPT_V0_1",
        "technical_status": "PASS",
        "reference_production": False,
        "reference_promotion_eligible": False,
        "matching_residual": cert.max_matching_residual,
        "rfe8_coordinate": cert.rfe8_shift_packet["coordinate"],
        "production_matching_field_input": "OPEN_INPUT",
        "verdict": "PASS_TIR_INTERLEAF_MATCHING_FIELD_INPUT_CONTRACT_WITH_PRODUCTION_INPUT_OPEN",
    }


if __name__ == "__main__":
    print(json.dumps(run_reference_controls(), indent=2, sort_keys=True))
