from __future__ import annotations

import math

from src.ciel_foundations.closure.admissibility import admissibility_correction



def test_admissible_channels_are_left_unchanged() -> None:
    out = admissibility_correction((0.2, 0.2), epsilon_c=1e-12, mode="correct")
    assert out.admissible is True
    assert out.corrected is False
    assert out.rejected is False
    assert out.gamma_out == (0.2, 0.2)
    assert math.isclose(out.c_out, 0.0, rel_tol=0.0, abs_tol=1e-12)



def test_non_admissible_channels_can_be_rejected() -> None:
    out = admissibility_correction((0.0, math.pi), epsilon_c=1e-12, mode="reject")
    assert out.admissible is False
    assert out.rejected is True
    assert out.corrected is False
    assert out.gamma_out is None



def test_non_admissible_channels_are_corrected_to_zero_defect() -> None:
    out = admissibility_correction((0.0, math.pi / 2.0), epsilon_c=1e-12, mode="correct")
    assert out.admissible is True
    assert out.corrected is True
    assert out.gamma_out is not None
    assert math.isclose(out.c_out, 0.0, rel_tol=0.0, abs_tol=1e-12)
    assert out.c_out <= out.c_in + 1e-12



def test_antiphase_degeneracy_uses_deterministic_fallback() -> None:
    out = admissibility_correction((0.0, math.pi), epsilon_c=1e-12, mode="correct")
    assert out.gamma_out == (0.0, 0.0)
    assert math.isclose(out.c_out, 0.0, rel_tol=0.0, abs_tol=1e-12)
