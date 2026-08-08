"""TIR-side typed bridge to canonical PhaseNav/NOEMA dependency state v0.7.

This module records software/provenance closure only. It does not change the
scientific status of a TIR formula and cannot consume measured masses or Yukawa
couplings as derivation parents.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json

PHASENAV_COMMIT = "54f65f2ca7d35cdd98f0ab8984cc1a8d74444a96"
NOEMA_COMMIT = "42a0a8916e81ca27f2213bf0f28538f046c2e89a"
ROUTING_DIM = 36
INTRINSIC_COEFFICIENT_DIM = 4


@dataclass(frozen=True)
class DependencyState:
    name: str
    status: str
    scientific_promotion: bool = False


STATES = (
    DependencyState("ROLE_ROUTER_HABC", "STRUCTURAL_ROLE_ROUTING_PASS"),
    DependencyState("ORBIT_DIRECTION", "IMPLEMENTED_PROJECT_ORBITAL_RULE"),
    DependencyState(
        "RELATIONAL_GRADIENT",
        "IMPLEMENTED_SOURCE_OPERATOR_CANDIDATE_TIR_BINDING",
    ),
    DependencyState("TIR_SLOT_BINDING", "OPEN"),
    DependencyState(
        "COLLATZ_STOPPING_ORIENTATION",
        "RETROSPECTIVE_CANDIDATE_NEEDS_PROSPECTIVE_TEST",
    ),
    DependencyState("TIR_COMMON_LIKELIHOOD", "OPEN"),
    DependencyState("TIR_NEUTRON_EDM", "PHYSICAL_FAIL"),
    DependencyState("SOH_C004", "OPEN"),
    DependencyState("SOH_C005", "OPEN"),
)


def integration_receipt() -> dict[str, object]:
    payload: dict[str, object] = {
        "schema": "tir.phasenav-noema-dependency/v0.7",
        "phasenav_commit": PHASENAV_COMMIT,
        "noema_commit": NOEMA_COMMIT,
        "routing_dimension": ROUTING_DIM,
        "intrinsic_coefficient_dimension": INTRINSIC_COEFFICIENT_DIM,
        "intrinsic_equals_routing": False,
        "states": {state.name: state.status for state in STATES},
        "firewall": {
            "measured_mass_as_parent": "FORBIDDEN",
            "measured_yukawa_as_parent": "FORBIDDEN",
            "vectorization_promotes_claim": False,
            "noema_memory_promotes_claim": False,
        },
        "scientific_promotion": "NOT_PERFORMED",
    }
    canonical = json.dumps(
        payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    payload["receipt_sha256"] = hashlib.sha256(canonical).hexdigest()
    return payload


def validate_bridge() -> dict[str, object]:
    receipt = integration_receipt()
    states = receipt["states"]
    assert isinstance(states, dict)
    assert ROUTING_DIM == 36
    assert INTRINSIC_COEFFICIENT_DIM == 4
    assert ROUTING_DIM != INTRINSIC_COEFFICIENT_DIM
    assert states["ROLE_ROUTER_HABC"] == "STRUCTURAL_ROLE_ROUTING_PASS"
    assert states["TIR_SLOT_BINDING"] == "OPEN"
    assert states["TIR_NEUTRON_EDM"] == "PHYSICAL_FAIL"
    assert states["SOH_C004"] == "OPEN"
    assert states["SOH_C005"] == "OPEN"
    assert all(not state.scientific_promotion for state in STATES)
    return {
        "status": "PASS",
        "receipt_sha256": receipt["receipt_sha256"],
        "scientific_promotion": "NOT_PERFORMED",
    }


if __name__ == "__main__":
    print(json.dumps(validate_bridge(), indent=2, sort_keys=True))
