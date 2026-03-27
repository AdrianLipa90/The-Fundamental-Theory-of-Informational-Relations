"""Consolidation solver for the active piko-scale fractal foundations spine."""

from __future__ import annotations

import math
from typing import Dict, Any

from src.ciel_foundations.geometry.projective_state import state_from_angles, bloch_vector
from src.ciel_foundations.holonomy.berry import berry_phase_latitude
from src.ciel_foundations.closure.euler import closure_magnitude
from src.ciel_foundations.solvers.tetrahedral_relational_frame_solver import regular_tetrahedron_vertices, relative_phase_triple
from src.ciel_foundations.solvers.nonlocal_holonomic_vortex_solver import poles_from_axis, order_parameter, is_nonlocal_holonomic_vortex


def build_spine_snapshot() -> Dict[str, Any]:
    psi = state_from_angles(math.pi / 2.0, 0.0)
    bloch = bloch_vector(psi)
    berry_phase = berry_phase_latitude(math.pi / 2.0)
    closure = closure_magnitude([0.0, math.pi])

    tetra = regular_tetrahedron_vertices()
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
        "tetra_relative_phases": gamma,
        "local_poles": poles,
        "local_order_parameter": (psi_local.real, psi_local.imag),
        "nonlocal_vortex": vortex,
    }


def spine_consistency_score(snapshot: Dict[str, Any]) -> float:
    score = 0.0
    score += 1.0 if abs(snapshot["closure_magnitude"]) < 1e-12 else 0.0
    score += 1.0 if abs(snapshot["berry_phase"] - math.pi) < 1e-12 else 0.0
    score += 1.0 if snapshot["nonlocal_vortex"] else 0.0
    return score / 3.0
