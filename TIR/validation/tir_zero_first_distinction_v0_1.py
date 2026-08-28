#!/usr/bin/env python3
"""Deterministic audit for the TIR zero -> first-distinction foundation.

The audit certifies the exact finite algebra that belongs directly to the TIR
crosswalk: zero entropy of the undivided carrier, the binary half seam, ln(2),
projector complementarity, Pauli noncommutativity, and a concrete pair of
noncommuting 3D rotation frames. Standard theorem dependencies for the unitary
generator, Robertson relation, CP^1 geometry, free SO(3) subgroups and
Banach--Tarski are emitted as typed requirements.
"""
from __future__ import annotations

import json
import math
from fractions import Fraction

Matrix = tuple[tuple[complex, ...], ...]


def matmul(a: Matrix, b: Matrix) -> Matrix:
    rows = len(a)
    inner = len(b)
    cols = len(b[0])
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols))
        for i in range(rows)
    )


def matsub(a: Matrix, b: Matrix) -> Matrix:
    return tuple(
        tuple(a[i][j] - b[i][j] for j in range(len(a[0])))
        for i in range(len(a))
    )


def matscale(c: complex, a: Matrix) -> Matrix:
    return tuple(tuple(c * value for value in row) for row in a)


def mateq(a: Matrix, b: Matrix, tol: float = 0.0) -> bool:
    for i in range(len(a)):
        for j in range(len(a[0])):
            if tol == 0.0:
                if a[i][j] != b[i][j]:
                    return False
            elif abs(a[i][j] - b[i][j]) > tol:
                return False
    return True


def matrix_receipt(a: Matrix) -> list[list[list[float]]]:
    return [
        [[float(value.real), float(value.imag)] for value in row]
        for row in a
    ]


def zero_and_half_certificate() -> dict[str, object]:
    h_zero = -1.0 * math.log(1.0)
    u = Fraction(1, 2)
    h_half = -0.5 * math.log(0.5) - 0.5 * math.log(0.5)
    return {
        "undivided_probability": [1, 1],
        "undivided_entropy": h_zero,
        "first_distinction_labels": ["N", "S"],
        "exchange_fixed_share": [u.numerator, u.denominator],
        "half_entropy": h_half,
        "ln2": math.log(2.0),
        "pass_zero": h_zero == 0.0,
        "pass_half_fixed_point": 1 - u == u,
        "pass_ln2": math.isclose(h_half, math.log(2.0), rel_tol=0.0, abs_tol=1e-15),
    }


def projector_certificate() -> dict[str, object]:
    pn: Matrix = ((1 + 0j, 0j), (0j, 0j))
    ps: Matrix = ((0j, 0j), (0j, 1 + 0j))
    ident: Matrix = ((1 + 0j, 0j), (0j, 1 + 0j))
    zero: Matrix = ((0j, 0j), (0j, 0j))
    add = tuple(tuple(pn[i][j] + ps[i][j] for j in range(2)) for i in range(2))
    passed = (
        mateq(matmul(pn, pn), pn)
        and mateq(matmul(ps, ps), ps)
        and mateq(matmul(pn, ps), zero)
        and mateq(add, ident)
    )
    return {
        "P_N": matrix_receipt(pn),
        "P_S": matrix_receipt(ps),
        "idempotent_N": mateq(matmul(pn, pn), pn),
        "idempotent_S": mateq(matmul(ps, ps), ps),
        "orthogonal": mateq(matmul(pn, ps), zero),
        "complete": mateq(add, ident),
        "pass": passed,
    }


def pauli_certificate() -> dict[str, object]:
    sx: Matrix = ((0j, 1 + 0j), (1 + 0j, 0j))
    sy: Matrix = ((0j, -1j), (1j, 0j))
    sz: Matrix = ((1 + 0j, 0j), (0j, -1 + 0j))
    comm_xz = matsub(matmul(sx, sz), matmul(sz, sx))
    expected_xz = matscale(-2j, sy)
    comm_zx = matsub(matmul(sz, sx), matmul(sx, sz))
    expected_zx = matscale(2j, sy)
    zero: Matrix = ((0j, 0j), (0j, 0j))
    return {
        "commutator_xz": matrix_receipt(comm_xz),
        "expected_xz_minus_2i_sigma_y": matrix_receipt(expected_xz),
        "commutator_zx": matrix_receipt(comm_zx),
        "expected_zx_2i_sigma_y": matrix_receipt(expected_zx),
        "pass_xz": mateq(comm_xz, expected_xz),
        "pass_zx": mateq(comm_zx, expected_zx),
        "noncommuting_distinction_axes": not mateq(comm_xz, zero),
        "pass": mateq(comm_xz, expected_xz) and mateq(comm_zx, expected_zx),
    }


def maximally_mixed_certificate() -> dict[str, object]:
    eigenvalues = (0.5, 0.5)
    entropy = -sum(lam * math.log(lam) for lam in eigenvalues)
    return {
        "rho_star": "I/2",
        "eigenvalues": list(eigenvalues),
        "von_neumann_entropy": entropy,
        "ln2": math.log(2.0),
        "pass": math.isclose(entropy, math.log(2.0), rel_tol=0.0, abs_tol=1e-15),
    }


def rotation_entry_certificate() -> dict[str, object]:
    rx: Matrix = (
        (1 + 0j, 0j, 0j),
        (0j, 0j, -1 + 0j),
        (0j, 1 + 0j, 0j),
    )
    rz: Matrix = (
        (0j, -1 + 0j, 0j),
        (1 + 0j, 0j, 0j),
        (0j, 0j, 1 + 0j),
    )
    rx_rz = matmul(rx, rz)
    rz_rx = matmul(rz, rx)
    noncommuting = not mateq(rx_rz, rz_rx)
    return {
        "R_x_pi_over_2": matrix_receipt(rx),
        "R_z_pi_over_2": matrix_receipt(rz),
        "R_x_R_z": matrix_receipt(rx_rz),
        "R_z_R_x": matrix_receipt(rz_rx),
        "distinct_axis_rotations_noncommute": noncommuting,
        "banach_tarski_theorem_dependencies": [
            "free non-abelian subgroup F2 of SO(3)",
            "paradoxical group action",
            "orbit-representative selection principle",
            "extension to three-dimensional sets",
        ],
        "pass": noncommuting,
    }


def build_receipt() -> dict[str, object]:
    zero_half = zero_and_half_certificate()
    projectors = projector_certificate()
    pauli = pauli_certificate()
    mixed = maximally_mixed_certificate()
    rotations = rotation_entry_certificate()
    passed = (
        zero_half["pass_zero"]
        and zero_half["pass_half_fixed_point"]
        and zero_half["pass_ln2"]
        and projectors["pass"]
        and pauli["pass"]
        and mixed["pass"]
        and rotations["pass"]
    )
    return {
        "schema": "TIR_ZERO_FIRST_DISTINCTION_V0_1",
        "scope": "TIR_STRUCTURAL_CROSSWALK",
        "dependency_graph": [
            "ZERO -> FIRST_DISTINCTION",
            "FIRST_DISTINCTION -> HALF_SEAM -> ln2",
            "FIRST_DISTINCTION -> C2 -> UNITARY_FLOW -> SCHRODINGER_GENERATOR",
            "C2 -> MULTIPLE_AXES -> PAULI_NONCOMMUTATIVITY -> ROBERTSON_HEISENBERG",
            "ORIENTED_AXIS -> S2 -> SO3 -> F2 -> PARADOXICAL_ACTION_PLUS_CHOICE -> BANACH_TARSKI",
        ],
        "standard_theorem_dependencies": {
            "schrodinger_branch": "strongly continuous one-parameter unitary group -> self-adjoint generator",
            "heisenberg_branch": "Robertson uncertainty theorem for self-adjoint observables",
            "geometry_branch": "CP1 is diffeomorphic to the two-sphere",
            "banach_tarski_branch": "free SO(3) subgroup + paradoxical action + choice-based orbit representatives",
        },
        "zero_and_half": zero_half,
        "projectors": projectors,
        "pauli": pauli,
        "maximally_mixed": mixed,
        "rotation_entry": rotations,
        "technical_status": "PASS" if passed else "FAIL",
    }


def main() -> None:
    receipt = build_receipt()
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if receipt["technical_status"] != "PASS":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
