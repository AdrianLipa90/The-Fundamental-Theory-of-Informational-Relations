# TIR Stella Distinction–Holonomy Bridge v0.1

Status: `EXACT_CONDITIONAL_STELLA_CLOSURE_BRIDGE_CANDIDATE`

Scope: TIR-internal bridge from the already-derived minimal tetrahedral Gram
class to (i) the Banach–Tarski free-rotation sector and (ii) the spinorial
half-turn/modulo sector. The theorem separates vertex relations, distinction
frames, spinorial lifts, and interpretation layers.

## 1. Upstream inputs

The minimal isotropic tetrahedral cell supplies four unit vectors

\[
\mathbf n_1,\ldots,\mathbf n_4\in\mathbb R^3
\]

with

\[
\sum_{i=1}^4\mathbf n_i=0,
\qquad
\mathbf n_i\cdot\mathbf n_j=-\frac13
\quad(i\ne j).
\]

An exact realization is

\[
\mathbf n_i=\frac{\mathbf v_i}{\sqrt3},
\]

with

\[
\mathbf v_1=(1,1,1),\quad
\mathbf v_2=(1,-1,-1),
\]

\[
\mathbf v_3=(-1,1,-1),\quad
\mathbf v_4=(-1,-1,1).
\]

The pure-qubit/Bloch orthocomplement is

\[
C:\mathbf n\mapsto-\mathbf n.
\]

Closing the tetrahedral frame under this orthocomplement gives

\[
\boxed{
\Sigma_{\rm stella}
=
T\cup(-T),
\qquad
T=\{\mathbf n_1,\ldots,\mathbf n_4\}.
}
\]

This is the eight-vertex stella-octangula/cube-vertex carrier.

The mathematics below is exact once this antipodal closure is included in the
scope. The stronger physical statement that every TIR tetrahedral use-case must
perform this closure is not asserted here.

## 2. Vertex relation spectrum

For stella vertices, the normalized dot products are exactly

\[
\mathbf n_i\cdot\mathbf n_i=1,
\]

\[
\mathbf n_i\cdot\mathbf n_j=-\frac13
\quad(i\ne j),
\]

\[
\mathbf n_i\cdot(-\mathbf n_i)=-1,
\]

\[
\mathbf n_i\cdot(-\mathbf n_j)=+\frac13
\quad(i\ne j).
\]

Thus the stella **vertex-pair** dot spectrum is

\[
\boxed{
\left\{-1,-\frac13,+\frac13,+1\right\}.
}
\]

There is no zero dot product among distinct stella vertices. Orthogonality
appears instead in the derived transport/distinction-frame sector below.

## 3. Common relational readout

For pure qubit projectors

\[
P_{\mathbf n}=\frac12(I+\mathbf n\cdot\boldsymbol\sigma),
\]

define

\[
\boxed{
R(\mathbf n,\mathbf m)
=
\operatorname{Tr}(P_{\mathbf n}P_{\mathbf m})
=
|\langle \mathbf n|\mathbf m\rangle|^2
=
\frac{1+\mathbf n\cdot\mathbf m}{2}.
}
\]

The stella vertex classes therefore give

\[
\boxed{
\begin{array}{ccl}
\mathbf n=\mathbf m &\Rightarrow& R=1,\\[1mm]
\text{same tetrahedron, distinct} &\Rightarrow& R=\frac13,\\[1mm]
\text{matched antipodes} &\Rightarrow& R=0,\\[1mm]
\text{cross-sector, unmatched} &\Rightarrow& R=\frac23.
\end{array}}
\]

If two **derived distinction frames** are orthogonal,

\[
\mathbf a\cdot\mathbf b=0,
\]

the same readout gives

\[
\boxed{R(\mathbf a,\mathbf b)=\frac12.}
\]

Hence \(1/3\) and \(1/2\) arise from the same projector-overlap principle but
from different geometric relation classes.

## 4. Banach–Tarski sector: cross-unmatched stella relations

For \(i\ne j\),

\[
\mathbf n_i\cdot(-\mathbf n_j)=\frac13,
\]

so the minimal rotation angle between the endpoints satisfies

\[
\boxed{\cos\theta=\frac13.}
\]

For a perfect matching
\(\{i,j,k,l\}=\{1,2,3,4\}\), define transport-axis numerators

\[
\mathbf a_{ij}=\mathbf n_i\times(-\mathbf n_j),
\qquad
\mathbf a_{kl}=\mathbf n_k\times(-\mathbf n_l).
\]

Then

\[
\begin{aligned}
\mathbf a_{ij}\cdot\mathbf a_{kl}
&=
(\mathbf n_i\cdot\mathbf n_k)
(\mathbf n_j\cdot\mathbf n_l)
-
(\mathbf n_i\cdot\mathbf n_l)
(\mathbf n_j\cdot\mathbf n_k)\\
&=
\frac19-\frac19\\
&=0.
\end{aligned}
\]

Thus every perfect matching supplies an orthogonal pair of rotation axes at the
same angle \(\arccos(1/3)\). The resulting free-rotation/Banach–Tarski reduction
is owned by `The-Book-of-Paradoxes`; this foundation records only the shared
geometry.

## 5. Four antipodal distinction axes

The matched antipodes define four unoriented axes

\[
\boxed{
\ell_i=\{\mathbf n_i,-\mathbf n_i\},
\qquad i=1,\ldots,4.
}
\]

Associate the Hermitian Pauli distinction generator

\[
\boxed{
\Sigma_i=\mathbf n_i\cdot\boldsymbol\sigma.
}
\]

Because \(|\mathbf n_i|=1\),

\[
\boxed{\Sigma_i^2=I.}
\]

For \(i\ne j\),

\[
\boxed{
\{\Sigma_i,\Sigma_j\}
=
2(\mathbf n_i\cdot\mathbf n_j)I
=
-\frac23I,
}
\]

while

\[
\boxed{
[\Sigma_i,\Sigma_j]
=
2i(\mathbf n_i\times\mathbf n_j)\cdot\boldsymbol\sigma
\ne0.
}
\]

Thus the tetrahedral distinction frames are intrinsically noncommuting.

## 6. Schrödinger × Heisenberg geometric packet

For each self-adjoint distinction generator \(\Sigma_i\), the standard
one-parameter unitary flow is

\[
\boxed{
U_i(\theta)
=
\exp\left(-\frac{i\theta}{2}\Sigma_i\right).
}
\]

This is the Schrödinger/unitary-generator branch on the same carrier on which
the multiple \(\Sigma_i\) furnish the Heisenberg/noncommuting-frame branch.

At the half-turn \(\theta=\pm\pi\),

\[
\boxed{
H_i^\pm
=
U_i(\pm\pi)
=
\mp i\Sigma_i.
}
\]

There are therefore

\[
\boxed{4\times2=8}
\]

oriented spinorial half-turn representatives.

The two signs represent the two \(SU(2)\) lifts/orientations of the same
\(SO(3)\) half-turn around the unoriented axis \(\ell_i\):

\[
H_i^-=-H_i^+.
\]

Every representative satisfies

\[
\boxed{
(H_i^\pm)^2=-I.
}
\]

The corresponding normalized angle class in

\[
\mathbb R/\mathbb Z
\]

is

\[
\boxed{
\left[\frac{\pm\pi}{2\pi}\right]
=
\left[\pm\frac12\right]
=
\left[\frac12\right].
}
\]

Hence

\[
\boxed{
\text{stella antipodal axes}
\longrightarrow
4\times2\,[1/2].
}
\]

This is a geometric/spinorial modulo statement, not a numerical fit.

## 7. Relation to the existing half seam

The primitive first-distinction theorem independently gives the exchange-fixed
probability coordinate

\[
\boxed{u=\frac12.}
\]

The stella half-turn packet gives independently the spinorial angle class

\[
\boxed{q=[1/2]\in\mathbb R/\mathbb Z.}
\]

These are distinct typed objects:

- \(u=1/2\): normalized binary share / probability base coordinate;
- \(q=[1/2]\): normalized half-turn / holonomy-angle class.

They may coexist in the same two-state lift without being identified.

On the half-seam phase fiber,

\[
|\psi(u,\varphi)\rangle
=
\sqrt{1-u}|N\rangle
+
e^{i\varphi}\sqrt u|S\rangle,
\]

the pair

\[
(u,q)=\left(\frac12,\left[\frac12\right]\right)
\]

corresponds to

\[
\varphi=2\pi q=\pi\pmod{2\pi},
\]

and therefore

\[
\boxed{
|\psi_\star\rangle
=
\frac{|N\rangle-|S\rangle}{\sqrt2}.
}
\]

The equal-weight result and the relative half-turn phase have separate
provenance.

## 8. IDT interface

`Informational-Dynamics-of-Time` already carries a mathematical phase
coordinate

\[
q\in\mathbb R/\mathbb Z
\]

and separately records projective \(2\pi\) closure and spinorial \(4\pi\)
closure.

The present theorem supplies a structurally compatible stella half-turn class

\[
[1/2]\in\mathbb R/\mathbb Z.
\]

The identification of this geometric class with the dynamical IDT temporal
phase is a **typed interface candidate**, not yet a derived physical coupling.

## 9. Claim classes

| Statement | Status |
|---|---|
| minimal isotropic four-frame has tetrahedral Gram | `SOURCE_DERIVED / EXACT_CONDITIONAL` |
| closure under Bloch orthocomplement produces stella octangula | `EXACT CONDITIONAL ON CLOSURE` |
| stella vertex dot spectrum is \(\{-1,-1/3,1/3,1\}\) | `EXACT` |
| pure-qubit readout \(R=(1+n\cdot m)/2\) | `EXACT` |
| stella vertex readouts are \(\{0,1/3,2/3,1\}\) | `EXACT` |
| orthogonal distinction frames give \(R=1/2\) | `EXACT` |
| perfect-matching transport axes are orthogonal | `EXACT` |
| \(\Sigma_i^2=I\) | `EXACT` |
| distinct tetrahedral \(\Sigma_i\) do not commute | `EXACT` |
| \(H_i^\pm=\mp i\Sigma_i\) | `EXACT` |
| there are eight oriented spinorial half-turn representatives | `EXACT` |
| \((H_i^\pm)^2=-I\) | `EXACT` |
| all eight normalized angle classes equal \([1/2]\in\mathbb R/\mathbb Z\) | `EXACT` |
| IDT temporal phase is physically identical to this class | `OPEN` |
| this bridge proves RH | `FAIL / NOT CLAIMED` |

## 10. Proof firewall

This theorem does **not**:

- promote antipodal completion into a universal physical law;
- identify the geometric modulo class with physical time without a coupling
  theorem;
- identify Bohmian mechanics or the Copenhagen interpretation with a single
  mathematical layer;
- prove a new xi functional equation;
- prove the Riemann Hypothesis.

Validator:

`TIR/validation/tir_stella_distinction_holonomy_v0_1.py`
