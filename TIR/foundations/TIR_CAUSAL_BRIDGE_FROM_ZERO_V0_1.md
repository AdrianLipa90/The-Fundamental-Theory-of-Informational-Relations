# TIR Causal Bridge from Zero v0.1

Status: `INTERMEDIATE_PROVENANCE__SUPERSEDED_BY_TIR_CANONICAL_DERIVATION_SPINE_V0_1`

Scope: historical intermediate dependency architecture retained for provenance. Canonical foundation DAG is now owned by `TIR_CANONICAL_DERIVATION_SPINE_V0_1.md` and `DEPENDENCY_EXPORT.json`.

## 1. Dependency before temporal order

Write

\[
\boxed{X\prec_{\rm dep}Y}
\]

when \(Y\) uses \(X\) as an upstream parent in the derivation graph.

## 2. Zero is relational, not ontic

Literal ontic nothing is not an object. The symbol \(0\) is admitted only as a null value of a relation/map:

\[
\boxed{R\prec_{\rm dep}0_R.}
\]

The minimum non-empty TIR content is

\[
\boxed{\mathcal R_1=(a\xleftrightarrow{R}b).}
\]

Orientation reversal gives

\[
\mathcal R_1\prec_{\rm dep}\{N,S\}.
\]

Exchange balance and normalization give

\[
\{N,S\}\prec_{\rm dep}\frac12,
\]

and the binary Shannon functional gives

\[
\frac12\prec_{\rm dep}\ln2.
\]

## 3. Relational sphere and quantum/projective continuation

The pole pair defines an oriented axis. Complete orientation closure gives the abstract relational sphere

\[
\boxed{
\{N,S\}
\prec_{\rm dep}
S^2.
}
\]

Then

\[
\boxed{
S^2\cong\mathbb{CP}^1
\prec_{\rm dep}
P(\mathbb C^2).
}
\]

Only after this identification is the sphere the standard Bloch sphere of a two-state quantum carrier.

The common primitive packet is therefore

\[
\boxed{
\mathcal C_0=
\left(
R,0_R,\{N,S\},\frac12,\ln2,S^2,\mathbb{CP}^1,P(\mathbb C^2)
\right).
}
\]

## 4. Arithmetic closure branch

Closed relational return satisfies

\[
\Delta_R(\gamma)=0.
\]

For a \(U(1)\) phase lift,

\[
e^{i\Delta\phi}=1
\iff
\Delta\phi=2\pi n,
\qquad n\in\mathbb Z.
\]

Thus

\[
0_R
\prec_{\rm dep}
\text{winding/degree}
\prec_{\rm dep}
\mathbb Z
\prec_{\rm dep}
\mathbb N_{\ge0}.
\]

## 5. TIR spatial, matter and time branches

The common packet feeds the sibling branches

\[
\boxed{
\mathcal C_0
\prec_{\rm dep}
\left\{
\mathcal G_X^{\rm TIR},
\mathcal B_{\rm SM}^{\rm TIR},
\mathcal B_T^{\rm IDT}
\right\}.
}
\]

The spatial--temporal join is

\[
\mathcal G_X^{\rm TIR}\otimes\mathcal B_T^{\rm IDT}
\to\mathfrak M_{XT},
\]

followed by matter coupling

\[
\mathfrak M_{XT}\otimes\mathcal B_{\rm SM}^{\rm TIR}
\to\mathfrak M_{XT+\rm matter}.
\]

## 6. Context-closure branch

If projection erases a relational coordinate, distinct context-bearing states can collapse to an apparent contradiction. The repair is to retain the kernel/context information:

\[
\boxed{
(P,C_1;\neg P,C_2)
\to
\widetilde X(C_1,C_2).
}
\]

This is the structural replacement for historical A8; no A8 axiom is used upstream.

## 7. Canonical DAG

```text
RELATION
  |-- relational nullity --> 0_R
  |       `-- closed phase return --> winding/degree --> Z --> N
  |
  `-- orientation reversal --> {N,S}
          |-- exchange balance --> 1/2 --> ln2
          `-- orientation closure --> S2 --> CP1 --> P(C2) --> quantum carrier
                                                   `--> Hilbert/Euler symmetry

COMMON PRIMITIVE CORE
  |-- TIR spatial geometry
  |-- TIR Standard Model
  `-- IDT time branch

spatial + time --> spacetime
spacetime + matter --> matter/field spacetime
```

## 8. Invariant

\[
\boxed{
N_{\rm nonlogical\ axioms}=0,
\qquad
N_{\rm legacy\ independent\ axioms}=0.
}
\]

Current dependency lattice:

`TIR/foundations/TIR_PRIMITIVE_DEPENDENCY_LATTICE_V0_2.md`.
