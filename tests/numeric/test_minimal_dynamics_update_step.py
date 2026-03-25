from __future__ import annotations

import math

from src.ciel_foundations.closure.dynamics import minimal_update_step



def test_accept_if_nonworsening_accepts_better_step() -> None:
    out = minimal_update_step((0.0, 1.0), (0.0, -1.0), dt=1.0, mode="accept_if_nonworsening")
    assert out.accepted is True
    assert out.rolled_back is False
    assert out.c_out <= out.c_in + 1e-12



def test_rollback_mode_rejects_nonadmissible_step() -> None:
    out = minimal_update_step((0.0, 0.0), (0.0, math.pi), dt=1.0, mode="rollback", epsilon_c=1e-12)
    assert out.accepted is False
    assert out.rolled_back is True
    assert out.gamma_out == out.gamma_in
    assert math.isclose(out.c_out, out.c_in, rel_tol=0.0, abs_tol=1e-12)



def test_correct_mode_returns_zero_defect_when_needed() -> None:
    out = minimal_update_step((0.0, 0.0), (0.0, math.pi), dt=1.0, mode="correct", epsilon_c=1e-12)
    assert out.accepted is True
    assert out.corrected is True
    assert math.isclose(out.c_out, 0.0, rel_tol=0.0, abs_tol=1e-12)



def test_angles_are_wrapped_mod_2pi() -> None:
    out = minimal_update_step((2.0 * math.pi - 0.1, 0.0), (1.0, 0.0), dt=0.2, mode="accept_if_nonworsening")
    assert 0.0 <= out.gamma_prop[0] < 2.0 * math.pi
