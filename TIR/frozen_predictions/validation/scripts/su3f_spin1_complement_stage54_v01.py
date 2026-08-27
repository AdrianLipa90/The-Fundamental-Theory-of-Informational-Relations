#!/usr/bin/env python3
"""Stage 54: project frozen Stage 42 family generators onto the 3+5 split."""
from __future__ import annotations

import json
import math
import numpy as np

TOL = 1e-12


def traceless(H):
    return H - np.trace(H) / 3.0 * np.eye(3, dtype=complex)


def hs(A, B):
    return float(np.trace(A.conj().T @ B).real)


def project_spin1(X, generators):
    out = np.zeros_like(X)
    coeffs = []
    for J in generators:
        c = hs(J, X) / hs(J, J)
        coeffs.append(c)
        out = out + c * J
    return out, coeffs


def casimir(X, generators):
    out = np.zeros_like(X)
    for J in generators:
        K = J @ X - X @ J
        out = out + J @ K - K @ J
    return out


def gell_mann_basis():
    return [
        np.array([[0,1,0],[1,0,0],[0,0,0]], complex),
        np.array([[0,-1j,0],[1j,0,0],[0,0,0]], complex),
        np.diag([1,-1,0]).astype(complex),
        np.array([[0,0,1],[0,0,0],[1,0,0]], complex),
        np.array([[0,0,-1j],[0,0,0],[1j,0,0]], complex),
        np.array([[0,0,0],[0,0,1],[0,1,0]], complex),
        np.array([[0,0,0],[0,0,-1j],[0,1j,0]], complex),
        np.diag([1,1,-2]).astype(complex) / math.sqrt(3.0),
    ]


def main() -> None:
    omega = np.exp(2j * math.pi / 3.0)
    F3 = np.array(
        [[1,1,1],[1,omega,omega**2],[1,omega**2,omega]], dtype=complex
    ) / math.sqrt(3.0)

    D = np.diag([-1.0/3.0, 0.0, 1.0/math.sqrt(5.0)]).astype(complex)
    C = F3 @ D @ F3.conj().T
    D0 = traceless(D)
    C0 = traceless(C)

    r2 = math.sqrt(2.0)
    Jx = np.array([[0,1,0],[1,0,1],[0,1,0]], complex) / r2
    Jy = np.array([[0,-1j,0],[1j,0,-1j],[0,1j,0]], complex) / r2
    Jz = np.diag([1,0,-1]).astype(complex)
    Js = [Jx, Jy, Jz]

    rows = {}
    for name, X in (("D0", D0), ("C0", C0)):
        P3, coeffs = project_spin1(X, Js)
        P5 = X - P3
        total2 = hs(X, X)
        n3_2 = hs(P3, P3)
        n5_2 = hs(P5, P5)
        rows[name] = {
            "spin1_coefficients_Jx_Jy_Jz": coeffs,
            "norm2_total": total2,
            "norm2_spin1": n3_2,
            "norm2_spin2": n5_2,
            "fraction_spin1": n3_2 / total2,
            "fraction_spin2": n5_2 / total2,
            "casimir_spin1_residual": float(np.max(np.abs(casimir(P3, Js) - 2.0 * P3))),
            "casimir_spin2_residual": float(np.max(np.abs(casimir(P5, Js) - 6.0 * P5))),
        }

    basis = gell_mann_basis()
    cad = np.array([
        [hs(basis[a], casimir(basis[b], Js)) / 2.0 for b in range(8)]
        for a in range(8)
    ])
    evals = np.linalg.eigvalsh(cad)

    expected_D5 = (143.0 - 63.0 * math.sqrt(5.0)) / 302.0
    checks = {
        "spin1_generators_HS_orthogonal": max(abs(hs(Js[i], Js[j]) - (2.0 if i == j else 0.0)) for i in range(3) for j in range(3)) < TOL,
        "D0_spin2_nonzero": rows["D0"]["fraction_spin2"] > 1e-6,
        "D0_exact_fraction_numeric_match": abs(rows["D0"]["fraction_spin2"] - expected_D5) < 1e-12,
        "C0_spin2_fraction_one_third": abs(rows["C0"]["fraction_spin2"] - 1.0/3.0) < 1e-12,
        "casimir_spectrum_3plus5": np.max(np.abs(evals - np.array([2,2,2,6,6,6,6,6], float))) < 1e-10,
        "projected_casimir_residuals_small": max(rows["D0"]["casimir_spin1_residual"], rows["D0"]["casimir_spin2_residual"], rows["C0"]["casimir_spin1_residual"], rows["C0"]["casimir_spin2_residual"]) < 1e-12,
    }

    result = {
        "schema": "TIR_POLYGONAL_STAGE54_SU3F_SPIN1_COMPLEMENT_V0_1",
        "rows": rows,
        "adjoint_casimir_eigenvalues": [float(x) for x in evals],
        "D0_spin2_fraction_exact": "(143-63*sqrt(5))/302",
        "C0_spin2_fraction_exact": "1/3",
        "checks": checks,
        "pass": all(checks.values()),
        "compact_embedding_dynamically_selected": False,
        "physical_spin2_particle_assignment_claimed": False,
        "CKM_input_used": False,
        "mass_input_used": False
    }
    print(json.dumps(result, indent=2))
    if not result["pass"]:
        raise SystemExit("Stage 54 audit failed")


if __name__ == "__main__":
    main()
