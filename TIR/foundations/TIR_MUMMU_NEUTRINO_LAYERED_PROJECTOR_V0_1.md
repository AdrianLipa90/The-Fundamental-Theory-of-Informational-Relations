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

\[
(phi,omega,g)
\to
H
\to
psi(\tau)
\to
P_j(\tau)
\to
mathbf n_j(\tau)
\to
mathcal A_j(\tau).
\]

See:

`TIR/foundations/TIR_MUMMU_QHTRI_PAIR_DYNAMICS_SOURCE_WITNESS_V0_1.md`

and

`TIR/foundations/TIR_MUMMU_SOURCE_MAGNUS_ORDER_V0_1.md`.

The source-derived horizontal/projective connection witness is

\[
\boxed{
mathcal W_j
=
left|
\boldsymbol\Omega_j
\times
dot{\boldsymbol\Omega}_j
\right|.
}
\]

For the pinned deterministic PNCS pair-0 fixture,

\[
mathcal W_0
approx
9.02843\times10^{-4}>0.
\]

The smooth-history Magnus defect begins as

\[
Omega_2(T)
=
-\frac{T^3}{12}[A_0,A_1]
+O(T^4),
\]

so the source-preserving MUMMU signature is kept typed rather than collapsed:

\[
\boxed{
mathfrak S_{\rm MUMMU}^{\rm source}
=
(C_4,mathcal W,mathcal D_{mathcal L}).
}
\]

Here the Stella anisotropy is quartic while the smooth horizontal/projective connection history first appears cubically in the Magnus expansion of that connection. This is not the Magnus expansion of the fixed 36D source Hamiltonian. No common scalar order is asserted.


## 17. QHTRI coefficient-identifiability firewall

The remaining QHTRI Hamiltonian coefficients have been isolated in

`TIR/foundations/TIR_MUMMU_QHTRI_COEFFICIENT_IDENTIFIABILITY_NOGO_V0_1.md`.

Write

\[
H=aD+bJ,
\]

where (D) is the standardized diagonal detuning operator and (J) is the
zero-diagonal spectrally normalized coupling operator.

They obey the exact Hilbert-Schmidt orthogonality

\[
\boxed{
operatorname{Tr}(DJ)=0.
}
\]

After normalization,

\[
widehat D=D/|D|_F,
qquad
widehat J=J/|J|_F,
\]

the Hamiltonian has the canonical two-coordinate form

\[
\boxed{
H
=
s
left(
coschi,widehat D
+
sinchi,widehat J
\right).
}
\]

The scale (s) only rescales the unitary time parameter,

\[
U_{s,chi}(t)=U_{1,chi}(st),
\]

while the projective orbit shape is controlled by the dimensionless mixing angle
(chi).

Moreover,

\[
\boxed{
operatorname{Tr}(H^2)=s^2
}
\]

is independent of (chi), so a quadratic minimum-action/norm principle cannot
select the detuning/coupling ratio.

The PNCS defaults (0.25,0.7) therefore remain regression/reference parameters,
not TIR-derived constants.  The only unresolved Hamiltonian freedom is now one
dimensionless mixing angle plus an external time-scale calibration.


## 18. Scale-free mixing-angle calibration

The remaining dimensionless QHTRI mixing angle is now separated from the
absolute Hamiltonian scale by

`TIR/foundations/TIR_MUMMU_QHTRI_MIXING_ANGLE_CALIBRATION_FIREWALL_V0_1.md`.

For a local pair define

\[
R_1
=
\frac{|Omega|}{|dot u|},
qquad
R_2
=
\frac{mathcal W}{|Omega|^3}.
\]

Under a common Hamiltonian scaling (Hmapsto sH),

\[
dot umapsto sdot u,
qquad
Omegamapsto sOmega,
qquad
mathcal Wmapsto s^3mathcal W,
\]

so

\[
\boxed{
R_1, R_2
\text{ are scale invariant.}
}
\]

On the pinned deterministic PNCS branch, (R_1) is numerically strictly
decreasing and (R_2) strictly increasing over (0<chi<pi/2), so the
trajectory shape can calibrate (chi) without fixing the absolute clock rate.

This does not promote (chi) to a fundamental constant. GREMLIN's existing
actuation firewall remains active: a source quantity may control Hamiltonian
parameters only through an explicit independent actuation law/receipt.


## 19. Proper-time scale calibration closure

The Hamiltonian scale is conditionally identifiable once the trajectory has a
typed ORCH/PNLF proper-time receipt:

`TIR/foundations/TIR_MUMMU_QHTRI_PROPER_TIME_SCALE_CALIBRATION_V0_1.md`.

For

\[
H=sK_chi
\]

define the normalized-branch local rate

\[
F_u(chi)
=
left.du/dt\right|_{H=K_chi}.
\]

The source dynamics gives

\[
du/dt=sF_u(chi).
\]

With an admitted time binding

\[
d\tau=g,dt,
\]

one obtains

\[
\boxed{
du/d\tau
=
\frac{s}{g}F_u(chi)
}
\]

and, for (F_u(chi)
eq0),

\[
\boxed{
s
=
g,
\frac{du/d\tau}{F_u(chi)}.
}
\]

Thus scale-free trajectory shape calibrates (chi), while the independent
typed clock receipt calibrates (s).

This closes model-level identifiability of the two QHTRI coefficient degrees of
freedom. It does not derive a fundamental actuation law selecting them before
observation.


## 20. Coefficient-free observed-hydro transport lane

A second local MUMMU transport lane is now available without the QHTRI graph
Hamiltonian defaults:

`TIR/foundations/TIR_MUMMU_COEFFICIENT_FREE_OBSERVED_HYDRO_CP1_V0_1.md`.

It conditionally composes two existing PNCS source components:

\[
\text{TemporalObservationReceipt probabilities}
+
\text{HydrodynamicTrace phases}.
\]

For one pair with fixed post-observation imbalance

\[
u=\frac{p_L-p_R}{p_L+p_R},
qquad
r=sqrt{1-u^2},
\]

and hydrodynamically evolving relative phase

\[
delta(\tau)=\theta_R(\tau)-\theta_L(\tau),
\]

the exact local generator is

\[
\boxed{
Omega
=
dotdelta
(-urcosdelta,,-ursindelta,,r^2).
}
\]

For (0<|u|<1), two sections with nonzero phase velocities and distinct
relative phases generically give

\[
\boxed{
Omega(\tau_1)\timesOmega(\tau_2)
e0.
}
\]

The pinned horizontal/projective connection witness gives

\[
\boxed{
|Omega_{50}\timesOmega_{100}|
approx
5.44020445\times10^{-6}>0
}
\]

without calling `qhtri_graph_hamiltonian` and therefore without using its reference coefficients (0.25,0.7). This witnesses the declared horizontal/projective connection only; the same phase-only trajectory admits a commuting diagonal source-Hamiltonian lift.

A known normalized trajectory also has the unique minimum-Frobenius Hermitian
representation

\[
\boxed{
H_{min}
=
|v\ranglelanglePsi|
+
|Psi\ranglelangle v|
-
langlePsi|v\rangle
|Psi\ranglelanglePsi|,
qquad
v=idotPsi.
}
\]

This closes a coefficient-free **descriptive** operator lane.  It does not
replace the predictive-dynamics problem: (H_{min}) represents an already
admitted trajectory rather than selecting that trajectory in advance.

The current native-source boundary remains explicit: PNCS does not yet emit one
receipt binding a `TemporalObservationReceipt` post-state to a
`HydrodynamicTrace` on the same (T^{36}) basis.  Until that object exists,
the composition remains source-compatible and conditional rather than a native
PNCS end-to-end contract.


## 21. Geometric/dynamical connection split

The coefficient-free observed-hydro lane has now been decomposed into its two
distinct operator structures.

The source phase law has the diagonal pair Hamiltonian

\[
\boxed{
H_{\rm phase}
=
-operatorname{diag}(v_L,v_R),
}
\]

so

\[
\boxed{
[H_{\rm phase}(\tau_1),H_{\rm phase}(\tau_2)]=0.
}
\]

The horizontal (CP^1) connection instead uses

\[
Omega
=
n\timesdot n
=
h-(ncdot h)n,
\]

whose direction depends on the moving projective state.  Its time-separated
generators may therefore fail to commute even while the underlying diagonal
phase Hamiltonians commute.

For the pinned observed-hydro fixture:

\[
|Omega_{50}\timesOmega_{100}|
approx5.44020445\times10^{-6},
\]

while the dynamical-Hamiltonian commutator is exactly zero.

Thus downstream MUMMU claims must type noncommutativity as either:

\[
\boxed{\text{GEOMETRIC / HORIZONTAL}}
\]

or

\[
\boxed{\text{DYNAMICAL / HAMILTONIAN}}.
\]

The current coefficient-free source-composed witness closes only the first.


## 21. Direct source-operator non-Abelianity closure

The operator-level ambiguity is separated by

TIR/foundations/TIR_MUMMU_SOURCE_OPERATOR_NONABELIANITY_FIREWALL_V0_1.md.

A changing horizontal \(CP^1\) generator,

\[
\boldsymbol\Omega_j
=
\mathbf n_j\times\dot{\mathbf n}_j,
\]

does not by itself imply a noncommuting source Hamiltonian. Fixed-modulus phase
motion provides an exact counterexample through

\[
H_D(\tau)
=
-\operatorname{diag}\dot\theta(\tau),
\qquad
[H_D(\tau_1),H_D(\tau_2)]=0.
\]

The actual source-operator test is instead performed on the native adaptive
v0.32 semantic trajectory. Because \(g_k\) is updated before each QHTRI lift,

\[
g_k\to J_k\to H_k
\]

is path dependent.

For the frozen seven-role semantic path, all six adjacent Hamiltonian
commutators satisfy

\[
\boxed{
\|[H_k,H_{k+1}]\|_F>0.
}
\]

The measured range is

\[
\boxed{
4.02678\times10^{-4}
\le
\|[H_k,H_{k+1}]\|_F
\le
4.94438\times10^{-4}.
}
\]

Moreover, the coupling channel alone satisfies

\[
\boxed{
[J_k,J_{k+1}]\neq0
}
\]

for every adjacent pair. Therefore the exact default magnitudes
\(0.25\) and \(0.7\) are not required for the existence of source-operator
noncommutativity.

A scale-free operator-direction witness is

\[
\boxed{
\widehat{\mathcal C}^{J}_{k,k+1}
=
\frac{
\|[J_k,J_{k+1}]\|_F
}{
\|J_k\|_F\|J_{k+1}\|_F
}.
}
\]

The local infinitesimal mechanism is even narrower. On the pinned initial
snapshot, pure normalized decay leaves \(J\) directionally unchanged, while
the phase-conditioned Hebbian update satisfies

\[
\boxed{
[J,\dot J]
=
\frac{[j,K_H]}{\rho^2}
\neq0.
}
\]

Numerically,

\[
\boxed{
\|[J,\dot J]\|_F
\approx
9.8075297286\times10^{-2}.
}
\]

The MUMMU source signature should therefore remain typed,

\[
\boxed{
\mathfrak S_{\rm MUMMU}
=
\left(
C_4,\,
\mathcal W_{\rm hor},\,
\mathcal C^H,\,
\mathcal D_{\mathcal L}
\right),
}
\]

where:

- \(C_4\) is the Stella geometric anisotropy;
- \(\mathcal W_{\rm hor}\) belongs to the horizontal/projective \(CP^1\) connection;
- \(\mathcal C^H\) is the direct source-Hamiltonian commutator channel;
- \(\mathcal D_{\mathcal L}\) is the loop/holonomy centrality defect.

No scalar weighting between these coordinates is introduced.

The remaining actuation-law problem is now quantitative and physical: derive
the microscopic origin and gain of the phase-conditioned adaptive coupling law.
It is no longer needed merely to establish the existence of a noncommuting
source-operator history in the computational model.
