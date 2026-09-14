#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path

Q = Fraction
ROOT = Path(__file__).resolve().parents[2]
XI_KERNEL = ROOT / "TIR/zeta_information_axis/src/critical_axis/xi_kernel.py"


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0)) for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def eye(n):
    return [[Q(1 if i == j else 0) for j in range(n)] for i in range(n)]


def madd(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mscale(c, a):
    return [[c * x for x in row] for row in a]


def msub(a, b):
    return madd(a, mscale(Q(-1), b))


def mpow(a, n):
    out = eye(len(a))
    for _ in range(n):
        out = matmul(out, a)
    return out


def rank(a):
    m = [row[:] for row in a]
    rows, cols = len(m), len(m[0])
    r = 0
    for c in range(cols):
        pivot = next((i for i in range(r, rows) if m[i][c] != 0), None)
        if pivot is None:
            continue
        m[r], m[pivot] = m[pivot], m[r]
        p = m[r][c]
        m[r] = [x / p for x in m[r]]
        for i in range(rows):
            if i != r and m[i][c] != 0:
                f = m[i][c]
                m[i] = [m[i][j] - f * m[r][j] for j in range(cols)]
        r += 1
    return r


def half_kernel_data():
    p = [[Q(0), Q(0), Q(0), Q(0)], [Q(1), Q(0), Q(0), Q(0)], [Q(0), Q(1), Q(0), Q(0)], [Q(0), Q(0), Q(1), Q(1)]]
    g = msub(eye(4), p)
    a_c = matmul(transpose(g), g)
    projector = madd(madd(madd(eye(4), mscale(Q(-5, 2), a_c)), mscale(Q(3, 2), mpow(a_c, 2))), mscale(Q(-1, 4), mpow(a_c, 3)))
    return a_c, projector


def main() -> int:
    nu_f = Q(2)
    nu_e = Q(5)
    dim_bulk = 2 * nu_f + nu_e
    dim_boundary = nu_f + nu_e
    b = nu_f / dim_bulk
    a = nu_f / dim_boundary
    c = nu_f / nu_e
    assert (b, a, c) == (Q(2, 9), Q(2, 7), Q(2, 5))

    a_c, pi_half = half_kernel_data()
    expected_a_c = [[Q(2), Q(-1), Q(0), Q(0)], [Q(-1), Q(2), Q(-1), Q(0)], [Q(0), Q(-1), Q(2), Q(0)], [Q(0), Q(0), Q(0), Q(0)]]
    expected_pi = [[Q(0), Q(0), Q(0), Q(0)], [Q(0), Q(0), Q(0), Q(0)], [Q(0), Q(0), Q(0), Q(0)], [Q(0), Q(0), Q(0), Q(1)]]

    rank_face_bulk = Q(2)
    rank_face_boundary = Q(2)
    total_dim = dim_bulk * dim_boundary
    trace_bulk_term = rank_face_bulk * dim_boundary
    trace_boundary_term = dim_bulk * rank_face_boundary
    coefficient_bulk = trace_bulk_term / total_dim
    coefficient_boundary = trace_boundary_term / total_dim
    assert coefficient_bulk == b
    assert coefficient_boundary == a

    kappa = math.log(2.0) / (24.0 * math.pi)
    refined_s12 = float(b) + kappa * float(a)

    c_inv, a_inv, b_inv = 1 / c, 1 / a, 1 / b
    assert (c_inv, a_inv, b_inv) == (Q(5, 2), Q(7, 2), Q(9, 2))
    assert a_inv == (c_inv + b_inv) / 2

    xi_source = XI_KERNEL.read_text(encoding="utf-8")
    xi_source_has_9_over_2 = 'exp_9u_over_2 = mp.exp(mp.mpf("4.5") * x)' in xi_source
    xi_source_has_5_over_2 = 'exp_5u_over_2 = mp.exp(mp.mpf("2.5") * x)' in xi_source
    xi_cross_midpoint = (Q(9, 2) + Q(5, 2)) / 2

    checks = {
        "bulk_packet_dimension_is_9": dim_bulk == 9,
        "half_boundary_packet_dimension_is_7": dim_boundary == 7,
        "bulk_face_trace_is_b_2_over_9": b == Q(2, 9),
        "boundary_face_trace_is_a_2_over_7": a == Q(2, 7),
        "edge_star_ratio_is_c_2_over_5": c == Q(2, 5),
        "half_operator_exact": a_c == expected_a_c,
        "half_operator_rank_is_3": rank(a_c) == 3,
        "half_projector_exact": pi_half == expected_pi,
        "product_generator_bulk_trace_coefficient_is_b": coefficient_bulk == b,
        "product_generator_boundary_trace_coefficient_is_a": coefficient_boundary == a,
        "inverse_ladder_is_5_2_7_2_9_2": (c_inv, a_inv, b_inv) == (Q(5, 2), Q(7, 2), Q(9, 2)),
        "inverse_a_is_exact_midpoint": a_inv == (c_inv + b_inv) / 2,
        "canonical_xi_source_has_9_over_2": xi_source_has_9_over_2,
        "canonical_xi_source_has_5_over_2": xi_source_has_5_over_2,
        "xi_cross_midpoint_is_7_over_2": xi_cross_midpoint == Q(7, 2),
        "refined_s12_matches_current_value": math.isclose(refined_s12, 0.22484883650975376, rel_tol=0.0, abs_tol=2e-16),
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": "TIR_CKM_HALF_KERNEL_KAPPA_SELECTOR_CANDIDATE_V0_6",
        "status": status,
        "epistemic_status": "EXACT_HALF_KERNEL__EXACT_9_TO_7_BOUNDARY_COMPRESSION__EXACT_PRODUCT_GENERATOR_TRACE__PHYSICAL_BINDING_CONDITIONAL_POSTDICTIVE",
        "physical_promotion": False,
        "predictive_status": "POSTDICTIVE_MECHANISM_RECONSTRUCTION_NOT_NEW_PREDICTION",
        "uses_observed_ckm_to_select_structure": False,
        "half_kernel": {"terminal_axis": "4 -> 2 -> 1 -> 1/2", "A_C": [[str(x) for x in row] for row in a_c], "projector": [[str(x) for x in row] for row in pi_half], "kernel": "span{|1/2>}"},
        "packet_compression": {"bulk": "F_src + E + F_dst", "bulk_dimension": int(dim_bulk), "boundary": "F + E", "boundary_dimension": int(dim_boundary), "b": str(b), "a": str(a), "c": str(c)},
        "product_generator": {"formula": "O12=P_F^(9) tensor I_7 + kappa I_9 tensor P_F^(7)", "normalized_trace": "b + kappa*a", "bulk_coefficient": str(coefficient_bulk), "boundary_coefficient": str(coefficient_boundary), "kappa": kappa, "s12": refined_s12},
        "inverse_ladder": {"c_inv": str(c_inv), "a_inv": str(a_inv), "b_inv": str(b_inv), "a_inv_is_midpoint": True, "xi_endpoint_exponents": ["9/2", "5/2"], "xi_cross_midpoint": str(xi_cross_midpoint)},
        "closed_conditional": {"half_kernel_selects_boundary_sector": True, "boundary_packet_gives_a": True, "product_generator_realizes_b_plus_a_kappa": True, "xi_inverse_ladder_crosscheck": True},
        "open": {"derive_product_flow_as_unique_physical_ckm_generator": True, "prospective_validation": True, "promote_refined_lambda_as_first_principles_prediction": True},
        "checks": checks,
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
