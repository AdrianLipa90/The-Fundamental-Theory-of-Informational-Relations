#!/usr/bin/env python3
from __future__ import annotations
import json
import numpy as np

I3 = np.eye(3, dtype=np.complex128)
P3 = np.array([[0,0,1],[1,0,0],[0,1,0]], dtype=np.complex128)

L = [
    np.array([[0,1,0],[1,0,0],[0,0,0]], complex),
    np.array([[0,-1j,0],[1j,0,0],[0,0,0]], complex),
    np.array([[1,0,0],[0,-1,0],[0,0,0]], complex),
    np.array([[0,0,1],[0,0,0],[1,0,0]], complex),
    np.array([[0,0,-1j],[0,0,0],[1j,0,0]], complex),
    np.array([[0,0,0],[0,0,1],[0,1,0]], complex),
    np.array([[0,0,0],[0,0,-1j],[0,1j,0]], complex),
    np.array([[1,0,0],[0,1,0],[0,0,-2]], complex) / np.sqrt(3.0),
]

ext = [np.kron(x, I3) for x in L]
family = np.kron(I3, P3)
rank = int(np.linalg.matrix_rank(np.stack([x.reshape(-1) for x in ext], axis=1)))
comm_max = float(max(np.max(np.abs(x @ family - family @ x)) for x in ext))
gram = np.array([[np.trace(a.conj().T @ b).real for b in ext] for a in ext])
gram_resid = float(np.max(np.abs(gram - 6.0*np.eye(8))))
checks = {
    "eight_independent_color_generators": rank == 8,
    "family_commutators_zero": comm_max < 1e-14,
    "extended_gell_mann_gram": gram_resid < 1e-12,
}
report = {
    "schema":"tir.polygonal.stage26.family-blind-gluon/v0.1",
    "status":"PASS" if all(checks.values()) else "FAIL",
    "checks":checks,
    "generator_rank":rank,
    "family_commutator_max_abs":comm_max,
    "gram_max_abs_residual":gram_resid,
    "scope":"eight su(3)_C generators extended over three family labels"
}
print(json.dumps(report, indent=2, sort_keys=True))
raise SystemExit(0 if report["status"] == "PASS" else 1)
