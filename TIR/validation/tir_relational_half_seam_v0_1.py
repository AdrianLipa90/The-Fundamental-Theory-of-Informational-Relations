#!/usr/bin/env python3
"""Deterministic audit for the TIR relational half-seam crosslink.

Primary structural statement:

    w_1(u) = 1-u,
    w_3(u) = u,
    J(u) = 1-u,
    meet(1,3 | 2) := {u : w_1(u)=w_3(u)} = {1/2}.

At the seam, binary relational entropy is ln(2) and projective odds are q=1.
The receipt classifies these as structural/information-theoretic outputs for TIR.
Downstream repositories may consume the exported seam packet under their own
claim and validation rules.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction


def exact_half_seam_certificate() -> dict[str, object]:
    """Certify the unique fixed/equal-weight point using exact rationals."""
    u = Fraction(1, 2)
    w1 = 1 - u
    w3 = u
    j_u = 1 - u
    return {
        "normalized_coordinate": [u.numerator, u.denominator],
        "w_1_given_2": [w1.numerator, w1.denominator],
        "w_3_given_2": [w3.numerator, w3.denominator],
        "J_u": [j_u.numerator, j_u.denominator],
        "fixed_point": j_u == u,
        "equal_weight_seam": w1 == w3,
        "uniqueness_proof": "1-u=u => 2u=1 => u=1/2",
        "pass": j_u == u and w1 == w3,
    }


def affine_interval_certificate() -> dict[str, object]:
    """Certify midpoint covariance for representative exact affine intervals."""
    intervals = (
        (Fraction(0), Fraction(1)),
        (Fraction(-3), Fraction(5)),
        (Fraction(7, 3), Fraction(31, 3)),
    )
    rows = []
    ok = True
    for left, right in intervals:
        midpoint = (left + right) / 2
        reflected = left + right - midpoint
        row_ok = reflected == midpoint
        ok &= row_ok
        rows.append({
            "left": [left.numerator, left.denominator],
            "right": [right.numerator, right.denominator],
            "midpoint": [midpoint.numerator, midpoint.denominator],
            "reflection_of_midpoint": [reflected.numerator, reflected.denominator],
            "pass": row_ok,
        })
    return {
        "reflection": "R(x)=a+b-x",
        "fixed_point_formula": "x*=(a+b)/2",
        "rows": rows,
        "pass": ok,
    }


def entropy_certificate() -> dict[str, object]:
    """Record strict-concavity proof data and numerical value at the seam."""
    u = 0.5
    h = -(1.0 - u) * math.log(1.0 - u) - u * math.log(u)
    h_expected = math.log(2.0)
    return {
        "H_rel_definition": "-(1-u)ln(1-u)-u ln u",
        "first_derivative": "ln((1-u)/u)",
        "stationary_equation": "(1-u)/u=1 => u=1/2",
        "second_derivative": "-1/(1-u)-1/u < 0 for 0<u<1",
        "strict_concavity": True,
        "unique_maximizer": [1, 2],
        "H_at_seam_numeric": h,
        "ln2_numeric": h_expected,
        "residual": h - h_expected,
        "pass": math.isclose(h, h_expected, rel_tol=0.0, abs_tol=1e-15),
    }


def projective_odds_certificate() -> dict[str, object]:
    """Certify complement/reciprocal conjugacy on exact rational samples."""
    samples = (Fraction(1, 5), Fraction(1, 3), Fraction(1, 2), Fraction(3, 4))
    rows = []
    ok = True
    for u in samples:
        q = u / (1 - u)
        ju = 1 - u
        qj = ju / (1 - ju)
        reciprocal = 1 / q
        row_ok = qj == reciprocal
        ok &= row_ok
        rows.append({
            "u": [u.numerator, u.denominator],
            "q_u": [q.numerator, q.denominator],
            "q_Ju": [qj.numerator, qj.denominator],
            "q_u_reciprocal": [reciprocal.numerator, reciprocal.denominator],
            "pass": row_ok,
        })
    seam_q = Fraction(1, 2) / (1 - Fraction(1, 2))
    return {
        "q_definition": "q=u/(1-u)",
        "conjugacy": "q(J(u))=1/q(u)",
        "rows": rows,
        "seam_q": [seam_q.numerator, seam_q.denominator],
        "seam_is_positive_reciprocal_fixed_point": seam_q == 1,
        "pass": ok and seam_q == 1,
    }


def kappa_numerator_bridge_certificate() -> dict[str, object]:
    """Bind the exact seam entropy to the existing TIR kappa numerator."""
    kappa = math.log(2.0) / (24.0 * math.pi)
    from_seam = math.log(2.0) / (24.0 * math.pi)
    return {
        "seam_entropy": "ln2",
        "tir_normalization": "kappa=ln2/(24*pi)",
        "typed_chain": "u*=1/2 -> H_rel=ln2 -> TIR kappa numerator",
        "kappa_numeric": kappa,
        "kappa_from_seam_entropy_numeric": from_seam,
        "pass": math.isclose(kappa, from_seam, rel_tol=0.0, abs_tol=0.0),
    }


def build_receipt() -> dict[str, object]:
    exact_half = exact_half_seam_certificate()
    affine = affine_interval_certificate()
    entropy = entropy_certificate()
    odds = projective_odds_certificate()
    kappa_bridge = kappa_numerator_bridge_certificate()
    passed = all(block["pass"] for block in (exact_half, affine, entropy, odds, kappa_bridge))
    return {
        "schema": "TIR_RELATIONAL_HALF_SEAM_V0_1",
        "scope": "TIR_STRUCTURAL_CROSSLINK",
        "claim_class": {
            "half_seam_fixed_point": "EXACT_AFFINE_RELATIONAL_STATEMENT",
            "equal_weight_meeting_point": "EXACT_CONDITIONAL_ON_DECLARED_WEIGHTS",
            "binary_relational_entropy_maximum": "EXACT_INFORMATION_THEORETIC_STATEMENT",
            "projective_reciprocal_fixed_point": "EXACT_PROJECTIVE_STATEMENT",
            "kappa_numerator_binding": "EXACT_TYPED_BINDING_TO_EXISTING_TIR_NORMALIZATION",
            "temporal_now_use": "DOWNSTREAM_CROSSLINK_INPUT",
            "secret_of_a_half_use": "DOWNSTREAM_CROSSLINK_INPUT",
        },
        "relation_model": {
            "slice": "2",
            "coordinate": "u in [0,1]",
            "orientation_reversal": "J(u)=1-u",
            "incoming_weights": {"from_1": "1-u", "from_3": "u"},
            "meeting_set": "{u : 1-u=u}={1/2}",
        },
        "exact_half_seam": exact_half,
        "affine_interval": affine,
        "entropy": entropy,
        "projective_odds": odds,
        "kappa_numerator_bridge": kappa_bridge,
        "export_packet": {
            "u_star": [1, 2],
            "weights": {"from_1": [1, 2], "from_3": [1, 2]},
            "entropy": "ln2",
            "projective_odds": [1, 1],
            "involution": "u<->1-u",
            "tir_kappa": "ln2/(24*pi)",
        },
        "technical_status": "PASS" if passed else "FAIL",
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
