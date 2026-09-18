# TIR CKM Projective Even-Sector Selector Candidate v0.3

Status: `CONDITIONAL_BASE_SELECTOR_CLOSURE / EXACT_A2_COMPOSITE_ROOT / KAPPA_REFINEMENT_OPEN_POSTDICTIVE`

Date: 2026-09-14

## Scope

This surface asks a narrower question than the historical CKM derivation:
can the **base** rational mixing weights be selected from the already validated
600-cell / binary-icosahedral representation structure by one typed rule,
without using CKM data?

The answer is yes conditional on the projective-sector selector stated below.
The later additive refinement \(a\kappa\) is deliberately excluded from the
closure and remains open because its historical provenance is postdictive.

## 1. Exact representation input

For the binary icosahedral group \(2I\subset SU(2)\), let

\[
V_\ell=\operatorname{Sym}^\ell(\mathbb C^2).
\]

Then

\[
\dim V_\ell=\ell+1.
\]

The central element \(-I\in SU(2)\) acts on \(V_\ell\) as

\[
(-1)^\ell I.
\]

Hence representations descending to the projective rotational quotient are the
even sectors.

The existing fail-closed McKay validator proves that the first reducible
restriction of the 600-cell / \(2I\) sequence occurs at

\[
\boxed{\ell_*=6.}
\]

Therefore the complete set of nontrivial projective sectors before and including
the first branching threshold is uniquely

\[
\boxed{\ell_1=2,\qquad\ell_2=4,\qquad\ell_3=6.}
\]

Their representation dimensions are

\[
\boxed{d_1=3,\qquad d_2=5,\qquad d_3=7.}
\]

This produces exactly three ordered projective slots without inserting a
three-generation numerical target.  Physical identification with quark
families remains a candidate binding; mathematically the three-slot carrier is
unique under the stated rule.

## 2. Selector rule

Let the fundamental McKay doublet dimension be

\[
q=2.
\]

The three ordered flavour slots form the \(A_2\) chain

\[
1\;---\;2\;---\;3.
\]

The two simple roots share the middle slot.  To avoid assigning the same
middle-sector scalar to both simple-root strengths, define the independent
simple-root weight from the **exclusive outer endpoint** of each edge by the
same normalized coefficient-space rule

\[
\boxed{
w(d)=\frac{q}{d^2}.
}
\]

Thus

\[
\boxed{
s_{12}^{(0)}=w(d_1)=\frac2{3^2}=\frac29,
}
\]

and

\[
\boxed{
s_{23}=w(d_3)=\frac2{7^2}=\frac2{49}.
}
\]

The shared middle slot supplies the representation-level bridge amplitude

\[
\boxed{
c=\frac{q}{d_2}=\frac25.}
\]

This is independently equal to the exact 600-cell edge-star overlap derived in
v0.1/v0.2.

The selector is reflection-equivariant: reversing the ordered chain exchanges
the two outer endpoints and therefore exchanges the two simple-root weights,
while the middle bridge remains unchanged.

## 3. Composite root

The standard \(A_2\) root algebra gives

\[
[E_{12},E_{23}]=E_{13}.
\]

The non-simple root therefore traverses both simple-root channels and the shared
middle bridge.  The corresponding incidence-dressed coefficient is

\[
\boxed{
s_{13}
=s_{12}^{(0)}\,c\,s_{23}
=\frac29\frac25\frac2{49}
=\frac8{2205}.
}
\]

This is exactly the archived TIR value, now obtained from one ordered selector
rule and the exact local \(A_2\) composition law.

## 4. Relation to the old endpoint dictionary

Stage 33 independently reconstructed

\[
a=\frac27,\qquad b=\frac29,\qquad c=\frac25
\]

from the lower/upper endpoints of the spherical polygonal/McKay ladder:
McKay defining dimension \(2\), affine endpoint node counts \(7,9\), and upper
polygonal endpoint \(5\).

The present derivation is not a restatement of that dictionary:

- \(2/9\) is also the nonzero principal cosine of non-adjacent local \(A_2\)
  planes and the left outer projective coefficient-space fraction;
- \(2/5\) is also an exact edge-star overlap and the middle projective amplitude
  fraction;
- \(2/7\) is also the right outer representation fraction;
- \(2/49\) is the right outer coefficient-space fraction.

Thus the same rational alphabet now has independent endpoint, incidence,
principal-angle and representation-rank provenance.

## 5. Why a^2/2 equals 2/49

Define the right-end amplitude fraction

\[
\boxed{a=\frac{q}{d_3}=\frac27.}
\]

Then the coefficient-space rule gives

\[
\frac{q}{d_3^2}
=\frac1q\left(\frac{q}{d_3}\right)^2.
\]

For \(q=2\),

\[
\boxed{
s_{23}=\frac{a^2}{2}=\frac2{49}.}
\]

Hence the historical factor \(1/2\) is not an extra fitted coefficient in this
selector: it is exactly the conversion between the fundamental-doublet
representation fraction and the associated coefficient-space fraction.

## 6. Base CKM surface

The conditionally selected base surface is therefore

\[
\boxed{
s_{12}^{(0)}=\frac29,
\qquad
s_{23}=\frac2{49},
\qquad
s_{13}=\frac8{2205},
\qquad
\cos\delta=\frac25.
}
\]

Using the exact Jarlskog identity gives

\[
J^{(0)}
=s_{12}^{(0)}s_{23}s_{13}
 c_{12}^{(0)}c_{23}c_{13}^2\sin\delta
\]

with numerical value

\[
\boxed{J^{(0)}\approx2.93817400082514\times10^{-5}.}
\]

This is a structural baseline, not a new prospective prediction.  No observed
CKM entry is consumed in its construction.

## 7. The remaining refinement gate

The currently retained v12 expression is

\[
\boxed{s_{12}=\frac29+\frac27\kappa.}
\]

The coefficient

\[
a=\frac27
\]

has now been recovered independently as the right outer projective
representation fraction, and

\[
\kappa=\frac{\ln2}{24\pi}
\]

has its own internal TIR normalization derivation.

However, the **operation** that sends

\[
\frac29\longmapsto\frac29+\frac27\kappa
\]

is not forced by the projective-sector selector above.  Moreover the historical
provenance audit records that this refinement was introduced after an earlier
CKM comparison.  Therefore it remains

`OPEN_POSTDICTIVE_REFINEMENT`

until an independently fixed oriented connection / linear-response operator
produces it.

This firewall is important: the new geometry closes the rational base selector;
it does not retroactively convert the later refinement into a prediction.

## 8. Conditional uniqueness statement

The base selector is unique **conditional on** the following declared TIR rule:

1. use nontrivial center-even \(2I\) sectors through the first reducibility
   threshold;
2. order them by increasing \(\ell\);
3. assign each simple root the same normalized coefficient-space doublet
   fraction at its exclusive outer endpoint;
4. use the shared middle representation fraction as the bridge amplitude;
5. generate the non-simple \(13\) root through the \(A_2\) commutator.

Under these conditions there is no remaining discrete choice:

\[
(\ell_1,\ell_2,\ell_3)=(2,4,6)
\]

and

\[
\left(s_{12}^{(0)},s_{23},c,s_{13}\right)
=
\left(\frac29,\frac2{49},\frac25,\frac8{2205}\right).
\]

What remains open is whether this selector rule itself follows from a deeper
TIR dynamical principle rather than being an admitted structural rule, and the
separate \(a\kappa\) refinement.

## 9. Relation to the Stage 37 no-go

Stage 37 proves that scalar functions of one common normal family axis cannot
produce nontrivial family mixing.  The present selector does not use only one
axis: v0.2 supplies a family of distinct local \(A_2\) planes with nontrivial
principal angles, including the exact \(2/9\) transport class.  Thus the new
incidence geometry supplies the type of second geometric structure required by
the Stage 37 no-go.

A future complex family-operator construction must still retain this
noncommuting relative geometry and add a non-removable holonomy phase without
reusing quarantined heavy-family ansatz rows.

## 10. Proof firewall

This candidate does not claim:

- a physical proof that the three even sectors are quark generations;
- a prospective CKM prediction;
- a derivation of the additive \(a\kappa\) refinement;
- that the selector rule is forced without its five explicit premises;
- that a full noncommuting complex \(H_u,H_d\) pair has already been produced
  from clean 600-cell data.

It does establish that the archived rational base CKM weights admit a single,
coherent, executable selector on the clean 600-cell/McKay/A2 structure, with
the historical postdictive refinement isolated rather than hidden.

Validator:

`TIR/validation/tir_ckm_projective_even_sector_selector_candidate_v0_3.py`
