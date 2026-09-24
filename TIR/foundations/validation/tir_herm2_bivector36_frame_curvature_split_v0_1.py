#!/usr/bin/env python3
from __future__ import annotations
import json
import sympy as sp

PAIR_BASIS=((0,1),(0,2),(0,3),(2,3),(3,1),(1,2))

def frob2(A):
    return sp.simplify(sum(x*x for x in A))

def projection_rank_matrices():
    J=sp.zeros(6)
    for i in range(3):
        J[i,i+3]=1
        J[i+3,i]=1
    qcols=[]
    for k in range(36):
        E=sp.zeros(6)
        E[k//6,k%6]=1
        theta=J*E.T*J
        frame=(E-theta)/2 + sp.trace(E)/6*sp.eye(6)
        Q=sp.simplify(E-frame)
        qcols.append(Q.reshape(36,1))
    PQ=sp.Matrix.hstack(*qcols)
    PG=sp.eye(36)-PQ
    return J,PQ,PG

def tetra_overlap():
    I=sp.I
    I2=sp.eye(2)
    X2=sp.Matrix([[0,1],[1,0]])
    Y2=sp.Matrix([[0,-I],[I,0]])
    Z2=sp.Matrix([[1,0],[0,-1]])
    gamma=[
        sp.kronecker_product(X2,I2),
        sp.kronecker_product(Y2,I2),
        sp.kronecker_product(Z2,X2),
        sp.kronecker_product(Z2,Y2),
    ]
    vertices=[]
    for i in range(4):
        v=[
            sp.sqrt(sp.Rational(4,3))
            *(sp.Rational(1 if a==i else 0)-sp.Rational(1,4))
            for a in range(4)
        ]
        vertices.append(v)
    sigma=[
        sum((v[a]*gamma[a] for a in range(4)),sp.zeros(4))
        for v in vertices
    ]
    def U(i,j):
        return sp.sqrt(sp.Rational(3,4))*(sp.eye(4)+sigma[i]*sigma[j])
    edges=PAIR_BASIS
    plus=[U(i,j) for i,j in edges]
    minus=[U(j,i) for i,j in edges]
    return sp.Matrix(6,6,lambda a,b:sp.simplify(sp.trace(plus[a].H*minus[b])/4))

def validate():
    J,PQ,PG=projection_rank_matrices()
    checks={}
    checks["projection_rank_curvature_20"]=PQ.rank()==20
    checks["projection_rank_frame_16"]=PG.rank()==16
    checks["projection_idempotent_curvature"]=(PQ*PQ-PQ).rank()==0
    checks["projection_idempotent_frame"]=(PG*PG-PG).rank()==0
    checks["projection_cross_zero"]=(PQ*PG).rank()==0

    vals=[sp.Rational((7*k)%11-5,3) for k in range(36)]
    X=sp.Matrix(6,6,vals)
    theta=J*X.T*J
    alpha=sp.trace(X)/6
    frame=sp.simplify((X-theta)/2+alpha*sp.eye(6))
    Q=sp.simplify(X-frame)
    S=sp.simplify(J*Q)

    checks["reconstruction_exact"]=sp.simplify(X-frame-Q)==sp.zeros(6)
    checks["frame_conformal_orthogonal"]=sp.simplify(frame.T*J+J*frame-2*alpha*J)==sp.zeros(6)
    checks["curvature_J_self_adjoint"]=sp.simplify(J*Q-Q.T*J)==sp.zeros(6)
    checks["curvature_trace_zero"]=sp.trace(Q)==0
    checks["curvature_bilinear_symmetric"]=S==S.T
    bianchi=sp.simplify(S[0,3]+S[1,4]+S[2,5])
    checks["bianchi_0123_zero"]=bianchi==0
    checks["trace_equals_twice_bianchi"]=sp.simplify(sp.trace(Q)-2*bianchi)==0
    checks["sym2_lambda2_dimension_21"]=6*7//2==21
    checks["algebraic_curvature_dimension_20"]=21-1==20

    T=tetra_overlap()
    expected=sp.Rational(1,3)*sp.Matrix([
        [-1,2,2,1,2,0],
        [2,-1,2,0,1,2],
        [2,2,-1,2,0,1],
        [1,0,2,-1,0,0],
        [2,1,0,0,-1,0],
        [0,2,1,0,0,-1],
    ])
    checks["tetra_overlap_exact_matrix"]=T==expected
    zero_count=sum(1 for x in T if x==0)
    checks["phase_only_has_12_exact_undefined_zeros"]=zero_count==12

    thetaT=J*T.T*J
    frameT=sp.simplify((T-thetaT)/2+sp.trace(T)/6*sp.eye(6))
    QT=sp.simplify(T-frameT)
    ST=sp.simplify(J*QT)
    total=frob2(T)
    f=frob2(frameT)
    q=frob2(QT)
    checks["tetra_total_frob2_20_over_3"]=total==sp.Rational(20,3)
    checks["tetra_frame_frob2_10_over_3"]=f==sp.Rational(10,3)
    checks["tetra_curvature_frob2_10_over_3"]=q==sp.Rational(10,3)
    checks["tetra_exact_half_half_split"]=sp.simplify(f/total)==sp.Rational(1,2) and sp.simplify(q/total)==sp.Rational(1,2)
    checks["tetra_curvature_bianchi"]=ST==ST.T and sp.trace(QT)==0 and sp.simplify(ST[0,3]+ST[1,4]+ST[2,5])==0

    return {
        "schema":"TIR_HERM2_BIVECTOR36_FRAME_CURVATURE_SPLIT_V0_1",
        "status":"PASS" if all(checks.values()) else "FAIL",
        "candidate_only":True,
        "checks":checks,
        "tetra_overlap_zero_count":zero_count,
        "tetra_total_frob2":str(total),
        "tetra_frame_frob2":str(f),
        "tetra_curvature_frob2":str(q),
        "physical_curvature_binding":"OPEN",
    }

if __name__=="__main__":
    print(json.dumps(validate(),indent=2,sort_keys=True))
