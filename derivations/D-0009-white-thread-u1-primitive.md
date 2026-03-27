# D-0009 — White-Thread U(1) primitive from Berry connection transport

## Status
`derived`

## Depends on
- `DEF-0002`
- `DEF-0010`

## Goal
Derive the minimal abelian White-Thread primitive from Berry-connection transport and establish the basic amplitude bound for normalized states.

## Step 1 — Berry connection transport
Given a connection one-form \(A\) along a path \(\gamma_{ij}\), define
\[
U[\gamma_{ij}] = \mathcal P\exp\!\left(i\int_{\gamma_{ij}} A\right).
\]
For a U(1) connection the path-ordering is trivial because all factors commute, hence
\[
U[\gamma_{ij}] = \exp\!\left(i\int_{\gamma_{ij}} A\right).
\]
This is the standard abelian holonomy construction and is the Wilson-line analogue in the U(1) sector.

## Step 2 — White-Thread matrix element
Define the transported pairwise quantity
\[
W_{ij}[\gamma] = \langle \Psi_i | U[\gamma_{ij}] | \Psi_j \rangle.
\]
This makes the White-Thread object a matrix element of the transport operator rather than a raw phase alone.

## Step 3 — Unitary magnitude bound
For normalized states and unitary transport,
\[
|W_{ij}[\gamma]| = |\langle \Psi_i | U[\gamma_{ij}] | \Psi_j \rangle|
\le \|\Psi_i\|\,\|U[\gamma_{ij}]\Psi_j\| = 1,
\]
using Cauchy--Schwarz and \(U^\dagger U = 1\).

## Result
The White-Thread primitive is canonically represented as a transported U(1) matrix element obeying
\[
W_{ij}[\gamma] = \langle \Psi_i | U[\gamma_{ij}] | \Psi_j \rangle,
\qquad
|W_{ij}[\gamma]|\le 1.
\]

## Scope restriction
This derivation closes only the minimal abelian primitive. It does not yet incorporate non-abelian transport, calibration layers, or effective pairwise amplification beyond the primitive bound.
