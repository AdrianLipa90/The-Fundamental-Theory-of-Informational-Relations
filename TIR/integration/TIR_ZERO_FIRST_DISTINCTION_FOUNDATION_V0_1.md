# TIR Zero → First Distinction Foundation v0.1

Status: `TIR_FIRST_DISTINCTION_FOUNDATION_CANDIDATE`

Scope: TIR-only formalization of the common structural root behind the relational half-seam, binary Shannon information, the minimal two-state Hilbert carrier, noncommuting distinction frames, and the rotation-group entry point used much later by paradoxical decomposition theorems.

The construction begins from zero relational distinction and adds structure one layer at a time.

## 0. Zero relational distinction

Let

\[
\mathfrak Z=\{\bullet\}
\]

be the undivided relational carrier. It has one label and the degenerate probability vector

\[
\mathbf p_0=(1).
\]

Its Shannon entropy is

\[
\boxed{H(\mathbf p_0)=0}.
\]

Define the distinction count

\[
D(\mathfrak Z)=0.
\]

This is the TIR zero layer: one carrier, one label, zero internal distinction.

## 1. First distinction: two poles

Apply the first distinction operator

\[
\Delta_1:\mathfrak Z\longmapsto\mathfrak B=\{N,S\}.
\]

The labels `N` and `S` are relational poles. Algebraically introduce complementary projectors

\[
P_N^2=P_N,\qquad P_S^2=P_S,
\]

\[
P_NP_S=0,\qquad P_N+P_S=I.
\]

The first distinction therefore creates the minimal binary partition

\[
\boxed{\mathfrak Z\xrightarrow{\Delta_1}\{N,S\}}.
\]

This is the primitive TIR distinction from which the half-seam branch is built.

## 2. Equal relational share and the birth of ln 2

Assign relational shares

\[
\mathbf p=(p_N,p_S),\qquad p_N+p_S=1.
\]

At the exchange-symmetric seam,

\[
p_N=p_S,
\]

hence

\[
\boxed{p_N=p_S=\frac12}.
\]

The binary Shannon entropy is

\[
H_2(p)=-p\ln p-(1-p)\ln(1-p).
\]

At the first symmetric distinction,

\[
\boxed{H_2(1/2)=\ln2}.
\]

Thus the zero-to-distinction chain is

\[
\boxed{
0_{\rm distinction}
\longrightarrow
\{N,S\}
\longrightarrow
\left(\frac12,\frac12\right)
\longrightarrow
\ln2.
}
\]

This supplies the local information-theoretic parent for the existing TIR normalization

\[
\boxed{\kappa=\frac{\ln2}{24\pi}}.
\]

The denominator `24π` retains its existing TIR structural role.

## 3. The half-seam as the fixed point of pole exchange

Normalize the relational coordinate by

\[
u\in[0,1],
\]

with pole exchange

\[
J(u)=1-u.
\]

The unique fixed point is

\[
J(u_\star)=u_\star
\iff
u_\star=\frac12.
\]

Therefore

\[
\boxed{
\operatorname{Fix}(J)=\left\{\frac12\right\}
}
\]

and the first distinction carries a canonical exchange seam.

This is the same TIR object registered by

`TIR/integration/TIR_RELATIONAL_HALF_SEAM_CROSSLINK_V0_1.md`.

## 4. Minimal coherent lift: the two-state Hilbert carrier

Represent the two distinguished poles by an orthonormal basis

\[
|N\rangle=\begin{pmatrix}1\\0\end{pmatrix},
\qquad
|S\rangle=\begin{pmatrix}0\\1\end{pmatrix}.
\]

The minimal complex Hilbert carrier spanning both alternatives is

\[
\boxed{\mathcal H_2\cong\mathbb C^2}.
\]

A normalized relational amplitude state is

\[
|\psi\rangle
=\alpha|N\rangle+\beta|S\rangle,
\qquad
|\alpha|^2+|\beta|^2=1.
\]

The symmetric half-seam has the equal-modulus condition

\[
|\alpha|=|\beta|=\frac1{\sqrt2},
\]

leaving relative phase as the internal coordinate:

\[
|\psi_{1/2}(\varphi)\rangle
=\frac{1}{\sqrt2}
\left(|N\rangle+e^{i\varphi}|S\rangle\right).
\]

## 5. Schrödinger branch

Add a continuous relational parameter `τ` and a strongly continuous one-parameter unitary flow

\[
U(\tau_1+\tau_2)=U(\tau_1)U(\tau_2),
\qquad U(0)=I.
\]

Its self-adjoint generator `G` gives

\[
U(\tau)=e^{-iG\tau/\hbar},
\]

and therefore

\[
\boxed{
i\hbar\frac{\partial}{\partial\tau}|\psi(\tau)\rangle
=G|\psi(\tau)\rangle.
}
\]

With physical time and Hamiltonian identification this is the Schrödinger evolution law.

## 6. Heisenberg branch

Multiple binary distinction frames on the same `\mathbb C^2` carrier are represented by Pauli generators satisfying

\[
\boxed{[\sigma_i,\sigma_j]=2i\varepsilon_{ijk}\sigma_k}.
\]

For self-adjoint `A,B`,

\[
\boxed{
\Delta A\Delta B\ge\frac12|\langle[A,B]\rangle|
}
\]

and for `S_i=\hbar\sigma_i/2`,

\[
[S_i,S_j]=i\hbar\varepsilon_{ijk}S_k.
\]

Thus incompatible distinction axes supply the operator-theoretic entry point for the Heisenberg/Robertson uncertainty structure.

## 7. Bloch-sphere closure

Pure states of `\mathbb C^2` modulo global phase form

\[
\boxed{\mathbb{CP}^1\cong S^2}.
\]

The maximally mixed binary state is

\[
\rho_\star=\frac12I,
\]

with

\[
\boxed{S(\rho_\star)=\ln2}.
\]

## 8. Rotation-group branch and Banach–Tarski entry point

The oriented two-pole axis embeds in `S^2`; changing distinction frames is represented by `SO(3)` rotations, with spinorial double cover `SU(2) -> SO(3)`.

The Banach--Tarski theorem branch uses the stronger group-theoretic chain

\[
\boxed{
S^2
\rightarrow
SO(3)
\supset
F_2
\rightarrow
\text{paradoxical group action}
\xrightarrow{\rm Choice}
\text{Banach--Tarski}.
}
\]

The common TIR root is the first relational distinction and the emergence of an oriented axis; the free-group, orbit and choice layers supply the later theorem requirements.

## 9. One root, four branches

```text
ZERO
  -> FIRST_DISTINCTION {N,S}
      -> HALF_SEAM 1/2 -> ln2 -> TIR kappa numerator
      -> C^2 -> unitary flow -> Schrodinger
      -> C^2 -> incompatible axes -> Heisenberg/Robertson
      -> oriented axis -> S^2 -> SO(3) -> F2 -> paradoxical action + Choice -> Banach-Tarski
```

## 10. Crosslink outputs

### Secret of a Half

```text
first_distinction = {N,S}
exchange           = N <-> S
fixed_share        = 1/2
entropy             = ln2
projective_odds     = 1
```

### Informational Dynamics of Time

```text
binary_relational_carrier = {N,S}
half_seam                 = 1/2
coherent_half_family      = (|N> + exp(i*phi)|S>)/sqrt(2)
phase_degree_of_freedom   = phi
```

The temporal repository may consume this packet at its `TIR -> Temporal Primitive` boundary and owns the later temporal dynamical promotion.

## 11. Claim classes

| Statement | TIR class |
|---|---|
| `H((1))=0` | EXACT INFORMATION-THEORETIC |
| first binary partition creates two distinguishable labels | EXACT DEFINITIONAL |
| exchange-symmetric shares are `(1/2,1/2)` | EXACT |
| `H_2(1/2)=ln2` | EXACT INFORMATION-THEORETIC |
| `Fix(u->1-u)={1/2}` | EXACT |
| minimal complex Hilbert span of two basis states is `C^2` | EXACT LINEAR-ALGEBRAIC |
| strongly continuous one-parameter unitary flow has a self-adjoint generator | STANDARD FUNCTIONAL-ANALYTIC THEOREM |
| Schrödinger generator equation with physical-time/Hamiltonian identification | EXACT CONDITIONAL |
| Pauli commutators | EXACT MATRIX IDENTITY |
| Robertson uncertainty relation | STANDARD OPERATOR THEOREM |
| `CP^1 ~= S^2` | STANDARD GEOMETRIC IDENTIFICATION |
| `S(I/2)=ln2` | EXACT QUANTUM-INFORMATION IDENTITY |
| `SO(3)` free non-abelian subgroup entry | STANDARD GROUP-THEORETIC INPUT |
| Banach--Tarski branch from free-group action plus choice | STANDARD SET-THEORETIC/GEOMETRIC THEOREM CHAIN |
| common first-distinction root | TIR STRUCTURAL CROSSWALK |
