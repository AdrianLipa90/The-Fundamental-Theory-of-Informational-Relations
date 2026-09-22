#!/usr/bin/env python3
"""Deterministic validator for TIR White-Thread spin-lift / Lyapunov v0.1."""
from __future__ import annotations

import cmath
import json
import math


TOL = 1.0e-10


def close(a, b, tol=TOL):
    return abs(a - b) <= tol


def u1_from_turn(q):
    return cmath.exp(2j * math.pi * q)


def spin_from_lift(q_tilde):
    return cmath.exp(1j * math.pi * q_tilde)


def edge_potential(delta, k1, khalf):
    return k1 * (1.0 - math.cos(delta)) + khalf * (
        1.0 - math.cos(delta / 2.0)
    )


def edge_gradient(delta, k1, khalf):
    return k1 * math.sin(delta) + 0.5 * khalf * math.sin(delta / 2.0)


def graph_potential(theta, edges, k1, khalf, gamma):
    total = 0.0
    for e, (i, j) in enumerate(edges):
        delta = theta[i] - theta[j] - gamma[e]
        total += edge_potential(delta, k1[e], khalf[e])
    return total


def graph_gradient(theta, edges, k1, khalf, gamma):
    grad = [0.0 for _ in theta]
    for e, (i, j) in enumerate(edges):
        delta = theta[i] - theta[j] - gamma[e]
        g = edge_gradient(delta, k1[e], khalf[e])
        grad[i] += g
        grad[j] -= g
    return grad


checks = {}

# Exact double-cover identities.
samples = (-3.75, -1.0, -0.5, 0.0, 0.5, 1.25, 4.75)
checks["spin_square_projects_to_u1"] = all(
    close(spin_from_lift(q) ** 2, u1_from_turn(q % 1.0)) for q in samples
)
checks["two_pi_shift_flips_spin"] = all(
    close(spin_from_lift(q + 1.0), -spin_from_lift(q)) for q in samples
)
checks["two_pi_shift_preserves_projected_u1"] = all(
    close(u1_from_turn((q + 1.0) % 1.0), u1_from_turn(q % 1.0)) for q in samples
)
checks["four_pi_shift_returns_spin"] = all(
    close(spin_from_lift(q + 2.0), spin_from_lift(q)) for q in samples
)
checks["half_turn_is_minus_one"] = close(u1_from_turn(0.5), -1.0 + 0.0j)
checks["half_seam_spin_lifts_are_plus_minus_i"] = (
    close(spin_from_lift(0.5), 1j)
    and close(spin_from_lift(1.5), -1j)
    and close(spin_from_lift(0.5) ** 2, -1.0 + 0.0j)
    and close(spin_from_lift(1.5) ** 2, -1.0 + 0.0j)
)

# Mixed 2pi / 4pi periodicity.
k1_test = 0.7
kh_test = 1.3
for_delta = (0.1, 1.0, 2.7, -3.4)
checks["full_potential_four_pi_periodic"] = all(
    close(
        edge_potential(d + 4.0 * math.pi, k1_test, kh_test),
        edge_potential(d, k1_test, kh_test),
    )
    for d in for_delta
)
checks["projective_term_two_pi_periodic"] = all(
    close(
        k1_test * (1.0 - math.cos(d + 2.0 * math.pi)),
        k1_test * (1.0 - math.cos(d)),
    )
    for d in for_delta
)
checks["spin_term_distinguishes_two_pi_sheet"] = any(
    not close(
        kh_test * (1.0 - math.cos((d + 2.0 * math.pi) / 2.0)),
        kh_test * (1.0 - math.cos(d / 2.0)),
    )
    for d in for_delta
)

# Finite graph gradient vs central finite difference.
theta = [0.2, 1.1, -0.7, 2.0]
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
k1 = [0.8, 0.5, 1.2, 0.9, 0.4]
khalf = [0.3, 1.1, 0.6, 0.2, 0.7]
gamma = [0.15, -0.3, 0.25, -0.4, 0.05]
grad = graph_gradient(theta, edges, k1, khalf, gamma)
eps = 1.0e-6
grad_fd = []
for i in range(len(theta)):
    plus = theta[:]
    minus = theta[:]
    plus[i] += eps
    minus[i] -= eps
    grad_fd.append(
        (
            graph_potential(plus, edges, k1, khalf, gamma)
            - graph_potential(minus, edges, k1, khalf, gamma)
        )
        / (2.0 * eps)
    )
checks["analytic_gradient_matches_finite_difference"] = all(
    close(a, b, 5.0e-8) for a, b in zip(grad, grad_fd)
)

# Overdamped Lyapunov identity: theta_dot_i = -grad_i / eta_i.
eta = [1.0, 1.5, 0.8, 2.0]
theta_dot = [-g / e for g, e in zip(grad, eta)]
vdot_chain_rule = sum(g * td for g, td in zip(grad, theta_dot))
vdot_expected = -sum((g * g) / e for g, e in zip(grad, eta))
checks["overdamped_lyapunov_identity"] = close(vdot_chain_rule, vdot_expected)
checks["overdamped_lyapunov_nonpositive"] = vdot_expected <= TOL

# Inertial energy balance algebra at one deterministic state:
# I theta_ddot + eta theta_dot + grad = 0.
inertia = [1.2, 0.7, 1.5, 0.9]
vel = [0.4, -0.2, 0.1, 0.3]
acc = [
    -(e * v + g) / mass
    for mass, e, v, g in zip(inertia, eta, vel, grad)
]
kinetic_rate = sum(mass * v * a for mass, v, a in zip(inertia, vel, acc))
potential_rate = sum(g * v for g, v in zip(grad, vel))
energy_rate = kinetic_rate + potential_rate
dissipation = -sum(e * v * v for e, v in zip(eta, vel))
checks["inertial_energy_balance"] = close(energy_rate, dissipation)
checks["inertial_energy_nonincreasing"] = energy_rate <= TOL

# Loop closure distinction: 2pi projective closure can be nontrivial in 4pi lift.
loop_projective = 2.0 * math.pi
checks["two_pi_loop_projectively_closed"] = close(
    cmath.exp(1j * loop_projective), 1.0 + 0.0j
)
checks["two_pi_loop_spin_flips"] = close(
    cmath.exp(0.5j * loop_projective), -1.0 + 0.0j
)
checks["four_pi_loop_spin_closes"] = close(
    cmath.exp(0.5j * (4.0 * math.pi)), 1.0 + 0.0j
)

passed = all(checks.values())
payload = {
    "schema": "TIR_WHITE_THREAD_SPIN_LIFT_LYAPUNOV_V0_1",
    "technical_status": "PASS" if passed else "FAIL",
    "checks": checks,
    "claims": {
        "spin_lift_double_cover_identities": all(
            checks[k]
            for k in (
                "spin_square_projects_to_u1",
                "two_pi_shift_flips_spin",
                "two_pi_shift_preserves_projected_u1",
                "four_pi_shift_returns_spin",
            )
        ),
        "mixed_periodic_potential": all(
            checks[k]
            for k in (
                "full_potential_four_pi_periodic",
                "projective_term_two_pi_periodic",
                "spin_term_distinguishes_two_pi_sheet",
            )
        ),
        "isolated_static_holonomy_lyapunov": all(
            checks[k]
            for k in (
                "overdamped_lyapunov_identity",
                "overdamped_lyapunov_nonpositive",
                "inertial_energy_balance",
                "inertial_energy_nonincreasing",
            )
        ),
        "physical_maxwell_binding_established": False,
        "physical_black_hole_interpretation_established": False,
        "physical_nonlocal_signalling_established": False,
    },
}
print(json.dumps(payload, indent=2, sort_keys=True))
raise SystemExit(0 if passed else 1)
