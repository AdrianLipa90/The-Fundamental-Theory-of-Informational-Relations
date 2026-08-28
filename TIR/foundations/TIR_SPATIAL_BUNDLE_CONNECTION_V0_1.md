# TIR Spatial Bundle and Connection v0.1

Status: `TIR_SPATIAL_BUNDLE_CONNECTION_CANDIDATE`

Scope: TIR-only continuation of the relational generator-space construction. The local three-dimensional generator carrier is glued across neighboring regions by its natural `SU(2)`/`SO(3)` symmetry. This produces the exact bundle-level precursor of a spatial connection and curvature. Identification with the tangent bundle and the Levi-Civita connection remains an explicit promotion gate.

## 1. Local generator carrier

At each admitted local relational patch `U_alpha`, the binary quantum construction supplies

\[
\boxed{
\mathfrak g_\alpha
\cong
\operatorname{Herm}_0(2)
\cong
\mathbb R^3.
}
\]

Introduce anti-Hermitian generators

\[
\boxed{
T_i=-\frac{i}{2}\sigma_i.
}
\]

They satisfy

\[
\boxed{
[T_i,T_j]=\varepsilon_{ijk}T_k.
}
\]

Thus the same local relational carrier has Lie algebra form

\[
\boxed{
\mathfrak{su}(2)\cong\mathfrak{so}(3)
}
\]

as real Lie algebras.

## 2. Gluing local relational frames

Let two local patches `U_alpha` and `U_beta` overlap. If their binary quantum frames are related by

\[
U_{\alpha\beta}(x)\in SU(2),
\]

then conjugation acts on the traceless Hermitian carrier by

\[
A_\beta
=
U_{\alpha\beta}A_\alpha U_{\alpha\beta}^\dagger.
\]

Through the adjoint representation this gives

\[
\boxed{
R_{\alpha\beta}(x)
=\operatorname{Ad}_{U_{\alpha\beta}(x)}
\in SO(3).
}
\]

Because the adjoint action preserves the Hilbert--Schmidt metric,

\[
\frac12\operatorname{Tr}(A_\beta B_\beta)
=
\frac12\operatorname{Tr}(A_\alpha B_\alpha),
\]

the transition functions preserve local length and orientation.

## 3. Cocycle closure

On a triple overlap, consistent gluing requires

\[
\boxed{
R_{\alpha\beta}
R_{\beta\gamma}
R_{\gamma\alpha}
=I.
}
\]

The corresponding `SU(2)` transitions may close up to the central kernel `{+I,-I}` under the double cover

\[
SU(2)\to SO(3).
\]

An exact `SO(3)` cocycle defines an oriented metric rank-three vector bundle

\[
\boxed{E_{\rm rel}\to\Sigma}.
\]

If a compatible `SU(2)` lift is globally admitted, it defines the corresponding spin bundle structure.

## 4. Connection from frame comparison

A smooth rule for comparing neighboring relational frames is represented locally by an `su(2)`-valued one-form

\[
\boxed{
\mathcal A
=\mathcal A^i T_i.
}
\]

Its curvature is

\[
\boxed{
\mathcal F
=d\mathcal A+\mathcal A\wedge\mathcal A.
}
\]

In components,

\[
\boxed{
\mathcal F^i
=d\mathcal A^i
+\frac12\varepsilon^i{}_{jk}
\mathcal A^j\wedge\mathcal A^k.
}
\]

Under the adjoint map, `A` induces an `so(3)` connection `omega` on the real generator bundle and `F` induces its curvature two-form `Omega`.

Thus the dependency chain is

\[
\boxed{
\text{local binary generator frames}
\to
SU(2)\text{ transition maps}
\to
SO(3)\text{ metric frame bundle}
\to
\omega
\to
\Omega.
}
\]

## 5. Spatial tangent promotion

The relational bundle becomes spatial tangent geometry only after the explicit identification

\[
\boxed{
E_{\rm rel}\;\widehat{=}\;T\Sigma.
}
\]

Once this is admitted, the local Hilbert--Schmidt metric becomes a spatial frame metric and `omega` becomes a metric-compatible spatial connection candidate.

A coframe (solder form)

\[
\boxed{
e^a=e^a{}_i\,dx^i}
\]

is required to identify internal relational directions with coordinate tangent directions.

The induced spatial metric is then

\[
\boxed{
h=\delta_{ab}\,e^a\otimes e^b.}
\]

This is the precise bridge from the internal three-dimensional relation-generator metric to the coordinate metric `h_ij`.

## 6. Levi-Civita gate

Metric compatibility alone does not uniquely select the Levi-Civita connection. The torsion two-form is

\[
\boxed{
T^a
=de^a+\omega^a{}_b\wedge e^b.
}
\]

The Levi-Civita connection is selected by imposing

\[
\boxed{T^a=0}
\]

along with metric compatibility.

Under this gate, the curvature two-form

\[
\Omega^a{}_b
=d\omega^a{}_b
+\omega^a{}_c\wedge\omega^c{}_b
\]

encodes the spatial Riemann tensor through

\[
\boxed{
\Omega^a{}_b
=\frac12 R^a{}_{bcd}\,e^c\wedge e^d.
}
\]

Therefore the continuum target

\[
(\Sigma,h,D,R)
\]

is reached through an explicit sequence of gluing, soldering, and torsion closure rather than being inserted as one undecomposed object.

## 7. Primitive geometry chain after this gate

The TIR spatial branch now has the candidate construction

\[
\boxed{
\mathbb C^2
\to
\operatorname{Herm}_0(2)
\to
E_{\rm rel}
\xrightarrow{\;e\;}
T\Sigma
\to
h
\to
\omega
\xrightarrow{T=0}
D^{\rm LC}
\to
R.
}
\]

The algebraic steps through `E_rel`, its metric, and its `SO(3)` frame symmetry are canonical after the binary quantum carrier. The solder form and tangent-bundle promotion are the central remaining geometric bridge.

## 8. Relation to the eight axioms

- **A2** supplies the complex binary quantum carrier.
- **A7** supplies the symmetry principle realized by local frame transformations.
- **A5** measures the resulting geometry through metric, holonomy, curvature and topological invariants.
- **A4** supplies an independent isotropic spherical selection check on the unit-direction locus.
- **A8** can act when local transition data fail a global closure condition, turning bundle obstruction data into an explicit closure gate.

## 9. Next TIR problem

The next primitive geometric question is no longer the formal existence of a three-dimensional internal carrier. It is the origin of the solder form:

\[
\boxed{
\text{What primitive TIR relation identifies internal generator directions with displacements between relational loci?}
}
\]

A derived solder map would close the bridge from quantum relational geometry to a genuine spatial tangent bundle and would make `h_ij`, connection, torsion and curvature downstream constructions.

## 10. Claim classes

| Statement | TIR class |
|---|---|
| `T_i=-i sigma_i/2` satisfy `su(2)` commutators | EXACT MATRIX IDENTITY |
| `su(2) ~= so(3)` as real Lie algebras | STANDARD EXACT LIE THEORY |
| `SU(2)` adjoint action gives `SO(3)` frame rotations | STANDARD EXACT REPRESENTATION THEORY |
| `SO(3)` cocycle defines an oriented metric rank-three vector bundle | STANDARD BUNDLE THEORY |
| connection curvature `F=dA+A wedge A` | STANDARD EXACT CONNECTION IDENTITY |
| `E_rel = T Sigma` | TIR SPATIAL PROMOTION GATE |
| solder form induces `h=delta_ab e^a tensor e^b` | STANDARD FRAME GEOMETRY |
| torsion-free metric-compatible connection is Levi-Civita | STANDARD EXACT GEOMETRY |
| curvature two-form encodes the Riemann tensor | STANDARD EXACT DIFFERENTIAL GEOMETRY |
| derivation of the solder form from primitive relations | OPEN TIR DERIVATION GATE |
