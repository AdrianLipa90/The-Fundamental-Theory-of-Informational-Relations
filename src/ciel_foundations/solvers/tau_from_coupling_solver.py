"""Toy solver for tau-from-coupling via a Laplacian generator."""

from __future__ import annotations

import math
from typing import List, Sequence


def _validate_kernel(A: Sequence[Sequence[float]], atol: float = 1e-12) -> None:
    n = len(A)
    if n == 0:
        raise ValueError("kernel must be nonempty")
    for row in A:
        if len(row) != n:
            raise ValueError("kernel must be square")
    for i in range(n):
        for j in range(n):
            if A[i][j] < -atol:
                raise ValueError("kernel must be nonnegative")
            if abs(A[i][j] - A[j][i]) > atol:
                raise ValueError("kernel must be symmetric")


def strength_vector(A: Sequence[Sequence[float]]) -> List[float]:
    _validate_kernel(A)
    return [float(sum(row)) for row in A]


def laplacian_matrix(A: Sequence[Sequence[float]]) -> List[List[float]]:
    d = strength_vector(A)
    n = len(A)
    return [[(d[i] if i == j else 0.0) - float(A[i][j]) for j in range(n)] for i in range(n)]


def _solve_linear(M: List[List[float]], b: List[float]) -> List[float]:
    n = len(M)
    A = [row[:] + [rhs] for row, rhs in zip(M, b)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(A[r][col]))
        if abs(A[pivot][col]) < 1e-14:
            raise ValueError("singular system in tau_from_coupling solver")
        A[col], A[pivot] = A[pivot], A[col]
        piv = A[col][col]
        for j in range(col, n + 1):
            A[col][j] /= piv
        for r in range(n):
            if r == col:
                continue
            factor = A[r][col]
            for j in range(col, n + 1):
                A[r][j] -= factor * A[col][j]
    return [A[i][n] for i in range(n)]


def log_tau_from_coupling(A: Sequence[Sequence[float]], kappa: float = 1.0) -> List[float]:
    d = strength_vector(A)
    n = len(d)
    dbar = sum(d) / n
    rhs = [kappa * (di - dbar) for di in d]
    L = laplacian_matrix(A)
    if n == 1:
        return [0.0]
    M = [row[:-1] for row in L[:-1]]
    b = rhs[:-1]
    xi_reduced = _solve_linear(M, b)
    xi = xi_reduced + [0.0]
    mean_xi = sum(xi) / n
    return [x - mean_xi for x in xi]


def tau_from_coupling(A: Sequence[Sequence[float]], kappa: float = 1.0, tau_star: float = 1.0) -> List[float]:
    xi = log_tau_from_coupling(A, kappa=kappa)
    return [tau_star * math.exp(x) for x in xi]
