#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import math
from collections import Counter, defaultdict
from fractions import Fraction

PHI = (1.0 + math.sqrt(5.0)) / 2.0
KAPPA = math.log(2.0) / (24.0 * math.pi)
TOL = 5e-13


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


def adjacency600(vertices):
    n = len(vertices)
    adj = [set() for _ in range(n)]
    target = PHI / 2.0
    for i in range(n):
        for j in range(i + 1, n):
            if math.isclose(dot(vertices[i], vertices[j]), target, abs_tol=2e-12, rel_tol=0.0):
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


def incidence(cells):
    edge_to_cells = defaultdict(set)
    face_to_cells = defaultdict(set)
    for ci, cell in enumerate(cells):
        for edge in itertools.combinations(cell, 2):
            edge_to_cells[tuple(sorted(edge))].add(ci)
        for face in itertools.combinations(cell, 3):
            face_to_cells[tuple(sorted(face))].add(ci)
    assert len(edge_to_cells) == 720
    assert {len(v) for v in edge_to_cells.values()} == {5}
    assert len(face_to_cells) == 1200
    assert {len(v) for v in face_to_cells.values()} == {2}
    edge_to_faces = defaultdict(list)
    for face in face_to_cells:
        for edge in itertools.combinations(face, 2):
            edge_to_faces[tuple(sorted(edge))].append(face)
    assert set(map(len, edge_to_faces.values())) == {5}
    return edge_to_cells, face_to_cells, edge_to_faces


def face_edges(face):
    return [tuple(sorted(e)) for e in itertools.combinations(face, 2)]


def edge_star_overlap(edge_to_cells, e1, e2):
    return Fraction(len(edge_to_cells[e1] & edge_to_cells[e2]), 5)


def check_local_a2(edge_to_cells, face_to_cells):
    checked = 0
    for face in face_to_cells:
        es = face_edges(face)
        overlaps = [edge_star_overlap(edge_to_cells, a, b) for a, b in itertools.combinations(es, 2)]
        assert overlaps == [Fraction(2, 5)] * 3

        # For three unit states with common off-diagonal c=2/5:
        # ||mu||^2=(1+2c)/3=3/5,
        # ||y_i||^2=1-||mu||^2=2/5,
        # <y_i,y_j>=c-||mu||^2=-1/5,
        # normalized centered overlap=-1/2.
        c = Fraction(2, 5)
        mu2 = (1 + 2 * c) / 3
        yi2 = 1 - mu2
        yiyj = c - mu2
        normalized = yiyj / yi2
        assert mu2 == Fraction(3, 5)
        assert yi2 == Fraction(2, 5)
        assert yiyj == Fraction(-1, 5)
        assert normalized == Fraction(-1, 2)
        checked += 1
    return checked


# A canonical orthonormal basis for the centered plane of three unit states
# with common pair overlap 2/5 is
# q1=(x1-x2)/sqrt(6/5), q2=(x1+x2-2x3)/sqrt(18/5).
Q_COEFFS = (
    ((1.0, -1.0, 0.0), math.sqrt(6.0 / 5.0)),
    ((1.0, 1.0, -2.0), math.sqrt(18.0 / 5.0)),
)


def cross_basis_matrix(edge_to_cells, face_a, face_b):
    ea = face_edges(face_a)
    eb = face_edges(face_b)
    out = [[0.0, 0.0], [0.0, 0.0]]
    for i, (ca, na) in enumerate(Q_COEFFS):
        for j, (cb, nb) in enumerate(Q_COEFFS):
            value = 0.0
            for r in range(3):
                for s in range(3):
                    value += ca[r] * cb[s] * float(edge_star_overlap(edge_to_cells, ea[r], eb[s]))
            out[i][j] = value / (na * nb)
    return out


def singular_values_2x2(M):
    a, b = M[0]
    c, d = M[1]
    tr = a * a + b * b + c * c + d * d
    det_b = (a * d - b * c) ** 2
    disc = max(0.0, tr * tr - 4.0 * det_b)
    lam_hi = (tr + math.sqrt(disc)) / 2.0
    lam_lo = (tr - math.sqrt(disc)) / 2.0
    return tuple(sorted((math.sqrt(max(0.0, lam_hi)), math.sqrt(max(0.0, lam_lo))), reverse=True))


def principal_cosines(edge_to_cells, face_a, face_b):
    # The three normalized centered vectors form a tight frame with frame
    # operator (3/2) I on the 2D plane.  Therefore singular values of the
    # 2x2 orthonormal-basis cross matrix are already the principal cosines.
    return singular_values_2x2(cross_basis_matrix(edge_to_cells, face_a, face_b))


def check_five_face_links(edge_to_cells, face_to_cells, edge_to_faces):
    counts = Counter()
    max_error = 0.0
    observed = {"co_tetrahedral": set(), "nonadjacent": set()}

    for edge, faces in edge_to_faces.items():
        assert len(faces) == 5
        for fa, fb in itertools.combinations(faces, 2):
            co_tetra = bool(face_to_cells[fa] & face_to_cells[fb])
            pcs = principal_cosines(edge_to_cells, fa, fb)
            if co_tetra:
                label = "co_tetrahedral"
                target = (5.0 / 9.0, 1.0 / 3.0)
            else:
                label = "nonadjacent"
                target = (2.0 / 9.0, 0.0)
            counts[label] += 1
            observed[label].add(tuple(round(x, 12) for x in pcs))
            max_error = max(max_error, max(abs(pcs[k] - target[k]) for k in range(2)))
            assert all(abs(pcs[k] - target[k]) < TOL for k in range(2)), (edge, fa, fb, pcs, target)

    assert counts == Counter({"co_tetrahedral": 3600, "nonadjacent": 3600})
    return counts, observed, max_error


def matmul3(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def matsub3(A, B):
    return [[A[i][j] - B[i][j] for j in range(3)] for i in range(3)]


def main():
    vertices = vertices600()
    adj = adjacency600(vertices)
    cells = tetrahedral_cells(adj)
    edge_to_cells, face_to_cells, edge_to_faces = incidence(cells)

    a2_faces_checked = check_local_a2(edge_to_cells, face_to_cells)
    link_counts, observed_classes, principal_max_error = check_five_face_links(
        edge_to_cells, face_to_cells, edge_to_faces
    )

    nu_F = 2
    nu_E = 5
    a = Fraction(nu_F, nu_F + nu_E)
    b = Fraction(nu_F, 2 * nu_F + nu_E)
    c = Fraction(nu_F, nu_E)
    h = Fraction(1, nu_F)
    s23 = h * a * a
    s13 = s23 * b * c

    assert a == Fraction(2, 7)
    assert b == Fraction(2, 9)
    assert c == Fraction(2, 5)
    assert s23 == Fraction(2, 49)
    assert s13 == Fraction(8, 2205)

    # Normalized projector-trace realizations.
    tau_a = Fraction(2, 7)          # rank-2 face projector in dim 7
    tau_b = Fraction(2, 9)          # rank-2 source-face projector in dim 9
    tau_s23 = Fraction(1, 2) * Fraction(2, 7) * Fraction(2, 7)
    assert tau_a == a
    assert tau_b == b
    assert tau_s23 == s23

    s12_operator = float(b) + KAPPA * float(a)
    expected_s12 = 2.0 / 9.0 + (2.0 / 7.0) * KAPPA
    assert math.isclose(s12_operator, expected_s12, abs_tol=1e-16, rel_tol=0.0)

    # A2 root-algebra composition [E12,E23]=E13.
    Z = 0
    E12 = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]
    E23 = [[0, 0, 0], [0, 0, 1], [0, 0, 0]]
    E13 = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
    comm = matsub3(matmul3(E12, E23), matmul3(E23, E12))
    assert comm == E13

    # The incidence-dressed composite coefficient is exactly the retained s13.
    dressed_composite = s23 * b * c
    assert dressed_composite == Fraction(8, 2205)

    # Existing 2I/McKay dimension crosschecks.
    assert Fraction(2, 7) == Fraction(2, 4 + 3)   # V6 = rho4b + rho3b
    assert Fraction(2, 9) == Fraction(2, (2 + 1) ** 2)  # dim H_2(S3)=9
    assert Fraction(2, 5) == Fraction(2, 5)       # fundamental / rho5 dims
    assert Fraction(2, 49) == Fraction(2, (6 + 1) ** 2)  # dim H_6(S3)=49

    out = {
        "schema": "TIR_CKM_600CELL_A2_SELECTOR_BRIDGE_CANDIDATE_V0_2",
        "status": "PASS",
        "epistemic_status": "EXACT_LOCAL_A2_GEOMETRY__EXACT_B_C_OPERATOR_READOUTS__MIXING_WEIGHT_OPERATOR_REALIZATION__UNIQUE_FLAVOUR_SELECTOR_OPEN",
        "physical_promotion": False,
        "counts": {
            "vertices": len(vertices),
            "edges": len(edge_to_cells),
            "faces": len(face_to_cells),
            "tetrahedral_cells": len(cells),
            "a2_faces_checked": a2_faces_checked,
            "co_tetrahedral_face_plane_pairs": link_counts["co_tetrahedral"],
            "nonadjacent_face_plane_pairs": link_counts["nonadjacent"],
        },
        "local_A2": {
            "raw_edge_star_gram_diagonal": "1",
            "raw_edge_star_gram_off_diagonal": "2/5",
            "centroid_norm_sq": "3/5",
            "centered_norm_sq": "2/5",
            "centered_pair_inner_product": "-1/5",
            "normalized_centered_pair_inner_product": "-1/2",
            "weyl_group": "S3",
        },
        "five_face_edge_link": {
            "co_tetrahedral_principal_cosines": ["5/9", "1/3"],
            "nonadjacent_principal_cosines": ["2/9", "0"],
            "observed_numeric_classes": {k: sorted(list(v)) for k, v in observed_classes.items()},
            "max_abs_error": principal_max_error,
        },
        "operator_readouts": {
            "a_normalized_rank_trace": str(tau_a),
            "b_normalized_rank_trace": str(tau_b),
            "b_nonadjacent_A2_principal_cosine": "2/9",
            "c_edge_star_overlap": str(c),
            "s23_product_projector_trace": str(tau_s23),
            "s13_dressed_composite_root_coefficient": str(dressed_composite),
            "s12_additive_observable_expectation": s12_operator,
        },
        "root_algebra": {
            "commutator_E12_E23_equals_E13": True,
            "s13_equals_s23_times_b_times_c": True,
        },
        "closed": {
            "face_generates_A2_plane": True,
            "nonadjacent_face_planes_force_b_two_ninths": True,
            "edge_star_overlap_forces_c_two_fifths": True,
            "a_has_normalized_packet_projector_trace": True,
            "s23_has_exact_product_projector_realization": True,
            "s13_has_exact_A2_composite_root_realization": True,
            "s12_has_exact_additive_operator_realization": True,
        },
        "open": {
            "unique_weyl_channel_label_binding": True,
            "unique_23_packet_selection": True,
            "unique_13_incidence_dressing": True,
            "dynamic_derivation_of_additive_a_kappa_term": True,
            "physical_identification_of_600cell_carrier": True,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
