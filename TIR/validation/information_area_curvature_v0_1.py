import math

KAPPA = math.log(2.0) / (24.0 * math.pi)


def fs_area_full_sphere() -> float:
    return math.pi


def berry_flux_full_sphere(sign: float = 1.0) -> float:
    return sign * 2.0 * math.pi


def physical_relational_area(a_fs: float, ell_r: float) -> float:
    if a_fs <= 0.0 or ell_r <= 0.0:
        raise ValueError("a_fs and ell_r must be positive")
    return ell_r * ell_r * a_fs


def xi_information_area(information_bits: float, a_fs: float, ell_r: float) -> float:
    return math.log(2.0) * information_bits / physical_relational_area(a_fs, ell_r)


def test_full_sphere_fs_area():
    assert abs(fs_area_full_sphere() - math.pi) < 1e-15


def test_full_sphere_berry_flux():
    assert abs(berry_flux_full_sphere() - 2.0 * math.pi) < 1e-15


def test_berry_to_fs_area_factor():
    assert abs(berry_flux_full_sphere() - 2.0 * fs_area_full_sphere()) < 1e-15


def test_physical_area_scales_quadratically():
    a_fs = 0.7
    assert abs(
        physical_relational_area(a_fs, 6.0)
        - 9.0 * physical_relational_area(a_fs, 2.0)
    ) < 1e-15


def test_xi_scales_inverse_square():
    base = xi_information_area(1.3, 0.7, 2.0)
    scaled = xi_information_area(1.3, 0.7, 6.0)
    assert abs(scaled - base / 9.0) < 1e-15


def test_kappa_substitution():
    assert abs(24.0 * math.pi * KAPPA - math.log(2.0)) < 1e-15
