# TIR MUMMU Orbital-Algebra Gauge-Covariant Closure v0.1

Status: `EXACT_ORBITAL_ADDRESS_INJECTIVITY / EXACT_PATH_REPRESENTATION_COVARIANCE / EXACT_ORBITAL_OBSTRUCTION_GAUGE_INVARIANCE / CENTRAL_HOLONOMY_PATH_INDEPENDENCE / PHYSICAL_BINDING_OPEN`

Date: 2026-09-23

## 1. Purpose

This theorem closes the path/reference-frame gate left open by
`TIR_MUMMU_QUARTIC_SEAM_ABELIAN_REDUCIBILITY_V0_1.md`
by using the orbital algebra rather than an arbitrary common-frame prescription.

The imported orbital-algebra state is typed as

\[
\boxed{
x_w=(w,\phi_w,\Pi_w,r_w,\theta_w,\tau_w),
}
\]

with structural carrier

\[
\boxed{
\mathcal O=
(V,\star,\circlearrowright,\Pi,\mathcal L,\tau).
}
\]

Here:

- \(w\) is the recursive orbital word/path address;
- \(\star\) is ordered path composition;
- \(\circlearrowright\) is orbital action;
- \(\Pi\) is the local frame/projection datum;
- \(\mathcal L\) is the Lagrange-hypernode/cross-link sector;
- \(\tau\) is proper-time provenance.

This theorem uses only the address, path-composition, local-frame and loop sectors.
It does not identify orbital memory with physical spacetime by assumption.

## 2. Source pins

The PNLF orbital-memory and orbital-governor contracts are read from

`AdrianLipa90/PhaseNav-Natural-Coding-System`

at main commit

`8855abed440e9949f576ffbe2153325f69e78963`.

The centered-hexagonal/Eisenstein source is read from

`AdrianLipa90/On-Primes`

branch

`feat/centered-hexagonal-prime-channel-v01-20260923`

at commit

`465e36061fe3c3e6e072b93020f33d5a60fe0c2f`.

That source proves

\[
H_n=3n^2+3n+1,
\qquad
H_n-H_{n-1}=6n,
\]

and the Eisenstein norm identity

\[
\boxed{
H_n=N((n+1)-n\omega),
\qquad
\omega=e^{2\pi i/3}.
}
\]

The shell count \(n\) and recursive word depth \(|w|\) remain distinct typed
coordinates in this theorem.

## 3. Six-port orbital alphabet

Use the Eisenstein unit alphabet

\[
\boxed{
\mathcal U_6=
\{\pm1,\pm\omega,\pm\omega^2\}.
}
\]

For a finite word

\[
w=a_1a_2\cdots a_d,
\qquad
u_{a_k}\in\mathcal U_6,
\]

define cumulative orientation

\[
P_k(w)=\prod_{j=1}^{k}u_{a_j}.
\]

Let the radial hierarchy be geometric,

\[
r_k=r_0\lambda^{k-1},
\qquad
0<\lambda<1.
\]

Define the orbital address

\[
\boxed{
z(w)=
\sum_{k=1}^{d}
r_k P_k(w).
}
\]

This is a recursive hexagonal/Eisenstein embedding of the orbital path word.

## 4. Prefix-separation theorem

Let \(w\neq v\) be finite words.

If neither is a prefix of the other and \(m\) is the first differing symbol,
then

\[
|P_m(w)-P_m(v)|\ge1
\]

because distinct vertices of the unit hexagon have minimum chord length one.

The tail difference is bounded by

\[
\sum_{k>m}
r_k|P_k(w)-P_k(v)|
\le
2\sum_{k>m}r_k
=
\frac{2r_m\lambda}{1-\lambda}.
\]

Therefore

\[
\boxed{
|z(w)-z(v)|
\ge
r_m\frac{1-3\lambda}{1-\lambda}.
}
\]

If \(w\) is a strict prefix of \(v\), the first extra term gives

\[
\boxed{
|z(v)-z(w)|
\ge
r_{|w|+1}\frac{1-2\lambda}{1-\lambda}.
}
\]

Hence

\[
\boxed{
0<\lambda<\frac13
\Longrightarrow
z:\mathcal W_6\to\mathbb C
\text{ is injective on finite orbital words.}
}
\]

This supplies a canonical geometric address for every finite prefix-tree orbital
path without a lookup table or arbitrary tie-breaker.

## 5. Orbital path representation

Let \(\mathsf{Path}(\mathcal O)\) be the ordered path/groupoid sector generated
by admitted orbital transitions.

Introduce an explicit transport representation

\[
\boxed{
\rho:
\mathsf{Path}(\mathcal O)
\longrightarrow SU(2)
}
\]

satisfying

\[
\boxed{
\rho(\gamma_2\star\gamma_1)
=
\rho(\gamma_2)\rho(\gamma_1).
}
\]

For the unique prefix path \(\gamma_w\) from the root \(0\) to orbital word
\(w\), define

\[
\boxed{
W_{0w}:=\rho(\gamma_w).
}
\]

The six Eisenstein ports supply the discrete branch alphabet. The non-Abelian
content may enter through the frame-dependent lift \(\Pi_w\) and the ordered
composition \(\star\); no claim is made that the scalar Eisenstein units
themselves are noncommuting.

## 6. Local MUMMU twist generator

To avoid conflating proper time \(\tau_w\) with torsion/twist, define a separate
local twist vector

\[
\boldsymbol\vartheta_w\in\mathbb R^3.
\]

Its local spinor generator is

\[
\boxed{
A_w
=
-\frac{i}{2}
\boldsymbol\vartheta_w\cdot\boldsymbol\sigma.
}
\]

Transport it to the root orbital frame:

\[
\boxed{
\widehat A_w
=
W_{0w}A_wW_{0w}^{-1}.
}
\]

This replaces the arbitrary common-frame assumption of the parent theorem with
an orbital-path-derived common frame.

## 7. Gauge covariance

Let each orbital node have a local gauge/frame transformation

\[
g_w\in SU(2).
\]

The local generator transforms as

\[
A_w'
=
g_wA_wg_w^{-1}.
\]

The orbital transporter transforms by endpoint covariance,

\[
\boxed{
W_{0w}'
=
g_0W_{0w}g_w^{-1}.
}
\]

Therefore

\[
\begin{aligned}
\widehat A_w'
&=
W_{0w}'A_w'(W_{0w}')^{-1}\\
&=
g_0\widehat A_wg_0^{-1}.
\end{aligned}
\]

All transported generators undergo the same root-frame conjugation.

## 8. Orbital non-Abelian obstruction

Define

\[
\boxed{
\mathcal O_{\rm orb}
=
\frac12
\sum_{u<v}
\|[\widehat A_u,\widehat A_v]\|_F^2.
}
\]

Because the Frobenius norm is invariant under unitary conjugation,

\[
\boxed{
\mathcal O_{\rm orb}'=\mathcal O_{\rm orb}.
}
\]

Thus the MUMMU non-Abelian obstruction is gauge invariant when transported by
the orbital algebra.

If every \(W_{0w}=I\), this reduces to the common-frame obstruction of the
quartic-seam theorem.

## 9. Lagrange hypernodes and alternate paths

The prefix tree has one canonical root path. A Lagrange hypernode

\[
\boxed{
\Lambda(x_1,\ldots,x_k)=L
}
\]

may admit cross-links between orbital branches and therefore create alternate
paths.

For two root-to-node paths \(\gamma,\gamma'\), define the root-based loop
holonomy

\[
\boxed{
H_{\gamma',\gamma}
=
W_{0w}^{(\gamma')}
\left(W_{0w}^{(\gamma)}\right)^{-1}
\in SU(2).
}
\]

Define the gauge-invariant centrality defect

\[
\boxed{
\delta_{\mathcal L}(H)
=
1-\frac14|\operatorname{Tr}H|^2.
}
\]

For \(SU(2)\),

\[
0\le\delta_{\mathcal L}(H)\le1,
\]

and

\[
\boxed{
\delta_{\mathcal L}(H)=0
\iff
H\in Z(SU(2))
=
\{+I,-I\}.
}
\]

For a finite admitted loop set \(\mathcal C_{\mathcal L}\), define

\[
\boxed{
\mathcal D_{\mathcal L}
=
\sum_{C\in\mathcal C_{\mathcal L}}
\delta_{\mathcal L}(H_C).
}
\]

## 10. Exact path-independence gate

If

\[
\boxed{
\mathcal D_{\mathcal L}=0,
}
\]

all admitted alternate-route holonomies are central.

For any local generator \(A_w\), an alternate path then changes the transporter
only by \(\pm I\), so

\[
\boxed{
\widehat A_w^{(\gamma')}
=
\widehat A_w^{(\gamma)}.
}
\]

Consequently

\[
\boxed{
\mathcal D_{\mathcal L}=0
\Longrightarrow
\mathcal O_{\rm orb}
\text{ is independent of admitted orbital path choice.}
}
\]

If \(\mathcal D_{\mathcal L}>0\), at least one admitted loop has noncentral
holonomy. For every noncentral \(H\in SU(2)\), there exists an
\(A\in\mathfrak{su}(2)\) such that

\[
HAH^{-1}\ne A.
\]

Thus nonzero \(\mathcal D_{\mathcal L}\) is an exact witness that orbital
history can carry information not reducible to the endpoint address alone.

## 11. MUMMU orbital signature

Do not collapse independent invariants into an arbitrary weighted scalar.

The minimal typed orbital signature is the tuple

\[
\boxed{
\mathfrak S_{\rm MUMMU}^{\rm orb}
=
\left(
C_4,
\mathcal O_{\rm orb},
\mathcal D_{\mathcal L}
\right).
}
\]

Its components mean:

- \(C_4\): Stella carrier anisotropy / quartic geometric seam;
- \(\mathcal O_{\rm orb}\): gauge-invariant noncommuting transported twist;
- \(\mathcal D_{\mathcal L}\): noncentral orbital-history/loop defect.

No coefficient joining these coordinates is introduced.

## 12. Relation to the quartic seam

The previous scalar quartic result remains

\[
\Delta\mathfrak P
=
-\frac1{108}C_4
+
\frac{\alpha^2\beta^2}{96}
+
O(6)
\]

for its declared two-history probe.

The orbital algebra does not replace that theorem. It supplies the missing
covariant provenance of the history operator:

\[
\boxed{
w
\to
z(w)
\to
\gamma_w
\to
W_{0w}
\to
\widehat A_w
\to
\mathcal O_{\rm orb}.
}
\]

Thus path memory is no longer represented by a free comparison of two
hand-selected histories.

## 13. Claim ledger

| Statement | Status |
|---|---|
| centered-hexagonal shell increment \(H_n-H_{n-1}=6n\) | `EXACT IMPORTED` |
| Eisenstein norm \(H_n=N((n+1)-n\omega)\) | `EXACT IMPORTED` |
| six-port recursive address definition | `MODEL DEFINITION` |
| \(\lambda<1/3\) implies finite-word address injectivity | `EXACT` |
| orbital transport is a path representation into \(SU(2)\) | `EXPLICIT BRIDGE PREMISE` |
| transported generator transforms by common root conjugation | `EXACT` |
| \(\mathcal O_{orb}\) is gauge invariant | `EXACT` |
| \(\delta_{\mathcal L}=0\iff H=\pm I\) for \(SU(2)\) | `EXACT` |
| \(\mathcal D_{\mathcal L}=0\) gives path-independent transported generators | `EXACT FINITE LOOP SET` |
| noncentral loop permits path-history dependence | `EXACT EXISTENCE STATEMENT` |
| orbital algebra is physical spacetime microstructure | `OPEN / NOT CLAIMED` |
| MUMMU is physically realized by neutrino layers | `OPEN / NOT CLAIMED` |

## 14. Validation

Deterministic validator:

`TIR/validation/tir_mummu_orbital_algebra_gauge_closure_v0_1.py`

Static receipt:

`TIR/validation/TIR_MUMMU_ORBITAL_ALGEBRA_GAUGE_CLOSURE_VALIDATION_V0_1.json`

The validator checks:

1. centered-hexagonal shell and Eisenstein-norm identities;
2. finite-word address separation for the \(\lambda=1/4\) probe;
3. path-composition endpoint gauge covariance;
4. transported-generator covariance;
5. gauge invariance of \(\mathcal O_{orb}\);
6. central \(\pm I\) path independence;
7. noncentral loop defect;
8. explicit noncentral path-memory witness.

## 15. Spin-connection closure

The former free-representation gate is closed by

`TIR/foundations/TIR_MUMMU_ORBITAL_SPIN_CONNECTION_UNIQUENESS_V0_1.md`.

For an admitted liminal trajectory

\[
\Lambda(\tau)=\bigl(\Pi,\theta(\tau),\varphi(\tau),\tau\bigr),
\]

define

\[
P(\tau)=\Pi[\theta(\tau)]
=\frac12(I+\mathbf n\cdot\boldsymbol\sigma).
\]

Projector kinematics forces every admissible \(SU(2)\) angular generator to be

\[
\boldsymbol\Omega
=
\mathbf n\times\dot{\mathbf n}
+
\lambda\mathbf n.
\]

The existing lifted orbital phase fixes the only remaining fiber freedom,

\[
\lambda=\dot\varphi,
\]

so the transporter is generated by the unique connection

\[
\boxed{
\mathcal A_\tau
=
-\frac{i}{2}
\left[
\mathbf n\times\dot{\mathbf n}
+
\dot\varphi\mathbf n
\right]\cdot\boldsymbol\sigma.
}
\]

Therefore

\[
\boxed{
\rho(\Lambda)
=
\mathcal P\exp\int_\Lambda\mathcal A_{\rm orb}
}
\]

is no longer a free bridge premise.

The remaining gate is the source-derived sector projection

\[
\boxed{
\Pi:T^{36}\to CP^1
}
\]

and the admission rule for the allowed Lagrange-loop set
\(\mathcal C_{\mathcal L}\), both without post-hoc fitted coefficients.
