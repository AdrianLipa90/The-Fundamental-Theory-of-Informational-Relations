#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import json
import math
import re
from pathlib import Path
from typing import Any, Mapping

SCHEMA = "TIR_MUMMU_QHTRI_PNLF_TRAJECTORY_RECEIPT_BINDING_V0_1"
SOURCE_PNCS_COMMIT = "8855abed440e9949f576ffbe2153325f69e78963"
DIGEST_RE = re.compile(r"^[0-9a-f]{64}$")


class BindingError(ValueError):
    pass


def canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")


def sha256(value: object) -> str:
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def finite(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise BindingError(f"{name} must be finite real")
    out = float(value)
    if not math.isfinite(out):
        raise BindingError(f"{name} must be finite real")
    return out


def positive(value: object, name: str) -> float:
    out = finite(value, name)
    if out <= 0.0:
        raise BindingError(f"{name} must be positive")
    return out


def text(value: object, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise BindingError(f"{name} must be non-empty text")
    return value.strip()


def digest(value: object, name: str) -> str:
    if not isinstance(value, str) or not DIGEST_RE.fullmatch(value):
        raise BindingError(f"{name} must be lowercase SHA-256")
    return value


def validate_binding(
    payload: Mapping[str, Any],
    *,
    declared_commitment: str | None = None,
) -> str:
    if not isinstance(payload, Mapping):
        raise BindingError("payload must be a mapping")
    if payload.get("schema") != SCHEMA:
        raise BindingError("schema mismatch")
    if payload.get("source_pncs_commit") != SOURCE_PNCS_COMMIT:
        raise BindingError("source PNCS commit mismatch")

    text(payload.get("segment_id"), "segment_id")
    text(payload.get("t36_basis_id"), "t36_basis_id")
    proper_time_model_id = text(
        payload.get("proper_time_model_id"),
        "proper_time_model_id",
    )
    tau_start = finite(payload.get("tau_start"), "tau_start")
    tau_end = finite(payload.get("tau_end"), "tau_end")
    tol = finite(payload.get("numeric_tolerance"), "numeric_tolerance")
    if tol < 0.0:
        raise BindingError("numeric_tolerance must be non-negative")
    if tau_end <= tau_start:
        raise BindingError("tau_end must exceed tau_start")

    steps = payload.get("steps")
    if not isinstance(steps, list) or not steps:
        raise BindingError("steps must be a non-empty ordered list")

    proper_sum = 0.0
    for expected_index, raw in enumerate(steps):
        if not isinstance(raw, Mapping):
            raise BindingError("step must be a mapping")
        index = raw.get("step_index")
        if isinstance(index, bool) or not isinstance(index, int):
            raise BindingError("step_index must be integer")
        if index != expected_index:
            raise BindingError("step indices must be contiguous and ordered")

        digest(raw.get("htri_step_receipt_sha256"), "htri_step_receipt_sha256")
        digest(raw.get("H_sha256"), "H_sha256")
        digest(
            raw.get("time_binding_receipt_sha256"),
            "time_binding_receipt_sha256",
        )
        step_model = text(
            raw.get("time_binding_model_id"),
            "time_binding_model_id",
        )
        if step_model != proper_time_model_id:
            raise BindingError("step time model differs from layer time model")

        htri_dt = positive(raw.get("htri_dt"), "htri_dt")
        coordinate_dt = positive(raw.get("coordinate_dt"), "coordinate_dt")
        combined_g = positive(raw.get("combined_g"), "combined_g")
        proper_dt = positive(raw.get("proper_dt"), "proper_dt")

        if abs(htri_dt - coordinate_dt) > tol:
            raise BindingError("HTRI dt differs from coordinate dt")
        expected_proper = coordinate_dt * combined_g
        if abs(proper_dt - expected_proper) > tol:
            raise BindingError("proper_dt differs from coordinate_dt*combined_g")
        proper_sum += proper_dt

    layer_span = tau_end - tau_start
    if abs(proper_sum - layer_span) > tol:
        raise BindingError("proper-time sum does not close PNLF interval")

    commitment = sha256(dict(payload))
    if declared_commitment is not None:
        digest(declared_commitment, "declared_commitment")
        if commitment != declared_commitment:
            raise BindingError("declared PNLF trajectory commitment mismatch")
    return commitment


def base_payload() -> dict[str, Any]:
    model = "pncs:orch-time-kernel:test:v1"
    steps = [
        {
            "step_index": 0,
            "htri_step_receipt_sha256": "a" * 64,
            "H_sha256": "b" * 64,
            "htri_dt": 0.01,
            "coordinate_dt": 0.01,
            "time_binding_receipt_sha256": "c" * 64,
            "time_binding_model_id": model,
            "combined_g": 0.8,
            "proper_dt": 0.008,
        },
        {
            "step_index": 1,
            "htri_step_receipt_sha256": "d" * 64,
            "H_sha256": "e" * 64,
            "htri_dt": 0.02,
            "coordinate_dt": 0.02,
            "time_binding_receipt_sha256": "f" * 64,
            "time_binding_model_id": model,
            "combined_g": 1.25,
            "proper_dt": 0.025,
        },
        {
            "step_index": 2,
            "htri_step_receipt_sha256": "1" * 64,
            "H_sha256": "2" * 64,
            "htri_dt": 0.015,
            "coordinate_dt": 0.015,
            "time_binding_receipt_sha256": "3" * 64,
            "time_binding_model_id": model,
            "combined_g": 0.6,
            "proper_dt": 0.009,
        },
    ]
    return {
        "schema": SCHEMA,
        "source_pncs_commit": SOURCE_PNCS_COMMIT,
        "segment_id": "pnlf:segment:mummu:test-001",
        "t36_basis_id": "pncs:t36:test-basis:v1",
        "proper_time_model_id": model,
        "tau_start": 2.0,
        "tau_end": 2.042,
        "numeric_tolerance": 1.0e-12,
        "steps": steps,
    }


def rejected(payload: Mapping[str, Any], commitment: str | None = None) -> bool:
    try:
        validate_binding(payload, declared_commitment=commitment)
    except (BindingError, TypeError, ValueError):
        return True
    return False


def main() -> int:
    checks: list[dict[str, Any]] = []
    base = base_payload()
    base_commitment = validate_binding(base)
    repeat_commitment = validate_binding(copy.deepcopy(base))
    checks.append({
        "name": "canonical_binding_is_deterministic",
        "status": "PASS" if base_commitment == repeat_commitment else "FAIL",
        "commitment": base_commitment,
    })

    validate_binding(base, declared_commitment=base_commitment)
    checks.append({
        "name": "declared_pnlf_commitment_matches_canonical_payload",
        "status": "PASS",
    })

    variants: list[tuple[str, dict[str, Any]]] = []

    changed_h = copy.deepcopy(base)
    changed_h["steps"][1]["H_sha256"] = "4" * 64
    variants.append(("hamiltonian_hash", changed_h))

    changed_htri_receipt = copy.deepcopy(base)
    changed_htri_receipt["steps"][0]["htri_step_receipt_sha256"] = "5" * 64
    variants.append(("htri_step_receipt", changed_htri_receipt))

    changed_time_receipt = copy.deepcopy(base)
    changed_time_receipt["steps"][2]["time_binding_receipt_sha256"] = "6" * 64
    variants.append(("time_binding_receipt", changed_time_receipt))

    changed_basis = copy.deepcopy(base)
    changed_basis["t36_basis_id"] = "pncs:t36:test-basis:v2"
    variants.append(("t36_basis", changed_basis))

    sensitivity = {
        name: validate_binding(candidate) != base_commitment
        for name, candidate in variants
    }
    checks.append({
        "name": "identity_fields_change_commitment",
        "status": "PASS" if all(sensitivity.values()) else "FAIL",
        "sensitivity": sensitivity,
    })

    reordered = copy.deepcopy(base)
    reordered["steps"] = [
        copy.deepcopy(base["steps"][2]),
        copy.deepcopy(base["steps"][0]),
        copy.deepcopy(base["steps"][1]),
    ]
    for index, step in enumerate(reordered["steps"]):
        step["step_index"] = index
    reordered_commitment = validate_binding(reordered)
    checks.append({
        "name": "ordered_step_sequence_enters_identity",
        "status": "PASS" if reordered_commitment != base_commitment else "FAIL",
        "reordered_commitment": reordered_commitment,
    })

    model_mismatch = copy.deepcopy(base)
    model_mismatch["steps"][1]["time_binding_model_id"] = "pncs:orch-time-kernel:test:v2"
    checks.append({
        "name": "mixed_time_models_fail_closed",
        "status": "PASS" if rejected(model_mismatch) else "FAIL",
    })

    dt_mismatch = copy.deepcopy(base)
    dt_mismatch["steps"][0]["htri_dt"] = 0.011
    checks.append({
        "name": "htri_coordinate_dt_mismatch_fails_closed",
        "status": "PASS" if rejected(dt_mismatch) else "FAIL",
    })

    proper_mismatch = copy.deepcopy(base)
    proper_mismatch["steps"][2]["proper_dt"] = 0.010
    proper_mismatch["tau_end"] = 2.043
    checks.append({
        "name": "per_step_proper_time_formula_fails_closed",
        "status": "PASS" if rejected(proper_mismatch) else "FAIL",
    })

    endpoint_mismatch = copy.deepcopy(base)
    endpoint_mismatch["tau_end"] = 2.041
    checks.append({
        "name": "pnlf_endpoint_closure_fails_closed",
        "status": "PASS" if rejected(endpoint_mismatch) else "FAIL",
    })

    stale_declared = "7" * 64
    checks.append({
        "name": "stale_declared_commitment_fails_closed",
        "status": "PASS" if rejected(base, stale_declared) else "FAIL",
    })

    bad_order = copy.deepcopy(base)
    bad_order["steps"][1]["step_index"] = 2
    checks.append({
        "name": "noncontiguous_step_indices_fail_closed",
        "status": "PASS" if rejected(bad_order) else "FAIL",
    })

    nonfinite = copy.deepcopy(base)
    nonfinite["steps"][0]["combined_g"] = float("inf")
    checks.append({
        "name": "nonfinite_numeric_input_fails_closed",
        "status": "PASS" if rejected(nonfinite) else "FAIL",
    })

    status = "PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL"
    out = {
        "schema": "TIR_MUMMU_QHTRI_PNLF_TRAJECTORY_RECEIPT_BINDING_VALIDATION_V0_1",
        "status": status,
        "claim_scope": (
            "candidate canonical provenance binding from ordered QHTRI step receipts "
            "and ORCH time bindings to one PNLF T36 trajectory commitment; native PNCS "
            "emitter and physical binding remain open"
        ),
        "source_pins": {"pncs_main": SOURCE_PNCS_COMMIT},
        "checks": checks,
        "summary": {
            "passed": sum(c["status"] == "PASS" for c in checks),
            "total": len(checks),
        },
    }
    Path(__file__).with_name(
        "TIR_MUMMU_QHTRI_PNLF_TRAJECTORY_RECEIPT_BINDING_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
