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
    return tuple(out)


def vertices600():
    out = []
    for i in range(4):
        for sign in (-1.0, 1.0):
            v = [0.0] * 4
            v[i] = sign
            out.append(v)
    for signs in itertools.product((-0.5, 0.5), repeat=4):
        out.append(list(signs))
    base = (0.0, 0.5, PHI / 2.0, 1.0 / (2.0 * PHI))
    for p in even_permutations4():
        perm = [base[p[i]] for i in range(4)]
        nz = [i for i, x in enumerate(perm) if x != 0.0]
        for signs in itertools.product((-1.0, 1.0), repeat=3):
            v = perm.copy()
            for idx, sign in zip(nz, signs):
                v[idx] *= sign
            out.append(v)
    vertices = np.asarray(out, dtype=np.float64)
    assert vertices.shape == (120, 4)
    assert len(np.unique(np.round(vertices, 14), axis=0)) == 120
    assert np.allclose(np.sum(vertices * vertices, axis=1), 1.0, rtol=0.0, atol=2e-15)
    return vertices


def monomial_exponents(total_degree: int):
    out = []
    for a in range(total_degree + 1):
        for b in range(total_degree - a + 1):
            for c in range(total_degree - a - b + 1):
                d = total_degree - a - b - c
                out.append((a, b, c, d))
    return tuple(out)


def harmonic_evaluation_matrix(points: np.ndarray, ell: int) -> np.ndarray:
    """Evaluate a numerical basis of homogeneous harmonic polynomials H_ell(R^4).

    Homogeneous degree-ell monomials are constrained by the Euclidean
    Laplacian. The nullspace of that exact coefficient map is the harmonic
    subspace, whose continuum dimension is (ell+1)^2.
    """
    exponents = monomial_exponents(ell)
    evaluation = np.column_stack(
        [np.prod(points ** np.asarray(e), axis=1) for e in exponents]
    )
    if ell < 2:
        return evaluation

    lower = monomial_exponents(ell - 2)
    lower_index = {e: i for i, e in enumerate(lower)}
    laplacian = np.zeros((len(lower), len(exponents)), dtype=np.float64)
    for j, e in enumerate(exponents):
        for coordinate in range(4):
            power = e[coordinate]
            if power >= 2:
                reduced = list(e)
                reduced[coordinate] -= 2
                laplacian[lower_index[tuple(reduced)], j] += power * (power - 1)

    _, singular_values, vh = np.linalg.svd(laplacian, full_matrices=True)
    rank = int(np.count_nonzero(singular_values > 1e-12))
    nullspace = vh[rank:].T
    assert nullspace.shape[1] == (ell + 1) ** 2
    return evaluation @ nullspace


def numerical_rank(matrix: np.ndarray) -> int:
    return int(np.linalg.matrix_rank(matrix, tol=1e-10))


def main():
    vertices = vertices600()

    per_sector_rank = {}
    cumulative_rank = {}
    blocks = []

    expected_sector_ranks = [1, 4, 9, 16, 25, 36, 25, 40]
    expected_cumulative_ranks = [1, 5, 14, 30, 55, 91, 116, 120]

    for ell in range(8):
        block = harmonic_evaluation_matrix(vertices, ell)
        blocks.append(block)
        sector_rank = numerical_rank(block)
        cumulative = np.column_stack(blocks)
        total_rank = numerical_rank(cumulative)

        assert sector_rank == expected_sector_ranks[ell], (
            ell,
            sector_rank,
            expected_sector_ranks[ell],
        )
        assert total_rank == expected_cumulative_ranks[ell], (
            ell,
            total_rank,
            expected_cumulative_ranks[ell],
        )

        per_sector_rank[str(ell)] = {
            "continuum_dimension": (ell + 1) ** 2,
            "sampled_rank": sector_rank,
        }
        cumulative_rank[str(ell)] = total_rank

    # Exact low-sector sampling through ell=5.
    for ell in range(6):
        assert per_sector_rank[str(ell)]["sampled_rank"] == (ell + 1) ** 2

    # First rank collapse occurs at ell=6: 49 continuum directions -> 25 sampled.
    assert per_sector_rank["6"]["continuum_dimension"] == 49
    assert per_sector_rank["6"]["sampled_rank"] == 25
    assert cumulative_rank["5"] == 91
    assert cumulative_rank["6"] == 116

    # ell=7 has rank 40 by itself but contributes exactly four new directions,
    # completing the finite 120-dimensional sample space.
    assert per_sector_rank["7"]["sampled_rank"] == 40
    assert cumulative_rank["7"] - cumulative_rank["6"] == 4
    assert cumulative_rank["7"] == 120

    print(
        json.dumps(
            {
                "schema": "TIR_600CELL_S3_RANK_CLOSURE_CANDIDATE_V0_2",
                "status": "PASS",
                "implementation_status": "CANDIDATE",
                "per_sector_rank": per_sector_rank,
                "cumulative_rank": cumulative_rank,
                "l0_l5_exact_sampling": True,
                "l6_first_rank_collapse": True,
                "l6_continuum_dimension": 49,
                "l6_sampled_rank": 25,
                "l7_sampled_rank": 40,
                "l7_new_directions_beyond_l0_l6": 4,
                "finite_sample_space_closed_by_l7": True,
                "finite_sample_dimension": 120,
                "physical_binding": False,
                "fractal_interpretation": "OPEN",
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
