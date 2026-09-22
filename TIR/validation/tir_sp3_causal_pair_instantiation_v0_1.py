#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from decimal import Decimal, getcontext
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
VALIDATION = ROOT / "validation"
sys.path.insert(0, str(VALIDATION))

import tir_sp3_3plus1_bundle_compatibility_v0_1 as sp3c

getcontext().prec = 80

C = Decimal("299792.458")
DT = Decimal("120")
TWO = Decimal(2)
FOUR = Decimal(4)
ONE_MICROSECOND_S = Decimal("1e-6")

THEOREM_RECEIPT = VALIDATION / "TIR_CAUSAL_3PLUS1_PAIR_CLOSURE_V0_1.json"
SP3_RECEIPT = VALIDATION / "TIR_SP3_DELTA_HERM2_HALF_LIFT_BRIDGE_V0_1.json"


def sha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def dec3(rec):
    return tuple(Decimal(x) for x in rec[:3])


def midpoint3(a, b):
    return tuple((x + y) / TWO for x, y in zip(a, b))


def norm_sq(v):
    return sum(x * x for x in v)


def main():
    theorem = load_json(THEOREM_RECEIPT)
    sp3_parent = load_json(SP3_RECEIPT)

    spatial = sp3c.spatial_capture()
    matching = sp3c.matching_input()
    bundle_cert = sp3c.certify_physical_realization_bundle_v02(
        {
            "schema": sp3c.BUNDLE_SCHEMA,
            "spatial_capture": spatial,
            "matching_input": matching,
        }
    )
    beta_map = {
        row["patch_id"]: tuple(Decimal(str(x)) for x in row["beta_match"])
        for row in matching["patches"]
    }

    ell = C * DT
    per_satellite = {}
    all_checks = []
    minimum_normalized_causal_margin = None
    minimum_full_difference_det = None
    minimum_half_difference_det = None
    maximum_shift_residual = Decimal(0)

    for sat in sp3c.SAT_IDS:
        x1 = dec3(sp3c.REC1[sat])
        x2 = dec3(sp3c.REC2[sat])
        dx = tuple(b - a for a, b in zip(x1, x2))
        dx2 = norm_sq(dx)

        # Full theorem-level difference:
        # D = ell I + dx.sigma
        # Half-difference:
        # H = D/2 = ell/2 I + dx/2 . sigma
        d0 = ell
        di = dx
        h0 = ell / TWO
        hi = tuple(v / TWO for v in dx)

        det_D = d0 * d0 - norm_sq(di)
        det_H_from_coefficients = h0 * h0 - norm_sq(hi)
        det_H_from_scaling = det_D / FOUR
        determinant_scaling_exact = det_H_from_coefficients == det_H_from_scaling

        r = tuple(v / ell for v in dx)
        r2 = norm_sq(r)
        normalized_causal_margin = Decimal(1) - r2
        determinant_margin_identity = (
            FOUR * det_H_from_coefficients / (ell * ell)
            == normalized_causal_margin
        )

        rnorm = r2.sqrt()
        h_lambda_min = (ell - dx2.sqrt()) / TWO
        h_lambda_max = (ell + dx2.sqrt()) / TWO
        d_lambda_min = ell - dx2.sqrt()
        strict_psd_future = (
            h_lambda_min > 0
            and h_lambda_max > 0
            and d_lambda_min > 0
            and det_H_from_coefficients > 0
            and det_D > 0
            and rnorm < 1
        )

        # Exact theorem centered endpoint realization A=-H, B=+H.
        A = (-h0,) + tuple(-v for v in hi)
        B = (h0,) + hi
        midpoint = tuple((a + b) / TWO for a, b in zip(A, B))
        halfdiff = tuple((b - a) / TWO for a, b in zip(A, B))
        full_difference = tuple(b - a for a, b in zip(A, B))
        H_coeff = (h0,) + hi
        D_coeff = (d0,) + di
        centered_midpoint_zero_exact = midpoint == (Decimal(0),) * 4
        centered_halfdifference_exact = halfdiff == H_coeff
        centered_full_difference_exact = full_difference == D_coeff

        # Observed spatial midpoint reconstruction.
        xbar = midpoint3(x1, x2)
        x1_rec = tuple(xbar[i] - hi[i] for i in range(3))
        x2_rec = tuple(xbar[i] + hi[i] for i in range(3))
        observed_midpoint_reconstruction_exact = x1_rec == x1 and x2_rec == x2

        # Lossless trace/Pauli coefficient recovery.
        trace_recovery_exact = TWO * h0 == ell
        pauli_recovery_exact = tuple(TWO * v for v in hi) == dx

        # Existing RFC shift equality within the already-declared float boundary.
        beta_packet = beta_map[sat]
        shift_packet = tuple(v / C for v in beta_packet)
        shift_residual = max(abs(r[i] - shift_packet[i]) for i in range(3))
        maximum_shift_residual = max(maximum_shift_residual, shift_residual)
        shift_match = shift_residual < Decimal("1e-15")

        # Existing raw-clock no-go rechecked directly.
        c1 = Decimal(sp3c.REC1[sat][3])
        c2 = Decimal(sp3c.REC2[sat][3])
        cmid_us = (c1 + c2) / TWO
        raw_x0_km = C * cmid_us * ONE_MICROSECOND_S
        raw_cone = raw_x0_km * raw_x0_km - norm_sq(xbar)
        raw_clock_rejected = raw_cone < 0

        checks = {
            "lossless_trace_recovery": trace_recovery_exact,
            "lossless_pauli_recovery": pauli_recovery_exact,
            "minkowski_determinant_scaling_exact": determinant_scaling_exact,
            "normalized_causal_margin_identity_exact": determinant_margin_identity,
            "strict_theorem_PSD_future_cone": strict_psd_future,
            "centered_midpoint_zero_exact": centered_midpoint_zero_exact,
            "centered_halfdifference_equals_H_exact": centered_halfdifference_exact,
            "centered_full_difference_equals_D_exact": centered_full_difference_exact,
            "observed_spatial_midpoint_reconstruction_exact": observed_midpoint_reconstruction_exact,
            "normalized_vector_matches_existing_RFE8_shift": shift_match,
            "raw_SP3_clock_direct_event_trace_identification_rejected": raw_clock_rejected,
        }
        all_checks.extend(checks.values())

        if minimum_normalized_causal_margin is None or normalized_causal_margin < minimum_normalized_causal_margin:
            minimum_normalized_causal_margin = normalized_causal_margin
        if minimum_full_difference_det is None or det_D < minimum_full_difference_det:
            minimum_full_difference_det = det_D
        if minimum_half_difference_det is None or det_H_from_coefficients < minimum_half_difference_det:
            minimum_half_difference_det = det_H_from_coefficients

        per_satellite[sat] = {
            "delta_x_km": [str(v) for v in dx],
            "D_coefficients_km": [str(v) for v in D_coeff],
            "H_coefficients_km": [str(v) for v in H_coeff],
            "r_equals_beta_over_c": [str(v) for v in r],
            "r_norm": str(rnorm),
            "normalized_causal_margin_1_minus_r2": str(normalized_causal_margin),
            "det_D_km2": str(det_D),
            "det_H_km2": str(det_H_from_coefficients),
            "H_lambda_min_km": str(h_lambda_min),
            "shift_residual": str(shift_residual),
            "checks": checks,
        }

    parent_checks = {
        "causal_theorem_parent_PASS": theorem.get("status") == "PASS",
        "causal_theorem_parent_candidate_only": theorem.get("authority") == "CANDIDATE_ONLY",
        "causal_theorem_does_not_claim_physical_event_binding": theorem.get("physical_event_binding_claim") is False,
        "causal_theorem_minkowski_signature_check_PASS": theorem.get("checks", {}).get(
            "determinant_hessian_is_minkowski_diag_plus_minus_minus_minus"
        ) is True,
        "causal_theorem_half_factor_uniqueness_PASS": theorem.get("checks", {}).get(
            "midpoint_half_difference_factor_one_half_is_unique"
        ) is True,
        "sp3_parent_PASS": sp3_parent.get("status") == "PASS",
        "sp3_parent_candidate_only": sp3_parent.get("authority") == "CANDIDATE_ONLY",
        "sp3_parent_no_physical_production_claim": sp3_parent.get("physical_production_claim") is False,
        "same_realization_bundle_gate_still_passes": (
            bundle_cert.same_physical_realization
            and bundle_cert.same_realization_receipt
        ),
    }

    global_checks = {
        **parent_checks,
        "all_five_frozen_pairs_instantiate_strict_theorem_future_cone": all(all_checks),
        "all_five_have_positive_normalized_causal_margin": minimum_normalized_causal_margin is not None
        and minimum_normalized_causal_margin > 0,
        "all_five_full_difference_determinants_positive": minimum_full_difference_det is not None
        and minimum_full_difference_det > 0,
        "all_five_half_difference_determinants_positive": minimum_half_difference_det is not None
        and minimum_half_difference_det > 0,
        "RFE8_shift_boundary_residual_below_1e_15": maximum_shift_residual < Decimal("1e-15"),
        "finite_compatibility_is_not_universal_empirical_confirmation": True,
        "physical_event_identity_not_promoted": True,
        "production_source_not_promoted": True,
    }

    status = "PASS" if all(global_checks.values()) else "FAIL"
    out = {
        "schema": "TIR_SP3_CAUSAL_PAIR_INSTANTIATION_RECEIPT_V0_1",
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "physical_event_binding_claim": False,
        "empirical_theory_confirmation": False,
        "evidence_class": "FINITE_EXTERNAL_SOURCE_COMPATIBILITY_WITNESS",
        "source": {
            "source_id": "RT218283.SP3@8013",
            "epoch1": sp3c.EPOCH1,
            "epoch2": sp3c.EPOCH2,
            "dt_s": str(DT),
            "c_km_s": str(C),
            "pair_count": len(sp3c.SAT_IDS),
            "physical_realization_id": sp3c.realization_id(),
        },
        "parent_receipts": {
            "causal_theorem_executable_receipt_sha256": theorem.get("executable_receipt_sha256"),
            "sp3_half_lift_candidate_receipt_sha256": sp3_parent.get("candidate_receipt_sha256"),
        },
        "bridge": {
            "full_difference": "D = c*dt I + delta_x dot sigma",
            "half_difference": "H = D/2",
            "minkowski_invariant": "det(D)=(c*dt)^2-|delta_x|^2",
            "half_invariant": "det(H)=det(D)/4",
            "normalized_margin": "4 det(H)/(c*dt)^2 = 1-|r|^2",
            "centered_pair": "A=-H; B=+H; (B-A)/2=H",
            "causal_order": "A<B because B-A=D is positive definite",
        },
        "metrics": {
            "minimum_normalized_causal_margin": str(minimum_normalized_causal_margin),
            "minimum_det_D_km2": str(minimum_full_difference_det),
            "minimum_det_H_km2": str(minimum_half_difference_det),
            "maximum_RFE8_shift_residual": str(maximum_shift_residual),
        },
        "checks": global_checks,
        "per_satellite": per_satellite,
        "interpretation_firewall": {
            "finite_source_compatibility_is_not_global_physical_spacetime_identity": True,
            "lossless_representation_is_not_proof_that_nature_ontologically_is_Herm2": True,
            "five_timelike_witnesses_do_not_establish_universal_causality_law": True,
            "raw_SP3_clock_correction_remains_rejected_as_event_trace_scale": True,
            "production_source_admission_remains_open": True,
        },
        "remaining_physical_gate": [
            "independent physical justification that local event translations use the Herm(2) carrier",
            "independent physical justification that future causality is the Hermitian PSD cone order",
            "production-grade source admission beyond the frozen finite archive witness",
        ],
    }
    out["receipt_sha256"] = sha(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
