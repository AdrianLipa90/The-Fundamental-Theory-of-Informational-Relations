from __future__ import annotations

import math


def equal_edge_latitude(n: int) -> float:
    if n < 3:
        raise ValueError("n must be >= 3")
    theta = 2.0 * math.pi / n
    return math.cos(theta) / (1.0 - math.cos(theta))


def classify(n: int, tol: float = 1e-12) -> str:
    c = equal_edge_latitude(n)
    if c < 1.0 - tol:
        return "NONDEGENERATE"
    if abs(c - 1.0) <= tol:
        return "DEGENERATE"
    return "OUTSIDE_UNIT_BLOCH_SPHERE"


def base_radius(c: float) -> float | None:
    if abs(c) > 1.0:
        return None
    return math.sqrt(max(0.0, 1.0 - c * c))


def main() -> None:
    print("N,c_N,r_N,status")
    for n in range(3, 13):
        c = equal_edge_latitude(n)
        r = base_radius(c)
        r_text = "NA" if r is None else f"{r:.12g}"
        print(f"{n},{c:.12g},{r_text},{classify(n)}")

    assert math.isclose(equal_edge_latitude(3), -1.0 / 3.0, abs_tol=1e-12)
    assert math.isclose(equal_edge_latitude(4), 0.0, abs_tol=1e-12)
    assert math.isclose(equal_edge_latitude(5), 1.0 / math.sqrt(5.0), abs_tol=1e-12)
    assert classify(6) == "DEGENERATE"
    assert all(classify(n) == "OUTSIDE_UNIT_BLOCH_SPHERE" for n in range(7, 13))
    print("STAGE_1_EQUAL_EDGE_AUDIT_PASS")


if __name__ == "__main__":
    main()
