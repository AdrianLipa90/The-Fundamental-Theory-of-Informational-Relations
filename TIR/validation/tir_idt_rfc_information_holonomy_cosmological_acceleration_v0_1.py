from __future__ import annotations
import json, math, random
import numpy as np

SCHEMA='TIR_IDT_RFC_INFORMATION_HOLONOMY_COSMOLOGICAL_ACCELERATION_VALIDATION_V0_1'

def event_accel(xs, hs):
    x0,x1,x2=map(float,xs)
    d=x1-x0
    if not math.isclose(x2-x1,d,rel_tol=0,abs_tol=1e-14) or d<=0:
        raise ValueError('equal positive spacing required')
    y=[]
    for h in hs:
        a=np.asarray(h,dtype=float)
        if a.shape!=(3,3) or not np.allclose(a,a.T,atol=1e-12,rtol=0):
            raise ValueError('symmetric 3x3 h required')
        sign,ld=np.linalg.slogdet(a)
        if sign<=0:
            raise ValueError('SPD determinant required')
        y.append(ld/6.0)
    yp=(y[2]-y[0])/(2*d)
    ypp=(y[2]-2*y[1]+y[0])/(d*d)
    return ypp+yp*yp

def main():
    checks=[]
    rng=random.Random(20260924)

    max_hdot=0.0
    max_acc=0.0
    for _ in range(128):
        k=10**rng.uniform(-2,1)
        rho=10**rng.uniform(-3,1)
        p=rng.uniform(-1.2,1.2)*rho
        H=math.sqrt(k*rho/3.0)
        Hp=-3*H*H + 0.5*k*(rho-p)
        acc=Hp+H*H
        target=-k*(rho+3*p)/6.0
        max_acc=max(max_acc,abs(acc-target))
        lhs=-(Hp+2*H*H)
        rhs=H*H + 0.5*k*(p-rho)
        max_hdot=max(max_hdot,abs(lhs-rhs))
    checks.append({
        'name':'rf_e13_flat_flrw_reduction',
        'pass':max(max_hdot,max_acc)<1e-12,
        'max_k_evolution_error':max_hdot,
        'max_acceleration_error':max_acc,
    })

    max_info=0.0
    mismatches=0
    for _ in range(256):
        k=10**rng.uniform(-2,1)
        alpha=10**rng.uniform(-3,1)
        X=10**rng.uniform(-4,1)
        Xp=rng.uniform(-3,3)*X
        phip2=Xp*Xp/(2*X)
        U=alpha*X/k
        rhoI=0.5*phip2+U
        pI=0.5*phip2-U
        acc1=-k*(rhoI+3*pI)/6.0
        acc2=alpha*X/3.0-k*Xp*Xp/(6*X)
        max_info=max(max_info,abs(acc1-acc2))
        crit=(abs(Xp/X) < math.sqrt(2*alpha/k))
        if (acc1>0) != crit and abs(acc1)>1e-13:
            mismatches+=1
    checks.append({
        'name':'information_scalar_acceleration_criterion',
        'pass':max_info<1e-12 and mismatches==0,
        'max_error':max_info,
        'sign_mismatches':mismatches,
    })

    max_split=0.0
    for _ in range(256):
        k=10**rng.uniform(-2,1)
        phip=rng.uniform(-3,3)
        U=10**rng.uniform(-4,1)
        K=0.5*phip*phip
        acc_full=-k*((K+U)+3*(K-U))/6.0
        Lambda=k*U
        acc_split=-k*(K+3*K)/6.0+Lambda/3.0
        max_split=max(max_split,abs(acc_full-acc_split))
    checks.append({
        'name':'scalar_vs_dynamic_lambda_no_double_count_roundtrip',
        'pass':max_split<1e-12,
        'max_error':max_split,
    })

    max_log=0.0
    for _ in range(128):
        J=10**rng.uniform(-3,2)
        A=10**rng.uniform(-2,1)
        w=10**rng.uniform(-2,2)
        c=3.0
        Jp=rng.uniform(-1,1)*J
        Ap=rng.uniform(-1,1)*A
        wp=rng.uniform(-1,1)*w
        analytic=Jp/J-Ap/A+2*wp/w
        dt=1e-7
        def Xi(s):
            return (J+s*Jp)/(A+s*Ap)*((w+s*wp)/c)**2
        fd=(math.log(Xi(dt))-math.log(Xi(-dt)))/(2*dt)
        max_log=max(max_log,abs(analytic-fd))
    checks.append({
        'name':'phase_clock_information_log_rate',
        'pass':max_log<2e-8,
        'max_error':max_log,
    })

    errs=[]
    H0=0.17
    q=-0.013
    r=0.091
    s=-0.047
    for d in [0.2,0.1,0.05,0.025,0.0125]:
        xs=[-d,0.0,d]
        hs=[]
        for x in xs:
            y=H0*x+0.5*q*x*x+(r/6.0)*x**3+(s/24.0)*x**4
            a=math.exp(y)
            hs.append(np.eye(3)*(a*a))
        est=event_accel(xs,hs)
        exact=q+H0*H0
        errs.append(abs(est-exact))
    ratios=[errs[i+1]/errs[i] for i in range(len(errs)-1)]
    checks.append({
        'name':'event_metric_acceleration_second_order',
        'pass':errs[-1]<5e-7 and all(0.20<ratio<0.30 for ratio in ratios),
        'errors':errs,
        'ratios':ratios,
    })

    max_part=0.0
    for _ in range(256):
        tau=rng.uniform(-math.pi,math.pi)
        C=math.cos(tau/2)**2
        D=math.sin(tau/2)**2
        max_part=max(max_part,abs(C+D-1),abs((C-D)-math.cos(tau)))
    d2_tau0=0.5*math.cos(0.0)
    d2_taupi=0.5*math.cos(math.pi)
    checks.append({
        'name':'holonomy_partition_and_stationary_classification',
        'pass':max_part<1e-15 and d2_tau0>0 and d2_taupi<0,
        'max_identity_error':max_part,
        'D_second_derivative_tau0':d2_tau0,
        'D_second_derivative_taupi':d2_taupi,
    })

    max_partition_gravity=0.0
    for _ in range(256):
        tau=rng.uniform(-math.pi,math.pi)
        U=10**rng.uniform(-4,2)
        C=math.cos(tau/2)**2
        D=math.sin(tau/2)**2
        max_partition_gravity=max(max_partition_gravity,abs(U*(C+D)-U))
    checks.append({
        'name':'holonomy_equal_stress_partition_no_go',
        'pass':max_partition_gravity<1e-12,
        'max_total_potential_error':max_partition_gravity,
        'meaning':'tau_R cannot affect gravity through the partition alone when both channels carry the same stress type',
    })

    max_tau=0.0
    for _ in range(64):
        alpha=10**rng.uniform(-3,1)
        X=10**rng.uniform(-3,1)
        k=10**rng.uniform(-2,1)
        tau=rng.uniform(-math.pi,math.pi)
        dt=1e-7
        def U(t):
            return alpha*X/k
        der=(U(tau+dt)-U(tau-dt))/(2*dt)
        max_tau=max(max_tau,abs(der))
    checks.append({
        'name':'current_rfl3_holonomy_spectator',
        'pass':max_tau==0.0,
        'max_tau_derivative':max_tau,
    })

    passed=all(c['pass'] for c in checks)
    out={
        'schema':SCHEMA,
        'technical_status':'PASS' if passed else 'FAIL',
        'verdict':(
            'PASS_ACCELERATION_CRITERION_CURRENT_HOLONOMY_SPECTATOR_HOLONOMY_ACTIVE_ATTRIBUTION_OPEN'
            if passed else
            'FAIL_COSMOLOGICAL_ACCELERATION_GATE'
        ),
        'canon_allowed':False,
        'checks':checks,
        'open_gates':[
            'ABSOLUTE_ALPHA_I_NORMALIZATION',
            'INDEPENDENT_PHASE_KG_SPECTRAL_MATCH',
            'PHYSICAL_HOLONOMY_D_CHANNEL_STRESS_ATTRIBUTION',
            'NONTRIVIAL_HOLONOMY_PERSISTENCE_OR_DYNAMICAL_STABILITY',
            'PRODUCTION_EVENT_SPATIAL_COSMOLOGY_REALIZATION',
        ],
    }
    print(json.dumps(out,indent=2,sort_keys=True))
    if not passed:
        raise SystemExit(1)

if __name__=='__main__':
    main()
