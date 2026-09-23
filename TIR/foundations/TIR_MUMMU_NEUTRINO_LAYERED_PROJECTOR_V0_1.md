# TIR MUMMU Neutrino-Layered Holographic Projector v0.1

Status: `MODEL_CANDIDATE / EXACT_LAYER_INTERFERENCE_THEOREM / EXACT_MOIRE_TWIST_SCALING / NEUTRINO_PHYSICAL_BINDING_OPEN / GRAVITY_BINDING_OPEN`

Date: 2026-09-23

## 1. Scope and epistemic boundary

This note formalizes a TIR model candidate: a layered holographic carrier built from Stella Octangula/Bloch cells, coherent cell oscillations, and relative layer twist. The emergent inter-layer interference field is named **MUMMU**.

The exact mathematics below concerns layered wave/interference geometry. Identification of the layers with physical neutrinos, of the collective source with physical mass density, or of the emergent metric with spacetime gravity is not established by these identities and remains a physical binding problem.

## 2. Layer carrier

Let

\[
\mathcal N=\{\Sigma_n\}_{n\in\mathbb Z}
\]

be an ordered family of holographic layers. Each layer carries the antipodally closed tetrahedral Bloch frame

\[
\Sigma_{\rm stella}=T\cup(-T),
\]

with eight Stella Octangula rays inherited from `TIR_STELLA_DISTINCTION_HOLONOMY_BRIDGE_V0_1.md`.

For reciprocal channel \(a\) on layer \(n\), define

\[
\psi_{n,a}(\mathbf x,t)
=c_{n,a}\exp\{i[\mathbf k_{n,a}\cdot\mathbf x-\omega_{n,a}t+\phi_{n,a}]\}.
\]

The layer orientation is

\[
\mathbf k_{n,a}=R(\theta_n)\mathbf k_{0,a}.
\]

The projected field and observable intensity are

\[
\boxed{\Psi(\mathbf x,t)=\sum_{n,a}\psi_{n,a}(\mathbf x,t)},
\qquad
\boxed{\mathcal P(\mathbf x,t)=|\Psi(\mathbf x,t)|^2}.
\]

## 3. MUMMU as the relational field

Define the MUMMU field as the non-diagonal part of the projector:

\[
\boxed{
\mathcal M
:=\sum_{(n,a)\ne(m,b)}
\psi_{n,a}\psi_{m,b}^*
}.
\]

Thus

\[
\mathcal P=\sum_{n,a}|\psi_{n,a}|^2+\mathcal M.
\]

MUMMU is therefore typed as a relational/interference field.

## 4. Exact two-layer moire scale

For one reciprocal channel with lattice period \(a\),

\[
k=\frac{2\pi}{a}.
\]

Let the second layer be rotated by \(\delta\theta\). Then

\[
\Delta\mathbf q=[R(\delta\theta)-I]\mathbf k
\]

has exact magnitude

\[
\boxed{|\Delta\mathbf q|=2k\sin\frac{|\delta\theta|}{2}}.
\]

Hence

\[
\boxed{
L_M=\frac{2\pi}{|\Delta\mathbf q|}
=\frac{a}{2\sin(|\delta\theta|/2)}
}.
\]

For \(|\delta\theta|\ll1\),

\[
\boxed{L_M\sim\frac{a}{|\delta\theta|}}.
\]

## 5. Layer torsion law

Define the model-specific layer-twist density

\[
\boxed{\tau_L(z):=\frac{d\theta}{dz}}.
\]

This must not be silently identified with Cartan torsion \(T^a\); the existing TIR curvature/torsion firewall remains intact.

For neighboring layers separated by \(d\),

\[
\delta\theta\simeq\tau_L d,
\]

so

\[
\boxed{
L_M\simeq\frac{a}{|\tau_L|d}
}.
\]

In the distinguished equal-spacing/equal-cell-scale case \(d=a\),

\[
\boxed{L_M\simeq\frac1{|\tau_L|}}.
\]

Thus the macroscopic interference length is, to leading order, the inverse layer-twist density and is independent of the microscopic carrier length.

## 6. N-layer holographic sharpening theorem

For a single channel whose inter-layer phase increment is \(\chi\),

\[
\Psi_N(\chi)=\sum_{n=0}^{N-1}e^{in\chi}.
\]

Therefore

\[
\boxed{
\Psi_N(\chi)
=e^{i(N-1)\chi/2}
\frac{\sin(N\chi/2)}{\sin(\chi/2)}
}
\]

and

\[
\boxed{
I_N(\chi)
=\left|\frac{\sin(N\chi/2)}{\sin(\chi/2)}\right|^2.
}
\]

The coherent maximum is

\[
\boxed{I_N(0)=N^2}.
\]

If \(\chi=\Delta q\,x\), the moire period is \(L_M=2\pi/|\Delta q|\), while the first zeros around a principal maximum occur at

\[
\boxed{|x|=\frac{L_M}{N}}.
\]

Hence the coherent projection sharpens as \(1/N\).

## 7. Neutrino phase-clock instantiation

TIR already carries

\[
\ell_\phi=\frac{\hbar c}{E}.
\]

If, as a model candidate only, a neutrino mass eigenstate at rest supplies \(E_i=m_i c^2\), define

\[
\boxed{a_i:=\ell_{\nu_i}=\frac{\hbar c}{m_i c^2}}.
\]

Using the current internally reconciled TIR candidate masses

\[
(m_1,m_2,m_3)=
(0.0050099939,0.0100199878,0.0500999391)\ {\rm eV}
\]

gives

\[
\boxed{
(\ell_{\nu_1},\ell_{\nu_2},\ell_{\nu_3})
\approx
(39.3867,19.6933,3.93867)\ \mu{\rm m}.
}
\]

The candidate mass ratio \(1:2:10\) therefore gives the inverse phase-clock ratio

\[
\boxed{1:\frac12:\frac1{10}}.
\]

No empirical promotion is implied.

## 8. Conditional weak-field bridge

The existing hexahedral/Bloch metric carrier has

\[
h_0=\frac{\ell_\phi^2}{6}I_3.
\]

Introduce a dimensionless collective layer deformation \(u(\mathbf x)\) through

\[
\omega(\mathbf x)=\omega_0e^{u(\mathbf x)},
\qquad
\ell_\phi(\mathbf x)=\ell_0e^{-u(\mathbf x)}.
\]

Then

\[
\boxed{h(\mathbf x)=h_0e^{-2u(\mathbf x)}}
\]

and for \(|u|\ll1\),

\[
\boxed{h\simeq h_0(1-2u)}.
\]

If a source density \(\rho_s\) couples to a gapless collective mode with

\[
\mathcal E[u]=\int d^3x\left[
\frac C2|\nabla u|^2+\lambda\rho_su
\right],
\]

stationarity gives

\[
\boxed{\nabla^2u=\frac{\lambda}{C}\rho_s}.
\]

The Newtonian weak-field equation is therefore recovered conditionally if

\[
\boxed{u=\Phi/c^2},
\qquad
\boxed{\lambda/C=4\pi G/c^2}.
\]

This does not derive \(G\). It isolates the microscopic closure target: derive \(\lambda/C\) from layered Stella/MUMMU dynamics.

## 9. Minimal universe pipeline

\[
\boxed{
0
\to
\text{distinction}
\to
\{\Sigma_n\}
\to
\text{Stella/Bloch oscillation}
\to
\tau_L
\to
\mathcal M\;(\text{MUMMU})
\to
\mathcal P
\to
\text{stable projected structure}.
}
\]

## 10. Claim classes

```text
layer carrier               = neutrino-like phase sheets        MODEL CANDIDATE
cell geometry               = Stella Octangula/Bloch closure    EXACT CONDITIONAL UPSTREAM
oscillation/interference    = coherent phase dynamics           EXACT MATHEMATICS
twist-to-moire scale        = L_M=a/[2 sin(delta theta/2)]      EXACT
torsion asymptotic          = L_M~a/(tau_L d)                   EXACT ASYMPTOTIC
special d=a collapse        = L_M~1/tau_L                       EXACT ASYMPTOTIC
N-layer projector           = Dirichlet kernel                  EXACT
physical neutrino identity  = OPEN
semantic mass = gravity     = OPEN
Cartan torsion identification = OPEN
Einstein/Newton closure      = OPEN; conditional bridge stated
```

## 11. Falsification / next gates

1. Derive the allowed layer spacing \(d\) rather than choosing \(d=a\).
2. Derive collective twist stiffness and source coupling \((C,\lambda)\) from the microscopic Stella/Bloch action.
3. Test whether the three neutrino mass channels remain mutually coherent over the required scale.
4. Test Lorentz covariance and compatibility with known neutrino propagation and cosmological constraints.
5. Determine whether layer twist induces the existing TIR Cartan connection while preserving the curvature/torsion firewall.
6. Recover a nontrivial weak-field potential without importing Newton's law beyond the explicit matching gate.

Validator:

`TIR/validation/tir_mummu_neutrino_layered_projector_v0_1.py`


## 12. Quartic-seam refinement

The layered projector now has a dedicated finite theorem surface for the first
non-isotropic Stella signature and the first scalar trace signature of
noncommuting `SU(2)` layer history:

`TIR/foundations/TIR_MUMMU_QUARTIC_SEAM_ABELIAN_REDUCIBILITY_V0_1.md`

The exact common-frame obstruction is

\[
\mathcal O_{\rm NC}
=
\frac12\sum_{m<n}
|\boldsymbol\tau_m\times\boldsymbol\tau_n|^2.
\]

On the commuting sector \(\mathcal O_{\rm NC}=0\), the finite transport is
simultaneously diagonalizable and, with uniform inter-layer phase increment,
reduces to the scalar Dirichlet channels of Section 6.

For the equal-weight Stella carrier, the first orientation-selecting harmonic is
quartic:

\[
S(\mathbf q)
=
1-\frac{r^2}{6}+\frac{r^4}{120}
-\frac1{108}C_4(\mathbf q)+O(r^6).
\]

For the declared sequential-vs-constant-axis `SU(2)` comparison with the same
integrated generator vector, the scalar history difference is also quartic:

\[
K_{\rm seq}-K_{\rm const}
=
\frac{\alpha^2\beta^2}{96}
+O(6).
\]

Their combined leading defect defines the **MUMMU quartic seam**:

\[
\boxed{
\Delta\mathfrak P
=
-\frac1{108}C_4(\mathbf q)
+
\frac{\alpha^2\beta^2}{96}
+
O(6).
}
\]

This refinement is mathematical only. It does not promote the physical
neutrino-layer, Cartan-torsion, or gravitational interpretations.


## 13. Orbital-algebra transport closure

The MUMMU history channel is now bound to the orbital algebra rather than an
arbitrary common frame:

`TIR/foundations/TIR_MUMMU_ORBITAL_ALGEBRA_GAUGE_COVARIANT_CLOSURE_V0_1.md`

The recursive six-port Eisenstein address is

\[
z(w)=
\sum_{k=1}^{|w|}
r_k\prod_{j=1}^{k}u_{a_j},
\qquad
u_{a_j}\in\{\pm1,\pm\omega,\pm\omega^2\}.
\]

For geometric radial ratio \(0<\lambda<1/3\), finite orbital words have
distinct addresses.  Their canonical prefix paths define orbital transport
\(W_{0w}\), and local twist generators are compared only after transport to the
root frame:

\[
\widehat A_w=W_{0w}A_wW_{0w}^{-1}.
\]

The gauge-invariant obstruction and Lagrange-loop defect are retained as
separate coordinates,

\[
\mathcal O_{\rm orb}
=
\frac12\sum_{u<v}
\|[\widehat A_u,\widehat A_v]\|_F^2,
\]

\[
\mathcal D_{\mathcal L}
=
\sum_C
\left(
1-\frac14|\operatorname{Tr}H_C|^2
\right).
\]

Together with the Stella quartic harmonic, the minimal typed signature is

\[
\boxed{
\mathfrak S_{\rm MUMMU}^{\rm orb}
=
(C_4,\mathcal O_{\rm orb},\mathcal D_{\mathcal L}).
}
\]

No arbitrary weighting between these invariants is introduced.


## 14. Derived orbital spin connection

The orbital path representation is now generated from admitted liminal
trajectories rather than supplied as a free \(SU(2)\) map:

`TIR/foundations/TIR_MUMMU_ORBITAL_SPIN_CONNECTION_UNIQUENESS_V0_1.md`.

Let

\[
P(\tau)
=
\Pi[\theta(\tau)]
=
\frac12(I+\mathbf n(\tau)\cdot\boldsymbol\sigma)
\]

be the explicit local \(CP^1\) reduction of the full T36 trajectory, and let
\(\varphi(\tau)\) be the admitted lifted orbital phase.  Then

\[
\boxed{
\mathcal A_{\rm orb}
=
-\frac{i}{2}
\left[
\mathbf n\times d\mathbf n
+
\mathbf n\,d\varphi
\right]\cdot\boldsymbol\sigma
}
\]

is the unique spin connection compatible with projector motion and the declared
spinorial fiber phase.

The path transporter is therefore

\[
\boxed{
\rho(\Lambda)
=
\mathcal P\exp\left(\int_\Lambda\mathcal A_{\rm orb}\right).
}
\]

This yields two independent exact sources of orbital memory:

\[
d\varphi\neq0
\quad\text{(fiber winding)}
\]

and

\[
\mathbf n\times d\mathbf n\neq0
\quad\text{(projective/Berry geometry)}.
\]

An endpoint-only law \(U_{vu}=F_vF_u^{-1}\) is excluded as a source of
nontrivial MUMMU holonomy because every closed product then telescopes to
identity.  Liminal path data are therefore structurally necessary, not optional.

The remaining mathematical binding is now the sector map
\(\Pi:T^{36}\to CP^1\) and its admission rule.


## 15. Eighteen-pair coupling firewall

The exact source-preserving T36 carrier is eighteen local projective factors,

\[
\Pi_{18}:T^{36}\to(CP^1)^{18},
\qquad
G_{36}=SU(2)^{18}.
\]

The coupling/admission analysis is recorded in

`TIR/foundations/TIR_MUMMU_18PAIR_INTERTWINER_ADMISSION_NOGO_V0_1.md`.

Two consequences are mandatory for downstream MUMMU work.

First, different factors of the uncoupled Lie algebra commute:

\[
[\mathfrak{su}(2)_j,\mathfrak{su}(2)_k]=0
\qquad(j\ne k).
\]

Therefore the non-Abelian MUMMU obstruction is **not** derived from the
uncoupled T36 pair geometry alone.

Second, the cardinality identity

\[
18=6\times3
\]

does not define a six-port × Pauli-triad intertwiner.  A single cyclic
\(C_{18}\) ordering cannot provide it either because

\[
C_{18}\not\cong C_6\times C_3.
\]

The minimal exact admission object is a pair of commuting source permutations

\[
S^6=R^3=I,
\qquad
SR=RS,
\qquad
\langle S\rangle\cap\langle R\rangle=\{I\},
\]

whose anchored joint orbit contains all eighteen pair labels.

Only after such an action is source-derived may different T36 pair sectors be
embedded into a common Pauli frame and contribute to a nonzero
\(\mathcal O_{\rm orb}\).


## 16. Source-derived local dynamics and asymptotic class

The local projective carrier is now dynamically closed at model level through
the existing PNCS QHTRI Hamiltonian:

[
(phi,omega,g)
	o
H
	o
psi(	au)
	o
P_j(	au)
	o
mathbf n_j(	au)
	o
mathcal A_j(	au).
]

See:

`TIR/foundations/TIR_MUMMU_QHTRI_PAIR_DYNAMICS_SOURCE_WITNESS_V0_1.md`

and

`TIR/foundations/TIR_MUMMU_SOURCE_MAGNUS_ORDER_V0_1.md`.

The source-derived local non-Abelian witness is

[
oxed{
mathcal W_j
=
left|
oldsymbolOmega_j
	imes
dot{oldsymbolOmega}_j
ight|.
}
]

For the pinned deterministic PNCS pair-0 fixture,

[
mathcal W_0
approx
9.02843	imes10^{-4}>0.
]

The smooth-history Magnus defect begins as

[
Omega_2(T)
=
-rac{T^3}{12}[A_0,A_1]
+O(T^4),
]

so the source-preserving MUMMU signature is kept typed rather than collapsed:

[
oxed{
mathfrak S_{m MUMMU}^{m source}
=
(C_4,mathcal W,mathcal D_{mathcal L}).
}
]

Here the Stella anisotropy is quartic while the smooth non-Abelian history first
appears cubically at operator level.  No common scalar order is asserted.


## 17. QHTRI coefficient-identifiability firewall

The remaining QHTRI Hamiltonian coefficients have been isolated in

`TIR/foundations/TIR_MUMMU_QHTRI_COEFFICIENT_IDENTIFIABILITY_NOGO_V0_1.md`.

Write

[
H=aD+bJ,
]

where (D) is the standardized diagonal detuning operator and (J) is the
zero-diagonal spectrally normalized coupling operator.

They obey the exact Hilbert-Schmidt orthogonality

[
oxed{
operatorname{Tr}(DJ)=0.
}
]

After normalization,

[
widehat D=D/|D|_F,
qquad
widehat J=J/|J|_F,
]

the Hamiltonian has the canonical two-coordinate form

[
oxed{
H
=
s
left(
coschi,widehat D
+
sinchi,widehat J
ight).
}
]

The scale (s) only rescales the unitary time parameter,

[
U_{s,chi}(t)=U_{1,chi}(st),
]

while the projective orbit shape is controlled by the dimensionless mixing angle
(chi).

Moreover,

[
oxed{
operatorname{Tr}(H^2)=s^2
}
]

is independent of (chi), so a quadratic minimum-action/norm principle cannot
select the detuning/coupling ratio.

The PNCS defaults (0.25,0.7) therefore remain regression/reference parameters,
not TIR-derived constants.  The only unresolved Hamiltonian freedom is now one
dimensionless mixing angle plus an external time-scale calibration.
