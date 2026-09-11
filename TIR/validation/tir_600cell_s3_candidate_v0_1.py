#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import math
import numpy as np

PHI = (1.0 + math.sqrt(5.0)) / 2.0


def even_permutations4():
    out = []
    for p in itertools.permutations(range(4)):
        inv = sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
        if inv % 2 == 0:
            out.append(p)
    return out


def vertices600():
    out = []
    for i in range(4):
        for s in (-1.0, 1.0):
            v = [0.0] * 4
            v[i] = s
            out.append(v)
    for signs in itertools.product((-0.5, 0.5), repeat=4):
        out.append(list(signs))
    base = (0.0, 0.5, PHI / 2.0, 1.0 / (2.0 * PHI))
    for p in even_permutations4():
        perm = [base[p[i]] for i in range(4)]
        nz = [i for i, x in enumerate(perm) if x != 0.0]
        for signs in itertools.product((-1.0, 1.0), repeat=3):
            v = perm.copy()
            for idx, s in zip(nz, signs):
                v[idx] *= s
            out.append(v)
    v = np.asarray(out, dtype=float)
    assert v.shape == (120, 4)
    assert len(np.unique(np.round(v, 14), axis=0)) == 120
    assert np.allclose(np.sum(v * v, axis=1), 1.0, atol=2e-15, rtol=0.0)
    return v


def adjacency600(v):
    dots = v @ v.T
    a = np.isclose(dots, PHI / 2.0, atol=2e-12, rtol=0.0).astype(float)
    np.fill_diagonal(a, 0.0)
    assert np.array_equal(a, a.T)
    assert np.all(a.sum(axis=1) == 12.0)
    assert int(a.sum() // 2) == 720
    return a


def s3_moment(exponents):
    if any(e % 2 for e in exponents):
        return 0.0
    half = [e // 2 for e in exponents]
    total = sum(half)
    if total == 0:
        return 1.0
    num = 1
    for h in half:
        for k in range(1, h + 1):
            num *= 2 * k - 1
    den = 1
    for j in range(total):
        den *= 4 + 2 * j
    return num / den


def exponent_tuples(max_degree):
    for total in range(max_degree + 1):
        for a in range(total + 1):
            for b in range(total - a + 1):
                for c in range(total - a - b + 1):
                    d = total - a - b - c
                    yield (a, b, c, d)


def main():
    v = vertices600()
    a = adjacency600(v)
    eig = np.linalg.eigvalsh(a)
    expected = {
        12.0: 1,
        6.0 * PHI: 4,
        4.0 * PHI: 9,
        3.0: 16,
        0.0: 25,
        -2.0: 36,
        -3.0: 16,
        2.0 * (1.0 - math.sqrt(5.0)): 9,
        3.0 * (1.0 - math.sqrt(5.0)): 4,
    }
    for value, multiplicity in expected.items():
        got = int(np.count_nonzero(np.isclose(eig, value, atol=2e-10, rtol=0.0)))
        assert got == multiplicity, (value, got, multiplicity)

    low = {}
    for ell, value in {
        0: 12.0,
        1: 6.0 * PHI,
        2: 4.0 * PHI,
        3: 3.0,
        4: 0.0,
        5: -2.0,
    }.items():
        got = int(np.count_nonzero(np.isclose(eig, value, atol=2e-10, rtol=0.0)))
        assert got == (ell + 1) ** 2
        low[str(ell)] = {
            "adjacency_eigenvalue": value,
            "multiplicity": got,
            "s3_laplacian": ell * (ell + 2),
        }

    max_error = 0.0
    for exps in exponent_tuples(11):
        sampled = float(np.mean(np.prod(v ** np.asarray(exps), axis=1)))
        exact = float(s3_moment(exps))
        max_error = max(max_error, abs(sampled - exact))
    assert max_error < 1e-14

    sampled12 = float(np.mean(v[:, 0] ** 12))
    exact12 = float(s3_moment((12, 0, 0, 0)))
    degree12_break = sampled12 - exact12
    assert math.isclose(degree12_break, 1.0 / 4096.0, abs_tol=1e-15, rel_tol=0.0)

    print(json.dumps({
        "schema": "TIR_600CELL_S3_CANDIDATE_VALIDATION_V0_1",
        "status": "PASS",
        "implementation_status": "CANDIDATE",
        "vertices": 120,
        "dimension": 4,
        "graph_degree": 12,
        "edges": 720,
        "validated_low_sectors": low,
        "spherical_design_degree_tested": 11,
        "spherical_design_max_abs_error": max_error,
        "degree12_break_x1_12": degree12_break,
        "physical_binding": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
