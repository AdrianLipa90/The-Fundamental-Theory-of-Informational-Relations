#!/usr/bin/env python3
from __future__ import annotations
import json, math
import numpy as np

TOL=1e-10

def tetrahedron_vertices():
    return np.array([
        [0.0,0.0,1.0],
        [2*math.sqrt(2)/3,0.0,-1/3],
        [-math.sqrt(2)/3,math.sqrt(6)/3,-1/3],
        [-math.sqrt(2)/3,-math.sqrt(6)/3,-1/3],
    ],float)

def octahedron_vertices():
    return np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],float)

def icosahedron_vertices():
    phi=(1+math.sqrt(5))/2
    pts=[]
    for a in (-1.0,1.0):
        for b in (-phi,phi):
            pts += [(0.0,a,b),(a,b,0.0),(b,0.0,a)]
    V=np.unique(np.asarray(pts,float),axis=0)
    return V/np.linalg.norm(V[0])

def adjacency(V):
    D=np.linalg.norm(V[:,None,:]-V[None,:,:],axis=-1)
    d=D[D>TOL].min()
    return ((D>TOL)&(np.abs(D-d)<1e-9)).astype(float)

def cN(N):
    q=2*math.pi/N
    return math.cos(q)/(1-math.cos(q))

def row(N,V):
    A=adjacency(V)
    d=int(round(float(A.sum(axis=1)[0])))
    c=cN(N)
    normalized=A/d
    residual=float(np.max(np.abs(normalized@V-c*V)))
    column_res=[float(np.max(np.abs(normalized@V[:,j]-c*V[:,j]))) for j in range(3)]
    vals=np.linalg.eigvalsh(normalized)
    multiplicity=int(np.count_nonzero(np.abs(vals-c)<1e-9))
    neighbour_dot=[]
    for i in range(len(V)):
        js=np.flatnonzero(A[i]>0.5)
        neighbour_dot.extend((V[js]@V[i]).tolist())
    return {
      'N':N,'vertices':len(V),'degree':d,'c_N':c,
      'coordinate_eigenvalue_residual':residual,
      'coordinate_column_residuals':column_res,
      'c_N_spectral_multiplicity':multiplicity,
      'coordinate_rank':int(np.linalg.matrix_rank(V)),
      'neighbour_dot_min':float(min(neighbour_dot)),
      'neighbour_dot_max':float(max(neighbour_dot)),
      'neighbour_dot_to_c_residual':float(max(abs(x-c) for x in neighbour_dot)),
    }

def main():
    rows={
      '3':row(3,tetrahedron_vertices()),
      '4':row(4,octahedron_vertices()),
      '5':row(5,icosahedron_vertices()),
    }
    checks={
      'all_coordinate_eigen_residuals_below_tol':all(r['coordinate_eigenvalue_residual']<TOL for r in rows.values()),
      'all_neighbour_dot_residuals_below_tol':all(r['neighbour_dot_to_c_residual']<TOL for r in rows.values()),
      'all_coordinate_subspaces_rank3':all(r['coordinate_rank']==3 for r in rows.values()),
      'c3_multiplicity3':rows['3']['c_N_spectral_multiplicity']==3,
      'c4_multiplicity3':rows['4']['c_N_spectral_multiplicity']==3,
      'c5_multiplicity3':rows['5']['c_N_spectral_multiplicity']==3,
    }
    out={
      'schema':'TIR-GEOMETRY-SPECTRUM-IDENTITY/0.1',
      'identity':'(A_N/N) X_N = c_N X_N for N=3,4,5',
      'rows':rows,
      'checks':checks,
      'verdict':'PASS' if all(checks.values()) else 'FAIL'
    }
    print(json.dumps(out,indent=2))
    return 0 if out['verdict']=='PASS' else 1

if __name__=='__main__':
    raise SystemExit(main())
