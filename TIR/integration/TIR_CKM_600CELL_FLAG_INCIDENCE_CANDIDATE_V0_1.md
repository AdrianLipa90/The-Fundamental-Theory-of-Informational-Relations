# TIR CKM 600-cell Flag-Incidence Bridge Candidate v0.1

Status: `EXACT_INCIDENCE_GEOMETRY / CKM_FORMULA_RECONSTRUCTION / SELECTOR_BINDING_OPEN`

Date: 2026-09-14

## Scope

This surface tests whether the current CKM structural ratios

\[
a=\frac27,\qquad b=\frac29,\qquad c=\frac25
\]

can be recovered from the already implemented regular 600-cell carrier without
using CKM data as input.

The result is deliberately split into two layers.

1. **Closed mathematical layer:** the 600-cell incidence counts, the local
   edge-star overlap \(2/5\), the ratio alphabet \((2/7,2/9,2/5)\), and exact
   reconstruction of the current CKM numerical inputs.
2. **Open selector layer:** a first-principles theorem forcing the three
   flavour channels to consume these readouts in exactly the present
   \(s_{12},s_{23},s_{13}\) pattern.

No physical identification of the 600-cell carrier is promoted here.

## 1. Upstream 600-cell carrier

Use the existing 120 unit vertices of the regular 600-cell in \(S^3\), with
nearest-neighbour adjacency defined by

\[
v_i\cdot v_j=\frac{\varphi}{2},
\qquad
\varphi=\frac{1+\sqrt5}{2}.
\]

The existing carrier is 12-regular with 720 undirected edges.

The present validator independently enumerates every \(K_4\) clique of this
adjacency graph and obtains exactly

\[
\boxed{600}
\]

tetrahedral cells.

From those cells it then reconstructs all lower-dimensional incidences rather
than inserting standard 600-cell face/edge counts by hand.

## 2. Exact local incidence theorem

Let \(\mathcal C\) be the set of 600 tetrahedral cells.

For a triangular face \(f\), define

\[
\operatorname{Star}(f)
=
\{T\in\mathcal C:f\subset T\}.
\]

For an edge \(e\), define

\[
\operatorname{Star}(e)
=
\{T\in\mathcal C:e\subset T\}.
\]

The exhaustive enumeration gives

\[
|\operatorname{Star}(f)|=2
\quad\text{for every one of the 1200 triangular faces},
\]

and

\[
|\operatorname{Star}(e)|=5
\quad\text{for every one of the 720 edges}.
\]

Define the two local incidence cardinalities

\[
\boxed{\nu_F=2,\qquad \nu_E=5.}
\]

They are generated directly from the coordinate model and clique incidence.

## 3. Typed flag packets and the CKM ratio alphabet

For an incident flag \(e\subset f\), distinguish the channel types rather than
taking a literal set union of stars.

A one-sided typed packet contains one face-side channel and one edge-star
channel,

\[
\mathcal P_-:=F\sqcup E,
\]

so

\[
|\mathcal P_-|=\nu_F+\nu_E=7.
\]

A source-to-target typed packet contains two face-side channels separated by
the edge-star channel,

\[
\mathcal P_0:=F_{\rm src}\sqcup E\sqcup F_{\rm dst},
\]

so

\[
|\mathcal P_0|=2\nu_F+\nu_E=9.
\]

The corresponding normalized structural readouts are therefore

\[
\boxed{
a_{\rm inc}
=
\frac{\nu_F}{\nu_F+\nu_E}
=
\frac27,
}
\]

\[
\boxed{
b_{\rm inc}
=
\frac{\nu_F}{2\nu_F+\nu_E}
=
\frac29,
}
\]

and

\[
\boxed{
c_{\rm inc}
=
\frac{\nu_F}{\nu_E}
=
\frac25.
}
\]

Hence the complete ratio alphabet used by the current CKM surface is recovered
from the single local incidence pair \((\nu_F,\nu_E)=(2,5)\).

This is an exact combinatorial statement about the typed packet definitions.
The still-open question is why the flavour-sector selector must use these
particular packet readouts in the current CKM channels.

## 4. Exact edge-star angle giving \(c=2/5\)

Let \(\ell^2(\mathcal C)\) carry the orthonormal tetrahedral-cell basis
\(\{|T\rangle:T\in\mathcal C\}\).

For every edge \(e\), define its normalized edge-star state

\[
\boxed{
|e_\star\rangle
=
\frac1{\sqrt5}
\sum_{T\supset e}|T\rangle.
}
\]

Take two distinct edges \(e,e'\) belonging to the same triangular face \(f\).
A tetrahedral cell contains both edges if and only if it contains their common
face, so

\[
\operatorname{Star}(e)\cap\operatorname{Star}(e')
=
\operatorname{Star}(f).
\]

Since every face belongs to exactly two tetrahedral cells,

\[
|\operatorname{Star}(e)\cap\operatorname{Star}(e')|=2.
\]

Therefore

\[
\boxed{
\langle e_\star|e'_\star\rangle
=
\frac25.
}
\]

The validator checks all

\[
1200\times3=3600
\]

pairs of edges that share a triangular face and finds the same overlap
\(2/5\) in every case.

Thus the current phase angle has an exact incidence-geometric representative:

\[
\boxed{
\delta_{\rm inc}
=
\arccos\langle e_\star|e'_\star\rangle
=
\arccos\frac25.
}
\]

The angle exists mathematically without any CKM fit. Identifying this
incidence angle as the physical CKM phase remains a sector-binding statement,
not a consequence of incidence combinatorics alone.

## 5. Binary half crosscheck

Because a triangular face has exactly two incident tetrahedral cells, exchange
of the two sides gives the normalized equal-share factor

\[
\boxed{h_F=\frac1{\nu_F}=\frac12.}
\]

This is numerically and structurally consistent with the independent Stella
distinction/holonomy half-readout, where orthogonal distinction frames give
\(R=1/2\).

The equality is retained as a crosscheck; the two derivations have distinct
provenance.

## 6. Exact reconstruction of the current CKM structural inputs

Using

\[
a=a_{\rm inc}=\frac27,\qquad
b=b_{\rm inc}=\frac29,\qquad
c=c_{\rm inc}=\frac25,\qquad
h=h_F=\frac12,
\]

the current CKM inputs become

\[
s_{12}=b+a\kappa,
\]

\[
s_{23}=ha^2
=
\frac12\left(\frac27\right)^2
=
\frac2{49},
\]

and

\[
s_{13}
=
s_{23}\,b\,c
=
\frac2{49}\frac29\frac25
=
\frac8{2205}.
\]

Equivalently,

\[
\boxed{
s_{13}=s_{23}\,b\,c,
}
\]

so the \(13\) channel is algebraically the composite of the \(23\) weight,
the uncorrected \(12\) base share, and the edge-star overlap.

The phase is

\[
\delta=\arccos c.
\]

With

\[
\kappa=\frac{\ln2}{24\pi},
\]

the resulting values are

\[
s_{12}=0.22484883650975376,
\]

\[
s_{23}=0.04081632653061224,
\]

\[
s_{13}=0.0036281179138321993,
\]

\[
\delta=66.42182152179817^\circ.
\]

Substitution into the exact CKM/Jarlskog closure gives

\[
\boxed{
J
=
2.9710657666807235\times10^{-5}.
}
\]

No experimental CKM target is consumed by the validator.

## 7. Independent 600-cell / \(2I\) representation crosscheck

The existing 600-cell McKay layer supplies the fundamental binary-icosahedral
doublet

\[
d_Q=2,
\]

the five-dimensional irrep

\[
d_{\rho_5}=5,
\]

and at the first reducible restriction

\[
V_6=\rho_{4b}\oplus\rho_{3b},
\qquad
\dim V_6=4+3=7.
\]

The scalar \(S^3\) harmonic dimensions are

\[
\dim\mathcal H_\ell(S^3)=(\ell+1)^2,
\]

hence

\[
\dim\mathcal H_2=9,
\qquad
\dim\mathcal H_6=49.
\]

Therefore the same ratios admit the independent representation-theoretic
crosswalk

\[
\boxed{
a=\frac{d_Q}{\dim V_6}=\frac27,
}
\]

\[
\boxed{
b=\frac{d_Q}{\dim\mathcal H_2}=\frac29,
}
\]

\[
\boxed{
c=\frac{d_Q}{d_{\rho_5}}=\frac25,
}
\]

and

\[
\boxed{
s_{23}=\frac{d_Q}{\dim\mathcal H_6}=\frac2{49}.
}
\]

This does not by itself prove the flavour selector, but it makes the incidence
recovery non-isolated: the same integer alphabet is reproduced by the
independent \(2I\)/McKay rank structure already present in the repository.

## 8. What is closed and what remains open

### Closed in this candidate surface

- the coordinate 600-cell contains exactly 600 tetrahedral \(K_4\) cells;
- every triangular face has tetrahedral incidence 2;
- every edge has tetrahedral incidence 5;
- the local typed packet dimensions are \(7\) and \(9\);
- the ratio alphabet \((a,b,c)=(2/7,2/9,2/5)\) follows exactly from those
  packet definitions;
- adjacent edge-star unit states have exact overlap \(2/5\);
- the current CKM input values and exact Jarlskog invariant are reconstructed
  from these ratios and \(\kappa\);
- the \(2I\)/McKay representation dimensions independently reproduce the same
  \(2,5,7,9,49\) integer structure.

### Still open

The remaining first-principles theorem is no longer “where do the integers
\(2,5,7,9\) come from?” The remaining gate is the **selector binding**:

\[
\boxed{
\text{derive a flavour-equivariant operator }
\mathcal M_{\rm CKM}
\text{ from the incidence/McKay carrier}
}
\]

such that its standard three-flavour reduction forces, rather than inserts,

\[
s_{12}=b+a\kappa,
\qquad
s_{23}=\frac{a^2}{2},
\qquad
s_{13}=\frac{a^2bc}{2}.
\]

In particular, the additive first-order correction

\[
a\kappa
\]

still requires an operator derivation. It is not promoted merely because the
dimensionless coefficient \(a=2/7\) now has independent incidence and
representation provenance.

A natural next target is an \(SU(3)_F\)-equivariant nearest-neighbour /
commutator construction in which the non-simple \(13\) root is generated from
the \(12\) and \(23\) sectors and the \(2/5\) edge-star overlap appears as the
geometric projection coefficient.

## 9. Proof firewall

This candidate does **not** claim:

- that the 600-cell is physically realized as a literal spacetime or particle
  lattice;
- that incidence cardinalities are automatically quantum amplitudes;
- that the current flavour selector is already unique;
- that the \(a\kappa\) correction has been derived;
- that empirical CKM agreement constitutes a proof of the selector.

The exact claim is narrower: the full discrete ratio alphabet and the current
phase cosine have independent, executable geometric provenance inside the
existing 600-cell candidate.

Validator:

`TIR/validation/tir_ckm_600cell_flag_incidence_candidate_v0_1.py`
