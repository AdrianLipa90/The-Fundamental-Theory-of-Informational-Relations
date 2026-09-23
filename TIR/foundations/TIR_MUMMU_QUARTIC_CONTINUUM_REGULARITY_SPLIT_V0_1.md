# TIR MUMMU Quartic/Continuum Regularity Split v0.1

Status: `EXACT_GENERAL_TWO_LAYER_QUARTIC / EXACT_SMOOTH_PATH_QUARTIC_ABSENCE / SOURCE_PINNED_QHTRI_SIXTH_ORDER_WITNESS / PHYSICAL_BINDING_OPEN`

Date: 2026-09-23

## 1. Purpose

The MUMMU quartic seam was first derived for two finite noncommuting
(SU(2)) history increments.  The QHTRI closure now supplies a smooth
source-derived local connection

[
mathcal A(t)
=
-rac{i}{2}oldsymbolOmega(t)cdotoldsymbolsigma .
]

This note separates two mathematically distinct limits:

1. **finite-layer/amplitude scaling** of two fixed noncommuting increments;
2. **short-time continuum scaling** of one smooth connection trajectory.

They do not have the same leading scalar-character order.

## 2. General two-layer theorem

Let

[
X(arepsilon)
=
expleft[
-rac{iarepsilon}{2}mathbf acdotoldsymbolsigma
ight],
]

[
Y(arepsilon)
=
expleft[
-rac{iarepsilon}{2}mathbf bcdotoldsymbolsigma
ight].
]

Define

[
K_{m seq}(arepsilon)
=
rac12operatorname{Tr}[X(arepsilon)Y(arepsilon)]
]

and the same-integrated-vector comparator

[
K_{m const}(arepsilon)
=
rac12operatorname{Tr}
expleft[
-rac{iarepsilon}{2}
(mathbf a+mathbf b)cdotoldsymbolsigma
ight].
]

Using the Pauli product identity,

[
K_{m seq}
=
cosrac{arepsilon a}{2}
cosrac{arepsilon b}{2}
-
rac{mathbf acdotmathbf b}{ab}
sinrac{arepsilon a}{2}
sinrac{arepsilon b}{2},
]

where (a=|mathbf a|), (b=|mathbf b|).

Expanding both characters gives

[
oxed{
K_{m seq}
-
K_{m const}
=
rac{arepsilon^4}{96}
left(
a^2b^2-(mathbf acdotmathbf b)^2
ight)
+
O(arepsilon^6).
}
]

Therefore

[
oxed{
K_{m seq}
-
K_{m const}
=
rac{arepsilon^4}{96}
|mathbf a	imesmathbf b|^2
+
O(arepsilon^6).
}
]

The former orthogonal-axis result

[
rac{alpha^2eta^2}{96}
]

is the special case

[
mathbf a=alphahat x,
qquad
mathbf b=etahat y.
]

Thus the quartic history coefficient is the squared Lie-bracket area.

## 3. Commutator form

For

[
A=-rac{i}{2}mathbf acdotoldsymbolsigma,
qquad
B=-rac{i}{2}mathbf bcdotoldsymbolsigma,
]

[
[A,B]
=
-rac{i}{2}
(mathbf a	imesmathbf b)cdotoldsymbolsigma
]

and

[
|[A,B]|_F^2
=
rac12|mathbf a	imesmathbf b|^2.
]

Hence

[
oxed{
K_{m seq}-K_{m const}
=
rac{arepsilon^4}{48}
|[A,B]|_F^2
+
O(arepsilon^6).
}
]

This gives the quartic seam a basis-independent common-frame form.

## 4. Source-derived QHTRI finite-layer binding

For one QHTRI-driven pair (j), the previous theorem derives

[
oldsymbolOmega_j(t)
=
mathbf n_j(t)	imesdot{mathbf n}_j(t).
]

Any two admitted finite layer intervals with dimensionless integrated generator
vectors

[
mathbf a_j
=
int_{I_1}oldsymbolOmega_j(t),dt,
qquad
mathbf b_j
=
int_{I_2}oldsymbolOmega_j(t),dt
]

may therefore be inserted into the exact two-layer theorem without choosing
Pauli axes by hand.

If the finite-layer approximation uses source samples with widths
(Delta	au_1,Delta	au_2),

[
mathbf a_j
simeq
Delta	au_1oldsymbolOmega_j(t_1),
qquad
mathbf b_j
simeq
Delta	au_2oldsymbolOmega_j(t_2).
]

Then the source-derived leading history coefficient is

[
oxed{
c_{4,j}^{m layer}
=
rac1{96}
|mathbf a_j	imesmathbf b_j|^2.
}
]

No (x/y) axis selection is required.

## 5. Smooth-path Magnus expansion

Now consider a single smooth trajectory near (t=0),

[
oldsymbolOmega(t)
=
mathbf a+mathbf b,t+O(t^2).
]

Let

[
U_{m path}(T)
=
mathcal P
exp
left[
-rac{i}{2}
int_0^T
oldsymbolOmega(t)cdotoldsymbolsigma,dt
ight]
]

and

[
U_{m int}(T)
=
exp
left[
-rac{i}{2}
left(
int_0^ToldsymbolOmega(t),dt
ight)cdotoldsymbolsigma
ight].
]

The first Magnus vector is

[
mathbf M_1
=
int_0^ToldsymbolOmega(t),dt
=
mathbf aT+rac12mathbf bT^2+O(T^3).
]

The second Magnus vector begins at

[
oxed{
mathbf M_2
=
-rac{T^3}{12}
(mathbf a	imesmathbf b)
+
O(T^4).
}
]

Because

[
mathbf acdot(mathbf a	imesmathbf b)=0,
qquad
mathbf bcdot(mathbf a	imesmathbf b)=0,
]

the scalar character cannot acquire an order-(T^4) or order-(T^5)
difference from this correction.

Therefore, for a sufficiently smooth connection,

[
oxed{
rac12operatorname{Tr}U_{m path}(T)
-
rac12operatorname{Tr}U_{m int}(T)
=
O(T^6).
}
]

The finite-layer quartic law and the smooth-short-time law are therefore
different scaling statements.

## 6. Structural interpretation

The quartic coefficient

[
rac1{96}|mathbf a	imesmathbf b|^2
]

survives when two noncommuting integrated increments remain finite objects while
their common amplitude is scaled by (arepsilon).

It does **not** automatically survive when one shrinks a smooth time interval
(T	o0), because neighboring generator axes become parallel to leading order.

Hence:

[
oxed{
	ext{quartic seam}
=
	ext{finite-layer/noncommuting-step signature}
}
]

whereas

[
oxed{
	ext{smooth continuum short-time scalar memory}
=
O(T^6)
	ext{ generically}.
}
]

This distinction is required before assigning a continuum physical meaning to
the layered MUMMU theorem.

## 7. QHTRI deterministic witness

Using the pinned PNCS v0.32 deterministic fixture and pair (j=9), the
source-derived smooth path gives positive scalar-character differences
consistent with sixth-order short-time scaling.

For the validator windows (T=0.2,0.4,0.8),

[
Delta K(T)
=
K_{m path}(T)-K_{m int}(T)
]

is approximately

[
(3.2	imes10^{-14},,
2.0	imes10^{-12},,
1.27	imes10^{-10}),
]

subject to finite discretization/float64 error at the smallest window.

The robust ratios satisfy approximately

[
oxed{
rac{Delta K(0.8)}{Delta K(0.4)}
approx64,
}
]

the factor expected from

[
(2T)^6/T^6=64.
]

This is a computational witness for the source-pinned fixture, not a universal
physical scaling measurement.

## 8. Correction to the previous T36 firewall

The earlier statement that source-binding of the quartic history term required
an **inter-factor** intertwiner is too strong.

The corrected statement is:

- local full-(CP^1) QHTRI dynamics already supplies source-derived
  noncommuting generators within one factor;
- these generators can source the finite-layer quartic invariant
  (|mathbf a	imesmathbf b|^2/96);
- inter-factor coupling remains open only for cross-pair organization;
- the continuum (T	o0) limit of the same smooth path has a different,
  generically sixth-order scalar-character onset.

## 9. Claim ledger

| Statement | Status |
|---|---|
| general two-vector quartic coefficient ( |mathbf a	imesmathbf b|^2/96 ) | `EXACT ASYMPTOTIC` |
| old (alpha^2eta^2/96) is the orthogonal special case | `EXACT` |
| coefficient equals (|[A,B]|_F^2/48) | `EXACT` |
| source QHTRI supplies local noncommuting (Omega_j(t)) | `SOURCE-PINNED COMPUTATIONAL PASS` |
| finite QHTRI layer increments may feed the generalized quartic theorem | `EXACT CONDITIONAL ON LAYER DISCRETIZATION` |
| smooth-path second Magnus vector begins at (O(T^3)) | `EXACT LOCAL EXPANSION` |
| smooth scalar-character path-vs-integrated difference has no quartic onset | `EXACT LOCAL REGULARITY RESULT` |
| pinned QHTRI fixture is consistent with sixth-order short-time scaling | `COMPUTATIONAL PASS` |
| physical MUMMU layers are discrete rather than continuum | `OPEN` |
| physical neutrino/gravity interpretation | `OPEN / NOT CLAIMED` |

## 10. Validation

Deterministic validator:

`TIR/validation/tir_mummu_quartic_continuum_regularity_split_v0_1.py`

Static receipt:

`TIR/validation/TIR_MUMMU_QUARTIC_CONTINUUM_REGULARITY_SPLIT_VALIDATION_V0_1.json`

## 11. Next gate

The mathematical bottleneck is now physical/structural rather than algebraic:

[
oxed{
	ext{what source-derived criterion defines a finite MUMMU layer boundary?}
}
]

If PhaseNav supplies a canonical reduction/event boundary, the generalized
quartic coefficient can be evaluated on those finite intervals without an
arbitrary time slicing.

If no such boundary exists, the continuum branch should retain the sixth-order
smooth-path law instead of importing the finite-layer quartic seam.
