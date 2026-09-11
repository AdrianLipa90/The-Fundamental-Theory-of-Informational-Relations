from __future__ import annotations

from collections import Counter
import json
from typing import Mapping

SCHEMA = "TIR_600CELL_MCKAY_E8_CLOSURE_CANDIDATE_V0_3"
PROMOTION_STATE = "CANDIDATE_ONLY"
PHYSICAL_BINDING = "OPEN"
EPISTEMIC = "EXACT_REPRESENTATION_THEORY__PHYSICAL_BINDING_OPEN"

# Stable local identifiers are deliberate: prime notation for the two 2D, 3D,
# and 4D irreducibles is convention-dependent across references.
IRREP_DIMS: dict[str, int] = {
    "rho1": 1,
    "rho2a": 2,
    "rho3a": 3,
    "rho4a": 4,
    "rho5": 5,
    "rho6": 6,
    "rho4b": 4,
    "rho3b": 3,
    "rho2b": 2,
}

# Affine E8 McKay graph for tensoring by the fundamental binary-icosahedral
# doublet Q=rho2a.
MCKAY_ADJACENCY: dict[str, tuple[str, ...]] = {
    "rho1": ("rho2a",),
    "rho2a": ("rho1", "rho3a"),
    "rho3a": ("rho2a", "rho4a"),
    "rho4a": ("rho3a", "rho5"),
    "rho5": ("rho4a", "rho6"),
    "rho6": ("rho5", "rho4b", "rho3b"),
    "rho4b": ("rho6", "rho2b"),
    "rho3b": ("rho6",),
    "rho2b": ("rho4b",),
}

EXPECTED: dict[int, Counter[str]] = {
    0: Counter({"rho1": 1}),
    1: Counter({"rho2a": 1}),
    2: Counter({"rho3a": 1}),
    3: Counter({"rho4a": 1}),
    4: Counter({"rho5": 1}),
    5: Counter({"rho6": 1}),
    6: Counter({"rho4b": 1, "rho3b": 1}),
    7: Counter({"rho6": 1, "rho2b": 1}),
}

EXPECTED_COEFFICIENT_RANKS = (1, 4, 9, 16, 25, 36, 25, 40)
EXPECTED_CUMULATIVE_RANKS = (1, 5, 14, 30, 55, 91, 116, 120)


class McKayClosureError(RuntimeError):
    pass


def _clean(counter: Mapping[str, int]) -> Counter[str]:
    out: Counter[str] = Counter()
    for irrep, multiplicity in counter.items():
        if irrep not in IRREP_DIMS:
            raise McKayClosureError(f"unknown irrep: {irrep}")
        if isinstance(multiplicity, bool) or not isinstance(multiplicity, int) or multiplicity < 0:
            raise McKayClosureError(f"invalid multiplicity for {irrep}: {multiplicity!r}")
        if multiplicity:
            out[irrep] = multiplicity
    return out


def validate_graph() -> None:
    if set(MCKAY_ADJACENCY) != set(IRREP_DIMS):
        raise McKayClosureError("McKay graph and irrep dimension table disagree")
    for irrep, neighbours in MCKAY_ADJACENCY.items():
        if len(set(neighbours)) != len(neighbours):
            raise McKayClosureError(f"duplicate McKay edge at {irrep}")
        for neighbour in neighbours:
            if irrep not in MCKAY_ADJACENCY.get(neighbour, ()):
                raise McKayClosureError(f"asymmetric McKay edge: {irrep} -- {neighbour}")
        lhs = 2 * IRREP_DIMS[irrep]
        rhs = sum(IRREP_DIMS[neighbour] for neighbour in neighbours)
        if lhs != rhs:
            raise McKayClosureError(
                f"dimension balance fails at {irrep}: 2*{IRREP_DIMS[irrep]} != {rhs}"
            )


def tensor_by_fundamental(decomposition: Mapping[str, int]) -> Counter[str]:
    src = _clean(decomposition)
    out: Counter[str] = Counter()
    for irrep, multiplicity in src.items():
        for neighbour in MCKAY_ADJACENCY[irrep]:
            out[neighbour] += multiplicity
    return out


def subtract_fail_closed(left: Mapping[str, int], right: Mapping[str, int]) -> Counter[str]:
    """Exact representation-ring subtraction that never discards negatives.

    collections.Counter subtraction is intentionally not used because it drops
    zero/negative entries and could hide an invalid branching recurrence.
    """
    a = _clean(left)
    b = _clean(right)
    keys = set(a) | set(b)
    raw = {key: a.get(key, 0) - b.get(key, 0) for key in keys}
    negative = {key: value for key, value in raw.items() if value < 0}
    if negative:
        raise McKayClosureError(f"negative representation multiplicity: {negative}")
    return Counter({key: value for key, value in raw.items() if value})


def sym_power_restrictions(ell_max: int = 7) -> dict[int, Counter[str]]:
    if isinstance(ell_max, bool) or not isinstance(ell_max, int) or not 0 <= ell_max <= 7:
        raise McKayClosureError("certified McKay recurrence range is ell=0..7")
    out: dict[int, Counter[str]] = {0: Counter({"rho1": 1})}
    if ell_max == 0:
        return out
    out[1] = Counter({"rho2a": 1})
    for ell in range(1, ell_max):
        # SU(2) Clebsch-Gordan recurrence:
        # Q tensor V_ell = V_(ell+1) + V_(ell-1).
        out[ell + 1] = subtract_fail_closed(tensor_by_fundamental(out[ell]), out[ell - 1])
    return out


def representation_dimension(decomposition: Mapping[str, int]) -> int:
    return sum(IRREP_DIMS[irrep] * multiplicity for irrep, multiplicity in _clean(decomposition).items())


def coefficient_rank(decomposition: Mapping[str, int]) -> int:
    # Restriction to the finite group spans End(V_rho) once for every irrep
    # type that occurs, irrespective of multiplicity in the restricted SU(2)
    # representation.
    return sum(IRREP_DIMS[irrep] ** 2 for irrep in _clean(decomposition))


def cumulative_carrier_rank(restrictions: Mapping[int, Mapping[str, int]], ell_max: int) -> int:
    seen: set[str] = set()
    for ell in range(ell_max + 1):
        seen.update(_clean(restrictions[ell]))
    return sum(IRREP_DIMS[irrep] ** 2 for irrep in seen)


def validate() -> dict[str, object]:
    validate_graph()
    restrictions = sym_power_restrictions(7)

    for ell, expected in EXPECTED.items():
        actual = restrictions[ell]
        if actual != expected:
            raise McKayClosureError(f"ell={ell} branching mismatch: {actual} != {expected}")
        if representation_dimension(actual) != ell + 1:
            raise McKayClosureError(f"ell={ell} representation dimension is not ell+1")

    ranks = tuple(coefficient_rank(restrictions[ell]) for ell in range(8))
    if ranks != EXPECTED_COEFFICIENT_RANKS:
        raise McKayClosureError(f"coefficient ranks mismatch: {ranks}")

    cumulative = tuple(cumulative_carrier_rank(restrictions, ell) for ell in range(8))
    if cumulative != EXPECTED_CUMULATIVE_RANKS:
        raise McKayClosureError(f"cumulative ranks mismatch: {cumulative}")

    reducible = tuple(ell for ell in range(8) if sum(restrictions[ell].values()) > 1)
    if not reducible or reducible[0] != 6:
        raise McKayClosureError(f"first reducible restriction must be ell=6, got {reducible}")

    all_irreps = set().union(*(set(restrictions[ell]) for ell in range(8)))
    if all_irreps != set(IRREP_DIMS):
        raise McKayClosureError("ell=0..7 does not encounter all nine 2I irreducibles")

    regular_dimension = sum(dim * dim for dim in IRREP_DIMS.values())
    if regular_dimension != 120:
        raise McKayClosureError(f"2I regular representation dimension mismatch: {regular_dimension}")

    return {
        "schema": SCHEMA,
        "status": "PASS",
        "promotion_state": PROMOTION_STATE,
        "physical_binding": PHYSICAL_BINDING,
        "epistemic": EPISTEMIC,
        "stable_irrep_labels": True,
        "conventional_prime_aliases_are_noncanonical": True,
        "mckay_graph": "AFFINE_E8",
        "fundamental_irrep": "rho2a",
        "irrep_dimensions": IRREP_DIMS,
        "restrictions": {
            str(ell): dict(sorted(restrictions[ell].items())) for ell in range(8)
        },
        "coefficient_ranks": list(ranks),
        "cumulative_carrier_ranks": list(cumulative),
        "ell6": {
            "restriction": "rho4b + rho3b",
            "coefficient_rank": 25,
            "meaning": "FIRST_IRREDUCIBILITY_BREAKING_FINITE_RESOLUTION_THRESHOLD",
        },
        "ell7": {
            "restriction": "rho6 + rho2b",
            "coefficient_rank": 40,
            "new_block_rank": 4,
            "cumulative_rank": 120,
            "meaning": "FINITE_REPRESENTATION_CLOSURE",
        },
        "group_algebra_dimension": regular_dimension,
        "group_algebra_statement": "C[2I] = direct_sum_rho End(V_rho)",
        "runtime_default": False,
        "canon_write_authority": False,
    }


if __name__ == "__main__":
    print(json.dumps(validate(), sort_keys=True, indent=2))
