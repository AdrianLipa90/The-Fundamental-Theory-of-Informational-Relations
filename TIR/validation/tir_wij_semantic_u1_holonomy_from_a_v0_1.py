#!/usr/bin/env python3
"""Deterministic audit for TIR semantic U(1) holonomy W_sem[A_sem]."""
from __future__ import annotations

import cmath
import json
import math


TOL = 1.0e-12


def transporter(edge_potentials):
    theta = math.fsum(float(x) for x in edge_potentials)
    return cmath.exp(1j * theta)


def close(a, b, tol=TOL):
    return abs(a - b) <= tol


checks = {}

edges_a = (0.20, -0.35)
edges_b = (0.80, 0.10)
w_a = transporter(edges_a)
w_b = transporter(edges_b)
w_ab = transporter(edges_a + edges_b)
checks["path_composition"] = close(w_ab, w_a * w_b)
checks["unit_modulus"] = close(abs(w_ab), 1.0)
checks["path_reversal"] = close(transporter(tuple(-x for x in reversed(edges_a))), w_a.conjugate())

open_edges = (0.25, -0.40, 0.75)
chi = (0.10, 0.55, -0.20, 0.35)
open_shifted = tuple(
    open_edges[k] + chi[k + 1] - chi[k] for k in range(len(open_edges))
)
expected_open = cmath.exp(1j * (chi[-1] - chi[0])) * transporter(open_edges)
checks["open_gauge_covariance"] = close(transporter(open_shifted), expected_open)

loop_edges = (0.25, -0.40, 0.75)
loop_chi = (0.10, 0.55, -0.20)
loop_shifted = tuple(
    loop_edges[k] + loop_chi[(k + 1) % len(loop_chi)] - loop_chi[k]
    for k in range(len(loop_edges))
)
checks["closed_gauge_invariance"] = close(transporter(loop_shifted), transporter(loop_edges))

z = complex(0.31, -0.47)
w = transporter((0.17, 0.29, -0.08))
coupling = w * z
checks["semantic_coupling_strength_preserved"] = close(abs(coupling), abs(z))
phase_shift = cmath.phase(coupling / z)
checks["semantic_coupling_phase_is_holonomy"] = close(
    cmath.exp(1j * phase_shift), w
)

passed = all(checks.values())
payload = {
    "schema": "TIR_WIJ_SEMANTIC_U1_HOLONOMY_FROM_A_V0_1",
    "technical_status": "PASS" if passed else "FAIL",
    "epistemic": "CHYBA",
    "canon_allowed": False,
    "checks": checks,
    "claims": {
        "u1_transport_algebra": passed,
        "physical_gauge_field_measured": False,
        "physical_nonlocal_signalling_established": False,
        "hypercharge_identification_established": False,
        "weak_boson_identification_established": False,
    },
}
print(json.dumps(payload, indent=2, sort_keys=True))
raise SystemExit(0 if passed else 1)
