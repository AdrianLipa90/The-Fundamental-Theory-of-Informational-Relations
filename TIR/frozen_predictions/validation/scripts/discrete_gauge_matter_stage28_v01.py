#!/usr/bin/env python3
from __future__ import annotations
import json
import numpy as np

l1=np.array([[0,1,0],[1,0,0],[0,0,0]],complex)
l2=np.array([[0,-1j,0],[1j,0,0],[0,0,0]],complex)
l3=np.array([[1,0,0],[0,-1,0],[0,0,0]],complex)
l4=np.array([[0,0,1],[0,0,0],[1,0,0]],complex)
l5=np.array([[0,0,-1j],[0,0,0],[1j,0,0]],complex)
l6=np.array([[0,0,0],[0,0,1],[0,1,0]],complex)
l7=np.array([[0,0,0],[0,0,-1j],[0,1j,0]],complex)
l8=np.array([[1,0,0],[0,1,0],[0,0,-2]],complex)/np.sqrt(3.0)

def su3_exp(H):
    vals, vecs=np.linalg.eigh(H)
    return vecs @ np.diag(np.exp(1j*vals)) @ vecs.conj().T

W01=su3_exp(0.19*l1+0.11*l4-0.07*l7)
W12=su3_exp(-0.13*l2+0.17*l6+0.09*l8)
W20=su3_exp(0.23*l3-0.08*l5+0.12*l7)
G0=su3_exp(0.15*l1-0.10*l8)
G1=su3_exp(0.21*l2+0.05*l4)
G2=su3_exp(-0.18*l3+0.14*l6)
Ws={(0,1):W01,(1,2):W12,(2,0):W20}
Gs=[G0,G1,G2]

base=np.array([
 [[1+.1j,.2-.3j,-.4+.2j],[.3+.2j,.7-.1j,.2+.4j],[-.2+.5j,.3+.1j,.8-.2j]],
 [[.6-.1j,-.4+.3j,.1+.2j],[.2+.1j,.5+.4j,-.3+.2j],[.7+.2j,-.1+.3j,.2-.4j]],
 [[.4+.4j,.1-.2j,.6+.1j],[-.3+.2j,.8-.1j,.1+.1j],[.5-.2j,.2+.4j,-.4+.3j]]
],complex)
q=base/np.linalg.norm(base,axis=2,keepdims=True)

def action(Ws,q,beta=1.37,eta=.83):
    U=Ws[(0,1)]@Ws[(1,2)]@Ws[(2,0)]
    gauge=beta*(3-np.trace(U).real)
    matter=0.0
    for (i,j),W in Ws.items():
        for f in range(3):
            matter+=float(np.real(q[i,f].conj()@W@q[j,f]))
    return gauge-eta*matter, gauge, matter

S0=action(Ws,q)
Wst={(i,j):Gs[i]@W@Gs[j].conj().T for (i,j),W in Ws.items()}
qt=np.empty_like(q)
for i in range(3):
    for f in range(3):
        qt[i,f]=Gs[i]@q[i,f]
S1=action(Wst,qt)
res=[float(abs(a-b)) for a,b in zip(S0,S1)]
checks={
    "full_action_invariant":res[0]<1e-12,
    "wilson_term_invariant":res[1]<1e-12,
    "matter_term_invariant":res[2]<1e-12,
}
report={
    "schema":"tir.polygonal.stage28.discrete-gauge-matter/v0.1",
    "status":"PASS" if all(checks.values()) else "FAIL",
    "checks":checks,
    "full_action_residual":res[0],
    "wilson_term_residual":res[1],
    "matter_term_residual":res[2],
    "family_copies":3,
    "scope":"discrete locally gauge-invariant color-plus-quark action form"
}
print(json.dumps(report,indent=2,sort_keys=True))
raise SystemExit(0 if report["status"]=="PASS" else 1)
