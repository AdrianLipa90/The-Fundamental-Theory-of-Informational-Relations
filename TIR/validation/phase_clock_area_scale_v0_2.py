import math


def test_fs_berry_area_relation():
    theta = 1.1
    da_fs_coeff = 0.25 * math.sin(theta)
    berry_coeff = 0.5 * math.sin(theta)
    assert math.isclose(abs(berry_coeff), 2.0 * da_fs_coeff, rel_tol=1e-15)


def test_phase_clock_scale_energy_form():
    hbar = 1.054_571_817e-34
    c = 299_792_458.0
    omega = 3.7e14
    energy = hbar * abs(omega)
    ell_phase = c / abs(omega)
    ell_energy = hbar * c / energy
    assert math.isclose(ell_phase, ell_energy, rel_tol=1e-15)


def test_constant_cell_area_reduction():
    c = 5.0
    omega = 2.0
    a_fs = 0.75
    ell = c / omega
    a_from_scale = ell * ell * a_fs
    a_from_rate = (c * c / (omega * omega)) * a_fs
    assert math.isclose(a_from_scale, a_from_rate, rel_tol=1e-15)


def test_information_curvature_scale_elimination():
    info_bits = 0.6
    kappa = math.log(2.0) / (24.0 * math.pi)
    omega = 4.0
    c = 9.0
    a_fs = 0.5
    j = math.log(2.0) * info_bits
    area = (c * c / (omega * omega)) * a_fs
    xi_area = j / area
    xi_rate = (24.0 * math.pi * kappa * info_bits / a_fs) * (omega / c) ** 2
    assert math.isclose(xi_area, xi_rate, rel_tol=1e-15)


def test_full_cp1_simplification():
    info_bits = 0.35
    kappa = math.log(2.0) / (24.0 * math.pi)
    omega = 2.4
    c = 6.2
    xi_general = (24.0 * math.pi * kappa * info_bits / math.pi) * (omega / c) ** 2
    xi_full = 24.0 * kappa * info_bits * (omega / c) ** 2
    assert math.isclose(xi_general, xi_full, rel_tol=1e-15)


def test_cycle_length_half_ratio():
    ell = 1.234
    assert math.isclose((2.0 * math.pi * ell) / (4.0 * math.pi * ell), 0.5, rel_tol=0.0, abs_tol=1e-15)
