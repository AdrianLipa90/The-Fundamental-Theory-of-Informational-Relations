# DEF-0013 — Semantic action measurement operators

## Status
`hypothesis`

## Depends on
- `DEF-0003`
- `DEF-0010`
- `DEF-0012`

## Objects defined here
1. `OBJ-SEMANTIC-LENGTH-OP-0001`
2. `OBJ-PHASE-COST-OP-0001`
3. `OBJ-RELATIONAL-DEFECT-OP-0001`
4. `OBJ-TRUTH-STRUCTURAL-OP-0001`
5. `OBJ-TRUTH-AUDIT-OP-0001`
6. `OBJ-SEMANTIC-ACTION-STACK-0001`

## Motivation
The project seed already fixed the semantic-action structure
\[
\mathcal S_{online}[\gamma]=\alpha\widehat L[\gamma]+\beta\widehat{\Delta\phi}[\gamma]+\kappa\widehat D_{rel}[\gamma]+\mu\widehat\Pi_{truth}^{struct}[\gamma]
\]
and explicitly separated online truth from audit truth. This module registers the first explicit operator stack for those components.

## 1. Semantic length operator
Let a sampled path be represented by successive state points and local positive metric weights. Define the discrete semantic-length operator
\[
\widehat L_d[\gamma] = \sum_{k=0}^{N-1}\sqrt{g_k}\,\|x_{k+1}-x_k\|.
\]
A continuous notation is
\[
\widehat L[\gamma] = \int_0^1 \sqrt{\dot x^\mu g^{(sem)}_{\mu\nu}(x)\dot x^\nu}\,ds.
\]
An admissible project ansatz for the effective semantic metric is
\[
g^{(sem)} = g^{(0)} + \lambda T^{(sem)},
\]
but this metric law is not promoted here beyond hypothesis level.

## 2. Phase-cost operator
For a phase sequence \(\phi_k\), define the discrete phase-transport cost
\[
\widehat{\Delta\phi}_d[\gamma] = \sum_{k=0}^{N-1}\bigl(1-\cos(\phi_{k+1}-\phi_k)\bigr).
\]
A holonomy-aware scalar variant is
\[
\widehat{\Delta\phi}_B[\gamma] = |\arg U[\gamma]-\phi_*|.
\]

## 3. Relational-defect operator
For sampled phase-vectors \(\gamma^{(k)}=(\gamma_1^{(k)},\dots,\gamma_m^{(k)})\), define
\[
\Delta_H^{(k)} = \sum_{j=1}^{m} e^{i\gamma_j^{(k)}}
\]
and the discrete closure-defect operator
\[
\widehat D_{rel}^{(H)}[\gamma] = \frac1N\sum_{k=1}^{N} |\Delta_H^{(k)}|^2.
\]
A resonance-based variant is
\[
\widehat D_{rel}^{(R)}[\gamma] = \frac1N\sum_{k=1}^{N} \bigl(1-R_k\bigr)
\]
for trajectory samples \(R_k = R(S_k,I_k)\in[0,1]\).
A mixed runtime form is admissible:
\[
\widehat D_{rel}[\gamma] = \omega_H \widehat D_{rel}^{(H)} + \omega_R \widehat D_{rel}^{(R)},
\qquad
\omega_H,\omega_R\ge 0.
\]

## 4. Truth operators
### Structural truth operator
For trajectory-aligned resonance samples \(R_k\in[0,1]\), define
\[
\widehat\Pi_{truth}^{struct}[\gamma] = \frac1N\sum_{k=1}^{N} (1-R_k).
\]

### Audit truth operator
For a finite audited fact-set \(F\), define
\[
\widehat\Pi_{truth}^{audit} = \frac1{|F|}\sum_{f\in F}\bigl(\delta_{false}(f)+\delta_{unmarked}(f)+\delta_{omit}(f)+\delta_{hall}(f)+\delta_{smooth}(f)\bigr).
\]
This operator belongs to post-hoc artifact evaluation rather than trajectory dynamics.

## 5. Canonical role
This module is the first candidate measurement stack that makes every semantic-action component computationally explicit.

## Scope restriction
The action decomposition is now operational, but the final semantic metric law, the runtime truth-potential operator, and calibration of the component coefficients remain open.
