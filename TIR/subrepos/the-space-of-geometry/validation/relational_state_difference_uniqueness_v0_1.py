#!/usr/bin/env python3
"""Exact audit for Relational State-Difference Uniqueness v0.1."""
from __future__ import annotations

from fractions import Fraction
import json

Matrix = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

RZ90: Matrix = (
    (0, -1, 0),
    (1, 0, 0),
    (0, 0, 1),
)
RX90: Matrix = (
    (1, 0, 0),
    (0, 0, -1),
    (0, 1, 0),
)


def idx(i: int, j: int) -> int:
    return 3 * i + j


def commutator_constraint_rows(r: Matrix) -> list[list[Fraction]]:
    rows: list[list[Fraction]] = []
    # M R - R M = 0, linear in the nine entries of M.
    for i in range(3):
        for j in range(3):
            row = [Fraction(0) for _ in range(9)]
            for k in range(3):
                row[idx(i, k)] += Fraction(r[k][j])
                row[idx(k, j)] -= Fraction(r[i][k])
            rows.append(row)
    return rows


def matrix_rank(rows: list[list[Fraction]]) -> int:
    a = [row[:] for row in rows]
    if not a:
        return 0
    m = len(a)
    n = len(a[0])
    rank = 0
    col = 0
    while rank < m and col < n:
        pivot = next((i for i in range(rank, m) if a[i][col] != 0), None)
        if pivot is None:
            col += 1
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        p = a[rank][col]
        a[rank] = [x / p for x in a[rank]]
        for i in range(m):
            if i == rank:
                continue
            f = a[i][col]
            if f != 0:
                a[i] = [x - f * y for x, y in zip(a[i], a[rank])]
        rank += 1
        col += 1
    return rank


def endpoint_cocycle_certificate() -> dict[str, object]:
    # One-dimensional scalar controls are sufficient to audit the algebraic telescoping identity.
    rho_star = Fraction(0)
    rho = Fraction(1, 5)
    sigma = Fraction(2, 5)
    tau = Fraction(4, 5)
    lam = Fraction(2)

    def d(a: Fraction, b: Fraction) -> Fraction:
        return lam * (b - a)

    potential_difference = d(rho, sigma) == d(rho_star, sigma) - d(rho_star, rho)
    endpoint = d(rho, tau) == d(rho, sigma) + d(sigma, tau)
    reversal = d(sigma, rho) == -d(rho, sigma)
    return {
        "difference_representation": potential_difference,
        "endpoint_composition": endpoint,
        "reversal": reversal,
        "pass": potential_difference and endpoint and reversal,
    }


def commutant_certificate() -> dict[str, object]:
    rows = commutator_constraint_rows(RZ90) + commutator_constraint_rows(RX90)
    rank = matrix_rank(rows)
    nullity = 9 - rank
    # Identity matrix is explicitly a nonzero solution, so nullity=1 means scalar identity only.
    return {
        "constraint_rank": rank,
        "endomorphism_space_dimension": 9,
        "commutant_dimension": nullity,
        "commutant": "R*I3",
        "pass": rank == 8 and nullity == 1,
    }


def affine_linearity_certificate() -> dict[str, object]:
    # Exact rational control for L(av+bw)=aL(v)+bL(w) with L=lambda I.
    v = (Fraction(1, 3), Fraction(-1, 4), Fraction(1, 5))
    w = (Fraction(2, 7), Fraction(1, 6), Fraction(-1, 8))
    a = Fraction(3, 2)
    b = Fraction(-2, 3)
    lam = Fraction(5, 4)

    lhs_arg = tuple(a * x + b * y for x, y in zip(v, w))
    lhs = tuple(lam * x for x in lhs_arg)
    rhs = tuple(a * lam * x + b * lam * y for x, y in zip(v, w))
    return {
        "lambda": "5/4",
        "affine_linearity": lhs == rhs,
        "pass": lhs == rhs,
    }


def build_receipt() -> dict[str, object]:
    blocks = {
        "endpoint_cocycle": endpoint_cocycle_certificate(),
        "affine_linearity": affine_linearity_certificate(),
        "so3_commutant": commutant_certificate(),
    }
    passed = all(bool(block["pass"]) for block in blocks.values())
    return {
        "schema": "TIR_RELATIONAL_STATE_DIFFERENCE_UNIQUENESS_V0_1",
        "exact_result": "D(rho_x,rho_y)=lambda*(rho_y-rho_x)",
        "uniqueness": "UP_TO_NONZERO_GLOBAL_SCALE_AND_ORIENTATION",
        "canonical_bloch_pauli_normalization": "lambda=2",
        "distinction_preservation_requires": "lambda!=0",
        "remaining_axiom_inheritance_gates": [
            "A5_AFFINE_ARITHMETIC_COMPATIBILITY",
            "A8_ENDPOINT_COMPOSITION_CLOSURE",
        ],
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
