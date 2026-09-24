from __future__ import annotations
import cmath
import math

TAU = 2.0 * math.pi


def so_generators(n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    return n * (n - 1) // 2


def half_generator_iterate(x: float, n: int) -> float:
    if n < 0:
        raise ValueError("n must be non-negative")
    return (2.0 ** n) * x + ((2.0 ** n) - 1.0)


def moire_reconstruct(phi1: float, phi2: float, amplitude: float = 1.0) -> tuple[complex, complex]:
    direct = amplitude * cmath.exp(1j * phi1) + amplitude * cmath.exp(1j * phi2)
    mean = 0.5 * (phi1 + phi2)
    delta = phi1 - phi2
    factored = 2.0 * amplitude * cmath.exp(1j * mean) * math.cos(0.5 * delta)
    return direct, factored


def antiphase_null(phi: float) -> float:
    z = cmath.exp(1j * phi) + cmath.exp(1j * (phi + math.pi))
    return abs(z)


def exact_displacement_defect_2d(du_x_dy: float, du_y_dx: float) -> float:
    """Exterior-derivative proxy d(du). Exact smooth displacement requires equality."""
    return du_y_dx - du_x_dy


def validate() -> dict:
    checks: dict[str, bool] = {}
    checks["so6_generators_15"] = so_generators(6) == 15
    checks["so6xso6_generators_30"] = 2 * so_generators(6) == 30
    checks["so36_generators_630"] = so_generators(36) == 630

    for pair in [(0.1, 0.7), (-1.2, 2.3), (math.pi / 2, -math.pi / 3)]:
        direct, factored = moire_reconstruct(*pair)
        checks[f"moire_identity_{pair}"] = abs(direct - factored) < 1e-12

    checks["antiphase_is_null"] = antiphase_null(0.371) < 1e-12
    checks["half_plus_to_two"] = abs(half_generator_iterate(0.5, 1) - 2.0) < 1e-12
    checks["half_minus_to_zero"] = abs(half_generator_iterate(-0.5, 1)) < 1e-12
    checks["plus_branch_n5"] = abs(half_generator_iterate(0.5, 5) - 47.0) < 1e-12
    checks["minus_branch_n6"] = abs(half_generator_iterate(-0.5, 6) - 31.0) < 1e-12
    checks["exact_displacement_zero_defect"] = abs(exact_displacement_defect_2d(0.25, 0.25)) < 1e-12
    checks["nonintegrable_candidate_nonzero"] = abs(exact_displacement_defect_2d(0.25, -0.5)) > 1e-12

    return {"status": "PASS" if all(checks.values()) else "FAIL", "checks": checks}


if __name__ == "__main__":
    import json
    print(json.dumps(validate(), indent=2, sort_keys=True))
