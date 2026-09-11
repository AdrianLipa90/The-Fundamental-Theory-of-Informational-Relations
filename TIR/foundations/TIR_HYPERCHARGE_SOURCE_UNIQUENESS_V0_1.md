# TIR Hypercharge Relative-Uniqueness and Normalization Closure v0.1

Status: `EXACT_RELATIVE_UNIQUENESS / TIR_NORMALIZATION_ANCHORED / NO_NU_R_FIELD_CONTENT`

Date: 2026-09-10

## Scope and field convention

Work with the one-generation chiral field content already used by the v12 anomaly audit:

- left-handed quark doublet `Q_L`,
- right-handed singlets `u_R`, `d_R`,
- left-handed lepton doublet `L_L`,
- right-handed charged-lepton singlet `e_R`,
- one Higgs doublet `H`.

No right-handed neutrino is included in this theorem. Adding a gauged `nu_R` changes the uniqueness problem and requires a separately typed extension gate.

Write the U(1) charges as

\[
(q,u,d,\ell,e,h)
=(Y_Q,Y_{uR},Y_{dR},Y_L,Y_{eR},Y_H).
\]

The anomaly convention matches v12: right-handed fermions enter anomaly sums through their left-handed charge conjugates, hence with the displayed minus signs.

## 1. Yukawa gauge-invariance relations

Gauge invariance of the ordinary one-Higgs Yukawa operators gives

\[
u=q+h,\qquad d=q-h,\qquad e=\ell-h.
\]

These relations imply the mixed colour anomaly identically:

\[
2q-u-d=0.
\]

## 2. SU(2)^2 U(1) anomaly

The one-generation coefficient is

\[
\mathcal A_{22Y}=N_c q+\ell.
\]

Cancellation forces

\[
\boxed{\ell=-N_c q}.
\]

Thus `Y_L` is not an independent external parent once `Y_Q` and the displayed field content are admitted.

## 3. Gravitational-U(1) anomaly

Using the Yukawa identities, the coloured contribution vanishes:

\[
N_c(2q-u-d)=0.
\]

The remaining coefficient is

\[
2\ell-e=\ell+h.
\]

Hence gravitational anomaly cancellation forces

\[
\boxed{h=N_c q}.
\]

Substitution into the Yukawa relations gives the unique relative charge vector

\[
\boxed{
(q,u,d,\ell,e,h)
=q\,(1,N_c+1,1-N_c,-N_c,-2N_c,N_c).
}
\]

For the v12 value `N_c=3`,

\[
(q,u,d,\ell,e,h)=q(1,4,-2,-3,-6,3).
\]

## 4. Cubic anomaly is then automatic

With `ell=-N_c q` and `h=N_c q`,

\[
N_c\left(2q^3-u^3-d^3\right)
=-6N_c^3 q^3,
\]
while

\[
2\ell^3-e^3=+6N_c^3 q^3.
\]

Therefore

\[
\boxed{\mathcal A_{YYY}=0}
\]

identically. The local anomaly system has no additional relative-charge branch under the declared field/Yukawa assumptions.

## 5. TIR normalization anchor

The active TIR discrete-label surface gives

\[
L_4=2,\qquad N_c=3,
\]

and the typed quark-prime map gives `q_s=7=L_3`. The legacy TIR normalization expression

\[
Y_Q=\frac{q_s}{L_3L_4N_c}
\]

therefore reduces exactly to

\[
\boxed{Y_Q=\frac{1}{L_4N_c}=\frac16}.
\]

This is the TIR normalization anchor. Anomaly cancellation alone fixes only ratios; it cannot fix an overall U(1) normalization.

With `q=1/6`, the unique vector becomes

\[
\boxed{
Y_Q=\frac16,
\quad Y_{uR}=\frac23,
\quad Y_{dR}=-\frac13,
\quad Y_L=-\frac12,
\quad Y_{eR}=-1,
\quad Y_H=\frac12.
}
\]

The previously external v12 value `Y_L=-1/2` is therefore derived from the TIR-normalized `Y_Q` plus the `SU(2)^2U(1)` anomaly constraint.

## 6. Epistemic boundary

This theorem establishes uniqueness **within the declared one-generation field content, one-Higgs Yukawa structure, anomaly convention, and TIR overall-normalization anchor**. It does not prove that the Standard Model field content or the TIR normalization formula is uniquely forced by geometry alone.

If a right-handed neutrino is added, or if additional anomaly-free U(1) currents are admitted, the theorem must be re-run with the enlarged field content; no uniqueness claim is exported automatically.

## Result

```text
HYPERCHARGE_RELATIVE_UNIQUENESS = CLOSED_EXACT_ON_DECLARED_FIELD_CONTENT
Y_L_EXTERNAL_PARENT = ELIMINATED
Y_H = Nc * Y_Q = DERIVED
CUBIC_ANOMALY = AUTOMATIC_AFTER_LINEAR_CONSTRAINTS
TIR_NORMALIZED_VECTOR = (1/6,2/3,-1/3,-1/2,-1,1/2)
RIGHT_HANDED_NEUTRINO_EXTENSION = NOT_IN_THIS_THEOREM
GEOMETRIC_UNIQUENESS_OF_TIR_NORMALIZATION_ANCHOR = SEPARATE_QUESTION
```
