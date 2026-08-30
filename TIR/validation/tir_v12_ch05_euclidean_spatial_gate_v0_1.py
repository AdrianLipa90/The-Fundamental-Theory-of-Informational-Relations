#!/usr/bin/env python3
"""Deterministic v12 audit for Chapter 5 Euclidean/spatial gate."""
from __future__ import annotations
import json, math

I=((1+0j,0j),(0j,1+0j))
SX=((0j,1+0j),(1+0j,0j))
SY=((0j,-1j),(1j,0j))
SZ=((1+0j,0j),(0j,-1+0j))
PAULI=(SX,SY,SZ)

def mm(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def tr(a): return a[0][0]+a[1][1]
def hs(a,b): return 0.5*tr(mm(a,b))
def add(a,b): return tuple(tuple(a[i][j]+b[i][j] for j in range(2)) for i in range(2))
def scale(c,a): return tuple(tuple(c*a[i][j] for j in range(2)) for i in range(2))
def eq(a,b,tol=1e-12): return all(abs(a[i][j]-b[i][j])<tol for i in range(2) for j in range(2))

gram=[[hs(PAULI[i],PAULI[j]) for j in range(3)] for i in range(3)]
pauli_orthonormal=all(abs(gram[i][j]-(1 if i==j else 0))<1e-12 for i in range(3) for j in range(3))
pauli_traceless=all(abs(tr(s))<1e-12 for s in PAULI)

def rho(r):
    out=scale(0.5,I)
    for c,s in zip(r,PAULI): out=add(out,scale(0.5*c,s))
    return out

def sub(a,b): return add(a,scale(-1,b))
rx=rho((0.2,-0.1,0.3)); ry=rho((-0.4,0.2,0.1)); rz=rho((0.1,0.25,-0.2))
Exy=scale(2,sub(ry,rx)); Eyz=scale(2,sub(rz,ry)); Exz=scale(2,sub(rz,rx))
endpoint_composition=eq(add(Exy,Eyz),Exz)
reversal=eq(scale(-1,Exy),scale(2,sub(rx,ry)))
endpoint_traceless=abs(tr(Exy))<1e-12

A=scale(2.0,SX); B=scale(3.0,SY)
orthogonal=abs(hs(A,B))<1e-12
pythagorean=abs(hs(add(A,B),add(A,B))-(hs(A,A)+hs(B,B)))<1e-12

n=(1/math.sqrt(3),)*3
Ns=((0j,0j),(0j,0j))
for c,s in zip(n,PAULI): Ns=add(Ns,scale(c,s))
unit_square=eq(mm(Ns,Ns),I,1e-12)

checks={
 "herm0_real_basis_dimension_3": len(PAULI)==3 and pauli_traceless,
 "pauli_hs_orthonormal": pauli_orthonormal,
 "canonical_endpoint_composition": endpoint_composition,
 "canonical_reversal": reversal,
 "endpoint_relation_traceless": endpoint_traceless,
 "pythagorean_from_hs_metric": orthogonal and pythagorean,
 "unit_generator_squares_to_identity": unit_square,
}
passed=all(checks.values())
payload={
 "schema":"TIR_V12_CH05_EUCLIDEAN_SPATIAL_GATE_V0_1",
 "technical_status":"PASS" if passed else "FAIL",
 "carrier":"Herm_0(2) ~= R^3",
 "metric":"<A,B>=Tr(AB)/2",
 "rank_stabilization_theorem":"nonzero full-SO(3)-invariant local span => rank 3",
 "continuum_gate":"regular solder/coframe refinement",
 "checks":checks,
}
print(json.dumps(payload,indent=2,sort_keys=True))
raise SystemExit(0 if passed else 1)
