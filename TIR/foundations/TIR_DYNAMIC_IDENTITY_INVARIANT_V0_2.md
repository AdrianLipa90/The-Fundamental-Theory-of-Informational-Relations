# TIR Dynamic Identity Invariant v0.2 — periodic simplex / Bloch–Floquet closure

Status: `EXACT_CONSTRUCTIVE_PERIODIC_N_SIMPLEX_REALIZATION / EXACT_FACE_HOLONOMY / EXACT_TETRAHEDRAL_HALF_TURN_UNIQUENESS`

Scope: close the periodic regular-simplex extension left conditional in v0.1 by giving an explicit Clifford carrier, canonical edge transports, a translation-periodic graph, its Bloch fibers, invariant-sector projectors, and the regular-simplex triangular holonomy law. The construction is purely mathematical. No biological, psychological, personal, consciousness, or physical-identity interpretation is asserted.

## 1. Regular n-simplex carrier

Let `n >= 2` and let `D=n+1`. In `R^D`, with standard basis `e_0,...,e_n`, define

\[
\bar e=\frac1D\sum_{a=0}^{n}e_a,
\qquad
v_i=\sqrt{\frac{D}{n}}\,(e_i-\bar e).
\]

Then the `v_i` lie in the `n`-dimensional hyperplane orthogonal to `(1,...,1)` and satisfy

\[
\boxed{v_i\cdot v_j=\begin{cases}1,&i=j,\\-1/n,&i\ne j.\end{cases}}
\]

Thus they are an explicit centered regular `n`-simplex.

## 2. Explicit Clifford realization

Choose Hermitian Euclidean Clifford generators

\[
\gamma_a^\dagger=\gamma_a,
\qquad
\{\gamma_a,\gamma_b\}=2\delta_{ab}I,
\qquad a,b=0,\dots,n.
\]

A concrete Jordan–Wigner representation exists in dimension

\[
2^{\lfloor (n+1)/2\rfloor}.
\]

For any vector `x in R^D`, write

\[
\Gamma(x)=\sum_{a=0}^{n}x_a\gamma_a.
\]

Then

\[
\{\Gamma(x),\Gamma(y)\}=2(x\cdot y)I.
\]

Define the simplex-sector operators

\[
\boxed{\Sigma_i=\Gamma(v_i).}
\]

Therefore

\[
\boxed{\Sigma_i^2=I}
\]

and, for `i != j`,

\[
\boxed{\{\Sigma_i,\Sigma_j\}=-\frac{2}{n}I.}
\]

This is an explicit higher-dimensional realization, not merely a dimension count.

## 3. Canonical edge transport for every simplex edge

Set

\[
c=-\frac1n.
\]

Because `n>=2`, `c>-1`; no two simplex vertices are antipodal. For each directed edge `j -> i`, define

\[
\boxed{
U_{ij}=\frac{I+\Sigma_i\Sigma_j}{\sqrt{2(1+c)}}
=\sqrt{\frac{n}{2(n-1)}}\,(I+\Sigma_i\Sigma_j).
}
\]

Using `\Sigma_i^2=\Sigma_j^2=I` and

\[
\Sigma_i\Sigma_j+\Sigma_j\Sigma_i=2cI,
\]

we obtain

\[
\begin{aligned}
U_{ij}U_{ij}^\dagger
&=\frac{(I+\Sigma_i\Sigma_j)(I+\Sigma_j\Sigma_i)}{2(1+c)}\\
&=I,
\end{aligned}
\]

so every canonical edge transport is unitary.

Moreover,

\[
\Sigma_i(I+\Sigma_i\Sigma_j)=\Sigma_i+\Sigma_j
=(I+\Sigma_i\Sigma_j)\Sigma_j,
\]

hence

\[
\boxed{\Sigma_iU_{ij}=U_{ij}\Sigma_j.}
\]

Finally,

\[
\boxed{U_{ji}=U_{ij}^\dagger.}
\]

Thus the full complete graph of the regular simplex has an explicit compatible unitary transport on every edge.

## 4. Exact triangular-face holonomy for n >= 3

Take an oriented face `(i,j,k)` and base it at `v_i`. Put

\[
c=-\frac1n.
\]

The first unit tangent direction is

\[
\hat p=\frac{v_j-cv_i}{\sqrt{1-c^2}}.
\]

Define

\[
\hat t_k=\frac{v_k-cv_i}{\sqrt{1-c^2}}.
\]

The internal angle `A_n` of the equilateral spherical triangle satisfies

\[
\cos A_n=\frac{c}{1+c}=-\frac1{n-1},
\]

so

\[
\boxed{A_n=\arccos\!\left(-\frac1{n-1}\right).}
\]

Let

\[
\hat q=\frac{\hat t_k-(\cos A_n)\hat p}{\sin A_n}.
\]

Then `\hat p,\hat q` are orthonormal tangent vectors at `v_i`. Define the oriented tangent bivector

\[
\boxed{J_{ijk}=\Gamma(\hat p)\Gamma(\hat q).}
\]

It obeys

\[
J_{ijk}^\dagger=-J_{ijk},
\qquad
J_{ijk}^2=-I,
\qquad
[J_{ijk},\Sigma_i]=0.
\]

The spherical excess of the face is

\[
\boxed{
\Omega_n=3\arccos\!\left(-\frac1{n-1}\right)-\pi.
}
\]

The ordered canonical spin transport around the face,

\[
W_{ijk}=U_{ij}U_{jk}U_{ki},
\]

is exactly

\[
\boxed{
W_{ijk}
=\cos\frac{\Omega_n}{2}\,I
+\sin\frac{\Omega_n}{2}\,J_{ijk}.
}
\]

Therefore

\[
\boxed{[W_{ijk},\Sigma_i]=0.}
\]

This is the spin lift of the Levi-Civita holonomy of the geodesic spherical face. Reversing orientation sends `J_{ijk} -> -J_{ijk}` and hence `W -> W^\dagger`.

## 5. Tetrahedral half-turn uniqueness theorem

Define the face-turn fraction

\[
\boxed{
q_n=\frac{\Omega_n}{2\pi}
=\frac{3\arccos[-1/(n-1)]-\pi}{2\pi},
\qquad n\ge3.
}
\]

A half-turn occurs iff

\[
q_n=\frac12.
\]

Equivalently,

\[
\Omega_n=\pi
\iff
3A_n-\pi=\pi
\iff
A_n=\frac{2\pi}{3}.
\]

Thus

\[
\cos A_n=-\frac12.
\]

But

\[
\cos A_n=-\frac1{n-1},
\]

so

\[
-\frac1{n-1}=-\frac12
\iff n=3.
\]

Hence

\[
\boxed{q_n=\frac12\iff n=3.}
\]

Within the regular-simplex family, the tetrahedron is therefore the unique dimension whose triangular canonical holonomy is an exact half-turn.

Typed form:

\[
\boxed{
-\frac13
\longrightarrow
\Omega_3=\pi
\longrightarrow
q_3=\frac12,
}
\]

while for general `n >= 3`,

\[
-\frac1n
\longrightarrow
\Omega_n
\longrightarrow
q_n.
\]

This is a generation law. It is not the identity `1/3=1/2`.

The limiting value is

\[
\lim_{n\to\infty}q_n=\frac14.
\]

Thus, for `n>3`, the regular-simplex triangular turn fraction is strictly below one half and tends toward one quarter.

## 6. Explicit translation-periodic n-simplex graph

Let cells be indexed by `m in Z`. Each cell contains the `D=n+1` simplex labels `i=0,...,n`. The real-space Hilbert space is

\[
\mathcal H
=\ell^2(\mathbb Z)\otimes\mathbb C^{D}\otimes\mathcal H_{\rm spin}.
\]

Define the cell invariant

\[
\boxed{
\Sigma_{\rm cell}
=\sum_{i=0}^{n}|i\rangle\langle i|\otimes\Sigma_i.
}
\]

and the full periodic invariant

\[
\Sigma_{\rm per}
=\sum_{m\in\mathbb Z}|m\rangle\langle m|\otimes\Sigma_{\rm cell}.
\]

Choose on-site blocks `M_i` satisfying

\[
[M_i,\Sigma_i]=0.
\]

For example,

\[
M_i=\epsilon_iI+\mu_i\Sigma_i
\]

with real `\epsilon_i,\mu_i`.

Inside each cell, connect any desired set of simplex labels with scalar amplitudes `t_{ij}` multiplying the canonical `U_{ij}`.

For a nontrivial translation link choose the cyclic permutation

\[
p(i)=i+1\pmod D.
\]

Connect `(m,i)` to `(m+1,p(i))` with amplitude `\tau U_{p(i),i}`. Every such edge obeys the same intertwining equation, so the infinite periodic graph is compatible by construction.

## 7. Bloch–Floquet fiber Hamiltonian

After the Bloch transform, `k in [-\pi,\pi)`, define

\[
\begin{aligned}
H_n(k)
={}&\sum_i |i\rangle\langle i|\otimes M_i\\
&-\sum_{i<j} t_{ij}
\left(
|i\rangle\langle j|\otimes U_{ij}
+|j\rangle\langle i|\otimes U_{ji}
\right)\\
&-\tau\sum_i\left(
e^{ik}|p(i)\rangle\langle i|\otimes U_{p(i),i}
+e^{-ik}|i\rangle\langle p(i)|\otimes U_{p(i),i}^\dagger
\right).
\end{aligned}
\]

Every diagonal block commutes with its local `\Sigma_i`; every off-diagonal block intertwines its source and target sectors. Therefore the graph theorem applies fiberwise:

\[
\boxed{[H_n(k),\Sigma_{\rm cell}]=0\qquad\forall k.}
\]

This closes the previously conditional periodic realization for this explicit canonical model.

No statement is made that every possible periodic gluing of a regular simplex has this property. The theorem applies to the construction above and to any other gluing that passes the same edge-intertwining gate.

## 8. Exact invariant-sector decomposition

Because

\[
\Sigma_{\rm cell}^2=I,
\]

define

\[
\boxed{P_\pm=\frac12(I\pm\Sigma_{\rm cell}).}
\]

Then

\[
P_\pm^2=P_\pm,
\qquad
P_+P_-=0,
\qquad
P_++P_-=I.
\]

Since `H_n(k)` commutes with `\Sigma_cell`,

\[
\boxed{P_+H_n(k)P_-=P_-H_n(k)P_+=0.}
\]

Hence

\[
\boxed{
H_n(k)=H_{n,+}(k)\oplus H_{n,-}(k)
}
\]

for every Bloch momentum. The characteristic polynomial factorizes correspondingly into the two invariant sectors.

This is an exact algebraic sector decomposition; it is not by itself a claim of a physical conserved charge.

## 9. Time-Floquet extension

Let the scalar couplings and commuting on-site blocks be time-periodic with period `T`, while retaining the same compatible edge transports:

\[
H_n(k,t+T)=H_n(k,t).
\]

If

\[
[H_n(k,t),\Sigma_{\rm cell}]=0
\qquad\forall k,t,
\]

then the time-ordered propagator `U_k(t)` preserves the invariant:

\[
U_k(t)^\dagger\Sigma_{\rm cell}U_k(t)=\Sigma_{\rm cell}.
\]

Therefore the one-period Floquet operator

\[
F_n(k)=\mathcal T\exp\left[-\frac{i}{\hbar}\int_0^T H_n(k,t)dt\right]
\]

satisfies

\[
\boxed{[F_n(k),\Sigma_{\rm cell}]=0\qquad\forall k.}
\]

Thus the Bloch fibers and the temporal Floquet propagator share the same exact DII sector decomposition whenever the instantaneous compatibility gate holds.

## 10. Loop-holonomy gate

Every closed path in the periodic graph has ordered transport `W_gamma`. Repeated edge intertwining gives

\[
\boxed{[W_\gamma,\Sigma_{a_0}]=0.}
\]

Consequently, loop compatibility is not an additional assumption for the canonical construction: it follows from the already-proved edge compatibility.

The explicit triangular-face formula above provides the nontrivial local holonomy value. Longer periodic Wilson loops need not be scalar; their required property is commutation with the base local sector.

## 11. Falsification

The construction fails if even one used edge transport is replaced by a generic unitary that does not satisfy

\[
\Sigma_aU_{ab}=U_{ab}\Sigma_b.
\]

The v0.2 validator deliberately replaces one cyclic inter-cell transport by the identity while keeping its source and target local operators distinct. The resulting Bloch Hamiltonian develops

\[
[H_{\rm bad}(k),\Sigma_{\rm cell}]\ne0.
\]

Thus the periodic theorem has a direct negative control and is not a tautological numerical pass.

## 12. Validation scope

The deterministic standard-library validator checks `n=2,...,7` and verifies numerically:

- regular-simplex Gram relations;
- local Clifford involutions and pair anticommutators;
- unitarity and directed-edge intertwining;
- reverse-edge adjoint relation;
- global DII involution;
- Hermiticity of sampled Bloch fibers;
- `[H_n(k),Sigma_cell]=0` at several momenta;
- vanishing `+/-` cross-sector blocks;
- the triangular holonomy formula for `n=3,...,7`;
- the tetrahedral `q_3=1/2` witness;
- a broken-edge negative control with nonzero commutator.

The numerical validator is a witness for the exact algebraic derivation, not a substitute for it.

## 13. Claim classes

| Statement | Status |
|---|---|
| centered regular `n`-simplex coordinates | `EXACT` |
| explicit Clifford `Sigma_i` realization | `EXACT` |
| canonical `U_ij` unitary and intertwining | `EXACT` |
| triangular holonomy formula for `n>=3` | `EXACT` |
| `q_n=[3 arccos(-1/(n-1))-pi]/(2pi)` | `EXACT` |
| `q_n=1/2 iff n=3` | `EXACT` |
| tetrahedron uniquely gives half-turn face holonomy in regular-simplex family | `EXACT` |
| explicit translation-periodic simplex graph | `EXACT_CONSTRUCTION` |
| `[H_n(k),Sigma_cell]=0` for every `k` in that construction | `EXACT` |
| exact `+/-` Bloch-sector decomposition | `EXACT` |
| periodic time-Floquet operator preserves DII under instantaneous compatibility | `EXACT` |
| validator over `n=2,...,7` | `NUMERICAL_WITNESS` |
| all arbitrary simplex gluings are compatible | `NOT_CLAIMED` |
| physical Hamiltonian identification | `NOT_CLAIMED` |
| biological, personal, psychological, consciousness, or physical identity binding | `NOT_CLAIMED` |
| quantum-computational advantage | `NOT_CLAIMED` |
