# TIR Zero → First Distinction Foundation v0.1

Status: `TIR_FIRST_DISTINCTION_FOUNDATION_CANDIDATE`

Scope: TIR-only formalization of the common structural root behind the relational half-seam, binary Shannon information, the minimal two-state Hilbert carrier, noncommuting distinction frames, and the rotation-group entry point used much later by paradoxical decomposition theorems.

The construction begins from the relational zero, which is explicitly pre-object, and adds support and distinction one layer at a time.

## 0. Relational zero: no object is hidden in zero

Let a relational presentation be

\[
\mathfrak R=(X,\mathcal D),
\]

where \(X\) is the support set and \(\mathcal D\) is the set of realized distinctions/relations.

The TIR zero layer is

\[
\boxed{
\mathfrak Z_{\rm rel}
=
(\varnothing,\varnothing).
}
\]

Therefore

\[
X_0=\varnothing,
\qquad
\mathcal D_0=\varnothing,
\qquad
\boxed{\nexists x\;(x\in X_0).}
\]

This is not a singleton carrier. It is the empty relational presentation. TIR defines existence relationally, so once that definition is fixed the absence of an existent object at the zero layer is an exact definitional consequence. The zero layer is therefore relational rather than a reified object called nothing.

Canonical owner: \`TIR/foundations/TIR_RELATIONAL_ZERO_AXIOM_V0_1.md\`.

## 0.1 Minimal nonzero support

Leaving relational zero requires nonempty support. The least nonempty support is

\[
\boxed{
\mathcal P=\{p\},
\qquad
|\mathcal P|=1.
}
\]

This point is the minimal support candidate, not the zero state:

\[
\boxed{
\mathfrak Z_{\rm rel}\neq \mathcal P.
}
\]

At this layer there is still no realized distinction. The unresolved presentation \((\mathcal P,\varnothing)\) does not yet satisfy the relational-existence criterion by itself.

## 1. First distinction: the minimal nontrivial partition

Let \(\Omega_{\mathcal P}\) be the state/aspect domain supported at \(\mathcal P\). A distinction is represented by a partition \(\Pi\) of that domain. A nontrivial distinction contains more than one nonempty block, so

\[
|\Pi|\ge 2.
\]

The minimal nontrivial distinction therefore has exactly two outcomes:

\[
\boxed{
|\Pi_1|=2,
\qquad
\Pi_1=\{N,S\}.
}
\]

The labels \(N,S\) are relational poles/aspects of the minimal carrier. They are not assumed to be two pre-existing spatial objects.

Only after the binary distinction has been established do we introduce the primitive exchange map

\[
J:N\leftrightarrow S,
\qquad
J^2=\mathrm{id}.
\]

Equivalently, choosing one pole label \(x\),

\[
Jx\neq x,
\qquad
\mathcal O_J(x)=\{x,Jx\}=\{N,S\}.
\]

Thus the first nonzero relational chain is

\[
\boxed{
\mathfrak Z_{\rm rel}
\longrightarrow
\mathcal P
\longrightarrow
\{N,S\}.
}
\]

Binarity follows from minimal nontrivial distinction; the involution expresses the subsequent exchange symmetry rather than being used to smuggle binarity into the premise.

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
0_{\rm rel}
\longrightarrow
\mathcal P
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
\boxed{\operatorname{Fix}(J)=\left\{\frac12\right\}}
\]

and the first distinction carries a canonical exchange seam.

## 4. Minimal coherent lift

Represent the two distinguished poles by an orthonormal basis `|N>` and `|S>`. The minimal complex Hilbert carrier spanning them is

\[
\boxed{\mathcal H_2\cong\mathbb C^2}.
\]

At equal pole weight,

\[
\boxed{
|\psi_{1/2}(\varphi)\rangle
=\frac{|N\rangle+e^{i\varphi}|S\rangle}{\sqrt2}
}
\]

and the remaining internal coordinate is relative phase `φ`.

## 5. Schrödinger branch

A strongly continuous one-parameter unitary relational flow has a self-adjoint generator `G`,

\[
U(\tau)=e^{-iG\tau/\hbar},
\]

hence

\[
\boxed{
i\hbar\frac{\partial}{\partial\tau}|\psi(\tau)\rangle
=G|\psi(\tau)\rangle.
}
\]

With the physical-time and Hamiltonian identification this is the Schrödinger evolution law.

## 6. Heisenberg branch

Multiple distinction axes on `\mathbb C^2` are represented by Pauli generators,

\[
\boxed{[\sigma_i,\sigma_j]=2i\varepsilon_{ijk}\sigma_k}.
\]

For self-adjoint observables,

\[
\boxed{\Delta A\Delta B\ge\frac12|\langle[A,B]\rangle|}.
\]

Thus incompatible relational axes supply the operator-theoretic entry point for the Heisenberg/Robertson uncertainty structure.

## 7. Bloch-sphere closure

Pure two-state rays form

\[
\boxed{\mathbb{CP}^1\cong S^2}.
\]

The equal statistical mixture is

\[
\rho_\star=\frac12I,
\qquad
\boxed{S(\rho_\star)=\ln2}.
\]

## 8. Rotation-group branch and Banach–Tarski entry point

The two-pole axis embeds in `S^2`; distinction-frame changes are represented by `SO(3)`, with spinorial double cover `SU(2) -> SO(3)`.

The Banach--Tarski theorem branch uses the stronger chain

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

## 11. Claim classes

| Statement | TIR class |
|---|---|
| `Z_rel=(empty,empty)` | DEFINITIONAL RELATIONAL ZERO |
| no object exists in relational zero | EXACT DEFINITIONAL CONSEQUENCE |
| minimal nonempty support is a point | EXACT SET-THEORETIC |
| minimal nontrivial distinction has two outcomes | EXACT DEFINITIONAL / SET-THEORETIC |
| exchange-symmetric shares are `(1/2,1/2)` | EXACT |
| `H_2(1/2)=ln2` | EXACT INFORMATION-THEORETIC |
| `Fix(u->1-u)={1/2}` | EXACT |
| minimal complex Hilbert span is `C^2` | EXACT LINEAR-ALGEBRAIC |
| unitary-flow generator theorem | STANDARD FUNCTIONAL-ANALYTIC THEOREM |
| Schrödinger generator equation with physical-time/Hamiltonian identification | EXACT CONDITIONAL |
| Pauli commutators | EXACT MATRIX IDENTITY |
| Robertson uncertainty relation | STANDARD OPERATOR THEOREM |
| `CP^1 ~= S^2` | STANDARD GEOMETRIC IDENTIFICATION |
| `S(I/2)=ln2` | EXACT QUANTUM-INFORMATION IDENTITY |
| free non-abelian subgroup entry in `SO(3)` | STANDARD GROUP-THEORETIC INPUT |
| Banach--Tarski branch from free-group action plus choice | STANDARD SET-THEORETIC/GEOMETRIC THEOREM CHAIN |
| common first-distinction root | TIR STRUCTURAL CROSSWALK |
