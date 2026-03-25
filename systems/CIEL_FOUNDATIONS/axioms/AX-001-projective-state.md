# AX-001 — Projective State Primacy

Status: **axiom**

## Formal statement
In a relational medium composed of information and potential, once a boundary of distinguishability is established and a nonzero primitive relational preference breaks the perfectly chaotic isotropic state, the minimal stable local state is not a raw amplitude vector but its phase-equivalence class.

Let the minimal local complex state be represented by

\[
\psi = \begin{pmatrix} a \\ b \end{pmatrix} \in \mathbb{C}^2 \setminus \{0\},
\qquad
\psi^\dagger \psi = 1.
\]

Physical locality is insensitive to global phase,

\[
\psi \sim e^{i\alpha}\psi,
\qquad
\alpha \in [0,2\pi),
\]

hence the physically meaningful local state space is the projective quotient

\[
[\psi] \in CP^1 = (\mathbb{C}^2 \setminus \{0\})/\mathbb{C}^{\times},
\]

with the normalized representative map

\[
\psi(\theta,\phi)=
\begin{pmatrix}
\cos(\theta/2) \\
 e^{i\phi}\sin(\theta/2)
\end{pmatrix},
\qquad
\theta \in [0,\pi],\; \phi \in [0,2\pi).
\]

Therefore the minimal emergent local geometry of state is

\[
CP^1 \simeq S^2,
\]

interpreted as the first projective sphere generated from chaos, potential, and relation.

## Dependency sketch
This axiom is a local formal consequence of the repo-level canonical postulate set:
- **P2** — primacy of relation over object,
- **P3** — relational medium of existence (information + potential),
- **P5** — spherical minimization under isotropy,
- **P6** — boundary as source of locality,
- **P7** — primitive relational preference and ordered phase motion,
- **P8** — attractor as local organization node.

Closest glossary neighbors:
- `../glossary/entries/chaos.md`
- `../glossary/entries/potential.md`
- `../glossary/entries/relation.md`
- `../glossary/entries/bloch_state.md`
- `../../../POSTULATES_CANON_PL_EN.md`

## Interpretation
This axiom does **not** yet assert the full downstream Hilbert ontology of later sectors. It states only the minimal local fact:

1. a local distinguishable region must carry a state,
2. the state is defined only up to global phase,
3. under isotropy and minimal boundary cost the first admissible projective geometry is `CP^1`,
4. equivalently, the first stable local chart is the Bloch sphere `S^2`.

In the current project ordering this is the first clean emergence step:

\[
\text{Chaos} \rightarrow \text{Potential} \rightarrow \text{Relation} \rightarrow CP^1.
\]

The object is therefore secondary. What appears first is a local projective organization of distinguishable phase, not a pre-given particle or classical point object.

## Operational consequences
- The first local state variable should be encoded projectively, not as an absolute complex amplitude.
- All downstream state initializers should respect phase equivalence.
- `bloch_state.md` is a downstream state object justified by this axiom, not an independent primitive.
- Closure, spectral identity, holonomy, and arithmetic seeds belong to later axioms and must not be imported here.

## Scope guard
This axiom intentionally excludes:
- white-thread structure,
- holonomic memory,
- `tau_i`,
- `A_ij`,
- `I0`,
- `CP^2` / neutrino-sector geometry.

Those are downstream layers and must not be smuggled into the `Chaos -> Potential -> Relation -> CP^1` foundation.