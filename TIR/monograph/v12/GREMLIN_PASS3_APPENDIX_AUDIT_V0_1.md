# GREMLIN Pass 3 — v12 Appendix Integration Audit v0.1

Status: `CANDIDATE_AUDIT_COMPLETE / DETERMINISTIC_PROMOTION_REQUIRED`

Branch: `feat/tir-monograph-v12-structural-skeleton`

Parent exact-head before Pass 3: `b95432d0c5a4aacdfa814c266629f09db6121ee6`

## Role boundary

GREMLIN is used as a bounded candidate-generation and adversarial-audit layer.
It has no independent execution or canon-promotion authority.  Findings below
enter v12 only after a direct algebraic check or deterministic validator gate.

## OWL — provenance routing

The four v12 appendix owners are:

- A: formal proofs, long algebra and legacy repairs;
- B: numerical receipts and reproducibility;
- C: prospective publication protocol;
- D: cross-framework interfaces.

Historical v11 appendices remain provenance sources and are not overwritten.

## HOUND — contradictions and formula drift

Pass 3 isolated the following high-value legacy surfaces.

1. **SU(3) representation label mismatch.**  
   The historical primer lists `(2,2)` as dimension 27 and labels it “Meson
   nonet”.  The dimension is correct; the label is not.  The flavour nonet is
   the reducible `3 x 3bar = 8 + 1` decomposition.  v12 Appendix A records the
   repair.

2. **Poincare distance normalization mismatch.**  
   The historical appendix uses
   `ds^2 = 4|dz|^2/(1-|z|^2)^2` but prints the geodesic distance with one
   `artanh` instead of `2 artanh`.  Radial integration fixes the factor two.
   v12 Appendix A records the repair.

3. **Operator-tetrahedron dihedral shortcut.**  
   The historical expression called a tetrahedral dihedral-angle rule is the
   planar law of cosines for a three-edge triangle.  v12 keeps the sector
   construction as historical provenance and quarantines that line as a
   geometry theorem source.

4. **Tetrahedron-volume / kappa-cubed binding.**  
   The historical volume proportionality lacks an independently derived Gram
   determinant plus scale map.  v12 routes the regular tetrahedral theorem to
   Chapter 6 and keeps the sector binding outside that theorem.

5. **Meson exponential arithmetic failure.**  
   The legacy pion/kaon expressions multiply Planck energy by order-one
   exponentials while printing MeV-scale targets.  v12 Appendix B keeps those
   formula FAIL witnesses explicit.

6. **Stale kappa ownership in an older SOH cross-relation appendix.**  
   One historical source describes `kappa = ln2/(24 pi)` as a structural
   definition/model postulate.  The canonical v12 source is the flavour-mixing
   normalization theorem, so Appendix D uses that derived ownership only.

## SPIDER — dependency ownership

The appendix dependency graph is now:

```text
A: theorem/algebra support
        |
        v
main chapters 4--14
        |
        +--> B: numerical receipts -> Chapter 19 verdict owner

C: frozen v10.7 prospective contract -> Chapter 20

D: TIR/SOH/IDT/RFC interfaces -> Chapter 21 completion frontier
```

This removes duplicate publication ownership: appendices support and audit;
main chapters own the active theorem/evidence narrative.

## MOLE — exact derivation candidates promoted after verification

The following candidates survived direct checks and are included:

- `dim(2,2)=27` and `3 x 3bar = 8 + 1`;
- `d_D(z1,z2)=2 artanh |(z1-z2)/(1-z1bar z2)|` for the displayed
  curvature `-1` disk metric;
- regular tetrahedral Gram spectrum `{0,4/3,4/3,4/3}`;
- common-baseline minimax error equal to half the invariant residual spread;
- accelerated-Collatz geometric-mean multiplier `rho_C=3/4` under the declared
  residue calculation;
- exact negative-inverse identity
  `Re(s)=1/2 <=> |1-1/s|=1`;
- IDT phase-clock dimensional carrier `ell_phi=c/|omega_t|`.

## MANTIS — duplicate/redundant ownership removals

- full kappa derivation remains owned by Chapter 9;
- current empirical verdicts remain owned by Chapter 19;
- prospective family decision status remains owned by Chapter 20;
- open SOH/IDT/RFC promotion gates remain owned by Chapter 21.

## Promotion gate

Pass 3 is promoted only if
`TIR/validation/tir_v12_appendix_integration_audit_v0_1.py`
returns `PASS` and the exact-head v12 publication workflow passes its hardened
LaTeX/PDF preflight.

GREMLIN promotion authority: `false`.
