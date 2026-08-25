#!/usr/bin/env python3
from __future__ import annotations
import json, math
import numpy as np

TOL = 1e-12


def element_order_cyclic(a: int, n: int) -> int:
    return 1 if a % n == 0 else n // math.gcd(a, n)


def direct_product_orders(n: int) -> list[int]:
    return [
        math.lcm(element_order_cyclic(a, n), element_order_cyclic(b, 2))
        for a in range(n) for b in range(2)
    ]


def matrix_order(U: np.ndarray, max_steps: int) -> int | None:
    I = np.eye(U.shape[0], dtype=np.complex128)
    for k in range(1, max_steps + 1):
        if float(np.max(np.abs(np.linalg.matrix_power(U, k) - I))) < TOL:
            return k
    return None


def local_spinor_row(N: int) -> dict:
    U = np.diag([
        np.exp(-1j * math.pi / N),
        np.exp(+1j * math.pi / N),
    ]).astype(np.complex128)
    orders = direct_product_orders(N)
    return {
        "N": N,
        "rotation_angle_SO3": 2.0 * math.pi / N,
        "spinor_generator_diagonal": [
            [float(U[0, 0].real), float(U[0, 0].imag)],
            [float(U[1, 1].real), float(U[1, 1].imag)],
        ],
        "U_power_N_minus_identity_error": float(np.max(np.abs(np.linalg.matrix_power(U, N) + np.eye(2)))),
        "U_power_2N_identity_error": float(np.max(np.abs(np.linalg.matrix_power(U, 2 * N) - np.eye(2)))),
        "spinor_lift_order": matrix_order(U, 4 * N),
        "C_N_times_C2_group_order": 2 * N,
        "C_N_times_C2_max_element_order": max(orders),
        "C_N_times_C2_is_cyclic": max(orders) == 2 * N,
    }


def global_row(N: int, name: str, rotation_group: str, binary_group: str) -> dict:
    V = 12 // (6 - N)
    G = N * V
    return {
        "N": N,
        "platonic_closure": name,
        "vertices": V,
        "vertex_stabilizer_order": N,
        "orientation_preserving_rotation_group": rotation_group,
        "rotation_group_order_by_orbit_stabilizer": G,
        "binary_spinor_double_cover": binary_group,
        "binary_group_order": 2 * G,
    }


def main() -> int:
    local = {str(N): local_spinor_row(N) for N in (3, 4, 5)}
    global_groups = {
        "3": global_row(3, "tetrahedron {3,3}", "A4", "2T binary tetrahedral"),
        "4": global_row(4, "octahedron {3,4}", "S4", "2O binary octahedral"),
        "5": global_row(5, "icosahedron {3,5}", "A5", "2I binary icosahedral"),
    }

    checks = {
        "N3_spinor_order_6": local["3"]["spinor_lift_order"] == 6,
        "N4_spinor_order_8": local["4"]["spinor_lift_order"] == 8,
        "N5_spinor_order_10": local["5"]["spinor_lift_order"] == 10,
        "N3_direct_product_matches_cyclic_lift": local["3"]["C_N_times_C2_is_cyclic"],
        "N4_direct_product_fails_to_supply_order_8": (
            not local["4"]["C_N_times_C2_is_cyclic"]
            and local["4"]["C_N_times_C2_max_element_order"] == 4
        ),
        "N5_direct_product_matches_cyclic_lift": local["5"]["C_N_times_C2_is_cyclic"],
        "local_matrix_residuals_below_tolerance": all(
            row["U_power_N_minus_identity_error"] < TOL
            and row["U_power_2N_identity_error"] < TOL
            for row in local.values()
        ),
        "global_rotation_orders_12_24_60": [global_groups[str(N)]["rotation_group_order_by_orbit_stabilizer"] for N in (3,4,5)] == [12,24,60],
        "binary_cover_orders_24_48_120": [global_groups[str(N)]["binary_group_order"] for N in (3,4,5)] == [24,48,120],
    }

    result = {
        "schema": "TIR-POLYGONAL-SPINOR-DOUBLE-COVER/0.1",
        "scope": "pure mathematics: local SU(2) lifts and global binary polyhedral closures",
        "local": local,
        "global": global_groups,
        "checks": checks,
        "key_discriminant": {
            "N4": "C4 x C2 has group order 8 but maximum element order 4, while the SU(2) preimage of the C4 rotation contains a generator of order 8; the local spinor lift is therefore the cyclic C8 preimage rather than the direct product C4 x C2.",
            "N5": "C5 x C2 is cyclic of order 10 and is abstractly isomorphic to the local C10 spinor preimage."
        },
        "verdict": "PASS" if all(checks.values()) else "FAIL"
    }
    print(json.dumps(result, indent=2))
    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
