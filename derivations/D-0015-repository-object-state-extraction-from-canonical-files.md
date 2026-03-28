# D-0015 — Repository object-state extraction from canonical files

## Status
`hypothesis`

## Depends on
- `DEF-0015`
- `DEF-0016`

## Goal
Derive a reproducible export path from canonical repository files to `objects_state.csv` and `couplings.csv`.

## Step 1 — Discover canonical files
Traverse the repository tree and collect file objects while excluding obvious runtime debris such as `.git` and `__pycache__` directories.

## Step 2 — Extract local features
For each file, record
\[
(\text{path},\text{type},\text{layer},\text{content\_hash},\text{size},\text{local\_mass}).
\]
The first local-mass ansatz is token count for text-like files and nonempty noncomment line count for Python source.

## Step 3 — Build couplings
For each ordered pair of files \((i,j)\), scan the textual content of \(i\) for exact relative-path mentions of \(j\). When such a mention exists, emit the coupling row
\[
(i,j,\text{relation\_type},C_{ij},\Delta\phi_{ij},m_{ij}).
\]
In the first extraction surface,
\[
\text{relation\_type}=\texttt{path\_mention},
\qquad
\Delta\phi_{ij}=0,
\qquad
C_{ij}=\text{exact mention count}.
\]

## Step 4 — Compute state fields
Define
\[
\text{crossref\_out}_i=\sum_j C_{ij},
\qquad
\text{crossref\_in}_i=\sum_j C_{ji}.
\]
Then set the first canonical extraction ansatz:
\[
\rho_i = \text{local\_mass}_i + \text{crossref\_in}_i + \text{crossref\_out}_i,
\]
\[
\mathcal N_i = \text{crossref\_in}_i + \text{crossref\_out}_i,
\]
\[
\vec s_i = (\text{local\_mass}_i,\text{crossref\_in}_i,\text{crossref\_out}_i,p_i,w_i,\nu_i).
\]
The pressure \(p_i\), weight \(w_i\), and character \(\chi_i\) are assigned by deterministic type maps.

## Step 5 — Energetic normalization
Insert these quantities into the raw-energy ansatz of `DEF-0015`:
\[
E_i^{raw}=F(\rho_i,p_i,w_i,\nu_i,\vec s_i,\chi_i,\mathcal N_i),
\]
then compute
\[
\widetilde E_i,\quad A_i,\quad \phi_i,\quad \psi_i.
\]

## Step 6 — Export surfaces
Write the resulting object rows to `objects_state.csv` and the coupling rows to `couplings.csv`, respecting the registered schemas.

## Registered fixture trace
For the registered three-file fixture,
\[
|\mathcal O|=3,
\qquad
|\mathcal C|=3.
\]
The three exported raw energies are approximately
\[
(38.86941557,\ 24.94578708,\ 10.96371863),
\]
which normalize to
\[
(0.51979107,\ 0.33359383,\ 0.14661509).
\]

## Result
The first executable extraction pipeline is therefore
\[
\text{repo tree}\to \mathcal L_i,\mathcal C \to \mathcal F_i \to E_i^{raw}\to \widetilde E_i,A_i,\phi_i \to \text{CSV exports}.
\]

## Scope restriction
This derivation closes only the first extraction layer. It does not yet infer semantic couplings beyond exact path mentions or calibrate the full raw-energy functional from repository history.
