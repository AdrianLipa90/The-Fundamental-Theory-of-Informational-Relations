#!/usr/bin/env python3
"""Deterministic audit for TIR Relational Generator Space v0.1."""
from __future__ import annotations

import json
import math

Matrix = tuple[tuple[complex, complex], tuple[complex, complex]]

I: Matrix = ((1 + 0j, 0j), (0j, 1 + 0j))
SX: Matrix = ((0j, 1 + 0j), (1 + 0j, 0j))
SY: Matrix = ((0j, -1j), (1j, 0j))
SZ: Matrix = ((1 + 0j, 0j), (0j, -1 + 0j))
PAULI = (SX, SY, SZ)


def matmul(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def dagger(a: Matrix) -> Matrix:
    return (
        (a[0][0].conjugate(), a[1][0].conjugate()),
        (a[0][1].conjugate(), a[1][1].conjugate()),
    )


def trace(a: Matrix) -> complex:
    return a[0][0] + a[1][1]


def add(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2)
    )  # type: ignore[return-value]


def scale(c: complex, a: Matrix) -> Matrix:
    return tuple(tuple(c * a[i][j] for j in range(2)) for i in range(2))  # type: ignore[return-value]


def hs(a: Matrix, b: Matrix) -> float:
    value = 0.5 * trace(matmul(a, b))
    if abs(value.imag) > 1e-12:
        raise ValueError("Hilbert-Schmidt product expected real")
    return float(value.real)


def mateq(a: Matrix, b: Matrix, tol: float = 1e-12) -> bool:
    return all(abs(a[i][j] - b[i][j]) <= tol for i in range(2) for j in range(2))


def pauli_metric_certificate() -> dict[str, object]:
    gram = [[hs(a, b) for b in PAULI] for a in PAULI]
    target = [[1.0 if i == j else 0.0 for j in range(3)] for i in range(3)]
    passed = all(abs(gram[i][j] - target[i][j]) <= 1e-12 for i in range(3) for j in range(3))
    traceless = all(abs(trace(s)) <= 1e-12 for s in PAULI)
    return {"gram": gram, "traceless_basis": traceless, "pass": passed and traceless}


def unit_sphere_certificate() -> dict[str, object]:
    rows = []
    passed = True
    samples = (
        (1.0, 0.0, 0.0),
        (0.0, 1.0, 0.0),
        (0.0, 0.0, 1.0),
        (1 / math.sqrt(3), 1 / math.sqrt(3), 1 / math.sqrt(3)),
    )
    for x, y, z in samples:
        a = add(add(scale(x, SX), scale(y, SY)), scale(z, SZ))
        norm_sq = hs(a, a)
        square = matmul(a, a)
        row_pass = abs(norm_sq - 1.0) <= 1e-12 and mateq(square, I)
        passed &= row_pass
        rows.append({"n": [x, y, z], "hs_norm_sq": norm_sq, "A2_equals_I": mateq(square, I), "pass": row_pass})
    return {"rows": rows, "pass": passed}


def su2_conjugation_certificate() -> dict[str, object]:
    # U = exp(-i theta sigma_z / 2), theta = pi/2.
    theta = math.pi / 2
    c = math.cos(theta / 2)
    s = math.sin(theta / 2)
    u: Matrix = ((c - 1j * s, 0j), (0j, c + 1j * s))
    ux = matmul(matmul(u, SX), dagger(u))
    uy = matmul(matmul(u, SY), dagger(u))
    uz = matmul(matmul(u, SZ), dagger(u))
    # With this convention z-rotation maps sigma_x -> sigma_y and sigma_y -> -sigma_x.
    pass_x = mateq(ux, SY)
    pass_y = mateq(uy, scale(-1, SX))
    pass_z = mateq(uz, SZ)
    metric_preserved = all(abs(hs(a, b) - hs(matmul(matmul(u, a), dagger(u)), matmul(matmul(u, b), dagger(u)))) <= 1e-12 for a in PAULI for b in PAULI)
    return {"sigma_x_to_sigma_y": pass_x, "sigma_y_to_minus_sigma_x": pass_y, "sigma_z_fixed": pass_z, "metric_preserved": metric_preserved, "pass": pass_x and pass_y and pass_z and metric_preserved}


def bloch_certificate() -> dict[str, object]:
    # |psi> = (|0> + exp(i phi)|1>)/sqrt(2), phi=pi/3.
    phi = math.pi / 3
    alpha = 1 / math.sqrt(2)
    beta = complex(math.cos(phi), math.sin(phi)) / math.sqrt(2)
    psi = (alpha + 0j, beta)

    def expectation(a: Matrix) -> float:
        ap = (
            a[0][0] * psi[0] + a[0][1] * psi[1],
            a[1][0] * psi[0] + a[1][1] * psi[1],
        )
        value = psi[0].conjugate() * ap[0] + psi[1].conjugate() * ap[1]
        if abs(value.imag) > 1e-12:
            raise ValueError("Expectation expected real")
        return float(value.real)

    r = [expectation(sigma) for sigma in PAULI]
    norm_sq = sum(v * v for v in r)
    return {"bloch_vector": r, "norm_sq": norm_sq, "pass": abs(norm_sq - 1.0) <= 1e-12}


def build_receipt() -> dict[str, object]:
    metric = pauli_metric_certificate()
    sphere = unit_sphere_certificate()
    rotation = su2_conjugation_certificate()
    bloch = bloch_certificate()
    passed = metric["pass"] and sphere["pass"] and rotation["pass"] and bloch["pass"]
    return {
        "schema": "TIR_RELATIONAL_GENERATOR_SPACE_V0_1",
        "scope": "TIR_BINARY_QUANTUM_TO_REAL_GENERATOR_SPACE_AUDIT",
        "herm2_real_dimension": 4,
        "herm0_2_real_dimension": 3,
        "conditional_spatial_dimension": 3,
        "standard_theorem_dependency": "Ad:SU(2)->SO(3) with kernel {+I,-I}",
        "spatial_promotion_gate_open": True,
        "next_gate": "GLUE_LOCAL_HERM0_2_CARRIERS_INTO_SPATIAL_TANGENT_BUNDLE",
        "blocks": {
            "pauli_hilbert_schmidt_metric": metric,
            "unit_generator_sphere": sphere,
            "sample_su2_conjugation_rotation": rotation,
            "pure_state_bloch_unit_vector": bloch,
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
