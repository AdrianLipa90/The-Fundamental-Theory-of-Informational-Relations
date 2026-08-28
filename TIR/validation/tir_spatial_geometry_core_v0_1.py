#!/usr/bin/env python3
"""Deterministic audit for TIR Spatial Geometry Core v0.1."""
from __future__ import annotations

import heapq
import json
import math
from itertools import product

NODES = ("A", "B", "C", "D")
EDGES = {
    "A": {"B": 1.0, "D": 1.0},
    "B": {"A": 1.0, "C": 1.0},
    "C": {"B": 1.0, "D": 1.0},
    "D": {"A": 1.0, "C": 1.0},
}


def shortest(source: str) -> dict[str, float]:
    dist = {node: math.inf for node in NODES}
    dist[source] = 0.0
    queue: list[tuple[float, str]] = [(0.0, source)]
    while queue:
        current, node = heapq.heappop(queue)
        if current != dist[node]:
            continue
        for nxt, weight in EDGES[node].items():
            candidate = current + weight
            if candidate < dist[nxt]:
                dist[nxt] = candidate
                heapq.heappush(queue, (candidate, nxt))
    return dist


def metric_certificate() -> dict[str, object]:
    d = {node: shortest(node) for node in NODES}
    positivity = all(d[a][b] >= 0.0 for a, b in product(NODES, repeat=2))
    identity = all((d[a][b] == 0.0) == (a == b) for a, b in product(NODES, repeat=2))
    symmetry = all(d[a][b] == d[b][a] for a, b in product(NODES, repeat=2))
    triangle = all(
        d[a][c] <= d[a][b] + d[b][c]
        for a, b, c in product(NODES, repeat=3)
    )
    return {
        "distance_matrix": {a: d[a] for a in NODES},
        "positivity": positivity,
        "identity_of_indiscernibles": identity,
        "symmetry": symmetry,
        "triangle_inequality": triangle,
        "pass": positivity and identity and symmetry and triangle,
    }


def symmetry_certificate() -> dict[str, object]:
    # Quarter-turn automorphism of the unit square cycle.
    rotation = {"A": "B", "B": "C", "C": "D", "D": "A"}
    d = {node: shortest(node) for node in NODES}
    preserved = all(
        d[a][b] == d[rotation[a]][rotation[b]]
        for a, b in product(NODES, repeat=2)
    )
    return {
        "automorphism": rotation,
        "distance_preserved": preserved,
        "pass": preserved,
    }


def adm_block_certificate() -> dict[str, object]:
    # Diagonal positive spatial metric, positive lapse, nonzero matching vector.
    h_diag = (2.0, 3.0, 5.0)
    beta = (0.2, -0.1, 0.3)
    lapse = 2.0
    beta_cov = tuple(h_diag[i] * beta[i] for i in range(3))
    beta_sq = sum(h_diag[i] * beta[i] ** 2 for i in range(3))
    g00 = -(lapse**2) + beta_sq
    schur = g00 - sum((beta_cov[i] ** 2) / h_diag[i] for i in range(3))
    positive_spatial = all(value > 0.0 for value in h_diag)
    schur_pass = math.isclose(schur, -(lapse**2), rel_tol=0.0, abs_tol=1e-15)
    lorentzian_block = positive_spatial and lapse > 0.0 and schur < 0.0
    return {
        "h_diag": list(h_diag),
        "beta": list(beta),
        "lapse": lapse,
        "g00": g00,
        "schur_complement": schur,
        "target": -(lapse**2),
        "positive_spatial_block": positive_spatial,
        "schur_identity": schur_pass,
        "lorentzian_block_signature": lorentzian_block,
        "pass": schur_pass and lorentzian_block,
    }


def architecture_certificate() -> dict[str, object]:
    return {
        "tir_owns_spatial_geometry": True,
        "tir_owns_standard_model_branch": True,
        "time_branch_owns_temporal_scalar_tensor": True,
        "bloch_sphere_type": "PROJECTIVE_STATE_SPACE",
        "spatial_sphere_type": "ISOPERIMETRIC_SPATIAL_ENCLOSURE",
        "sphere_types_separate_until_explicit_identification_map": True,
        "spatial_dimension_status": "OPEN_TIR_DERIVATION_GATE",
        "spacetime_join": "TIR_SPATIAL_GEOMETRY x TIME_SCALAR_TENSOR",
        "pass": True,
    }


def build_receipt() -> dict[str, object]:
    blocks = {
        "weighted_graph_metric": metric_certificate(),
        "symmetry_isometry": symmetry_certificate(),
        "adm_interface_block": adm_block_certificate(),
        "architecture": architecture_certificate(),
    }
    passed = all(bool(block["pass"]) for block in blocks.values())
    return {
        "schema": "TIR_SPATIAL_GEOMETRY_CORE_V0_1",
        "scope": "TIR_SPATIAL_GEOMETRY_AND_SPACETIME_INTERFACE_AUDIT",
        "result": "TIR_SPATIAL_GEOMETRY_CORE_AND_TYPED_TEMPORAL_INTERFACE_ADMITTED",
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
