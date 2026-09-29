# TIR Primitive Dependency Lattice v0.1

Status: `PRIMITIVE_DEPENDENCY_LATTICE_CANDIDATE`

Scope: TIR-only analysis of primitive dependencies. Temporal normalization, phase-rate selection, temporal-wave dynamics, and NOW dynamics are downstream crosslink work. The present frontier asks which structures follow from the A0 relational-existence root plus the eight A1--A8 TIR axioms before temporal dynamics enters.

## 1. Primitive axioms by logical role

A0 is the relational-existence root definition. The eight owner axioms A1--A8 then separate naturally into four roles.

### Ontological / representational roots

- **A0 — Relational Existence / Zero:** existence is admitted only through realized distinction/relation; the pre-object zero is `Z_rel=(empty,empty)` and contains no object.
- **A1 — Point Minimality:** the minimal non-empty support candidate is a point `P`, distinct from relational zero.
- **A2 — Quantum Point:** the minimal carrier admits a quantum-state representation.
- **A3 — Information Primacy:** physically relevant structure is carried by distinguishable informational relations.

### Symmetry / geometry roots

- **A4 — Spherical Geometric Efficiency:** spherical realization is selected by the declared isotropic boundary/volume efficiency functional.
- **A7 — Universal Symmetry:** primitive relational laws admit symmetry actions.

### Arithmetic roots

- **A5 — Arithmetic Measures Geometry:** arithmetic values encode geometric invariants.
- **A6 — Natural Numbers from Complex Phase Closure:** natural indices arise operationally as discrete closure/winding indices of complex phase structure.

### Meta-closure root

- **A8 — Paradox Stabilization:** incompatible valid projections trigger a higher-order contextual closure constraint.

These roles are distinct. In particular A6 is not used as a premise to create the first binary distinction.

## 2. Circularity firewall: zero, support, distinction, then exchange

The primitive dependency begins before the point:

\[
\boxed{
\mathfrak Z_{\rm rel}
=
(\varnothing,\varnothing).
}
\]

By the A0 semantics there is no existent object in this presentation. The least nonempty support is then the singleton point

\[
\boxed{
\mathcal P=\{p\}.
}
\]

The point is support only; it is not yet a realized relation.

Let \(\Pi\) be a partition of the point's state/aspect domain. Nontrivial distinction means more than one nonempty block,

\[
|\Pi|>1.
\]

Therefore the minimal nontrivial distinction satisfies

\[
\boxed{
|\Pi_1|=2,
\qquad
\Pi_1=\{N,S\}.
}
\]

This is ordinary meta-mathematical cardinality, not the later physical-emergence claim of A6.

Only after the two outcomes exist does A7 supply exchange symmetry,

\[
J:N\leftrightarrow S,
\qquad
J^2=\mathrm{id}.
\]

Thus the non-circular primitive chain is

\[
\boxed{
\mathfrak Z_{\rm rel}
\rightarrow
\mathcal P
\rightarrow
\{N,S\}
\rightarrow
J:N\leftrightarrow S.
}
\]

The earlier route that inferred binarity from a nontrivial involution is no longer needed as the foundational proof: the involution is now the symmetry of the already-minimal binary distinction.

## 3. Half from exchange invariance

Attach normalized relational weights

\[
w_N+w_S=1.
\]

A7 exchange invariance requires

\[
(w_N,w_S)=(w_S,w_N),
\]

hence

\[
w_N=w_S.
\]

Normalization then gives

\[
\boxed{w_N=w_S=\frac12.}
\]

Thus the half-point needs no temporal input and no phase-rate input. It is the unique normalized fixed share of primitive pole exchange.

Equivalently, with `u=w_S`,

\[
J(u)=1-u,
\qquad
\operatorname{Fix}(J)=\left\{\frac12\right\}.
\]

## 4. ln 2 from information primacy

Using the A3 Shannon carrier for a binary normalized relation,

\[
H_2(u)=-(1-u)\ln(1-u)-u\ln u,
\]

the symmetric primitive distinction gives

\[
\boxed{H_2(1/2)=\ln2.}
\]

Therefore the first primitive closed chain is

\[
\boxed{
0_{\rm rel}
\rightarrow
\text{POINT SUPPORT}
\rightarrow
\text{MINIMAL BINARY DISTINCTION}
\rightarrow
\text{EXCHANGE SYMMETRY}
\rightarrow
\frac12
\rightarrow
\ln2.
}
\]

Its minimal TIR parent set is:

```text
A0  relational-existence semantics / empty relational zero
A1  minimal nonempty point support
D1  minimal nontrivial distinction -> binary partition
A3  informational weighting / Shannon carrier
A7  exchange symmetry
```

A2 is not required for the scalar half/ln2 theorem. It enters at the coherent lift.

## 5. Quantum lift as an independent converging branch

A2 assigns the primitive point a quantum representation. Once the first exchange pair exists, the minimal coherent carrier spanning both alternatives is

\[
\boxed{\mathcal H_{NS}\cong\mathbb C^2.}
\]

With pole basis `|N>`,`|S>`, the equal-weight coherent family is

\[
\boxed{
|\psi_{1/2}(\varphi)\rangle
=\frac{|N\rangle+e^{i\varphi}|S\rangle}{\sqrt2}.
}
\]

The scalar half-point therefore lifts to a relative-phase family. This is a primitive coherent structure; its temporal parametrization belongs to the temporal crosslink rather than to the present dependency frontier.

The minimal parent set for this node is

```text
A2  quantum carrier
+ primitive binary distinction
+ half balance
```

## 6. Sphere: two independent roads converge

There are two distinct TIR roads to spherical structure.

### Quantum-projective road

For a two-state complex quantum carrier,

\[
\mathbb{CP}^1\cong S^2.
\]

Thus the Bloch sphere follows from the standard projective geometry of the A2 binary quantum lift.

### Geometric-selection road

A4 independently selects the sphere for the declared isotropic fixed-volume/minimal-boundary functional via

\[
A^3\ge 36\pi V^2,
\]

with equality at the sphere.

Therefore A4 is a **convergent selector**, rather than a necessary premise for the mathematical identity `CP^1 ~= S^2`.

This is an important dependency distinction:

\[
\boxed{
A2+\text{binary quantum carrier}
\rightarrow \mathbb{CP}^1\cong S^2
\leftarrow A4\text{ spherical efficiency selection}.
}
\]

## 7. Arithmetic branch after geometry and complex phase

A5 and A6 are kept downstream of the first distinction.

For complex phase

\[
z=e^{i\theta},
\]

a closed orbit satisfies

\[
z^n=1.
\]

Equivalently,

\[
\Delta\theta=2\pi n
\]

for a winding/closure index. A5 interprets such discrete values as arithmetic measures of geometric closure; A6 promotes the closure index as the operational TIR origin of natural-number labels.

The dependency is therefore

\[
\boxed{
\text{complex phase geometry}
\xrightarrow{A5}\text{discrete geometric invariant}
\xrightarrow{A6}\text{natural closure index}.
}
\]

This ordering removes the need to assume physical natural-number emergence in order to derive the earlier binary distinction.

## 8. A8 as a transverse closure operator

A8 is not a parent of `1/2` or `ln2`. It acts across the lattice whenever two valid projections cease to fit inside one current representation.

Represent this schematically as

\[
\boxed{
(P,C_1;\neg P,C_2)
\xrightarrow{A8}
\widetilde X(C_1,C_2),
}
\]

where the enlarged carrier preserves the contexts and requires a closure law.

Thus A8 is transverse to the generative spine:

```text
primitive branch -----> derived structure
       |                     |
       +------ A8 gate ------+
              when contextual incompatibility appears
```

## 9. Minimal dependency table

| Derived node | Minimal TIR parents | Mathematical bridge |
|---|---|---|
| primitive point | A1 | foundational postulate |
| exchange partner / pole pair | A1 + A7 | nontrivial involution orbit |
| normalized half balance | pole pair + A3 + A7 | exchange invariance + normalization |
| `ln2` | half balance + A3 | binary Shannon identity |
| complex two-state carrier | pole pair + A2 | two-state Hilbert span |
| coherent half family | `C^2` + half balance | relative complex phase |
| Bloch sphere | `C^2` | `CP^1 ~= S^2` |
| sphere selected as efficient isotropic enclosure | A4 | isoperimetric equality case |
| arithmetic geometric invariant | geometry + A5 | winding / degree / multiplicity |
| natural closure index | complex phase + A5 + A6 | phase closure |
| paradox closure gate | A8 + contextual incompatibility | context lift |

## 10. Primitive frontier

The active TIR primitive frontier is

\[
\boxed{
\text{POINT}
\rightarrow
\text{FIRST EXCHANGE}
\rightarrow
\{N,S\}
\rightarrow
\frac12
\rightarrow
\ln2
}
\]

with the converging structural branches

\[
\{N,S\}
\xrightarrow{A2}
\mathbb C^2
\rightarrow
\mathbb{CP}^1\cong S^2,
\]

and

\[
S^2/\text{phase geometry}
\xrightarrow{A5,A6}
\text{discrete arithmetic closure indices}.
\]

The temporal programme receives these structures as crosslink inputs and owns the later temporal derivations.

## 11. Supersession note

`TIR_FIRST_DISTINCTION_THEOREM_V0_2.md` is the current primitive proof surface for the first distinction. The earlier v0.1 file remains historical provenance.