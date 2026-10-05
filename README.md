# Projective Residue Schur — Reduction of the Generation Split to the Chiral Asymmetry of Projection Locking

J. Beau, Independent Researcher, France

## Status

Working paper, v3.0 (local candidate; last deposited version 2.1). DOI: [10.5281/zenodo.20601040](https://doi.org/10.5281/zenodo.20601040)

## Abstract

The fermionic sub-programme of Cosmochrony locates the three-generation mass split in the
$J_3$-odd part of the squared projective endomorphism $E_\Pi^2$ read on the gauge-singlet
generation triplet $C^3_{\mathrm{gen}}$ through a reading map $\Phi$, parametrised by a single real number $u$ through
$\Phi(E_\Pi^2) = \mathrm{diag}(1, \tfrac{1}{2} + u, \tfrac{1}{2} - u)$, with the
even sector $\mathrm{diag}(1, \tfrac{1}{2}, \tfrac{1}{2})$, the algebraic value of $(C_2 - J_3^2)/C_2$ at
$C_2 = 2$. Its reading as the Born–Infeld even sector would require an identification between the
conditional $3 \times 3$ model of O30 on $\mathrm{Sym}^2(V_\rho)$ and $(E_\Pi^2)_{\mathrm{even}}$; no such
identification is available, so that reading is not used here.

This note fixes the structural status of $u$ before any explicit construction of $E_\Pi$.

1. **Schur form.** For every locking operator $0 \preceq P \preceq 1$, the Schur expression
   $E_\Pi[P] = -\Pi_S \, D \, (1-P) \, D \, \Pi_S^{*} = -N^{\dagger} N$ with $N = (1-P)^{1/2} D\,\Pi_S^{*}$ is negative
   semi-definite. For the reference operator $P = \Pi_S^{*}\Pi_S$, under a contraction hypothesis, it is the compression
   remainder of the projected Dirac square (Q14's projective endomorphism when $\Pi_S D^2 \Pi_S^*$ is the Lichnerowicz
   operator). It is zero-order under an explicit symbol condition; for the reference operator on an irreducible Clifford
   fibre that condition forces $P = 1$ and $E_\Pi = 0$, so a non-zero residue needs a multiplicity space.
   $\Pi_S^{*}\Pi_S$ is idempotent if and only if $\Pi_S$ is a partial isometry.

2. **Chiral block reduction.** The chiral block decomposition relates the antiunitary chiral equivariance defect
   $$\Delta_\chi(P) = \pi_{LL} - \tau \, \overline{\pi_{RR}} \, \tau^{-1}$$
   of the eliminated block $1 - P$ to $u$ only as a structural reading, not a theorem. Under the generation-reading
   hypothesis [H-Gen], a non-zero split requires $J_\Pi P J_\Pi^{-1} \neq P$; in particular $u$ vanishes for the
   reference operator $\Pi_S^{*}\Pi_S$.

3. **Stratification.** Under a generation-reading hypothesis, if the locking operator commutes with $J_\Pi$ then
   $u = 0$. The minimal non-injectivity $c \leftrightarrow q - c$ is $J_\Pi$-symmetric, so on the structurally
   motivated reading of axioms A1–A3 $u = 0$ there; a non-zero $u$ requires a breaking of $J_\Pi$-equivariance, which
   on that reading can come only from the projection-locking axiom A4.

4. **Seeley–DeWitt conventions.** The conventions are fixed for the reference residue on a flat background, where
   $u = 0$; no spectral definition of $u$ is given for a general locking operator.

5. **No finite chiral label.** It is argued that $u$ is not accessible to any finite front observable: chirality is a
   Lorentzian rather than a finite-fibre datum.

6. **Finite sector.** The finite locking data are invariant under the parity $c \leftrightarrow q - c$, whose
   identification with $J_\Pi$ is open; under that identification, an equivariant construction of the finite locking
   operator and a finite reading, $u_{\mathrm{fin}} = 0$.

7. **Schur-null and Schur-transverse loci.** The $J_\Pi$-odd tilt of the locking operator, transported by the Schur
   map and read on the outer generation weights, is the $J$-odd part of the first-order polarisation; the locking is
   Schur-null when it vanishes and Schur-transverse otherwise. The oriented metaplectic step has the exact
   $\mathfrak{sl}_2$ opening $\alpha(x, y) = xy\,(r/\sinh r) \not\equiv 0$, produced by the commutator $[E,F] = H$.
   That the transported tilt equals this opening up to a non-zero factor is supplied by no source; under that
   hypothesis the locking is Schur-transverse.

Neither the sign of the Born–Infeld genus of the A4 companion note nor the non-vanishing of $u$ follows from this
note. The open deliverables are that hypothesis, the explicit Lorentzian eliminated block $1 - P(s)$, the
absolute normalisation $|u|$, and the projected Yukawa sector.

## Scope

For the reference operator $P = \Pi_S^{*}\Pi_S$ the compression remainder and its properties are established under the
stated hypotheses, and under the generation-reading hypothesis [H-Gen] (with $J_\Pi$-compatible $D$ and $\Pi_S$) the framework gives $u = 0$. For a general locking
operator $P \neq \Pi_S^{*}\Pi_S$ only the Schur expression and its sign are unconditional; the compression-remainder
formula and the Seeley–DeWitt identification do not transfer to it, and every consequence for a non-zero split is
conditional. The note localises necessary conditions and missing constructions; it derives no physical mechanism for a
non-zero split. Under the generation reading and the chiral splitting, a non-zero residue of a $J_\Pi$-commuting locking operator (in particular the reference one) cannot lie on the left-admissible branch of
Q14, since $J_\Pi$-invariance and $E\preceq0$ force it to vanish there.

The multiplicative reading of the generation triplet (reading map $\Phi$ multiplicative and positivity-preserving) is a
separate hypothesis, [H-Mult], not part of [H-Gen], which supplies only a real-linear $\Phi$. In the chiral rank-two left-admissible frame with a non-singular even sector,
[H-Mult] forces $u\equiv0$ (or admits no $\Phi$), so it cannot support a non-zero split there.

## Position in the programme

This note belongs to the **fermionic matter sub-programme** (Presentation Note 6). It refines
Q14's open deliverable on the inter-generation splitting by examining $u$ through the antiunitary
chiral equivariance defect and identifying the Schur-null and Schur-transverse loci of the A4 direction, and identifies
the front observables of the companion angular-amplitude and oriented-frontier notes as null
controls rather than carriers of $u$.

## Compilation

```bash
bash compile.sh
```

Runs `pdflatex → bibtex → pdflatex → pdflatex` on `tex/ProjectiveResidueSchur.tex` and produces
`out/ProjectiveResidueSchur.pdf`.

## Reproduction

```bash
cd code
python -W error schur_transversality_alpha.py
python -W error schur_symbol_obstruction.py
```

The first script verifies the exact $\mathfrak{sl}_2$ opening of the oriented step; the second verifies, in exact
arithmetic, the algebraic statements on the symbol condition (finite model, at a point). Neither controls terms
containing the derivative of $\Pi_S^{*}$. Dependencies: `code/requirements.txt`.

## Known debt (scripts)

`code/frontB2_no_horizontal_operation.py`, `code/frontB_recursive_type_rigidity.py` and
`code/spin-stratum-type-rigidity-test.py` are exploratory checks (√5 / 2I data) not cited by the TeX and supporting no
retained result; they are kept for history only.
