# TIR SP3 Causal Pair Instantiation v0.1

Status: CANDIDATE_ONLY / FINITE_EXTERNAL_SOURCE_COMPATIBILITY_WITNESS / EXACT_THEOREM_INSTANTIATION_ON_FROZEN_PAIRS / PHYSICAL_EVENT_IDENTITY_NOT_CLAIMED / CANON_ALLOWED_FALSE

Date: 2026-09-19

## 1. Purpose

This note connects two already validated objects without collapsing their evidence classes:

1. the exact conditional theorem
   TIR Causal 3+1 Pair Closure v0.1;
2. the frozen two-epoch SP3 Herm(2) half-lift witness.

The target claim is not

\[
\text{physical spacetime}=\operatorname{Herm}(2).
\]

The target claim is narrower:

\[
\boxed{
\text{the five frozen observed event differences admit a lossless Herm(2) representation that instantiates the exact causal-pair theorem.}
}
\]

## 2. Source pair differences

For each satellite \(s\), the frozen source supplies two observed spatial positions

\[
\mathbf x_s^{(1)},\qquad \mathbf x_s^{(2)}
\]

at epochs separated by

\[
\Delta t=120\ {\rm s}.
\]

Define

\[
\Delta\mathbf x_s
=
\mathbf x_s^{(2)}-\mathbf x_s^{(1)}
\]

and the source-owned temporal separation

\[
\Delta x^0
=
c\Delta t.
\]

The raw SP3 clock-correction column is not used as this event separation; that direct identification has already been refuted by the existing no-go test.

## 3. Full difference and half-difference lifts

Define the full Hermitian pair difference

\[
\boxed{
D_s
=
c\Delta t\,I
+
\Delta\mathbf x_s\cdot\boldsymbol\sigma
}
\]

and the centered half-difference

\[
\boxed{
H_s
=
\frac{D_s}{2}.
}
\]

This is exactly the theorem-level centered relation variable

\[
H=\frac{B-A}{2}.
\]

The existing SP3 bridge already verifies

\[
\operatorname{Tr}H_s=c\Delta t
\]

and

\[
\operatorname{Tr}(H_s\sigma_i)=\Delta x_s^i.
\]

Therefore the observed 3+1 difference is recovered without loss.

## 4. Exact Minkowski determinant on the source pairs

By the causal 3+1 theorem,

\[
\det D_s
=
(c\Delta t)^2
-
|\Delta\mathbf x_s|^2.
\]

Since

\[
H_s=\frac{D_s}{2},
\]

\[
\boxed{
\det H_s
=
\frac14
\left[
(c\Delta t)^2
-
|\Delta\mathbf x_s|^2
\right].
}
\]

Writing

\[
\mathbf r_s
=
\frac{\Delta\mathbf x_s}{c\Delta t}
=
\frac{\boldsymbol\beta_s}{c},
\]

one also has

\[
\boxed{
\frac{4\det H_s}{(c\Delta t)^2}
=
1-|\mathbf r_s|^2.
}
\]

Thus the external-source causal margin is measured by the same determinant invariant as the exact theorem.

## 5. Positive-cone instantiation

The theorem defines the future cone by

\[
\mathcal C_+
=
\operatorname{PSD}(2).
\]

The existing SP3 witness establishes, for all five frozen source pairs,

\[
H_s>0.
\]

Positive scaling therefore gives

\[
D_s=2H_s>0.
\]

Hence every frozen pair instantiates a strict future relation in the theorem-level cone:

\[
\boxed{
D_s\in\operatorname{int}\mathcal C_+.
}
\]

Equivalently,

\[
c\Delta t>|\Delta\mathbf x_s|.
\]

## 6. Centered endpoint realization

For theorem compatibility one may work in the local affine chart centered at the pair midpoint and define

\[
A_s=-H_s,
\qquad
B_s=+H_s.
\]

Then

\[
\boxed{
B_s-A_s=D_s
}
\]

and

\[
\boxed{
\frac{A_s+B_s}{2}=0,
\qquad
\frac{B_s-A_s}{2}=H_s.
}
\]

Therefore

\[
\boxed{
A_s\prec B_s
}
\]

under the theorem-level PSD cone order.

This centered representation does not assert an absolute physical Hermitian coordinate for either endpoint. It represents the observed source difference only.

## 7. Relation to the observed spatial midpoint

Independently, the observed spatial midpoint is

\[
\bar{\mathbf x}_s
=
\frac{
\mathbf x_s^{(1)}
+
\mathbf x_s^{(2)}
}{2}.
\]

The existing bridge verifies

\[
\mathbf x_s^{(1)}
=
\bar{\mathbf x}_s
-
\frac{\Delta\mathbf x_s}{2},
\]

\[
\mathbf x_s^{(2)}
=
\bar{\mathbf x}_s
+
\frac{\Delta\mathbf x_s}{2}.
\]

Thus the same factor \(1/2\) appearing in the theorem-level endpoint decomposition is the factor that exactly reconstructs the two observed spatial endpoints from their measured midpoint and displacement.

## 8. What this adds beyond the two parent results

The theorem alone proves an abstract conditional statement inside \(\operatorname{Herm}(2)\).

The SP3 bridge alone proves a finite observationally anchored Hermitian half-lift.

Together they establish:

\[
\boxed{
\text{external 3+1 difference}
\to
\text{lossless Herm(2) lift}
\to
\text{Minkowski determinant}
\to
\text{strict PSD future cone}
\to
\text{unique centered /2 pair representation}.
}
\]

No new fit parameter is introduced.

## 9. Falsification conditions

This finite compatibility witness would fail if any frozen source pair satisfied any of the following:

1. trace recovery failed;
2. Pauli-component recovery failed;
3. \(\det H_s\le0\);
4. \(H_s\) was not positive definite;
5. the determinant did not equal the Minkowski interval expression;
6. the normalized source vector differed from the existing RF-E8 shift beyond the declared boundary tolerance;
7. the source epoch separation had to be replaced by the raw SP3 clock-correction column.

The current frozen source passes 1--6 and the raw-clock alternative is explicitly rejected by 7.

## 10. Evidence boundary

Established:

- external two-epoch source: PRESENT;
- source-owned \(\Delta t\): PRESENT;
- source-owned \(\Delta\mathbf x\): PRESENT;
- lossless 3+1 to Herm(2) difference representation: EXACT ON FROZEN SOURCE;
- theorem determinant instantiated: EXACT ON FROZEN SOURCE;
- strict theorem PSD future cone: PASS ON ALL FIVE PAIRS;
- theorem factor \(1/2\) instantiated by observed midpoint reconstruction: EXACT;
- normalized vector equals existing RF-E8 shift: PASS.

Not established:

- that physical event coordinates globally are Hermitian matrices;
- that every physical event relation uses the PSD cone order;
- that this finite source validates the theorem for arbitrary physical systems;
- global spacetime identity;
- production-source promotion.

Therefore the evidence class is

\[
\boxed{
\text{FINITE EXTERNAL-SOURCE COMPATIBILITY WITNESS}.
}
\]

It is evidence for compatibility between the exact theorem and the observed source, not empirical confirmation of a universal physical theory.
