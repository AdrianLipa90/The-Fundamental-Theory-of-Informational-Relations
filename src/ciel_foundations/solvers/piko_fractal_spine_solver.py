"""Consolidation solver for the active piko-scale fractal foundations spine."""

from __future__ import annotations

import math
from typing import Dict, Any

from src.ciel_foundations.geometry.projective_state import state_from_angles, bloch_vector
from src.ciel_foundations.holonomy.berry import berry_phase_latitude
from src.ciel_foundations.closure.euler import closure_magnitude
from src.ciel_foundations.solvers.tetrahedral_relational_frame_solver import regular_tetrahedron_vertices, relative_phase_triple, pairwise_dot_matrix
from src.ciel_foundations.solvers.nonlocal_holonomic_vortex_solver import poles_from_axis, order_parameter, is_nonlocal_holonomic_vortex


def _tetrahedron_consistency(dot_matrix: list[list[float]], atol: float = 1e-12) -> bool:
    for i in range(4):
        for j in range(4):
            expected = 1.0 if i == j else -1.0 / 3.0
            if abs(dot_matrix[i][j] - expected) > atol:
                return False
    return True


def build_spine_snapshot() -> Dict[str, Any]:
    psi = state_from_angles(math.pi / 2.0, 0.0)
    bloch = bloch_vector(psi)
    berry_phase = berry_phase_latitude(math.pi / 2.0)
    closure = closure_magnitude([0.0, math.pi])

    tetra = regular_tetrahedron_vertices()
    tetra_dots = pairwise_dot_matrix(tetra)
    gamma = relative_phase_triple([0.0, 0.4, 1.2, -0.7])

    poles = poles_from_axis((0.0, 0.0, 1.0))
    psi_local = order_parameter(4.0, math.pi / 2.0)
    displacements = [
        (0.0, 1.0, 0.0, 0.0),
        (1.0, 0.0, 0.0, 0.0),
        (0.0, -1.0, 0.0, 0.0),
        (-1.0, 0.0, 0.0, 0.0),
    ]
    u_forms = [
        (0.0, 1.0, 0.0, 0.0),
        (1.0, 0.0, 0.0, 0.0),
        (0.0, -1.0, 0.0, 0.0),
        (-1.0, 0.0, 0.0, 0.0),
    ]
    vortex = is_nonlocal_holonomic_vortex(displacements, u_forms)

    return {
        "cp1_bloch": bloch,
        "berry_phase": berry_phase,
        "closure_magnitude": closure,
        "tetrahedron_vertices": tetra,
        "tetrahedron_dot_matrix": tetra_dots,
        "tetra_relative_phases": gamma,
        "local_poles": poles,
        "local_order_parameter": (psi_local.real, psi_local.imag),
        "nonlocal_vortex": vortex,
    }


def spine_consistency_score(snapshot: Dict[str, Any]) -> float:
    checks = []
    checks.append(abs(snapshot["closure_magnitude"]) < 1e-12)
    checks.append(abs(snapshot["berry_phase"] - math.pi) < 1e-12)
    checks.append(_tetrahedron_consistency(snapshot["tetrahedron_dot_matrix"]))
    checks.append(abs(snapshot["local_order_parameter"][0]) < 1e-12 and abs(snapshot["local_order_parameter"][1] - 2.0) < 1e-12)
    checks.append(bool(snapshot["nonlocal_vortex"]))
    return sum(1.0 for c in checks if c) / float(len(checks))
