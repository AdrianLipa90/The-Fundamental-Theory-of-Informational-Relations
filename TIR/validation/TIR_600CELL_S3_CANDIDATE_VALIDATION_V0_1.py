#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import math

import numpy as np

PHI = (1.0 + math.sqrt(5.0)) / 2.0


def parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2


def vertices600():
    rows = []
    for axis in range(4):
        for sign in (-1.0, 1.0):
            v = [0.0] * 4
            v[axis] = sign
            rows.append(tuple(v))
    rows.extend(itertools.product((-0.5, 0.5), repeat=4))
    base = (0.0, 0.5, PHI / 2.0, 1.0 / (2.0 * PHI))
    for p in (p for p in itertools.permutations(range(4)) if parity(p) == 0):
        q = [base[p[i]] for i in range(4)]
        nz = [i for i, x in enumerate(q) if x != 0.0]
        for signs in itertools.product((-1.0, 1.0), repeat=3):
            v = q.copy()
            for i, sign in zip(nz, signs):
                v[i] *= sign
            rows.append(tuple(v))
    return np.unique(np.round(np.asarray(rows, dtype=np.float64), 14), axis=0)


def moment_s3(exp):
    if any(e % 2 for e in exp):
        return 0.0
    half = [e // 2 for e in exp]
    total = sum(half)
    value = math.gamma(2.0) / math.gamma(2.0 + total)
    for b in half:
        value *= math.gamma(b + 0.5) / math.gamma(0.5)
    return float(value)


def exponents_of_total(total):
    for a in range(total + 1):
        for b in range(total - a + 1):
            for c in range(total - a - b + 1):
                yield (a, b, c, total - a - b - c)


def clusters(values, tol=1e-9):
    out = []
    for x in np.sort(values):
        x = float(x)
        if not out or abs(x - out[-1][0]) > tol:
            out.append([x, 1])
        else:
            out[-1][1] += 1
    return [(float(x), int(n)) for x, n in out]


def main():
    v = vertices600()
    assert v.shape == (120, 4)
    assert np.allclose(np.linalg.norm(v, axis=1), 1.0, rtol=0.0, atol=4e-14)
    dots = v @ v.T
    a = np.isclose(dots, PHI / 2.0, rtol=0.0, atol=2e-13).astype(np.float64)
    np.fill_diagonal(a, 0.0)
    assert np.array_equal(a, a.T)
    assert np.all(a.sum(axis=1) == 12.0)
    assert int(a.sum() // 2) == 720

    observed = clusters(np.linalg.eigvalsh(a))
    expected = [
        (-6.0 / PHI, 4), (-3.0, 16), (-4.0 / PHI, 9), (-2.0, 36),
        (0.0, 25), (3.0, 16), (4.0 * PHI, 9), (6.0 * PHI, 4), (12.0, 1),
    ]
    assert len(observed) == len(expected)
    for (got_v, got_m), (want_v, want_m) in zip(observed, expected):
        assert got_m == want_m
        assert math.isclose(got_v, want_v, rel_tol=0.0, abs_tol=3e-12)

    l0_l5 = [(1, 0), (4, 3), (9, 8), (16, 15), (25, 24), (36, 35)]
    assert sum(mult for mult, _ in l0_l5) == 91

    checked = 0
    max_error = 0.0
    for total in range(12):
        for exp in exponents_of_total(total):
            sampled = float(np.mean(np.prod(v ** np.asarray(exp), axis=1)))
            exact = moment_s3(exp)
            max_error = max(max_error, abs(sampled - exact))
            checked += 1
    assert checked == 1365
    assert max_error < 3e-14

    sampled12 = float(np.mean(v[:, 0] ** 12))
    exact12 = moment_s3((12, 0, 0, 0))
    witness12 = sampled12 - exact12
    assert math.isclose(witness12, 1.0 / 4096.0, rel_tol=0.0, abs_tol=2e-15)

    print(json.dumps({
        "schema": "TIR_600CELL_S3_CANDIDATE_VALIDATION_V0_1",
        "status": "PASS",
        "claim_status": "CANDIDATE",
        "active_working_version": True,
        "canonical": False,
        "physical_binding": "OPEN",
        "vertices": 120,
        "dimension": 4,
        "degree": 12,
        "edges": 720,
        "supported_l": [0, 1, 2, 3, 4, 5],
        "supported_dimension": 91,
        "s3_angular_eigenvalues": [0, 3, 8, 15, 24, 35],
        "monomials_checked_degree_le_11": checked,
        "max_degree_le_11_error": max_error,
        "degree_12_witness_error": witness12,
        "degree_12_witness_expected": 1.0 / 4096.0,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
