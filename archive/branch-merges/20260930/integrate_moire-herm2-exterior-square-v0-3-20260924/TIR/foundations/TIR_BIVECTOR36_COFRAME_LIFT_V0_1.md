# TIR Bivector-36 to Coframe Lift v0.1

Status: CANDIDATE_FOUNDATIONAL_BRIDGE / EXACT_EXTERIOR_SQUARE_IDENTITIES / STANDARD_PLEBANSKI_CROSSWALK / PHYSICAL_SOURCE_BINDING_OPEN
Date: 2026-09-24

## 1. Purpose

This file replaces the arbitrary question "which four coordinates should be selected from 36?" by a four-dimensional exterior-algebra gate.

For a four-dimensional vector space V,

\[
\dim \Lambda^2 V = \binom42 = 6,
\qquad
\dim \operatorname{End}(\Lambda^2 V)=36.
\]

Thus a 36-component object may be organized naturally as a 6x6 operator on bivectors. This is also the coefficient count of a non-chiral two-form field \(B^{IJ}{}_{\mu\nu}\): six antisymmetric internal pairs \([IJ]\) by six antisymmetric spacetime pairs \([\mu\nu]\).

This counting is exact. It does not imply that every PhaseNav 36-vector is automatically a gravitational B-field.

## 2. Coframe exterior-square map

Let an invertible coframe be represented locally by a 4x4 matrix \(e^I{}_{\mu}\). It induces a linear map on two-forms

\[
\Lambda^2 e:\Lambda^2 V\to\Lambda^2 V.
\]

In the ordered bivector basis

\[
(01,02,03,23,31,12),
\]

its 6x6 matrix is the second compound matrix

\[
\boxed{B=C_2(e)},
\]

whose entries are the 2x2 minors

\[
B_{[IJ][\mu\nu]}=e^I{}_{\mu}e^J{}_{\nu}-e^I{}_{\nu}e^J{}_{\mu}.
\]

Equivalently,

\[
B^{IJ}=e^I\wedge e^J.
\]

This is the direct non-chiral simplicity factorization used as the TIR lift target.

## 3. Wedge-pairing gate

The wedge product gives a canonical symmetric bilinear pairing on \(\Lambda^2 V\) valued in \(\Lambda^4V\). Relative to an orientation/volume normalization and the above basis, its matrix is

\[
J=\begin{pmatrix}0&I_3\\I_3&0\end{pmatrix},
\]

with signature (3,3).

For every invertible coframe,

\[
\boxed{C_2(e)^T J C_2(e)=\det(e)J},
\]

and

\[
\boxed{\det C_2(e)=\det(e)^3}.
\]

Therefore a raw 6x6 hyperlayer matrix M can be rejected before any metric interpretation unless there is a nonzero scalar \(\lambda\) such that

\[
M^TJM=\lambda J,
\qquad
\det M=\lambda^3.
\]

This is an exact necessary liftability gate. Passing it is not declared globally sufficient without connected-component/orientation/reality checks. Locally it is the natural exterior-square representation gate associated with the \(\mathfrak{sl}(4,\mathbb R)\simeq\mathfrak{so}(3,3)\) bivector structure.

## 4. Plebanski/Urbantke crosswalk

Standard Plebanski gravity uses two-form variables plus simplicity constraints to recover tetrad/metric geometry. In the non-chiral formulation the unconstrained B field has 36 components. The simplicity constraints select the metric/tetrad sector rather than allowing a generic 6x6 area-type field.

In a chiral sector, a nondegenerate triple of self-dual two-forms can reconstruct a conformal metric through the Urbantke construction. The standard simplicity relation can be written schematically as

\[
\Sigma^i\wedge\Sigma^j\propto\delta^{ij}\,\omega.
\]

TIR therefore adopts the firewall

\[
\boxed{36D\ \text{hyperlayer} \neq \text{coframe}}
\]

unless a declared decoder produces B data that pass the simplicity/liftability gate.

## 5. Exact half split

After a metric and orientation are available, the Hodge star acts on two-forms. In an oriented Euclidean 4D sector,

\[
\star^2=1,
\]

so the exact projectors are

\[
\boxed{P_{\pm}=\frac12(I\pm\star)}.
\]

Each has rank three, giving

\[
\Lambda^2=\Lambda^2_+\oplus\Lambda^2_-,
\qquad 6=3+3.
\]

In Lorentzian signature, \(\star^2=-1\) on real two-forms; the analogous self-dual/anti-self-dual split is made after complexification, with projectors involving \(\pm i\star\). The Euclidean formula must not be copied unchanged into a real Lorentzian sector.

The factor 1/2 here is theorem-level projector normalization. Its connection to other project-level appearances of 1/2 is a crosswalk, not an identity of physical mechanisms.

## 6. Tetrahedral six-edge indexing firewall

A tetrahedron has exactly six unordered edges, indexed by the two-element subsets of four vertices. A 4D bivector basis also has six antisymmetric index pairs.

There is therefore a natural abstract pair-index crosswalk

\[
\{i,j\}\longleftrightarrow [ij],
\]

but the two six-element structures remain different mathematical objects. The existing TIR rule that distinct six-element structures are not physically identified remains in force.

Stella Octangula may provide an oriented dual-sheet visualization. Any identification with the self-dual/anti-self-dual Hodge sectors requires an explicit orientation/signature map and remains CANDIDATE_ONLY.

## 7. Non-arbitrary 36D -> 4D gate

The proposed chain is now

\[
\boxed{
\mathcal M_{36}
\xrightarrow{\mathcal D}
B\in\operatorname{End}(\Lambda^2V)
\xrightarrow{\text{simplicity/liftability}}
[e]
\xrightarrow{}
g_{\mu\nu}=\eta_{IJ}e^I{}_{\mu}e^J{}_{\nu}
\xrightarrow{}
\omega_{LC}
\xrightarrow{}
R[\omega_{LC}].
}
\]

The first arrow \(\mathcal D\), from the specific PhaseNav/moire observables to B-field coefficients, is still OPEN. The second arrow is no longer arbitrary: it is constrained by exterior-square/Plebanski geometry.

The lift has unavoidable gauge/discrete ambiguity. In particular \(e\) and \(-e\) induce the same \(C_2(e)\). Physical claims must be formulated in gauge-invariant metric/curvature/holonomy quantities.

## 8. Dynamics and gravity firewall

A pointwise liftable B field may produce a spacetime-dependent tetrad \(e(x)\). Gravity is not the 6x6 matrix itself. The physical gate remains

\[
B(x)\to e(x)\to g(x)\to R[g].
\]

A field that is merely a coordinate Jacobian or otherwise globally removable does not establish physical gravity. Conversely, a tetrad-induced metric can have nonzero Levi-Civita curvature even though an auxiliary Maurer-Cartan form built from a group-valued frame is pure gauge; these connections must not be conflated.

## 9. Relation to memory

Once a physical connection is selected, persistent path dependence is represented by holonomy

\[
\mathfrak M[\gamma]=\mathcal P\exp\oint_\gamma\Omega.
\]

The bivector gate gives a natural six-channel carrier for area/loop transport, but it does not by itself prove that the universe is a memory system. That ontological statement remains OPEN.

## 10. Promotion ledger

- dim Lambda^2(R^4)=6: PASS EXACT
- dim End(Lambda^2(R^4))=36: PASS EXACT
- B=C2(e) two-form/coframe map: PASS EXACT
- C2(e)^T J C2(e)=det(e)J: PASS EXACT
- det C2(e)=det(e)^3: PASS EXACT
- perturbed generic 6x6 rejected by exact gate: PASS VALIDATOR
- Hodge 1/2 projectors and 3+3 split in Euclidean 4D: PASS STANDARD
- Lorentzian split requiring complexification: PASS FIREWALL
- Plebanski simplicity B -> tetrad/metric sector: PASS STANDARD CROSSWALK
- Urbantke metric reconstruction from nondegenerate chiral B triple: PASS STANDARD CROSSWALK
- PhaseNav/moire observables -> unique B coefficients: OPEN
- B -> unique tetrad globally: OPEN COMPONENT/GAUGE DETAILS
- hyperlayer dynamics -> Einstein dynamics without inserted GR assumptions: OPEN
- physical universe-memory ontology: OPEN
- Clay Millennium problem closure: NOT CLAIMED

## 11. Standard-literature anchors

The standard crosswalk is grounded in four-dimensional bivector geometry, Plebanski constrained-BF gravity, simplicity constraints and Urbantke metric reconstruction. These anchors are external mathematics/GR results; the TIR novelty claim, if any, concerns only how the project attempts to bind its 36D hyperlayer state to that standard gate.


## 12. Correction: 20D complement is a curvature sector

The earlier liftability discussion remains valid for matrices claimed to be a finite exterior square \(C_2(e)\). However, a generic 36-component relation operator need not be close to that finite-image submanifold in order to be geometrically meaningful.

At the Lie/linear level,

\[
\operatorname{Mat}_6
=
\mathfrak{co}(3,3)_{16}
\oplus
\mathcal Q_{20}.
\]

With \(J\) the wedge pairing, \(Q\in\mathcal Q_{20}\) obeys

\[
JQ=Q^TJ,
\qquad
\operatorname{tr}Q=0.
\]

Setting \(S=JQ\) makes \(S\) symmetric, and \(\operatorname{tr}Q=0\) is exactly the single four-dimensional algebraic Bianchi condition on the associated pair-symmetric four-index tensor. Hence

\[
\boxed{
\mathcal Q_{20}\cong\mathcal K(V),
}
\]

the 20-dimensional space of algebraic Riemann curvature tensors.

Therefore the term "simplicity defect" is deprecated as a universal interpretation of \(Q\). A nonzero \(Q\) may instead be the algebraic-curvature channel. Physical promotion still requires proving that it equals the curvature of the selected spacetime connection, rather than an arbitrary pointwise algebraic tensor.
