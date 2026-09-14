#!/usr/bin/env python3
from __future__ import annotations

import cmath
import itertools
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction

PHI = (1.0 + math.sqrt(5.0)) / 2.0
KAPPA = math.log(2.0) / (24.0 * math.pi)


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
            out.append(tuple(v))
    for signs in itertools.product((-0.5, 0.5), repeat=4):
        out.append(tuple(signs))
    base = (0.0, 0.5, PHI / 2.0, 1.0 / (2.0 * PHI))
    for p in even_permutations4():
        perm = [base[p[i]] for i in range(4)]
        nz = [i for i, x in enumerate(perm) if x != 0.0]
        for signs in itertools.product((-1.0, 1.0), repeat=3):
            v = perm.copy()
            for idx, s in zip(nz, signs):
                v[idx] *= s
            out.append(tuple(v))
    assert len(out) == 120
    assert len({tuple(round(x, 14) for x in v) for v in out}) == 120
    return out


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def adjacency600(v):
    n = len(v)
    adj = [set() for _ in range(n)]
    target = PHI / 2.0
    for i in range(n):
        for j in range(i + 1, n):
            if math.isclose(dot(v[i], v[j]), target, abs_tol=2e-12, rel_tol=0.0):
                adj[i].add(j)
                adj[j].add(i)
    assert all(len(row) == 12 for row in adj)
    assert sum(len(row) for row in adj) // 2 == 720
    return adj


def tetrahedral_cells(adj):
    cells = set()
    for a, neigh_a in enumerate(adj):
        neigh = sorted(b for b in neigh_a if b > a)
        for b, c, d in itertools.combinations(neigh, 3):
            if c in adj[b] and d in adj[b] and d in adj[c]:
                cells.add((a, b, c, d))
    assert len(cells) == 600
    return sorted(cells)


def ckm_matrix(s12, s23, s13, delta):
    c12 = math.sqrt(1.0 - s12 * s12)
    c23 = math.sqrt(1.0 - s23 * s23)
    c13 = math.sqrt(1.0 - s13 * s13)
    epos = cmath.exp(1j * delta)
    eneg = cmath.exp(-1j * delta)
    return [
        [c12 * c13, s12 * c13, s13 * eneg],
        [-s12 * c23 - c12 * s23 * s13 * epos,
         c12 * c23 - s12 * s23 * s13 * epos,
         s23 * c13],
        [s12 * s23 - c12 * c23 * s13 * epos,
         -c12 * s23 - s12 * c23 * s13 * epos,
         c23 * c13],
    ]


def dagger_product_residual(V):
    worst = 0.0
    for i in range(3):
        for j in range(3):
            val = sum(V[i][k] * V[j][k].conjugate() for k in range(3))
            target = 1.0 if i == j else 0.0
            worst = max(worst, abs(val - target))
    return worst


def det3(M):
    return (
        M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
    )


def main():
    vertices = vertices600()
    adj = adjacency600(vertices)
    cells = tetrahedral_cells(adj)

    face_counts = Counter()
    edge_counts = Counter()
    edge_to_cells = defaultdict(set)

    for ci, cell in enumerate(cells):
        for face in itertools.combinations(cell, 3):
            face_counts[tuple(sorted(face))] += 1
        for edge in itertools.combinations(cell, 2):
            edge = tuple(sorted(edge))
            edge_counts[edge] += 1
            edge_to_cells[edge].add(ci)

    assert len(face_counts) == 1200
    assert set(face_counts.values()) == {2}
    assert len(edge_counts) == 720
    assert set(edge_counts.values()) == {5}

    face_edge_pairs = 0
    edge_star_overlap_values = set()
    for face in face_counts:
        fedges = [tuple(sorted(e)) for e in itertools.combinations(face, 2)]
        for e1, e2 in itertools.combinations(fedges, 2):
            inter = len(edge_to_cells[e1] & edge_to_cells[e2])
            assert inter == 2
            overlap = Fraction(inter, len(edge_to_cells[e1]))
            edge_star_overlap_values.add(overlap)
            face_edge_pairs += 1

    assert face_edge_pairs == 3600
    assert edge_star_overlap_values == {Fraction(2, 5)}

    nu_F = 2
    nu_E = 5
    a = Fraction(nu_F, nu_F + nu_E)
    b = Fraction(nu_F, 2 * nu_F + nu_E)
    c = Fraction(nu_F, nu_E)
    h = Fraction(1, nu_F)

    assert a == Fraction(2, 7)
    assert b == Fraction(2, 9)
    assert c == Fraction(2, 5)
    assert h == Fraction(1, 2)

    s12 = float(b) + float(a) * KAPPA
    s23 = float(h * a * a)
    s13 = s23 * float(b) * float(c)
    delta = math.acos(float(c))

    assert math.isclose(s23, 2.0 / 49.0, abs_tol=1e-15, rel_tol=0.0)
    assert math.isclose(s13, 8.0 / 2205.0, abs_tol=1e-15, rel_tol=0.0)

    # Independent 600-cell / 2I representation-rank crosschecks already
    # established elsewhere in the repository.
    d_Q = 2
    dim_rho5 = 5
    dim_V6 = 7
    dim_H2 = 9
    dim_H6 = 49
    assert a == Fraction(d_Q, dim_V6)
    assert b == Fraction(d_Q, dim_H2)
    assert c == Fraction(d_Q, dim_rho5)
    assert Fraction(2, 49) == Fraction(d_Q, dim_H6)

    V = ckm_matrix(s12, s23, s13, delta)
    unitary_residual = dagger_product_residual(V)
    det_residual = abs(det3(V) - 1.0)
    assert unitary_residual < 1e-14
    assert det_residual < 1e-14

    c12 = math.sqrt(1.0 - s12 * s12)
    c23 = math.sqrt(1.0 - s23 * s23)
    c13 = math.sqrt(1.0 - s13 * s13)
    J = s12 * s23 * s13 * c12 * c23 * c13 * c13 * math.sin(delta)
    Jq = (V[0][0] * V[1][1] * V[0][1].conjugate() * V[1][0].conjugate()).imag
    assert math.isclose(J, Jq, abs_tol=1e-18, rel_tol=0.0)

    out = {
        "schema": "TIR_CKM_600CELL_FLAG_INCIDENCE_CANDIDATE_V0_1",
        "status": "PASS",
        "epistemic_status": "EXACT_INCIDENCE_GEOMETRY__CKM_FORMULA_RECONSTRUCTION__SELECTOR_BINDING_OPEN",
        "physical_promotion": False,
        "counts": {
            "vertices": len(vertices),
            "edges": len(edge_counts),
            "faces": len(face_counts),
            "tetrahedral_cells": len(cells),
            "cells_per_face": nu_F,
            "cells_per_edge": nu_E,
            "face_edge_pairs_checked": face_edge_pairs,
        },
        "ratios": {
            "a": str(a),
            "b": str(b),
            "c": str(c),
            "h": str(h),
        },
        "edge_star": {
            "shared_cell_count_for_edges_of_same_face": 2,
            "normalized_overlap": str(next(iter(edge_star_overlap_values))),
            "delta_deg": math.degrees(delta),
        },
        "representation_crosscheck": {
            "fundamental_doublet_dim": d_Q,
            "rho5_dim": dim_rho5,
            "V6_dim": dim_V6,
            "H2_dim": dim_H2,
            "H6_dim": dim_H6,
        },
        "ckm_reconstruction": {
            "kappa": KAPPA,
            "s12": s12,
            "s23": s23,
            "s13": s13,
            "delta_deg": math.degrees(delta),
            "J": J,
            "unitarity_residual_max_abs": unitary_residual,
            "determinant_minus_one_abs": det_residual,
        },
        "closed": {
            "uniform_face_incidence_two": True,
            "uniform_edge_incidence_five": True,
            "edge_star_overlap_two_fifths": True,
            "ratio_alphabet_recovered": True,
            "current_ckm_formula_values_reproduced": True,
        },
        "open": {
            "flavour_selector_for_s12": True,
            "flavour_selector_for_s23": True,
            "flavour_selector_for_s13": True,
            "first_order_kappa_correction_operator": True,
            "physical_identification_of_600cell_carrier": True,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
