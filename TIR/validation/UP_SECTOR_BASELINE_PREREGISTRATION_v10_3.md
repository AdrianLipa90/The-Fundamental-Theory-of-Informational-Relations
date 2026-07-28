# Up-sector absolute-baseline preregistration v10.3

> **Historical status / superseded:** v10.4 proved that a single common additive
> `B_up` cannot close the fixed v10.2 up-sector trace.  This file is retained as
> the original constraint freeze and contamination declaration, but its
> common-baseline architecture is no longer an admissible next step.  The active
> architecture rules are now defined by
> `UP_SECTOR_COMMON_BASELINE_NO_GO_v10_4.md` and
> `UP_SECTOR_ARCHITECTURE_PREREGISTRATION_v10_5.md`.

## Status

- **Artifact class:** historical preregistration / constraint freeze
- **Formula selected:** no
- **Numerical benchmark performed:** no
- **Canonical promotion allowed:** no
- **Debt 9 status:** open
- **Purpose:** preserve the pre-v10.4 contamination and integrity declaration
- **Active architecture status:** superseded by v10.4 and v10.5

## 1. Contamination declaration

The following information has already been inspected and therefore cannot serve as a clean prospective holdout:

- all nine charged-fermion validation masses in the repository;
- the v10.1 quarter-power residuals;
- the v10.2 sector-holonomy residuals;
- the approximately `24.18x` absolute offset in the first-generation up-quark channel;
- the relative agreement obtained for the `c/t` release.

Any subsequent formula that is evaluated only against the same charged-fermion mass table is exploratory, even when its executable contains no mass input. Hashing a formula after it has been chosen from known residuals does not restore prospective independence.

## 2. Original research question — now closed as insufficient

The original v10.3 question was whether one could derive a **single common absolute baseline for the entire up-type sector** from already declared informational geometry, without using a `u`-specific correction and without changing the successful relative release between `u`, `c`, and `t`.

The proposed decomposition was

\[
\ln\frac{m_{u_g}}{m_e}
=
B_{\rm up}
+
\Delta_{\rm up}(g),
\qquad g\in\{1,2,3\}.
\]

v10.4 proves that this architecture cannot simultaneously remove the `u` residual and retain the current absolute `c/t` scale while `Delta_up(g)` is held fixed.  The proposal is therefore retained only as the hypothesis that was tested and rejected.

## 3. Frozen allowed inputs

A future candidate may use only coordinates already present before v10.3 in mass-free or pre-mass artifacts:

1. the informational preference quantum
   \[
   \kappa=\frac{\ln2}{24\pi};
   \]
2. the fixed structural constants `L3=7`, `L4=2`, and `L5=5`;
3. twin-prime pairs and their centre seeds `p+1`;
4. ordinary or accelerated Collatz invariants computed from those declared seeds;
5. Euler–Berry action and holonomy coordinates generated without observed masses;
6. the v3.4 sector-orientation coordinates, including colour depth, chiral path, hypercharge and electric-charge labels;
7. the v3.5 mass-free White-Thread/open-holonomy matrix;
8. Ramanujan coordinates already declared as a mandatory non-fit layer;
9. algebraic identities derived from the above objects without numerical residual minimization.

Heavy-quark rows marked `old_doc_bridge_ansatz_quarantined` must remain quarantined. Their presence may be reported but may not be silently upgraded into a first-principles input.

## 4. Forbidden inputs and operations

The following are prohibited:

- observed `u`, `c`, or `t` masses anywhere in candidate construction;
- the known factor `24.18`, its logarithm, or a nearby rational/transcendental approximation as a design target;
- a constant or phase acting only on `u`;
- independent coefficients for `u`, `c`, and `t`;
- scanning candidate formulas and selecting the one with the smallest error on the known charged-fermion table;
- selecting powers, signs, normalizations, seed mappings or branches after viewing their mass residuals;
- importing archived mass solvers, PDG tables, fitted Yukawa values or old residual corrections;
- describing the same charged-fermion table as a prospective holdout;
- promoting a candidate because it reproduces already inspected masses.

These prohibitions remain active under v10.5.

## 5. Historical structural invariants

The original v10.3 baseline candidate was required to satisfy:

1. one common action on `u`, `c`, and `t`;
2. no mass-derived generation refit;
3. preservation of
   \[
   m_u<m_c<m_t;
   \]
4. dimensionless structural action with the electron as the sole dimensional anchor;
5. mandatory Ramanujan continuity;
6. complete provenance;
7. no particle-name branch;
8. preservation of old-document quarantine.

The first condition is superseded because v10.4 proves it is insufficient.  Conditions 2--8 remain part of the active integrity policy.

## 6. Historical formula-selection procedure

Before any numerical comparison, v10.3 required a symbolic derivation, machine-readable input ledger, exact branch/sign conventions, operator fingerprint, algebraic checks and a named independent observable.

That process requirement remains valid.  The object to be derived is no longer a single common `B_up`; v10.5 allows only a universal pre-existing-sector functional or a universal relative-release operator.

## 7. Independent validation requirement

No clean unused charged-fermion mass remains inside the current table. Therefore a future result is promotion-eligible only when tested against an observable or dataset that did not participate in formula selection.

An admissible independent test must satisfy all of the following:

- it is named before its value is inspected for this purpose;
- it follows from the same frozen operator without an additional free scale;
- its extraction does not reuse the target mass residual as an intermediate quantity;
- the success and failure thresholds are fixed beforehand;
- failure is retained and reported without rewriting the operator.

v10.5 names the primary prospective observable as the first qualifying post-2026-07-28 joint ATLAS/CMS direct charm-to-top Higgs-coupling likelihood.

## 8. Active gates after supersession

### Technical gate

PASS requires deterministic execution, complete provenance, finite outputs, stable hashing and reproduction from a clean checkout.

### No-hidden-fit gate

PASS requires zero observed mass or mixing inputs in the operator, zero particle-specific coefficients, zero residual scans and a source ledger for every term.

### Structural gate

The active structural gate is defined in v10.5: the candidate must be a universal sector functional or a universal relative-release operator, must pass cross-transfer and must preserve quarantine.

### Prospective validation gate

PASS requires the independently preregistered observable. The known charged-fermion masses cannot satisfy this gate.

### Canonical gate

Canonical promotion requires all four gates. Technical or retrospective numerical success alone is insufficient.

## 9. Superseded conclusion

The v10.2 sector-holonomy trace remains a retrospective hypothesis generator.  v10.4 closes the common-baseline-only route.  The next implementation must begin from the v10.5 architecture freeze and must not infer a coefficient from the known `u` residual.
