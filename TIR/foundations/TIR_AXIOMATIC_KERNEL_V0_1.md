# TIR Axiomatic Kernel v0.1

Status: `FOUNDATIONAL_AXIOM_SET_CANDIDATE`

Scope: TIR-only foundational kernel. This document records the A0 relational-existence root together with the eight owner-specified A1--A8 axioms, giving each an explicit mathematical type, dependency role, and validation boundary. A0 fixes the semantics of the zero layer; downstream theorems require their own derivations and standard mathematical dependencies.

## Axiom A0 — Relational Existence and Relational Zero

**Statement.** TIR admits an entity as existent only through a realized distinction or relation that makes it identifiable in the relational presentation.

Write

\[
\mathfrak R=(X,\mathcal D),
\]

with support set \(X\) and realized distinction/relation set \(\mathcal D\). The pre-object zero layer is

\[
\boxed{\mathfrak Z_{\rm rel}=(\varnothing,\varnothing).}
\]

It is not a point, not a singleton, and not a reified object called "nothing". It is zero realized relational structure. Hence

\[
\boxed{\nexists x\;(x\in X_0).}
\]

The logical status is exact but scoped: once existence is defined relationally in TIR, the absence of an existent object in the empty relational presentation is forced by definition. The definition itself is the TIR ontological entry rule, not a theorem of unrestricted logic independent of semantics.

Canonical owner: \`TIR/foundations/TIR_RELATIONAL_ZERO_AXIOM_V0_1.md\`.

## Axiom A1 — Point Minimality

**Statement.** The least nonzero support is a point.

TIR formalization:

\[
\boxed{\mathcal P=\{p\},\qquad |\mathcal P|=1.}
\]

This is the minimal non-empty support after \(\mathfrak Z_{\rm rel}\). It must not be identified with relational zero:

\[
\boxed{\mathfrak Z_{\rm rel}\neq\mathcal P.}
\]

The unresolved point \((\mathcal P,\varnothing)\) is only the minimal support candidate. By A0 it is not yet a fully admitted existent TIR object until a nontrivial distinction is realized on its state/aspect domain.

A1 therefore fixes support minimality without smuggling an object into the zero layer.

## Axiom A2 — Quantum Point

**Statement.** A point is a quantum object.

TIR formalization: every minimal carrier admits a quantum state representation

\[
\boxed{|\mathcal P\rangle\in\mathcal H,\qquad \langle\mathcal P|\mathcal P\rangle=1,}
\]

with complex amplitudes and phase available when the carrier is relationally resolved into alternatives.

A2 is a physical postulate of TIR. At the unresolved point-support layer it asserts only quantum representability; it does not by itself fix a two-dimensional Hilbert space, \(\mathbb C^2\), \(\mathbb{CP}^1\), or a Bloch sphere. The minimal \(\mathbb C^2\) carrier is admitted only after the minimal nontrivial distinction has produced the two alternatives \(\{N,S\}\). The Hilbert-space machinery used after this postulate follows standard quantum mathematics.

## Axiom A3 — Information Primacy

**Statement.** Information is the fundamental building block of reality.

TIR formalization:

\[
\boxed{\text{physical structure is represented by distinguishable informational relations}.}
\]

For a probability partition \(\mathbf p\), distinguishability is quantified locally by Shannon information

\[
H(\mathbf p)=-\sum_i p_i\ln p_i.
\]

The undivided carrier has

\[
H((1))=0.
\]

The first nontrivial symmetric distinction has two alternatives and therefore

\[
H\!\left(\frac12,\frac12\right)=\ln2.
\]

## Axiom A4 — Spherical Geometric Efficiency

**Statement.** The most efficient geometric figure is the sphere.

TIR mathematical typing: geometric efficiency must be attached to an explicit functional. The canonical TIR efficiency functional is minimal boundary measure at fixed enclosed volume. In three dimensions the isoperimetric inequality is

\[
\boxed{A^3\ge 36\pi V^2,}
\]

with equality for the sphere.

Thus, for the declared boundary/volume criterion, the sphere is the extremal isotropic enclosure.

A4 is used as the TIR geometric-selection postulate when an isotropic bounded realization is required. Other efficiency functionals must be declared separately.

## Axiom A5 — Arithmetic Measures Geometry

**Statement.** Arithmetic is a measure of geometry.

TIR formalization: arithmetic quantities encode geometric invariants and relational counts. Canonical examples include

\[
n=\frac{1}{2\pi}\oint d\theta\in\mathbb Z,
\]

for winding, together with discrete counts of intersections, orbit closures, covering degree, multiplicity, and graph incidence.

The axiom is therefore represented as

\[
\boxed{\text{geometric relation}\xrightarrow{\text{invariant}}\text{arithmetic value}.}
\]

## Axiom A6 — Natural Numbers from Complex Phase Closure

**Statement.** Natural numbers derive from complex numbers.

TIR formalization: natural numbers arise as discrete closure indices of complex phase structure.

Let

\[
z=e^{i\theta}.
\]

A closed phase orbit satisfies

\[
z^n=1
\]

for an integer closure index \(n\). Equivalently,

\[
\theta=\frac{2\pi k}{n}.
\]

TIR therefore uses the typed relation

\[
\boxed{\text{complex phase closure}\longrightarrow n\in\mathbb N}
\]

as the operational content of A6. This is an emergence/encoding statement inside TIR, rather than a replacement for the standard set-theoretic inclusion chain among number systems.

## Axiom A7 — Universal Symmetry

**Statement.** The universe is symmetric.

TIR formalization: fundamental relational laws are symmetry-governed. For a symmetry group \(G\) acting on state space \(X\), the law carrier \(\mathcal L\) satisfies

\[
\boxed{\mathcal L(g\cdot x)=\mathcal L(x),\qquad g\in G.}
\]

Observed asymmetry may arise through state selection, orientation, bifurcation, or symmetry breaking while the parent law remains symmetry-governed.

The minimal first distinction is therefore represented by a pole-exchange symmetry

\[
J:N\leftrightarrow S,
\qquad J^2=\mathrm{id}.
\]

Its symmetric fixed share is

\[
\boxed{p_N=p_S=\frac12.}
\]

## Axiom A8 — Paradox Stabilization

**Statement.** Paradoxes are stabilizers of reality.

TIR formalization: a paradox marks a boundary at which two valid relational descriptions cannot be consistently identified inside the current projection and therefore trigger a higher-order closure.

Let two chart-dependent statements be valid in contexts \(C_1,C_2\):

\[
P\mid C_1,\qquad \neg P\mid C_2.
\]

The TIR paradox operator does not collapse them into an untyped contradiction. It lifts them to a context-bearing state

\[
\boxed{\mathfrak P:(P,C_1;\neg P,C_2)\mapsto\widetilde X,}
\]

where a closure law must specify how both projections arise.

The stabilization rule is

\[
\boxed{\text{apparent contradiction}\rightarrow\text{context lift}\rightarrow\text{closure constraint}.}
\]

A8 is a methodological/structural axiom. A named mathematical paradox still retains all theorem-specific hypotheses required by standard mathematics.

## Minimal generative spine

The first four operational steps of the kernel are

\[
\boxed{
\mathfrak Z_{\rm rel}
\xrightarrow{A1}
\mathcal P
\xrightarrow{\text{minimal nontrivial distinction}}
\{N,S\}
\xrightarrow{A2}
\mathcal H_2
\xrightarrow{A3}
\text{normalized informational relation}
\xrightarrow{A7}
\{N,S\}_{\rm symmetric}
\xrightarrow{}
\left(\frac12,\frac12\right)
\xrightarrow{H}
\ln2.
}
\]

This binds directly to the existing TIR half-seam:

\[
\operatorname{Fix}(u\mapsto1-u)=\left\{\frac12\right\},
\qquad
H_2(1/2)=\ln2.
\]

The resulting information value enters the existing TIR normalization

\[
\boxed{\kappa=\frac{\ln2}{24\pi}.}
\]

## Quantum branch

The first binary distinction lifts the quantum carrier to the minimal two-alternative Hilbert space

\[
\mathcal H_2\cong\mathbb C^2.
\]

The equal-share coherent family is

\[
|\psi_{1/2}(\varphi)\rangle
=\frac{|N\rangle+e^{i\varphi}|S\rangle}{\sqrt2}.
\]

From here the dependency branches are explicit:

\[
\mathbb C^2
+\text{strongly continuous unitary flow}
\longrightarrow
\text{self-adjoint generator}
\longrightarrow
\text{Schrödinger evolution},
\]

and

\[
\mathbb C^2
+\text{multiple distinction axes}
\longrightarrow
[\sigma_i,\sigma_j]\ne0
\longrightarrow
\text{Robertson--Heisenberg uncertainty}.
\]

The axiomatic kernel supplies the carrier; the generator and uncertainty theorems retain their standard hypotheses.

## Geometric and arithmetic branch

A4, A5, A6 and A7 combine into the typed ladder

\[
\boxed{
\text{two-pole orientation}
\rightarrow
S^2
\rightarrow
\text{phase/rotation structure}
\rightarrow
\text{winding and closure indices}
\rightarrow
\mathbb N.
}
\]

For the quantum two-state carrier, the standard projective identification

\[
\mathbb{CP}^1\cong S^2
\]

provides the canonical Bloch-sphere realization.

## Paradox branch and Banach--Tarski crosswalk

The Banach--Tarski theorem sits far downstream of the same oriented-sphere branch:

\[
S^2
\rightarrow
SO(3)
\supset
F_2
\rightarrow
\text{paradoxical group action}
\rightarrow
\text{choice-based orbit representatives}
\rightarrow
\text{Banach--Tarski}.
\]

A8 classifies the paradox as a closure/stability boundary in the TIR crosswalk. The theorem itself retains the standard group-action and choice dependencies.

## Axiom-to-result firewall

The axioms are parents, not substitutes for proofs. The first exact result already available inside this branch is the symmetric binary half-seam:

\[
A3+A7+\text{binary first distinction}
\Longrightarrow
p_N=p_S=\frac12
\Longrightarrow
H_2=\ln2.
\]

The following edges require additional mathematical hypotheses beyond the eight axioms:

\[
\mathbb C^2+\text{strong continuity and unitarity}
\Longrightarrow
\text{Schrödinger generator equation},
\]

\[
\mathbb C^2+\text{self-adjoint incompatible observables}
\Longrightarrow
\text{Robertson--Heisenberg relation},
\]

\[
S^2+SO(3)+F_2+\text{paradoxical action}+\mathrm{Choice}
\Longrightarrow
\text{Banach--Tarski}.
\]

This firewall keeps the common TIR root explicit while preserving the independent theorem assumptions of every downstream branch.

## First exact derivation frontier

The immediate theorem programme is intentionally narrow. Before extending the kernel toward dynamics, TIR should close the following chain in order:

\[
\boxed{
A0+A1+A3+A7
\rightarrow
\Delta_1
\rightarrow
\{N,S\}
\rightarrow
J^2=\mathrm{id}
\rightarrow
\operatorname{Fix}(J)=\left\{\frac12\right\}
\rightarrow
H_2=\ln2.
}
\]

The first open derivational question is therefore the status of \(\Delta_1\): the minimal rule that turns the undivided point-carrier into the first non-zero distinction while preserving the parent symmetry. Closing that rule is the next TIR foundation gate.

## Dependency graph

```text
A0 RELATIONAL EXISTENCE / ZERO
  -> A1 POINT MINIMALITY
      -> FIRST DISTINCTION
  -> A2 QUANTUM POINT
  -> A3 INFORMATION PRIMACY
      -> FIRST DISTINCTION
          -> A7 SYMMETRIC POLE EXCHANGE
              -> HALF SEAM 1/2
                  -> ln2
                  -> kappa numerator
              -> C^2
                  -> UNITARY FLOW -> SCHRODINGER
                  -> MULTIPLE AXES -> HEISENBERG/ROBERTSON
              -> A4 SPHERICAL REALIZATION
                  -> S^2 / SO(3)
                      -> A5 ARITHMETIC GEOMETRIC INVARIANTS
                      -> A6 COMPLEX PHASE CLOSURE -> NATURAL INDICES
                      -> FREE GROUP ACTION + CHOICE -> BANACH-TARSKI
A8 PARADOX STABILIZATION
  -> contextual lift / closure gate across branches
```

## Claim classes

| Axiom | TIR type |
|---|---|
| A0 relational existence / zero | FOUNDATIONAL DEFINITION + EXACT DEFINITIONAL CONSEQUENCE |
| A1 point minimality | FOUNDATIONAL SUPPORT-MINIMALITY POSTULATE |
| A2 quantum point | FOUNDATIONAL PHYSICAL POSTULATE |
| A3 information primacy | FOUNDATIONAL INFORMATIONAL POSTULATE |
| A4 sphere efficiency | GEOMETRIC SELECTION POSTULATE WITH ISOPERIMETRIC TYPING |
| A5 arithmetic measures geometry | STRUCTURAL CORRESPONDENCE POSTULATE |
| A6 naturals from complex phase closure | STRUCTURAL EMERGENCE POSTULATE |
| A7 universal symmetry | FOUNDATIONAL SYMMETRY POSTULATE |
| A8 paradox stabilization | META-STRUCTURAL CLOSURE POSTULATE |

## Crosslinks

The existing TIR-owned half-seam remains the first exact derived bridge:

`TIR/integration/TIR_RELATIONAL_HALF_SEAM_CROSSLINK_V0_1.md`

The canonical zero semantics is owned by:

`TIR/foundations/TIR_RELATIONAL_ZERO_AXIOM_V0_1.md`

The zero-to-first-distinction construction remains the detailed branch expansion:

`TIR/integration/TIR_ZERO_FIRST_DISTINCTION_FOUNDATION_V0_1.md`

Sibling repositories remain crosslink consumers only in this pass.
