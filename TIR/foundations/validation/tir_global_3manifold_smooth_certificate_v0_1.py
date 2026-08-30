#!/usr/bin/env python3
"""Closed combinatorial 3-manifold certifier for TIR Gate A5 v0.1."""
from __future__ import annotations

import json
from collections import Counter, defaultdict
from itertools import combinations


def graph_connected(adj, nodes):
    nodes = set(nodes)
    if not nodes:
        return False
    seen = set()
    stack = [next(iter(nodes))]
    while stack:
        x = stack.pop()
        if x in seen:
            continue
        seen.add(x)
        stack.extend(adj.get(x, set()) - seen)
    return seen == nodes


def vertex_link_triangles(tetrahedra, vertex):
    return [tuple(sorted(x for x in tet if x != vertex)) for tet in tetrahedra if vertex in tet]


def certify_sphere_link(triangles):
    triangles = [tuple(sorted(t)) for t in triangles]
    if not triangles or any(len(t) != 3 or len(set(t)) != 3 for t in triangles):
        return False, {"reason": "invalid_link_triangle"}
    if len(set(triangles)) != len(triangles):
        return False, {"reason": "duplicate_link_triangle"}

    vertices = set(x for tri in triangles for x in tri)
    edge_to_tri = defaultdict(list)
    for i, tri in enumerate(triangles):
        for edge in combinations(tri, 2):
            edge_to_tri[tuple(sorted(edge))].append(i)

    bad_edge_incidence = {
        str(edge): len(owners) for edge, owners in edge_to_tri.items() if len(owners) != 2
    }
    if bad_edge_incidence:
        return False, {"reason": "link_edge_incidence", "bad_edges": bad_edge_incidence}

    triangle_adj = {i: set() for i in range(len(triangles))}
    for owners in edge_to_tri.values():
        a, b = owners
        triangle_adj[a].add(b)
        triangle_adj[b].add(a)
    if not graph_connected(triangle_adj, triangle_adj):
        return False, {"reason": "link_disconnected"}

    # A triangulated closed surface must have a single cycle as the link of
    # every one of its vertices. This rejects pseudomanifold singularities.
    for v in vertices:
        cycle_adj = defaultdict(set)
        for tri in triangles:
            if v in tri:
                a, b = [x for x in tri if x != v]
                cycle_adj[a].add(b)
                cycle_adj[b].add(a)
        cycle_vertices = set(cycle_adj)
        if not cycle_vertices:
            return False, {"reason": "empty_vertex_link_in_surface", "vertex": v}
        if any(len(cycle_adj[x]) != 2 for x in cycle_vertices):
            return False, {"reason": "surface_vertex_link_not_cycle", "vertex": v}
        if not graph_connected(cycle_adj, cycle_vertices):
            return False, {"reason": "surface_vertex_link_disconnected", "vertex": v}

    v_count = len(vertices)
    e_count = len(edge_to_tri)
    f_count = len(triangles)
    chi = v_count - e_count + f_count
    if chi != 2:
        return False, {
            "reason": "link_euler_characteristic_not_two",
            "V": v_count,
            "E": e_count,
            "F": f_count,
            "chi": chi,
        }

    return True, {"V": v_count, "E": e_count, "F": f_count, "chi": chi, "surface": "S2"}


def certify_closed_combinatorial_3manifold(tetrahedra):
    tetrahedra = [tuple(sorted(tet)) for tet in tetrahedra]
    if not tetrahedra:
        return False, {"reason": "empty_complex"}
    if any(len(tet) != 4 or len(set(tet)) != 4 for tet in tetrahedra):
        return False, {"reason": "invalid_tetrahedron"}
    if len(set(tetrahedra)) != len(tetrahedra):
        return False, {"reason": "duplicate_tetrahedron"}

    face_to_tets = defaultdict(list)
    for i, tet in enumerate(tetrahedra):
        for face in combinations(tet, 3):
            face_to_tets[tuple(sorted(face))].append(i)

    bad_faces = {
        str(face): len(owners) for face, owners in face_to_tets.items() if len(owners) != 2
    }
    if bad_faces:
        return False, {"reason": "closed_face_incidence", "bad_faces": bad_faces}

    tet_adj = {i: set() for i in range(len(tetrahedra))}
    for owners in face_to_tets.values():
        a, b = owners
        tet_adj[a].add(b)
        tet_adj[b].add(a)
    if not graph_connected(tet_adj, tet_adj):
        return False, {"reason": "tetrahedral_complex_disconnected"}

    vertices = sorted(set(x for tet in tetrahedra for x in tet))
    link_receipts = {}
    for vertex in vertices:
        ok, receipt = certify_sphere_link(vertex_link_triangles(tetrahedra, vertex))
        link_receipts[str(vertex)] = receipt
        if not ok:
            return False, {
                "reason": "vertex_link_not_S2",
                "vertex": vertex,
                "link": receipt,
            }

    return True, {
        "tetrahedra": len(tetrahedra),
        "vertices": len(vertices),
        "triangular_faces": len(face_to_tets),
        "all_vertex_links": "S2",
        "link_receipts": link_receipts,
    }


def boundary_of_4_simplex():
    vertices = range(5)
    return [tuple(x for x in vertices if x != omitted) for omitted in vertices]


def main():
    positive = boundary_of_4_simplex()
    positive_ok, positive_receipt = certify_closed_combinatorial_3manifold(positive)

    open_face = positive[:-1]
    open_ok, open_receipt = certify_closed_combinatorial_3manifold(open_face)

    duplicate = positive + [positive[0]]
    duplicate_ok, duplicate_receipt = certify_closed_combinatorial_3manifold(duplicate)

    shifted = [tuple(x + 10 for x in tet) for tet in positive]
    disconnected = positive + shifted
    disconnected_ok, disconnected_receipt = certify_closed_combinatorial_3manifold(disconnected)

    checks = [
        {
            "name": "boundary_of_4_simplex_certifies_closed_3manifold",
            "pass": positive_ok,
            "receipt": positive_receipt,
        },
        {
            "name": "open_face_control_rejected",
            "pass": not open_ok and open_receipt.get("reason") == "closed_face_incidence",
            "receipt": open_receipt,
        },
        {
            "name": "duplicate_tetrahedron_control_rejected",
            "pass": not duplicate_ok and duplicate_receipt.get("reason") == "duplicate_tetrahedron",
            "receipt": duplicate_receipt,
        },
        {
            "name": "disconnected_control_rejected",
            "pass": not disconnected_ok and disconnected_receipt.get("reason") == "tetrahedral_complex_disconnected",
            "receipt": disconnected_receipt,
        },
        {
            "name": "positive_control_all_five_vertex_links_are_S2",
            "pass": positive_ok
            and len(positive_receipt.get("link_receipts", {})) == 5
            and all(r.get("chi") == 2 for r in positive_receipt.get("link_receipts", {}).values()),
        },
    ]

    passed = all(check["pass"] for check in checks)
    receipt = {
        "schema": "TIR_GLOBAL_3MANIFOLD_SMOOTH_CERTIFICATE_VALIDATION_V0_1",
        "technical_status": "PASS" if passed else "FAIL",
        "verdict": (
            "PASS_TIR_GLOBAL_3MANIFOLD_SMOOTH_CERTIFIER"
            if passed
            else "FAIL_TIR_GLOBAL_3MANIFOLD_SMOOTH_CERTIFIER"
        ),
        "certificate_scope": "finite closed tetrahedral complexes",
        "positive_control": "boundary of 4-simplex (standard S3 triangulation)",
        "actual_tir_global_relational_complex": "OPEN_INPUT",
        "smooth_realization_bridge": "STANDARD_MOISE_THEOREM_AFTER_COMBINATORIAL_3MANIFOLD_PASS",
        "checks": checks,
    }
    print(json.dumps(receipt, indent=2, sort_keys=True))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
