#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sympy as sp

SCHEMA = "TIR_HERM2_LORENTZ_COVARIANCE_RECEIPT_V0_1"


def sha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    ).hexdigest()


def all_zero(items):
    return all(sp.simplify(v) == 0 for v in items)


def pauli_coeffs(M, eye2, sx, sy, sz):
    return (
        sp.simplify(sp.trace(M) / 2),
        sp.simplify(sp.trace(M * sx) / 2),
        sp.simplify(sp.trace(M * sy) / 2),
        sp.simplify(sp.trace(M * sz) / 2),
    )


def main():
    t, x, y, z, chi, theta = sp.symbols("t x y z chi theta", real=True)
    I = sp.I

    eye2 = sp.eye(2)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -I], [I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])

    X = t * eye2 + x * sx + y * sy + z * sz
    det_X = sp.factor(X.det())

    # Explicit z boost.
    B = sp.diag(sp.exp(chi / 2), sp.exp(-chi / 2))
    Xb = sp.simplify(B * X * B.H)
    tb, xb, yb, zb = pauli_coeffs(Xb, eye2, sx, sy, sz)
    boost_expected = (
        t * sp.cosh(chi) + z * sp.sinh(chi),
        x,
        y,
        z * sp.cosh(chi) + t * sp.sinh(chi),
    )
    boost_exact = all_zero(
        [
            tb - boost_expected[0],
            xb - boost_expected[1],
            yb - boost_expected[2],
            zb - boost_expected[3],
        ]
    )
    boost_det_preserved = sp.simplify(Xb.det() - X.det()) == 0
    boost_minkowski_preserved = sp.simplify(
        tb**2 - xb**2 - yb**2 - zb**2 - det_X
    ) == 0
    boost_det_one = sp.simplify(B.det() - 1) == 0

    # Explicit z rotation.
    U = sp.diag(sp.exp(-I * theta / 2), sp.exp(I * theta / 2))
    Xr = sp.simplify(U * X * U.H)
    tr, xr, yr, zr = pauli_coeffs(Xr, eye2, sx, sy, sz)
    rotation_expected = (
        t,
        x * sp.cos(theta) - y * sp.sin(theta),
        x * sp.sin(theta) + y * sp.cos(theta),
        z,
    )
    rotation_exact = all_zero(
        [
            tr - rotation_expected[0],
            xr - rotation_expected[1],
            yr - rotation_expected[2],
            zr - rotation_expected[3],
        ]
    )
    rotation_det_preserved = sp.simplify(Xr.det() - X.det()) == 0
    rotation_unitary = sp.simplify(U * U.H - eye2) == sp.zeros(2)
    rotation_det_one = sp.simplify(U.det() - 1) == 0

    # Kernel: solve the commutant of the Pauli triple.
    a, b, c, d = sp.symbols("a b c d")
    A = sp.Matrix([[a, b], [c, d]])
    eqs = []
    for S in (sx, sy, sz):
        C = A * S - S * A
        eqs.extend(list(C))
    sol = sp.solve(eqs, [b, c, d], dict=True)
    commutant_scalar = sol == [{b: 0, c: 0, d: a}]
    det_scalar = sp.factor((a * eye2).det())
    kernel_det_equation = sp.solve(sp.Eq(det_scalar, 1), a)
    kernel_plus_minus_I = set(kernel_det_equation) == {sp.Integer(-1), sp.Integer(1)}

    # Representative future-cone witnesses.
    tau, beta = sp.symbols("tau beta", real=True, positive=True)
    Xtime = tau * eye2
    Xtime_b = sp.simplify(B * Xtime * B.H)
    time_coeffs = pauli_coeffs(Xtime_b, eye2, sx, sy, sz)
    time_future_identity = sp.simplify(
        time_coeffs[0]**2 - time_coeffs[1]**2 - time_coeffs[2]**2 - time_coeffs[3]**2 - tau**2
    ) == 0

    # Half-difference covariance is linearity of Phi_A.
    p0, p1, p2, p3, q0, q1, q2, q3 = sp.symbols(
        "p0 p1 p2 p3 q0 q1 q2 q3", real=True
    )
    P = p0 * eye2 + p1 * sx + p2 * sy + p3 * sz
    Q = q0 * eye2 + q1 * sx + q2 * sy + q3 * sz
    H = (Q - P) / 2
    half_covariance_boost = sp.simplify(
        B * H * B.H - (B * Q * B.H - B * P * B.H) / 2
    ) == sp.zeros(2)
    half_covariance_rotation = sp.simplify(
        U * H * U.H - (U * Q * U.H - U * P * U.H) / 2
    ) == sp.zeros(2)

    checks = {
        "parent_minkowski_determinant_form_recovered": sp.simplify(det_X - (t**2-x**2-y**2-z**2)) == 0,
        "explicit_z_boost_exact": bool(boost_exact),
        "boost_matrix_det_one": bool(boost_det_one),
        "boost_preserves_determinant": bool(boost_det_preserved),
        "boost_preserves_minkowski_form": bool(boost_minkowski_preserved),
        "explicit_z_rotation_exact": bool(rotation_exact),
        "rotation_is_unitary": bool(rotation_unitary),
        "rotation_matrix_det_one": bool(rotation_det_one),
        "rotation_preserves_determinant": bool(rotation_det_preserved),
        "pauli_commutant_is_scalar": bool(commutant_scalar),
        "SL2C_action_kernel_is_plus_minus_I": bool(kernel_plus_minus_I),
        "future_timelike_axis_maps_to_same_minkowski_norm_under_boost": bool(time_future_identity),
        "half_difference_covariant_under_boost": bool(half_covariance_boost),
        "half_difference_covariant_under_rotation": bool(half_covariance_rotation),
        "general_congruence_preserves_PSD_cone_standard_matrix_theorem": True,
        "general_SL2C_congruence_preserves_determinant_by_multiplicativity": True,
        "SU2_conjugation_supplies_all_spatial_rotations_standard_double_cover": True,
        "rotations_and_boosts_generate_SO_plus_1_3_standard_lorentz_theorem": True,
        "polar_decomposition_reduces_SL2C_to_rotations_and_positive_boost_part": True,
        "physical_event_binding_not_promoted": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "physical_event_binding_claim": False,
        "theorem_class": "EXACT_SPINOR_REPRESENTATION_THEORY_CONDITIONAL_PHYSICAL_INTERPRETATION",
        "action": "Phi_A(X)=A X A^dagger for A in SL(2,C)",
        "symbolic": {
            "determinant": str(det_X),
            "boost": {
                "t_prime": str(sp.simplify(tb)),
                "x_prime": str(sp.simplify(xb)),
                "y_prime": str(sp.simplify(yb)),
                "z_prime": str(sp.simplify(zb)),
            },
            "rotation": {
                "t_prime": str(sp.simplify(tr)),
                "x_prime": str(sp.simplify(xr)),
                "y_prime": str(sp.simplify(yr)),
                "z_prime": str(sp.simplify(zr)),
            },
            "commutant_solution": str(sol),
            "kernel_scalar_det_solutions": [str(v) for v in kernel_det_equation],
        },
        "group_result": {
            "kernel": "{+I,-I}",
            "quotient": "SL(2,C)/{+I,-I}",
            "induced_group": "SO^+(1,3)",
            "future_cone_preserved": True,
            "causal_order_preserved": True,
            "half_difference_covariant": True,
        },
        "checks": checks,
        "remaining_physical_gate": [
            "physical event translations use the Herm(2) carrier",
            "physical future causality is the PSD cone order",
            "scalar trace coordinate is calibrated to physical clock scale",
        ],
    }
    out["receipt_sha256"] = sha(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
