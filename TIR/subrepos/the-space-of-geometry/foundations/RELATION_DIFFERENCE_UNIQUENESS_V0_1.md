# Relation-Difference Uniqueness v0.1

Status: `EXACT_CONDITIONAL_RELATION_DIFFERENCE_UNIQUENESS_THEOREM_CANDIDATE`

Scope: sharpen the remaining `RELATION_AS_CANONICAL_QUANTUM_STATE_DIFFERENCE` gate. The goal is to determine whether the difference law can be selected uniquely from local relational requirements rather than inserted as a definition.

## 1. State-affine carrier

For the admitted binary quantum point,

\[
\rho_x=\frac12(I+\mathbf r_x\cdot\boldsymbol\sigma),
\qquad |\mathbf r_x|\le1,
\]

and the normalized-state affine hull is

\[
\mathcal A_2=\frac12I+\operatorname{Herm}_0(2).
\]

Let

\[
V:=\operatorname{Herm}_0(2)\cong\mathbb R^3
\]

be its translation space.

We seek an oriented primitive relation map

\[
R:\mathcal A_2\times\mathcal A_2\to V.
\]

## 2. Structural requirements

Assume the relation obeys four local requirements.

### R1 — source closure

The relation contains no independent local degree of freedom beyond the two endpoint states. Thus it is a function only of the ordered pair `(rho_x,rho_y)`.

### R2 — translation invariance in the affine hull

For every admissible common affine shift `H in V`,

\[
R(\rho_x+H,\rho_y+H)=R(\rho_x,\rho_y)
\]

whenever both shifted points lie in the admitted affine domain.

Therefore the relation depends only on the state difference. There exists a map

\[
F:V\to V
\]

such that

\[
\boxed{R(\rho_x,\rho_y)=F(\rho_y-\rho_x).}
\]

### R3 — endpoint composition

For every admitted triple,

\[
\boxed{
R(\rho_x,\rho_z)
=R(\rho_x,\rho_y)+R(\rho_y,\rho_z).
}
\]

In difference variables this becomes the Cauchy additivity relation

\[
\boxed{F(A+B)=F(A)+F(B).}
\]

Assume continuity at the origin. Then `F` is real-linear.

### R4 — rotational covariance

For the common local quantum-frame action,

\[
\rho\mapsto U\rho U^\dagger,
\qquad U\in SU(2),
\]

require

\[
R(U\rho_xU^\dagger,U\rho_yU^\dagger)
=U R(\rho_x,\rho_y)U^\dagger.
\]

Hence

\[
F(UAU^\dagger)=UF(A)U^\dagger.
\]

So `F` is an intertwiner of the real irreducible adjoint `SO(3)` representation carried by `V`.

## 3. Uniqueness theorem

Because the defining real three-dimensional `SO(3)` representation is irreducible, every real-linear endomorphism commuting with all rotations is a scalar multiple of the identity. Therefore

\[
\boxed{F(A)=cA}
\]

for some real constant `c`.

Thus every continuous, compositional, affine-translation-invariant and rotationally covariant source-closed local relation has the form

\[
\boxed{
R(\rho_x,\rho_y)=c(\rho_y-\rho_x).
}
\]

Nondegenerate distinguishability requires

\[
c\ne0.
\]

Orientation convention fixes the sign. The remaining magnitude is one unit normalization.

## 4. Canonical Bloch normalization

Write

\[
\rho_y-\rho_x
=\frac12(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma.
\]

Choosing the generator coefficient vector to equal the Bloch-coordinate difference fixes

\[
\boxed{c=2.}
\]

Hence

\[
\boxed{
\mathcal E_{xy}
=2(\rho_y-\rho_x)
=(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma.
}
\]

The factor `2` is therefore a normalization choice after the structural uniqueness theorem; the direction and functional form of the relation are fixed before that normalization.

## 5. Immediate closure

The unique normalized relation satisfies

\[
\mathcal E_{yx}=-\mathcal E_{xy},
\]

\[
\mathcal E_{xz}=\mathcal E_{xy}+\mathcal E_{yz},
\]

and

\[
\mathcal E_{xy}+\mathcal E_{yz}+\mathcal E_{zx}=0.
\]

With

\[
\langle A,B\rangle=\frac12\operatorname{Tr}(AB),
\]

its norm is

\[
\boxed{
\|\mathcal E_{xy}\|^2
=|\mathbf r_y-\mathbf r_x|^2.
}
\]

Thus affine composition and the local Euclidean quadratic form arise on the same object.

## 6. TIR dependency crosswalk

The theorem hypotheses have a direct dependency interpretation:

\[
\begin{array}{rcl}
A1+A3 &\rightsquigarrow& \text{source closure},\\
A3 &\rightsquigarrow& \text{nondegenerate distinguishability},\\
A7 &\rightsquigarrow& \text{rotational covariance},\\
A8 &\rightsquigarrow& \text{endpoint composition / zero local relation defect},\\
A5 &\rightsquigarrow& \text{metric and unit normalization}.
\end{array}
\]

The mathematical uniqueness result itself is exact once R1--R4 and continuity are admitted.

The foundational frontier is therefore reduced from

`RELATION_AS_CANONICAL_QUANTUM_STATE_DIFFERENCE`

to the narrower rule bundle

\[
\boxed{
\texttt{SOURCE\_CLOSED + COMPOSITIONAL + COVARIANT PRIMITIVE RELATION}.
}
\]

If these properties are derived as the operational content of A1/A3/A7/A8, the difference relation follows uniquely up to scale, with A5/Bloch normalization fixing that scale.

## 7. Consequence for spatial promotion

Combining this theorem with `QUANTUM_POINT_AFFINE_SPATIAL_CARRIER_V0_1.md` gives

\[
\boxed{
\rho_x
\longrightarrow
\mathcal E_{xy}=2(\rho_y-\rho_x)
\in\operatorname{Herm}_0(2)
\cong\mathbb R^3.
}
\]

The representation-theoretic result `SPATIAL_PROMOTION_UNIQUENESS_V0_1.md` then becomes an independent uniqueness cross-check of the same three-dimensional carrier.

## 8. Claim classes

| Statement | Class |
|---|---|
| common affine-translation invariance makes the relation depend only on endpoint difference | EXACT CONDITIONAL |
| endpoint composition makes the difference map additive | EXACT |
| additive + continuous implies real-linear | STANDARD EXACT THEOREM |
| rotational covariance makes the linear map an `SO(3)` intertwiner | EXACT |
| every such endomorphism of the defining real `SO(3)` representation is `c I` | EXACT REPRESENTATION THEORY |
| `c=2` under Bloch-coordinate generator normalization | EXACT NORMALIZATION |
| A1/A3 imply source closure | TIR BRIDGE CANDIDATE |
| A8 selects endpoint composition for the primitive relation | TIR BRIDGE CANDIDATE |
| A7 selects covariance of the primitive relation | TIR BRIDGE CANDIDATE |
| admitting the bridge properties fixes the primitive relation to the state difference up to scale | EXACT CONDITIONAL |
