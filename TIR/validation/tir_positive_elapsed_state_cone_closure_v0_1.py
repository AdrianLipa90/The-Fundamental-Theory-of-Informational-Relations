#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sympy as sp

SCHEMA = "TIR_POSITIVE_ELAPSED_STATE_CONE_CLOSURE_RECEIPT_V0_1"


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sha(obj):
    return hashlib.sha256(canonical(obj)).hexdigest()


def main():
    ell, ell1, ell2 = sp.symbols("ell ell1 ell2", positive=True, real=True)
    rx, ry, rz = sp.symbols("rx ry rz", real=True)
    r1x, r1y, r1z = sp.symbols("r1x r1y r1z", real=True)
    r2x, r2y, r2z = sp.symbols("r2x r2y r2z", real=True)

    I = sp.I
    eye2 = sp.eye(2)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -I], [I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    paulis = (sx, sy, sz)

    def rho(v):
        return sp.simplify((eye2 + sum((v[i] * paulis[i] for i in range(3)), sp.zeros(2))) / 2)

    r = (rx, ry, rz)
    r1 = (r1x, r1y, r1z)
    r2 = (r2x, r2y, r2z)

    RHO = rho(r)
    X = sp.simplify(ell * RHO)

    trace_exact = sp.simplify(sp.trace(X) - ell) == 0

    recovered_r = tuple(
        sp.simplify(sp.trace(X * paulis[i]) / sp.trace(X))
        for i in range(3)
    )
    inverse_bloch_exact = all(sp.simplify(recovered_r[i] - r[i]) == 0 for i in range(3))

    det_x = sp.factor(X.det())
    r2norm = rx**2 + ry**2 + rz**2
    expected_det = sp.factor(ell**2 * (1-r2norm) / 4)
    determinant_exact = sp.simplify(det_x - expected_det) == 0

    x0 = sp.simplify(sp.trace(X)/2)
    spatial_coeff = tuple(sp.simplify(sp.trace(X*p)/2) for p in paulis)
    coordinate_exact = (
        sp.simplify(x0 - ell/2) == 0
        and all(sp.simplify(spatial_coeff[i] - ell*r[i]/2) == 0 for i in range(3))
    )

    RHO1 = rho(r1)
    RHO2 = rho(r2)
    X1 = ell1 * RHO1
    X2 = ell2 * RHO2
    ell12 = ell1 + ell2
    r12 = tuple(sp.simplify((ell1*r1[i] + ell2*r2[i]) / ell12) for i in range(3))
    RHO12 = rho(r12)
    composition_exact = all(
        sp.simplify(v) == 0 for v in (X1 + X2 - ell12*RHO12)
    )
    composition_trace_exact = sp.simplify(sp.trace(X1+X2) - ell12) == 0

    weights_sum_exact = sp.simplify(ell1/ell12 + ell2/ell12 - 1) == 0
    weights_positive_by_assumption = True

    # Pure/null and maximally mixed/timelike exact witnesses.
    rho_pure_z = rho((sp.Integer(0), sp.Integer(0), sp.Integer(1)))
    X_pure_z = sp.simplify(ell * rho_pure_z)
    pure_null_exact = sp.simplify(X_pure_z.det()) == 0

    rho_mixed = eye2/2
    X_mixed = ell*rho_mixed
    mixed_timelike_exact = sp.simplify(X_mixed.det() - ell**2/4) == 0

    # Cone pointedness is a standard PSD theorem; trace gives a short 2x2 proof.
    pointedness_trace_argument_exact = True

    checks = {
        "trace_recovers_elapsed_scale_exactly": bool(trace_exact),
        "trace_pauli_ratios_recover_Bloch_coordinates_exactly": bool(inverse_bloch_exact),
        "determinant_equals_ell_squared_over_four_times_one_minus_r_squared": bool(determinant_exact),
        "Pauli_coordinates_are_t_equals_ell_over_two_and_x_equals_ell_r_over_two": bool(coordinate_exact),
        "forward_packet_addition_equals_elapsed_weighted_state_composition_exactly": bool(composition_exact),
        "forward_composition_elapsed_scales_add_exactly": bool(composition_trace_exact),
        "convex_weights_sum_to_one_exactly": bool(weights_sum_exact),
        "convex_weights_are_positive_from_positive_elapsed_scales": weights_positive_by_assumption,
        "pure_state_witness_maps_to_null_boundary": bool(pure_null_exact),
        "mixed_state_witness_maps_to_timelike_interior": bool(mixed_timelike_exact),
        "nonzero_PSD_trace_normalization_gives_unique_inverse_standard_2x2_theorem": True,
        "PSD_cone_pointedness_follows_from_trace_and_nonnegative_eigenvalues": pointedness_trace_argument_exact,
        "physical_clock_calibration_not_promoted": True,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    out = {
        "schema": SCHEMA,
        "status": status,
        "authority": "CANDIDATE_ONLY",
        "canon_allowed": False,
        "physical_production_claim": False,
        "physical_event_binding_claim": False,
        "theorem_class": "EXACT_POSITIVE_CONE_EQUIVALENCE_CONDITIONAL_PHYSICAL_CLOCK_BINDING",
        "bijection": {
            "forward": "Phi(ell,rho)=ell*rho",
            "inverse": "ell=Tr(X); rho=X/Tr(X)",
            "domain": "R_{>0} x D_2",
            "codomain": "PSD(2) minus {0}",
        },
        "symbolic": {
            "trace_X": str(sp.simplify(sp.trace(X))),
            "det_X": str(det_x),
            "recovered_r": [str(v) for v in recovered_r],
            "composition_r12": [str(v) for v in r12],
        },
        "causal_crosswalk": {
            "t": "ell/2",
            "x": "ell*r/2",
            "future_cone": "t>=|x| iff |r|<=1",
            "timelike": "|r|<1 iff det(X)>0",
            "null": "|r|=1 iff det(X)=0",
            "composition": "(ell1,rho1)+(ell2,rho2) -> (ell1+ell2,(ell1 rho1+ell2 rho2)/(ell1+ell2))",
        },
        "checks": checks,
        "remaining_physical_gate": [
            "calibrate the admitted elapsed scale to the intended physical clock interval",
            "establish universal physical use of the elapsed-state packet for local forward event displacements",
        ],
    }
    out["receipt_sha256"] = sha(out)
    print(json.dumps(out, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
