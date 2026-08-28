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

The pole distinction therefore admits two different levels of description:

\[
\{p_N,p_S\}
\quad\text{and}\quad
\{\alpha,\beta\},
\]

with

\[
p_N=|\alpha|^2,
\qquad
p_S=|\beta|^2.
\]

The symmetric half-seam has the equal-modulus condition

\[
|\alpha|=|\beta|=\frac1{\sqrt2}.
\]

Its remaining degree of freedom is relative phase:

\[
|\psi_{1/2}(\varphi)\rangle
=\frac{1}{\sqrt2}
\left(|N\rangle+e^{i\varphi}|S\rangle\right).
\]

This is the TIR entry point for coherent two-alternative structure.

## 5. Schrödinger branch: continuous unitary relational flow

Add a continuous relational parameter `τ` and a strongly continuous one-parameter unitary flow

\[
U(\tau_1+\tau_2)=U(\tau_1)U(\tau_2),
\qquad
U(0)=I.
\]

By the standard unitary-generator theorem there is a self-adjoint generator `G` such that

\[
U(\tau)=e^{-iG\tau/\hbar}.
\]

For

\[
|\psi(\tau)\rangle=U(\tau)|\psi(0)\rangle,
\]

differentiation gives

\[
\boxed{
i\hbar\frac{\partial}{\partial\tau}|\psi(\tau)\rangle
=G|\psi(\tau)\rangle.
}
\]

When `τ` is the physical time parameter and `G=H`, this is the Schrödinger evolution law.

The dependency ladder is therefore

\[
\boxed{
0
\rightarrow
\text{first distinction}
\rightarrow
\mathbb C^2
\rightarrow
\text{continuous unitary flow}
\rightarrow
\text{Schrödinger generator equation}.
}
\]

Within TIR the first distinction supplies the two-pole carrier; the unitary-flow assumptions supply the dynamical layer.

## 6. Heisenberg branch: more than one distinction axis

One binary distinction defines one pole axis. A second binary distinction frame on the same `\mathbb C^2` carrier introduces another observable decomposition.

The canonical traceless binary observables are the Pauli generators

\[
\sigma_x=
\begin{pmatrix}
0&1\\1&0
\end{pmatrix},
\qquad
\sigma_y=
\begin{pmatrix}
0&-i\\i&0
\end{pmatrix},
\qquad
\sigma_z=
\begin{pmatrix}
1&0\\0&-1
\end{pmatrix}.
\]

They satisfy

\[
\boxed{
[\sigma_i,\sigma_j]
=2i\,\varepsilon_{ijk}\sigma_k.
}
\]

For two self-adjoint observables `A,B`, the Robertson relation gives

\[
\boxed{
\Delta A\,\Delta B
\ge
\frac12\left|\langle[A,B]\rangle\right|.
}
\]

For spin operators

\[
S_i=\frac{\hbar}{2}\sigma_i,
\]

one obtains

\[
[S_i,S_j]=i\hbar\varepsilon_{ijk}S_k.
\]

Thus the TIR dependency ladder for the Heisenberg branch is

\[
\boxed{
0
\rightarrow
\text{first distinction}
\rightarrow
\text{two-pole carrier}
\rightarrow
\text{multiple distinction axes}
\rightarrow
\text{noncommutativity}
\rightarrow
\text{uncertainty relation}.
}
\]

The uncertainty structure appears when the same binary carrier is interrogated along incompatible relational axes.

## 7. Bloch-sphere closure of the two-pole carrier

Pure states of `\mathbb C^2` modulo global phase form

\[
\boxed{\mathbb{CP}^1\cong S^2}.
\]

The poles `N,S` become antipodal points on the Bloch sphere. Every pure two-state distinction frame is represented by an oriented diameter.

A normalized density operator can be written as

\[
\rho=\frac12\left(I+\mathbf r\cdot\boldsymbol\sigma\right),
\qquad |\mathbf r|\le1.
\]

The maximally mixed binary state is

\[
\boxed{\rho_\star=\frac12I},
\]

with von Neumann entropy

\[
\boxed{S(\rho_\star)=\ln2}.
\]

This gives a second exact appearance of the same binary information value at equal pole weight.

## 8. Rotation-group branch and the Banach–Tarski entry point

Once the two-pole axis is embedded in `S^2`, changing distinction frames is naturally represented by rotations.

The frame group is

\[
SO(3),
\]

with the spinorial double cover

\[
SU(2)\to SO(3).
\]

Two rotations about suitably chosen different axes can generate a noncommuting subgroup. The Banach–Tarski theorem branch uses a stronger group-theoretic layer: a free non-abelian subgroup

\[
F_2\subset SO(3),
\]

its paradoxical group action, extension from the sphere to three-dimensional sets, and a choice principle selecting orbit representatives.

The structural dependency ladder is therefore

\[
\boxed{
0
\rightarrow
\text{first distinction}
\rightarrow
\text{oriented two-pole axis}
\rightarrow
\text{multiple rotated axes}
\rightarrow
SO(3)
\supset
F_2
\rightarrow
\text{paradoxical decomposition}
\xrightarrow{\rm Choice}
\text{Banach--Tarski}.
}
\]

For TIR, the common root is the first relational distinction and the emergence of an oriented axis. The Banach--Tarski theorem itself enters after the explicit `SO(3)`, free-group, orbit and choice layers are present.

## 9. One root, four branches

The shared root can be summarized as

\[
\boxed{
\mathfrak Z
\xrightarrow{\Delta_1}
\{N,S\}
\xrightarrow{\rm exchange}
\frac12
}
\]

followed by four typed branches:

\[
\frac12
\xrightarrow{\rm Shannon}
\ln2,
\]

\[
\{N,S\}
\xrightarrow{\rm coherent\ lift}
\mathbb C^2
\xrightarrow{\rm unitary\ flow}
\text{Schrödinger},
\]

\[
\mathbb C^2
\xrightarrow{\rm multiple\ axes}
[\sigma_i,\sigma_j]\ne0
\xrightarrow{\rm Robertson}
\text{Heisenberg uncertainty},
\]

\[
\{N,S\}
\xrightarrow{\rm oriented\ axis}
S^2
\xrightarrow{\rm rotations}
SO(3)
\supset F_2
\xrightarrow{\rm paradoxical\ action+Choice}
\text{Banach--Tarski}.
\]

The first distinction is therefore the shared TIR root; each branch records its own additional mathematical structure explicitly.

## 10. Crosslink outputs

### Secret of a Half

Export

```text
first_distinction = {N,S}
exchange           = N <-> S
fixed_share        = 1/2
entropy             = ln2
projective_odds     = 1
```

This binds directly to the existing complement/reciprocal half interface.

### Informational Dynamics of Time

Export

```text
binary_relational_carrier = {N,S}
half_seam                 = 1/2
coherent_half_family      = (|N> + exp(i*phi)|S>)/sqrt(2)
phase_degree_of_freedom   = phi
```

The temporal repository may consume this packet at its `TIR -> Temporal Primitive` boundary and owns every later temporal dynamical promotion.

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
| Schrödinger equation from the unitary generator with physical time and Hamiltonian identification | EXACT CONDITIONAL |
| Pauli commutators | EXACT MATRIX IDENTITY |
| Robertson uncertainty relation | STANDARD OPERATOR THEOREM |
| `CP^1 ~= S^2` two-state pure-state geometry | STANDARD GEOMETRIC IDENTIFICATION |
| `S(I/2)=ln2` | EXACT QUANTUM-INFORMATION IDENTITY |
| `SO(3)` contains free non-abelian subgroups used in paradoxical decompositions | STANDARD GROUP-THEORETIC INPUT |
| Banach--Tarski branch from free-group action plus choice | STANDARD SET-THEORETIC/GEOMETRIC THEOREM CHAIN |
| common first-distinction root across these branches | TIR STRUCTURAL CROSSWALK |

## 12. Dependency firewall

The source dependency graph is explicit:

```text
ZERO
  -> FIRST_DISTINCTION
      -> HALF_SEAM -> ln2 -> TIR kappa numerator
      -> C^2 -> unitary flow -> Schrodinger
      -> C^2 -> incompatible axes -> Heisenberg/Robertson
      -> oriented axis -> S^2 -> SO(3) -> F2 -> paradoxical action + Choice -> Banach-Tarski
```

Every arrow carries only the structure introduced at that layer. This keeps the common root visible while preserving the theorem requirements of each branch.
