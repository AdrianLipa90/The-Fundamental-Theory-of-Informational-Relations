# The Space of Geometry — Referee Claim Firewall v1.1

Status: `TIR_SPACE_OF_GEOMETRY_REFEREE_CLAIM_FIREWALL_V1_1`

Purpose: freeze the publication-level scope, proof classes, domain distinctions, and reviewer-facing dependency boundaries of `paper/THE_SPACE_OF_GEOMETRY_V1_1.tex` before any release or merge decision.

## 1. Canonical manuscript surface

The canonical publication source is

`paper/THE_SPACE_OF_GEOMETRY_V1_1.tex`.

The local derivation starts its new work from the imported binary quantum carrier

\[
\mathcal H_2\cong\mathbb C^2.
\]

The parent TIR provenance chain supplies the route into this carrier. The publication theorem scope then begins with normalized two-level states and their affine hull.

## 2. Carrier / physical-domain firewall

The affine hull of normalized Hermitian two-level states is

\[
\mathcal A_2=\frac12I+\operatorname{Herm}_0(2),
\]

with translation carrier

\[
\boxed{
V=\operatorname{Herm}_0(2)\cong\mathbb R^3.
}
\]

For physical density-state endpoints the realizable single-edge coefficient domain is

\[
\boxed{
\mathcal R_{\rm phys}
=\{\mathbf d\cdot\boldsymbol\sigma:\ |\mathbf d|\le2\}.
}
\]

Therefore the publication uses two explicitly different domain types:

- `AFFINE_TRANSLATION_CARRIER`: the full real vector carrier `V`;
- `PHYSICAL_SINGLE_EDGE_DOMAIN`: the radius-two chord ball realized by pairs of physical density states.

The exact converse realization

\[
\mathbf r_x=-\frac12\mathbf d,
\qquad
\mathbf r_y=+\frac12\mathbf d
\]

shows that every coefficient vector with `|d|<=2` occurs for physical endpoints.

## 3. Relation normalization firewall

The canonical torsor displacement is

\[
\delta_{xy}=\rho_y-\rho_x.
\]

The exported Pauli-coordinate relation is

\[
\boxed{
\mathcal E_{xy}=2\delta_{xy}
=(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma.
}
\]

The factor `2` fixes the Bloch/Pauli coordinate normalization. A common positive dimensional conversion from this local norm to a laboratory length unit belongs to physical calibration downstream.

The dimensionless identities of the paper are invariant under a common positive rescaling of all local relation lengths.

## 4. Euclidean claim firewall

The metric structure used in the manuscript is

\[
\boxed{
\langle A,B\rangle=\frac12\operatorname{Tr}(AB),
}
\]

and in Pauli coefficients it is exactly

\[
\frac12\operatorname{Tr}
[(\mathbf a\cdot\boldsymbol\sigma)(\mathbf b\cdot\boldsymbol\sigma)]
=\mathbf a\cdot\mathbf b.
\]

Theorem E is therefore an exact inner-product identity on the local carrier:

\[
\|A+B\|^2
=\|A\|^2+\|B\|^2+2\langle A,B\rangle.
\]

Under the exact orthogonality condition

\[
\langle A,B\rangle=0,
\]

the endpoint relation obeys

\[
\boxed{a^2+b^2=c^2.}
\]

No tetrahedral theorem occurs upstream of this endpoint in the publication dependency DAG.

## 5. Physical Pythagorean certificate

Theorem R supplies an explicit physical-state family. For orthogonal unit vectors `u,v` and

\[
a^2+b^2\le1,
\]

choose

\[
\mathbf r_x=0,
\qquad
\mathbf r_y=a\mathbf u,
\qquad
\mathbf r_z=a\mathbf u+b\mathbf v.
\]

All endpoints lie in the Bloch ball and the relation vectors obey the same Pythagorean identity.

The deterministic publication certificate is

\[
\boxed{
a=\frac35,\quad b=\frac45,\quad c=1,}
\]

so

\[
\boxed{
\frac9{25}+\frac{16}{25}=1.
}
\]

This certificate is an exact model-level physical realization inside the admitted binary density-state domain.

## 6. Tetrahedral claim firewall

The finite-cell branch begins independently from the real affine carrier dimension:

\[
\dim_{\mathbb R}V=3.
\]

For `m` affine support points,

\[
\dim\operatorname{Aff}\{x_1,\ldots,x_m\}\le m-1,
\]

therefore full three-dimensional support requires

\[
m\ge4.
\]

At equality the minimal full-dimensional cell is

\[
\boxed{\Delta^3.}
\]

Its unlabeled automorphism group is

\[
\operatorname{Aut}(\Delta^3)\cong S_4,
\]

and the six edges form one `S_4` orbit. A5 supplies the scalar edge measure

\[
q_{ij}=\frac12\operatorname{Tr}(\mathcal E_{ij}^2),
\]

while A7 supplies invariance of that law on the intrinsic orbit. One orbit plus one invariant scalar edge law yields six equal edge lengths and therefore the regular tetrahedron.

This is the active publication proof of regularity. Moment isotropy is retained as a consequence/crosscheck downstream of regularity.

## 7. SIC convergence firewall

The qubit SIC branch is independently typed `INFORMATIONAL_CONVERGENCE_CROSSCHECK`.

A qubit has three independent Bloch coordinates and a normalized `m`-outcome probability vector has at most `m-1` independent real values, hence informational completeness requires

\[
m\ge4.
\]

The symmetric minimal rank-one qubit solution is tetrahedral and has

\[
\boxed{
\mathbf n_a\cdot\mathbf n_b=-\frac13
\quad(a\ne b).
}
\]

The same Gram invariant appears in the regular finite spatial frame. The publication records this equality as finite-frame convergence while preserving the separate physical types of measurement outcomes and spatial relation edges.

## 8. Local / global firewall

The manuscript endpoint is local relation geometry. It establishes:

- an origin-independent affine displacement;
- a real three-dimensional carrier;
- a positive rotationally invariant inner product;
- norm, angle and orthogonality;
- exact carrier-level Pythagorean closure;
- an exact physical-state Pythagorean realization class;
- the minimal finite full-dimensional tetrahedral cell and its regularity theorem.

The downstream geometry programme begins with transport between distinct local carriers, physical unit calibration, tetrahedral gluing/refinement, curvature/holonomy/torsion, and the TIR × Time spacetime closure.

The regular tetrahedral dihedral relation

\[
5\arccos(1/3)<2\pi<6\arccos(1/3)
\]

is the explicit local-to-global boundary marker used by the manuscript.

## 9. Proof-class ledger

| Publication claim | Class |
|---|---|
| `A_2 = I/2 + Herm_0(2)` | EXACT LINEAR ALGEBRA |
| `dim_R Herm_0(2)=3` | EXACT LINEAR ALGEBRA |
| `delta_xy=rho_y-rho_x` | EXACT AFFINE TORSOR DISPLACEMENT |
| endpoint composition | EXACT AFFINE IDENTITY |
| `SU(2)/{±I} ~= SO(3)` | EXACT REPRESENTATION THEORY |
| trace inner product / Pauli dot product | EXACT MATRIX ALGEBRA |
| physical chord domain `|d|<=2` | EXACT PHYSICAL-STATE DOMAIN THEOREM |
| Theorem E / Pythagorean identity | EXACT INNER-PRODUCT CONSEQUENCE |
| Theorem R / `3/5,4/5,1` | EXACT MODEL-LEVEL PHYSICAL REALIZATION |
| minimum four support vertices in 3D | EXACT AFFINE-DIMENSION THEOREM |
| `Aut(Delta^3)=S4`, one six-edge orbit | EXACT COMBINATORICS |
| regularity from A5+A7 orbit invariance | EXACT CONDITIONAL TIR AXIOM CROSSWALK |
| tetrahedral Gram `-1/3` | EXACT CONSEQUENCE OF REGULARITY |
| tetrahedral qubit SIC | STANDARD QUANTUM-INFORMATION CROSSCHECK |
| first-distinction route into `C^2` | IMPORTED PARENT TIR PROVENANCE |
| global carrier gluing and physical scale | DOWNSTREAM GEOMETRY PROGRAMME |

## 10. Referee challenge matrix

### Challenge A — "The three-dimensional carrier is merely assumed."

Response surface: Theorem 3 in the manuscript derives

\[
\dim_{\mathbb R}\operatorname{Herm}_0(2)=3
\]

from the trace-one affine hull of Hermitian `2x2` operators. The parent TIR root supplies the binary carrier `C^2`; the real three-dimensional translation space is then exact linear algebra.

### Challenge B — "The full affine carrier contains differences that physical states cannot realize."

Response surface: Theorem R-domain separates the full carrier from the physical chord subset and proves exactly

\[
\mathcal R_{\rm phys}\cong\mathbb B^3_2.
\]

The physical Pythagorean certificate is constructed entirely inside this subset.

### Challenge C — "Pythagoras is obtained by assuming a tetrahedral Euclidean cell."

Response surface: the publication DAG reaches Theorem E directly from affine composition plus the Hilbert--Schmidt/Pauli inner product. The tetrahedral branch forks separately from the common carrier.

### Challenge D — "The tetrahedron is selected through a SIC premise."

Response surface: Theorem T1 follows from affine dimension and Theorem T2 from intrinsic `S4` edge-orbit invariance under A5+A7. SIC enters afterward as an independent Gram-frame convergence check.

### Challenge E — "A local dimensionless norm is already a laboratory spatial distance."

Response surface: the manuscript uses the Pauli-normalized local relation norm as the model geometric measure. Physical unit calibration is explicitly assigned to the downstream geometry programme.

### Challenge F — "A regular tetrahedral local frame automatically supplies global flat three-space."

Response surface: the manuscript marks the global boundary by the regular-tetrahedron dihedral mismatch and routes gluing/refinement/curvature to the downstream programme.

## 11. Release criterion

The v1.1 publication candidate passes the referee firewall when all of the following are simultaneously verified:

1. the canonical manuscript contains the carrier/physical-domain distinction;
2. the radius-two physical chord theorem and its converse are present;
3. the exact `3/5,4/5,1` physical Pythagorean certificate is present;
4. the dependency audit is acyclic;
5. the tetrahedral branch has no incoming dependency into either Pythagorean endpoint;
6. the SIC branch remains crosscheck-only in the dependency graph;
7. the local/global and normalization/calibration boundaries are explicit;
8. XeLaTeX/PDF structural preflight passes on the exact branch head.

Verdict token:

`PASS_V1_1_REFEREE_CLAIM_FIREWALL`
