#!/usr/bin/env python3
"""Deterministic algebraic gate for TIR SE(3) global gluing candidate v0.1."""
from __future__ import annotations

import json
import math
from typing import Iterable, Tuple

Matrix = Tuple[Tuple[float, float, float], Tuple[float, float, float], Tuple[float, float, float]]
Vector = Tuple[float, float, float]
SE3 = Tuple[Matrix, Vector]

I3: Matrix = ((1.0, 0.0, 0.0), (0.0, 1.0, 0.0), (0.0, 0.0, 1.0))
ZERO: Vector = (0.0, 0.0, 0.0)
TOL = 1e-12


def mm(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )  # type: ignore[return-value]


def mv(a: Matrix, v: Vector) -> Vector:
    return tuple(sum(a[i][k] * v[k] for k in range(3)) for i in range(3))  # type: ignore[return-value]


def vt(a: Vector, b: Vector) -> Vector:
    return tuple(a[i] + b[i] for i in range(3))  # type: ignore[return-value]


def vneg(a: Vector) -> Vector:
    return tuple(-x for x in a)  # type: ignore[return-value]


def transpose(a: Matrix) -> Matrix:
    return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))  # type: ignore[return-value]


def compose(g2: SE3, g1: SE3) -> SE3:
    r2, t2 = g2
    r1, t1 = g1
    return mm(r2, r1), vt(mv(r2, t1), t2)


def inverse(g: SE3) -> SE3:
    r, t = g
    rinv = transpose(r)
    return rinv, vneg(mv(rinv, t))


def path_product(edges: Iterable[SE3]) -> SE3:
    out: SE3 = (I3, ZERO)
    for edge in edges:
        out = compose(edge, out)
    return out


def conjugate(h: SE3, g: SE3) -> SE3:
    return compose(compose(h, g), inverse(h))


def rz(theta: float) -> Matrix:
    c = math.cos(theta)
    s = math.sin(theta)
    return ((c, -s, 0.0), (s, c, 0.0), (0.0, 0.0, 1.0))


def norm(v: Vector) -> float:
    return math.sqrt(sum(x * x for x in v))


def max_matrix_error(a: Matrix, b: Matrix) -> float:
    return max(abs(a[i][j] - b[i][j]) for i in range(3) for j in range(3))


def max_vector_error(a: Vector, b: Vector) -> float:
    return max(abs(a[i] - b[i]) for i in range(3))


def is_identity(g: SE3) -> bool:
    r, t = g
    return max_matrix_error(r, I3) <= TOL and norm(t) <= TOL


def check(name: str, condition: bool, details: dict[str, object], checks: list[dict[str, object]]) -> None:
    checks.append({"name": name, "pass": bool(condition), **details})


def main() -> None:
    checks: list[dict[str, object]] = []

    # 1. Exact semidirect composition against direct affine evaluation.
    g1: SE3 = (rz(math.pi / 3.0), (1.25, -0.5, 0.75))
    g2: SE3 = (rz(-math.pi / 5.0), (-0.2, 0.4, 1.1))
    x: Vector = (0.3, -1.2, 2.0)
    gc = compose(g2, g1)
    direct = vt(mv(g2[0], vt(mv(g1[0], x), g1[1])), g2[1])
    composed = vt(mv(gc[0], x), gc[1])
    err = max_vector_error(direct, composed)
    check("semidirect_composition", err <= TOL, {"max_abs_error": err}, checks)

    # 2. Inverse closure.
    left = compose(inverse(g1), g1)
    right = compose(g1, inverse(g1))
    inv_ok = is_identity(left) and is_identity(right)
    check("inverse_identity", inv_ok, {"left": left, "right": right}, checks)

    # 3. Closed affine loop with exactly zero total holonomy.
    e1: SE3 = (I3, (1.0, 0.0, 0.0))
    e2: SE3 = (I3, (0.0, 2.0, 0.0))
    e3: SE3 = (I3, (-1.0, -2.0, 0.0))
    loop_closed = path_product((e1, e2, e3))
    check("exact_loop_identity", is_identity(loop_closed), {"loop": loop_closed}, checks)

    # 4. Gauge/frame covariance by explicit conjugation.
    base_loop: SE3 = (rz(math.pi / 7.0), (0.6, -0.1, 0.3))
    h: SE3 = (rz(math.pi / 4.0), (3.0, -2.0, 0.5))
    transformed = conjugate(h, base_loop)
    expected_r = mm(mm(h[0], base_loop[0]), transpose(h[0]))
    rot_err = max_matrix_error(transformed[0], expected_r)
    check("loop_conjugation_covariance", rot_err <= TOL, {"rotation_max_abs_error": rot_err}, checks)

    # 5. Pure translation norm invariance when R_loop = I.
    pure: SE3 = (I3, (0.4, -1.2, 2.3))
    pure_transformed = conjugate(h, pure)
    pure_rot_err = max_matrix_error(pure_transformed[0], I3)
    norm_err = abs(norm(pure_transformed[1]) - norm(pure[1]))
    check(
        "pure_translation_norm_invariance",
        pure_rot_err <= TOL and norm_err <= TOL,
        {"rotation_max_abs_error": pure_rot_err, "norm_abs_error": norm_err},
        checks,
    )

    # 6. Rotational-only insufficiency witness.
    rot_only_a = path_product(((I3, (1.0, 0.0, 0.0)), (I3, (-1.0, 0.0, 0.0))))
    rot_only_b = path_product(((I3, (1.0, 0.0, 0.0)), (I3, (0.0, 0.0, 0.0))))
    same_rot = max_matrix_error(rot_only_a[0], rot_only_b[0]) <= TOL
    different_affine = abs(norm(rot_only_a[1]) - norm(rot_only_b[1])) > 1e-6
    check(
        "rotational_only_insufficiency",
        same_rot and different_affine and is_identity(rot_only_a) and not is_identity(rot_only_b),
        {"closed_translation_norm": norm(rot_only_a[1]), "open_translation_norm": norm(rot_only_b[1])},
        checks,
    )

    # 7. Noncommutative composition witness: translation is rotated before addition.
    a: SE3 = (rz(math.pi / 2.0), (1.0, 0.0, 0.0))
    b: SE3 = (I3, (0.0, 1.0, 0.0))
    ab = compose(a, b)
    ba = compose(b, a)
    noncomm = max_matrix_error(ab[0], ba[0]) > TOL or max_vector_error(ab[1], ba[1]) > TOL
    check("semidirect_noncommutativity", noncomm, {"ab": ab, "ba": ba}, checks)

    passed = all(c["pass"] for c in checks)
    receipt = {
        "schema": "TIR_SE3_GLOBAL_GLUE_HOLONOMY_VALIDATION_V0_1",
        "technical_status": "PASS" if passed else "FAIL",
        "verdict": "PASS_TIR_SE3_AFFINE_HOLONOMY_ALGEBRAIC_GATE" if passed else "FAIL_TIR_SE3_AFFINE_HOLONOMY_ALGEBRAIC_GATE",
        "checks": checks,
        "physical_curvature_promotion": "GATED",
        "physical_torsion_promotion": "GATED",
        "gremlin_authority": "CANDIDATE_ONLY",
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
