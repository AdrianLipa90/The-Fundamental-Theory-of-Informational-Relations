# TIR Zero-Axiom Relational Foundation v0.1

Status: `OWNER_CANONICAL_ZERO_AXIOM_FOUNDATION__DERIVATION_AUDIT_OPEN`

Scope: canonical TIR root typing. This document replaces the former use of eight non-logical foundational axioms with a zero-nonlogical-axiom programme. It does not erase historical axiom documents; it reclassifies them as legacy provenance and downstream theorem/sector targets.

## 0. Foundation count

TIR now declares

\[
\boxed{N_{\rm nonlogical\ axioms}=0.}
\]

Ordinary logic, definitions, typing rules and standard mathematical theorems used later are background formal machinery and are not counted as physical or ontological TIR axioms.

The audit rule is strict:

\[
\boxed{\text{anything not derived must remain an explicit open theorem, sector binding, or conditional rule.}}
\]

## 1. Ontic nothing is not an object

Let \(\mathcal O\) denote the TIR ontic domain: the class of admissible referents in a representation.

`Nothing` is not introduced as an element of \(\mathcal O\). If it were an element, it would already be a referent and therefore not literal absence.

The TIR typing is

\[
\boxed{\mathsf{Nothing}\notin\mathcal O.}
\]

This is not the statement that the arithmetic number \(0\) is forbidden. It is the statement that **ontic nothing is not an object**.

Accordingly,

\[
\boxed{0\neq\mathsf{Nothing}.}
\]

A written symbol, equation, state vector, empty-set symbol or coordinate value is already a representation and therefore cannot itself be literal ontic nothing.

## 2. Zero exists only as relational nullity

Within an admitted representation, the symbol \(0\) may occur as the null value of a relation, difference, residual, charge, winding defect, coordinate or other typed map.

For a relational comparison \(\Delta_R\),

\[
\Delta_R(a,a)=0
\]

is a statement about a relation. It is not the existence of an ontic zero-object.

Hence the canonical TIR typing is

\[
\boxed{0\equiv\text{relational nullity, never ontic nothing}.}
\]

The zero symbol is therefore downstream of an admitted relation or map:

\[
\boxed{R\prec_{\rm dep}0_R.}
\]

## 3. Minimum admitted content: relation

Because literal nothing is not an ontic object and zero is only a relational value, the first non-empty TIR content is not a point-substance. It is a relation.

Write the minimal relational carrier as

\[
\boxed{\mathcal R_1=(a\xleftrightarrow{R}b).}
\]

The endpoints are typed first by their roles in \(R\); they are not required to be independent primitive substances upstream of the relation.

Thus the canonical root statement is

\[
\boxed{\min(\text{TIR admitted content})=\text{RELATION}.}
\]

This supersedes the former A1 wording `the least that can exist is a point`.

## 4. Relation gives the pole pair

A nontrivial relation has two orientation roles. Define orientation reversal

\[
J:(a,b;R)\mapsto(b,a;R^{-1}),
\qquad
J^2=\mathrm{id}.
\]

For a non-self-collapsed distinction, the two orientation classes are distinct. Rename them

\[
\boxed{N=[a\to b],\qquad S=[b\to a].}
\]

The primitive exchange orbit is therefore

\[
\boxed{\mathcal O_J=\{N,S\}.}
\]

The two poles are not inserted as independent axioms; they are the two orientation roles of the minimal relation.

## 5. Exchange balance gives the half-seam

Attach normalized nonnegative relational shares

\[
w_N,w_S\ge0,
\qquad
w_N+w_S=1.
\]

At the exchange-invariant relation,

\[
(w_N,w_S)=(w_S,w_N),
\]

so

\[
\boxed{w_N=w_S=\frac12.}
\]

The unique fixed coordinate of pole exchange is therefore

\[
\boxed{\operatorname{Fix}(u\mapsto1-u)=\left\{\frac12\right\}.}
\]

The corresponding binary Shannon information is

\[
\boxed{H_2(1/2)=\ln2.}
\]

This is the first exact scalar branch downstream of the relation.

## 6. From pole pair to the sphere

The relation first supplies an axis with two poles. In an admitted three-real-dimensional direction carrier, choose a unit representative \(\hat n\) and write

\[
N\mapsto+\hat n,
\qquad
S\mapsto-\hat n.
\]

The full orientation orbit of a unit direction is

\[
\operatorname{Orb}_{SO(3)}(\hat n)
\cong
SO(3)/SO(2)
\cong
S^2.
\]

Equivalently, after the standard minimal coherent two-state lift,

\[
\mathcal H_{NS}\cong\mathbb C^2,
\]

pure rays satisfy

\[
\boxed{\mathbb{CP}^1\cong S^2.}
\]

Thus the primitive relation supplies the pole pair; the already-developed TIR coherent/projective geometry closes that pole pair into the Bloch sphere.

The origin \(\mathbf 0\in\mathbb R^3\) in this representation is a coordinate origin, not ontic nothing.

## 7. Canonical dependency spine

The new root dependency is

```text
NO ONTIC ZERO OBJECT
  -> RELATION
      -> ORIENTATION REVERSAL
          -> POLE PAIR {N,S}
              -> EXCHANGE BALANCE 1/2
                  -> ln2
              -> MINIMAL COHERENT TWO-STATE LIFT C^2
                  -> CP1 ~= S2
                      -> TIR geometry / phase / information branches
```

In formula form,

\[
\boxed{
\mathsf{Nothing}\notin\mathcal O
\;\Longrightarrow_{\rm TIR}\;
\mathcal R_1
\;\Longrightarrow\;
\{N,S\}
\;\Longrightarrow\;
\frac12
\;\Longrightarrow\;
\ln2
}
\]

with the geometric continuation

\[
\boxed{
\{N,S\}
\longrightarrow
\mathbb C^2
\longrightarrow
\mathbb{CP}^1\cong S^2
\longrightarrow
\mathrm{TIR}.
}
\]

The arrow labelled \(\Longrightarrow_{\rm TIR}\) is the canonical metalogical foundation statement of this programme and remains subject to independent formal audit; it is not represented as a theorem of ordinary set theory merely because it is canonical inside TIR.

## 8. Reclassification of former A1--A8

The historical file `TIR_AXIOMATIC_KERNEL_V0_1.md` remains provenance. Its labels A1--A8 are no longer counted as canonical non-logical axioms.

| Former label | New status |
|---|---|
| A1 point minimality | SUPERSEDED by relational minimality |
| A2 quantum point | DOWNSTREAM QUANTUM-LIFT / PHYSICAL-BINDING THEOREM TARGET |
| A3 information primacy | RELATIONAL INFORMATION THEOREM / DEFINITIONAL LAYER |
| A4 spherical efficiency | DOWNSTREAM GEOMETRIC THEOREM / SELECTION CRITERION |
| A5 arithmetic measures geometry | DOWNSTREAM INVARIANT-MAP THEOREM FAMILY |
| A6 naturals from complex phase closure | DOWNSTREAM PHASE-CLOSURE THEOREM FAMILY |
| A7 universal symmetry | DOWNSTREAM SYMMETRY/CLOSURE LAW TO DERIVE OR TYPE CONDITIONALLY |
| A8 paradox stabilization | META-STRUCTURAL CLOSURE RULE / THEOREM TARGET |

No item in this table may be silently promoted from target to theorem. Each downstream branch keeps its own proof and empirical gates.

## 9. Claim classes and firewall

| Statement | Current class |
|---|---|
| `N_nonlogical_axioms = 0` | CANONICAL TIR FOUNDATION DECLARATION |
| ontic nothing is not represented as an object | TIR METALOGICAL TYPING |
| `0 != ontic nothing` | TIR TYPING / DEFINITIONAL DISTINCTION |
| zero appears as relational nullity | TIR RELATIONAL TYPING |
| orientation reversal has a two-element orbit for a nontrivial dyad | EXACT |
| exchange-invariant normalized share is `(1/2,1/2)` | EXACT |
| `H_2(1/2)=ln2` | EXACT INFORMATION-THEORETIC |
| `CP1 ~= S2` | STANDARD GEOMETRIC IDENTIFICATION |
| relation alone proves all later physical TIR laws | NOT CLAIMED; DOWNSTREAM DERIVATION REQUIRED |
| TIR is empirically universal | NOT ESTABLISHED BY THIS FOUNDATION ALONE |

The foundation therefore changes the **axiom count** without erasing the proof burden.

## 10. Canonical invariant

The TIR root is now summarized by

\[
\boxed{
N_{\rm nonlogical\ axioms}=0,
\qquad
0_{\rm ontic}\ \text{is not an object},
\qquad
\min\mathcal O_{\rm TIR}=R,
\qquad
R\mapsto\{N,S\},
\qquad
\{N,S\}\leadsto S^2,
\qquad
S^2\leadsto\mathrm{TIR}.
}
\]

The associated deterministic implementation certificate is

`TIR/validation/tir_zero_axiom_relational_foundation_v0_1.py`.
