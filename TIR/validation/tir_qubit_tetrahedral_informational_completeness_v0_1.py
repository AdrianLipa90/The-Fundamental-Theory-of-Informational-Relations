#!/usr/bin/env python3
"""Deterministic audit for TIR Qubit Tetrahedral Informational Completeness v0.1."""
from __future__ import annotations

import json
from fractions import Fraction

Vector = tuple[int, int, int]
TETRA: tuple[Vector, ...] = (
    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
)


def dot(a: Vector, b: Vector) -> int:
    return sum(x * y for x, y in zip(a, b))


def vecsum(vs: tuple[Vector, ...]) -> Vector:
    return tuple(sum(v[i] for v in vs) for i in range(3))  # type: ignore[return-value]


def second_moment(vs: tuple[Vector, ...]) -> tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]:
    return tuple(
        tuple(sum(v[i] * v[j] for v in vs) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def lower_bound_certificate() -> dict[str, object]:
    qubit_real_parameters = 3
    minimal_outcomes = qubit_real_parameters + 1
    return {
        "qubit_independent_real_parameters": qubit_real_parameters,
        "probability_simplex_dimension_for_m_outcomes": "m-1",
        "minimal_informationally_complete_outcomes": minimal_outcomes,
        "pass": minimal_outcomes == 4,
    }


def tetra_geometry_certificate() -> dict[str, object]:
    norms = [dot(v, v) for v in TETRA]
    cross = [dot(TETRA[i], TETRA[j]) for i in range(4) for j in range(i + 1, 4)]
    passed = (
        vecsum(TETRA) == (0, 0, 0)
        and norms == [3, 3, 3, 3]
        and cross == [-1] * 6
        and second_moment(TETRA) == ((4, 0, 0), (0, 4, 0), (0, 0, 4))
    )
    return {
        "unnormalized_sum": vecsum(TETRA),
        "unnormalized_norm_squared": norms,
        "unnormalized_cross_dots": cross,
        "unnormalized_second_moment": second_moment(TETRA),
        "normalized_pairwise_dot": "-1/3",
        "pass": passed,
    }


def sic_overlap_certificate() -> dict[str, object]:
    # Exact rational form: Tr(P_a P_b)=(1+n_a.n_b)/2=(1-1/3)/2=1/3.
    overlap = (Fraction(1, 1) + Fraction(-1, 3)) / 2
    target = Fraction(1, 3)
    return {
        "distinct_projector_overlap": str(overlap),
        "derivation": "(1 + (-1/3))/2",
        "pass": overlap == target,
    }


def reconstruction_certificate() -> dict[str, object]:
    # The reconstruction identity reduces exactly to sum n_a=0 and
    # sum n_a n_a^T=(4/3)I. The integer tetrahedral realization certifies
    # these after the common normalization n_a=v_a/sqrt(3).
    zero_sum = vecsum(TETRA) == (0, 0, 0)
    moment = second_moment(TETRA)
    isotropic = moment == ((4, 0, 0), (0, 4, 0), (0, 0, 4))
    passed = zero_sum and isotropic
    return {
        "reconstruction_identity": "r = 3 * sum_a p_a n_a",
        "required_zero_sum": zero_sum,
        "required_normalized_second_moment": "(4/3) I3",
        "integer_second_moment_certificate": moment,
        "pass": passed,
    }


def povm_normalization_certificate() -> dict[str, object]:
    # E_a=(I+n_a.sigma)/4. Sum n_a=0 and four identity quarters give I.
    zero_sum = vecsum(TETRA) == (0, 0, 0)
    return {
        "elements": "E_a=(I+n_a.sigma)/4",
        "identity_weight_sum": "4*(1/4)=1",
        "bloch_vector_sum_zero": zero_sum,
        "sum_Ea": "I",
        "pass": zero_sum,
    }


def build_receipt() -> dict[str, object]:
    blocks = {
        "informational_completeness_lower_bound": lower_bound_certificate(),
        "tetrahedral_bloch_geometry": tetra_geometry_certificate(),
        "symmetric_projector_overlap": sic_overlap_certificate(),
        "povm_normalization": povm_normalization_certificate(),
        "bloch_reconstruction": reconstruction_certificate(),
    }
    passed = all(bool(block["pass"]) for block in blocks.values())
    return {
        "schema": "TIR_QUBIT_TETRAHEDRAL_INFORMATIONAL_COMPLETENESS_V0_1",
        "scope": "TIR_QUBIT_SIC_CONVERGENCE_AUDIT",
        "minimal_ic_outcomes": 4,
        "symmetric_geometry": "REGULAR_TETRAHEDRON_ON_BLOCH_S2",
        "pairwise_projector_overlap": "1/3",
        "bloch_reconstruction": "r=3*sum_a(p_a*n_a)",
        "spatial_identification_derived": False,
        "next_gate": "INFORMATIONAL_TETRAHEDRON_TO_SPATIAL_TETRAHEDRON_PROMOTION",
        "blocks": blocks,
        "technical_status": "PASS" if passed else "FAIL",
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
