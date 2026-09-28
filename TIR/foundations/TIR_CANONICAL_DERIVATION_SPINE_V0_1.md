# TIR Canonical Derivation Spine v0.1

Status: `CANONICAL_SOURCE_RECONCILIATION__ZERO_NONLOGICAL_AXIOMS__NO_COMPILE`

Scope: source-first reconstruction of the TIR foundation from already-existing theorem, Lagrangian, Bloch/Fubini--Study, Berry/Euler, spin-lift, half-seam and affine-geometry surfaces. This document does not replace the historical sources; it fixes their dependency order and claim classes.

## 0. Axiom count and metalogical layer

TIR declares

\[
\boxed{N_{\rm nonlogical\ axioms}=0.}
\]

Logic, definitions, typing rules and standard mathematical theorems are background machinery. Any TIR-specific statement that cannot be derived from the canonical parents below remains conditional or open and is not silently renamed as a definition.

## 1. Absolute nothing cannot exist

Define absolute nothing by absence of any relation, distinction or referent:

\[
\mathsf N := \neg\exists R.
\]

TIR uses relational existence typing:

\[
\operatorname{Exist}(x)\Longrightarrow\exists R_x.
\]

Therefore an existing absolute nothing would require

\[
\operatorname{Exist}(\mathsf N)
\Longrightarrow
\exists R_{\mathsf N},
\]

while its defining content gives

\[
\mathsf N\Longrightarrow\neg\exists R.
\]

Hence

\[
\boxed{\neg\operatorname{Exist}(\mathsf N).}
\]

This is the canonical replacement for the weaker wording “nothing is not an object.”

The arithmetic symbol \(0\) is not identified with \(\mathsf N\). In TIR, zero is a typed relational nullity:

\[
\boxed{0_R=\text{vanishing value/defect of an admitted relation or map}.}
\]

## 2. Two minima: object and structure

The minimum non-empty object carrier has cardinality one:

\[
|P|=1.
\]

Equivalently, under ordinary topological typing, the minimum object dimension is zero and the connected singleton carrier is a point. Therefore

\[
\boxed{\min(\text{object})=P.}
\]

This does not compete with relational primacy. A point by itself carries no nontrivial internal comparison. The minimum nontrivial structure is a relation:

\[
\boxed{\min(\text{nontrivial structure})=R.}
\]

Thus the canonical typing is

\[
\boxed{
\text{minimum object}=\text{point},
\qquad
\text{minimum nontrivial structure}=\text{relation}.
}
\]

This resolves the historical A1/relational-minimality ambiguity.

## 3. First distinction from a nontrivial relation

A nontrivial relation has two ordered roles. Write them as source and target:

\[
s(R),\qquad t(R).
\]

For a non-self-collapsed relation,

\[
s(R)\neq t(R).
\]

Orientation reversal defines an involution

\[
J:(s,t;R)\mapsto(t,s;R^{-1}),
\qquad
J^2=\mathrm{id}.
\]

Its primitive orbit is therefore

\[
\boxed{\mathcal O_J=\{N,S\}.}
\]

This is the source-clean version of the existing first-distinction theorem: the two poles are roles of the minimum nontrivial relation, not independent substances.

## 4. Exchange balance, half-seam and information

For normalized nonnegative shares,

\[
w_N+w_S=1,
\]

exchange invariance gives

\[
(w_N,w_S)=(w_S,w_N)
\Longrightarrow
\boxed{w_N=w_S=\frac12}.
\]

With the binary Shannon functional,

\[
H_2(u)=-(1-u)\ln(1-u)-u\ln u,
\]

the balanced relation gives

\[
\boxed{H_2(1/2)=\ln2.}
\]

The scalar branch is therefore

\[
\boxed{
R\to\{N,S\}\to\frac12\to\ln2.
}
\]

## 5. Minimal continuous phase carrier: \(S^1\cong U(1)\)

The existing relational Lagrangian contains one internal phase coordinate

\[
\chi\in U(1)
\]

with covariant phase velocity

\[
D_t\chi=\dot\chi+\mathcal A_a(q)\dot q^a.
\]

Independently, the half-seam theorem gives the coherent equal-weight phase fibre

\[
\pi^{-1}\!\left(\frac12,\frac12\right)
=
\left\{
\frac{|N\rangle+e^{i\varphi}|S\rangle}{\sqrt2}
:
\varphi\in S^1
\right\}.
\]

Hence the canonical phase carrier is

\[
\boxed{U(1)\cong S^1.}
\]

A connected compact one-dimensional Lie phase group is, up to isomorphism, the circle group. This makes the phase-circle typing structural rather than a coordinate convention.

## 6. Euler--Berry closure forces the primitive spin sector

On the projective two-state surface, the Berry phase of a closed loop enclosing solid angle \(\Omega\) in spin sector \(s\) is

\[
\gamma_B=-s\,\Omega
\]

up to orientation convention.

For the primitive hemisphere loop,

\[
\Omega=2\pi.
\]

The nontrivial Euler projective-sign closure requires

\[
e^{i\gamma_B}=-1.
\]

Therefore

\[
2\pi s=\pi\pmod{2\pi}.
\]

The minimal positive solution is

\[
\boxed{s=\frac12.}
\]

A doubled traversal closes the lift:

\[
\boxed{2\pi\mapsto -I,\qquad 4\pi\mapsto +I.}
\]

This promotes the archived Euler--Berry spin gate into the active foundational source graph while preserving its original epistemic classification: formal/symbolic closure, not a claim about every physical spin assignment.

## 7. Spin polarization forces the pole pair

The spin-\(1/2\) carrier has two eigenstates of a chosen distinction generator:

\[
\sigma_z|N\rangle=+|N\rangle,
\qquad
\sigma_z|S\rangle=-|S\rangle.
\]

Thus the binary relational roles and the spinorial polar states coincide at the canonical two-state realization:

\[
\boxed{\{N,S\}_{R}\longleftrightarrow\{N,S\}_{\rm spin}.}
\]

The relation and the poles are therefore not separately postulated layers.

## 8. From the phase circle to the Bloch sphere without presupposing \(SO(3)\)

The equal-weight coherent states form the equatorial phase circle

\[
S^1_{\rm half}.
\]

The two spin-polar states supply the north and south endpoints. The topological suspension of the equator is

\[
\boxed{\Sigma S^1\cong S^2.}
\]

Equivalently,

\[
S^2
=
\left(S^1\times[-1,1]\right)/
\left(S^1\times\{-1\}\sim S,;
S^1\times\{+1\}\sim N\right).
\]

This is the canonical non-circular route

\[
\boxed{
S^1_{\rm phase}
+
\{N,S\}_{\rm spin}
\longrightarrow
S^2.
}
\]

No prior \(SO(3)\) assumption is used to manufacture the sphere.

Euler phase closure and Euler characteristic are kept distinct. The former selects the nontrivial spinorial sign; the latter provides the consistency check

\[
\chi(S^1)=0,
\qquad
\chi(\Sigma S^1)=2-\chi(S^1)=2
\]

as required for \(S^2\).

## 9. Complex/projective realization and the Bloch metric

With two complex amplitudes and one global \(U(1)\) phase quotient,

\[
|\psi\rangle
=
\alpha|N\rangle+\beta|S\rangle,
\qquad
|\alpha|^2+|\beta|^2=1,
\]

the pure-state ray space is

\[
\boxed{
P(\mathbb C^2)=\mathbb{CP}^1\cong S^2.
}
\]

The induced Fubini--Study metric is

\[
\boxed{
ds_{\rm FS}^2
=
\frac14\left(d\theta^2+\sin^2\theta\,d\varphi^2\right).
}
\]

The Berry curvature is

\[
\boxed{
F_B
=
\frac12\sin\theta\,d\theta\wedge d\varphi,
}
\]

with

\[
\frac1{2\pi}\int_{S^2}F_B=1.
\]

Thus the Bloch/Kähler/Fubini--Study geometry is one coherent projective structure.

## 10. Canonical foundation DAG

The active foundation is not a single overloaded arrow but a commuting dependency graph:

```text
ABSOLUTE NOTHING IS NON-REALIZABLE
        |
        v
MINIMUM OBJECT = POINT
        |
        +-----------------------------+
        |                             |
        v                             v
MINIMUM NONTRIVIAL STRUCTURE = RELATION     RELATIONAL PHASE LAGRANGIAN
        |                             |
        v                             v
ORIENTATION ROLES {N,S}             U(1) ~= S1
        |                             |
        v                             |
EXCHANGE BALANCE 1/2 --> ln2         |
        |                             |
        +-----------> EULER/BERRY NONTRIVIAL SIGN
                           |
                           v
                        SPIN 1/2
                           |
                           v
                      POLAR STATES N,S
                           |
                           v
                 SUSPENSION(S1) ~= S2
                           |
                           v
                     CP1 ~= S2
                           |
                           v
                 FUBINI-STUDY / BERRY
                           |
                           v
                 Herm_0(2) ~= R3
```

The lower geometry then continues through the already-audited affine relation, tetrahedral, holonomy, solder/torsion, Cartan and GR branches.

## 11. Source promotion map

The canonical active proof surfaces are:

- point/first distinction provenance:
  `TIR/foundations/TIR_FIRST_DISTINCTION_THEOREM_V0_2.md`;
- half-seam / \(S^1\) fibre:
  `TIR/foundations/TIR_HALF_SEAM_PHASE_FIBER_V0_1.md`;
- Hilbert--Kähler / Fubini--Study / Berry / relational Lagrangian:
  `archive/v7.9/full/01_foundational_formal_notes/hilbert_kahler_phase_hamiltonian/main.tex`;
- Euler--Berry spin selection:
  `archive/v7.9/full/22_euler_identity_berry_phase_spin_constraint_v2_4/METATIME_SM_EULER_IDENTITY_BERRY_PHASE_SPIN_CONSTRAINT_v2_4.md`;
- spin lift / \(2\pi\)-\(4\pi\) closure:
  `TIR/foundations/TIR_WHITE_THREAD_SPIN_LIFT_LYAPUNOV_V0_1.md`;
- Bloch/Berry spinor cross-check:
  `TIR/zeta_information_axis/monograph/chapters/04_bloch_berry_spinor.tex`;
- affine three-real-dimensional carrier:
  `TIR/foundations/TIR_RELATIONAL_GENERATOR_SPACE_V0_1.md` and the Space-of-Geometry naturality theorems.

The detailed provenance classification is maintained in

`TIR/provenance/TIR_FOUNDATION_PROOF_SOURCE_REGISTRY_V0_1.md`.

## 12. Legacy A1--A8 status

The historical labels remain searchable provenance, but they are not independent axioms.

[
oxed{
N_{\rm legacy\ labels}=8,
\qquad
N_{\rm legacy\ independent\ axioms}=0.
}
]

The current foundation therefore uses

[
oxed{N_{\rm nonlogical\ axioms}=0}
]

while retaining explicit proof obligations for downstream physical bindings.
