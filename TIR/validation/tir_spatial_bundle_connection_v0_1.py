#!/usr/bin/env python3
"""Deterministic audit for TIR Spatial Bundle and Connection v0.1."""
from __future__ import annotations

import json

Matrix = tuple[tuple[complex, complex], tuple[complex, complex]]

SX: Matrix = ((0j, 1 + 0j), (1 + 0j, 0j))
SY: Matrix = ((0j, -1j), (1j, 0j))
SZ: Matrix = ((1 + 0j, 0j), (0j, -1 + 0j))
PAULI = (SX, SY, SZ)


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def matsub(a: Matrix, b: Matrix) -> Matrix:
    return tuple(tuple(a[i][j] - b[i][j] for j in range(2)) for i in range(2))  # type: ignore[return-value]


def scale(c: complex, a: Matrix) -> Matrix:
    return tuple(tuple(c * a[i][j] for j in range(2)) for i in range(2))  # type: ignore[return-value]


def mateq(a: Matrix, b: Matrix, tol: float = 1e-12) -> bool:
    return all(abs(a[i][j] - b[i][j]) <= tol for i in range(2) for j in range(2))


def commutator(a: Matrix, b: Matrix) -> Matrix:
    return matsub(matmul(a, b), matmul(b, a))


def t_generators() -> tuple[Matrix, Matrix, Matrix]:
    return tuple(scale(-0.5j, sigma) for sigma in PAULI)  # type: ignore[return-value]


def lie_algebra_certificate() -> dict[str, object]:
    tx, ty, tz = t_generators()
    checks = {
        "[Tx,Ty]=Tz": mateq(commutator(tx, ty), tz),
        "[Ty,Tz]=Tx": mateq(commutator(ty, tz), tx),
        "[Tz,Tx]=Ty": mateq(commutator(tz, tx), ty),
    }
    return {"checks": checks, "pass": all(checks.values())}


def so3_generator_certificate() -> dict[str, object]:
    # Standard real so(3) generators J_i with (J_i)_{jk}=-epsilon_{ijk}.
    jx = (
        (0.0, 0.0, 0.0),
        (0.0, 0.0, -1.0),
        (0.0, 1.0, 0.0),
    )
    jy = (
        (0.0, 0.0, 1.0),
        (0.0, 0.0, 0.0),
        (-1.0, 0.0, 0.0),
    )
    jz = (
        (0.0, -1.0, 0.0),
        (1.0, 0.0, 0.0),
        (0.0, 0.0, 0.0),
    )

    def mm(a, b):
        return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)) for i in range(3))

    def sub(a, b):
        return tuple(tuple(a[i][j] - b[i][j] for j in range(3)) for i in range(3))

    def eq(a, b, tol=1e-12):
        return all(abs(a[i][j] - b[i][j]) <= tol for i in range(3) for j in range(3))

    checks = {
        "[Jx,Jy]=Jz": eq(sub(mm(jx, jy), mm(jy, jx)), jz),
        "[Jy,Jz]=Jx": eq(sub(mm(jy, jz), mm(jz, jy)), jx),
        "[Jz,Jx]=Jy": eq(sub(mm(jz, jx), mm(jx, jz)), jy),
    }
    return {"checks": checks, "pass": all(checks.values())}


def cocycle_certificate() -> dict[str, object]:
    # Exact orientation-preserving quarter-turn matrices with R_ab R_bc R_ca = I.
    r_ab = (
        (0, -1, 0),
        (1, 0, 0),
        (0, 0, 1),
    )
    r_bc = (
        (1, 0, 0),
        (0, 0, -1),
        (0, 1, 0),
    )

    def mm(a, b):
        return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(3)) for j in range(3)) for i in range(3))

    def transpose(a):
        return tuple(tuple(a[j][i] for j in range(3)) for i in range(3))

    identity = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    r_ac = mm(r_ab, r_bc)
    r_ca = transpose(r_ac)
    closure = mm(mm(r_ab, r_bc), r_ca)
    return {"closure_matrix": closure, "pass": closure == identity}


def frame_metric_certificate() -> dict[str, object]:
    # h_ij = delta_ab e^a_i e^b_j for a nontrivial coframe.
    e = (
        (2.0, 0.0, 0.0),
        (0.0, 3.0, 0.0),
        (0.0, 0.0, 4.0),
    )
    h = tuple(tuple(sum(e[a][i] * e[a][j] for a in range(3)) for j in range(3)) for i in range(3))
    expected = ((4.0, 0.0, 0.0), (0.0, 9.0, 0.0), (0.0, 0.0, 16.0))
    positive_diagonal = all(h[i][i] > 0 for i in range(3))
    return {"h": h, "positive_diagonal": positive_diagonal, "pass": h == expected and positive_diagonal}


def build_receipt() -> dict[str, object]:
    blocks = {
        "su2_structure_constants": lie_algebra_certificate(),
        "so3_structure_constants": so3_generator_certificate(),
        "sample_so3_cocycle": cocycle_certificate(),
        "coframe_metric_construction": frame_metric_certificate(),
    }
    passed = all(block["pass"] for block in blocks.values())
    return {
        "schema": "TIR_SPATIAL_BUNDLE_CONNECTION_V0_1",
        "scope": "TIR_LOCAL_GENERATOR_TO_SPATIAL_BUNDLE_AUDIT",
        "rank": 3,
        "structure_group": "SO(3)",
        "double_cover_group": "SU(2)",
        "tangent_bundle_promotion_open": True,
        "solder_form_derivation_open": True,
        "levi_civita_gate": "metric_compatibility_plus_zero_torsion",
        "next_gate": "DERIVE_SOLDER_FORM_FROM_PRIMITIVE_RELATIONAL_DISPLACEMENT",
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
