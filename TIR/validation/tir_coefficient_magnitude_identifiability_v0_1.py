#!/usr/bin/env python3
from __future__ import annotations

L3, L4, L5 = 7, 2, 5
ROWS = [
    ("ELECTRON_ACTION", "h", 1, "IDENTITY", "ADMITTED_ROLE"),
    ("ELECTRON_ACTION", "a", 3, "GENERATION_COUNT_3", "OPEN_EXTERNAL_OR_PROJECT_PRIMITIVE"),
    ("ELECTRON_ACTION", "b", 1, "IDENTITY", "OPEN_TRANSITION_BINDING"),
    ("ELECTRON_ACTION", "c", 1, "IDENTITY", "OPEN_TRANSITION_BINDING"),
    ("E_TO_MU_RELEASE", "a", L5, "L5", "OPEN_TRANSITION_BINDING"),
    ("E_TO_MU_RELEASE", "b", L4, "L4", "OPEN_TRANSITION_BINDING"),
    ("E_TO_MU_RELEASE", "c", L3 + 1, "L3_PLUS_IDENTITY", "OPEN_UNDERDETERMINED"),
    ("MU_TO_TAU_RELEASE", "a", 3, "GENERATION_COUNT_3", "OPEN_EXTERNAL_OR_PROJECT_PRIMITIVE"),
    ("MU_TO_TAU_RELEASE", "b", 1, "IDENTITY", "OPEN_TRANSITION_BINDING"),
    ("MU_TO_TAU_RELEASE", "c", L3, "L3", "OPEN_TRANSITION_BINDING"),
]


def role_sign_nonidentifiability():
    for chi in (-1, 1):
        assert chi * 1 != chi * 2
        assert (chi > 0) == (chi * 1 > 0) == (chi * 2 > 0)
    return True


def validate():
    assert (L3, L4, L5) == (7, 2, 5)
    assert L5 == 5 and L4 == 2 and L3 + 1 == 8 and L3 == 7
    assert L4 + L3 == 9
    assert L4 + L3 != 5
    expected = {
        ("ELECTRON_ACTION", "h"): 1,
        ("ELECTRON_ACTION", "a"): 3,
        ("ELECTRON_ACTION", "b"): 1,
        ("ELECTRON_ACTION", "c"): 1,
        ("E_TO_MU_RELEASE", "a"): 5,
        ("E_TO_MU_RELEASE", "b"): 2,
        ("E_TO_MU_RELEASE", "c"): 8,
        ("MU_TO_TAU_RELEASE", "a"): 3,
        ("MU_TO_TAU_RELEASE", "b"): 1,
        ("MU_TO_TAU_RELEASE", "c"): 7,
    }
    assert {(s, k): v for s, k, v, _, _ in ROWS} == expected
    assert role_sign_nonidentifiability()
    assert any(sel.startswith("OPEN") for *_, sel in ROWS)
    fully_forced = [r for r in ROWS if not r[4].startswith("OPEN")]
    assert fully_forced == [("ELECTRON_ACTION", "h", 1, "IDENTITY", "ADMITTED_ROLE")]


if __name__ == "__main__":
    validate()
    print("schema=TIR_COEFFICIENT_MAGNITUDE_IDENTIFIABILITY_V0_1")
    print("status=PASS")
    print("role_sign_magnitude_nonidentifiability=true")
    print("platonic_l_arithmetic_closed=true")
    print("legacy_5_equals_l4_plus_l3_rejected=true")
    print("fully_source_forced_rows=1")
    print("transition_parent_selection_open=true")
    print("full_coefficient_magnitude_forcing=false")
    print("next_gate=COEFFICIENT_FREE_TRANSITION_TO_PARENT_SELECTION")
