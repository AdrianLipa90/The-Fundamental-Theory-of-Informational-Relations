# TIR Relative Phase-Rate Ratio v0.1

Status: `EXACT_CONDITIONAL_RELATIVE_RATE_THEOREM_CANDIDATE`

Scope: TIR-only continuation of the half-fiber rate no-go theorem. The absolute rate scale remains free. This gate asks whether a dimensionless ratio of phase rates can nevertheless be fixed before importing physical time.

## 1. Common relational cycle

Let two admitted `U(1)` phase fibers carry phase coordinates

\[
\varphi_i,\qquad \varphi_j.
\]

Let `C` be one common oriented relational cycle on which both fibers close. A5–A6 encode their phase closures by winding integers

\[
\boxed{
\oint_C d\varphi_i=2\pi m_i,
\qquad
\oint_C d\varphi_j=2\pi m_j,
\qquad
m_i,m_j\in\mathbb Z.
}
\]

For nonzero denominator winding `m_j != 0`, define the closure ratio

\[
\boxed{
R_{ij}[C]
:=
\frac{\oint_C d\varphi_i}{\oint_C d\varphi_j}
=
\frac{m_i}{m_j}.
}
\]

The ratio is dimensionless and depends only on the two winding classes evaluated on the same relational cycle.

## 2. Reparameterization invariance

Let the same cycle be parameterized by any strictly increasing parameter `lambda`,

\[
\omega_i^{(\lambda)}=\frac{d\varphi_i}{d\lambda},
\qquad
\omega_j^{(\lambda)}=\frac{d\varphi_j}{d\lambda}.
\]

Then

\[
\oint_C d\varphi_i
=\int_C \omega_i^{(\lambda)}d\lambda,
\qquad
\oint_C d\varphi_j
=\int_C \omega_j^{(\lambda)}d\lambda.
\]

Under a positive reparameterization

\[
\lambda'=f(\lambda),
\qquad
\frac{d\lambda'}{d\lambda}>0,
\]

both rates transform with the same inverse Jacobian,

\[
\omega_a^{(\lambda')}
=
\omega_a^{(\lambda)}\frac{d\lambda}{d\lambda'},
\qquad a\in\{i,j\},
\]

so the integrated closure ratio is unchanged.

Therefore

\[
\boxed{R_{ij}[C]=m_i/m_j}
\]

requires no absolute time coordinate.

## 3. Average phase-rate ratio

For any common parameter interval of size

\[
\Delta\lambda_C=\int_C d\lambda>0,
\]

define the cycle-averaged rates

\[
\bar\omega_i^{(\lambda)}
:=\frac{1}{\Delta\lambda_C}\oint_Cd\varphi_i,
\qquad
\bar\omega_j^{(\lambda)}
:=\frac{1}{\Delta\lambda_C}\oint_Cd\varphi_j.
\]

Then exactly

\[
\boxed{
\frac{\bar\omega_i^{(\lambda)}}{\bar\omega_j^{(\lambda)}}
=
\frac{m_i}{m_j}.
}
\]

The common interval cancels. Hence the winding arithmetic fixes a dimensionless average relative-rate ratio while leaving the common absolute scale undetermined.

## 4. Instantaneous ratio firewall

The winding data alone do not fix the pointwise ratio

\[
\frac{d\varphi_i/d\lambda}{d\varphi_j/d\lambda}.
\]

Two phase paths can have the same endpoint windings while redistributing their local phase velocity differently along the cycle. A pointwise ratio becomes fixed only after an additional synchronization/locking law is declared.

Thus the exact pre-temporal statement is the common-cycle integrated/average ratio,

\[
\boxed{
\text{common closure arithmetic}
\Rightarrow
\text{dimensionless average relative phase-rate ratio},
}
\]

while the absolute rate and local rate profile remain separate downstream inputs.

## 5. Relation to A4–A7

The theorem uses the following TIR roles:

- A4 supplies the admitted isotropic spherical/Bloch geometric carrier when the quantum half-fiber is realized geometrically;
- A5 maps closed geometric phase transport to arithmetic winding data;
- A6 identifies the integer closure indices as natural-number phase-closure labels;
- A7 supplies symmetry of the parent relational law and permits comparison of equivalent phase fibers without selecting an absolute external clock.

The exact ratio theorem itself follows from the common-cycle closure equations and does not require an absolute temporal normalization.

## 6. Information-rate ratio

TIR already has

\[
d\mathcal I_a=\kappa d\varphi_a,
\qquad
\Gamma_{\mathcal I,a}^{(\lambda)}
=\kappa\omega_a^{(\lambda)}.
\]

For a common `kappa`, the same cycle gives

\[
\boxed{
\frac{\overline{\Gamma}_{\mathcal I,i}}
{\overline{\Gamma}_{\mathcal I,j}}
=
\frac{m_i}{m_j}.
}
\]

Thus phase-winding arithmetic also fixes the corresponding average relative information-rate ratio before a physical clock scale is introduced.

## 7. Crosslink to Informational Dynamics of Time

TIR exports the typed packet

```text
phase_fibers              = U(1)_i, U(1)_j
common_relational_cycle   = C
winding_i                 = m_i
winding_j                 = m_j
relative_phase_rate_ratio = m_i / m_j
relative_info_rate_ratio  = m_i / m_j
absolute_rate_scale       = FREE
local_rate_profile        = OPEN unless synchronization law supplied
```

IDT may subsequently use its activity-derived intrinsic measure

\[
d\Theta=\mathfrak a\,d\lambda
\]

to convert the free group-rate coordinate into the intrinsic temporal phase rate

\[
\boxed{
\Omega_\Theta:=\frac{d\varphi}{d\Theta}
=\frac{1}{\mathfrak a}\frac{d\varphi}{d\lambda}.
}
\]

For two fibers evaluated against the same local temporal measure,

\[
\frac{\Omega_{\Theta,i}}{\Omega_{\Theta,j}}
=
\frac{d\varphi_i}{d\varphi_j}
\]

where the pointwise ratio is admitted only when the required synchronization law is supplied; on a common closed cycle the average ratio remains `m_i/m_j` exactly.

## 8. Theorem statement

### Theorem — common-cycle relative phase-rate quantization

Let two TIR `U(1)` phase fibers close on the same oriented relational cycle `C` with nonzero winding indices `m_i,m_j`. Then the dimensionless ratio of their accumulated phases and their average rates over that common cycle is

\[
\boxed{
R_{ij}[C]=\frac{m_i}{m_j}\in\mathbb Q.
}
\]

This ratio is invariant under every common positive reparameterization of the cycle. The theorem fixes no absolute rate scale.

## 9. Next gate

The next question is whether an existing TIR relation supplies a natural synchronization/locking law that promotes the common-cycle average ratio to a local ratio along the orbit while preserving the absolute-rate no-go theorem.
