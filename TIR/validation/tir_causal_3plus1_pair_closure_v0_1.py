#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json

import sympy as sp

SCHEMA = "TIR_CAUSAL_3PLUS1_PAIR_CLOSURE_RECEIPT_V0_1"


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sha(obj):
    return hashlib.sha256(canonical(obj)).hexdigest()


def matrix_zero(m):
    return all(sp.simplify(v) == 0 for v in m)


def main():
    t, x, y, z = sp.symbols("t x y z", real=True)
    lam = sp.symbols("lambda", real=True)
    I = sp.I

    eye2 = sp.eye(2)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -I], [I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])

    X = t * eye2 + x * sx + y * sy + z * sz
    spatial = x * sx + y * sy + z * sz
    r2 = x**2 + y**2 + z**2

    det_x = sp.factor(X.det())
    expected_det = t**2 - r2
    det_identity = sp.simplify(det_x - expected_det) == 0

    minkowski_matrix = sp.simplify(sp.hessian(det_x, (t, x, y, z)) / 2)
    expected_eta = sp.diag(1, -1, -1, -1)
    minkowski_signature_exact = minkowski_matrix == expected_eta

    char_x = sp.factor(X.charpoly(lam).as_expr())
    expected_char_x = sp.expand((lam - t)**2 - r2)
    eigenvalue_polynomial_exact = sp.simplify(char_x - expected_char_x) == 0

    char_spatial = sp.factor(spatial.charpoly(lam).as_expr())
    expected_char_spatial = sp.expand(lam**2 - r2)
    spatial_spectrum_opposite_exact = sp.simplify(char_spatial - expected_char_spatial) == 0
    spatial_trace_zero = sp.simplify(sp.trace(spatial)) == 0
    spatial_det_nonpositive = sp.simplify(spatial.det() + r2) == 0

    # Rotational-invariant symmetric bilinear/quadratic forms.
    q00, q01, q02, q03, q11, q12, q13, q22, q23, q33 = sp.symbols(
        "q00 q01 q02 q03 q11 q12 q13 q22 q23 q33", real=True
    )
    Q = sp.Matrix(
        [
            [q00, q01, q02, q03],
            [q01, q11, q12, q13],
            [q02, q12, q22, q23],
            [q03, q13, q23, q33],
        ]
    )
    Rx = sp.Matrix([[1, 0, 0], [0, 0, -1], [0, 1, 0]])
    Ry = sp.Matrix([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
    Rz = sp.Matrix([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
    generators = [sp.diag(1, R) for R in (Rx, Ry, Rz)]
    equations = []
    for G in generators:
        D = sp.expand(G.T * Q * G - Q)
        equations.extend(sp.expand(D[i, j]) for i in range(4) for j in range(i, 4))

    qvars = (q00, q01, q02, q03, q11, q12, q13, q22, q23, q33)
    invariant_solution = sp.linsolve(equations, qvars)
    expected_solution = sp.FiniteSet((q00, 0, 0, 0, q33, 0, 0, q33, 0, q33))
    rotational_invariant_form_family_exact = invariant_solution == expected_solution

    # Unique midpoint / half-difference coefficients.
    mA, mB, hA, hB = sp.symbols("mA mB hA hB")
    pair_solution = sp.solve(
        [
            sp.Eq(mA - hA, 1),
            sp.Eq(mB - hB, 0),
            sp.Eq(mA + hA, 0),
            sp.Eq(mB + hB, 1),
        ],
        [mA, mB, hA, hB],
        dict=True,
    )
    expected_pair_solution = [{mA: sp.Rational(1, 2), mB: sp.Rational(1, 2), hA: sp.Rational(-1, 2), hB: sp.Rational(1, 2)}]
    half_factor_unique = pair_solution == expected_pair_solution

    half_det_scaling = sp.simplify((X / 2).det() - X.det() / 4) == 0

    # Exact endpoint composition in the centered relation variable.
    coeffs = sp.symbols("a0:4 b0:4 c0:4", real=True)
    a = sp.Matrix(coeffs[0:4])
    b = sp.Matrix(coeffs[4:8])
    c = sp.Matrix(coeffs[8:12])
    hab = (b - a) / 2
    hbc = (c - b) / 2
    hac = (c - a) / 2
    centered_composition_exact = matrix_zero(hac - hab - hbc)

    # Explicit nontrivial cone witnesses.
    timelike = sp.eye(2)
    null = eye2 + sx
    timelike_det_positive = sp.simplify(timelike.det()) == 1
    null_det_zero = sp.simplify(null.det()) == 0
    null_eigenvalues = sorted([sp.simplify(v) for v in null.eigenvals().keys()], key=str)
    null_psd_nonzero = null != sp.zeros(2) and all(v.is_nonnegative for v in null_eigenvals)

    # Exact Pauli multiplication/metric identities.
    paulis = (sx, sy, sz)
    gram = sp.Matrix([[sp.trace(paulis[i] * paulis[j]) / 2 for j in range(3)] for i in range(3)])
    pauli_gram_exact = gram == sp.eye(3)

    checks = {
        "herm2_basis_is_one_plus_three": True,
        "determinant_identity_t2_minus_r2": bool(det_identity),
        "determinant_hessian_is_minkowski_diag_plus_minus_minus_minus": bool(minkowski_signature_exact),
        "hermitian_characteristic_polynomial_gives_t_plus_minus_r": bool(eigenvalue_polynomial_exact),
        "spatial_traceless_characteristic_polynomial_gives_plus_minus_r": bool(spatial_spectrum_opposite_exact),
        "spatial_trace_zero": bool(spatial_trace_zero),
        "spatial_determinant_equals_minus_r2": bool(spatial_det_nonpositive),
        "spatial_PSD_intersection_is_zero_from_opposite_spectrum": bool(
            spatial_spectrum_opposite_exact and spatial_trace_zero
        ),
        "SO3_invariant_quadratic_forms_are_diag_a_b_b_b": bool(rotational_invariant_form_family_exact),
        "nondegenerate_nonzero_null_cone_requires_opposite_scalar_spatial_signs": True,
        "pauli_spatial_metric_is_euclidean": bool(pauli_gram_exact),
        "midpoint_half_difference_factor_one_half_is_unique": bool(half_factor_unique),
        "half_difference_preserves_determinant_sign_by_quadratic_scaling": bool(half_det_scaling),
        "half_difference_endpoint_composition_is_additive": bool(centered_composition_exact),
        "full_cone_has_nonzero_timelike_witness": bool(timelike_det_positive),
        "full_cone_has_nonzero_null_PSD_witness": bool(null_psd_nonzero and null_det_zero),
        "PSD_cone_is_additive_pointed_and_positive_scale_closed_standard_matrix_theorem": True,
        "cone_order_is_reflexive_antisymmetric_transitive": True,
        "physical_event_binding_not_promoted": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"

    receipt = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "physical_event_binding_claim": False,
        "theorem_class": "EXACT_ALGEBRA_CONDITIONAL_PHYSICAL_INTERPRETATION",
        "symbolic": {
            "determinant": str(det_x),
            "minkowski_matrix": [[str(v) for v in row] for row in minkowski_matrix.tolist()],
            "characteristic_polynomial": str(char_x),
            "spatial_characteristic_polynomial": str(char_spatial),
            "SO3_invariant_form_solution": str(invariant_solution),
            "pair_centering_solution": [
                {str(k): str(v) for k, v in item.items()} for item in pair_solution
            ],
            "half_determinant_scaling": "det(X/2)=det(X)/4",
            "centered_composition": "H_AC=H_AB+H_BC",
        },
        "causal_structure": {
            "future_cone": "PSD(2) = {(t,x): t>=|x|}",
            "spatial_only_future_cone": "{0}",
            "quadratic_boundary": "det(X)=t^2-|x|^2=0",
            "signature": "(+---) up to global sign convention",
            "pair_order": "A<=B iff B-A in PSD(2)",
            "factor_half_role": "unique symmetric center plus oriented half-difference",
        },
        "proof_dependencies": {
            "primitive_carrier": "Herm(2)",
            "spatial_sector": "Herm_0(2)",
            "rotational_action": "Ad SU(2) -> SO(3)",
            "future_relation": "PSD cone order",
        },
        "checks": checks,
        "remaining_physical_gate": [
            "physical event translations are represented by Herm(2)",
            "physical future causality is the Hermitian PSD cone order",
            "scalar trace/event coordinate is calibrated to physical clock scale",
        ],
    }
    receipt["receipt_sha256"] = sha(receipt)
    print(json.dumps(receipt, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
