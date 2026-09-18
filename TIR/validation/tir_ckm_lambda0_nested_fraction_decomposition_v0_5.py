#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction

import tir_ckm_600cell_a2_selector_bridge_candidate_v0_2 as geo
import tir_half_seam_phase_fiber_v0_1 as half_seam
import tir_kappa_flavour_mixing_normalization_v0_1 as flavour_norm
import tir_600cell_mckay_e8_closure_candidate_v0_3 as mckay


def frac(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def main() -> int:
    # Route A: reconstruct the local 600-cell incidence packet from coordinates.
    vertices = geo.vertices600()
    adjacency = geo.adjacency600(vertices)
    cells = geo.tetrahedral_cells(adjacency)
    edge_to_cells, face_to_cells, _edge_to_faces = geo.incidence(cells)

    face_incidences = {len(star) for star in face_to_cells.values()}
    edge_incidences = {len(star) for star in edge_to_cells.values()}
    assert face_incidences == {2}
    assert edge_incidences == {5}

    nu_f = next(iter(face_incidences))
    nu_e = next(iter(edge_incidences))
    packet_dimension = 2 * nu_f + nu_e
    lambda_incidence = Fraction(nu_f, packet_dimension)

    # Route B: independent SU(3)_F + McKay representation bookkeeping.
    flavour_receipt = flavour_norm.build_receipt()
    assert flavour_receipt["technical_status"] == "PASS"
    su3_dimension = int(flavour_receipt["mixing_algebra_dimension"])
    identity_dimension = 1
    matrix_channel_dimension = su3_dimension + identity_dimension

    mckay_receipt = mckay.validate()
    assert mckay_receipt["status"] == "PASS"
    fundamental_irrep = str(mckay_receipt["fundamental_irrep"])
    doublet_dimension = int(mckay_receipt["irrep_dimensions"][fundamental_irrep])

    lambda_representation = Fraction(doublet_dimension, matrix_channel_dimension)
    inverse_lambda_effective = Fraction(matrix_channel_dimension, doublet_dimension)

    # Preserve the unsimplified/nested structure instead of immediately reducing 2/9.
    denominator_full_units = su3_dimension // doublet_dimension
    denominator_residual = Fraction(identity_dimension, doublet_dimension)
    nested_denominator = Fraction(denominator_full_units, 1) + denominator_residual
    lambda_nested = Fraction(1, 1) / nested_denominator

    # Route C: independent half-seam provenance. This is a crosscheck, not an
    # identification of the McKay doublet with the half-seam mechanism.
    half_receipt = half_seam.build_receipt()
    assert half_receipt["technical_status"] == "PASS"
    half = Fraction(1, 2)
    half_weighted_packet = Fraction(packet_dimension, 1) * half
    lambda_half_packet = Fraction(1, 1) / half_weighted_packet

    checks = {
        "600cell_has_600_tetrahedral_cells": len(cells) == 600,
        "600cell_face_incidence_is_2": nu_f == 2,
        "600cell_edge_incidence_is_5": nu_e == 5,
        "source_edge_target_packet_is_9": packet_dimension == 9,
        "incidence_lambda0_is_2_over_9": lambda_incidence == Fraction(2, 9),
        "su3_dimension_is_8": su3_dimension == 8,
        "identity_channel_is_1": identity_dimension == 1,
        "su3_plus_identity_is_9": matrix_channel_dimension == 9,
        "mckay_fundamental_dimension_is_2": doublet_dimension == 2,
        "representation_lambda0_is_2_over_9": lambda_representation == Fraction(2, 9),
        "effective_inverse_lambda0_is_9_over_2": inverse_lambda_effective == Fraction(9, 2),
        "nested_denominator_is_4_plus_half": denominator_full_units == 4 and denominator_residual == Fraction(1, 2),
        "nested_denominator_equals_9_over_2": nested_denominator == Fraction(9, 2),
        "nested_lambda0_is_1_over_4_plus_half": lambda_nested == Fraction(2, 9),
        "half_seam_audit_passes": half_receipt["technical_status"] == "PASS",
        "half_is_reciprocal_of_doublet_dimension": half == Fraction(1, doublet_dimension),
        "half_weighted_packet_is_9_over_2": half_weighted_packet == Fraction(9, 2),
        "half_packet_lambda0_is_2_over_9": lambda_half_packet == Fraction(2, 9),
        "all_three_routes_agree_exactly": lambda_incidence == lambda_representation == lambda_nested == lambda_half_packet,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": "TIR_CKM_LAMBDA0_NESTED_FRACTION_DECOMPOSITION_V0_5",
        "status": status,
        "epistemic_status": "EXACT_RATIONAL_IDENTITY__INDEPENDENT_PROVENANCE_CROSSCHECK__DYNAMICAL_BINDING_OPEN",
        "physical_promotion": False,
        "uses_observed_ckm": False,
        "uses_observed_masses": False,
        "lambda0": {
            "reduced": frac(lambda_nested),
            "nested": "1/(4+1/2)",
            "inverse": frac(inverse_lambda_effective),
            "decimal": float(lambda_nested),
        },
        "route_A_600cell_incidence": {
            "nu_F": nu_f,
            "nu_E": nu_e,
            "packet": "F_src + E + F_dst",
            "packet_dimension": packet_dimension,
            "formula": "nu_F/(2*nu_F+nu_E)",
            "value": frac(lambda_incidence),
        },
        "route_B_flavour_mckay": {
            "su3_dimension": su3_dimension,
            "identity_dimension": identity_dimension,
            "matrix_channel_dimension": matrix_channel_dimension,
            "mckay_fundamental_irrep": fundamental_irrep,
            "mckay_doublet_dimension": doublet_dimension,
            "formula": "d_Q/(dim(su3)+1)",
            "value": frac(lambda_representation),
            "inverse_decomposition": f"({su3_dimension}+{identity_dimension})/{doublet_dimension} = {denominator_full_units}+{frac(denominator_residual)}",
        },
        "route_C_half_seam_crosscheck": {
            "half": frac(half),
            "packet_dimension": packet_dimension,
            "effective_denominator": frac(half_weighted_packet),
            "formula": "1/(packet_dimension*half)",
            "value": frac(lambda_half_packet),
            "provenance_note": "Exact numerical bridge only; half-seam and McKay-doublet mechanisms remain distinct provenance routes.",
        },
        "checks": checks,
        "closed": {
            "lambda0_exact_value": True,
            "nested_fraction_identity": True,
            "incidence_representation_half_seam_exact_agreement": True,
        },
        "open": {
            "physical_effective_packet_interpretation": True,
            "derive_additive_a_kappa_operator": True,
            "promote_refined_lambda_as_prospective_prediction": True,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
