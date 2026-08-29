# XF-7 — Laguerre-hierarchy crosswalk and signed oscillatory tail

Status: research formalism with typed epistemic firewall.

## 1. Purpose

XF-6 produced an exact positive central corridor and a conditional transverse
mass envelope for

\[
M(a,b)=\Phi(a+b)\Phi(a-b),\qquad a>|b|.
\]

Its remaining large-|x| issue is that replacing the oscillatory tail by its
absolute value before integration discards the phase cancellation that becomes
more important as the certified positive corridor shrinks like \(O(|x|^{-1})\).

XF-7 adds two layers:

1. an exact coordinate crosswalk from the Planat--Solé Laguerre hierarchy to
   derivatives of the repository Xi kernel \(\Phi\);
2. a correlation-preserving integration-by-parts bound for the signed
   \(b\)-oscillatory tail.

The global RH-level sign obligation remains OPEN.

## 2. External inputs and firewall

### 2.1 Kernel positivity and radial decrease

The classical Riemann Xi kernel satisfies

\[
\Phi(r)>0,\qquad \Phi'(r)<0\quad(r>0).
\]

This property is treated as `STANDARD_EXTERNAL_THEOREM`; it is recorded in
Michel Planat, *A Theta-Kernel Reformulation of Riemann-Xi Growth and the
Obstruction to Blockwise Positivity*, Symmetry 18 (2026), 1283,
doi:10.3390/sym18081283.

Define

\[
A_0(r):=-\frac{\Phi'(r)}{\Phi(r)}.
\]

Hence \(A_0(r)>0\) for \(r>0\).

### 2.2 Planat--Solé second-level concavity

Michel Planat and Patrick Solé, *Second-Level Concavity of the Riemann Xi
Kernel*, arXiv:2608.19160 (19 August 2026), set

\[
s(t)=\Phi(\sqrt t),\qquad
F(t)=s'(t)^2-s(t)s''(t),
\]

and report

\[
(\log F)''(t)<0\qquad(t>0),
\]

with the associated double Turán inequalities.

Repository status:

`PLANAT_SOLE_SECOND_LEVEL_CONCAVITY = EXTERNAL_PREPRINT_CLAIM`.

It is not admitted automatically by `XF7_SOLVER`; it must be supplied as an
explicit premise if that route is evaluated.

## 3. Exact coordinate crosswalk

Put \(t=r^2\), \(r>0\).  The chain rule gives

\[
s'(t)=\frac{\Phi'(r)}{2r},
\]

and

\[
s''(t)=\frac{\Phi''(r)}{4r^2}-\frac{\Phi'(r)}{4r^3}.
\]

Therefore

\[
\boxed{
F(r^2)=
\frac{r\left(\Phi'(r)^2-\Phi(r)\Phi''(r)\right)
+\Phi(r)\Phi'(r)}{4r^3}
}.
\]

Define

\[
B_0(r):=rA_0'(r)-A_0(r).
\]

Using \(A_0=-\Phi'/\Phi\), the numerator above reduces exactly to
\(\Phi(r)^2B_0(r)\). Hence

\[
\boxed{
F(r^2)=\frac{\Phi(r)^2B_0(r)}{4r^3}
}.
\]

Status: `EXACT`.

Because \(\Phi>0\) and \(r>0\),

\[
F(r^2)>0\iff B_0(r)>0.
\]

Status: `EXACT_CONDITIONAL` when positivity of \(F\) is supplied.

## 4. Radial ratio monotonicity

Define

\[
q(r):=\frac{A_0(r)}{r}.
\]

Then

\[
\boxed{
q'(r)=\frac{B_0(r)}{r^2}
}.
\]

Thus \(B_0>0\) makes \(q\) strictly increasing.  Since the standard kernel
monotonicity gives \(A_0>0\), one also has \(q>0\).

Moreover

\[
B_0=rA_0'-A_0>0
\quad\Longrightarrow\quad
A_0'>\frac{A_0}{r}>0,
\]

so

\[
\boxed{
(\log\Phi)''=-A_0'<0.
}
\]

Therefore first-Laguerre positivity in the \(s(t)=\Phi(\sqrt t)\) coordinate,
together with the standard radial decrease of \(\Phi\), implies strict
log-concavity of \(\Phi\).

Status of this implication: `EXACT`.

The Planat--Solé premise feeding it remains `EXTERNAL_PREPRINT_CLAIM`.

## 5. Adaptive transverse mass envelope

For \(0<b<a\),

\[
-\partial_b\log M(a,b)
=A_0(a+b)-A_0(a-b).
\]

Since \(A_0(r)=rq(r)\) and \(q\) is positive increasing,

\[
A_0(a+b)-A_0(a-b)
\ge 2b\,q(a-b).
\]

Therefore

\[
\boxed{
-\partial_b\log M(a,b)
\ge 2b\frac{A_0(a-b)}{a-b}.
}
\]

Integrating from \(0\) to \(b\), and using monotonicity of \(q\), gives

\[
\boxed{
M(a,b)
\le
M(a,0)
\exp\!\left[-b^2\frac{A_0(a-b)}{a-b}\right].
}
\]

The same formula holds with \(|b|\) by evenness.

Status: `EXACT_CONDITIONAL` under \(A_0>0\) and \(B_0>0\) on the required
radial interval.

Unlike the XF-6 Gaussian envelope, no externally chosen curvature floor
\(\lambda\) appears: the exponent is determined by the kernel itself.

## 6. Signed oscillatory tail

For fixed \(a\), let

\[
M_a(b):=M(a,b).
\]

Suppose \(M_a\) is nonincreasing on \([r,a]\), with \(0\le r<a\), and let
\(x\ne0\). Integration by parts gives

\[
\int_r^a M_a(b)\cos(2xb)\,db
=
\left[\frac{M_a(b)\sin(2xb)}{2x}\right]_r^a
-
\frac{1}{2x}\int_r^a M_a'(b)\sin(2xb)\,db.
\]

Since \(M_a'\le0\), its total variation on \([r,a]\) is
\(M_a(r)-M_a(a)\). Consequently

\[
\boxed{
\left|\int_r^a M(a,b)\cos(2xb)\,db\right|
\le \frac{M(a,r)}{|x|}.
}
\]

Status: `EXACT_CONDITIONAL` under monotonicity of the transverse mass.

Combining with the XF-7 adaptive envelope yields

\[
\boxed{
\left|\int_r^a M(a,b)\cos(2xb)\,db\right|
\le
\frac{M(a,0)}{|x|}
\exp\!\left[-r^2\frac{A_0(a-r)}{a-r}\right].
}
\]

This preserves an explicit inverse-frequency gain from the cosine rather than
replacing the phase by an absolute value before integration.

For the first XF-5 curvature sector this becomes

\[
\left|
 a^2\cosh(2ya)
 \int_r^a M(a,b)\cos(2xb)\,db
\right|
\le
\frac{a^2\cosh(2|y|a)}{|x|}M(a,r),
\]

with the adaptive exponential refinement available above.

## 7. Remaining correlated sector

The XF-5 kernel also contains

\[
b^2\cos(2xa)\cosh(2yb),
\]

whose oscillation is longitudinal in \(a\), not transverse in \(b\).  XF-7
therefore isolates the next precise obligation:

`XF7_GLOBAL_SIGNED_CORE_TAIL_DOMINATION = OPEN_SUFFICIENT_ROUTE`.

A closure must retain the correlation between:

- the exact positive central corridor;
- the signed \(b\)-oscillatory sector bounded above;
- the remaining \(a\)-oscillatory sector.

No reverse implication from this sufficient route is inserted into the typed
solver.

## 8. Numerical validation surface

`src/critical_axis/laguerre_hierarchy.py` validates the exact coordinate
identities with explicit finite Xi-kernel truncation.

`src/critical_axis/signed_tail.py` provides finite-evaluator diagnostics for
the signed integration-by-parts bound.

Reference-point sign checks are labeled numerical diagnostics.  The exact
identities and conditional inequalities are kept separate from sampled
validation.

## 9. Epistemic ledger

| Claim | Status |
|---|---|
| Xi-kernel positivity and strict radial decrease | STANDARD_EXTERNAL_THEOREM |
| Planat--Solé second-level concavity | EXTERNAL_PREPRINT_CLAIM |
| \(s(t)=\Phi(\sqrt t)\) derivative crosswalk | EXACT |
| \(F(r^2)=\Phi^2B_0/(4r^3)\) | EXACT |
| \(q'=B_0/r^2\) | EXACT |
| supplied \(F>0\) + standard radial decrease -> TP2 | EXACT_CONDITIONAL |
| adaptive transverse mass envelope | EXACT_CONDITIONAL |
| signed cosine-tail \(1/|x|\) bound | EXACT_CONDITIONAL |
| full correlated signed core--tail domination | OPEN_SUFFICIENT_ROUTE |
| Riemann hypothesis | OPEN |
