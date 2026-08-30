# XF-2 — Naive Xi-Branch Hermite–Biehler Audit

Status: `NUMERICAL_COUNTEREXAMPLE_PASS / RAW_BRANCH_HB_CANDIDATE_FAIL / RIGOROUS_BOUND_CERTIFICATE_OPEN`

## 1. Target inherited from the operator programme

The de Branges route seeks an entire function \(E\) satisfying a decomposition of the form

\[
\Xi(z)=\frac12\left(E(z)+E^{\#}(z)\right),
\qquad
E^{\#}(z)=\overline{E(\overline z)},
\]

together with the Hermite–Biehler half-plane inequality

\[
|E(z)|>|E^{\#}(z)|,
\qquad \Im z>0.
\]

XF-1 supplies the canonical kernel branches

\[
A_+(z)=\int_0^\infty\Phi(u)e^{izu}\,du,
\qquad
A_-(z)=\int_0^\infty\Phi(u)e^{-izu}\,du,
\]

and reality of \(\Phi\) gives the entire-function relation

\[
\boxed{A_-(z)=A_+^{\#}(z).}
\]

Therefore the raw branch choice

\[
E_0(z):=2A_-(z),
\qquad
E_0^{\#}(z)=2A_+(z)
\]

has exactly the required symmetric reconstruction

\[
\boxed{
\Xi(z)=\frac12\left(E_0(z)+E_0^{\#}(z)\right).
}
\]

This makes \(E_0\) a canonical first candidate for the de Branges programme.

## 2. Hermite–Biehler margin

For the raw candidate define

\[
\Delta_{HB}(z)
:=
|A_-(z)|^2-|A_+(z)|^2.
\]

The desired upper-half-plane inequality for \(E_0=2A_-\) requires

\[
\Delta_{HB}(z)>0
\qquad
\text{for every }\Im z>0.
\]

## 3. Reproducible counterexample witness

Using the XF-1 runtime evaluator with

- 35 decimal digits working precision,
- 12 Riemann-kernel series terms,
- integration range \(0\le u\le4\),

at

\[
\boxed{z=17+0.1i}
\]

the branch moduli are

\[
|A_-(z)|\approx0.056731791396945661016,
\]

\[
|A_+(z)|\approx0.056754081729940098961,
\]

which gives

\[
\boxed{
\Delta_{HB}(17+0.1i)
\approx
-2.52963790216282018\times10^{-6}.
}
\]

The sign is opposite to the raw-candidate Hermite–Biehler requirement.

The repository pins this witness in `tests/test_xi_kernel.py`. The numerical separation from zero is more than an order of magnitude above the regression threshold used by the test.

## 4. Verdict

The direct identification

\[
E=2A_-
\]

is classified

\[
\boxed{\texttt{RAW\_BRANCH\_HB\_CANDIDATE = FAIL}.}
\]

The conjugate orientation \(E=2A_+\) exchanges the sign of the same margin and therefore cannot repair a globally sign-changing branch margin by a fixed orientation alone.

The useful result is the elimination of the simplest de Branges candidate while retaining the exact XF-1 identity

\[
\Xi=A_++A_-.
\]

## 5. Remaining constructive frontier

The next candidate must add independently motivated structure before the Hermite–Biehler gate. Admissible directions include:

1. a canonical nonvanishing multiplier \(M(z)\) with controlled \(M/M^{\#}\) modulus;
2. a differential or integral transform of the half-kernel branch;
3. a de Branges space generated from a canonical pair derived from \(\Phi\), rather than the raw one-sided transform itself;
4. a positivity kernel whose associated entire function has a provable half-plane modulus ordering.

Every candidate must preserve the exact reconstruction of \(\Xi\), expose its analytic domain, and pass a half-plane counterexample scan before theorem work is attempted.

## 6. Evidence status

- `A_- = A_+^#`: `EXACT`
- `Xi = A_+ + A_-`: `EXACT`
- `E0 = 2 A_-` symmetric Xi reconstruction: `EXACT`
- witness at `z=17+0.1i`: `NUMERICAL_PASS`
- raw-branch Hermite–Biehler candidate: `FAIL_NUMERICAL_COUNTEREXAMPLE`
- rigorous interval/error-bound certificate for the witness: `OPEN`
- transformed/corrected Hermite–Biehler candidate: `OPEN`
- Riemann hypothesis: `OPEN`
