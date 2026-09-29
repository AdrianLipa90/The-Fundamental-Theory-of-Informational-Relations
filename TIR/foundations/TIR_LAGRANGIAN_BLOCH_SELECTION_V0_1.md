# TIR Lagrangian--Bloch Selection Theorem v0.1

Status: \`EXACT_MINIMAL_COHERENT_PROJECTIVE_GEOMETRY__TIR_SOURCE_RECONCILIATION\`

Scope: close the foundation seam between the primitive point/relational distinction, the independent \(U(1)\cong S^1\) phase core, the projective two-state carrier, the Bloch sphere, and the Fubini--Study Lagrangian geometry. This theorem introduces no empirical physical binding.

## 1. Primitive point and first nontrivial coherent relation

The minimum non-empty object carrier is a point \(P\). A nontrivial relation distinguishes two orientation roles

\[
\{N,S\}.
\]

Normalized relational shares are

\[
(1-u,u),
\qquad
0\le u\le1.
\]

The independent relational phase core supplies

\[
\varphi\in U(1)\cong S^1.
\]

The smallest coherent two-role extension carrying this population coordinate and relative phase is

\[
\boxed{
|\psi(u,\varphi)\rangle
=
\sqrt{1-u}\,|N\rangle
+
e^{i\varphi}\sqrt{u}\,|S\rangle.
}
\]

The endpoints are phase-independent:

\[
u=0\Rightarrow[\psi]=[N],
\qquad
u=1\Rightarrow[\psi]=[S].
\]

Hence the relative-phase circle collapses at the two endpoints.

## 2. Quotient geometry

The parameter space before endpoint identification is

\[
S^1\times[0,1].
\]

Collapsing the lower boundary circle to \(N\) and the upper boundary circle to \(S\) gives

\[
\boxed{
\left(S^1\times[0,1]\right)/
\left(
S^1\times\{0\}\sim N,\;
S^1\times\{1\}\sim S
\right)
\cong
\Sigma S^1
\cong
S^2.
}
\]

Thus the sphere follows from the phase fibre plus the two pole endpoints; no pre-existing \(SO(3)\) action is required.

Equivalently, the same coherent state is a normalized vector in \(\mathbb C^2\). Removing global phase gives the Hopf/projective quotient

\[
\boxed{
S^3/U(1)
=
\mathbb{CP}^1
\cong
S^2.
}
\]

The suspension and projective quotients are two descriptions of the same minimal two-state coherent geometry.

## 3. Explicit Bloch map

Define

\[
\mathbf r(u,\varphi)
=
\left(
2\sqrt{u(1-u)}\cos\varphi,\;
2\sqrt{u(1-u)}\sin\varphi,\;
1-2u
\right).
\]

Then

\[
|\mathbf r|^2
=
4u(1-u)+(1-2u)^2
=
1.
\]

Therefore

\[
\boxed{\mathbf r:[\psi]\mapsto S^2}
\]

is the standard Bloch realization. At \(u=1/2\),

\[
\boxed{
\mathbf r(1/2,\varphi)
=
(\cos\varphi,\sin\varphi,0),
}
\]

so the TIR half-seam fibre is exactly the Bloch equator.

## 4. Euler closure of the topology

Suspension obeys

\[
\chi(\Sigma X)=2-\chi(X).
\]

Because

\[
\chi(S^1)=0,
\]

we obtain

\[
\boxed{
\chi(S^2)=\chi(\Sigma S^1)=2.
}
\]

This is the topological Euler closure of the phase circle into the sphere.

It must not be confused with Euler's complex identity \(e^{i\pi}=-1\), which enters the Berry/spin closure after the projective geometry has been established.

## 5. Fubini--Study metric is the canonical projective metric

On normalized rays,

\[
ds_{\rm FS}^2
=
\langle d\psi|d\psi\rangle
-
|\langle\psi|d\psi\rangle|^2.
\]

Using

\[
u=\sin^2\frac{\theta}{2},
\]

the metric becomes

\[
\boxed{
ds_{\rm FS}^2
=
\frac14
\left(
d\theta^2+\sin^2\theta\,d\varphi^2
\right).
}
\]

For \(\mathbb{CP}^1\), the \(PU(2)\)-invariant Kähler metric is unique up to one positive overall scale. TIR fixes the standard Fubini--Study normalization above.

Thus the minimal coherent projective carrier does not admit an arbitrary angular metric once projective-unitary invariance and the standard normalization are imposed.

## 6. Lagrangian geometry

The existing TIR relational phase Lagrangian has the geometric kinetic term

\[
L_{\rm geom}
=
\frac12 g_{ab}(q)\dot q^a\dot q^b.
\]

On the minimal coherent projective carrier, the canonical projective choice is

\[
\boxed{
g_{ab}=g^{\rm FS}_{ab}
}
\]

up to the overall scale fixed by the chosen Fubini--Study normalization.

Hence the minimal projective Lagrangian geometry is

\[
\boxed{
(\mathbb{CP}^1,g_{\rm FS})
\cong
(S^2,g_{\rm round}/4).
}
\]

This is the precise TIR content of “the point/minimal carrier maps to Bloch geometry through the Lagrangian”: a primitive point carrying the first nontrivial coherent relation has the minimal normalized projective configuration space \(\mathbb{CP}^1\), and its invariant Kähler kinetic metric is Fubini--Study.

## 7. Berry curvature and next theorem

The Kähler/Berry curvature is

\[
\boxed{
F_B
=
\frac12\sin\theta\,d\theta\wedge d\varphi,
}
\]

with

\[
\boxed{
\frac1{2\pi}\int_{S^2}F_B=1.
}
\]

The next canonical theorem is the already-existing Euler--Berry spin gate:

\[
(\mathbb{CP}^1,g_{\rm FS},F_B)
+
e^{i\gamma_B}=-1
\Longrightarrow
\boxed{s_{\min}=\frac12}.
\]

That spin theorem remains separately sourced and preserves its original status \`FORMAL_SYMBOLIC_PASS\`.

## 8. Dependency result

The foundation seam is therefore

\[
\boxed{
P
\to
R
\to
\{N,S\},
\qquad
R
\to
U(1)\cong S^1,
}
\]

followed by

\[
\boxed{
\{N,S\}
+
U(1)\cong S^1
\to
\Sigma S^1
\cong
S^2
\cong
\mathbb{CP}^1
\to
g_{\rm FS}
\to
F_B
\to
s=\frac12.
}
\]

The scalar information branch

\[
\{N,S\}\to\frac12\to\ln2
\]

commutes with the same binary carrier.

## 9. Claim classes

| Statement | Class |
|---|---|
| \(S^1\) with the two boundary circles collapsed gives \(\Sigma S^1\cong S^2\) | STANDARD EXACT TOPOLOGY |
| normalized two-complex-state rays give \(\mathbb{CP}^1\cong S^2\) | STANDARD EXACT PROJECTIVE GEOMETRY |
| Bloch map has unit norm | EXACT |
| half-seam fibre is the equator | EXACT |
| \(\chi(\Sigma S^1)=2\) | STANDARD EXACT TOPOLOGY |
| Fubini--Study formula on \(\mathbb{CP}^1\) | STANDARD EXACT |
| \(PU(2)\)-invariant Kähler metric uniqueness up to scale on \(\mathbb{CP}^1\) | STANDARD GEOMETRIC RESULT |
| standard FS normalization fixes the scale used by TIR | CONVENTION / NORMALIZATION |
| TIR relational Lagrangian uses this minimal projective metric | SOURCE-RECONCILED TIR IDENTIFICATION |
| Euler--Berry sign selects minimal spin \(1/2\) | DOWNSTREAM FORMAL_SYMBOLIC_PASS |
| empirical universality of the carrier | NOT CLAIMED HERE |

Validator:

\`TIR/validation/tir_lagrangian_bloch_selection_v0_1.py\`.
