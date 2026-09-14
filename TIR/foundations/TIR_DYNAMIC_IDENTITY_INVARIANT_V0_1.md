# TIR Dynamic Identity Invariant v0.1

Status: `EXACT_TETRAHEDRAL_INVARIANT / EXACT_ABSTRACT_GRAPH_THEOREM / CONDITIONAL_PERIODIC_N_SIMPLEX_REALIZATION`

Scope: define a transport-compatible operator invariant on the tetrahedral/Stella carrier and on an abstract node graph. The construction is purely mathematical. No biological, psychological, personal, or physical identity binding is asserted.

## 1. Upstream tetrahedral carrier

Let

\[
\mathbf n_0,\ldots,\mathbf n_3\in S^2
\]

be the regular tetrahedral frame with

\[
\mathbf n_i\cdot\mathbf n_j=-\frac13\qquad(i\ne j).
\]

Define the Hermitian local sector operators

\[
\boxed{\Sigma_i=\mathbf n_i\cdot\boldsymbol\sigma.}
\]

Because \(|\mathbf n_i|=1\),

\[
\boxed{\Sigma_i^2=I.}
\]

These are the already-established tetrahedral Pauli distinction generators.

## 2. Canonical compatible edge transport

For two non-antipodal unit frames \(\mathbf n_i,\mathbf n_j\), define

\[
\boxed{
U_{ij}=
\frac{I+\Sigma_i\Sigma_j}
{\sqrt{2(1+\mathbf n_i\cdot\mathbf n_j)}}.
}
\]

For the regular tetrahedron,

\[
1+\mathbf n_i\cdot\mathbf n_j=\frac23,
\]

so

\[
\boxed{U_{ij}=\frac{\sqrt3}{2}(I+\Sigma_i\Sigma_j).}
\]

The Pauli product identity implies

\[
\boxed{U_{ij}U_{ij}^\dagger=I}
\]

and the transport-intertwining relation

\[
\boxed{
U_{ij}\Sigma_jU_{ij}^\dagger=\Sigma_i,
}
\]

equivalently

\[
\boxed{\Sigma_iU_{ij}=U_{ij}\Sigma_j.}
\]

Thus a local operator label may vary from node to node while remaining covariantly compatible under edge transport.

## 3. Abstract graph invariant theorem

Let \(G=(V,E)\) be a finite graph. At each node \(a\in V\), let \(\Sigma_a\) be a Hermitian involution,

\[
\Sigma_a^2=I.
\]

Let each directed edge \(b\to a\) carry a unitary \(U_{ab}\) satisfying

\[
\boxed{\Sigma_aU_{ab}=U_{ab}\Sigma_b.}
\]

On

\[
\mathcal H_G=\ell^2(V)\otimes\mathcal H_{\rm int},
\]

define

\[
\boxed{
\Sigma_G=\sum_{a\in V}|a\rangle\langle a|\otimes\Sigma_a.
}
\]

Consider a block Hamiltonian

\[
H=
\sum_a |a\rangle\langle a|\otimes M_a
-
\sum_{(a,b)\in E}
 t_{ab}|a\rangle\langle b|\otimes U_{ab}
+\mathrm{h.c.}
\]

with

\[
[M_a,\Sigma_a]=0
\]

and compatible edge transports as above.

For diagonal blocks,

\[
(\Sigma_GH-H\Sigma_G)_{aa}=[\Sigma_a,M_a]=0.
\]

For an off-diagonal block,

\[
(\Sigma_GH-H\Sigma_G)_{ab}
=-t_{ab}(\Sigma_aU_{ab}-U_{ab}\Sigma_b)=0.
\]

Therefore

\[
\boxed{[H,\Sigma_G]=0.}
\]

This is an exact algebraic theorem for any graph satisfying the stated hypotheses.

Consequently, for time-independent \(H\),

\[
U(t)=e^{-iHt/\hbar}
\]

obeys

\[
\boxed{U(t)^\dagger\Sigma_GU(t)=\Sigma_G.}
\]

We call \(\Sigma_G\) the **Dynamic Identity Invariant (DII)** of the compatible operator sector.

## 4. Closed-loop compatibility and holonomy

For a closed path

\[
\gamma:a_0\to a_1\to\cdots\to a_m=a_0,
\]

define the ordered holonomy

\[
\boxed{
W_\gamma=U_{a_0a_{m-1}}\cdots U_{a_2a_1}U_{a_1a_0}.
}
\]

Repeated application of the edge intertwining relation gives

\[
\boxed{W_\gamma\Sigma_{a_0}W_\gamma^\dagger=\Sigma_{a_0},}
\]

hence

\[
\boxed{[W_\gamma,\Sigma_{a_0}]=0.}
\]

This is a necessary loop-consistency condition for a globally compatible sector.

## 5. Exact tetrahedral face holonomy

For the canonical tetrahedral transports,

\[
W_{012}=U_{01}U_{12}U_{20}
\]

reduces exactly to

\[
\boxed{W_{012}=+i\Sigma_0.}
\]

Reversing the face orientation gives

\[
\boxed{W_{021}=-i\Sigma_0.}
\]

Therefore

\[
\boxed{W_{012}^2=-I,\qquad W_{012}^4=I}
\]

and

\[
\boxed{[W_{012},\Sigma_0]=0.}
\]

The local tetrahedral relation \(-1/3\) and the resulting half-turn holonomy are differently typed invariants. This result does **not** identify the scalar values \(1/3\) and \(1/2\).

## 6. Geometric origin of the half-turn

The tetrahedral vertices determine an equilateral spherical triangle with side length \(s\) satisfying

\[
\cos s=-\frac13.
\]

For an equilateral spherical triangle,

\[
\cos A=\frac{\cos s}{1+\cos s}.
\]

Thus

\[
\cos A=\frac{-1/3}{2/3}=-\frac12,
\qquad
\boxed{A=\frac{2\pi}{3}.}
\]

Its spherical excess is

\[
\boxed{
\Omega=3A-\pi=\pi.
}
\]

Hence the regular tetrahedral \(-1/3\) geometry generates an exact \(\pi\)-holonomy / half-turn on each oriented face.

Typed statement:

\[
\boxed{
-\frac13\ \text{tetrahedral geometry}
\longrightarrow
\Omega=\pi
\longrightarrow
\left[\frac12\right]\ \text{turn class}.
}
\]

This is a generation relation, not an equality of fractions.

## 7. Time-dependent invariant equation

For a time-dependent Hamiltonian and operator family, the standard invariant equation is

\[
\boxed{
\frac{\partial\Sigma_G}{\partial t}
+\frac{i}{\hbar}[H(t),\Sigma_G(t)]=0.
}
\]

If this equation holds, the expectation and spectral sector associated with the invariant are transported consistently by the dynamics.

This repository does not claim novelty for the general time-dependent invariant equation. The TIR-specific content is the tetrahedral/Stella carrier, its canonical compatible transports, and the exact tetrahedral face-holonomy reduction above.

## 8. Periodic and Bloch–Floquet extension

If a compatible graph admits a translation group \(\Gamma\), a Bloch–Floquet decomposition may be written as

\[
H\cong\int_{\mathrm{BZ}}^\oplus H(k)\,dk.
\]

A periodic DII sector requires

\[
\boxed{[H(k),\Sigma_G(k)]=0\quad\text{for every }k\text{ in the Brillouin zone}.}
\]

This is an exact acceptance condition once \(H(k)\) and \(\Sigma_G(k)\) are specified.

For a regular \(n\)-simplex,

\[
\mathbf v_i\cdot\mathbf v_j=-\frac1n
\qquad(i\ne j).
\]

A higher-dimensional realization may replace Pauli generators by a Clifford representation \(\Gamma(\mathbf v)\) satisfying

\[
\{\Gamma(\mathbf v),\Gamma(\mathbf w)\}
=2(\mathbf v\cdot\mathbf w)I.
\]

The abstract graph theorem then remains exact if the required edge-intertwining equations hold. A specific periodic \(n\)-simplex realization is `CONDITIONAL` until its Clifford representation, gluing data, loop holonomies, and Bloch-sector compatibility are explicitly constructed and validated.

## 9. Falsification gate

The invariant is not automatic.

If any edge fails

\[
\Sigma_aU_{ab}=U_{ab}\Sigma_b,
\]

then a generic Hamiltonian using that edge need not commute with \(\Sigma_G\).

The deterministic validator includes a negative control in which one compatible tetrahedral edge transport is replaced by the identity. The corresponding global commutator becomes nonzero.

Thus the construction is falsifiable by direct matrix computation.

## 10. Claim classes

| Statement | Status |
|---|---|
| tetrahedral \(\Sigma_i^2=I\) | `EXACT` |
| canonical \(U_{ij}\) is unitary | `EXACT` |
| \(U_{ij}\Sigma_jU_{ij}^\dagger=\Sigma_i\) | `EXACT` |
| abstract graph theorem \([H,\Sigma_G]=0\) under stated hypotheses | `EXACT` |
| loop holonomy commutes with the local sector under compatible transport | `EXACT` |
| tetrahedral face holonomy \(W=\pm i\Sigma\) | `EXACT` |
| tetrahedral spherical excess \(\Omega=\pi\) | `EXACT` |
| time-dependent invariant equation | `STANDARD_INVARIANT_EQUATION` |
| periodic/Bloch acceptance equation | `EXACT_GIVEN_SPECIFIED_PERIODIC_DATA` |
| general periodic \(n\)-simplex realization | `CONDITIONAL` |
| biological, psychological, personal, or physical identity binding | `NOT_CLAIMED` |
| physical Hamiltonian identification | `NOT_CLAIMED` |
