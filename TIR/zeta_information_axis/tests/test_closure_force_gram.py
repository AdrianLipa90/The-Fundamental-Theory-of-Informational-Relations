from __future__ import annotations

import mpmath as mp

from critical_axis.closure_force_gram import (
    closure_radial_force,
    closure_radial_force_direct,
    debranges_kernel,
    lagarias_normalized_force,
    normalized_closure_force,
    regularized_pick_kernel,
    regularized_pick_kernel_diagonal,
    xf8_force_from_margin,
)


def test_radial_force_matches_direct_differentiation() -> None:
    mp.mp.dps = 60
    x = mp.mpf("10")
    r = mp.mpf("0.04")
    direct = closure_radial_force_direct(x, r)
    exact = closure_radial_force(x, r)
    assert abs(direct - exact) < mp.mpf("1e-45")


def test_xf8_margin_is_radial_force() -> None:
    mp.mp.dps = 60
    x = mp.mpf("7")
    r = mp.mpf("0.09")
    assert abs(
        xf8_force_from_margin(x, r) - closure_radial_force(x, r)
    ) < mp.mpf("1e-45")


def test_regularized_pick_diagonal_is_radial_force() -> None:
    mp.mp.dps = 60
    x = mp.mpf("8")
    y = mp.mpf("0.2")
    assert abs(
        regularized_pick_kernel_diagonal(x, y)
        - closure_radial_force(x, y * y)
    ) < mp.mpf("1e-45")


def test_debranges_crosswalk_off_diagonal() -> None:
    mp.mp.dps = 60
    z = mp.mpc("3.0", "0.2")
    w = mp.mpc("4.0", "0.1")
    lhs = regularized_pick_kernel(z, w)
    rhs = mp.pi * debranges_kernel(z, w)
    assert abs(lhs - rhs) < mp.mpf("1e-45")


def test_lagarias_force_matches_xi_coordinate_force() -> None:
    mp.mp.dps = 60
    t = mp.mpf("9")
    r = mp.mpf("0.04")
    lhs = lagarias_normalized_force(t, r)
    rhs = normalized_closure_force(t, r)
    assert abs(lhs - rhs) < mp.mpf("1e-40")
