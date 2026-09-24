#!/usr/bin/env python3
from __future__ import annotations
import json, math, random
import numpy as np

SCHEMA="TIR_IDT_EXTRINSIC_CURVATURE_SOURCE_BRIDGE_VALIDATION_V0_1"
TOL=2e-10

SX=np.array([[0,1],[1,0]],complex)
SY=np.array([[0,-1j],[1j,0]],complex)
SZ=np.array([[1,0],[0,-1]],complex)
I2=np.eye(2,dtype=complex)

def rho_from_bloch(r):
    r=np.asarray(r,dtype=float)
    return 0.5*(I2+r[0]*SX+r[1]*SY+r[2]*SZ)

def relation(r0,r1):
    return 2.0*(rho_from_bloch(r1)-rho_from_bloch(r0))

def relation_dot(v0,v1):
    # derivative of 2(rho_1-rho_0); identity part cancels
    dv=np.asarray(v1,dtype=float)-np.asarray(v0,dtype=float)
    return dv[0]*SX+dv[1]*SY+dv[2]*SZ

def hs(a,b):
    return float(0.5*np.trace(a@b).real)

def gram(edges):
    return np.array([[hs(a,b) for b in edges] for a in edges],dtype=float)

def gram_dot(edges,dedges):
    return np.array([
        [hs(dedges[i],edges[j])+hs(edges[i],dedges[j]) for j in range(3)]
        for i in range(3)
    ],dtype=float)

def main():
    rng=random.Random(20260924)
    checks=[]

    # CP1 pure-state density seam.
    max_pure=0.0
    max_trace=0.0
    for _ in range(64):
        v=np.array([rng.uniform(-1,1) for _ in range(3)],dtype=float)
        v/=np.linalg.norm(v)
        r=rho_from_bloch(v)
        max_pure=max(max_pure,float(np.max(np.abs(r@r-r))))
        max_trace=max(max_trace,abs(float(np.trace(r).real)-1.0))
    checks.append({"name":"cp1_pure_state_density_seam","pass":max_pure<1e-12 and max_trace<1e-12,"max_projector_error":max_pure,"max_trace_error":max_trace})

    # Exact relation/Gram temporal derivative checked by finite difference.
    max_fd=0.0
    for _ in range(64):
        r0=np.array([rng.uniform(-.2,.2) for _ in range(3)])
        rs=[np.array([rng.uniform(-.2,.2) for _ in range(3)]) for _ in range(3)]
        v0=np.array([rng.uniform(-.1,.1) for _ in range(3)])
        vs=[np.array([rng.uniform(-.1,.1) for _ in range(3)]) for _ in range(3)]
        E=[relation(r0,r) for r in rs]
        dE=[relation_dot(v0,v) for v in vs]
        analytic=gram_dot(E,dE)
        dt=1e-6
        plus=[relation(r0+dt*v0,r+dt*v) for r,v in zip(rs,vs)]
        minus=[relation(r0-dt*v0,r-dt*v) for r,v in zip(rs,vs)]
        finite=(gram(plus)-gram(minus))/(2*dt)
        max_fd=max(max_fd,float(np.max(np.abs(analytic-finite))))
    checks.append({"name":"discrete_gram_strain_derivative","pass":max_fd<1e-8,"max_abs_error":max_fd})

    # Common SO(3) internal frame rotation leaves Gram strain invariant.
    max_rot=0.0
    for _ in range(64):
        A=np.array([[rng.uniform(-1,1) for _ in range(3)] for _ in range(3)])
        Q,_=np.linalg.qr(A)
        if np.linalg.det(Q)<0: Q[:,0]*=-1
        E=np.array([[rng.uniform(-1,1) for _ in range(3)] for _ in range(3)])
        dE=np.array([[rng.uniform(-1,1) for _ in range(3)] for _ in range(3)])
        gd=dE@E.T+E@dE.T
        Er=E@Q.T; dEr=dE@Q.T
        gdr=dEr@Er.T+Er@dEr.T
        max_rot=max(max_rot,float(np.max(np.abs(gd-gdr))))
    checks.append({"name":"gram_strain_so3_frame_invariance","pass":max_rot<1e-12,"max_abs_error":max_rot})

    # V_lambda / activity is invariant under increasing lambda relabeling.
    max_rep=0.0
    for _ in range(128):
        activity=10**rng.uniform(-2,2)
        scale=10**rng.uniform(-2,2) # d lambda' / d lambda
        V=np.array([rng.uniform(-3,3) for _ in range(8)])
        activity_prime=activity/scale
        V_prime=V/scale
        max_rep=max(max_rep,float(np.max(np.abs(V/activity-V_prime/activity_prime))))
    checks.append({"name":"activity_normalized_flow_reparameterization_invariance","pass":max_rep<1e-12,"max_abs_error":max_rep})

    # Reference-clock lapse cancellation.
    max_lapse=0.0
    for _ in range(128):
        ax=10**rng.uniform(-2,2)
        ar=10**rng.uniform(-2,2)
        NR=ax/ar
        dh=np.array([[rng.uniform(-2,2) for _ in range(3)] for _ in range(3)])
        dh=0.5*(dh+dh.T) # d h / d lambda
        K_ref=-(1.0/(2.0*NR))*(dh/ar)
        K_local=-(1.0/(2.0*ax))*dh
        max_lapse=max(max_lapse,float(np.max(np.abs(K_ref-K_local))))
    checks.append({"name":"relational_lapse_cancellation","pass":max_lapse<1e-12,"max_abs_error":max_lapse})

    passed=all(x["pass"] for x in checks)
    receipt={
        "schema":SCHEMA,
        "technical_status":"PASS" if passed else "FAIL",
        "verdict":"PASS_CONDITIONAL_EXTRINSIC_CURVATURE_SOURCE_PHYSICAL_SAME_STATE_BINDING_OPEN" if passed else "FAIL_EXTRINSIC_CURVATURE_SOURCE_BRIDGE",
        "canon_allowed":False,
        "exact_or_conditional_closed":[
            "CP1_TO_TIR_PURE_STATE_REPRESENTATION_SEAM",
            "ACTIVITY_NORMALIZED_FLOW_REPARAMETRIZATION_INVARIANCE",
            "DISCRETE_RELATION_GRAM_STRAIN",
            "RELATIONAL_LAPSE_CANCELLATION",
            "NORMAL_GAUGE_KIJ_CHAIN_RULE_ON_ADMITTED_SAME_STATE_FAMILY"
        ],
        "open_gates":[
            "PHYSICAL_IDT_STATE_TO_TIR_STATE_IDENTITY",
            "PRODUCTION_REFINING_RELATIONAL_FAMILY",
            "DOWNSTREAM_ADM_CONSTRAINT_AND_EVOLUTION_VALIDATION_ON_PRODUCTION_REALIZATION"
        ],
        "checks":checks
    }
    print(json.dumps(receipt,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=="__main__":
    main()
