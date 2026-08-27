#!/usr/bin/env python3
from __future__ import annotations
import json
import numpy as np

l1=np.array([[0,1,0],[1,0,0],[0,0,0]],complex)
l2=np.array([[0,-1j,0],[1j,0,0],[0,0,0]],complex)
l3=np.array([[1,0,0],[0,-1,0],[0,0,0]],complex)
l4=np.array([[0,0,1],[0,0,0],[1,0,0]],complex)
l6=np.array([[0,0,0],[0,0,1],[0,1,0]],complex)
l7=np.array([[0,0,0],[0,0,-1j],[0,1j,0]],complex)
l8=np.array([[1,0,0],[0,1,0],[0,0,-2]],complex)/np.sqrt(3.0)

def su3_exp(H):
    vals, vecs=np.linalg.eigh(H)
    return vecs @ np.diag(np.exp(1j*vals)) @ vecs.conj().T

W=su3_exp(0.23*l1-0.17*l4+0.31*l7)
Gi=su3_exp(0.41*l2+0.13*l8)
Gj=su3_exp(-0.19*l3+0.29*l6)
qi=np.array([1+0.2j,-0.3+0.4j,0.7-0.1j],complex); qi/=np.linalg.norm(qi)
qj=np.array([0.2-0.5j,0.8+0.1j,-0.1+0.2j],complex); qj/=np.linalg.norm(qj)

B=qi.conj() @ W @ qj
Wt=Gi @ W @ Gj.conj().T
Bt=(Gi@qi).conj() @ Wt @ (Gj@qj)
reverse=qj.conj() @ W.conj().T @ qi

res_gauge=float(abs(B-Bt))
res_reverse=float(abs(reverse-np.conj(B)))
res_unit=float(np.max(np.abs(W.conj().T@W-np.eye(3))))
res_det=float(abs(np.linalg.det(W)-1.0))
checks={
    "gauge_invariant_bilinear":res_gauge<1e-12,
    "reverse_link_conjugacy":res_reverse<1e-12,
    "W_unitary":res_unit<1e-12,
    "W_special":res_det<1e-12,
}
report={
    "schema":"tir.polygonal.stage27.quark-link-coupling/v0.1",
    "status":"PASS" if all(checks.values()) else "FAIL",
    "checks":checks,
    "gauge_residual":res_gauge,
    "reverse_residual":res_reverse,
    "unitarity_residual":res_unit,
    "determinant_residual":res_det,
    "scope":"gauge-invariant graph-level quark-link coupling"
}
print(json.dumps(report,indent=2,sort_keys=True))
raise SystemExit(0 if report["status"]=="PASS" else 1)
