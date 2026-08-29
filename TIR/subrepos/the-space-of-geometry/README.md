# The Space of Geometry

Status: `TIR_SUBREPO_V1_1_REFEREE_FIREWALL_CANDIDATE`

Working title:

> **The Space of Geometry: From First Distinction to Pythagoras**

Current manuscript source:

`paper/THE_SPACE_OF_GEOMETRY_V1_1.tex`

Current research spine and publication controls:

- `RESEARCH_SPINE_V0_10.md`
- `publication/PROOF_DEPENDENCY_AUDIT_V0_3.md`
- `publication/REFEREE_CLAIM_FIREWALL_V1_1.md`

The common local carrier is

\[
\mathbb C^2
\to
\rho_x
\to
\mathcal A_2
\to
\delta(\rho_x,\rho_y)
\to
\operatorname{Herm}_0(2)\cong\mathbb R^3.
\]

The canonical local relation and metric are

\[
\mathcal E_{xy}=2(\rho_y-\rho_x),
\qquad
\langle A,B\rangle=\frac12\operatorname{Tr}(AB).
\]

For physical binary density states, the exact single-edge reachable set is

\[
\boxed{
\mathcal R_{\rm phys}
=\{\mathbf d\cdot\boldsymbol\sigma:\ |\mathbf d|\le2\}.
}
\]

Every vector in this radius-two coefficient ball is realized by the physical endpoints

\[
\mathbf r_x=-\frac12\mathbf d,
\qquad
\mathbf r_y=+\frac12\mathbf d.
\]

The Pythagorean endpoint has an explicit physical-state realization. For orthogonal unit directions and

\[
a^2+b^2\le1,
\]

the states

\[
\mathbf r_x=0,
\qquad
\mathbf r_y=a\mathbf u,
\qquad
\mathbf r_z=a\mathbf u+b\mathbf v
\]

are physical and satisfy

\[
\boxed{a^2+b^2=c^2.}
\]

The exact normalized certificate is

\[
\boxed{
\frac9{25}+\frac{16}{25}=1
}
\]

from \(a=3/5\), \(b=4/5\), \(c=1\).

From the same three-real-dimensional carrier the finite-cell branch gives

\[
\operatorname{Herm}_0(2)
\to
\Delta^3
\xrightarrow{A5+A7}
\text{regular tetrahedron},
\]

while the qubit-SIC branch independently converges on the same tetrahedral Gram frame

\[
n_a\cdot n_b=-\frac13\qquad(a\ne b).
\]

The synchronized publication dependency graph is acyclic and separates three outputs from the common carrier:

\[
\operatorname{Herm}_0(2)
\to
\begin{cases}
\text{Theorem E: Euclidean identity}\to\text{Pythagoras},\\
\text{Theorem R: physical-state realization}\to\text{physical Pythagoras},\\
\text{Theorems T1/T2: minimal finite support}\to\text{regular tetrahedron}.
\end{cases}
\]

Theorem Q remains an independent tetrahedral SIC convergence crosscheck.

The referee firewall freezes six reviewer-facing boundaries:

- full affine carrier versus physical single-edge chord domain;
- torsor displacement versus Pauli/Bloch normalization;
- exact local inner-product identity versus physical-state realization;
- Euclidean/Pythagorean branch versus finite-cell tetrahedral branch;
- spatial finite-frame theorem versus SIC convergence crosscheck;
- local relation geometry versus downstream physical calibration and global carrier gluing.

Physical unit calibration and gluing of distinct local carriers into global spatial extent belong to the downstream geometry programme.

Current release surfaces:

- `paper/THE_SPACE_OF_GEOMETRY_V1_1.tex`
- `RESEARCH_SPINE_V0_10.md`
- `foundations/CANONICAL_SPATIAL_RELATION_EXTRACTION_V0_1.md`
- `foundations/PHYSICAL_RELATION_CHORD_REALIZABILITY_V0_1.md`
- `foundations/A5_A7_SIMPLEX_EDGE_ORBIT_REGULARITY_V0_1.md`
- `publication/PROOF_DEPENDENCY_AUDIT_V0_3.md`
- `publication/REFEREE_CLAIM_FIREWALL_V1_1.md`
- `validation/space_of_geometry_spine_v0_10.py`
- `validation/physical_relation_chord_realizability_v0_1.py`
- `validation/publication_proof_dependency_audit_v0_3.py`
- `validation/referee_claim_firewall_v1_1.py`
- `.github/workflows/compile-space-of-geometry.yml`

The compile workflow targets v1.1 and now performs the synchronized dependency audit, exact physical-state realizability audit, referee claim firewall, XeLaTeX build, PDF structural preflight, and content-addressed receipt generation.

TIR remains the parent Source of Truth for the primitive axioms and first-distinction chain.
