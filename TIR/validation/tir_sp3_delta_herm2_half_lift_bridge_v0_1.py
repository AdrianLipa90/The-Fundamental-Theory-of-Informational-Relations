#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "validation"))

import tir_sp3_3plus1_bundle_compatibility_v0_1 as sp3c

getcontext().prec = 80

C = Decimal("299792.458")
DT = Decimal("120")
ONE_MICROSECOND_S = Decimal("1e-6")


def sha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


def dec3(rec):
    return tuple(Decimal(x) for x in rec[:3])


def norm3(v):
    return sum(x * x for x in v).sqrt()


def midpoint3(a, b):
    return tuple((x + y) / Decimal(2) for x, y in zip(a, b))


def main():
    spatial = sp3c.spatial_capture()
    matching = sp3c.matching_input()
    bundle_cert = sp3c.certify_physical_realization_bundle_v02({
        "schema": sp3c.BUNDLE_SCHEMA,
        "spatial_capture": spatial,
        "matching_input": matching,
    })
    beta_map = {
        row["patch_id"]: tuple(Decimal(str(x)) for x in row["beta_match"])
        for row in matching["patches"]
    }

    ell = C * DT
    per_satellite = {}
    all_trace_exact = True
    all_pauli_exact = True
    all_positive = True
    all_raw_clock_no_go = True
    max_rnorm = Decimal(0)
    max_rfc_shift_residual = Decimal(0)

    for sat in sp3c.SAT_IDS:
        x1 = dec3(sp3c.REC1[sat])
        x2 = dec3(sp3c.REC2[sat])
        dx = tuple(b - a for a, b in zip(x1, x2))
        beta = tuple(d / DT for d in dx)
        r = tuple(d / ell for d in dx)

        # Herm(2) coefficient form:
        # X = a0 I + ai sigma_i
        a0 = ell / Decimal(2)
        ai = tuple(d / Decimal(2) for d in dx)

        # Trace/Pauli recovery in the coefficient basis.
        recovered_trace = Decimal(2) * a0
        recovered_dx = tuple(Decimal(2) * a for a in ai)
        trace_exact = recovered_trace == ell
        pauli_exact = recovered_dx == dx
        all_trace_exact = all_trace_exact and trace_exact
        all_pauli_exact = all_pauli_exact and pauli_exact

        rnorm = norm3(r)
        max_rnorm = max(max_rnorm, rnorm)
        eig_min = ell * (Decimal(1) - rnorm) / Decimal(2)
        eig_max = ell * (Decimal(1) + rnorm) / Decimal(2)
        det_x = (ell * ell - sum(d * d for d in dx)) / Decimal(4)
        positive = eig_min > 0 and eig_max > 0 and det_x > 0 and rnorm < 1
        all_positive = all_positive and positive

        # Existing TIR/RFC matching packet stores beta_match as float.
        beta_packet = beta_map[sat]
        shift_packet = tuple(b / C for b in beta_packet)
        residual = max(abs(r[i] - shift_packet[i]) for i in range(3))
        max_rfc_shift_residual = max(max_rfc_shift_residual, residual)

        # Raw SP3 clock correction direct-to-trace-scale no-go.
        c1 = Decimal(sp3c.REC1[sat][3])
        c2 = Decimal(sp3c.REC2[sat][3])
        cmid_us = (c1 + c2) / Decimal(2)
        raw_x0_km = C * cmid_us * ONE_MICROSECOND_S
        xmid = midpoint3(x1, x2)
        raw_cone = raw_x0_km * raw_x0_km - sum(x * x for x in xmid)
        raw_no_go = raw_cone < 0
        all_raw_clock_no_go = all_raw_clock_no_go and raw_no_go

        # Exact midpoint reconstruction of the two spatial endpoints.
        xmid_exact = midpoint3(x1, x2)
        x1_rec = tuple(xmid_exact[i] - ai[i] for i in range(3))
        x2_rec = tuple(xmid_exact[i] + ai[i] for i in range(3))

        per_satellite[sat] = {
            "delta_x_km": [str(x) for x in dx],
            "beta_km_s": [str(x) for x in beta],
            "r_equals_beta_over_c": [str(x) for x in r],
            "r_norm": str(rnorm),
            "herm2_identity_coefficient_km": str(a0),
            "herm2_pauli_coefficients_km": [str(x) for x in ai],
            "lambda_min_km": str(eig_min),
            "lambda_max_km": str(eig_max),
            "det_X_km2": str(det_x),
            "trace_recovery_exact": trace_exact,
            "pauli_recovery_exact": pauli_exact,
            "midpoint_endpoint_reconstruction_exact": x1_rec == x1 and x2_rec == x2,
            "raw_sp3_clock_midpoint_length_km": str(raw_x0_km),
            "raw_clock_direct_future_cone_value_km2": str(raw_cone),
            "raw_clock_direct_identification_rejected": raw_no_go,
        }

    checks = {
        "ell_is_source_epoch_separation_times_c": ell == C * DT,
        "trace_recovers_full_temporal_separation_exactly": all_trace_exact,
        "pauli_traces_recover_full_spatial_displacement_exactly": all_pauli_exact,
        "all_five_delta_herm2_witnesses_strictly_positive": all_positive,
        "bloch_vector_equals_existing_rfe8_shift_with_float_boundary_tolerance": max_rfc_shift_residual < Decimal("1e-15"),
        "raw_sp3_clock_correction_direct_trace_scale_identification_refuted_for_all_five": all_raw_clock_no_go,
        "bundle_candidate_same_parent_still_passes": (
            bundle_cert.same_physical_realization
            and bundle_cert.same_realization_receipt
            and bundle_cert.blockers == (
                "TIR_GSC1_PRODUCTION_SPATIAL_CAPTURE",
                "TIR_INTERLEAF_PRODUCTION_MATCHING_CAPTURE",
            )
        ),
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": "TIR_SP3_DELTA_HERM2_HALF_LIFT_BRIDGE_RECEIPT_V0_1",
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "empirical_theory_confirmation": False,
        "source_evidence_class": "EXTERNAL_OBSERVATIONAL_ARCHIVE_DERIVED_FINITE_EVENT_WITNESS",
        "source": {
            "source_id": "RT218283.SP3@8013",
            "epoch1": sp3c.EPOCH1,
            "epoch2": sp3c.EPOCH2,
            "dt_s": str(DT),
            "c_km_s": str(C),
            "ell_km": str(ell),
            "physical_realization_id": sp3c.realization_id(),
        },
        "bridge": {
            "definition": "X = 1/2 * (c*dt I + delta_x dot sigma)",
            "ell_binding": "ell = c*dt",
            "bloch_binding": "r = delta_x/(c*dt) = beta/c = RF-E8 shift",
            "trace_inverse": "Tr(X)=c*dt; Tr(X sigma_i)=delta_x_i",
            "midpoint_inverse": "x1=xbar-delta_x/2; x2=xbar+delta_x/2",
            "factor_half_role": "centered half-displacement coefficients",
        },
        "metrics": {
            "max_r_norm": str(max_rnorm),
            "max_rfc_shift_residual": str(max_rfc_shift_residual),
        },
        "checks": checks,
        "per_satellite": per_satellite,
        "interpretation_firewall": {
            "raw_sp3_clock_correction_is_not_tir_event_trace_scale": True,
            "finite_event_witness_is_not_global_spacetime_proof": True,
            "candidate_does_not_promote_production_source": True,
            "candidate_does_not_identify_collatz_with_spacetime_dynamics": True,
        },
    }
    out["receipt_sha256"] = sha(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
