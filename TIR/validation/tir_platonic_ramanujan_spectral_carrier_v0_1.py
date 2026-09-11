#!/usr/bin/env python3
"""Deterministic validation for the TIR Platonic-Ramanujan spectral carrier v0.1.

Scope:
- finite graph/combinatorial facts;
- exact/algebraic spectrum checks to floating tolerance;
- local linearized stability bound for the declared candidate regularizer.

This validator does not establish a physical interpretation or global nonlinear
stability of PhaseNav.
"""

from __future__ import annotations

import json
import math
from itertools import combinations, product

import numpy as np


SQRT5 = math.sqrt(5.0)
TOL = 2e-12

ICOSAHEDRAL_EDGES = (
    (0, 1), (0, 5), (0, 7), (0, 8), (0, 11),
    (1, 2), (1, 5), (1, 6), (1, 8),
    (2, 3), (2, 6), (2, 8), (2, 9),
    (3, 4), (3, 6), (3, 9), (3, 10),
    (4, 5), (4, 6), (4, 10), (4, 11),
    (5, 6), (5, 11),
    (7, 8), (7, 9), (7, 10), (7, 11),
    (8, 9), (9, 10), (10, 11),
)


def adjacency(n: int, edges: tuple[tuple[int, int], ...]) -> np.ndarray:
    a = np.zeros((n, n), dtype=np.float64)
    for i, j in edges:
        if i == j:
            raise AssertionError("self-loop")
        a[i, j] = 1.0
        a[j, i] = 1.0
    return a


def tetrahedron() -> np.ndarray:
    return np.ones((4, 4), dtype=np.float64) - np.eye(4)


def cube() -> np.ndarray:
    vertices = list(product((0, 1), repeat=3))
    index = {v: i for i, v in enumerate(vertices)}
    edges: list[tuple[int, int]] = []
    for i, v in enumerate(vertices):
        for bit in range(3):
            w = list(v)
            w[bit] ^= 1
            j = index[tuple(w)]
            if i < j:
                edges.append((i, j))
    return adjacency(8, tuple(edges))


def octahedron() -> np.ndarray:
    opposite = {0: 1, 1: 0, 2: 3, 3: 2, 4: 5, 5: 4}
    edges = tuple(
        (i, j)
        for i in range(6)
        for j in range(i + 1, 6)
        if opposite[i] != j
    )
    return adjacency(6, edges)


def icosahedron() -> np.ndarray:
    return adjacency(12, ICOSAHEDRAL_EDGES)


def dodecahedron() -> np.ndarray:
    ai = icosahedron()
    faces: list[tuple[int, int, int]] = []
    for tri in combinations(range(12), 3):
        if ai[tri[0], tri[1]] and ai[tri[0], tri[2]] and ai[tri[1], tri[2]]:
            faces.append(tri)
    assert len(faces) == 20
    edges: list[tuple[int, int]] = []
    for i, f in enumerate(faces):
        sf = set(f)
        for j in range(i + 1, len(faces)):
            if len(sf.intersection(faces[j])) == 2:
                edges.append((i, j))
    assert len(edges) == 30
    return adjacency(20, tuple(edges))


def spectrum(a: np.ndarray) -> np.ndarray:
    return np.linalg.eigvalsh(a)


def assert_spectrum(a: np.ndarray, expected: list[float]) -> None:
    got = np.sort(spectrum(a))
    exp = np.sort(np.asarray(expected, dtype=np.float64))
    assert got.shape == exp.shape
    assert np.allclose(got, exp, rtol=0.0, atol=TOL), (got, exp)


def is_connected(a: np.ndarray) -> bool:
    seen = {0}
    stack = [0]
    while stack:
        i = stack.pop()
        for j in np.flatnonzero(a[i]):
            jj = int(j)
            if jj not in seen:
                seen.add(jj)
                stack.append(jj)
    return len(seen) == a.shape[0]


def ramanujan_metrics(a: np.ndarray, *, bipartite: bool = False) -> dict[str, float | bool | int]:
    deg = np.sum(a, axis=1)
    assert np.all(deg == deg[0])
    k = int(deg[0])
    eig = np.sort(spectrum(a))[::-1]
    nontrivial: list[float] = []
    for x in eig:
        if abs(float(x) - k) <= TOL:
            continue
        if bipartite and abs(float(x) + k) <= TOL:
            continue
        nontrivial.append(float(x))
    rho = max(abs(x) for x in nontrivial)
    bound = 2.0 * math.sqrt(k - 1.0)
    return {
        "vertices": int(a.shape[0]),
        "degree": k,
        "rho_nontrivial": rho,
        "ramanujan_bound": bound,
        "is_ramanujan": bool(rho <= bound + TOL),
    }


def carrier36() -> np.ndarray:
    ai = icosahedron()
    k3 = tetrahedron()[:3, :3]
    a = np.kron(ai, np.eye(3)) + np.kron(np.eye(12), k3)
    assert a.shape == (36, 36)
    return a


def main() -> int:
    platonic = {
        "tetrahedron": (tetrahedron(), [3.0] + [-1.0] * 3, False),
        "cube": (cube(), [3.0] + [1.0] * 3 + [-1.0] * 3 + [-3.0], True),
        "octahedron": (octahedron(), [4.0] + [0.0] * 3 + [-2.0] * 2, False),
        "dodecahedron": (
            dodecahedron(),
            [3.0] + [SQRT5] * 3 + [1.0] * 5 + [0.0] * 4 + [-2.0] * 4 + [-SQRT5] * 3,
            False,
        ),
        "icosahedron": (
            icosahedron(),
            [5.0] + [SQRT5] * 3 + [-1.0] * 5 + [-SQRT5] * 3,
            False,
        ),
    }

    platonic_metrics: dict[str, dict[str, float | bool | int]] = {}
    for name, (a, expected, bipartite) in platonic.items():
        assert np.array_equal(a, a.T)
        assert np.all(np.diag(a) == 0.0)
        assert is_connected(a)
        assert_spectrum(a, expected)
        metrics = ramanujan_metrics(a, bipartite=bipartite)
        assert metrics["is_ramanujan"]
        platonic_metrics[name] = metrics

    g36 = carrier36()
    assert np.array_equal(g36, g36.T)
    assert np.all(np.diag(g36) == 0.0)
    assert is_connected(g36)
    assert np.all(g36.sum(axis=1) == 7.0)
    assert int(g36.sum() // 2) == 126

    expected36 = (
        [7.0] * 1
        + [2.0 + SQRT5] * 3
        + [4.0] * 2
        + [SQRT5 - 1.0] * 6
        + [1.0] * 5
        + [2.0 - SQRT5] * 3
        + [-2.0] * 10
        + [-1.0 - SQRT5] * 6
    )
    assert_spectrum(g36, expected36)
    metrics36 = ramanujan_metrics(g36)
    assert metrics36["degree"] == 7
    assert math.isclose(
        float(metrics36["rho_nontrivial"]), 2.0 + SQRT5, rel_tol=0.0, abs_tol=TOL
    )
    assert metrics36["is_ramanujan"]

    normalized_gap = 1.0 - (2.0 + SQRT5) / 7.0
    assert math.isclose(normalized_gap, (5.0 - SQRT5) / 7.0, abs_tol=TOL)

    L3, L4, L5 = 7, 2, 5
    assert L4 + L5 == L3
    assert int(g36.sum(axis=1)[0]) == L3
    assert int(icosahedron().sum(axis=1)[0]) == L5
    assert int((np.ones((3, 3)) - np.eye(3)).sum(axis=1)[0]) == L4

    result = {
        "schema": "TIR_PLATONIC_RAMANUJAN_SPECTRAL_CARRIER_VALIDATION_V0_1",
        "status": "PASS",
        "claim_scope": "EXACT_GRAPH_SPECTRAL_FACTS_PLUS_TIR_CANDIDATE_CARRIER",
        "platonic_graphs": platonic_metrics,
        "carrier36": {
            **metrics36,
            "edge_count": 126,
            "rho_exact": "2+sqrt(5)",
            "normalized_laplacian_gap": normalized_gap,
            "normalized_laplacian_gap_exact": "(5-sqrt(5))/7",
            "degree_identity": "7 = L3 = L4+L5 = 2+5",
            "factorization": "I12 square K3",
        },
        "stability_statement": {
            "scope": "LOCAL_LINEARIZATION_ONLY",
            "candidate_term": "C_PR=-(beta/7) A sin(phi_i-phi_j)",
            "mean_zero_decay_rate_lower_bound": "beta*(5-sqrt(5))/7",
            "global_nonlinear_stability_claim": False,
        },
        "physical_claim": False,
    }
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
