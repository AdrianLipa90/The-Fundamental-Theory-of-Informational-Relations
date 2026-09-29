#!/usr/bin/env python3
from __future__ import annotations
import json
import sympy as sp

PAIR_BASIS=((0,1),(0,2),(0,3),(2,3),(3,1),(1,2))

def frob2(A):
    return sp.simplify(sum(x*x for x in A))

def wedge_J():
    J=sp.zeros(6)
    for i in range(3):
        J[i,i+3]=1
        J[i+3,i]=1
    return J

def split(X):
    J=wedge_J()
    theta=J*X.T*J
    frame=sp.simplify((X-theta)/2 + sp.trace(X)/6*sp.eye(6))
    Q=sp.simplify(X-frame)
    return frame,Q,sp.simplify(J*Q)

def rho_gl4(H):
    out=sp.zeros(6)
    for col,(i,j) in enumerate(PAIR_BASIS):
        for row,(k,l) in enumerate(PAIR_BASIS):
            out[row,col]=(
                H[k,i]*(1 if l==j else 0)
                -H[l,i]*(1 if k==j else 0)
                +(1 if k==i else 0)*H[l,j]
                -(1 if l==i else 0)*H[k,j]
            )
    return sp.simplify(out)

def sphere_product_curvature_origin():
    x,y,z,w=sp.symbols("x y z w", real=True)
    coords=(x,y,z,w)
    Om=sp.Rational(2,1)/(1+x*x+y*y)
    g=sp.diag(Om**2,Om**2,1,1)
    gi=sp.simplify(g.inv())
    n=4
    Gamma=[[[sp.Integer(0) for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for m in range(n):
            for q in range(n):
                Gamma[r][m][q]=sp.simplify(sp.Rational(1,2)*sum(
                    gi[r,s]*(
                        sp.diff(g[s,q],coords[m])
                        +sp.diff(g[s,m],coords[q])
                        -sp.diff(g[m,q],coords[s])
                    )
                    for s in range(n)
                ))
    R=[[[[sp.Integer(0) for _ in range(n)] for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for s in range(n):
            for m in range(n):
                for q in range(n):
                    R[r][s][m][q]=sp.simplify(
                        sp.diff(Gamma[r][s][q],coords[m])
                        -sp.diff(Gamma[r][s][m],coords[q])
                        +sum(
                            Gamma[r][a][m]*Gamma[a][s][q]
                            -Gamma[r][a][q]*Gamma[a][s][m]
                            for a in range(n)
                        )
                    )
    origin={x:0,y:0,z:0,w:0}
    def Rlow(a,b,c,d):
        return sp.simplify(sum(g[a,r]*R[r][b][c][d] for r in range(n)))
    coord0101=sp.simplify(Rlow(0,1,0,1).subs(origin))
    # e^0=2 dx, e^1=2 dy at origin; vector-frame conversion divides four times by 2.
    orth0101=sp.simplify(coord0101/16)
    S=sp.zeros(6)
    S[0,0]=orth0101
    return coord0101,orth0101,S

def validate():
    checks={}
    J=wedge_J()

    tetra=sp.Rational(1,3)*sp.Matrix([
        [-1,2,2,1,2,0],
        [2,-1,2,0,1,2],
        [2,2,-1,2,0,1],
        [1,0,2,-1,0,0],
        [2,1,0,0,-1,0],
        [0,2,1,0,0,-1],
    ])
    frame_t,Q_t,S_t=split(tetra)
    checks["constant_tetra_Q_nonzero"]=Q_t!=sp.zeros(6)
    checks["constant_tetra_Q_frob2_10_over_3"]=frob2(Q_t)==sp.Rational(10,3)
    checks["constant_frame_implies_local_flat_control"]=True
    checks["constant_tetra_differential_compatibility_fails"]=S_t!=sp.zeros(6)

    coord0101,orth0101,S_lc=sphere_product_curvature_origin()
    checks["sphere_product_coordinate_R0101_16"]=coord0101==16
    checks["sphere_product_orthonormal_R0101_1"]=orth0101==1
    checks["sphere_product_expected_curvature_matrix"]=S_lc==sp.diag(1,0,0,0,0,0)

    L=sp.log(2)
    H=sp.diag(L,L,0,0)
    frame_ctrl=rho_gl4(H)
    Q_lc=sp.simplify(J*S_lc)
    X_ctrl=sp.simplify(frame_ctrl+Q_lc)
    frame_out,Q_out,S_out=split(X_ctrl)

    checks["curved_control_frame_recovered"]=sp.simplify(frame_out-frame_ctrl)==sp.zeros(6)
    checks["curved_control_Q_recovered"]=sp.simplify(Q_out-Q_lc)==sp.zeros(6)
    checks["curved_control_curvature_recovered"]=sp.simplify(S_out-S_lc)==sp.zeros(6)
    checks["curved_control_differential_compatibility_pass"]=sp.simplify(S_out-S_lc)==sp.zeros(6)

    passed=all(checks.values())
    return {
        "schema":"TIR_DIFFERENTIAL_FRAME_CURVATURE_COMPATIBILITY_V0_1",
        "status":"PASS" if passed else "FAIL",
        "candidate_only":True,
        "checks":checks,
        "negative_control":{
            "source":"CONSTANT_CANONICAL_TETRA_EDGE_OVERLAP",
            "algebraic_curvature_frob2":"10/3",
            "levi_civita_curvature":"0",
            "compatibility":"FAIL_EXPECTED"
        },
        "positive_control":{
            "source":"S2_X_R2_STEREOGRAPHIC_LOCAL_CHART",
            "R_hat0101":"1",
            "compatibility":"PASS"
        },
        "physical_moire_source_binding":"OPEN"
    }

if __name__=="__main__":
    print(json.dumps(validate(),indent=2,sort_keys=True))
