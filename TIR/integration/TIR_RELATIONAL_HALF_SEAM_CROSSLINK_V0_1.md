# TIR Relational Half-Seam Crosslink v0.1

Status: `TIR_STRUCTURAL_CROSSLINK_CANDIDATE`

Scope: TIR-only formalization of the statement that the two opposite relational
orientations associated with states `1` and `3` meet at the half-point of the
intermediate state `2`. This file is the bridge surface for sibling work in
`secret-of-a-half` and `Informational-Dynamics-of-Time`; source authority for the
theorem below remains in TIR.

## 1. Relational coordinate inside state 2

Let the intermediate relational domain be represented by an affine interval

\[
I_2=[a,b],\qquad a<b.
\]

Introduce the normalized affine coordinate

\[
u=\frac{x-a}{b-a}\in[0,1].
\]

The two directed relational shares carried into state `2` are

\[
\boxed{w_{1|2}(u)=1-u},\qquad
\boxed{w_{3|2}(u)=u},
\]

so that

\[
w_{1|2}(u)+w_{3|2}(u)=1.
\]

Orientation reversal across state `2` is the involution

\[
\boxed{J_2(u)=1-u},\qquad J_2^2=\mathrm{id}.
\]

It exchanges the two relational shares:

\[
w_{1|2}(J_2u)=w_{3|2}(u),\qquad
w_{3|2}(J_2u)=w_{1|2}(u).
\]

## 2. Relational Half-Seam Theorem

Define the meeting set of the two opposite relational orientations by equal
share:

\[
\mathcal S_{13|2}
=\{u\in[0,1]:w_{1|2}(u)=w_{3|2}(u)\}.
\]

Then

\[
1-u=u
\iff
2u=1
\iff
\boxed{u_\star=\frac12}.
\]

Hence

\[
\boxed{\mathcal S_{13|2}=\left\{\frac12\right\}}.
\]

The same point is the unique fixed point of the orientation-reversal involution:

\[
J_2(u_\star)=u_\star.
\]

In the original affine coordinate,

\[
\boxed{x_\star=\frac{a+b}{2}}.
\]

This is the precise TIR form of

\[
\boxed{1\;\longrightarrow\;\tfrac12(2)\;\longleftarrow\;3}.
\]

The half-point therefore enters first as a relational seam: the unique point at
which the two complementary orientations inside the intermediate domain carry
equal relational weight.

## 3. Information-theoretic lift

Associate binary relational entropy with the two complementary shares:

\[
H_{13|2}(u)
=-(1-u)\ln(1-u)-u\ln u.
\]

For `0<u<1`,

\[
H'_{13|2}(u)=\ln\frac{1-u}{u},
\]

and

\[
H''_{13|2}(u)
=-\frac1{1-u}-\frac1u<0.
\]

Thus the entropy is strictly concave and its unique stationary point is

\[
\boxed{u_\star=\frac12}.
\]

At the relational seam,

\[
\boxed{H_{13|2}(u_\star)=\ln2}.
\]

This gives the typed TIR chain

\[
\boxed{
\mathcal S_{13|2}
\xrightarrow{\;u_\star=1/2\;}
H_{13|2}=\ln2
\xrightarrow{\;\text{TIR normalization}\;}
\kappa=\frac{\ln2}{24\pi}
}.
\]

The seam theorem supplies the exact relational origin of the `ln2` numerator in
this chain. The factor `24\pi` remains the existing TIR normalization layer and
keeps its current claim class.

## 4. Projective lift

Define projective odds

\[
q(u)=\frac{u}{1-u},\qquad 0<u<1.
\]

Under the same TIR orientation reversal,

\[
q(J_2u)
=\frac{1-u}{u}
=\frac1{q(u)}.
\]

Therefore the half-seam maps to the positive reciprocal fixed point

\[
\boxed{u_\star=\frac12\quad\Longleftrightarrow\quad q_\star=1}.
\]

This is the direct structural crosslink to the complement/reciprocal layer of
`secret-of-a-half`.

## 5. Crosslink contract: Secret of a Half

TIR exports the immutable structural packet

```text
TIR_RELATIONAL_HALF_SEAM_V0_1
u_star              = 1/2
w_1_given_2          = 1/2
w_3_given_2          = 1/2
orientation_reverse = u -> 1-u
projective_odds      = 1
relational_entropy   = ln2
kappa                = ln2/(24*pi)
```

The sibling `secret-of-a-half` programme may identify this packet with its
binary complement fixed point, reciprocal fixed point, Fisher--Rao midpoint,
and entropy maximum. Its own zeta/theorem promotion rules remain the authority
for downstream claims.

Reference repository:

`AdrianLipa90/secret-of-a-half`

Observed reference head during this crosslink pass:

`4cf36453ee2b6d33a1f9177ca324b9ef491270be`

## 6. Crosslink contract: Informational Dynamics of Time

The current temporal dependency spine is

\[
\mathrm{TIR}
\rightarrow
\mathrm{Temporal\ Primitive}
\rightarrow
\mathrm{Temporal\ Wave}
\rightarrow
\mathrm{NOW}
\rightarrow\cdots
\]

TIR supplies a candidate structural boundary packet at its outgoing interface:

\[
\boxed{
\mathrm{TIR}
\;\xrightarrow{\;\mathcal S_{13|2}\;}
\left(u_\star=\frac12,\;H=\ln2,\;q=1\right)
\;\dashrightarrow\;
\mathrm{Temporal\ Primitive}
\rightarrow
\mathrm{Temporal\ Wave}
\rightarrow
\mathrm{NOW}
}.
\]

The dashed arrow is a cross-repository interface. The TIR statement carried by
that arrow is the exact relational half-seam packet above. Temporal evolution,
wave dynamics and the operational role of `NOW` are adjudicated by
`Informational-Dynamics-of-Time`.

Reference repository:

`AdrianLipa90/Informational-Dynamics-of-Time`

Observed reference head during this crosslink pass:

`7f46792bc1f18904808f6af9813a35ed81f3ac15`

## 7. Coordinate firewall

The exact primitive is relational balance

\[
\boxed{w_{1|2}=w_{3|2}=\frac12}.
\]

The geometric statement

\[
x_\star=\frac{a+b}{2}
\]

uses the declared affine encoding of relation share across `I_2`. A later
physical coordinate may use another chart; the crosslink packet therefore
carries both the invariant relational balance and the explicit affine chart.

## 8. Claim classes

| Statement | TIR class |
|---|---|
| `J_2(u)=1-u` is an involution | EXACT DEFINITIONAL |
| `Fix(J_2)={1/2}` | EXACT |
| equal-share meeting set is `{1/2}` | EXACT CONDITIONAL ON DECLARED COMPLEMENTARY WEIGHTS |
| affine physical-coordinate midpoint is `(a+b)/2` | EXACT CONDITIONAL ON DECLARED AFFINE CHART |
| `H_{13|2}` has unique maximum `ln2` at `1/2` | EXACT INFORMATION-THEORETIC |
| `q(J_2u)=1/q(u)` and `q_star=1` | EXACT PROJECTIVE |
| seam entropy feeds the `ln2` numerator of `kappa` | EXACT TYPED TIR BINDING |
| `24*pi` denominator | EXISTING TIR STRUCTURAL NORMALIZATION |
| use of the packet by Secret of a Half | CROSSLINK INPUT |
| use of the packet by Dynamics of Time / NOW | CROSSLINK INPUT |

## 9. Validation

Deterministic executable audit:

`TIR/validation/tir_relational_half_seam_v0_1.py`

The audit checks:

- exact rational half-seam equality;
- fixed-point property under `u -> 1-u`;
- affine midpoint covariance on exact rational intervals;
- strict-concavity certificate and `H(1/2)=ln2` implementation check;
- complement/reciprocal conjugacy on exact rational samples;
- exact typed binding of the seam entropy to the existing TIR `kappa` numerator.

## 10. Dependency direction

```text
TIR RELATIONAL HALF-SEAM
  |---> secret-of-a-half       [crosslink consumer]
  `---> Informational-Dynamics-of-Time [crosslink consumer]
```

All source modifications for v0.1 are confined to the TIR repository.
