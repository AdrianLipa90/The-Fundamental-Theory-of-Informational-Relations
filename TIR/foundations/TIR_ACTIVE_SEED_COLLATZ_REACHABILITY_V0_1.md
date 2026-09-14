# TIR Active-Seed Collatz Reachability v0.1

Status: `EXACT_CENTER_PROJECTION_REACHABILITY / LABEL_CYCLE_NOT_DERIVED / SELECTOR_REMAINS_OPEN`

Date: 2026-09-14

Scope: compare the active Stage-22 ordered TIR seed labels and the Stage-24 cyclic label operator with the ordinary full Collatz map on the integer center projection of those twin-prime seeds. This is a mathematical source audit only. No particle-mass, Yukawa, transition-rate, or physical-time claim is made.

## 1. Active ordered seed basis

Stage 22 fixes

\[
\boxed{s_1=(3,5),\qquad s_2=(5,7),\qquad s_3=(11,13).}
\]

For the integer center projection

\[
m(p,p+2)=p+1,
\]

the active centers are

\[
\boxed{m_1=4,\qquad m_2=6,\qquad m_3=12.}
\]

Stage 24 independently defines the cyclic label operator

\[
P_s|s_1\rangle=|s_2\rangle,
\qquad
P_s|s_2\rangle=|s_3\rangle,
\qquad
P_s|s_3\rangle=|s_1\rangle,
\]

while explicitly leaving a dynamical derivation of that cycle from Collatz/Poincare seed evolution as a separate gate.

## 2. Ordinary full Collatz map on the center projection

Use

\[
C(n)=
\begin{cases}
n/2,& n\equiv0\pmod2,\\
3n+1,& n\equiv1\pmod2.
\end{cases}
\]

The active center trajectories begin

\[
4\to2\to1\to4\to\cdots,
\]

\[
6\to3\to10\to5\to16\to8\to4\to2\to1\to\cdots,
\]

\[
12\to6\to3\to10\to5\to16\to8\to4\to2\to1\to\cdots.
\]

Hence

\[
\boxed{C(12)=6}
\]

and

\[
\boxed{C^6(6)=4,\qquad C^7(12)=4.}
\]

Define the first-hitting distance

\[
d_C(x,y)=\min\{k\ge0:C^k(x)=y\}
\]

when the set is nonempty. Then

\[
\boxed{d_C(12,6)=1,\qquad d_C(6,4)=6,\qquad d_C(12,4)=7.}
\]

Thus the center projection carries the exact directed reachability chain

\[
\boxed{m_3\longrightarrow m_2\longrightarrow m_1.}
\]

The reverse upward hits do not occur: the orbit of 4 is the terminal `4-2-1` cycle and never contains 6 or 12; the displayed finite orbit of 6 reaches the terminal cycle without containing 12.

## 3. Stage-24 label cycle is not the raw center Collatz operator

The Stage-24 label cycle requires the three directed label edges

\[
s_1\to s_2,
\qquad
s_2\to s_3,
\qquad
s_3\to s_1.
\]

Under the center projection these would require

\[
4\to6,
\qquad
6\to12,
\qquad
12\to4.
\]

Raw Collatz reachability supplies only the third of these directions:

\[
C^7(12)=4,
\]

whereas no iterate of 4 reaches 6 and no iterate of 6 reaches 12.

Therefore

\[
\boxed{P_s\ne C\ \text{on the active integer center projection}.}
\]

More strongly, no choice of fixed positive iterate `C^r` realizes the three-cycle on these three centers, because the first required edge `4 -> 6` is absent from the full forward orbit of 4.

This does not rule out a richer seed-pair, Poincare, holonomic, or lifted dynamical operator. It rules out identifying the already-defined Stage-24 label cycle with the ordinary raw Collatz map on the center projection.

## 4. Exact corridor parity words

For a finite corridor from `x` to a first hit of `y`, record the parities of the states before the hit:

\[
w_C(x\to y)=\big(C^k(x)\bmod2\big)_{k=0}^{d_C(x,y)-1}.
\]

For the two reverse-generation adjacent corridors,

\[
6\to4:\quad
6,3,10,5,16,8\to4,
\]

so

\[
\boxed{w_C(6\to4)=010100,}
\]

and

\[
12\to6:\quad12\to6,
\]

so

\[
\boxed{w_C(12\to6)=0.}
\]

These words are coefficient-free and transition-sensitive. They distinguish the two adjacent generation corridors without reading any coefficient packet.

## 5. IDT parity-phase coordinates

The canonical IDT Collatz--Fubini--Study phase is

\[
q_C(x)=\sum_{k\ge0}\frac{C^k(x)\bmod2}{2^{k+1}}\pmod1,
\]

with terminal values

\[
q_C(4)=\frac17,
\qquad q_C(2)=\frac27,
\qquad q_C(1)=\frac47,
\]

and exact doubling law

\[
q_C(Cx)=2q_C(x)\pmod1.
\]

If `x` reaches 1 after `L_x` steps, the same IDT registry gives

\[
q_C(x)=\sum_{k=0}^{L_x-1}\frac{b_k(x)}{2^{k+1}}
+\frac{4}{7\,2^{L_x}}.
\]

For the active centers this evaluates exactly to

\[
\boxed{
q_C(4)=\frac17,
\qquad
q_C(6)=\frac{141}{448},
\qquad
q_C(12)=\frac{141}{896}.
}
\]

The reachability chain is phase-compatible:

\[
\boxed{2q_C(12)=q_C(6),}
\]

\[
\boxed{2^6q_C(6)=q_C(4)\pmod1,}
\]

\[
\boxed{2^7q_C(12)=q_C(4)\pmod1.}
\]

Equivalently for

\[
\zeta_C(x)=e^{2\pi iq_C(x)},
\]

\[
\zeta_C(6)=\zeta_C(12)^2,
\qquad
\zeta_C(4)=\zeta_C(6)^{64}=\zeta_C(12)^{128}.
\]

## 6. Selector consequence

The previous stopping-length-only selector route was falsified under active seed precedence. The present theorem supplies a richer coefficient-free transition fingerprint:

\[
\boxed{
\mathfrak F(x\to y)
=
\big(d_C(x,y),w_C(x\to y),q_C(x),q_C(y)\big).
}
\]

For the two reverse-generation adjacent corridors,

\[
\mathfrak F(6\to4)\ne\mathfrak F(12\to6).
\]

Therefore the current active seed geometry does contain coefficient-free data capable of distinguishing these two corridors.

However, this theorem does **not** define or derive the map

\[
\mathfrak F\longmapsto(P_h,P_a,P_b,P_c).
\]

Consequently

\[
\boxed{\texttt{COEFFICIENT_TRANSITION_PARENT_SELECTOR remains OPEN}.}
\]

The exact gain is narrower: transition identifiability can use the full finite Collatz corridor/parity-phase fingerprint rather than the already-falsified stopping-length scalar alone.

## 7. Claim ledger

```text
stage22_active_seed_order = IMPORTED_CURRENT_REPOSITORY_PRECEDENCE
active_center_projection = EXACT_DEFINITION
center_reachability_chain_12_to_6_to_4 = EXACT_INTEGER_COMPUTATION
stage24_label_cycle_equals_raw_center_collatz = FALSE
corridor_parity_words = EXACT_INTEGER_COMPUTATION
idt_qC_4_qC_6_qC_12 = EXACT_CONDITIONAL_ON_DISPLAYED_TERMINAL_ORBITS
idt_phase_doubling_on_active_chain = EXACT
corridor_fingerprint_distinguishes_two_adjacent_reverse_generation_corridors = EXACT
coefficient_parent_map_from_fingerprint = OPEN
physical_transition_binding = NOT_CLAIMED
```

## 8. Reproducibility

Deterministic validator:

`TIR/validation/tir_active_seed_collatz_reachability_v0_1.py`

It independently computes all displayed center orbits, first-hitting distances, corridor parity words, exact rational IDT phases, and the incompatibility between the Stage-24 label cycle and raw center Collatz dynamics.