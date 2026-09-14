# TIR Coefficient Transition Selector — Composition No-Go v0.3

Status: `EXACT_BINARY_SELECTOR_FALSIFICATION / PARITY_ONLY_LOCAL_COCYCLE_NO_GO / ADDITIVE_SELECTOR_REQUIREMENT / Q_PHASE_ORIENTATION_CANDIDATE / SELECTOR_REMAINS_OPEN`

Date: 2026-09-14

Scope: exact internal audit of transition-selector composition on the active Stage-22 charged-lepton seed basis. No particle mass, Yukawa coupling, fitted coefficient, residual-to-target input, or physical-time binding is used.

## 1. Active seed-center chain and release vectors

Stage 22 fixes the active ordered seed basis

\[
s_1=(3,5),\qquad s_2=(5,7),\qquad s_3=(11,13),
\]

with integer centers

\[
m_1=4,\qquad m_2=6,\qquad m_3=12.
\]

The exact center reachability theorem gives

\[
12\to6\to3\to10\to5\to16\to8\to4,
\]

hence the composable reverse-generation corridors

\[
\gamma_{21}:6\to4,
\qquad
\gamma_{32}:12\to6,
\qquad
\gamma_{31}=\gamma_{32}\circ\gamma_{21}:12\to4.
\]

The existing coefficient generator records the signed adjacent release vectors

\[
\boxed{R_{e\mu}=(0,5,2,8)},
\]

\[
\boxed{R_{\mu\tau}=(0,3,-1,-7)}.
\]

Its exact lattice identity defines the composed release

\[
\boxed{
R_{e\tau}=R_{e\mu}+R_{\mu\tau}=(0,8,1,1).
}
\]

This is integer-vector addition inside the already-declared generator lattice; it is not a new physical fit.

## 2. Binary odd-corridor magnitude candidate

The canonical finite TIR counts are

\[
N_F=3,
\qquad
L_3=7,
\qquad
L_4=2,
\qquad
L_5=5,
\qquad
I=1.
\]

For the two adjacent reverse corridors,

\[
\gamma_{21}:6,3,10,5,16,8\to4
\]

contains the odd pre-hit states `3,5`, while

\[
\gamma_{32}:12\to6
\]

contains no odd pre-hit state.

Define the coefficient-free binary corridor flag

\[
\delta_{\rm odd}(\gamma)
=
\begin{cases}
1,&\gamma\text{ contains at least one odd pre-hit state},\\
0,&\text{otherwise}.
\end{cases}
\]

A natural retrospective reconstruction of the two known magnitude packets is

\[
M_{\delta}(\gamma)
=
\bigl(0,
N_F+\delta L_4,
I+\delta I,
L_3+\delta I\bigr).
\]

Then

\[
M_{\delta}(\gamma_{21})=(0,5,2,8)=|R_{e\mu}|,
\]

and

\[
M_{\delta}(\gamma_{32})=(0,3,1,7)=|R_{\mu\tau}|.
\]

Thus the binary rule reproduces the two adjacent historical magnitude vectors without reading masses or Yukawas.

## 3. Exact composition falsification

The composed corridor is

\[
\gamma_{31}:12\to6\to3\to10\to5\to16\to8\to4.
\]

It contains the same odd pre-hit set `3,5`, hence

\[
\delta_{\rm odd}(\gamma_{31})=1.
\]

Therefore the binary magnitude rule predicts

\[
M_{\delta}(\gamma_{31})=(0,5,2,8).
\]

But exact generator composition gives

\[
|R_{e\tau}|=(0,8,1,1).
\]

Hence

\[
\boxed{
M_{\delta}(\gamma_{31})\ne |R_{e\tau}|.
}
\]

So the rule

\[
(N_F,I,L_3)+\delta_{\rm odd}(L_4,I,I)
\]

is **falsified as a universal transition-parent magnitude selector** on the active three-seed system. Its exact reproduction of the two adjacent packets is retained only as a local retrospective structural coincidence/candidate.

This result does not imply that odd-corridor information is irrelevant. It proves that one binary odd/non-odd bit is insufficient to define a composition-compatible global selector.

## 4. Necessary additive-cocycle condition

Let a signed transition selector on reverse center corridors be

\[
\Omega:\gamma_{ji}\mapsto R_{ij}\in\mathbb Z^4.
\]

If it is compatible with the existing generator addition law, then every composable pair must satisfy

\[
\boxed{
\Omega(\gamma_{31})
=
\Omega(\gamma_{32})+\Omega(\gamma_{21}).
}
\]

Thus a surviving universal selector must behave as a vector-valued additive path cocycle on the active transition graph, or provide an equivalent construction whose output obeys this composition law.

Composition compatibility is necessary, not sufficient: it constrains the missing selector but does not derive it.

## 5. Parity-only local step cocycle no-go

A stronger local simplification also fails.

Assume that every Collatz step contributes one fixed integer vector according only to the parity of its source state:

\[
\omega(n\to Cn)
=
\begin{cases}
E,&n\text{ even},\\
O,&n\text{ odd},
\end{cases}
\qquad E,O\in\mathbb Z^4,
\]

and corridor release is the sum of step contributions.

The corridor `12 -> 6` is one even step, so exact matching to the second adjacent release forces

\[
E=R_{\mu\tau}=(0,3,-1,-7).
\]

The parity word of `6 -> 4` is

\[
010100,
\]

containing four even and two odd source states. Therefore exact matching to the first adjacent release would require

\[
4E+2O=R_{e\mu}=(0,5,2,8).
\]

Solving gives

\[
2O=R_{e\mu}-4R_{\mu\tau}=(0,-7,6,36),
\]

hence

\[
\boxed{O=(0,-7/2,3,18)}.
\]

The linear component is not an integer, contradicting the declared coefficient lattice

\[
(h,a,b,c)\in\mathbb Z^4.
\]

Therefore

\[
\boxed{
\text{no parity-only constant local step cocycle }(E,O)\in\mathbb Z^4
\text{ reproduces both adjacent release vectors}.
}
\]

A surviving local construction must depend on more than the single parity bit — for example on state value, seed/path position, projective phase, holonomy, or another independently derived transition-sensitive invariant.

## 6. Exact IDT phase-difference structure

The canonical IDT parity-phase values on the active centers are

\[
q_C(4)=\frac17,
\qquad
q_C(6)=\frac{141}{448},
\qquad
q_C(12)=\frac{141}{896}.
\]

Using the canonical lifted rational representatives, the generation-direction differences are

\[
\boxed{
q_C(6)-q_C(4)=\frac{11}{64}>0,
}
\]

\[
\boxed{
q_C(12)-q_C(6)=-\frac{141}{896}<0,
}
\]

and

\[
\boxed{
q_C(12)-q_C(4)=\frac{13}{896}>0.
}
\]

They obey exact additivity:

\[
\boxed{
q_C(12)-q_C(4)
=
\bigl(q_C(6)-q_C(4)\bigr)
+
\bigl(q_C(12)-q_C(6)\bigr).
}
\]

The signs coincide with the signed return-axis and curvature components of the three release vectors:

\[
\operatorname{sgn}(b,c)_{e\mu}=(+,+),
\]

\[
\operatorname{sgn}(b,c)_{\mu\tau}=(-,-),
\]

\[
\operatorname{sgn}(b,c)_{e\tau}=(+,+).
\]

Thus

\[
\chi_q(i\to j)
:=
\operatorname{sgn}\bigl(q_C(m_j)-q_C(m_i)\bigr)
\]

is an exact coefficient-free additive-phase **orientation candidate** consistent with all three active release vectors.

However, no theorem currently identifies `chi_q` with the TIR gradient/orbit/chiral sign source or with physical release orientation. Therefore

\[
\boxed{\chi_q\to\operatorname{sgn}(b,c)\text{ binding remains OPEN}.}
\]

The result is a structural compatibility statement, not a promotion of the coefficient selector.

## 7. Selector frontier after this theorem

Closed here:

```text
binary_odd_corridor_magnitude_selector_universal = FALSE
binary_odd_corridor_rule_matches_two_adjacent_packets = TRUE_RETROSPECTIVE
composition_additivity_required_for_universal_signed_selector = TRUE
parity_only_constant_step_cocycle_in_Z4 = IMPOSSIBLE
qC_lifted_phase_difference_additive_on_active_chain = EXACT
qC_difference_sign_matches_b_c_signs_on_e_mu_mu_tau_e_tau = EXACT_STRUCTURAL_CORRELATION
```

Still open:

```text
COEFFICIENT_TRANSITION_PARENT_SELECTOR = OPEN
state_sensitive_vector_cocycle_derivation = OPEN
qC_phase_to_TIR_orientation_binding = OPEN
physical_mass_or_Yukawa_binding = OPEN
```

## 8. Reproducibility

Deterministic validator:

`TIR/validation/tir_coefficient_selector_composition_nogo_v0_3.py`

The validator independently computes all three active Collatz corridors, parity words, odd-state flags, exact rational IDT phases, the composed release vector, failure of the binary magnitude rule, impossibility of an integer parity-only step cocycle, and the phase-sign compatibility statements.