# TIR Coefficient Role and Orientation Forcing v0.1

Status: `EXACT_ROLE_AND_SIGN_FORCING_THEOREM_CANDIDATE`

Date: 2026-08-29

## 1. Source generator

The intrinsic coefficient state is

\[
\boxed{(h,a,b,c)\in\mathbb Z^4}
\]

with generator

\[
\boxed{
G(h,a,b,c)
=\frac h2+a\kappa+b\frac{\kappa}{L_3}+c\frac{\kappa^2}{2}.
}
\]

The four coefficient slots are structurally routed by the existing atomic canonization layer:

\[
\begin{aligned}
h&\leftarrow\text{projective half / spin identity},\\
a&\leftarrow\text{generation seed / Ramanujan release},\\
b&\leftarrow\text{Collatz terminal / return axis},\\
c&\leftarrow\text{Poincare--Berry curvature / holonomy}.
\end{aligned}
\]

## 2. Role-forcing theorem

### Theorem 1 — typed slot uniqueness

Let the source-role set be

\[
\mathcal R
=\{R_h,R_a,R_b,R_c\}
\]

with

\[
R_h=\text{projective-half-spin},
\quad
R_a=\text{generation-release},
\quad
R_b=\text{return-axis},
\quad
R_c=\text{curvature-holonomy}.
\]

Let the generator basis be

\[
\mathcal B
=\left\{
\frac12,
\kappa,
\frac{\kappa}{L_3},
\frac{\kappa^2}{2}
\right\}.
\]

Under the canonical role router, each role owns exactly one basis slot and each basis slot has exactly one source role. Hence the role-to-slot map is a bijection:

\[
\boxed{
R_h\leftrightarrow h,
\quad
R_a\leftrightarrow a,
\quad
R_b\leftrightarrow b,
\quad
R_c\leftrightarrow c.
}
\]

No permutation of the coefficient slots preserves the declared parent types unless it is the identity permutation.

### Proof

The four parent sets are pairwise typed by distinct invariants:

- the `h` parents contain the projective half and spin-half identity;
- the `a` parents contain twin-prime seed index, Ramanujan scaling and generation assignment;
- the `b` parents contain terminal Collatz/return orientation;
- the `c` parents contain tetrahedral depth, Poincare disk and Berry connection.

A slot permutation preserving all parent types must therefore fix each of the four role classes separately. Hence the only admissible role-preserving permutation is the identity.

## 3. Gradient-orientation theorem

The runtime source operator is

\[
s(\alpha_s,x)=\tanh(-\alpha_s x),
\qquad
x=\frac{\partial V}{\partial\phi},
\qquad
\alpha_s>0.
\]

### Theorem 2 — scale-independent gradient sign

For every finite `x` and every positive `alpha_s`,

\[
\boxed{
\operatorname{sgn}s(\alpha_s,x)
=
\operatorname{sgn}(-x).
}
\]

### Proof

For `alpha_s>0`, multiplication by `alpha_s` preserves sign. The function `tanh` is odd, strictly increasing and vanishes only at zero. Therefore the sign of `tanh(-alpha_s x)` equals the sign of `-x`, independently of the magnitude of `alpha_s`.

Thus the orientation class requires no fitted spin-amplitude parameter:

\[
\boxed{
\chi_{\nabla}
:=\operatorname{sgn}\!\left(-\frac{\partial V}{\partial\phi}\right)
\in\{-1,0,+1\}.
}
\]

## 4. Directed-orbit orientation theorem

The canonical orbital direction rule is

\[
\chi_O=
\begin{cases}
+1,&\text{attractor}\to\text{satellite},\\
-1,&\text{satellite}\to\text{attractor},\\
0,&\text{neutral}.
\end{cases}
\]

The chiral path supplies the independent orientation label

\[
\chi_H=
\begin{cases}
+1,&H_+,\\
-1,&H_-,\\
0,&\text{neutral}.
\end{cases}
\]

## 5. Consensus forcing theorem

### Theorem 3 — unique admissible sign under source agreement

For an atomic/orbital state define the nonzero source-sign set

\[
S=\{\chi_\nabla,\chi_O,\chi_H\}\setminus\{0\}.
\]

If

\[
S\ne\varnothing
\qquad\text{and}\qquad
|S|=1
\]

as a set of sign values, then there is a unique orientation compatible with all active source operators:

\[
\boxed{
\chi_{\rm TIR}=\chi_\nabla=\chi_O=\chi_H
}
\]

for every nonzero participating source.

### Proof

Each active source independently maps the same pre-coefficient state to an element of `{-1,+1}`. If all active values agree, any opposite assignment violates every nonzero source returning the common sign. Therefore exactly one sign is admissible.

If active source signs disagree, the state is routed to the conflict surface rather than silently assigned a coefficient sign.

## 6. Slot application

Because Theorem 1 fixes which source class owns each coefficient slot, Theorems 2--3 can be applied without coefficient permutation ambiguity.

The resulting forcing architecture is

\[
\boxed{
\text{pre-coefficient state}
\to
\begin{cases}
R_h\to h,\\
R_a\to a,\\
R_b\to b,\\
R_c\to c,
\end{cases}
\qquad
(\chi_\nabla,\chi_O,\chi_H)
\to\chi_{\rm TIR}.
}
\]

Thus **slot identity and orientation/sign are framework-forced whenever the declared source operators are mutually consistent.**

## 7. Magnitude layer

After role and sign forcing, the remaining coefficient information is magnitude:

\[
|h|,|a|,|b|,|c|.
\]

The source ownership already identifies where each magnitude must come from:

\[
\boxed{
\begin{aligned}
|h|&\leftarrow\text{projective/spin closure count},\\
|a|&\leftarrow\text{generation seed/release count},\\
|b|&\leftarrow\text{Collatz return invariant},\\
|c|&\leftarrow\text{curvature/holonomy invariant}.
\end{aligned}}
\]

This converts the previous undifferentiated coefficient-binding question into four typed integer-invariant extraction problems. No cross-slot coefficient search is required.

## 8. Circularity firewall

The parent data admitted to the forcing map exclude:

- observed particle masses;
- observed Yukawa couplings;
- an already recovered coefficient tuple;
- a PhaseNav envelope generated from that tuple;
- residual-to-target information.

The theorem therefore acts on coefficient-free geometry and routing state.

## 9. Promotion status

The exact results established by this candidate are:

```text
slot_role_bijection = EXACT
only_role_preserving_slot_permutation = identity
gradient_sign_independent_of_positive_alpha_s = EXACT
consensus_orientation_unique_when_sources_agree = EXACT
coefficient_search_over_slot_permutations = ELIMINATED
```

The next extraction is the magnitude theorem for the four typed source invariants.