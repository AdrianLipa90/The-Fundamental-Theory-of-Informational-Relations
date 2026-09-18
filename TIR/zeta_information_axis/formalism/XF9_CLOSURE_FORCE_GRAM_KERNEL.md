# XF-9 — Closure-defect radial force and regularized de Branges Gram kernel

## Status ledger

- `EXACT`: closure-defect radial potential identity
- `EXACT`: radial-force / XF-8 differential-margin identity
- `STANDARD_EXTERNAL_THEOREM`: Lagarias/Hinkkanen logarithmic-derivative positivity criterion
- `EXACT_AWAY_FROM_ZEROS`: Pick-kernel representation of the normalized force
- `EXACT`: pole-free regularized Pick kernel
- `EXACT`: crosswalk to the differential de Branges kernel of XF-8
- `OPEN_RH_EQUIVALENT_CRITERION`: global positive radial force on the open critical half-strip
- `OPEN_OPERATOR_ROUTE`: positive-semidefinite full Gram kernel
- `RIEMANN_HYPOTHESIS`: OPEN

## 1. Coordinates and the PhaseNav square

Use the TIR coordinate

\[
\Xi(z)=\xi\!\left(\frac12+iz\right),
\qquad z=x+iy.
\]

The secret-of-a-half native closure defect is

\[
r=\left(\Re s-\frac12\right)^2.
\]

Set

\[
y=\sqrt r\ge0.
\]

Then

\[
\Xi(x+iy)
=
\xi\!\left(\frac12-y+ix\right).
\]

The functional equation and reality symmetry of \(\xi\) imply

\[
\boxed{
|\Xi(x+iy)|^2
=
\left|
\xi\!\left(\frac12+y+ix\right)
\right|^2.
}
\]

Thus the same non-negative scalar

\[
\boxed{r=y^2}
\]

is simultaneously:

1. the squared transverse displacement from the critical line;
2. the SOH native closure defect;
3. the radial variable of the Xi modulus surface.

Define the closure potential

\[
\boxed{
V_x(r):=
|\Xi(x+i\sqrt r)|^2.
}
\]

No RH assumption enters this identity.

## 2. Exact radial force

Define

\[
\boxed{
\mathcal F_x(r):=\partial_rV_x(r).
}
\]

For \(r>0\), put \(y=\sqrt r\) and \(z=x+iy\). Analyticity gives

\[
\partial_y|\Xi(z)|^2
=
2\,\Im\!\left(\Xi(z)\overline{\Xi'(z)}\right).
\]

Since \(\partial_r=(2y)^{-1}\partial_y\),

\[
\boxed{
\mathcal F_x(r)
=
\frac{
\Im\!\left(\Xi(z)\overline{\Xi'(z)}\right)
}{y}.
}
\]

At \(r=0\), the removable limit is

\[
\boxed{
\mathcal F_x(0)
=
|\Xi'(x)|^2-\Xi(x)\Xi''(x)
=
L_1[\Xi](x).
}
\]

Thus the first Laguerre quantity is the boundary stiffness of the closure
potential.

## 3. Exact XF-8 crosswalk

XF-8 defines

\[
E_D(z)=\Xi(z)+i\Xi'(z),
\qquad
E_D^\#(z)=\Xi(z)-i\Xi'(z),
\]

and the differential margin

\[
\Delta_D(z)
=
|E_D(z)|^2-|E_D^\#(z)|^2.
\]

XF-8 already proves

\[
\Delta_D(z)
=
4\,\Im\!\left(\Xi(z)\overline{\Xi'(z)}\right)
=
2\,\partial_y|\Xi(z)|^2.
\]

Therefore, for \(r>0\),

\[
\boxed{
\mathcal F_x(r)
=
\frac{\Delta_D(x+i\sqrt r)}{4\sqrt r}.
}
\]

This is an exact identification: the XF-8 Hermite--Biehler margin is the
closure-defect radial force multiplied by \(4\sqrt r\).

XF-8 also has

\[
\Delta_D(x+iy)=4\int_0^yQ_\Xi(x,v)\,dv,
\]

hence

\[
\boxed{
\mathcal F_x(r)
=
\frac1{\sqrt r}
\int_0^{\sqrt r}Q_\Xi(x,v)\,dv.
}
\]

The pointwise XF-5 curvature is therefore replaced by its exact radial average.

## 4. Lagarias/Hinkkanen criterion in the closure variable

On the right half of the critical strip write

\[
s=\frac12+y+ix,
\qquad y>0.
\]

By the modulus identity in Section 1,

\[
V_x(y^2)=|\xi(s)|^2.
\]

Differentiating directly in the right-half-plane coordinate gives, away from
zeros,

\[
\boxed{
\partial_r\log V_x(r)
=
\frac1{\sqrt r}
\Re\!\left[
\frac{\xi'}{\xi}
\left(\frac12+\sqrt r+ix\right)
\right].
}
\]

Lagarias records the classical equivalence

\[
\mathrm{RH}
\iff
\Re\!\left(\frac{\xi'}{\xi}(s)\right)>0
\quad
\text{for }\Re s>\frac12.
\]

Therefore the closure-coordinate form is

\[
\boxed{
\mathrm{RH}
\iff
\partial_r\log V_x(r)>0
\quad
\forall x\in\mathbb R,\ r>0,
}
\]

where the right side is interpreted on the zero-free domain supplied by the
criterion.

Because all non-trivial zeros lie in \(0<\Re s<1\), it is sufficient to
control the open half-strip

\[
0<r<\frac14.
\]

A pole-free equivalent strip formulation is

\[
\boxed{
\mathrm{RH}
\iff
\mathcal F_x(r)>0
\quad
\forall x\in\mathbb R,\ 0<r<\frac14.
}
\]

Indeed, under RH the Lagarias criterion and \(V_x(r)>0\) give positive force.
Conversely, an off-critical zero would give an interior zero of the
non-negative differentiable function \(V_x(r)\), where its radial derivative
cannot be strictly positive.

This is an RH-equivalent reformulation, not a proof of the missing sign.

## 5. Normalized Pick kernel and its pole problem

Define away from Xi zeros

\[
m_\Xi(z):=-\frac{\Xi'(z)}{\Xi(z)}.
\]

Its Pick kernel is

\[
P_m(z,w)
=
\frac{
m_\Xi(z)-\overline{m_\Xi(w)}
}{
z-\bar w
}.
\]

On the diagonal \(z=x+iy\), \(y>0\),

\[
\boxed{
P_m(z,z)
=
\frac{\Im m_\Xi(z)}{y}
=
\partial_r\log V_x(r).
}
\]

Thus the normalized closure force is the diagonal Pick density.

However \(m_\Xi\) has poles at Xi zeros. Any proof route that attempts to
propagate monotonicity through \(m_\Xi\) must explicitly handle these poles;
they cannot be ignored.

## 6. Pole-free regularized Pick kernel

Multiply the Pick kernel by the natural Xi congruence factor. Define

\[
\boxed{
\mathscr K_\Xi(z,w)
:=
\frac{
\Xi(z)\overline{\Xi'(w)}
-\Xi'(z)\overline{\Xi(w)}
}{
z-\bar w
}.
}
\]

Away from zeros,

\[
\boxed{
\mathscr K_\Xi(z,w)
=
\Xi(z)\overline{\Xi(w)}\,P_m(z,w).
}
\]

Unlike \(P_m\), this expression is pole-free. Its apparent diagonal
singularity is removable.

On the diagonal,

\[
\boxed{
\mathscr K_\Xi(z,z)
=
\frac{
\Im(\Xi(z)\overline{\Xi'(z)})
}{\Im z}
=
\mathcal F_x((\Im z)^2).
}
\]

Thus the exact closure force is the diagonal of a regularized two-point
kernel rather than an isolated scalar.

## 7. Exact de Branges crosswalk

Using the XF-8 differential pair

\[
E_D=\Xi+i\Xi',
\qquad
E_D^\#=\Xi-i\Xi',
\]

take the standard de Branges kernel convention

\[
K_{E_D}(z,w)
=
\frac{
E_D(z)\overline{E_D(w)}
-
E_D^\#(z)\overline{E_D^\#(w)}
}{
2\pi i(\bar w-z)
}.
\]

Direct expansion gives

\[
E_D(z)\overline{E_D(w)}
-
E_D^\#(z)\overline{E_D^\#(w)}
=
-2i
\left[
\Xi(z)\overline{\Xi'(w)}
-
\Xi'(z)\overline{\Xi(w)}
\right].
\]

Therefore

\[
\boxed{
\mathscr K_\Xi(z,w)
=
\pi K_{E_D}(z,w).
}
\]

XF-8 previously exposed the diagonal margin. XF-9 promotes the exact
two-point kernel identity as the corresponding Gram/Loewner interface.

The algebraic identity is `EXACT`. Global positive-semidefiniteness of the
full kernel is not promoted here; it remains an operator-level research route.

## 8. Relation to the square quotient

SOH-G001 has

\[
\xi\!\left(\frac12+z\right)=F(z^2).
\]

Hence

\[
\boxed{
\frac{\xi'}{\xi}
\left(\frac12+z\right)
=
2z\frac{F'(z^2)}{F(z^2)}.
}
\]

If RH holds, the zeros of \(F\) are real negative, and the logarithmic
derivative has a Stieltjes resolvent representation. SOH-G025 records this
as the quotient-plane dual-Hankel/S-fraction route.

Thus XF-9 and SOH-G025 are two coordinate representations of the same
operator geometry:

```text
SOH square quotient w=z^2
        |
        | F'/F  (Stieltjes / dual Hankel / S-fraction)
        v
regularized quotient Gram kernels
        ||
        || coordinate crosswalk
        v
Xi Pick kernel -> regularization -> de Branges kernel
        |
        v
diagonal = closure radial force = XF-8 margin/(4 sqrt(r))
```

## 9. Executable regression surface

`src/critical_axis/closure_force_gram.py` implements:

- \(V_x(r)\);
- the exact radial force and the \(r=0\) Laguerre limit;
- direct differentiation as a regression diagnostic;
- the normalized Lagarias force;
- the XF-8 differential branches and margin;
- the pole-free regularized Pick kernel;
- the standard de Branges kernel under the convention above;
- the exact \(\mathscr K_\Xi=\pi K_{E_D}\) crosswalk.

`tests/test_closure_force_gram.py` checks these identities numerically at
declared finite points. Such tests validate implementation identities only;
finite sign sampling is not a proof of RH.

## 10. Proof targets

The shortest scalar target is

\[
\boxed{
\mathcal F_x(r)>0
\quad
(x\in\mathbb R,\ 0<r<1/4).
}
\]

Equivalent existing forms are:

\[
\Re\frac{\xi'}{\xi}\left(\frac12+\sqrt r+ix\right)>0,
\]

and

\[
\Delta_D(x+i\sqrt r)>0.
\]

The new operator-level sufficient route is to establish an appropriate
positive-semidefinite Gram property for \(\mathscr K_\Xi\) (equivalently the
corresponding de Branges kernel) without assuming real-zero localization.

No such global positivity theorem is claimed here.

## 11. PRIOR_ART_AND_INDEPENDENT_REDISCOVERY

This section is normative provenance. Overlap with prior or concurrent
literature is credited explicitly. INDEPENDENT_REDISCOVERY means that the
project re-derived a structure before the targeted literature cross-check;
it does **not** assert historical priority.

### 11.1 PRIOR_ART

- **Lagarias (1999; correction 2005):** the classical positivity criterion
  for the logarithmic derivative of the Riemann Xi function and its
  Pick/Nevanlinna interpretation. XF-9's normalized scalar force is a
  closure-coordinate rewriting of this established criterion.
- **de Branges (1968):** reproducing-kernel/Hermite--Biehler theory underlying
  the de Branges kernel used in the XF-8/XF-9 crosswalk.
- **Denisov--Yattselev (2026):** Loewner kernels for Nevanlinna--Pick
  functions, sign-regularity, Gram total positivity, and links to
  Pólya-frequency series. This is direct prior/concurrent art for the
  operator-level Pick/Loewner -> Gram -> determinant pathway.
- **Covei (2026):** independent formalization of the pole obstruction for
  naive pointwise logarithmic-derivative concavity and a spectral-averaging
  regularization. This supports XF-9's insistence on a pole-free formulation.
- **Planat--Solé (2026):** second-level concavity of the first Laguerre
  expression for the Riemann Xi kernel and the associated double-Turán
  inequalities. Their result is external prior/concurrent art for the
  higher-curvature part of the later boundary-certificate route.
- **Csordas, Dimitrov--Xu, Wang--Yang, Sokal/Sokal--Walrad:** positive-definite
  kernels, Wronskians/Laguerre inequalities, complete monotonicity, Stieltjes
  moments, and continued fractions used elsewhere in the same crosswalk.
- **Michałowski (2026):** coefficient Toeplitz-minor tail positivity and a
  certified PF_5 failure for the continuous de Bruijn--Newman kernel. The
  latter is a provenance firewall: coefficient total positivity and
  continuous-kernel total positivity must not be conflated.

### 11.2 INDEPENDENT_REDISCOVERY

Before the targeted 18 September 2026 preprint spider, the project had already
re-derived the following structures:

1. the diagonal normalized force as a Pick-kernel density;
2. the pole obstruction in \(-\Xi'/\Xi\);
3. pole removal by congruence with the underlying entire function;
4. the promotion from a diagonal scalar margin to a two-point Gram kernel;
5. the equivalence between quotient-plane Stieltjes/Hankel kernels and the
   Xi-plane regularized kernel under the square-coordinate crosswalk.

After the literature cross-check, items 1--4 are treated as independent
rediscoveries of mechanisms with substantial prior/concurrent art. The
literature receives theorem-level credit wherever it supplies the same
implication. XF-9 keeps only the exact project-specific coordinate identities
as its own contribution.

### 11.3 PROJECT-SPECIFIC CROSSWALKS

As of the search dated 18 September 2026, the following are retained as
project-specific crosswalks, not historical-priority claims:

- the identification of
  \[
  r=(\Re s-\tfrac12)^2
  \]
  simultaneously as SOH closure defect, squared transverse displacement, and
  the radial variable of the Xi modulus surface;
- the exact identity
  \[
  \mathcal F_x(r)=\frac{\Delta_D(x+i\sqrt r)}{4\sqrt r}
  \]
  joining the SOH closure coordinate to the pre-existing XF-8 differential
  Hermite--Biehler margin;
- the pole-free kernel identity
  \[
  \mathscr K_\Xi(z,w)=\pi K_{E_D}(z,w),
  \]
  under the explicit XF-8 convention used in this repository;
- the coordinate diagram joining the SOH square quotient \(F(z^2)\), its
  Stieltjes dual-Hankel/S-fraction representation, and the Xi/de Branges
  two-point kernel.

If an equivalent pre-existing formula is later located, this section must be
updated immediately and the relevant credit transferred. Provenance is
maintained as a revisable research ledger rather than an ownership assertion.

## References

- J. C. Lagarias, *On a positivity property of the Riemann xi-function*,
  Acta Arith. **89** (1999), 217--234. The paper records
  \(\Re(\xi'/\xi)>0\) for \(\Re s>1\) and the RH-equivalent extension to
  \(\Re s>1/2\).
- J. C. Lagarias, *Correction to: On a positivity property of the Riemann
  xi-function*, Acta Arith. **116** (2005), 293--294.
- G. Csordas, *Fourier transforms of positive definite kernels and the
  Riemann xi-Function*, arXiv:1309.0055.
- D. K. Dimitrov and Y. Xu, *Wronskians of Fourier and Laplace transforms*,
  arXiv:1606.05011.
