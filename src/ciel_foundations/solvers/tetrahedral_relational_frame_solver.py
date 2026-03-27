"""System-style solver for the tetrahedral relational frame on S^2."""

from __future__ import annotations

import cmath
import math
from typing import List, Sequence, Tuple

Vector3 = Tuple[float, float, float]


def regular_tetrahedron_vertices() -> List[Vector3]:
    base = [
        (1.0, 1.0, 1.0),
        (1.0, -1.0, -1.0),
        (-1.0, 1.0, -1.0),
        (-1.0, -1.0, 1.0),
    ]
    scale = 1.0 / math.sqrt(3.0)
    return [(scale * x, scale * y, scale * z) for x, y, z in base]


def dot(u: Vector3, v: Vector3) -> float:
    return u[0] * v[0] + u[1] * v[1] + u[2] * v[2]


def pairwise_dot_matrix(vertices: Sequence[Vector3] | None = None) -> List[List[float]]:
    verts = list(vertices) if vertices is not None else regular_tetrahedron_vertices()
    return [[dot(u, v) for v in verts] for u in verts]


def relative_phase_triple(phases: Sequence[float]) -> Tuple[float, float, float]:
    if len(phases) != 4:
        raise ValueError("expected four phases for tetrahedral vertices")
    phi0 = phases[0]
    return (phases[1] - phi0, phases[2] - phi0, phases[3] - phi0)


def closure_defect_from_relative_triple(phases: Sequence[float]) -> complex:
    g1, g2, g3 = relative_phase_triple(phases)
    return cmath.exp(1j * g1) + cmath.exp(1j * g2) + cmath.exp(1j * g3)
