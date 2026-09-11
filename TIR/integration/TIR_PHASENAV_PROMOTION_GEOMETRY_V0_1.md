# TIR × PhaseNav promotion geometry v0.1 — CANDIDATE_ONLY

Status: `CANDIDATE_ONLY / PHYSICAL_BINDING_OPEN / CANON_WRITE_AUTHORITY_FALSE / EPISTEMIC_CHYBA`.

## 1. Promotion object

A typed promotion between carrier levels is a linear map

`P_n : (E_n,G_n,J_n,D_n) -> (E_{n+1},G_{n+1},J_{n+1},D_{n+1})`.

The three primary defects are

`Delta_G = P^† G_{n+1} P - G_n`,

`Upsilon = J_{n+1} P - P J_n`,

`Xi = D_{n+1} P - P D_n = dP + A_{n+1}P - P A_n`.

A mathematically exact promotion on the declared structures requires the relevant defect to vanish.

## 2. Normalization theorem/interface

For a raw full-rank map `M`, define

`P = M (M^† G_{n+1} M)^(-1/2) G_n^(1/2)`.

Then `P^† G_{n+1} P = G_n`. For equal metric and symmetric doubling `M=[I;I]`, this reduces to `P=[I;I]/sqrt(2)`.

This identifies the familiar `1/sqrt(2)` coefficient as the symmetric special case of metric normalization, not as an independently inserted constant.

## 3. Connection and curvature compatibility

The connection defect is a covariant derivative on `Hom(E_n,E_{n+1})`. Applying the induced covariant derivative gives the curvature mismatch

`nabla^Hom Xi = F_{n+1}P - P F_n`.

Hence exact connection intertwining implies exact curvature intertwining:

`Xi=0 => F_{n+1}P = P F_n`.

This is the admissible mathematical interface for any future SM–GR bridge. No physical unification claim follows from the interface alone.

## 4. Tangential/normal split

For an isometric promotion in an orthonormal frame, `Pi=PP^†`, `Q=I-Pi`, and

`Xi = P Xi_parallel + K`,

with

`Xi_parallel = P^† dP + P^† A_{n+1} P - A_n`,

`K = Q(dP + A_{n+1}P)`.

Thus compatibility separates into induced-connection agreement and absence of orthogonal leakage.

## 5. Quantum geometric tensor

Define

`QGT_{mu,nu} = (d_mu P)^† Q (d_nu P)`.

For rank one, its Hermitian/real part is the Fubini–Study quantum metric and its anti-Hermitian/imaginary part determines Berry curvature up to convention. The same `dP` therefore carries both metric and phase/holonomy information.

## 6. Spectroscopic interface

For `H(lambda)|n>=E_n|n>` and `m != n`, standard perturbation theory gives

`<m|d_mu n> = <m|d_mu H|n>/(E_n-E_m)`.

Therefore

`Q^(n)_{mu,nu} = sum_{m!=n} <n|d_mu H|m><m|d_nu H|n>/(E_n-E_m)^2`.

This supplies a falsifiable bridge between a predicted geometric tensor and measured transition energies/matrix elements. It does not assert that a specific chemical system already realizes the PhaseNav carrier.

## 7. Relational/entanglement scalar for two qubits

For a normalized pure two-qubit state `(c00,c01,c10,c11)`, the separable Segre locus obeys

`c00*c11 - c01*c10 = 0`.

Define candidate relational magnitude

`R_2 = 2 |c00*c11 - c01*c10|`.

For pure two-qubit states this equals concurrence. The definition is exact in that domain; extrapolation to general TIR relations is not canonical.

## 8. Carrier hierarchy

The working finite-dimensional carrier ladder is

`H ~ R^4 ~ C^2`, `O ~ R^8 ~ C^4`, `S_16 ~ R^16 ~ C^8`, `A_32 ~ R^32 ~ C^16`.

Normalized spheres are `S^3,S^7,S^15,S^31`; projective pure-state spaces are `CP^1,CP^3,CP^7,CP^15` after quotient by global complex phase. Classical Hopf fibrations remain separate structure and must not be conflated with the full multi-qubit projective state space.

## 9. Epistemic boundary

Exact here: linear algebra, metric normalization, complex-structure intertwining, connection/curvature intertwining identity, QGT construction, Segre condition and two-qubit concurrence identity.

Candidate physical binding: identification of these carrier levels with atomic/molecular structure, electrophotonic dynamics, Standard-Model fields, gravity, or spacetime microstructure.
