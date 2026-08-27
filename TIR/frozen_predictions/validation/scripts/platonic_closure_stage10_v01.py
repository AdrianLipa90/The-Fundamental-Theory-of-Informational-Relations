#!/usr/bin/env python3
from __future__ import annotations
import json, math
import numpy as np

TOL = 1e-12

def equal_edge_star(N: int):
    theta = 2.0 * math.pi / N
    c = math.cos(theta) / (1.0 - math.cos(theta))
    r2 = 1.0 - c*c
    r = math.sqrt(max(0.0, r2)) if r2 >= -TOL else float('nan')
    apex = np.array([0.0, 0.0, 1.0])
    base = np.array([[r*math.cos(2*math.pi*k/N), r*math.sin(2*math.pi*k/N), c] for k in range(N)])
    return c, r, apex, base

def closure_counts(N: int):
    if N >= 6:
        return None
    d = 6 - N
    return {"V": 12.0/d, "E": 6.0*N/d, "F": 4.0*N/d}

def standard_icosahedron():
    phi = (1.0 + math.sqrt(5.0))/2.0
    pts=[]
    for a in (-1.0,1.0):
        for b in (-phi,phi):
            pts += [(0.0,a,b),(a,b,0.0),(b,0.0,a)]
    V=np.unique(np.asarray(pts,float),axis=0)
    V=V/np.linalg.norm(V[0])
    return V

def main():
    rows={}
    ok=True
    for N in (3,4,5,6):
        c,r,P,B=equal_edge_star(N)
        da=np.linalg.norm(B-P,axis=1)
        db=np.array([np.linalg.norm(B[(k+1)%N]-B[k]) for k in range(N)])
        defect=2*math.pi-N*math.pi/3
        counts=closure_counts(N)
        row={
            "N":N,"c_N":c,"base_radius":r,
            "apex_edge_spread":float(np.ptp(da)),
            "base_edge_spread":float(np.ptp(db)),
            "equal_edge_residual":float(np.max(np.abs(da-db))),
            "angular_defect":defect,"closure_counts":counts,
        }
        if counts:
            row["gauss_bonnet_residual"] = abs(counts["V"]*defect-4*math.pi)
        rows[str(N)]=row

    c4,r4,P4,B4=equal_edge_star(4)
    oct_vertices=np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],float)
    oct_neigh=[v for v in oct_vertices if abs(P4@v) < TOL]
    oct_ok=(abs(c4)<TOL and len(oct_neigh)==4 and all(abs(P4@v)<TOL for v in oct_neigh))

    I=standard_icosahedron(); target=1/math.sqrt(5)
    p=I[0]
    neigh=np.where(np.abs(I@p-target)<1e-10)[0]
    sub=I[neigh]@I[neigh].T
    deg=[]
    for i in range(5):
        deg.append(int(np.count_nonzero(np.abs(sub[i]-target)<1e-10)))
    icosa_ok=(len(neigh)==5 and deg==[2,2,2,2,2])

    expected={3:(4,6,4),4:(6,12,8),5:(12,30,20)}
    for N,(V,E,F) in expected.items():
        c=rows[str(N)]["closure_counts"]
        ok &= abs(c["V"]-V)<TOL and abs(c["E"]-E)<TOL and abs(c["F"]-F)<TOL
        ok &= rows[str(N)]["equal_edge_residual"]<TOL
        ok &= rows[str(N)]["gauss_bonnet_residual"]<TOL
    ok &= oct_ok and icosa_ok
    ok &= abs(rows["6"]["angular_defect"])<TOL and rows["6"]["base_radius"]<TOL

    result={
        "schema":"TIR-POLYGONAL-PLATONIC-CLOSURE/0.1",
        "scope":"pure mathematics; no particle/atomic/PDG inputs",
        "rows":rows,
        "N4_octahedral_local_star":oct_ok,
        "N5_icosahedral_local_star":icosa_ok,
        "finite_spherical_closures":{"3":"tetrahedron {3,3}","4":"octahedron {3,4}","5":"icosahedron {3,5}"},
        "N6_boundary":"Euclidean triangular {3,6}; zero angular defect; finite spherical V formula diverges",
        "verdict":"PASS" if ok else "FAIL",
    }
    print(json.dumps(result,indent=2))
    return 0 if ok else 1

if __name__=='__main__':
    raise SystemExit(main())
