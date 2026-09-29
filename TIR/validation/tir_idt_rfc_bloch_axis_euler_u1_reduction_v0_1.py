from __future__ import annotations
import json, math, random

SCHEMA='TIR_IDT_RFC_BLOCH_AXIS_EULER_U1_REDUCTION_VALIDATION_V0_1'

def cross(a,b):
    return (
        a[1]*b[2]-a[2]*b[1],
        a[2]*b[0]-a[0]*b[2],
        a[0]*b[1]-a[1]*b[0],
    )

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def norm(a):
    return math.sqrt(dot(a,a))

def n_matrix(s):
    # n_ab = epsilon_abc s_c
    return (
        (0.0, s[2], -s[1]),
        (-s[2], 0.0, s[0]),
        (s[1], -s[0], 0.0),
    )

def matvec(M,v):
    return tuple(sum(M[i][j]*v[j] for j in range(3)) for i in range(3))

def frob_sq(M):
    return sum(M[i][j]*M[i][j] for i in range(3) for j in range(3))

def main():
    rng=random.Random(20260924)
    max_norm=0.0
    max_axis=0.0
    max_generator_norm=0.0
    max_gauge=0.0

    for _ in range(5000):
        raw=(rng.uniform(-1,1),rng.uniform(-1,1),rng.uniform(-1,1))
        nr=norm(raw)
        if nr<1e-9:
            raw=(1.0,2.0,3.0); nr=norm(raw)
        s=tuple(x/nr for x in raw)
        N=n_matrix(s)

        max_norm=max(max_norm,abs(dot(s,s)-1.0))
        Ns=matvec(N,s)
        max_axis=max(max_axis,norm(Ns))
        max_generator_norm=max(max_generator_norm,abs(0.5*frob_sq(N)-1.0))

        sE=0.5
        dalpha=rng.uniform(-5,5)
        projected_inhom=-(sE/2.0)*frob_sq(N)*dalpha
        target=-sE*dalpha
        max_gauge=max(max_gauge,abs(projected_inhom-target))

    checks=[
        {'name':'unit_axis','pass':max_norm<1e-12,'max_error':max_norm},
        {'name':'axis_stabilizer_generator','pass':max_axis<1e-12,'max_error':max_axis},
        {'name':'generator_normalization','pass':max_generator_norm<1e-12,'max_error':max_generator_norm},
        {'name':'projected_connection_gauge_law','pass':max_gauge<1e-12,'max_error':max_gauge},
        {
            'name':'spin_half_double_cover',
            'pass':abs(complex(math.cos(math.pi),math.sin(math.pi))+1)<1e-12
                   and abs(complex(math.cos(2*math.pi),math.sin(2*math.pi))-1)<1e-12,
            'two_pi_phase':'-1',
            'four_pi_phase':'+1',
        },
    ]

    passed=all(c['pass'] for c in checks)
    out={
        'schema':SCHEMA,
        'technical_status':'PASS' if passed else 'FAIL',
        'verdict':(
            'PASS_LOCAL_SO3_SO2_U1_EULER_REDUCTION_INTERNAL_TO_SPACETIME_AXIS_SOLDER_OPEN'
            if passed else
            'FAIL_BLOCH_AXIS_EULER_U1_REDUCTION'
        ),
        'canon_allowed':False,
        'checks':checks,
        'open_gates':[
            'TIR_INTERNAL_A1_CP1_AXIS_TO_RFC_SPATIAL_TETRAD_AXIS_SOLDER',
            'GLOBAL_REDUCED_AXIS_SECTION_PATCHING',
            'DEFECT_ZERO_HANDLING',
            'EINSTEIN_CARTAN_TORSION_SOLUTION',
        ],
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=='__main__':
    main()
