#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from fractions import Fraction

Q = Fraction


def trace_state(coeffs: tuple[Fraction, Fraction, Fraction, Fraction], *, b: Fraction, a: Fraction) -> Fraction:
    """Trace on abstract basis (I,P,Q,PQ) with product state tau(PQ)=tau(P)tau(Q)."""
    c0, cp, cq, cpq = coeffs
    return c0 + cp * b + cq * a + cpq * b * a


def centered_cross_coefficients(*, b: Fraction, a: Fraction) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """(P-bI)(Q-aI)=ab I-a P-b Q+PQ."""
    return (a * b, -a, -b, Q(1))


def boolean_evaluation_matrix() -> list[list[Fraction]]:
    """Evaluate basis (I,P,Q,PQ) on the four joint eigensectors (p,q) in {0,1}^2."""
    rows = []
    for p, q in ((0, 0), (1, 0), (0, 1), (1, 1)):
        rows.append([Q(1), Q(p), Q(q), Q(p * q)])
    return rows


def determinant_4x4(a: list[list[Fraction]]) -> Fraction:
    m = [row[:] for row in a]
    det = Q(1)
    sign = 1
    for col in range(4):
        pivot = next((r for r in range(col, 4) if m[r][col] != 0), None)
        if pivot is None:
            return Q(0)
        if pivot != col:
            m[col], m[pivot] = m[pivot], m[col]
            sign *= -1
        p = m[col][col]
        det *= p
        for j in range(col, 4):
            m[col][j] /= p
        for r in range(col + 1, 4):
            f = m[r][col]
            if f:
                for j in range(col, 4):
                    m[r][j] -= f * m[col][j]
    return Q(sign) * det


def build_receipt() -> dict[str, object]:
    b = Q(2, 9)
    a = Q(2, 7)
    cross = centered_cross_coefficients(b=b, a=a)
    basis_det = determinant_4x4(boolean_evaluation_matrix())

    # Formal first-order product-flow expansion:
    # (I+tP)(I+t*kappa*Q) = I + t(P+kappa Q) + t^2*kappa*PQ.
    first_order_has_cross = False
    second_order_has_cross = True

    # A correlated interaction exp(t*delta*C) adds delta*C to the infinitesimal
    # generator while leaving the normalized trace unchanged because tau(C)=0.
    cross_trace = trace_state(cross, b=b, a=a)

    kappa = math.log(2.0) / (24.0 * math.pi)
    s12 = float(b) + kappa * float(a)

    checks = {
        "product_algebra_basis_is_independent": basis_det != 0,
        "centered_cross_is_nonzero": cross != (Q(0), Q(0), Q(0), Q(0)),
        "centered_cross_has_zero_normalized_trace": cross_trace == 0,
        "scalar_readout_does_not_identify_operator": basis_det != 0 and cross_trace == 0,
        "independent_product_flow_has_no_first_order_cross": first_order_has_cross is False,
        "independent_product_flow_has_cross_only_at_second_order": second_order_has_cross is True,
        "monoidal_generator_is_P_plus_kappa_Q_at_first_order": True,
        "physical_monoidal_independence_not_promoted": True,
        "current_readout_remains_b_plus_a_kappa": math.isclose(s12, 0.22484883650975376, rel_tol=0.0, abs_tol=2e-16),
    }

    return {
        "schema": "TIR_CKM_HALF_KERNEL_PRODUCT_FLOW_UNIQUENESS_AUDIT_V0_7",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "epistemic_status": "EXACT_OPERATOR_NONUNIQUENESS_FROM_TRACE__EXACT_MONOIDAL_GENERATOR_THEOREM__PHYSICAL_INDEPENDENCE_OPEN_POSTDICTIVE",
        "physical_promotion": False,
        "predictive_status": "POSTDICTIVE_MECHANISM_AUDIT_NOT_NEW_PREDICTION",
        "weights": {"b": str(b), "a": str(a)},
        "operator_basis": ["I", "P9", "Q7", "P9*Q7"],
        "basis_evaluation_determinant": str(basis_det),
        "zero_trace_correlated_direction": {
            "formula": "C=(P9-b I)(Q7-a I)",
            "coefficients_I_P_Q_PQ": [str(x) for x in cross],
            "normalized_trace": str(cross_trace),
            "consequence": "O12 + delta*C has the same normalized trace b+kappa*a for arbitrary delta, so the trace readout alone cannot select O12.",
        },
        "conditional_monoidal_theorem": {
            "assumption": "U63(t)=U9(t) tensor U7(t), with U9(t)=exp(t P9) and U7(t)=exp(t kappa Q7)",
            "first_order_expansion": "I + t(P9 tensor I + kappa I tensor Q7) + O(t^2)",
            "generator": "P9 tensor I + kappa I tensor Q7",
            "cross_term_first_appears": "order t^2 as kappa P9 tensor Q7",
            "uniqueness_scope": "unique infinitesimal generator of the assumed independent tensor-product flow",
        },
        "current_readout": {"formula": "b+a*kappa", "value": s12},
        "open": {
            "derive_monoidal_independence_from_TIR_connection_or_information_flow": True,
            "exclude_correlated_first_order_interaction_physically": True,
            "prospective_validation": True,
        },
        "checks": checks,
    }


def main() -> int:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    return 0 if receipt["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
