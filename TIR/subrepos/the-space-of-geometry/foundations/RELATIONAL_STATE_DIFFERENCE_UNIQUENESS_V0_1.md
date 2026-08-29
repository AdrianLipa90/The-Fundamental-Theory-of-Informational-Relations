# Relational State-Difference Uniqueness v0.1

Status: `EXACT_CONDITIONAL_RELATIONAL_DIFFERENCE_UNIQUENESS_THEOREM_CANDIDATE`

Scope: sharpen the remaining affine quantum-point bridge. The theorem asks whether the canonical relation generator `E_xy proportional to rho_y-rho_x` is selected uniquely by endpoint closure, affine arithmetic compatibility, primitive rotational symmetry and distinction preservation.

## 1. Affine quantum-point carrier

Let

\[
\mathcal A_2=\frac12I+V,
\qquad
V:=\operatorname{Herm}_0(2)\cong\mathbb R^3.
\]

Take the maximally mixed affine center

\[
\rho_*:=\frac12I.
\]

It is fixed by every local `SU(2)` frame transformation.

Let

\[
D:\mathcal A_2\times\mathcal A_2\to V
\]

be a candidate local relational displacement map.

## 2. Endpoint closure implies a difference representation

Assume the endpoint composition law

\[
\boxed{
D(\rho,\tau)=D(\rho,\sigma)+D(\sigma,\tau)
}
\]

for admitted local triples.

Set

\[
f(\rho):=D(\rho_*,\rho).
\]

Then

\[
D(\rho_*,\sigma)
=D(\rho_*,\rho)+D(\rho,\sigma),
\]

so

\[
\boxed{
D(\rho,\sigma)=f(\sigma)-f(\rho).
}
\]

Thus every closed endpoint relation is an exact affine difference of a one-point coordinate map.

## 3. A5 affine arithmetic compatibility

Require that the coordinate map respects affine arithmetic on the normalized-state hull. Writing

\[
\rho=\rho_*+v,
\qquad v\in V,
\]

define

\[
L(v):=f(\rho_*+v)-f(\rho_*).
\]

The affine-compatibility condition is

\[
\boxed{
L(av+bw)=aL(v)+bL(w)
}
\]

whenever the affine combinations are admitted locally, extended by continuity to the affine hull.

Hence

\[
L:V\to V
\]

is a real linear map and

\[
\boxed{
D(\rho,\sigma)=L(\sigma-\rho).
}
\]

This is the precise mathematical form of the A5 bridge used here: arithmetic composition of state differences is inherited by geometric relation composition.

## 4. A7 covariance fixes the linear map up to scale

Require common-frame covariance

\[
\boxed{
D(U\rho U^\dagger,U\sigma U^\dagger)
=U D(\rho,\sigma)U^\dagger.
}
\]

Because `rho_*` is fixed, this implies

\[
L(\operatorname{Ad}_U v)
=\operatorname{Ad}_U L(v).
\]

Thus `L` lies in the commutant of the standard real `SO(3)` representation on

\[
V\cong\operatorname{Herm}_0(2).
\]

That representation is irreducible, and its real commutant consists only of scalar multiples of the identity. Therefore

\[
\boxed{
L=\lambda I_V
}
\]

for some real scalar `lambda`.

Hence

\[
\boxed{
D(\rho,\sigma)=\lambda(\sigma-\rho).
}
\]

## 5. A3 distinction preservation removes the zero map

If

\[
\lambda=0,
\]

then every pair of quantum point states has the same zero relation generator. All admitted state distinctions are collapsed.

Under distinction preservation,

\[
\boxed{\lambda\ne0.}
\]

The sign is an orientation convention and `|lambda|` is the remaining global relation-length scale.

Using the standard Bloch normalization

\[
\rho=\frac12(I+\mathbf r\cdot\boldsymbol\sigma),
\]

the canonical Pauli-coordinate convention is

\[
\boxed{\lambda=2,}
\]

which gives

\[
\boxed{
\mathcal E_{xy}=2(\rho_y-\rho_x)
=(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma.
}
\]

## 6. Uniqueness theorem

### Theorem — relational state-difference uniqueness

For the normalized binary quantum-point affine hull, suppose a local relation map:

1. satisfies endpoint composition;
2. respects affine arithmetic on state differences;
3. is covariant under the full primitive `PSU(2) ~= SO(3)` frame symmetry;
4. preserves nontrivial point-state distinctions.

Then the relation map is uniquely fixed up to one nonzero global scalar:

\[
\boxed{
D(\rho_x,\rho_y)=\lambda(\rho_y-\rho_x),
\qquad \lambda\ne0.
}
\]

With canonical Bloch/Pauli normalization, `lambda=2`.

Thus the affine quantum-point bridge is not an arbitrary vector assignment: under the declared TIR closure/arithmetic/symmetry requirements it is the unique local relation law up to choice of unit and orientation.

## 7. Axiom crosswalk

The candidate axiom inheritance becomes

\[
\boxed{
\begin{array}{rcl}
A2 &\to& \mathcal A_2=I/2+\operatorname{Herm}_0(2),\\[1mm]
A8 &\to& \text{endpoint composition / zero local relation defect},\\[1mm]
A5 &\to& \text{affine arithmetic compatibility},\\[1mm]
A7 &\to& SU(2)\text{ covariance / }SO(3)\text{ equivariance},\\[1mm]
A3 &\to& \lambda\ne0\text{ by distinction preservation}.
\end{array}
}
\]

The mathematical uniqueness closure after these inherited rules is exact.

The remaining foundational task is therefore narrower than `RELATION_AS_CANONICAL_QUANTUM_STATE_DIFFERENCE`: establish the A5 and A8 inheritance rules in the primitive TIR wording strongly enough to justify affine compatibility and endpoint composition as local spatial laws.

## 8. Claim classes

| Statement | Class |
|---|---|
| endpoint cocycle implies `D(rho,sigma)=f(sigma)-f(rho)` | EXACT |
| affine compatibility makes the centered map linear | EXACT |
| an `SO(3)`-equivariant linear endomorphism of the defining real 3D carrier is scalar | EXACT REPRESENTATION THEORY |
| distinction preservation requires `lambda != 0` | EXACT CONDITIONAL |
| the resulting relation law is unique up to scale and orientation | EXACT CONDITIONAL THEOREM |
| A8 supplies endpoint composition as the primitive spatial closure law | TIR AXIOM-INHERITANCE GATE |
| A5 supplies affine arithmetic compatibility of local relation differences | TIR AXIOM-INHERITANCE GATE |
