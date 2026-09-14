# TIR Coefficient Selector — Cocycle / Potential Reduction v0.4

Status: `EXACT_C3_COEFFICIENT_COBBOUNDARY / EXACT_IDT_PHASE_COBBOUNDARY / SCALAR_LINEAR_PHASE_MAP_NO_GO / SU3_ENDPOINT_ABELIANIZATION_NO_GO / PARENT_VALUATION_INJECTIVE_ON_CURRENT_ALPHABET / SELECTOR_REMAINS_OPEN`

Date: 2026-09-14

Scope: internal algebraic reduction of the remaining transition-parent selector problem on the active Stage-22 / Stage-24 three-seed carrier. No measured mass, Yukawa coupling, recovered target tuple, residual-to-target quantity, CKM/PMNS value, or physical-time binding is used.

## 1. Active Stage-24 label cycle

Stage 22 fixes

\[
s_1=(3,5),\qquad s_2=(5,7),\qquad s_3=(11,13),
\]

and Stage 24 defines the exact label cycle

\[
\boxed{s_1\to s_2\to s_3\to s_1.}
\]

The same Stage-24 source explicitly keeps dynamical Collatz realization separate; the present theorem uses only the exact finite label cycle.

Let

\[
R_{12}:=R_{e\mu}=(0,5,2,8),
\]

\[
R_{23}:=R_{\mu\tau}=(0,3,-1,-7),
\]

be the two already-declared signed adjacent release vectors in the TIR coefficient lattice

\[
\Lambda=\mathbb Z^4.
\]

The existing generator addition law gives

\[
R_{13}=R_{12}+R_{23}=(0,8,1,1).
\]

To close the directed Stage-24 cycle, the third edge is forced algebraically:

\[
\boxed{
R_{31}:=-R_{13}=(0,-8,-1,-1).
}
\]

Therefore

\[
\boxed{R_{12}+R_{23}+R_{31}=0.}
\]

No new physical transition is claimed for `R_31`; it is the unique lattice edge required by additive closure of the abstract Stage-24 label cycle.

## 2. Exact vertex-potential representation

Choose the gauge

\[
K(s_1)=0.
\]

Define

\[
\boxed{K(s_2)=R_{12}=(0,5,2,8),}
\]

\[
\boxed{K(s_3)=R_{13}=(0,8,1,1).}
\]

Then all three cycle edges are exact differences:

\[
R_{12}=K(s_2)-K(s_1),
\]

\[
R_{23}=K(s_3)-K(s_2),
\]

\[
R_{31}=K(s_1)-K(s_3).
\]

Thus the current closed coefficient edge assignment is an exact `Z^4`-valued coboundary on the Stage-24 `C_3` label graph.

### Uniqueness up to a global constant

If another potential `K'` has the same edge differences on the connected three-node graph, then

\[
K'(s_j)-K(s_j)
\]

is equal at every vertex. Hence

\[
\boxed{K'=K+C,\qquad C\in\mathbb Z^4.}
\]

The potential is therefore unique modulo one global additive lattice gauge.

### Selector consequence

This does **not** derive `K` from seed geometry: the displayed potential is reconstructed from the already-declared release lattice.

It does, however, reduce the architecture of any additive selector. Instead of independently selecting a packet for every ordered transition, it is sufficient to derive a coefficient-free vertex potential

\[
\boxed{
\widehat K:\{s_1,s_2,s_3\}\longrightarrow\mathbb Z^4
}
\]

such that transition vectors are its differences.

The missing theorem is now narrower:

\[
\text{coefficient-free seed geometry}
\longrightarrow \widehat K(s)
\longrightarrow \widehat K(s_j)-\widehat K(s_i).
\]

## 3. Current parent alphabet is injectively valued

The current finite magnitude-parent alphabet is

\[
\mathcal P=\{0,I,F,X_4,X_5,X_3,X_3+I\}.
\]

The canonical counts are

\[
I=1,\qquad N_F=3,\qquad (L_3,L_4,L_5)=(7,2,5),
\]

so the existing valuation gives

\[
\nu(0)=0,
\quad \nu(I)=1,
\quad \nu(X_4)=2,
\quad \nu(F)=3,
\quad \nu(X_5)=5,
\quad \nu(X_3)=7,
\quad \nu(X_3+I)=8.
\]

These seven integers are pairwise distinct. Therefore

\[
\boxed{
\nu|_{\mathcal P}\text{ is injective}.
}
\]

Consequently, within the current declared parent alphabet, once a coefficient-free theorem supplies a magnitude vector whose entries lie in

\[
\{0,1,2,3,5,7,8\},
\]

the corresponding magnitude-parent label in each slot is unique.

This does not remove the need to derive the coefficient vector. It shows that no second combinatorial ambiguity remains at the present parent-valuation layer after the vector is known.

## 4. IDT phase is a second exact coboundary

The canonical IDT Collatz phases on the active seed centers are

\[
q_1:=q_C(4)=\frac17,
\qquad
q_2:=q_C(6)=\frac{141}{448},
\qquad
q_3:=q_C(12)=\frac{141}{896}.
\]

Define directed lifted phase differences on the Stage-24 cycle:

\[
\Delta q_{12}=q_2-q_1=\frac{11}{64},
\]

\[
\Delta q_{23}=q_3-q_2=-\frac{141}{896},
\]

\[
\Delta q_{31}=q_1-q_3=-\frac{13}{896}.
\]

They close exactly:

\[
\boxed{
\Delta q_{12}+\Delta q_{23}+\Delta q_{31}=0.
}
\]

Thus the lifted phase edge assignment is the exact scalar coboundary `dq` of the vertex potential `q=(q_1,q_2,q_3)`.

The signs are

\[
(+,-,-).
\]

For the three coefficient-cycle edges, the signed `b` and `c` slots are

\[
R_{12}:\quad (b,c)=(2,8),
\]

\[
R_{23}:\quad (b,c)=(-1,-7),
\]

\[
R_{31}:\quad (b,c)=(-1,-1),
\]

so their sign pattern is also

\[
(+,-,-).
\]

Hence

\[
\boxed{
\operatorname{sgn}(\Delta q_{ij})
=
\operatorname{sgn}(b_{ij})
=
\operatorname{sgn}(c_{ij})
}
\]

for all three directed Stage-24 cycle edges in the present closed lattice extension.

This is an exact structural correlation. No current theorem identifies the IDT lifted phase difference with the TIR return-axis or curvature orientation source, so the binding remains `OPEN`.

The `a` slot is intentionally excluded from this statement: on `R_23`, `a=+3` while `Delta q_23<0`.

## 5. Scalar-linear phase map cannot generate the coefficient lattice

Suppose the entire coefficient edge vector were generated from the scalar IDT phase difference by one fixed vector

\[
v\in\mathbb R^4
\]

through

\[
R_{ij}=v\,\Delta q_{ij}.
\]

Then every nonzero pair of release vectors would be collinear.

But the `(a,b)` projections of the two adjacent vectors are

\[
(5,2),\qquad(3,-1),
\]

with determinant

\[
\boxed{5(-1)-3(2)=-11\ne0.}
\]

Therefore `R_12` and `R_23` are not collinear, and no fixed scalar-to-vector multiplier can generate both.

Equivalently, no affine vertex law

\[
K(s)=K_0+v\,q_C(s)
\]

can reproduce the current coefficient potential.

Thus

\[
\boxed{
q_C\text{ alone cannot linearly encode the full }\mathbb Z^4\text{ coefficient state}.
}
\]

Its surviving role in the present evidence is narrower: an additive scalar phase coordinate with an exact sign correlation to the `b,c` cycle orientations.

## 6. Endpoint SU(3) holonomy cannot abelianize to a nonzero Z^4 selector

Consider any future holonomic construction that assigns to a composable path `gamma`

\[
W(\gamma)\in SU(3)
\]

with the usual transport composition law

\[
W(\gamma_2\circ\gamma_1)=W(\gamma_2)W(\gamma_1).
\]

Suppose a coefficient selector depended **only** on the endpoint holonomy through a composition-preserving map

\[
\Phi:SU(3)\to\mathbb Z^4
\]

satisfying

\[
\Phi(UV)=\Phi(U)+\Phi(V).
\]

Then `Phi` is a group homomorphism from `SU(3)` to an abelian group.

Standard Lie-group structure gives

\[
[SU(3),SU(3)]=SU(3),
\]

i.e. `SU(3)` is perfect and its abelianization is trivial. Every homomorphism from a perfect group to an abelian group annihilates the full commutator subgroup, hence

\[
\boxed{\Phi\equiv0.}
\]

But the TIR release lattice has nonzero edges, for example

\[
R_{12}=(0,5,2,8)\ne0.
\]

Therefore

\[
\boxed{
\text{no nontrivial additive }\mathbb Z^4\text{ selector can depend only on endpoint }SU(3)\text{ holonomy via a group homomorphism}.
}
\]

This is a mathematical no-go, not a rejection of holonomy. A valid holonomic selector must retain additional data before endpoint group reduction, for example a path-local cochain, seed labels, a separately quantized curvature/path integral, or another structure that is not merely the abelianization of `W(gamma)`.

The archived `W_ij` / local-connection modules are evidence that such path-local holonomic objects exist as structural candidates, but their own canon status is not promoted by this theorem.

## 7. Exact architecture after v0.4

The surviving architecture is

\[
\boxed{
\text{coefficient-free seed/path state}
\longrightarrow
\widehat K(s)\in\mathbb Z^4
\longrightarrow
R_{ij}=\widehat K(s_j)-\widehat K(s_i)
\longrightarrow
\text{unique current parent labels via }\nu^{-1}.
}
\]

Any holonomic assistance must enter upstream of the integer potential, not as a nonzero homomorphic abelianization of endpoint `SU(3)` holonomy.

The IDT phase potential may constrain orientation of the return/curvature slots, but its binding to those roles is not derived here.

## 8. Claim ledger

```text
stage24_seed_cycle = IMPORTED_EXACT_LABEL_STRUCTURE
R12_R23 = IMPORTED_HISTORICAL_SIGNED_RELEASE_LATTICE
R31_required_by_cycle_closure = EXACT
coefficient_cycle_sum = ZERO_EXACT
coefficient_edge_assignment_is_Z4_coboundary = EXACT
coefficient_vertex_potential_unique_mod_global_Z4_constant = EXACT
current_parent_valuation_is_injective = EXACT
IDT_lifted_phase_cycle_sum = ZERO_EXACT
IDT_phase_edge_assignment_is_scalar_coboundary = EXACT
q_phase_sign_matches_b_c_on_all_three_closed_cycle_edges = EXACT_STRUCTURAL_CORRELATION
q_phase_to_b_c_orientation_binding = OPEN
fixed_linear_q_to_Z4_coefficient_map = IMPOSSIBLE
endpoint_SU3_homomorphism_to_nonzero_Z4_selector = IMPOSSIBLE_BY_STANDARD_PERFECT_GROUP_THEOREM
coefficient_free_vertex_potential_K_derivation = OPEN
COEFFICIENT_TRANSITION_PARENT_SELECTOR = OPEN
physical_mass_or_Yukawa_binding = OPEN_DOWNSTREAM
```

## 9. Reproducibility

Deterministic validator:

`TIR/validation/tir_coefficient_cocycle_potential_reduction_v0_4.py`

The validator source-audits the existing coefficient generator and Stage-24 cycle, independently recomputes the IDT rational phases, verifies the closed `Z^4` edge sum and vertex-potential differences, verifies injectivity of the current parent valuation, verifies the scalar-linear-map determinant no-go, and records the `SU(3)` endpoint abelianization theorem as a standard-theorem dependency rather than pretending to numerically prove a Lie-group theorem.