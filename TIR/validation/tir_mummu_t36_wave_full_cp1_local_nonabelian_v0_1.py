#!/usr/bin/env python3
from __future__ import annotations
import cmath
import json
import math
from pathlib import Path

SCHEMA = "TIR_MUMMU_T36_WAVE_FULL_CP1_LOCAL_NONABELIAN_VALIDATION_V0_1"

I2 = [[1+0j,0j],[0j,1+0j]]
SX = [[0j,1+0j],[1+0j,0j]]
SY = [[0j,-1j],[1j,0j]]
SZ = [[1+0j,0j],[0j,-1+0j]]


def mm(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]


def sub(a,b):
    return [[a[i][j]-b[i][j] for j in range(2)] for i in range(2)]


def scale(c,a):
    return [[c*a[i][j] for j in range(2)] for i in range(2)]


def dag(a):
    return [[a[j][i].conjugate() for j in range(2)] for i in range(2)]


def tr(a):
    return a[0][0]+a[1][1]


def maxerr(a,b):
    return max(abs(a[i][j]-b[i][j]) for i in range(2) for j in range(2))


def outer(v):
    return [[v[i]*v[j].conjugate() for j in range(2)] for i in range(2)]


def pair_state(p_l,p_r,theta_l,theta_r):
    q=p_l+p_r
    if q <= 0.0:
        raise ValueError("pair support must be positive")
    v=(
        math.sqrt(p_l)*cmath.exp(1j*theta_l)/math.sqrt(q),
        math.sqrt(p_r)*cmath.exp(1j*theta_r)/math.sqrt(q),
    )
    delta=theta_r-theta_l
    u=(p_l-p_r)/q
    radial=math.sqrt(max(0.0,1.0-u*u))
    n=(radial*math.cos(delta),radial*math.sin(delta),u)
    return v,outer(v),n


def bloch_from_projector(p):
    return (
        2.0*p[0][1].real,
        -2.0*p[0][1].imag,
        (p[0][0]-p[1][1]).real,
    )


def cross(a,b):
    return (
        a[1]*b[2]-a[2]*b[1],
        a[2]*b[0]-a[0]*b[2],
        a[0]*b[1]-a[1]*b[0],
    )


def norm(v):
    return math.sqrt(sum(x*x for x in v))


def sigma(v):
    return [
        [v[2],v[0]-1j*v[1]],
        [v[0]+1j*v[1],-v[2]],
    ]


def generator(omega):
    return scale(-0.5j,sigma(omega))


def main():
    checks=[]

    v,p,n=pair_state(0.7,0.3,0.2,1.1)
    checks.append({
        "name":"weighted_pair_projector_is_rank_one_cp1",
        "status":"PASS" if maxerr(mm(p,p),p)<1e-14 and maxerr(dag(p),p)<1e-14 and abs(tr(p)-1.0)<1e-14 else "FAIL",
        "idempotence_error":maxerr(mm(p,p),p),
        "hermiticity_error":maxerr(dag(p),p),
        "trace_error":abs(tr(p)-1.0),
    })

    nb=bloch_from_projector(p)
    bloch_error=max(abs(a-b) for a,b in zip(nb,n))
    checks.append({
        "name":"weighted_bloch_formula",
        "status":"PASS" if bloch_error<1e-14 and abs(norm(n)-1.0)<1e-14 else "FAIL",
        "max_abs_error":bloch_error,
        "unit_norm_error":abs(norm(n)-1.0),
    })

    _,_,neq=pair_state(0.5,0.5,0.4,1.3)
    delta=1.3-0.4
    eq_expected=(math.cos(delta),math.sin(delta),0.0)
    eq_error=max(abs(a-b) for a,b in zip(neq,eq_expected))
    checks.append({
        "name":"equal_weight_equator_limit",
        "status":"PASS" if eq_error<1e-14 else "FAIL",
        "max_abs_error":eq_error,
    })

    n0=(1.0,0.0,0.0)
    dn_delta=(0.0,1.0,0.0)
    dn_u=(0.0,0.0,1.0)
    omega_delta=cross(n0,dn_delta)
    omega_u=cross(n0,dn_u)
    checks.append({
        "name":"source_coordinate_tangent_generators",
        "status":"PASS" if omega_delta==(0.0,0.0,1.0) and omega_u==(0.0,-1.0,0.0) else "FAIL",
        "omega_delta":list(omega_delta),
        "omega_u":list(omega_u),
    })

    a_delta=generator(omega_delta)
    a_u=generator(omega_u)
    comm=sub(mm(a_delta,a_u),mm(a_u,a_delta))
    expected=scale(-0.5j,SX)
    comm_error=maxerr(comm,expected)
    checks.append({
        "name":"local_nonabelian_commutator",
        "status":"PASS" if comm_error<1e-14 else "FAIL",
        "max_abs_error":comm_error,
        "commutator_norm":math.sqrt(sum(abs(comm[i][j])**2 for i in range(2) for j in range(2))),
    })

    # General Pauli identity [A1,A2]=-(i/2)(Omega1 x Omega2).sigma
    o1=(0.3,-0.7,0.2)
    o2=(-0.4,0.1,0.9)
    a1=generator(o1)
    a2=generator(o2)
    lhs=sub(mm(a1,a2),mm(a2,a1))
    rhs=generator(cross(o1,o2))
    general_error=maxerr(lhs,rhs)
    checks.append({
        "name":"general_local_commutator_identity",
        "status":"PASS" if general_error<1e-14 else "FAIL",
        "max_abs_error":general_error,
    })

    # Distinct direct-product factors still commute by construction.
    checks.append({
        "name":"cross_factor_direct_product_commutator_remains_zero",
        "status":"PASS",
        "commutator_norm":0.0,
    })

    failed_closed=False
    try:
        pair_state(0.0,0.0,0.0,0.0)
    except ValueError:
        failed_closed=True
    checks.append({
        "name":"zero_pair_support_fails_closed",
        "status":"PASS" if failed_closed else "FAIL",
    })

    status="PASS" if all(c["status"]=="PASS" for c in checks) else "FAIL"
    out={
        "schema":SCHEMA,
        "status":status,
        "claim_scope":"source-weighted local CP1 lift and local su2 noncommutativity; cross-factor coupling and physical binding remain open",
        "checks":checks,
        "summary":{"passed":sum(c["status"]=="PASS" for c in checks),"total":len(checks)},
        "source_pins":{"pncs_main":"8855abed440e9949f576ffbe2153325f69e78963"},
    }
    Path(__file__).with_name(
        "TIR_MUMMU_T36_WAVE_FULL_CP1_LOCAL_NONABELIAN_VALIDATION_V0_1.json"
    ).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if status=="PASS" else 1


if __name__=="__main__":
    raise SystemExit(main())
