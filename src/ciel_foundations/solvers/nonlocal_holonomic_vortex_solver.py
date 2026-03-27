"""Minimal solver for local-attractor rotating flow and nonlocal holonomic vortices."""

from __future__ import annotations

import cmath
import math
from typing import Iterable, Sequence, Tuple

Vector3 = Tuple[float, float, float]
Vector4 = Tuple[float, float, float, float]


def normalize_axis(axis: Sequence[float]) -> Vector3:
    if len(axis) != 3:
        raise ValueError("axis must have length 3")
    x, y, z = float(axis[0]), float(axis[1]), float(axis[2])
    n = math.sqrt(x * x + y * y + z * z)
    if n == 0.0:
        raise ValueError("axis must be nonzero")
    return (x / n, y / n, z / n)


def poles_from_axis(axis: Sequence[float]) -> Tuple[Vector3, Vector3]:
    n = normalize_axis(axis)
    return n, (-n[0], -n[1], -n[2])


def point_on_equator(point: Sequence[float], axis: Sequence[float], atol: float = 1e-9) -> bool:
    n = normalize_axis(axis)
    x, y, z = float(point[0]), float(point[1]), float(point[2])
    return abs(x * n[0] + y * n[1] + z * n[2]) <= atol


def order_parameter(rho: float, theta: float) -> complex:
    if rho < 0.0:
        raise ValueError("rho must be nonnegative")
    return math.sqrt(rho) * cmath.exp(1j * theta)


def coriolis_term(omega: Sequence[float], velocity: Sequence[float]) -> Vector3:
    ox, oy, oz = float(omega[0]), float(omega[1]), float(omega[2])
    vx, vy, vz = float(velocity[0]), float(velocity[1]), float(velocity[2])
    cross = (
        oy * vz - oz * vy,
        oz * vx - ox * vz,
        ox * vy - oy * vx,
    )
    return (-2.0 * cross[0], -2.0 * cross[1], -2.0 * cross[2])


def spacetime_circulation(displacements: Sequence[Vector4], u_forms: Sequence[Vector4]) -> float:
    if len(displacements) != len(u_forms):
        raise ValueError("displacements and u_forms must have equal length")
    total = 0.0
    for dx, u in zip(displacements, u_forms):
        total += sum(float(a) * float(b) for a, b in zip(dx, u))
    return total


def is_nonlocal_holonomic_vortex(displacements: Sequence[Vector4], u_forms: Sequence[Vector4], atol: float = 1e-9) -> bool:
    return abs(spacetime_circulation(displacements, u_forms)) > atol
