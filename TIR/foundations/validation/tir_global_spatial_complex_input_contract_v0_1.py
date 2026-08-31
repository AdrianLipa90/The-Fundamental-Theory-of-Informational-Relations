#!/usr/bin/env python3
"""Fail-closed input contract for a production TIR global spatial complex."""
from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from typing import Any

from tir_global_3manifold_smooth_certificate_v0_1 import (
    boundary_of_4_simplex,
    certify_closed_combinatorial_3manifold,
)

SCHEMA = "TIR_GLOBAL_SPATIAL_COMPLEX_INPUT_V0_1"


class SpatialComplexInputError(ValueError):
    """Raised when a supplied spatial-complex dataset violates the input contract."""


@dataclass(frozen=True)
class SpatialComplexInputCertificate:
    input_valid: bool
    integrity_valid: bool
    manifold_certified: bool
    production_input: bool
    promotion_eligible: bool
    dataset_id: str
    incidence_sha256: str
    manifold_receipt: dict[str, Any]


def _require_nonempty_string(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise SpatialComplexInputError(f"{name} must be a non-empty string")
    return value.strip()


def _canonical_incidence_payload(vertices, tetrahedra):
    return {
        "vertices": sorted(vertices),
        "tetrahedra": sorted([list(sorted(tet)) for tet in tetrahedra]),
    }


def incidence_sha256(vertices, tetrahedra):
    payload = _canonical_incidence_payload(vertices, tetrahedra)
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def build_input_dataset(*, dataset_id, vertices, tetrahedra, source, source_commit_or_digest, production):
    return {
        "schema": SCHEMA,
        "dataset_id": dataset_id,
        "representation": "closed_tetrahedral_complex",
        "production": bool(production),
        "provenance": {
            "source": source,
            "source_commit_or_digest": source_commit_or_digest,
        },
        "vertices": list(vertices),
        "tetrahedra": [list(tet) for tet in tetrahedra],
        "incidence_sha256": incidence_sha256(vertices, tetrahedra),
    }


def validate_input_dataset(data):
    if not isinstance(data, dict):
        raise SpatialComplexInputError("dataset must be a JSON object")
    if data.get("schema") != SCHEMA:
        raise SpatialComplexInputError(f"schema must equal {SCHEMA}")
    dataset_id = _require_nonempty_string(data.get("dataset_id"), "dataset_id")
    if data.get("representation") != "closed_tetrahedral_complex":
        raise SpatialComplexInputError("representation must be closed_tetrahedral_complex")
    if type(data.get("production")) is not bool:
        raise SpatialComplexInputError("production must be a boolean")

    provenance = data.get("provenance")
    if not isinstance(provenance, dict):
        raise SpatialComplexInputError("provenance must be an object")
    _require_nonempty_string(provenance.get("source"), "provenance.source")
    _require_nonempty_string(
        provenance.get("source_commit_or_digest"),
        "provenance.source_commit_or_digest",
    )

    raw_vertices = data.get("vertices")
    if not isinstance(raw_vertices, list) or not raw_vertices:
        raise SpatialComplexInputError("vertices must be a non-empty list")
    vertices = [_require_nonempty_string(v, "vertex id") for v in raw_vertices]
    if len(set(vertices)) != len(vertices):
        raise SpatialComplexInputError("vertex ids must be unique")
    vertex_set = set(vertices)

    raw_tetrahedra = data.get("tetrahedra")
    if not isinstance(raw_tetrahedra, list) or not raw_tetrahedra:
        raise SpatialComplexInputError("tetrahedra must be a non-empty list")
    tetrahedra = []
    for index, raw_tet in enumerate(raw_tetrahedra):
        if not isinstance(raw_tet, list) or len(raw_tet) != 4:
            raise SpatialComplexInputError(f"tetrahedron {index} must contain exactly four vertex ids")
        tet_values = tuple(_require_nonempty_string(v, f"tetrahedron {index} vertex") for v in raw_tet)
        if len(set(tet_values)) != 4:
            raise SpatialComplexInputError(f"tetrahedron {index} repeats a vertex")
        missing = set(tet_values) - vertex_set
        if missing:
            raise SpatialComplexInputError(
                f"tetrahedron {index} references undeclared vertices: {sorted(missing)}"
            )
        tetrahedra.append(tet_values)

    used_vertices = {v for tet in tetrahedra for v in tet}
    unused = vertex_set - used_vertices
    if unused:
        raise SpatialComplexInputError(f"declared vertices are unused: {sorted(unused)}")

    supplied_digest = _require_nonempty_string(data.get("incidence_sha256"), "incidence_sha256")
    computed_digest = incidence_sha256(vertices, tetrahedra)
    if supplied_digest != computed_digest:
        raise SpatialComplexInputError(
            f"incidence_sha256 mismatch: supplied={supplied_digest}, computed={computed_digest}"
        )

    manifold_ok, manifold_receipt = certify_closed_combinatorial_3manifold(tetrahedra)
    production = data["production"]
    return SpatialComplexInputCertificate(
        input_valid=True,
        integrity_valid=True,
        manifold_certified=bool(manifold_ok),
        production_input=production,
        promotion_eligible=bool(production and manifold_ok),
        dataset_id=dataset_id,
        incidence_sha256=computed_digest,
        manifold_receipt=manifold_receipt,
    )


def reference_dataset(*, production=False):
    tetrahedra = [tuple(str(v) for v in tet) for tet in boundary_of_4_simplex()]
    vertices = sorted({v for tet in tetrahedra for v in tet})
    return build_input_dataset(
        dataset_id="reference-boundary-of-4-simplex",
        vertices=vertices,
        tetrahedra=tetrahedra,
        source="TIR A5 reference control only",
        source_commit_or_digest="REFERENCE_CONTROL_NOT_PRODUCTION",
        production=production,
    )


def main():
    checks = []

    reference = reference_dataset(production=False)
    cert = validate_input_dataset(reference)
    checks.append({
        "name": "reference_input_contract_and_A5_certificate_pass",
        "pass": cert.input_valid and cert.integrity_valid and cert.manifold_certified,
    })
    checks.append({
        "name": "reference_control_cannot_promote_without_production_flag",
        "pass": not cert.production_input and not cert.promotion_eligible,
    })

    tampered = json.loads(json.dumps(reference))
    tampered["tetrahedra"][0][0] = "999"
    try:
        validate_input_dataset(tampered)
        tamper_rejected = False
    except SpatialComplexInputError:
        tamper_rejected = True
    checks.append({"name": "tampered_incidence_rejected", "pass": tamper_rejected})

    missing_provenance = json.loads(json.dumps(reference))
    missing_provenance["provenance"]["source"] = ""
    try:
        validate_input_dataset(missing_provenance)
        provenance_rejected = False
    except SpatialComplexInputError:
        provenance_rejected = True
    checks.append({"name": "missing_provenance_rejected", "pass": provenance_rejected})

    open_complex = json.loads(json.dumps(reference))
    open_complex["tetrahedra"] = open_complex["tetrahedra"][:-1]
    open_tets = [tuple(t) for t in open_complex["tetrahedra"]]
    open_complex["vertices"] = sorted({v for tet in open_tets for v in tet})
    open_complex["incidence_sha256"] = incidence_sha256(open_complex["vertices"], open_tets)
    open_cert = validate_input_dataset(open_complex)
    checks.append({
        "name": "valid_input_contract_does_not_mask_nonmanifold_complex",
        "pass": open_cert.input_valid
        and open_cert.integrity_valid
        and not open_cert.manifold_certified
        and not open_cert.promotion_eligible,
    })

    passed = all(check["pass"] for check in checks)
    receipt = {
        "schema": "TIR_GLOBAL_SPATIAL_COMPLEX_INPUT_CONTRACT_VALIDATION_V0_1",
        "technical_status": "PASS" if passed else "FAIL",
        "verdict": (
            "PASS_TIR_GLOBAL_SPATIAL_COMPLEX_INPUT_CONTRACT_WITH_PRODUCTION_INPUT_OPEN"
            if passed
            else "FAIL_TIR_GLOBAL_SPATIAL_COMPLEX_INPUT_CONTRACT"
        ),
        "production_spatial_complex": "OPEN_INPUT",
        "promotion_rule": "production=true AND integrity_valid AND manifold_certified",
        "reference_control_promotion_eligible": cert.promotion_eligible,
        "checks": checks,
        "reference_certificate": asdict(cert),
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
