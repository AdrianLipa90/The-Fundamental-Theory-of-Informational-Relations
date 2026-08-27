from __future__ import annotations

import cmath
import math

TOL = 1e-12


def c_equal_edge(n: int) -> float:
    theta = 2.0 * math.pi / n
    q = math.cos(theta)
    return q / (1.0 - q)


def r_equal_edge(n: int) -> float:
    c = c_equal_edge(n)
    value = max(0.0, 1.0 - c * c)
    return math.sqrt(value)


def lifted_step(z: complex, sheet: int) -> tuple[complex, int]:
    omega = cmath.exp(2j * math.pi / 3.0)
    return omega * z, -sheet


def iterate(z: complex, sheet: int, steps: int) -> tuple[complex, int]:
    for _ in range(steps):
        z, sheet = lifted_step(z, sheet)
    return z, sheet


def close(a: complex, b: complex, tol: float = TOL) -> bool:
    return abs(a - b) <= tol


def main() -> None:
    z0 = 0.37 + 0.19j
    s0 = 1

    z3, s3 = iterate(z0, s0, 3)
    z6, s6 = iterate(z0, s0, 6)

    assert close(z3, z0), (z3, z0)
    assert s3 == -s0, (s3, s0)
    assert close(z6, z0), (z6, z0)
    assert s6 == s0, (s6, s0)

    c6 = c_equal_edge(6)
    r6 = r_equal_edge(6)
    assert abs(c6 - 1.0) <= TOL, c6
    assert abs(r6) <= TOL, r6

    print("STAGE_7_GEOMETRIC_SEPARATION_PASS")
    print(f"projected_period_3={close(z3, z0)}")
    print(f"sheet_flips_after_3={s3 == -s0}")
    print(f"lifted_period_6={close(z6, z0) and s6 == s0}")
    print(f"equal_edge_c6={c6:.12f}")
    print(f"equal_edge_r6={r6:.12f}")
    print("direct_identification=six_lifted_states != six_polygon_vertices")


if __name__ == "__main__":
    main()
