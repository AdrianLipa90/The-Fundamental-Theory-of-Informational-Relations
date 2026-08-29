# Quantum Relation as Affine Torsor Displacement v0.1

Status: `TIR_QUANTUM_RELATION_AFFINE_TORSOR_BRIDGE_CANDIDATE`

Scope: sharpen the remaining local spatial bridge by separating a standard affine-space theorem from the TIR physical typing rule that identifies a primitive informational relation with the intrinsic displacement between two quantum-point states.

## 1. Quantum-point affine carrier

For the admitted binary quantum carrier

\[
\mathcal H_2\cong\mathbb C^2,
\]

associate to a normalized point state `|psi_x>` its density operator

\[
\rho_x=|\psi_x\rangle\langle\psi_x|,
\qquad
\rho_x=\rho_x^\dagger,
\qquad
\operatorname{Tr}\rho_x=1.
\]

The affine hull of normalized Hermitian two-level states is

\[
\boxed{
\mathcal A_2
=\{\rho=\rho^\dagger:\operatorname{Tr}\rho=1\}
=\frac12I+V,
}
\]

with translation space

\[
\boxed{
V=\operatorname{Herm}_0(2)
\cong\mathbb R^3.
}
\]

The pure-state Bloch sphere affinely spans this same carrier.

## 2. Affine spaces are torsors

An affine space `A` modeled on a real vector space `V` has a free and transitive translation action

\[
A\times V\to A,
\qquad
(x,v)\mapsto x+v.
\]

For every ordered pair `x,y in A` there is a unique vector `v in V` such that

\[
\boxed{x+v=y.}
\]

Define this unique vector as the affine displacement

\[
\boxed{\delta(x,y):=y-x.}
\]

This construction uses no choice of origin.

## 3. Exact torsor identities

The affine displacement obeys identically

\[
\boxed{\delta(x,x)=0,}
\]

\[
\boxed{\delta(y,x)=-\delta(x,y),}
\]

and

\[
\boxed{\delta(x,z)=\delta(x,y)+\delta(y,z).}
\]

Therefore

\[
\boxed{\delta(x,y)+\delta(y,z)+\delta(z,x)=0.}
\]

It is also invariant under a common translation:

\[
\boxed{
\delta(x+a,y+a)=\delta(x,y)
}
\]

whenever the translated points are represented in the same affine chart.

Thus endpoint composition and triangular closure are structural properties of affine displacement itself.

## 4. Canonical quantum relation displacement

Applying the torsor construction to `A_2`,

\[
\boxed{
\delta(\rho_x,\rho_y)=\rho_y-\rho_x
\in\operatorname{Herm}_0(2).
}
\]

With the standard Bloch form

\[
\rho_x=\frac12(I+\mathbf r_x\cdot\boldsymbol\sigma),
\]

we have

\[
\rho_y-\rho_x
=\frac12(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma.
\]

Using the Pauli-coordinate normalization adopted in the spatial branch,

\[
\boxed{
\mathcal E_{xy}:=2\,\delta(\rho_x,\rho_y)
=2(\rho_y-\rho_x)
=(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma.
}
\]

The factor `2` is a global coordinate normalization; the intrinsic torsor displacement is `rho_y-rho_x`.

## 5. Uniqueness of the intrinsic displacement

Let `Delta:A x A -> V` be a candidate map that is required to return the actual translation taking the first affine point to the second:

\[
\boxed{x+\Delta(x,y)=y.}
\]

Because the translation action is free, this vector is unique. Therefore

\[
\boxed{
\Delta(x,y)=\delta(x,y)=y-x.
}
\]

Hence the state-difference relation is not one vector assignment among many once the physical relation is typed specifically as the intrinsic affine displacement of the quantum-point carrier.

The earlier theorem `RELATIONAL_STATE_DIFFERENCE_UNIQUENESS_V0_1.md` remains useful for a weaker starting point, where the relation map is not assumed a priori to be the torsor displacement and uniqueness is instead obtained from endpoint closure, affine compatibility and rotational covariance.

## 6. Symmetry covariance

For a common unitary frame change

\[
\rho\mapsto U\rho U^\dagger,
\]

the displacement transforms as

\[
\boxed{
\delta(U\rho_xU^\dagger,U\rho_yU^\dagger)
=U\,\delta(\rho_x,\rho_y)\,U^\dagger.
}
\]

Thus the torsor displacement is automatically `SU(2)`-covariant, and its coefficient-vector action factors through

\[
PSU(2)\cong SO(3).
\]

## 7. Metric and Pythagorean endpoint

On the normalized Pauli displacement

\[
\mathcal E_{xy}=2(\rho_y-\rho_x),
\]

use

\[
\langle A,B\rangle
=\frac12\operatorname{Tr}(AB).
\]

Then

\[
\boxed{
\|\mathcal E_{xy}\|^2
=|\mathbf r_y-\mathbf r_x|^2.
}
\]

Because torsor composition gives

\[
\mathcal E_{xz}=\mathcal E_{xy}+\mathcal E_{yz},
\]

orthogonal consecutive relations satisfy

\[
\boxed{
\|\mathcal E_{xz}\|^2
=\|\mathcal E_{xy}\|^2
+\|\mathcal E_{yz}\|^2.
}
\]

This is the local Pythagorean closure already registered in the subrepo.

## 8. TIR typing rule

The mathematical theorem is exact. The remaining TIR question is a typing question:

\[
\boxed{
\text{Does A3 type the primitive ordered relation between A2 quantum points as their intrinsic affine displacement?}
}
\]

A compact candidate inheritance rule is:

> A physical relation between two primitive quantum loci is represented by the origin-independent displacement that carries the first normalized quantum-point state to the second in the affine state hull.

Under that typing rule, the earlier `RELATION_AS_CANONICAL_QUANTUM_STATE_DIFFERENCE` gate closes by the standard torsor theorem rather than by an additional dynamical law.

A8 then acts as a consistency cross-check: local same-context endpoint composition is already exact for affine displacements, while nontrivial context/holonomy belongs to a lifted downstream closure sector.

A5 acts on the metric layer: arithmetic invariants such as `Tr(E^2)/2` measure the resulting relation geometry.

## 9. Shortest dependency line

\[
\boxed{
A2\;\text{quantum point}
\to
\mathcal A_2=\frac12I+\operatorname{Herm}_0(2)
\to
\text{affine torsor displacement}
\to
\mathcal E_{xy}\in\operatorname{Herm}_0(2)\cong\mathbb R^3
\to
\text{endpoint composition + metric}
\to
\Delta^3
\to
\text{Pythagoras}.
}
\]

The only TIR-specific bridge in this shortened route is the A3 relational typing of the physical ordered relation as the intrinsic affine displacement.

## 10. Claim classes

| Statement | Class |
|---|---|
| normalized Hermitian `2 x 2` states have affine hull `I/2 + Herm_0(2)` | EXACT |
| `Herm_0(2)` has real dimension three | EXACT |
| every ordered pair in an affine torsor has a unique displacement vector | EXACT AFFINE GEOMETRY |
| affine displacement obeys reversal and endpoint composition | EXACT |
| quantum-state displacement is `rho_y-rho_x` | EXACT |
| Pauli-normalized displacement is `2(rho_y-rho_x)` | EXACT CONVENTION |
| common `SU(2)` conjugation preserves the displacement law | EXACT |
| A3 identifies the primitive physical relation with intrinsic affine displacement | TIR FOUNDATIONAL TYPING GATE |
| under that typing, local relation carrier and Pythagorean closure follow | EXACT CONDITIONAL |
