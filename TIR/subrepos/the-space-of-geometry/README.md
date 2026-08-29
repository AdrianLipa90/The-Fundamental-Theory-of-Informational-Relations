# The Space of Geometry

Status: `TIR_SUBREPO_V1_0_RELEASE_CANDIDATE_REALIZABILITY_HARDENED`

Working title:

> **The Space of Geometry: From First Distinction to Pythagoras**

Final publication source:

`paper/THE_SPACE_OF_GEOMETRY_V1_0.tex`

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

The Pythagorean endpoint is physically realizable inside the Bloch ball. For orthogonal unit directions and

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

The fundamental paper terminates at local Pythagorean closure. Physical unit calibration and gluing of distinct local carriers into global spatial extent belong to the downstream geometry programme.

Current publication surfaces:

- `paper/THE_SPACE_OF_GEOMETRY_V1_0.tex`
- `RESEARCH_SPINE_V0_10.md`
- `foundations/CANONICAL_SPATIAL_RELATION_EXTRACTION_V0_1.md`
- `foundations/PHYSICAL_RELATION_CHORD_REALIZABILITY_V0_1.md`
- `foundations/A5_A7_SIMPLEX_EDGE_ORBIT_REGULARITY_V0_1.md`
- `validation/physical_relation_chord_realizability_v0_1.py`

TIR remains the parent Source of Truth for the primitive axioms and first-distinction chain.
