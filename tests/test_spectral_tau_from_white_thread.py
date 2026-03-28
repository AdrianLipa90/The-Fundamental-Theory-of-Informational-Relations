import numpy as np

from src.ciel_foundations.solvers.spectral_tau_from_white_thread_solver import (
    build_symmetric_coupling_matrix,
    characteristic_coefficients_3x3_zero_diag,
    hermitian_projection_entry,
    spectral_tau_modes,
)


def test_hermitian_projection_reduces_to_real_part_in_symmetric_sector():
    w = 0.74224129 + 0.12412309j
    a = hermitian_projection_entry(w)
    assert abs(a - 0.74224129) < 1e-10


def test_characteristic_coefficients_match_registered_toy_matrix():
    s2, s3 = characteristic_coefficients_3x3_zero_diag(0.74224129, 0.5, 0.3)
    assert abs(s2 - 0.8909211506872641) < 1e-12
    assert abs(s3 - 0.222672387) < 1e-12


def test_spectral_tau_modes_match_registered_roots():
    A = build_symmetric_coupling_matrix(0.74224129, 0.5, 0.3)
    tau = spectral_tau_modes(A)
    expected = np.array([0.99893394, -0.39159292, -0.60734102])
    # eigvalsh sorted ascending, helper reverses descending
    assert np.allclose(tau, expected, atol=1e-8)
