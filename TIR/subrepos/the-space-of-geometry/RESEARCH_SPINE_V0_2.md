# The Space of Geometry — Research Spine v0.2

Status: `TIR_SPACE_OF_GEOMETRY_SPINE_CANDIDATE_V0_2`

This version narrows the paper to the shortest local derivation ending at Pythagoras and separates global continuum construction into a downstream programme.

## 1. Imported primitive line

\[
0\prec P\prec\{N,S\}\prec\frac12\prec\ln2\prec\mathbb C^2.
\]

The binary quantum carrier supplies

\[
\mathfrak g_{\rm rel}
=\operatorname{Herm}_0(2)
\cong\mathbb R^3
\]

with

\[
\boxed{
\langle A,B\rangle
=\frac12\operatorname{Tr}(AB).
}
\]

## 2. Promotion theorem in minimal form

Instead of declaring

\[
T_x\Sigma=\operatorname{Herm}_0(2),
\]

the subrepo now uses the conditional uniqueness theorem:

> A minimal nonzero finite-dimensional real carrier that faithfully and orthogonally realizes the full primitive `PSU(2) ~= SO(3)` symmetry has real dimension three and is equivalent, up to orthogonal frame change, to the defining `SO(3)` representation.

Because `Herm_0(2)` already realizes this representation through the `SU(2)` adjoint action,

\[
\boxed{
V_x\simeq\operatorname{Herm}_0(2)\simeq\mathbb R^3
}
\]

under the declared spatial-realization criterion.

The invariant positive metric is unique up to a positive scale.

The active promotion gate is now:

\[
\boxed{
\text{derive the minimal faithful real orthogonal realization criterion from the primitive TIR axioms.}
}
\]

## 3. Minimal spatial geometry

For a three-dimensional affine carrier the minimal full-dimensional simplex has four affinely independent vertices:

\[
\boxed{
\dim V_x=3
\Longrightarrow
\Delta^3.
}
\]

With equal norm and full local isotropy,

\[
\sum_{a=1}^{4}n_a=0,
\]

\[
\sum_{a=1}^{4}n_an_a^T=\frac43I_3,
\]

and therefore

\[
\boxed{
n_a\cdot n_b=-\frac13\quad(a\ne b).
}
\]

Thus the minimal isotropic full-dimensional cell is the regular tetrahedron.

## 4. Informational convergence as a cross-check

A generic qubit has three independent real Bloch coordinates. A normalized `m`-outcome probability vector supplies at most `m-1` independent values, so informational completeness requires

\[
m\ge4.
\]

The minimal symmetric qubit IC/SIC construction is tetrahedral.

This remains an independent convergence route. The local Euclidean/Pythagorean derivation uses the spatial carrier theorem directly; informational completeness is a cross-check rather than an additional premise.

## 5. Local displacement geometry

For

\[
A=A^a\sigma_a,
\]

define

\[
\boxed{
\|A\|^2
=\frac12\operatorname{Tr}(A^2)
=\delta_{ab}A^aA^b.
}
\]

For consecutive displacements in one local frame,

\[
C=A+B.
\]

The transported form is

\[
\mathcal E_{xz}
=
\mathcal E_{xy}
+
\operatorname{Ad}(U_{xy})\mathcal E_{yz}.
\]

## 6. Angle and orthogonality

\[
\boxed{
\cos\theta
=\frac{\langle A,B\rangle}{\|A\|\|B\|}
}
\]

and

\[
\boxed{
A\perp B
\iff
\langle A,B\rangle=0.
}
\]

The Pauli generator metric therefore supplies Euclidean angles directly on the promoted local carrier.

## 7. Pythagorean closure

Bilinearity gives

\[
\|A+B\|^2
=\|A\|^2+\|B\|^2+2\langle A,B\rangle.
\]

For orthogonal `A,B`,

\[
\boxed{
\|A+B\|^2
=\|A\|^2+\|B\|^2.
}
\]

With

\[
a=\|A\|,\qquad b=\|B\|,\qquad c=\|A+B\|,
\]

we obtain

\[
\boxed{a^2+b^2=c^2.}
\]

This is the endpoint of the paper.

## 8. Global-gluing separation theorem

For a regular tetrahedron,

\[
\theta_T=\arccos(1/3)
\]

and

\[
\boxed{5\theta_T<2\pi<6\theta_T.}
\]

Hence congruent regular tetrahedra cannot exactly fill a flat neighborhood around an edge by face-to-face gluing.

Therefore the regular tetrahedron is treated as the minimal local isotropic cell. Global flat or curved continuum construction belongs to a separate refinement problem and is not required for the local Pythagorean endpoint.

## 9. Revised dependency chain

```text
FIRST DISTINCTION
      |
      v
C^2
      |
      v
Herm_0(2)
      |
      +--> real dimension 3
      +--> Hilbert-Schmidt inner product
      +--> Ad SU(2) = SO(3) rotational carrier
      |
      v
MINIMAL FAITHFUL SPATIAL REALIZATION CRITERION
      |
      v
local V_x ~= R^3
      |
      v
minimal simplex Delta^3
      |
      v
regular tetrahedral local isotropy
      |
      v
local norm + additive displacement
      |
      v
angle / orthogonality
      |
      v
PYTHAGOREAN CLOSURE
```

## 10. Remaining core gate

The central proof task has been reduced to one physical derivation:

\[
\boxed{
\text{Why must local physical relational directions realize the full primitive rotational symmetry faithfully, orthogonally and minimally?}
}
\]

Once this criterion is derived from the primitive TIR axioms, the remainder of the paper to Pythagoras is theorem-driven.

The informational tetrahedron/spatial tetrahedron identification and global refinement remain valuable downstream crosslinks, but they are no longer prerequisites for the paper endpoint.
