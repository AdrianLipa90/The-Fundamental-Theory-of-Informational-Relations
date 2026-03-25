# AX-003 — Primitive Relational Preference and Ordered Phase Motion

Status: **axiom**

## Formal statement
Once a local distinguishable state exists, any nonzero primitive relational preference breaks exact isotropy of continuation and induces ordered phase motion around the local organization node.

Let a minimal relation between two local state sectors be written as

\[
R_{ij} = w_{ij} e^{i\phi_{ij}},
\qquad
w_{ij} > 0,
\]

with amplitude coupling \(w_{ij}\) and relative phase \(\phi_{ij}\). In the perfectly isotropic limit no direction in phase continuation is preferred. If there exists a nonzero primitive relational preference

\[
\varepsilon_{ij} \neq 0,
\]

then the continuation of the local state is no longer indifferent under all infinitesimal phase directions. The ordered part of evolution is therefore governed by a phase-gradient field

\[
\omega_{ij} := \partial_t \phi_{ij},
\]

or, more generally, by a local phase-flow vector

\[
V_\phi := \nabla \phi.
\]

A nonzero \(V_\phi\) defines an oriented continuation around the local distinguishable region. Under the spherical minimality established by AX-001 and AX-002, the minimal persistent ordered response is rotational rather than translational:

\[
\varepsilon \neq 0
\quad\Rightarrow\quad
V_\phi \neq 0
\quad\Rightarrow\quad
\text{primitive local rotational dynamics.}
\]

Thus the first ordered dynamical structure of a local state is a phase rotation on the projective sphere,

\[
CP^1 \simeq S^2,
\]

and the minimal local dynamical degree of freedom is an oriented phase motion around a local axis.

## Dependency sketch
This axiom continues directly from:
- **P3** — relational medium as information + potential,
- **P5** — spherical minimization,
- **P6** — boundary as source of locality,
- **P7** — nonzero primitive preference induces symmetry breaking and rotational flow,
- **P8** — attractor as local vortex / organization node,
- **AX-001** — first local state chart is `CP^1`,
- **AX-002** — locality persists only when boundary distinction closes sufficiently.

Closest glossary neighbors:
- `../glossary/entries/relation.md`
- `../glossary/entries/potential.md`
- `../glossary/entries/bloch_state.md`
- `../../../POSTULATES_CANON_PL_EN.md`

## Interpretation
AX-001 gave the first local state geometry. AX-002 gave the persistence condition for locality. AX-003 gives the first **dynamics** of that local state.

The point is:

1. relation is not only existence of coupling, but also phase asymmetry,
2. nonzero relational preference breaks exact isotropy,
3. broken isotropy induces ordered phase continuation,
4. on the minimal local projective sphere the first stable continuation is rotational,
5. this is the primitive origin of local spin-like behavior.

At this level, `spin` is used in the minimal dynamical sense: an oriented rotational response of the local phase state around a local axis. This axiom does **not yet** impose half-integer quantization, spinor closure classes, Berry holonomy, or transport spectra. Those are later refinements of the primitive rotational fact established here.

The current emergence chain therefore becomes:

\[
\text{Chaos}
\rightarrow
\text{Potential}
\rightarrow
\text{Relation}
\rightarrow
\text{Boundary}
\rightarrow
\text{Locality}
\rightarrow
CP^1
\rightarrow
\text{ordered phase motion}.
\]

## Operational consequences
- The first local dynamical variable should be represented by phase flow, not by absolute position.
- A local axis is emergent from ordered phase continuation; it is not inserted by hand.
- Rotational organization is earlier than spectral identity and earlier than holonomic memory.
- Any later notion of spin, chirality, or circulation must reduce consistently to this primitive rotational phase response.

## Scope guard
This axiom intentionally excludes:
- spinor closure quantization,
- Berry phase and white-thread transport,
- spectral identity from holonomy,
- `tau_i`, `A_ij`, `I0`,
- `CP^2` and neutrino / CP sectors.

Those belong to later sectors. Here we establish only the first ordered phase dynamics after locality emerges.