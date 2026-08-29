#!/usr/bin/env python3
from __future__ import annotations

import itertools
import math

ROLES = {
    "h": "projective_half_spin_identity",
    "a": "generation_seed_release",
    "b": "collatz_return_axis",
    "c": "poincare_berry_curvature_holonomy",
}

PARENT_SIGNATURES = {
    "h": frozenset({"HALF", "SPIN_HALF", "CP1"}),
    "a": frozenset({"TWIN_PRIME", "RAMANUJAN", "GENERATION"}),
    "b": frozenset({"COLLATZ_TERMINAL", "RETURN_DIRECTION"}),
    "c": frozenset({"TETRAHEDRAL_DEPTH", "POINCARE_DISK", "BERRY_CONNECTION"}),
}

RUNTIME_EPS = 1e-15


def exact_sign(x: float) -> int:
    return 1 if x > 0.0 else -1 if x < 0.0 else 0


def runtime_sign3(x: float, eps: float = RUNTIME_EPS) -> int:
    return 1 if x > eps else -1 if x < -eps else 0


def exact_spin_sign(dv: float, alpha: float) -> int:
    assert math.isfinite(dv)
    assert math.isfinite(alpha) and alpha > 0.0
    return exact_sign(math.tanh(-alpha * dv))


def runtime_gradient_orientation(dv: float) -> int:
    assert math.isfinite(dv)
    return runtime_sign3(-dv)


def consensus(*values: int) -> int | None:
    active = [v for v in values if v != 0]
    if not active:
        return 0
    if len(set(active)) == 1:
        return active[0]
    return None


def validate_role_bijection() -> None:
    assert set(ROLES) == {"h", "a", "b", "c"}
    assert len(set(ROLES.values())) == 4
    assert len(set(PARENT_SIGNATURES.values())) == 4

    slots = tuple(ROLES)
    preserving = []
    for perm in itertools.permutations(slots):
        mapping = dict(zip(slots, perm))
        if all(PARENT_SIGNATURES[s] == PARENT_SIGNATURES[mapping[s]] for s in slots):
            preserving.append(mapping)
    assert len(preserving) == 1
    assert all(preserving[0][s] == s for s in slots)


def validate_exact_gradient_scale_independence() -> None:
    values = (-100.0, -3.5, -1e-6, -1e-18, 0.0, 1e-18, 1e-6, 2.0, 100.0)
    alphas = (1e-9, 1e-3, 0.1, 1.0, 10.0, 1e3)
    for dv in values:
        expected = exact_sign(-dv)
        for alpha in alphas:
            got = exact_spin_sign(dv, alpha)
            assert got == expected, (dv, alpha, got, expected)


def validate_runtime_deadband() -> None:
    assert runtime_gradient_orientation(2.0 * RUNTIME_EPS) == -1
    assert runtime_gradient_orientation(-2.0 * RUNTIME_EPS) == 1
    assert runtime_gradient_orientation(RUNTIME_EPS) == 0
    assert runtime_gradient_orientation(-RUNTIME_EPS) == 0
    assert runtime_gradient_orientation(0.0) == 0


def validate_consensus_uniqueness() -> None:
    assert consensus(1, 1, 1) == 1
    assert consensus(-1, -1, -1) == -1
    assert consensus(1, 0, 1) == 1
    assert consensus(-1, 0, -1) == -1
    assert consensus(0, 0, 0) == 0
    assert consensus(1, -1, 0) is None
    assert consensus(-1, 1, 1) is None


def main() -> None:
    validate_role_bijection()
    validate_exact_gradient_scale_independence()
    validate_runtime_deadband()
    validate_consensus_uniqueness()

    print("schema=TIR_COEFFICIENT_ROLE_ORIENTATION_FORCING_V0_1")
    print("status=PASS")
    print("slot_role_bijection=true")
    print("role_preserving_permutations=1")
    print("identity_is_only_role_preserving_permutation=true")
    print("exact_gradient_sign_scale_independent=true")
    print(f"runtime_neutral_deadband_eps={RUNTIME_EPS:.1e}")
    print("runtime_deadband_validated=true")
    print("consensus_orientation_unique=true")
    print("coefficient_slot_permutation_search_eliminated=true")
    print("next_gate=TYPED_INTEGER_MAGNITUDE_EXTRACTION")


if __name__ == "__main__":
    main()
