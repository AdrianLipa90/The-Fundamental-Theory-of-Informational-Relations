# TIR Pre-Spacetime Stella Alternation–Successor Bridge v0.1

Status: EXACT_TWO_SECTOR_SUCCESSOR_ALGEBRA / STELLA_BINDING_CONDITIONAL / PRESPACETIME_ONLY

Date: 2026-09-28

## 1. Scope and firewall

This note is upstream of physical time and physical space.

No variable in the exact core below is assumed to be a physical clock coordinate, proper time, spatial coordinate, metric distance, velocity, or dynamical duration. The primitive data are relations, sector labels, incidence, composition, and an abstract transformation.

The intended dependency direction is

\[
\boxed{
\text{relation}
\to
\text{symmetry}
\to
\text{alternation}
\to
\text{order}
\to
\text{IDT temporal structure},
}
\]

in parallel with

\[
\boxed{
\text{relation}
\to
\text{incidence}
\to
\text{geometry}
\to
\text{TIR spatial structure}.
}
\]

Thus time and space are downstream interpretations/constructions, not background variables of this theorem.

## 2. Upstream Stella packet

The existing TIR Stella carrier is

\[
\mathcal S_\star=T_4^+\cup T_4^-,
\]

where the two tetrahedral frames are related by the admitted antipodal/Bloch-orthocomplement closure.

Existing exact results used only as compatibility data are:

\[
\Sigma_{\rm stella}=T\cup(-T),
\]

and, inside the regular-simplex holonomy family,

\[
q_3=\frac12
\]

uniquely for the tetrahedral dimension.

The present construction does not identify that geometric half-turn with physical elapsed time. It uses the two-sector Stella structure as a candidate realization of an abstract two-sector alternation.

Vertex names are not primitive observables here. Any admitted relabelling that preserves the tetrahedral relational structure leaves the sector-level construction unchanged.

## 3. Abstract doubled carrier

Define the pre-spacetime carrier

\[
\boxed{
\mathcal X=\mathbb N_0\times\mathbb Z_2.
}
\]

Write a state as

\[
x=(n,\sigma),
\qquad
n\in\mathbb N_0,
\quad
\sigma\in\{0,1\}.
\]

The integer \(n\) is a coarse successor label. It is not a time coordinate.

The binary label \(\sigma\) records which member of a complementary two-sector pair is active.

For the Stella binding candidate,

\[
\sigma=0\leftrightarrow T_4^+,
\qquad
\sigma=1\leftrightarrow T_4^-.
\]

Only this sector identification is used; no rigid vertex naming is required.

## 4. Elementary alternation and full successor

Define the elementary alternation operator

\[
\boxed{
\mathsf H(n,0)=(n,1),
\qquad
\mathsf H(n,1)=(n+1,0).
}
\]

Define the coarse successor

\[
\boxed{
\mathsf S(n,\sigma)=(n+1,\sigma).
}
\]

Then, for either value of \(\sigma\),

\[
\boxed{
\mathsf H^2(n,\sigma)=\mathsf S(n,\sigma).
}
\]

Therefore

\[
\boxed{\mathsf H^2=\mathsf S.}
\]

This is the exact algebraic meaning of "half-step" in this construction: one application of \(\mathsf H\) is a square root of the full successor on the doubled carrier.

It does not presuppose a temporal metric.

## 5. Normalized half grading

After choosing one application of \(\mathsf S\) as one coarse unit, define the grading

\[
\boxed{
g(n,\sigma)=n+\frac{\sigma}{2}.
}
\]

Then

\[
\boxed{
g(\mathsf Hx)-g(x)=\frac12,
}
\]

and

\[
\boxed{
g(\mathsf Sx)-g(x)=1.
}
\]

Thus the numerical sequence

\[
\frac12,1,\frac32,2,\ldots
\]

is not inserted as a pre-existing physical time axis. It is the normalized grading of successive applications of the abstract alternation operator.

Starting from \(x_0=(0,0)\),

\[
x_0
\xrightarrow{\mathsf H}
(0,1)
\xrightarrow{\mathsf H}
(1,0)
\xrightarrow{\mathsf H}
(1,1)
\xrightarrow{\mathsf H}
(2,0)
\to\cdots,
\]

which gives the alternating sector pattern

\[
-,+,-,+,\ldots
\]

at grades

\[
\frac12,1,\frac32,2,\ldots
\]

after the declared choice of initial sector.

## 6. Relational gluing chain

Let coarse vertices be

\[
V_n=\{n\},
\qquad n\ge1,
\]

and elementary relations be the two-point incidence sets

\[
\boxed{
E_n=\{n,n+1\}.
}
\]

Adjacent relations satisfy

\[
\boxed{
E_n\cap E_{n+1}=\{n+1\}.
}
\]

Hence the compressed incidence notation

\[
\boxed{
1\,|\,12\,|\,23\,|\,34\,|\,45\,|\,\cdots
}
\]

means that every next relation preserves exactly one boundary element of its predecessor while adjoining one new endpoint.

No continuum is assumed. The continuity-like property at this level is relational overlap/gluing.

## 7. Hilbert shift

On the countably infinite coarse carrier define

\[
\boxed{
\mathsf S_{\mathbb N}(n)=n+1.
}
\]

This is the standard unilateral/Hilbert-hotel shift: it is injective but not surjective on \(\mathbb N\).

It acts on relations by

\[
\boxed{
\mathsf S_{\mathbb N}(E_n)=E_{n+1}.
}
\]

The incidence rule is preserved:

\[
E_n\cap E_{n+1}=\{n+1\}
\Longrightarrow
E_{n+1}\cap E_{n+2}=\{n+2\}.
\]

The coarse projection of the doubled carrier therefore carries the same successor structure, while \(\mathsf H\) supplies an exact two-sector square root:

\[
\boxed{
\mathsf H^2=\mathsf S.
}
\]

This is the precise Hilbert-hotel connection. No claim that the unilateral shift is an automorphism is made.

## 8. Separation from the existing spinorial half-turn

TIR already uses spinorial half-turn operators

\[
H_i^\pm=\mp i\Sigma_i,
\qquad
(H_i^\pm)^2=-I.
\]

Those operators and the new successor square root \(\mathsf H\) are different typed objects.

The exact statements are:

\[
q_3=\frac12
\]

for tetrahedral triangular holonomy, and independently

\[
\mathsf H^2=\mathsf S
\]

for the doubled successor carrier.

The Stella binding says these structures are compatible with the same two-sector geometry. It does not identify \(-I\) with the unilateral successor and does not use one equation to prove the other.

## 9. Pre-spacetime interpretation

The exact core supports two downstream routes.

Order route:

\[
\boxed{
\text{two-sector relation}
\to
\mathsf H
\to
\mathsf S
\to
\text{serial order}
\to
\text{IDT}.
}
\]

Incidence route:

\[
\boxed{
\text{relations }E_n
\to
\text{overlap/incidence}
\to
\text{geometric realization}
\to
\text{TIR spatial sector}.
}
\]

The theorem therefore sits before a spacetime split. It supplies a common relational skeleton from which temporal order and spatial incidence may be developed separately.

## 10. Claim classes

| Statement | Status |
|---|---|
| doubled carrier \(\mathbb N_0\times\mathbb Z_2\) | EXACT DEFINITION |
| elementary alternation \(\mathsf H\) | EXACT DEFINITION |
| full successor \(\mathsf S\) | EXACT DEFINITION |
| \(\mathsf H^2=\mathsf S\) | EXACT |
| normalized grading increments \(1/2\) and \(1\) | EXACT AFTER UNIT NORMALIZATION |
| \(E_n\cap E_{n+1}=\{n+1\}\) | EXACT |
| unilateral Hilbert shift preserves the incidence law | EXACT |
| unilateral shift is injective and non-surjective on \(\mathbb N\) | EXACT |
| Stella \(T_4^+/T_4^-\) realizes the abstract binary sectors | CONDITIONAL STRUCTURAL BINDING |
| tetrahedral \(q_3=1/2\) is compatible with the half-step normalization | EXACT CROSSWALK / NO IDENTITY CLAIM |
| physical time has already been assumed | FALSE / EXCLUDED BY CONSTRUCTION |
| physical space has already been assumed | FALSE / EXCLUDED BY CONSTRUCTION |
| unique physical spacetime follows from this theorem alone | NOT CLAIMED |

## 11. Handoff to IDT

The sibling IDT theorem is

Informational-Dynamics-of-Time/formalism/00A_pretemporal_stella_halfstep_successor.md

and receives only:

- the abstract two-sector carrier;
- the exact relation \(\mathsf H^2=\mathsf S\);
- the incidence chain;
- the normalized half grading;
- the explicit statement that no clock or physical spacetime exists at this layer.

IDT remains responsible for deriving temporal precedence, duration measures, clock comparison, and calibrated time downstream.

Validator:

TIR/validation/tir_stella_prespacetime_halfstep_successor_v0_1.py
