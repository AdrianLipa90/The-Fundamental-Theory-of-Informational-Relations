#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

import tir_ckm_600cell_a2_selector_bridge_candidate_v0_2 as geo

ROOT = Path(__file__).resolve().parents[2]
STAGE35 = ROOT / "TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE35_HERMITIAN_FAMILY_PAIR_V0_1.md"
STAGE36 = ROOT / "TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE36_COMPLEX_HOLONOMY_CP_V0_1.md"
STAGE37 = ROOT / "TIR/frozen_predictions/validation/TIR_POLYGONAL_EXCITATION_STAGE37_COMMON_FAMILY_AXIS_NOGO_V0_1.md"

EXPECTED_A = (
    (Fraction(1), Fraction(2, 5), Fraction(2, 5)),
    (Fraction(2, 5), Fraction(2, 5), Fraction(1, 5)),
    (Fraction(2, 5), Fraction(1, 5), Fraction(2, 5)),
)
EXPECTED_N = (
    (Fraction(1), Fraction(2, 5), Fraction(2, 5)),
    (Fraction(2, 5), Fraction(0), Fraction(0)),
    (Fraction(2, 5), Fraction(0), Fraction(0)),
)
EXPECTED_COMM = (
    (Fraction(0), Fraction(-6, 25), Fraction(-6, 25)),
    (Fraction(6, 25), Fraction(0), Fraction(0)),
    (Fraction(6, 25), Fraction(0), Fraction(0)),
)
EXPECTED_SQUARE_COMM = (
    (Fraction(0), Fraction(-48, 125), Fraction(-48, 125)),
    (Fraction(48, 125), Fraction(0), Fraction(0)),
    (Fraction(48, 125), Fraction(0), Fraction(0)),
)


def ordered_face_edges_about_shared(edge, face):
    u, v = sorted(edge)
    w = next(x for x in face if x not in edge)
    return [
        tuple(sorted((u, v))),
        tuple(sorted((u, w))),
        tuple(sorted((v, w))),
    ]


def relation_matrix(edge_to_cells, shared_edge, face_a, face_b):
    ea = ordered_face_edges_about_shared(shared_edge, face_a)
    eb = ordered_face_edges_about_shared(shared_edge, face_b)
    return tuple(
        tuple(geo.edge_star_overlap(edge_to_cells, x, y) for y in eb)
        for x in ea
    )


def mm(A, B):
    return tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(3)) for j in range(3))
        for i in range(3)
    )


def sub(A, B):
    return tuple(tuple(A[i][j] - B[i][j] for j in range(3)) for i in range(3))


def transpose(A):
    return tuple(tuple(A[j][i] for j in range(3)) for i in range(3))


def main() -> int:
    vertices = geo.vertices600()
    adj = geo.adjacency600(vertices)
    cells = geo.tetrahedral_cells(adj)
    edge_to_cells, face_to_cells, edge_to_faces = geo.incidence(cells)

    patterns = {
        "co_tetrahedral": Counter(),
        "nonadjacent": Counter(),
    }

    for edge, faces in edge_to_faces.items():
        assert len(faces) == 5
        for fa, fb in itertools.combinations(faces, 2):
            co_tetra = bool(face_to_cells[fa] & face_to_cells[fb])
            label = "co_tetrahedral" if co_tetra else "nonadjacent"
            patterns[label][relation_matrix(edge_to_cells, edge, fa, fb)] += 1

    assert patterns["co_tetrahedral"] == Counter({EXPECTED_A: 3600})
    assert patterns["nonadjacent"] == Counter({EXPECTED_N: 3600})

    assert transpose(EXPECTED_A) == EXPECTED_A
    assert transpose(EXPECTED_N) == EXPECTED_N

    comm = sub(mm(EXPECTED_A, EXPECTED_N), mm(EXPECTED_N, EXPECTED_A))
    assert comm == EXPECTED_COMM
    assert any(x != 0 for row in comm for x in row)

    H_A = mm(EXPECTED_A, EXPECTED_A)
    H_N = mm(EXPECTED_N, EXPECTED_N)
    assert transpose(H_A) == H_A
    assert transpose(H_N) == H_N

    # H=M^T M=M^2 for symmetric M, hence positive-semidefinite exactly.
    assert H_A == mm(transpose(EXPECTED_A), EXPECTED_A)
    assert H_N == mm(transpose(EXPECTED_N), EXPECTED_N)

    square_comm = sub(mm(H_A, H_N), mm(H_N, H_A))
    assert square_comm == EXPECTED_SQUARE_COMM
    max_abs_square_comm = max(abs(x) for row in square_comm for x in row)
    assert max_abs_square_comm == Fraction(48, 125)

    stage35 = STAGE35.read_text(encoding="utf-8")
    stage36 = STAGE36.read_text(encoding="utf-8")
    stage37 = STAGE37.read_text(encoding="utf-8")
    provenance = {
        "stage35_real_noncommuting_mechanism_precedent_present": "STAGE_35_HERMITIAN_FAMILY_PAIR_PASS_WITH_INPUT_PROVENANCE_AND_CP_BOUNDARY" in stage35,
        "stage35_heavy_source_quarantine_present": "old_doc_bridge_ansatz_quarantined" in stage35,
        "stage36_complex_mechanism_quarantine_present": "STAGE_36_COMPLEX_HOLONOMY_CP_MECHANISM_PASS__SOURCE_PROMOTION_QUARANTINED" in stage36,
        "stage37_no_go_present": "STAGE_37_COMMON_FAMILY_AXIS_NOGO_PASS" in stage37,
        "stage37_requires_second_operator": "A non-trivial family transformation requires at least one additional operator" in stage37,
    }
    assert all(provenance.values())

    checks = {
        "all_3600_co_tetrahedral_pairs_share_one_exact_matrix": patterns["co_tetrahedral"] == Counter({EXPECTED_A: 3600}),
        "all_3600_nonadjacent_pairs_share_one_exact_matrix": patterns["nonadjacent"] == Counter({EXPECTED_N: 3600}),
        "both_relation_operators_real_symmetric": transpose(EXPECTED_A) == EXPECTED_A and transpose(EXPECTED_N) == EXPECTED_N,
        "relation_operators_do_not_commute": comm == EXPECTED_COMM,
        "PSD_square_pair_is_exact_MtM": H_A == mm(transpose(EXPECTED_A), EXPECTED_A) and H_N == mm(transpose(EXPECTED_N), EXPECTED_N),
        "PSD_square_pair_does_not_commute": square_comm == EXPECTED_SQUARE_COMM,
        "PSD_square_commutator_max_entry_is_48_over_125": max_abs_square_comm == Fraction(48, 125),
        **provenance,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": "TIR_CKM_600CELL_CLEAN_NONCOMMUTING_FAMILY_PAIR_CANDIDATE_V0_4",
        "status": status,
        "epistemic_status": "EXACT_REAL_NONCOMMUTING_PAIR__STAGE37_MECHANISM_REPAIR__COMPLEX_CP_OPERATOR_OPEN",
        "physical_promotion": False,
        "uses_observed_ckm": False,
        "uses_observed_masses": False,
        "uses_quarantined_heavy_family_rows": False,
        "counts": {
            "co_tetrahedral_pairs": 3600,
            "nonadjacent_pairs": 3600,
        },
        "operators": {
            "M_A": [[str(x) for x in row] for row in EXPECTED_A],
            "M_N": [[str(x) for x in row] for row in EXPECTED_N],
            "commutator": [[str(x) for x in row] for row in comm],
            "PSD_square_commutator": [[str(x) for x in row] for row in square_comm],
            "PSD_square_commutator_max_abs": str(max_abs_square_comm),
        },
        "checks": checks,
        "closed": {
            "clean_second_family_operator_mechanism": True,
            "stage37_commuting_axis_obstruction_avoided": True,
        },
        "open": {
            "unique_up_down_physical_binding": True,
            "degeneracy_splitting": True,
            "clean_complex_holonomy_lift": True,
            "nonzero_jarlskog_from_clean_pair": True,
            "additive_a_kappa_refinement": True,
        },
    }
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
