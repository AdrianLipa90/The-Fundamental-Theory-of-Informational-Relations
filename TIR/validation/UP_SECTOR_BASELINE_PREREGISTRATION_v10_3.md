# Up-sector absolute-baseline preregistration v10.3

## Status

- **Artifact class:** preregistration / constraint freeze
- **Formula selected:** no
- **Numerical benchmark performed:** no
- **Canonical promotion allowed:** no
- **Debt 9 status:** open
- **Purpose:** prevent post-residual formula selection after the retrospective v10.2 sector-holonomy signal

## 1. Contamination declaration

The following information has already been inspected and therefore cannot serve as a clean prospective holdout:

- all nine charged-fermion validation masses in the repository;
- the v10.1 quarter-power residuals;
- the v10.2 sector-holonomy residuals;
- the approximately `24.18x` absolute offset in the first-generation up-quark channel;
- the relative agreement obtained for the `c/t` release.

Any subsequent formula that is evaluated only against the same charged-fermion mass table is exploratory, even when its executable contains no mass input. Hashing a formula after it has been chosen from known residuals does not restore prospective independence.

## 2. Research question

Can one derive a **single common absolute baseline for the entire up-type sector** from already declared informational geometry, without using a `u`-specific correction and without changing the successful relative release between `u`, `c`, and `t`?

The desired decomposition is

\[
\ln\frac{m_{u_g}}{m_e}
=
B_{\rm up}
+
\Delta_{\rm up}(g),
\qquad g\in\{1,2,3\},
\]

where:

- `B_up` is common to `u`, `c`, and `t`;
- `Delta_up(g)` is the already declared relative-generation trace;
- neither term may contain observed up-sector masses or residual-derived numbers.

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

## 5. Structural invariants that must be preserved

Every admissible baseline candidate must satisfy all of the following before any external validation:

1. **Common-sector action:** the same `B_up` acts on `u`, `c`, and `t`.
2. **No generation refit:** the v10.2 relative-generation release is not re-estimated from masses.
3. **Order preservation:**
   \[
   m_u<m_c<m_t.
   \]
4. **Dimensional discipline:** `B_up` is dimensionless; the electron remains the only dimensional mass anchor in the current one-anchor architecture.
5. **Ramanujan continuity:** the mandatory Ramanujan layer cannot be removed merely because another coordinate gives lower residuals.
6. **Provenance:** every source field must be named, versioned and hashed.
7. **Single formula:** no conditional branch keyed by particle name.
8. **Quarantine preservation:** old-document heavy-sector assumptions remain explicitly labelled.

## 6. Formula-selection procedure

Before any numerical comparison is made, a future module must produce:

- a symbolic derivation of `B_up`;
- a machine-readable list of all structural inputs;
- the exact branch/sign conventions;
- an operator fingerprint;
- algebraic and dimensional checks;
- a declaration of the independent observable to be used for prospective validation.

If more than one formula remains possible after symbolic derivation, none may be selected using the known charged-fermion masses. The alternatives must be retained as a finite preregistered family and tested on an independent observable under a multiplicity-aware rule.

## 7. Independent validation requirement

No clean unused charged-fermion mass remains inside the current table. Therefore a future result is promotion-eligible only when tested against an observable or dataset that did not participate in formula selection.

An admissible independent test must satisfy all of the following:

- it is named before its value is inspected for this purpose;
- it follows from the same up-sector baseline without an additional free scale;
- its extraction does not reuse the target mass residual as an intermediate quantity;
- the success and failure thresholds are fixed beforehand;
- failure is retained and reported without rewriting the baseline.

Until such a test is identified, a new `B_up` formula may be documented only as a structural candidate.

## 8. Prospective gates

### Technical gate

PASS requires deterministic execution, complete provenance, finite outputs, stable hashing and reproduction from a clean checkout.

### No-hidden-fit gate

PASS requires zero observed mass or mixing inputs in the operator, zero particle-specific coefficients, zero residual scans and a source ledger for every term.

### Structural gate

PASS requires a common up-sector baseline, preservation of `u<c<t`, preservation of the relative `c/t` release and compatibility with the declared colour/chirality geometry.

### Prospective validation gate

PASS requires an independent preregistered observable. The known charged-fermion masses cannot satisfy this gate.

### Canonical gate

Canonical promotion requires all four gates. Technical or retrospective numerical success alone is insufficient.

## 9. Current frozen conclusion

The v10.2 sector-holonomy trace is retained as a strong retrospective hypothesis generator. Its numerical pattern motivates the search for a common absolute up-sector baseline, but it does not determine that baseline.

The next implementation must begin from this preregistration and must not infer a new coefficient from the known `u` residual.
