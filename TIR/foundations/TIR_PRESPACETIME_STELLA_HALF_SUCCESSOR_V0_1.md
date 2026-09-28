# TIR Pre-Spacetime Stella Half-Successor v0.1

Status: EXACT_PRESPACETIME_STELLA_ALTERNATION / PRETIME_SUCCESSOR_INTERFACE_TO_IDT

## 1. Premise boundary

This construction is upstream of both physical time and physical space.

The words sphere, tetrahedron, rotation and vertex refer here to a relational/state-space representation. They do not presuppose an ambient physical \(\mathbb R^3\) or a pre-existing temporal coordinate.

The upstream Stella carrier is

\[
\Sigma_\star=T_+\cup T_-,
\]

with the regular tetrahedral Gram relation already established in TIR_STELLA_DISTINCTION_HOLONOMY_BRIDGE_V0_1.md.

## 2. Vertex-label quotient

For one tetrahedral sector,

\[
G_{ij}=
\begin{cases}
1,&i=j,\\
-1/3,&i\ne j.
\end{cases}
\]

Every permutation \(p\in S_4\) preserves this relation matrix:

\[
\boxed{G_{p(i)p(j)}=G_{ij}.}
\]

Therefore a concrete vertex name is not fundamental data of the regular tetrahedral relation class.

The quotient by this relabelling symmetry permits pole/vertex roles to be exchanged without changing the underlying tetrahedral relational invariant.

This is finite tetrahedral symmetry, not a particle-physics supersymmetry assertion.

## 3. Dynamic Stella without primitive time

"Dynamic" means that the configuration admits nontrivial transformations and composable alternation. It does not mean that a body is already moving as a function of \(t\).

Let the two Stella sectors be labelled \(+\) and \(-\). Introduce the primitive alternating relation \(H:+\leftrightarrow-\), but retain occurrence history so that two switches are not collapsed to the identity.

The occurrence carrier is

\[
\mathcal X=\mathbb N_0\times\{+,-\}
\]

with

\[
H(n,+)=(n,-),
\qquad
H(n,-)=(n+1,+).
\]

Define

\[
S(n,\epsilon)=(n+1,\epsilon).
\]

Then

\[
\boxed{H^2=S.}
\]

Thus a complete successor is composed of two complementary Stella-sector alternations.

## 4. Structural half

Define

\[
\nu(n,+)=n,
\qquad
\nu(n,-)=n+\frac12.
\]

Then

\[
\boxed{\nu(HX)-\nu(X)=\frac12}
\]

and

\[
\boxed{\nu(SX)-\nu(X)=1.}
\]

The half appears before any metric clock: it is the coordinate of the intermediate dual-sector occurrence required to factor one complete successor.

This links, but does not identify, three separately typed halves already present in the stack:

1. binary exchange seam \(u=1/2\);
2. spinorial half-turn class \([1/2]\);
3. pretime successor half-index \(\Delta\nu=1/2\).

Their equality as numbers is exact; semantic identification requires explicit maps.

## 5. Relational incidence chain

Let

\[
V_n=n,
\qquad
E_n=(n,n+1).
\]

Then

\[
\boxed{E_n\cap E_{n+1}=\{n+1\}.}
\]

Hence the shorthand

\[
\boxed{1|12|23|34|45|\cdots}
\]

denotes a glued one-dimensional relational complex in which each new relation preserves one endpoint of the previous relation.

No background space is needed. Incidence is prior to geometry.

The later spatial branch may turn appropriate incidence data into geometry; the later temporal branch may turn compositional occurrence order plus positive activity into time.

## 6. Hilbert shift

The full successor acts on the countable occurrence skeleton by

\[
n\mapsto n+1.
\]

On a Hilbert basis this is the unilateral shift

\[
\boxed{\mathcal U e_n=e_{n+1}.}
\]

It is an injective isometry with proper range. This is the exact Hilbert-hotel mechanism: the entire countable occupancy can be shifted while preserving local adjacency.

It is not an automorphism on \(\mathbb N_0\), because \(e_0\) has no preimage. A bilateral \(\mathbb Z\) extension makes the shift invertible.

## 7. Emergence ordering

The construction gives the dependency chain

\[
\boxed{
\text{RELATION}
\to
\text{DUAL TETRAHEDRAL CLASS}
\to
\text{ALTERNATION }H
\to
\text{SUCCESSOR }S=H^2
\to
\text{COMPOSITION ORDER}.
}
\]

On the temporal lane,

\[
\boxed{
\text{COMPOSITION ORDER}
+
\text{POSITIVE ACTIVITY}
\to
\text{IDT TEMPORAL PRECEDENCE}.
}
\]

Separately,

\[
\boxed{
\text{RELATION}
\to
\text{INCIDENCE}
\to
\text{GEOMETRIC CARRIER}
\to
\text{TIR SPATIAL GEOMETRY}.
}
\]

Therefore neither physical time nor physical space is used to derive the pre-spacetime carrier.

## 8. Inference by alternating relative transformation

The Stella pair need not encode inference in a privileged lobe or fixed vertex.

After quotienting vertex labels, the invariant carrier can instead be the alternating relative transformation plus its composition history:

\[
\boxed{
[\Sigma_\star],\quad
\epsilon\in\mathbb Z_2,\quad
H^k.
}
\]

This makes relational history, rather than a fixed geometric label, the primitive inferential datum.

## 9. IDT handoff

The exact IDT consumer is formalism/00H_tetrahedral_half_successor_pretime.md in AdrianLipa90/Informational-Dynamics-of-Time.

TIR exports

\[
(\Sigma_\star,S_4\text{-label quotient},H,S=H^2,\text{incidence chain}).
\]

IDT then owns the transition from this pretime skeleton to positive activity weights, temporal precedence, clock comparison and eventual calibration.

## 10. Claim classes

| Statement | Status |
|---|---|
| regular tetrahedral Gram is \(S_4\)-relabel invariant | EXACT |
| Stella has two dual tetrahedral sectors under admitted antipodal closure | UPSTREAM EXACT CONDITIONAL |
| occurrence-preserving alternation satisfies \(H^2=S\) | EXACT |
| half-index increment is \(1/2\) per alternation | EXACT |
| adjacent relational edges share exactly one endpoint | EXACT |
| Hilbert unilateral shift preserves adjacency | EXACT |
| Hilbert unilateral shift is surjective | FALSE |
| physical time exists prior to the construction | NOT ASSUMED |
| physical space exists prior to the construction | NOT ASSUMED |
| pretime half-index equals calibrated physical half-duration | OPEN / REQUIRES CALIBRATION |

## 11. Proof firewall

This theorem is a mathematical pre-spacetime factorization. It does not by itself identify the abstract sphere with physical space, the alternation count with seconds, or tetrahedral finite symmetry with particle-physics supersymmetry.

Validator: TIR/validation/tir_prespacetime_stella_half_successor_v0_1.py.
Receipt: TIR/validation/TIR_PRESPACETIME_STELLA_HALF_SUCCESSOR_V0_1.json.
