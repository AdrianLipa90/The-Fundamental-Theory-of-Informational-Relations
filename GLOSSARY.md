# Glossary

## Tau / kernel / White-Thread / action stack

### White-Thread primitive
Minimal transported pairwise quantity
\[
W_{ij}[\gamma] = \langle \Psi_i|U[\gamma_{ij}]|\Psi_j\rangle.
\]
See `DEF-0010`.

### Loose-thread bundle
Finite family of admissible auxiliary paths for a fixed ordered pair. See `DEF-0011`.

### Effective White-Thread
Convexly aggregated transported pairwise amplitude
\[
W_{ij}^{eff} = \sum_a \alpha_a W_{ij}^{(a)}.
\]
See `DEF-0011`.

### Semantic path action
Scalar cost assigned to a candidate path. See `DEF-0012`.

### Dynamic path weights
Softmax-like normalized path weights
\[
\alpha_a = \frac{e^{-\sigma \mathcal S(\gamma^{(a)})}}{\sum_b e^{-\sigma \mathcal S(\gamma^{(b)})}}.
\]
See `DEF-0012`.

### Hermitian coupling projection
Real symmetric coupling extracted from effective White-Thread transport. See `DEF-0014`.

### Spectral tau modes
Eigenvalue-defined relational timescales
\[
\tau_i = \lambda_i(A).
\]
See `DEF-0014`.

### Object-state energy functional
Raw energetic state model for a canonical repository object.
\[
E_i^{raw}=F(\rho_i,p_i,w_i,\nu_i,\vec s_i,\chi_i,\mathcal N_i).
\]
See `DEF-0015`.

### Topological object seed
Seed computed from local and nonlocal object-state data rather than from local content alone. See `DEF-0015`.

### Normalized object amplitude
Amplitude derived from normalized energy
\[
A_i=\sqrt{\widetilde E_i}.
\]
See `DEF-0015`.

### Local object state
Complex state assigned to a canonical object
\[
\psi_i=A_i e^{i\phi_i}.
\]
See `DEF-0015`.

### Repository object-state extraction
Executable export path from a repository tree to `objects_state.csv` and `couplings.csv`. See `DEF-0016`.

### Local mass
First extracted scalar mass of a file object; token count for text-like files and nonempty noncomment line count for Python in the current extraction surface.

### Relational pressure
Deterministic type-based pressure assignment used by the first extraction surface.

### Couplings export
Table of extracted object-to-object relations in `couplings.csv`, currently generated from exact relative-path mentions.

### Flavor / color sector
Reserved downstream classification layer for fermion-sector interpretation. Not yet canonically identified in the current toy spectral bridge.
