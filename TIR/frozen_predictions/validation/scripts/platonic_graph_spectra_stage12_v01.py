#!/usr/bin/env python3
from __future__ import annotations
import json, math
import numpy as np

TOL=1e-10

def octahedron_vertices():
    return np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],dtype=float)

def icosahedron_vertices():
    phi=(1+math.sqrt(5))/2
    pts=[]
    for a in (-1.0,1.0):
        for b in (-phi,phi):
            pts += [(0.0,a,b),(a,b,0.0),(b,0.0,a)]
    V=np.unique(np.asarray(pts,float),axis=0)
    return V/np.linalg.norm(V[0])

def edge_adjacency(V):
    D=np.linalg.norm(V[:,None,:]-V[None,:,:],axis=-1)
    dmin=float(D[D>TOL].min())
    A=((D>TOL)&(np.abs(D-dmin)<1e-9)).astype(float)
    return A,dmin

def spectral_row(V, expected_degree, expected_sorted):
    A,d=edge_adjacency(V)
    ev=np.linalg.eigvalsh(A)
    target=np.array(sorted(expected_sorted),float)
    L=expected_degree*np.eye(len(V))-A
    lev=np.linalg.eigvalsh(L)
    H=A/expected_degree
    hev=np.linalg.eigvalsh(H)
    return {
      'vertices':len(V),
      'edge_length':d,
      'degree_sequence':A.sum(axis=1).astype(int).tolist(),
      'adjacency_eigenvalues':ev.tolist(),
      'adjacency_target_residual':float(np.max(np.abs(ev-target))),
      'laplacian_eigenvalues':lev.tolist(),
      'normalized_exchange_eigenvalues':hev.tolist(),
      'hermiticity_error':float(np.max(np.abs(H-H.T))),
      'spectral_radius_normalized_exchange':float(np.max(np.abs(hev))),
    }

def main():
    sq5=math.sqrt(5)
    r4=spectral_row(octahedron_vertices(),4,[-2,-2,0,0,0,4])
    r5=spectral_row(icosahedron_vertices(),5,[-sq5,-sq5,-sq5,-1,-1,-1,-1,-1,sq5,sq5,sq5,5])
    checks={
      'N4_degree_4': all(x==4 for x in r4['degree_sequence']),
      'N5_degree_5': all(x==5 for x in r5['degree_sequence']),
      'N4_spectrum_exact': r4['adjacency_target_residual']<TOL,
      'N5_spectrum_exact': r5['adjacency_target_residual']<TOL,
      'N4_normalized_exchange_unit_spectral_radius': abs(r4['spectral_radius_normalized_exchange']-1)<TOL,
      'N5_normalized_exchange_unit_spectral_radius': abs(r5['spectral_radius_normalized_exchange']-1)<TOL,
    }
    out={
      'schema':'TIR-PLATONIC-GRAPH-SPECTRA/0.1',
      'scope':'pure geometry and graph spectral mathematics',
      'N4_octahedron':r4,
      'N5_icosahedron':r5,
      'characteristic_polynomials':{
        'N4':'lambda^3 (lambda - 4) (lambda + 2)^2',
        'N5':'(lambda - 5) (lambda + 1)^5 (lambda^2 - 5)^3'
      },
      'canonical_exchange_normalization':{
        'N4':'H4=A4/4',
        'N5':'H5=A5/5',
        'reason':'regular-graph spectral radius equals degree for these connected positive adjacency matrices'
      },
      'checks':checks,
      'verdict':'PASS' if all(checks.values()) else 'FAIL'
    }
    print(json.dumps(out,indent=2))
    return 0 if out['verdict']=='PASS' else 1

if __name__=='__main__':
    raise SystemExit(main())
