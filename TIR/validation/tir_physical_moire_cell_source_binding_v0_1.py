#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

HBAR = 1.054571817e-34
C0 = 299792458.0

C_DELTA_FS = 8.0 / (9.0 * math.sqrt(3.0) * math.pi)
Q_DELTA_FS = C_DELTA_FS ** (-1.0 / 3.0)
AHAT_DELTA = math.sqrt(8.0 / 3.0)
GAMMA_DELTA_M = AHAT_DELTA * Q_DELTA_FS

SCHEMA = "tir.physical-moire-cell-binding/v0.1"
CAL_ROLE = "MUMMU_PHASE_CLOCK_CELL_CANDIDATE"
VALID_KINDS = {"TIR_TETRA_EDGE", "PHASE_FREQUENCY", "REST_MASS"}
SOURCE_CLASSES = {"PRODUCTION_SOURCE", "REFERENCE_CONTROL", "CANDIDATE_SOURCE"}


class ContractError(ValueError):
    pass


def _finite_positive(x, name):
    y = float(x)
    if not math.isfinite(y) or y <= 0.0:
        raise ContractError(f"{name} must be finite and positive")
    return y


def _finite_nonnegative(x, name):
    y = float(x)
    if not math.isfinite(y) or y < 0.0:
        raise ContractError(f"{name} must be finite and nonnegative")
    return y


def _sha256(s, name):
    if not isinstance(s, str) or len(s) != 64:
        raise ContractError(f"{name} must be a 64-hex digest")
    try:
        int(s, 16)
    except ValueError as exc:
        raise ContractError(f"{name} must be hexadecimal") from exc
    return s.lower()


def _source_ref(s, name):
    if not isinstance(s, str) or not s.strip():
        raise ContractError(f"{name} must be non-empty")
    return s.strip()


def _sigma_from_relative(value, sigma):
    if sigma is None:
        return None
    s = _finite_nonnegative(sigma, "uncertainty")
    return s


def _ratio_record(kind, observed, predicted, sigma_observed, sigma_predicted=0.0):
    defect = abs(observed - predicted) / max(abs(observed), abs(predicted))
    denom = math.hypot(sigma_observed or 0.0, sigma_predicted or 0.0)
    z = None if denom == 0.0 else (observed - predicted) / denom
    return {
        "kind": kind,
        "observed": observed,
        "predicted": predicted,
        "relative_defect": defect,
        "z_score": z,
    }


def validate_packet(packet):
    if packet.get("schema") != SCHEMA:
        raise ContractError(f"schema must be {SCHEMA}")

    rid = _source_ref(packet.get("physical_realization_id"), "physical_realization_id")
    source_class = packet.get("source_class")
    if source_class not in SOURCE_CLASSES:
        raise ContractError("invalid source_class")

    cal = packet.get("calibration")
    if not isinstance(cal, dict):
        raise ContractError("calibration must be an object")
    if cal.get("role") != CAL_ROLE:
        raise ContractError(f"calibration.role must be {CAL_ROLE}")

    cal_ref = _source_ref(cal.get("source_ref"), "calibration.source_ref")
    cal_sha = _sha256(cal.get("source_sha256"), "calibration.source_sha256")

    a_direct = cal.get("a_m_m")
    l_m = cal.get("l_m_m")
    twist = cal.get("twist_rad")

    if a_direct is None and (l_m is None or twist is None):
        raise ContractError("supply a_m_m or both l_m_m and twist_rad")

    a_direct_v = None if a_direct is None else _finite_positive(a_direct, "a_m_m")
    a_direct_sigma = None
    if a_direct_v is not None and cal.get("a_m_sigma_m") is not None:
        a_direct_sigma = _finite_nonnegative(cal.get("a_m_sigma_m"), "a_m_sigma_m")

    a_moire = None
    a_moire_sigma = None
    if l_m is not None or twist is not None:
        if l_m is None or twist is None:
            raise ContractError("l_m_m and twist_rad must be supplied together")
        L = _finite_positive(l_m, "l_m_m")
        th = float(twist)
        if not math.isfinite(th) or th == 0.0 or abs(th) >= math.pi:
            raise ContractError("twist_rad must be finite with 0 < |twist| < pi")
        s = math.sin(abs(th) / 2.0)
        a_moire = 2.0 * L * s

        sigL = 0.0
        sigT = 0.0
        if cal.get("l_m_sigma_m") is not None:
            sigL = _finite_nonnegative(cal.get("l_m_sigma_m"), "l_m_sigma_m")
        if cal.get("twist_sigma_rad") is not None:
            sigT = _finite_nonnegative(cal.get("twist_sigma_rad"), "twist_sigma_rad")
        da_dL = 2.0 * s
        da_dT = L * math.cos(abs(th) / 2.0)
        a_moire_sigma = math.hypot(da_dL * sigL, da_dT * sigT)

    if a_direct_v is not None:
        a_m = a_direct_v
        a_sigma = a_direct_sigma or 0.0
        calibration_mode = "DIRECT"
    else:
        a_m = a_moire
        a_sigma = a_moire_sigma or 0.0
        calibration_mode = "MOIRE_RECONSTRUCTED"

    consistency = None
    if a_direct_v is not None and a_moire is not None:
        rel = abs(a_direct_v - a_moire) / max(a_direct_v, a_moire)
        den = math.hypot(a_direct_sigma or 0.0, a_moire_sigma or 0.0)
        z = None if den == 0.0 else (a_direct_v - a_moire) / den
        consistency = {
            "a_direct_m": a_direct_v,
            "a_moire_m": a_moire,
            "relative_defect": rel,
            "z_score": z,
        }

    vals = packet.get("validations")
    if not isinstance(vals, list) or len(vals) < 1:
        raise ContractError("at least one independent validation is required")

    predictions = {
        "a_m_m": a_m,
        "L_delta_pred_m": GAMMA_DELTA_M * a_m,
        "omega_phase_pred_rad_s": C0 / a_m,
        "rest_mass_pred_kg": HBAR / (C0 * a_m),
        "rest_energy_pred_J": HBAR * C0 / a_m,
        "m_inverse_length_pred_per_m": 1.0 / a_m,
    }

    records = []
    validation_shas = set()
    for idx, item in enumerate(vals):
        if not isinstance(item, dict):
            raise ContractError(f"validation[{idx}] must be an object")
        kind = item.get("kind")
        if kind not in VALID_KINDS:
            raise ContractError(f"validation[{idx}].kind invalid")
        if item.get("same_physical_mode") is not True:
            raise ContractError(f"validation[{idx}] must declare same_physical_mode=true")
        ref = _source_ref(item.get("source_ref"), f"validation[{idx}].source_ref")
        sha = _sha256(item.get("source_sha256"), f"validation[{idx}].source_sha256")
        if sha == cal_sha:
            raise ContractError("anti-circularity failure: calibration and validation share source digest")
        validation_shas.add(sha)

        value = _finite_positive(item.get("value"), f"validation[{idx}].value")
        sigma = 0.0
        if item.get("sigma") is not None:
            sigma = _finite_nonnegative(item.get("sigma"), f"validation[{idx}].sigma")

        if kind == "TIR_TETRA_EDGE":
            ratio = value / a_m
            pred_ratio = GAMMA_DELTA_M
            # first-order ratio uncertainty, treating a_m calibration uncertainty explicitly
            sig_ratio = math.hypot(sigma / a_m, value * a_sigma / (a_m * a_m))
        elif kind == "PHASE_FREQUENCY":
            ratio = value * a_m / C0
            pred_ratio = 1.0
            sig_ratio = math.hypot(a_m * sigma / C0, value * a_sigma / C0)
        else:
            ratio = value * C0 * a_m / HBAR
            pred_ratio = 1.0
            sig_ratio = math.hypot(C0 * a_m * sigma / HBAR, value * C0 * a_sigma / HBAR)

        rec = _ratio_record(kind, ratio, pred_ratio, sig_ratio)
        rec.update({"source_ref": ref, "source_sha256": sha})
        records.append(rec)

    production_status = "NON_PRODUCTION"
    if source_class == "PRODUCTION_SOURCE":
        if rid.lower().startswith(("synthetic", "reference", "fixture", "runtime")):
            raise ContractError("production realization id may not be synthetic/reference/runtime")
        production_status = "PRODUCTION_PACKET_STRUCTURE_PASS"

    return {
        "schema": SCHEMA,
        "structure_status": "PASS",
        "production_status": production_status,
        "physical_realization_id": rid,
        "source_class": source_class,
        "calibration": {
            "mode": calibration_mode,
            "source_ref": cal_ref,
            "source_sha256": cal_sha,
            "a_m_m": a_m,
            "a_m_sigma_m": a_sigma,
            "direct_vs_moire": consistency,
        },
        "constants": {
            "C_delta_fs": C_DELTA_FS,
            "Q_delta_fs": Q_DELTA_FS,
            "a_hat_delta": AHAT_DELTA,
            "gamma_delta_M": GAMMA_DELTA_M,
        },
        "predictions": predictions,
        "anti_circularity": {
            "status": "PASS",
            "validation_source_count": len(validation_shas),
            "calibration_digest_distinct_from_all_validations": True,
        },
        "validation_records": records,
        "open_gates": [
            "MUMMU_PHYSICAL_CELL_REALIZATION",
            "SAME_PHYSICAL_MODE_BINDING",
            "RADIAL_INFORMATION_SOURCE_BINDING",
            "PHYSICAL_JOINT_INFORMATION_STATE_BINDING",
            "COMMON_RELATIONAL_AREA_SOURCE_BINDING",
            "TIR_RFC_CELL_CHART_SOURCE_BINDING",
            "TRANSLATIONAL_OBSERVABLE",
            "GENERAL_MATTER_MULTIPLET",
        ],
        "canon_allowed": False,
    }


def _reference_fixture():
    a = 2.0e-6
    l_delta = GAMMA_DELTA_M * a
    omega = C0 / a
    mass = HBAR / (C0 * a)
    return {
        "schema": SCHEMA,
        "physical_realization_id": "reference-fixture-001",
        "source_class": "REFERENCE_CONTROL",
        "calibration": {
            "role": CAL_ROLE,
            "source_ref": "reference://moire-cell",
            "source_sha256": hashlib.sha256(b"calibration").hexdigest(),
            "a_m_m": a,
            "a_m_sigma_m": 1.0e-9,
        },
        "validations": [
            {
                "kind": "TIR_TETRA_EDGE",
                "source_ref": "reference://tetra-edge",
                "source_sha256": hashlib.sha256(b"tetra-edge").hexdigest(),
                "same_physical_mode": True,
                "value": l_delta,
                "sigma": 2.0e-9,
            },
            {
                "kind": "PHASE_FREQUENCY",
                "source_ref": "reference://phase-frequency",
                "source_sha256": hashlib.sha256(b"phase-frequency").hexdigest(),
                "same_physical_mode": True,
                "value": omega,
                "sigma": 1.0e8,
            },
            {
                "kind": "REST_MASS",
                "source_ref": "reference://rest-mass",
                "source_sha256": hashlib.sha256(b"rest-mass").hexdigest(),
                "same_physical_mode": True,
                "value": mass,
                "sigma": mass * 1.0e-3,
            },
        ],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("packet", nargs="?")
    ap.add_argument("--reference-fixture", action="store_true")
    ns = ap.parse_args()

    if ns.reference_fixture:
        packet = _reference_fixture()
    elif ns.packet:
        packet = json.loads(Path(ns.packet).read_text())
    else:
        raise SystemExit("provide packet JSON or --reference-fixture")

    try:
        out = validate_packet(packet)
    except ContractError as exc:
        print(json.dumps({"schema": SCHEMA, "structure_status": "FAIL", "error": str(exc)}, indent=2))
        raise SystemExit(1)

    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
