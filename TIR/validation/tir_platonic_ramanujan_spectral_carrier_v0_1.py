#!/usr/bin/env python3
"""Deterministic validation for TIR Platonic-Ramanujan spectral carrier v0.1."""
from __future__ import annotations
import json, math
from itertools import combinations, product
import numpy as np

SQRT5=math.sqrt(5.0); TOL=2e-12
ICOSAHEDRAL_EDGES=((0,1),(0,5),(0,7),(0,8),(0,11),(1,2),(1,5),(1,6),(1,8),(2,3),(2,6),(2,8),(2,9),(3,4),(3,6),(3,9),(3,10),(4,5),(4,6),(4,10),(4,11),(5,6),(5,11),(7,8),(7,9),(7,10),(7,11),(8,9),(9,10),(10,11))

def adjacency(n,edges):
    a=np.zeros((n,n),dtype=np.float64)
    for i,j in edges: a[i,j]=a[j,i]=1.0
    return a

def tetrahedron(): return np.ones((4,4))-np.eye(4)

def cube():
    vs=list(product((0,1),repeat=3)); idx={v:i for i,v in enumerate(vs)}; edges=[]
    for i,v in enumerate(vs):
        for b in range(3):
            w=list(v); w[b]^=1; j=idx[tuple(w)]
            if i<j: edges.append((i,j))
    return adjacency(8,tuple(edges))

def octahedron():
    opp={0:1,1:0,2:3,3:2,4:5,5:4}
    return adjacency(6,tuple((i,j) for i in range(6) for j in range(i+1,6) if opp[i]!=j))

def icosahedron(): return adjacency(12,ICOSAHEDRAL_EDGES)

def dodecahedron():
    ai=icosahedron(); faces=[]
    for tri in combinations(range(12),3):
        if ai[tri[0],tri[1]] and ai[tri[0],tri[2]] and ai[tri[1],tri[2]]: faces.append(tri)
    assert len(faces)==20
    edges=[]
    for i,f in enumerate(faces):
        sf=set(f)
        for j in range(i+1,len(faces)):
            if len(sf.intersection(faces[j]))==2: edges.append((i,j))
    assert len(edges)==30
    return adjacency(20,tuple(edges))

def assert_spectrum(a,expected):
    assert np.allclose(np.sort(np.linalg.eigvalsh(a)),np.sort(np.asarray(expected,float)),rtol=0.0,atol=TOL)

def connected(a):
    seen={0}; stack=[0]
    while stack:
        i=stack.pop()
        for j in np.flatnonzero(a[i]):
            j=int(j)
            if j not in seen: seen.add(j); stack.append(j)
    return len(seen)==a.shape[0]

def ramanujan(a,bipartite=False):
    deg=a.sum(1); assert np.all(deg==deg[0]); k=int(deg[0]); eig=np.linalg.eigvalsh(a); vals=[]
    for x in eig:
        if abs(float(x)-k)<=TOL: continue
        if bipartite and abs(float(x)+k)<=TOL: continue
        vals.append(float(x))
    rho=max(abs(x) for x in vals); bound=2.0*math.sqrt(k-1.0)
    return {"vertices":int(a.shape[0]),"degree":k,"rho_nontrivial":rho,"ramanujan_bound":bound,"is_ramanujan":bool(rho<=bound+TOL)}

def carrier36():
    k3=np.ones((3,3))-np.eye(3)
    return np.kron(icosahedron(),np.eye(3))+np.kron(np.eye(12),k3)

def main():
    platonic={
      "tetrahedron":(tetrahedron(),[3.0]+[-1.0]*3,False),
      "cube":(cube(),[3.0]+[1.0]*3+[-1.0]*3+[-3.0],True),
      "octahedron":(octahedron(),[4.0]+[0.0]*3+[-2.0]*2,False),
      "dodecahedron":(dodecahedron(),[3.0]+[SQRT5]*3+[1.0]*5+[0.0]*4+[-2.0]*4+[-SQRT5]*3,False),
      "icosahedron":(icosahedron(),[5.0]+[SQRT5]*3+[-1.0]*5+[-SQRT5]*3,False),
    }
    pm={}
    for name,(a,expected,bip) in platonic.items():
        assert np.array_equal(a,a.T); assert np.all(np.diag(a)==0); assert connected(a); assert_spectrum(a,expected)
        pm[name]=ramanujan(a,bip); assert pm[name]["is_ramanujan"]
    g=carrier36(); assert g.shape==(36,36); assert np.array_equal(g,g.T); assert connected(g); assert np.all(g.sum(1)==7); assert int(g.sum()//2)==126
    expected=[7.0]+[2+SQRT5]*3+[4.0]*2+[SQRT5-1]*6+[1.0]*5+[2-SQRT5]*3+[-2.0]*10+[-1-SQRT5]*6
    assert_spectrum(g,expected); gm=ramanujan(g); assert gm["is_ramanujan"]
    assert math.isclose(gm["rho_nontrivial"],2+SQRT5,rel_tol=0.0,abs_tol=TOL)
    gap=(5-SQRT5)/7; assert 1-(2+SQRT5)/7==gap
    assert 2+5==7 and int(g.sum(1)[0])==7
    out={"schema":"TIR_PLATONIC_RAMANUJAN_SPECTRAL_CARRIER_VALIDATION_V0_1","status":"PASS","claim_scope":"EXACT_GRAPH_SPECTRAL_FACTS_PLUS_TIR_CANDIDATE_CARRIER","platonic_graphs":pm,"carrier36":{**gm,"edge_count":126,"rho_exact":"2+sqrt(5)","normalized_laplacian_gap":gap,"normalized_laplacian_gap_exact":"(5-sqrt(5))/7","degree_identity":"7 = L3 = L4+L5 = 2+5","factorization":"I12 square K3"},"stability_statement":{"scope":"LOCAL_LINEARIZATION_ONLY","mean_zero_decay_rate_lower_bound":"beta*(5-sqrt(5))/7","global_nonlinear_stability_claim":False},"physical_claim":False}
    print(json.dumps(out,sort_keys=True,indent=2)); return 0

if __name__=="__main__": raise SystemExit(main())
