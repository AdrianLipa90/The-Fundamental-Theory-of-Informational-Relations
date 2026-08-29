# The Space of Geometry — Proof Dependency Audit v0.1

Status: `TIR_SPACE_OF_GEOMETRY_PUBLICATION_PROOF_AUDIT_V0_1`

Purpose: freeze the exact theorem dependency graph used by `paper/THE_SPACE_OF_GEOMETRY_V1_0.tex`, detect circular reasoning, and separate the direct Euclidean endpoint from the finite-cell tetrahedral branch.

## 1. Node classes

The publication chain is typed into four classes.

- `IMPORT`: result imported from the parent TIR foundations.
- `EXACT`: algebraic, affine, linear-algebraic, group-theoretic, or Euclidean theorem.
- `AXIOM_CROSSWALK`: a TIR axiom supplies the declared physical/geometric role of an exact mathematical structure.
- `CROSSCHECK`: mathematically independent convergence result used for corroboration, not as a premise of the main endpoint.

## 2. Canonical dependency graph

Let the nodes be:

`P0` — imported binary quantum carrier `H_2 ~= C^2`.

`C1` — normalized state affine hull

\[
\mathcal A_2=\frac12I+\operatorname{Herm}_0(2),
\qquad
\dim_{\mathbb R}\operatorname{Herm}_0(2)=3.
\]

`C2` — canonical ordered-pair torsor displacement

\[
\delta_{xy}=\rho_y-\rho_x.
\]

`C3` — generator normalization and covariance

\[
\mathcal E_{xy}=2(\rho_y-\rho_x),
\qquad
PSU(2)\cong SO(3).
\]

`C4` — invariant positive inner product

\[
\langle A,B\rangle=\frac12\operatorname{Tr}(AB).
\]

`E1` — additive endpoint composition

\[
\mathcal E_{xz}=\mathcal E_{xy}+\mathcal E_{yz}.
\]

`E2` — norm polarization identity

\[
\|A+B\|^2=\|A\|^2+\|B\|^2+2\langle A,B\rangle.
\]

`E3` — Pythagorean closure under orthogonality

\[
\boxed{a^2+b^2=c^2}.
\]

`T1` — minimal finite full-dimensional support in a real three-dimensional affine carrier requires four vertices, hence

\[
\Delta^3.
\]

`T2` — intrinsic simplex automorphism structure

\[
\operatorname{Aut}(\Delta^3)\cong S_4,
\]

with one six-edge orbit.

`T3` — A5+A7 edge-measure invariance on that intrinsic orbit.

`T4` — equal six edge measures imply a regular tetrahedron.

`Q1` — tetrahedral qubit SIC/tight-frame convergence with

\[
n_a\cdot n_b=-\frac13\quad(a\ne b).
\]

The active edges are

```text
P0 -> C1
C1 -> C2
C2 -> C3
C3 -> C4
C2 -> E1
C4 -> E2
E1 -> E3
E2 -> E3
C1 -> T1
T1 -> T2
C4 -> T3
T2 -> T3
T3 -> T4
C1 -> Q1
T4 -> Q1
```

The `Q1` edge from `T4` records equality of the spatial tetrahedral Gram frame with the SIC frame. `Q1` is not a premise of `T4` or `E3`.

## 3. Direct Euclidean branch

The shortest path to the paper endpoint is

\[
\boxed{
P0\to C1\to C2\to(C3,C4,E1,E2)\to E3.
}
\]

No tetrahedral node occurs on every path from `P0` to `E3`. Therefore

\[
\boxed{
\text{Pythagorean closure is independent of tetrahedral regularity.}
}
\]

This protects the paper from the earlier possible circular ordering in which the tetrahedron could appear to be required before the Euclidean inner-product identity.

## 4. Finite-cell branch

The finite-cell theorem branches from the same common carrier:

\[
\boxed{
C1\to T1\to T2\to T3\to T4.
}
\]

Here the logic is:

1. real affine dimension three fixes the minimum number of full-dimensional support vertices to four;
2. four affinely independent vertices define the abstract `3`-simplex;
3. its unlabeled automorphism group is `S_4` and its six edges form one orbit;
4. A5 supplies the scalar edge measure and A7 supplies invariance of that law under the intrinsic simplex automorphisms;
5. one orbit plus invariant scalar measure gives six equal edge lengths;
6. a nondegenerate tetrahedron with six equal edges is regular.

No moment-isotropy assumption and no SIC premise is active in this shortest regularity proof.

## 5. SIC role firewall

The qubit informational branch is typed `CROSSCHECK`.

A generic qubit has three independent Bloch coordinates. A normalized `m`-outcome probability vector supplies at most `m-1` independent real values, hence informational completeness requires

\[
m\ge4.
\]

The symmetric minimal rank-one qubit solution is tetrahedral. Its Gram geometry agrees with the regular spatial simplex:

\[
\boxed{n_a\cdot n_b=-\frac13.}
\]

The publication may state convergence of the two finite frames. Physical identity of measurement outcome and spatial adjacency is not required by Theorem E or Theorem T.

## 6. Imported-root firewall

The paper begins new geometric work at `P0 = C^2`. The parent TIR first-distinction chain remains provenance:

\[
0\to P\to\text{DISTINCTION}\to\{N,S\}\to\frac12\to\ln2\to\mathbb C^2.
\]

The publication therefore has two proof scopes:

- parent provenance for the route into `C^2`;
- self-contained local geometry derivation from `C^2` to `E3` and `T4`.

## 7. Scale firewall

The structural relation is the torsor displacement

\[
\delta_{xy}=\rho_y-\rho_x.
\]

The factor `2` in

\[
\mathcal E_{xy}=2\delta_{xy}
\]

is the Pauli/Bloch generator normalization. It fixes the coordinate convention, while a physical dimensional length scale remains a downstream calibration layer.

Thus the dimensionless Pythagorean identity is insensitive to a common positive scale factor.

## 8. Publication verdict

The v1.0 theorem graph is acyclic and has one common carrier followed by two parallel branches:

\[
\boxed{
\operatorname{Herm}_0(2)
\to
\begin{cases}
\text{Euclidean branch}\to\text{Pythagoras},\\
\text{finite-cell branch}\to\text{regular tetrahedron}.
\end{cases}
}
\]

The tetrahedral SIC result is an independent convergence crosscheck.

Publication status under this audit:

`PASS_LOCAL_DEPENDENCY_GRAPH`.
