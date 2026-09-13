# XF-8B — Cayley–Schur / de Branges–Pick gate

Status: `EXACT_CAYLEY_IDENTITY / EXACT_PICK_KERNEL_IDENTITY / RH_EQUIVALENT_SCHUR_GATE / RIEMANN_HYPOTHESIS_OPEN`

Parent routes: XF-8 differential Hermite–Biehler bridge, XF-8A tilted-autocorrelation / Bochner reduction.

## 1. Purpose

XF-8 established the canonical differential pair

\[
E_D(z)=\Xi(z)+i\Xi'(z),
\qquad
E_D^{\#}(z)=\Xi(z)-i\Xi'(z),
\]

with exact zero boundary phase

\[
\Xi(z_0)=0
\Longrightarrow
\frac{E_D^{\#}(z_0)}{E_D(z_0)}=-1=e^{i\pi}
\]

at every simple zero. The remaining localization gate is the strict upper-half-plane modulus ordering

\[
|E_D^{\#}(z)|<|E_D(z)|,
\qquad \Im z>0.
\]

XF-8B rewrites this gate as a standard Cayley/Schur condition and exposes the associated Pick/de Branges kernel. This does not prove the missing sign. It converts the surviving scalar positivity problem into a canonical analytic-function and reproducing-kernel statement.

## 2. Canonical Weyl logarithmic derivative

Away from Xi zeros define

\[
\boxed{
m_\Xi(z):=-\frac{\Xi'(z)}{\Xi(z)}.}
\]

Then

\[
E_D(z)=\Xi(z)\bigl(1-i m_\Xi(z)\bigr),
\]

\[
E_D^{\#}(z)=\Xi(z)\bigl(1+i m_\Xi(z)\bigr).
\]

Therefore the differential branch quotient is exactly

\[
\boxed{
\Theta_D(z)
:=\frac{E_D^{\#}(z)}{E_D(z)}
=
\frac{1+i m_\Xi(z)}{1-i m_\Xi(z)}.
}
\]

This is a Cayley transform of the Weyl/logarithmic-derivative variable.

Write

\[
m_\Xi(z)=a+ib.
\]

Then

\[
|1-i m_\Xi|^2=(1+b)^2+a^2,
\]

\[
|1+i m_\Xi|^2=(1-b)^2+a^2.
\]

Hence, wherever Xi is nonzero,

\[
\boxed{
\operatorname{Im}m_\Xi(z)>0
\iff
|\Theta_D(z)|<1
\iff
|E_D(z)|>|E_D^{\#}(z)|.
}
\]

This is the exact Cayley equivalence.

## 3. Margin identity

The XF-8 margin satisfies

\[
\Delta_D(z)
:=|E_D(z)|^2-|E_D^{\#}(z)|^2.
\]

Substituting the Cayley factorization gives

\[
\boxed{
\Delta_D(z)
=4|\Xi(z)|^2\operatorname{Im}m_\Xi(z).
}
\]

Thus the three surviving formulations are identical away from zeros:

\[
\boxed{
\Delta_D>0
\iff
\operatorname{Im}m_\Xi>0
\iff
|\Theta_D|<1.
}
\]

At a simple Xi zero the logarithmic derivative has a pole but the differential quotient has the finite boundary value

\[
\boxed{
\Theta_D(z_0)=-1=e^{i\pi}.
}
\]

So the Euler antiphase is the distinguished unit-circle boundary value of the Cayley variable.

## 4. Schur formulation

Let

\[
\mathbb C_+:=\{z:\operatorname{Im}z>0\}.
\]

If the strict differential margin is positive throughout \(\mathbb C_+\), then \(E_D\) cannot vanish there and

\[
\Theta_D:\mathbb C_+\to\mathbb D
\]

is analytic with

\[
|\Theta_D(z)|<1.
\]

Conversely, if \(\Theta_D\) is analytic and Schur on \(\mathbb C_+\), then

\[
|E_D^{\#}|<|E_D|
\]

and no Xi zero can occur in \(\mathbb C_+\), because every simple zero requires the unit-modulus value \(-1\). Schwarz symmetry then excludes the lower half-plane as well.

For the Riemann Xi function this is an RH-equivalent reformulation:

\[
\boxed{
\mathrm{RH}
\iff
\Theta_D\text{ is Schur on }\mathbb C_+
}
\]

with the usual understanding that the quotient is continued only where its denominator is nonzero; strict Hermite–Biehler ordering supplies that zero-free denominator automatically.

Because the nontrivial zeta zeros are already confined to the critical strip, the actual exclusion problem only needs the image strip

\[
0<\operatorname{Im}z<\frac12.
\]

No RH promotion is made here.

## 5. Pick kernel

For an analytic Schur function on \(\mathbb C_+\), the standard Pick kernel is

\[
\boxed{
P_\Theta(z,w)
=
\frac{1-\Theta_D(z)\overline{\Theta_D(w)}}
{-i(z-\overline w)}.
}
\]

The Schur property is equivalent to positive semidefiniteness of this kernel on every finite set of upper-half-plane points.

Multiplying by the nonvanishing factors \(E_D(z)\overline{E_D(w)}\) yields the congruent de Branges-type kernel

\[
\boxed{
K_D(z,w)
=
\frac{
E_D(z)\overline{E_D(w)}
-
E_D^{\#}(z)\overline{E_D^{\#}(w)}
}{-i(z-\overline w)}.
}
\]

Up to a positive conventional normalization constant, this is the canonical de Branges kernel associated with the pair \((E_D,E_D^{\#})\).

## 6. Exact divided-Wronskian form

Because Xi is real entire,

\[
\overline{\Xi(w)}=\Xi(\overline w),
\qquad
\overline{\Xi'(w)}=\Xi'(\overline w).
\]

Direct expansion gives

\[
E_D(z)\overline{E_D(w)}
-
E_D^{\#}(z)\overline{E_D^{\#}(w)}
=
2i\Bigl[
\Xi'(z)\Xi(\overline w)
-
\Xi(z)\Xi'(\overline w)
\Bigr].
\]

Hence

\[
\boxed{
K_D(z,w)
=
2\,
\frac{
\Xi'(z)\Xi(\overline w)
-
\Xi(z)\Xi'(\overline w)
}{\overline w-z}.
}
\]

This is an exact two-point divided-Wronskian representation.

On the diagonal \(w=z=x+iy\), \(y>0\),

\[
-i(z-\overline z)=2y,
\]

so

\[
\boxed{
K_D(z,z)
=
\frac{\Delta_D(z)}{2y}.
}
\]

Thus the scalar XF-8 gate is exactly the diagonal of the Pick/de Branges kernel.

For the normalized Pick kernel,

\[
\boxed{
P_\Theta(z,z)
=
\frac{1-|\Theta_D(z)|^2}{2y}
=
\frac{\Delta_D(z)}{2y|E_D(z)|^2}.
}
\]

## 7. Boundary / horizon interpretation

In the Xi coordinate

\[
z=x+iy,
\]

the critical line is the boundary

\[
y=0,
\]

while the open critical strip off the line maps to

\[
0<|y|<\frac12.
\]

The exact differential zero condition gives

\[
\Theta_D(z_0)=-1,
\]

a point on the unit-circle boundary of the Schur disk. Therefore the precise analytic version of the horizon picture is:

\[
\boxed{
0<y<\frac12
\Longrightarrow
\Theta_D(z)\in\mathbb D
}
\]

and every zero attempts to hit the boundary point

\[
\boxed{-1=e^{i\pi}.}
\]

If the Schur/Pick gate is proved, such a boundary hit is impossible in the open strip and can occur only on the geometric boundary \(y=0\).

This interpretation is exact only after the Schur gate is supplied. The geometric language by itself is not a proof of that gate.

## 8. Relation to the nonlocal positivity obstruction

Recent theta-kernel work shows that the Xi growth derivative has a genuinely nonlocal cancellation structure: phase-aligned blockwise positivity and independent domination of separated oscillatory sectors cannot recover the global sign. XF-8A already encountered the same phenomenon internally: individual positive-mixture slices can have negative Fourier transform while the integrated kernel remains the correct object.

XF-8B therefore deliberately keeps the complete analytic quotient and its Pick kernel intact. The admissible next target is not positivity of local blocks but a global positive-kernel representation for \(K_D\) or \(P_\Theta\).

External provenance relevant to this boundary:

- J. C. Lagarias, *On a positivity property of the Riemann xi-function*, Acta Arith. 89 (1999): positivity of the logarithmic derivative is RH-equivalent.
- D. K. Dimitrov and Y. Xu, *Wronskians of Fourier and Laplace Transforms*: correlation-kernel / Wronskian positive-definiteness framework and an RH-equivalent density criterion.
- M. Planat, *A Theta-Kernel Reformulation of Riemann-Xi Growth and the Obstruction to Blockwise Positivity*, Symmetry 18 (2026), 1283: peer-reviewed global-growth reformulation and blockwise obstruction.
- M. Planat, *Nonlocal Cancellation in a Theta-Kernel Decomposition of the Riemann Xi-Growth Derivative* (2026 preprint): all-algebraic-order cancellation of separated sectors; tracked as `EXTERNAL_PREPRINT_RESULT`.

## 9. Promotion ledger

- `M_XI = -XI_PRIME / XI`: `EXACT_AWAY_FROM_ZEROS`
- `THETA_D = (1+i M_XI)/(1-i M_XI)`: `EXACT_AWAY_FROM_ZEROS`
- `IM(M_XI)>0 <-> |THETA_D|<1`: `EXACT`
- `DELTA_D = 4 |XI|^2 IM(M_XI)`: `EXACT_AWAY_FROM_ZEROS`
- `SIMPLE_ZERO -> THETA_D=-1=EXP(i*pi)`: `EXACT`
- `PICK_KERNEL_FORMULA`: `STANDARD + EXACT_SUBSTITUTION`
- `DE_BRANGES_DIVIDED_WRONSKIAN_FORM`: `EXACT`
- `K_D(z,z)=DELTA_D/(2 Im z)`: `EXACT`
- `THETA_D_SCHUR_ON_UPPER_HALF_PLANE`: `OPEN / RH_EQUIVALENT`
- `PICK_KERNEL_GLOBAL_PSD`: `OPEN / RH_EQUIVALENT`
- `RIEMANN_HYPOTHESIS`: `OPEN`

## 10. Next proof target

Seek an independently positive Gram/operator representation

\[
K_D(z,w)=\langle v_w,v_z\rangle_{\mathcal H}
\]

for all \(z,w\in\mathbb C_+\), derived from the Xi/theta kernel without assuming real Xi zeros.

Such a representation would imply positive semidefiniteness of every Pick matrix and therefore the Schur/Hermite–Biehler gate. Until that global Gram representation (or an equivalent theorem) is proved, RH remains OPEN.
