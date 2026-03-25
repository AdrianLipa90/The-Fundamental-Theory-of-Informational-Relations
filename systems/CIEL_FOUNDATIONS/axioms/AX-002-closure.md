# AX-002 — Boundary Closure and Locality

Status: **axiom**

## Formal statement
A local state can persist only if the boundary of distinguishability that defines it is sufficiently closed to separate interior from exterior under relational evolution.

Let the relational medium be written schematically as

\[
\mathcal M_{\mathrm{rel}} = (I,\Pi),
\]

where \(I\) denotes information and \(\Pi\) potential. A local region \(\Omega\subset \mathcal M_{\mathrm{rel}}\) becomes physically meaningful only when there exists a boundary of distinguishability

\[
\partial\Omega
\]

such that the inside and outside are not dynamically indistinguishable. Define the contrast across the boundary by a generic boundary mismatch functional

\[
\Delta_{\partial\Omega}
:=
\big\| (I,\Pi)_{\mathrm{in}} - (I,\Pi)_{\mathrm{out}} \big\|_{\partial\Omega}.
\]

A necessary condition for locality is

\[
\Delta_{\partial\Omega} > 0.
\]

A necessary condition for persistence is that the boundary be closure-admissible, i.e. that the region does not dissolve immediately back into the undifferentiated medium. In minimal form this means that \(\partial\Omega\) must support a stable closed distinguishability class:

\[
\partial\Omega \sim S^1
\]

at the level of the first local section, so that a bounded interior can exist. Under isotropy and spherical minimization, the corresponding minimal local state chart is the projective sphere established in AX-001:

\[
\Omega_{\mathrm{state}} \leadsto CP^1 \simeq S^2.
\]

Therefore:

\[
\boxed{
\text{boundary} \Rightarrow \text{locality},
\qquad
\text{closure-admissible boundary} \Rightarrow \text{persistent local identity}.
}
\]

## Dependency sketch
This axiom is a direct continuation of the repo-level canonical postulates:
- **P2** — primacy of relation over object,
- **P3** — relational medium of existence,
- **P5** — spherical minimization,
- **P6** — boundary as source of locality,
- **P7** — primitive relational preference generating ordered motion,
- **AX-001** — emergence of the first projective local state chart `CP^1`.

Closest glossary neighbors:
- `../glossary/entries/relation.md`
- `../glossary/entries/potential.md`
- `../glossary/entries/bloch_state.md`
- `../../../POSTULATES_CANON_PL_EN.md`

## Interpretation
AX-001 established what the first local state geometry is once locality exists. AX-002 states the condition under which locality itself can persist.

The key distinction is:

1. **Boundary** creates distinction.
2. **Distinction** creates locality.
3. **Closure-admissibility** prevents immediate reabsorption into chaos.
4. **Persistent locality** is the first operational meaning of local identity.

At this stage, closure does **not** yet mean holonomic memory, white-thread transport, or quantized loop phase. It means only that the system supports a bounded local region capable of remaining distinct long enough to host a state.

In the current ordering the emergence chain becomes:

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
CP^1.
\]

## Operational consequences
- Any downstream local object must be representable as an interior/exterior distinction sustained by a closure-admissible boundary.
- Local identity is not primitive; it is licensed by boundary persistence.
- The first closed form required by the theory is topological closure of distinguishability, not yet spectral or holonomic closure.
- White threads, residual phase, and memory traces must be deferred to later axioms.

## Scope guard
This axiom intentionally excludes:
- Berry transport,
- white-thread channels,
- holonomic memory,
- transport spectra,
- arithmetic seeds,
- spinor closure classes,
- neutrino / CP sectors.

Those belong to later closure refinements. Here, `closure` means only the minimal persistent boundedness of a local distinguishable region.