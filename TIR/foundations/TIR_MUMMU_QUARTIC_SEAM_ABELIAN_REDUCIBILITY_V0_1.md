# TIR MUMMU Quartic Seam and Abelian-Reducibility Theorem v0.1

Status: `EXACT_FINITE_STELLA_FACTORISATION / EXACT_COMMON_FRAME_SU2_REDUCIBILITY_CRITERION / EXACT_QUARTIC_ONSET / PHYSICAL_BINDING_OPEN`

Date: 2026-09-23

## 1. Scope

This theorem refines the MUMMU layered-projector candidate by separating:

1. the exact finite geometry of the equal-weight Stella Octangula carrier;
2. the exact common-frame obstruction to Abelian reduction of layered `SU(2)` transport;
3. the leading scalar signature of noncommuting torsion history;
4. the first anisotropic harmonic of the Stella carrier.

The theorem is mathematical. It does not establish that physical neutrinos form the
layers, that layer twist is physical Cartan torsion, or that MUMMU is the physical
spacetime field.

Parent surface:

`TIR/foundations/TIR_MUMMU_NEUTRINO_LAYERED_PROJECTOR_V0_1.md`

## 2. Equal-weight Stella structure factor

Use the eight antipodally completed tetrahedral vertices

\[
\mathcal V
=
\left\{
\frac1{\sqrt3}(s_x,s_y,s_z):
s_x,s_y,s_z\in\{-1,+1\}
\right\}.
\]

Define the normalized structure factor

\[
\boxed{
S(\mathbf q)
=
\frac18
\sum_{\mathbf n\in\mathcal V}
e^{i\mathbf q\cdot\mathbf n}.
}
\]

Because the signs separate independently,

\[
\boxed{
S(\mathbf q)
=
\cos\frac{q_x}{\sqrt3}
\cos\frac{q_y}{\sqrt3}
\cos\frac{q_z}{\sqrt3}.
}
\]

This identity is exact.

## 3. Isotropy through cubic order

The equal-weight moments satisfy

\[
\frac18\sum_{\mathbf n\in\mathcal V}\mathbf n=0,
\]

\[
\boxed{
\frac18\sum_{\mathbf n\in\mathcal V}
n_i n_j
=
\frac13\delta_{ij},
}
\]

and every odd third moment vanishes:

\[
\frac18\sum_{\mathbf n\in\mathcal V}
n_i n_j n_k=0.
\]

Hence no orientation-selecting scalar term survives through cubic order.

Introduce

\[
r^2=q_x^2+q_y^2+q_z^2
\]

and the cubic-symmetry quartic harmonic

\[
\boxed{
C_4(\mathbf q)
=
q_x^4+q_y^4+q_z^4
-
\frac35r^4.
}
\]

Expanding the exact factorization gives

\[
\boxed{
S(\mathbf q)
=
1
-
\frac{r^2}{6}
+
\frac{r^4}{120}
-
\frac1{108}C_4(\mathbf q)
+
O(r^6).
}
\]

Therefore the first anisotropic Stella signature occurs at degree four.

## 4. Common-frame SU(2) layer generators

Let each layer carry a common-frame anti-Hermitian generator

\[
\boxed{
A_n
=
-\frac{i}{2}
\boldsymbol\tau_n\cdot\boldsymbol\sigma,
}
\]

where \(\boldsymbol\tau_n\in\mathbb R^3\) is the layer-twist generator and
\(\boldsymbol\sigma\) is the Pauli vector.

The commutator is

\[
\boxed{
[A_m,A_n]
=
-\frac{i}{2}
(\boldsymbol\tau_m\times\boldsymbol\tau_n)
\cdot\boldsymbol\sigma.
}
\]

With the Frobenius norm,

\[
\boxed{
\|[A_m,A_n]\|_F^2
=
\frac12
|\boldsymbol\tau_m\times\boldsymbol\tau_n|^2.
}
\]

Define the finite common-frame non-Abelian obstruction

\[
\boxed{
\mathcal O_{\rm NC}
=
\sum_{m<n}
\|[A_m,A_n]\|_F^2
=
\frac12
\sum_{m<n}
|\boldsymbol\tau_m\times\boldsymbol\tau_n|^2.
}
\]

Since every summand is nonnegative,

\[
\boxed{
\mathcal O_{\rm NC}=0
\iff
[A_m,A_n]=0
\quad\forall m,n.
}
\]

For `SU(2)` generators this is equivalent to all nonzero
\(\boldsymbol\tau_n\) lying on one common unoriented axis.

Thus all generators are simultaneously diagonalizable exactly on
\(\mathcal O_{\rm NC}=0\).

## 5. Abelian-reducibility theorem

On the sector \(\mathcal O_{\rm NC}=0\), choose the common eigenbasis of the
generators. The two spinor components then acquire only scalar phase increments.
Consequently the transport part of the layered projector splits into two scalar
\(U(1)\) channels.

If, in addition, the phase increment is uniform from layer to layer, each channel
reduces to

\[
\sum_{n=0}^{N-1}e^{in\chi},
\]

and therefore to the Dirichlet projector already derived in the parent MUMMU
surface.

Hence, under the declared common-frame finite-layer assumptions,

\[
\boxed{
\mathcal O_{\rm NC}=0
\Longrightarrow
\text{two scalar phase channels},
}
\]

and with uniform phase increment,

\[
\boxed{
\mathcal O_{\rm NC}=0
\Longrightarrow
\text{Dirichlet-layer reduction}.
}
\]

Conversely, a single global basis in which every infinitesimal layer generator is
diagonal implies pairwise commutation and therefore \(\mathcal O_{\rm NC}=0\).

The Dirichlet conclusion itself additionally requires the uniform-increment
premise; it is not claimed from commutativity alone.

## 6. Same integrated twist, different history

Consider two histories with the same integrated generator vector
\((\alpha,\beta,0)\).

Sequential history:

\[
H_{\rm seq}
=
e^{-i\alpha\sigma_x/2}
e^{-i\beta\sigma_y/2}.
\]

Constant-axis history:

\[
H_{\rm const}
=
e^{-i(\alpha\sigma_x+\beta\sigma_y)/2}.
\]

Define the normalized scalar characters

\[
K_{\rm seq}
=
\frac12\operatorname{Tr}H_{\rm seq},
\qquad
K_{\rm const}
=
\frac12\operatorname{Tr}H_{\rm const}.
\]

Exactly,

\[
\boxed{
K_{\rm seq}
=
\cos\frac\alpha2
\cos\frac\beta2,
}
\]

while

\[
\boxed{
K_{\rm const}
=
\cos\frac{\sqrt{\alpha^2+\beta^2}}2.
}
\]

Therefore an integrated twist vector alone does not determine the scalar holonomy
character.

Under the simultaneous scaling

\[
(\alpha,\beta)\mapsto
(\varepsilon\alpha,\varepsilon\beta),
\]

the difference is

\[
\boxed{
K_{\rm seq}-K_{\rm const}
=
\frac{\varepsilon^4\alpha^2\beta^2}{96}
+
O(\varepsilon^6).
}
\]

There is no order-two history term in this scalar character.

## 7. MUMMU quartic seam

Define the minimal scalar frame-averaged projector

\[
\boxed{
\mathfrak P(\mathbf q,H)
=
S(\mathbf q)
\frac12\operatorname{Tr}H.
}
\]

Compare:

- the exact Stella carrier with sequential noncommuting history;
- an isotropic carrier through quartic order with the constant-axis history
  carrying the same integrated generator vector.

Scale

\[
\mathbf q\mapsto\varepsilon\mathbf q,
\qquad
(\alpha,\beta)\mapsto
(\varepsilon\alpha,\varepsilon\beta).
\]

Then

\[
\boxed{
\Delta\mathfrak P
=
\varepsilon^4
\left[
-\frac1{108}C_4(\mathbf q)
+
\frac{\alpha^2\beta^2}{96}
\right]
+
O(\varepsilon^6).
}
\]

This is the **MUMMU quartic seam**.

The two terms have distinct typed provenance:

\[
-\frac1{108}C_4
\quad\text{: Stella carrier anisotropy},
\]

\[
\frac{\alpha^2\beta^2}{96}
\quad\text{: noncommuting history memory}.
\]

Both survive first at degree four in this scalar readout.

## 8. What is exact and what is open

| Statement | Status |
|---|---|
| eight-vertex Stella structure factor factorizes into three cosines | `EXACT` |
| equal-weight first moment vanishes | `EXACT` |
| second moment is \(I_3/3\) | `EXACT` |
| all third moments vanish | `EXACT` |
| first Stella anisotropy is \(-C_4/108\) at degree four | `EXACT ASYMPTOTIC` |
| \(\mathcal O_{NC}=\frac12\sum|\tau_m\times\tau_n|^2\) | `EXACT COMMON-FRAME` |
| \(\mathcal O_{NC}=0\) iff the finite generator family commutes | `EXACT COMMON-FRAME` |
| commuting family admits a common eigenbasis | `EXACT FINITE SU(2)` |
| uniform commuting layer phases reduce to Dirichlet channels | `EXACT CONDITIONAL` |
| sequential-vs-constant scalar character first differs at quartic order | `EXACT ASYMPTOTIC` |
| combined quartic seam coefficient | `EXACT ASYMPTOTIC` |
| local layer twist equals physical Cartan torsion | `OPEN / NOT CLAIMED` |
| physical neutrino layers realize this carrier | `OPEN / NOT CLAIMED` |
| quartic seam is experimentally present in nature | `OPEN` |
| construction is globally novel in mathematics | `OPEN / PRIOR-ART SEARCH REQUIRED` |

## 9. Gauge/frame firewall

The finite obstruction above is a **common-frame** theorem. Under a common global
change of basis

\[
A_n\mapsto U A_n U^{-1},
\]

the Frobenius commutator norm and therefore \(\mathcal O_{NC}\) are invariant.

For genuinely layer-local gauges, generators at different layers must first be
parallel-transported to a common reference frame before the cross-layer
commutator obstruction is formed. That gauge-covariant extension is a downstream
theorem and is not silently assumed here.

## 10. Validation

Deterministic validator:

`TIR/validation/tir_mummu_quartic_seam_abelian_reducibility_v0_1.py`

Static receipt:

`TIR/validation/TIR_MUMMU_QUARTIC_SEAM_ABELIAN_REDUCIBILITY_VALIDATION_V0_1.json`

Hosted workflow:

`.github/workflows/tir-mummu-quartic-seam-v01.yml`

## 11. Next theorem gate

The next nontrivial gate is to replace the common-frame obstruction with a
gauge-covariant transported obstruction. For a reference layer \(0\), transport
each generator to the same frame,

\[
\widehat A_n
=
W_{0n}A_nW_{0n}^{-1},
\]

and test whether

\[
\sum_{m<n}
\|[\widehat A_m,\widehat A_n]\|_F^2
\]

is independent of admissible path/refinement choices under the declared MUMMU
connection law.

That step would connect the present finite theorem to the existing TIR
holonomy/connection branch without identifying layer twist with physical gravity
by assumption.


## 12. T36/QHTRI source-binding refinement

The earlier inter-factor-only firewall was too strong and is superseded by

`TIR/foundations/TIR_MUMMU_T36_WAVE_FULL_CP1_LOCAL_NONABELIAN_V0_1.md`,

`TIR/foundations/TIR_MUMMU_QHTRI_PAIR_DYNAMICS_V0_1.md`,

and

`TIR/foundations/TIR_MUMMU_QUARTIC_CONTINUUM_REGULARITY_SPLIT_V0_1.md`.

The source T36 phase-plus-amplitude carrier gives eighteen full local
\(CP^1\) factors. QHTRI unitary dynamics moves an individual factor away from
the equal-amplitude equator and generates source-derived noncommuting local
generators.

The two-history quartic theorem admits the basis-independent form

\[
\boxed{
K_{\rm seq}-K_{\rm const}
=
\frac{\varepsilon^4}{96}
|\mathbf a\times\mathbf b|^2
+
O(\varepsilon^6)
=
\frac{\varepsilon^4}{48}
\|[A,B]\|_F^2
+
O(\varepsilon^6).
}
\]

Hence an inter-factor intertwiner is **not required** for a local source-derived
quartic finite-layer history term.

A separate regularity firewall remains necessary. If the same source connection
is treated as one smooth short-time trajectory rather than two finite layer
increments, the path-ordered scalar character differs from its integrated
constant-axis comparator only at

\[
\boxed{O(T^6)}
\]

under the smooth local expansion. The pinned QHTRI fixture exhibits the
corresponding doubling ratio approximately \(64\), not the quartic ratio
\(16\).

Therefore the finite-layer quartic seam and the smooth continuum short-time
limit are distinct typed regimes. What remains open is the source-derived rule
that determines finite MUMMU layer/reduction boundaries.
