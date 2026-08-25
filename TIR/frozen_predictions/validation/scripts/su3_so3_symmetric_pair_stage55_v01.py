#!/usr/bin/env python3
"""Stage 55: verify the su(3)=so(3)+p compact symmetric-pair brackets."""
from __future__ import annotations

import json
import math
import numpy as np

TOL = 1e-10


def hs(A, B):
    return float(np.trace(A.conj().T @ B).real)


def bracket(A, B):
    return -1j * (A @ B - B @ A)


def independent(mats):
    selected, vecs = [], []
    for X in mats:
        v = np.concatenate([X.real.ravel(), X.imag.ravel()])
        if np.linalg.norm(v) < TOL:
            continue
        if not vecs:
            selected.append(X); vecs.append(v); continue
        old = np.linalg.matrix_rank(np.stack(vecs, axis=1), TOL)
        new = np.linalg.matrix_rank(np.stack(vecs + [v], axis=1), TOL)
        if new > old:
            selected.append(X); vecs.append(v)
    return selected


def gell_mann():
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
    r2 = math.sqrt(2.0)
    Jx = np.array([[0,1,0],[1,0,1],[0,1,0]], complex) / r2
    Jy = np.array([[0,-1j,0],[1j,0,-1j],[0,1j,0]], complex) / r2
    Jz = np.diag([1,0,-1]).astype(complex)
    Js = [Jx, Jy, Jz]

    def casimir(X):
        out = np.zeros_like(X)
        for J in Js:
            K = J @ X - X @ J
            out += J @ K - K @ J
        return out

    def Pk(X):
        return (6.0 * X - casimir(X)) / 4.0

    def Pp(X):
        return (casimir(X) - 2.0 * X) / 4.0

    base = gell_mann()
    k_basis = independent([Pk(X) for X in base])
    p_basis = independent([Pp(X) for X in base])

    residual_kk = max(np.linalg.norm(Pp(bracket(A, B))) for A in k_basis for B in k_basis)
    residual_kp = max(np.linalg.norm(Pk(bracket(A, B))) for A in k_basis for B in p_basis)
    residual_pp = max(np.linalg.norm(Pp(bracket(A, B))) for A in p_basis for B in p_basis)

    checks = {
        "rank_k_3": len(k_basis) == 3,
        "rank_p_5": len(p_basis) == 5,
        "kk_in_k": residual_kk < 1e-12,
        "kp_in_p": residual_kp < 1e-12,
        "pp_in_k": residual_pp < 1e-12,
    }

    result = {
        "schema": "TIR_POLYGONAL_STAGE55_SU3_SO3_SYMMETRIC_PAIR_V0_1",
        "dimensions": {"k": len(k_basis), "p": len(p_basis), "total": len(k_basis) + len(p_basis)},
        "forbidden_projection_residuals": {
            "Pp([k,k])": float(residual_kk),
            "Pk([k,p])": float(residual_kp),
            "Pp([p,p])": float(residual_pp),
        },
        "symmetric_pair": "(su(3), so(3))",
        "coset": "SU(3)/SO(3)",
        "coset_dimension": 5,
        "checks": checks,
        "pass": all(checks.values()),
        "CKM_input_used": False,
        "mass_input_used": False,
        "polygon_N5_identification_claimed": False
    }
    print(json.dumps(result, indent=2))
    if not result["pass"]:
        raise SystemExit("Stage 55 audit failed")


if __name__ == "__main__":
    main()
