# The Space of Geometry — Research Spine v0.3

Status: `TIR_SPACE_OF_GEOMETRY_AFFINE_QUANTUM_POINT_SPINE_CANDIDATE`

## 1. Shortest current derivation line

The current preferred local route is

\[
\boxed{
0
\to P
\to \text{FIRST DISTINCTION}
\to \mathbb C^2
\to \rho_x
\to \operatorname{Aff}(\mathcal D_2)
\to \operatorname{Herm}_0(2)
\to \mathbb R^3
\to \Delta^3
\to \text{metric / angle / orthogonality}
\to a^2+b^2=c^2.
}
\]

Here

\[
\operatorname{Aff}(\mathcal D_2)
=\frac12I+\operatorname{Herm}_0(2)
\]

is the three-real-dimensional affine hull of normalized binary quantum states.

## 2. Quantum point relation

For primitive point states

\[
\rho_x=\frac12(I+\mathbf r_x\cdot\boldsymbol\sigma),
\]

define the local relation generator

\[
\boxed{
\mathcal E_{xy}=2(\rho_y-\rho_x)
=(\mathbf r_y-\mathbf r_x)\cdot\boldsymbol\sigma.
}
\]

Then, exactly,

\[
\mathcal E_{yx}=-\mathcal E_{xy},
\]

\[
\boxed{
\mathcal E_{xz}=\mathcal E_{xy}+\mathcal E_{yz},
}
\]

and

\[
\mathcal E_{xy}+\mathcal E_{yz}+\mathcal E_{zx}=0.
\]

The local affine composition law is therefore already present in the canonical state-difference relation.

## 3. Dimension and metric

Because

\[
\dim_{\mathbb R}\operatorname{Herm}(2)=4
\]

and normalized states obey one real trace constraint,

\[
\boxed{
\dim_{\mathbb R}\operatorname{Aff}(\mathcal D_2)=3.
}
\]

The translation space is

\[
\operatorname{Herm}_0(2)
=\operatorname{span}_{\mathbb R}\{\sigma_x,\sigma_y,\sigma_z\}.
\]

With

\[
\langle A,B\rangle=\frac12\operatorname{Tr}(AB),
\]

we have

\[
\boxed{
\|\mathcal E_{xy}\|^2
=|\mathbf r_y-\mathbf r_x|^2.
}
\]

Thus the same object supplies dimensionality, displacement addition and Euclidean quadratic measure.

## 4. Tetrahedral minimum

A three-dimensional affine carrier requires four affinely independent points for its minimal full-dimensional simplex:

\[
\boxed{\Delta^3.}
\]

Under equal norm and full isotropy,

\[
\sum_{a=1}^{4}\mathbf n_a=0,
\qquad
\mathbf n_a\cdot\mathbf n_b=-\frac13\quad(a\ne b),
\]

so the minimal cell is the regular tetrahedron.

The same four pure-state directions are the tetrahedral qubit SIC frame. Under the affine quantum-point relation bridge, the informational and local geometric tetrahedra occupy the same affine carrier.

## 5. Pythagorean closure

For two consecutive local relations

\[
A=\mathcal E_{xy},
\qquad
B=\mathcal E_{yz},
\]

endpoint composition gives

\[
\mathcal E_{xz}=A+B.
\]

Hence

\[
\|\mathcal E_{xz}\|^2
=\|A\|^2+\|B\|^2+2\langle A,B\rangle.
\]

For

\[
\langle A,B\rangle=0,
\]

we obtain

\[
\boxed{
\|\mathcal E_{xz}\|^2
=\|\mathcal E_{xy}\|^2+\|\mathcal E_{yz}\|^2,
}
\]

or

\[
\boxed{a^2+b^2=c^2.}
\]

## 6. Remaining foundational gate

The previous v0.2 route required the physical local carrier to be declared a minimal faithful orthogonal realization of `SO(3)`.

The affine quantum-point route reduces the active bridge to one more primitive statement:

\[
\boxed{
\texttt{RELATION\_AS\_CANONICAL\_QUANTUM\_STATE\_DIFFERENCE}.
}
\]

Operationally:

> for two primitive quantum loci, their local physical relation is carried by the canonical affine difference of their normalized binary quantum states.

Once this rule is admitted or derived from A1--A3, the three-dimensional carrier, additive endpoint law and invariant local metric follow together.

The minimal-faithful `SO(3)` theorem remains valuable as an independent uniqueness cross-check of the resulting three-dimensional carrier.

## 7. Dependency classes

```text
A1: primitive point
  |
A2: binary quantum point state rho_x
  |
A3 bridge: relation = canonical information-state difference
  |
E_xy = 2(rho_y-rho_x) in Herm_0(2)
  |-----------------------------|
  v                             v
real dimension 3          exact endpoint addition
  |                             |
  +-----------> HS metric <-----+
                    |
                    v
                 Delta^3
                    |
                    v
              regular tetrahedron
                    |
                    v
          angle / orthogonality
                    |
                    v
              PYTHAGORAS
```

## 8. Downstream boundary

Global manifold refinement, curvature, nontrivial holonomy and the TIR x Time spacetime join remain downstream. The endpoint of this subrepo is the local Euclidean closure above.
