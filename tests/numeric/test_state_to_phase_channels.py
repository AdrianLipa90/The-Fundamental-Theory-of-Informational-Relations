from __future__ import annotations

import math

import numpy as np

from Simulations.code.closure.closure_operator import closure_operator
from src.ciel_foundations.closure.phase_channels import state_to_phase_channels



def test_state_to_phase_channels_is_global_phase_invariant() -> None:
    psi = np.array([1.0 / np.sqrt(2.0), 1.0j / np.sqrt(2.0)], dtype=np.complex128)
    alpha = 0.913
    psi2 = np.exp(1j * alpha) * psi
    out1 = state_to_phase_channels(psi)
    out2 = state_to_phase_channels(psi2)
    assert math.isclose(out1.gamma[0], out2.gamma[0], rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(out1.gamma[1], out2.gamma[1], rel_tol=0.0, abs_tol=1e-12)
    assert out1.pole_chart is out2.pole_chart



def test_north_pole_sets_phi_to_zero() -> None:
    psi = np.array([1.0 + 0.0j, 0.0 + 0.0j], dtype=np.complex128)
    out = state_to_phase_channels(psi)
    assert math.isclose(out.gamma[0], 0.0, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(out.gamma[1], 0.0, rel_tol=0.0, abs_tol=1e-12)
    assert out.pole_chart is True



def test_state_to_closure_bridge_is_deterministic() -> None:
    psi = np.array([1.0 / np.sqrt(2.0), np.exp(1j * 0.3) / np.sqrt(2.0)], dtype=np.complex128)
    g1 = state_to_phase_channels(psi).gamma
    g2 = state_to_phase_channels(psi).gamma
    d1, r1, c1 = closure_operator(g1)
    d2, r2, c2 = closure_operator(g2)
    assert np.allclose(d1, d2, atol=1e-12)
    assert math.isclose(r1, r2, rel_tol=0.0, abs_tol=1e-12)
    assert math.isclose(c1, c2, rel_tol=0.0, abs_tol=1e-12)
