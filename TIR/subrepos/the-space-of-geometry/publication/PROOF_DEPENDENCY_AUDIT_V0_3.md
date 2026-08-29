# The Space of Geometry — Proof Dependency Audit v0.3

Status: `TIR_SPACE_OF_GEOMETRY_PUBLICATION_V1_1_SYNCHRONIZED_PROOF_AUDIT`

Purpose: bind the hardened local dependency graph to `paper/THE_SPACE_OF_GEOMETRY_V1_1.tex` and verify that the physical-state realizability theorem is a constructive branch from the common carrier rather than a replacement for the carrier-level Euclidean theorem.

## 1. Common carrier

The manuscript begins new geometric work at the imported binary carrier and derives

\[
\boxed{
\mathbb C^2
\to
\mathcal A_2=\frac12I+V
\to
V=\operatorname{Herm}_0(2)\cong\mathbb R^3
}
\]

with canonical endpoint relation

\[
\boxed{
\mathcal E_{xy}=2(\rho_y-\rho_x)
}
\]

and invariant metric

\[
\boxed{
\langle A,B\rangle=\frac12\operatorname{Tr}(AB).
}
\]

## 2. Three publication outputs

The current manuscript has three theorem outputs from the common carrier.

### E — carrier Euclidean closure

\[
\mathcal E_{xz}=\mathcal E_{xy}+\mathcal E_{yz}
\]

and the invariant inner product give

\[
\boxed{a^2+b^2=c^2}
\]

for orthogonal consecutive relations.

### R — physical-state realization

For physical density-state endpoints the exact single-edge relation domain is

\[
\boxed{
\mathcal R_{\rm phys}
=\{\mathbf d\cdot\boldsymbol\sigma:\ |\mathbf d|\le2\}.
}
\]

Theorem R constructs a physical right-triangle family for

\[
a^2+b^2\le1,
\]

with exact normalized certificate

\[
\boxed{
\frac9{25}+\frac{16}{25}=1.
}
\]

### T — minimal finite cell

Real affine dimension three gives

\[
\boxed{\Delta^3}
\]

as minimal full-dimensional finite support. The intrinsic edge orbit under

\[
\operatorname{Aut}(\Delta^3)\cong S_4
\]

combined with A5 measure and A7 law invariance gives equal six edge lengths and therefore the regular tetrahedron.

## 3. Independent informational convergence

The qubit SIC branch is a crosscheck. It converges on

\[
\boxed{n_a\cdot n_b=-\frac13\qquad(a\ne b)}
\]

without serving as a premise of E, R, or T.

## 4. Carrier-domain firewall

The manuscript explicitly distinguishes

\[
\boxed{V=\operatorname{Herm}_0(2)\cong\mathbb R^3}
\]

from

\[
\boxed{\mathcal R_{\rm phys}\cong\mathbb B^3_2.}
\]

The first is the affine translation carrier. The second is the bounded single-edge subset realized by physical endpoints in one local binary state fiber. Since the latter contains a neighborhood of zero, it spans all three carrier directions.

## 5. Dependency firewall

The active dependency graph is acyclic and obeys:

- tetrahedral nodes are not ancestors of carrier Pythagoras;
- tetrahedral nodes are not ancestors of physical-state Pythagoras;
- the SIC node is not an ancestor of any main theorem endpoint;
- physical-state realizability depends on the Bloch-domain constraint plus the already derived relation and metric;
- global gluing and dimensional scale remain downstream.

Thus no finite-cell theorem is used to manufacture the Euclidean identity it later inherits.

## 6. Publication synchronization

Canonical manuscript:

`paper/THE_SPACE_OF_GEOMETRY_V1_1.tex`

Canonical research spine:

`RESEARCH_SPINE_V0_10.md`

Canonical physical-realizability theorem:

`foundations/PHYSICAL_RELATION_CHORD_REALIZABILITY_V0_1.md`

Canonical deterministic publication audit:

`validation/publication_proof_dependency_audit_v0_3.py`

## 7. Verdict

\[
\boxed{
\text{COMMON CARRIER}
\to
\begin{cases}
E:\ \text{Pythagoras},\\
R:\ \text{physical Pythagoras},\\
T:\ \text{regular tetrahedron},
\end{cases}
\qquad
Q:\ \text{independent SIC convergence}.
}
\]

Publication status:

`PASS_V1_1_SYNCHRONIZED_LOCAL_PROOF_GRAPH`.
