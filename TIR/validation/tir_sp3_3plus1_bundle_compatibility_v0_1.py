#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from decimal import Decimal, getcontext
from itertools import combinations
from pathlib import Path

import numpy as np

FOUNDATION_VALIDATION = Path(__file__).resolve().parents[1] / "foundations" / "validation"
sys.path.insert(0, str(FOUNDATION_VALIDATION))

from tir_interleaf_matching_field_input_contract_v0_1 import payload_sha256
from tir_production_realization_binding_v0_2 import (
    BUNDLE_SCHEMA,
    MATCHING_SCHEMA,
    SPATIAL_SCHEMA,
    certify_matching_input_v02,
    certify_physical_realization_bundle_v02,
    certify_spatial_capture_v02,
)

getcontext().prec = 80

SOURCE_URL = "https://software.rtcm-ntrip.org/browser/ntrip/branches/BNC_2.12/Example_Configs/Input/RT218283.SP3?rev=8013"
SOURCE_REV = "8013"
EPOCH1 = "2015-01-21T00:01:00Z"
EPOCH2 = "2015-01-21T00:03:00Z"
DT = Decimal("120")
C_KM_S = 299792.458
SAT_IDS = ("G01", "G02", "G03", "G04", "G05")

REC1 = {
    "G01": ("-20211.852590", "-13534.722421", "-10912.571617", "-9.945341"),
    "G02": ("-2486.675251", "15651.983479", "21665.396870", "543.075190"),
    "G03": ("-13217.118012", "-20316.554735", "10814.894646", "161.246676"),
    "G04": ("-11048.109091", "-16496.227733", "-18079.087021", "-5.933971"),
    "G05": ("1415.296556", "25391.537629", "7286.804159", "-290.125298"),
}
REC2 = {
    "G01": ("-20043.488953", "-13516.640374", "-11240.133653", "-9.945279"),
    "G02": ("-2799.216197", "15576.603484", "21676.134685", "543.075198"),
    "G03": ("-13229.808727", "-20481.341421", "10482.835849", "161.249567"),
    "G04": ("-10782.320197", "-16449.365320", "-18281.546350", "-5.934176"),
    "G05": ("1347.312437", "25290.546183", "7641.773766", "-290.124639"),
}


def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sha(obj):
    return hashlib.sha256(canon(obj)).hexdigest()


def source_records():
    return {
        "source_url": SOURCE_URL,
        "source_revision": SOURCE_REV,
        "epochs": [EPOCH1, EPOCH2],
        "satellites": list(SAT_IDS),
        "epoch1": REC1,
        "epoch2": REC2,
    }


def source_sha():
    return sha(source_records())


def realization_id():
    return "physical:igs-sp3:sha256:" + source_sha()


def spatial_capture():
    tets = []
    for omitted in SAT_IDS:
        tets.append(tuple(s for s in SAT_IDS if s != omitted))
    cells = [
        {"cell_id": f"tet-{i}", "vertices": list(tet)}
        for i, tet in enumerate(sorted(tets))
    ]
    return {
        "schema": SPATIAL_SCHEMA,
        "physical_realization_id": realization_id(),
        "physical_realization_receipt_sha256": source_sha(),
        "capture_id": "igs-sp3-g01-g05-20150121T0001Z-candidate",
        "source": {
            "source_id": "RT218283.SP3@8013",
            "source_class": "CANDIDATE_SOURCE",
            "immutable_ref": SOURCE_URL,
        },
        "tetrahedral_cells": cells,
    }


def matching_input():
    p1 = {
        s: np.array([float(x) for x in REC1[s][:3]], dtype=float)
        for s in SAT_IDS
    }
    p2 = {
        s: np.array([float(x) for x in REC2[s][:3]], dtype=float)
        for s in SAT_IDS
    }
    beta = {s: (p2[s] - p1[s]) / float(DT) for s in SAT_IDS}
    patches = [
        {"patch_id": s, "beta_match": beta[s].tolist()}
        for s in SAT_IDS
    ]
    overlaps = []
    I = np.eye(3)
    for s in SAT_IDS[1:]:
        v = beta["G01"] - beta[s]
        overlaps.append(
            {
                "source": "G01",
                "target": s,
                "spatial_jacobian": I.tolist(),
                "time_drift": v.tolist(),
            }
        )
    digest = payload_sha256(
        temporal_coordinate_kind="t",
        c_scale=C_KM_S,
        patches=[
            {"patch_id": p["patch_id"], "beta_match": tuple(p["beta_match"])}
            for p in patches
        ],
        overlaps=[
            {
                "source": o["source"],
                "target": o["target"],
                "spatial_jacobian": tuple(tuple(row) for row in o["spatial_jacobian"]),
                "time_drift": tuple(o["time_drift"]),
            }
            for o in overlaps
        ],
    )
    return {
        "schema": MATCHING_SCHEMA,
        "physical_realization_id": realization_id(),
        "physical_realization_receipt_sha256": source_sha(),
        "dataset_id": "igs-sp3-interleaf-candidate-v02",
        "production": False,
        "provenance": {
            "source": "RT218283.SP3@8013 external archive derived candidate",
            "source_commit_or_digest": source_sha(),
        },
        "temporal_coordinate": {
            "kind": "t",
            "x0_binding": "x0=c*t",
            "c_scale": C_KM_S,
        },
        "patches": patches,
        "overlaps": overlaps,
        "payload_sha256": digest,
    }


def exact_two_epoch_reconstruction():
    ok = True
    for s in SAT_IDS:
        a = tuple(Decimal(x) for x in REC1[s])
        b = tuple(Decimal(x) for x in REC2[s])
        mid = tuple((x + y) / Decimal(2) for x, y in zip(a, b))
        rate = tuple((y - x) / DT for x, y in zip(a, b))
        a2 = tuple(m - DT * r / Decimal(2) for m, r in zip(mid, rate))
        b2 = tuple(m + DT * r / Decimal(2) for m, r in zip(mid, rate))
        ok = ok and a2 == a and b2 == b
    return ok


def main():
    spatial = spatial_capture()
    matching = matching_input()
    bundle = {
        "schema": BUNDLE_SCHEMA,
        "spatial_capture": spatial,
        "matching_input": matching,
    }

    sc = certify_spatial_capture_v02(spatial)
    mc = certify_matching_input_v02(matching)
    bc = certify_physical_realization_bundle_v02(bundle)

    expected_blockers = (
        "TIR_GSC1_PRODUCTION_SPATIAL_CAPTURE",
        "TIR_INTERLEAF_PRODUCTION_MATCHING_CAPTURE",
    )

    checks = {
        "source_record_is_literal_3plus1": all(
            len(REC1[s]) == 4 and len(REC2[s]) == 4 for s in SAT_IDS
        ),
        "two_epoch_midpoint_tangent_reconstructs_exact_decimal_source": exact_two_epoch_reconstruction(),
        "spatial_manifold_certified": sc.manifold_certified,
        "spatial_candidate_not_production": not sc.production_source_admitted,
        "spatial_not_promotion_eligible": not sc.promotion_review_eligible,
        "matching_handoff_compatible": mc.handoff_compatible,
        "matching_candidate_not_production": not mc.production_input,
        "matching_not_promotion_eligible": not mc.promotion_review_eligible,
        "same_physical_realization": bc.same_physical_realization,
        "same_realization_receipt": bc.same_realization_receipt,
        "bundle_not_promotion_eligible": not bc.promotion_review_eligible,
        "only_production_evidence_blockers_remain": bc.blockers == expected_blockers,
        "canon_allowed_false": not bc.canon_allowed,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": "TIR_SP3_3PLUS1_BUNDLE_COMPATIBILITY_RECEIPT_V0_1",
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "empirical_theory_confirmation": False,
        "source_evidence_class": "EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED_MODEL_LEVEL",
        "source_sha256": source_sha(),
        "physical_realization_id": realization_id(),
        "spatial": {
            "manifold_certified": sc.manifold_certified,
            "production_source_admitted": sc.production_source_admitted,
            "promotion_review_eligible": sc.promotion_review_eligible,
            "capture_sha256": sc.capture_sha256,
            "incidence_sha256": sc.incidence_sha256,
        },
        "matching": {
            "handoff_compatible": mc.handoff_compatible,
            "production_input": mc.production_input,
            "promotion_review_eligible": mc.promotion_review_eligible,
            "payload_sha256": mc.payload_sha256,
        },
        "bundle": {
            "same_physical_realization": bc.same_physical_realization,
            "same_realization_receipt": bc.same_realization_receipt,
            "spatial_ready": bc.spatial_ready,
            "matching_ready": bc.matching_ready,
            "promotion_review_eligible": bc.promotion_review_eligible,
            "blockers": list(bc.blockers),
        },
        "checks": checks,
        "interpretation_firewall": {
            "candidate_source_not_production_source": True,
            "archive_derived_topology_not_direct_spatial_measurement": True,
            "mnemonic_not_physical_evidence": True,
            "sp3_tuple_not_identified_with_herm2_event_carrier": True,
            "two_epoch_transform_not_identified_with_collatz": True,
        },
    }
    out["receipt_sha256"] = sha(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
