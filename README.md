# Projective Residue Schur — Reduction of the Generation Split to the Chiral Asymmetry of Projection Locking

J. Beau, Independent Researcher, France

## Status

Working paper, v3.0 (candidate, not deposited). DOI: [10.5281/zenodo.20601040](https://doi.org/10.5281/zenodo.20601040)

## Abstract

The fermionic sub-programme of Cosmochrony locates the three-generation mass split in the
$J_3$-odd part of the squared projective endomorphism $E_\Pi^2$ restricted to the gauge-singlet
generation triplet $C^3_{\mathrm{gen}}$, parametrised by a single real number $u$ through
$E_\Pi^2|_{C^3_{\mathrm{gen}}} = \mathrm{diag}(1, \tfrac{1}{2} + u, \tfrac{1}{2} - u)$, with the
even sector $\mathrm{diag}(1, \tfrac{1}{2}, \tfrac{1}{2})$, the algebraic value of $(C_2 - J_3^2)/C_2$ at
$C_2 = 2$. Its reading as the Born–Infeld even sector would require an identification between the
conditional $3 \times 3$ model of O30 on $\mathrm{Sym}^2(V_\rho)$ and $(E_\Pi^2)_{\mathrm{even}}$; no such
identification is available, so that reading is not used here.

This note fixes the structural status of $u$ before any explicit construction of $E_\Pi$.

1. **Schur complement form.** Under a contraction hypothesis on $\Pi_S$, the compression remainder of the projected
Dirac square admits a
   universal Feshbach/Schur form
   $E_\Pi = -\Pi_S \, D \, (1-P) \, D \, \Pi_S^{*} = -N^{\dagger} N$ with
   $N = (1-P)^{1/2} D\,\Pi_S^{*}$ and $P = \Pi_S^{*} \Pi_S$, negative semi-definite and vanishing where $P = 1$.
   It is zero-order under an explicit symbol condition; on irreducible Clifford fibres that condition forces
   $P = 1$ and $E_\Pi = 0$, so a non-zero residue needs a fibre on which the Clifford action is reducible.
   $P^2 = P$ holds if and only if $\Pi_S$ is a partial isometry.

2. **Chiral block reduction.** The chiral block decomposition expresses the antiunitary chiral equivariance defect
   $$\Delta_\chi(P) = \pi_{LL} - \tau \, \overline{\pi_{RR}} \, \tau^{-1}$$
   of the eliminated block $1 - P$, after $\mathcal{D}^{\pm}$-transport and projection to the generation triplet; a
   a non-zero split requires that the locking operator break $J_\Pi$-equivariance, under a generation-carrier
hypothesis.

3. **Stratification.** If the locking operator commutes with $J_\Pi$ then $u = 0$. The minimal non-injectivity
   $c \leftrightarrow q - c$ is $J_\Pi$-symmetric, so on the structurally motivated reading of axioms A1–A3
   $u = 0$ there; a non-zero $u$ requires a breaking of $J_\Pi$-equivariance, which on that reading can come
   only from the projection-locking axiom A4.

4. **Seeley–DeWitt lock.** The conventions are locked so that the operator-level and
   spectral-level definitions of $u$ coincide on a flat background; $u$ is
   normalisation-independent in the ratio.

5. **No finite chiral label.** A no-go result establishes that $u$ is not accessible to any
   finite front observable: chirality is a Lorentzian rather than a finite-fibre datum.

6. **Finite/Lorentzian separation.** If the finite locking operator is constructed equivariantly from the finite
   locking data, it is $J_\Pi$-equivariant ($u_{\mathrm{fin}} = 0$); a non-zero generation split can then arise only
   in the Lorentzian completion of the Born–Infeld saturation.

7. **Schur-null and Schur-transverse loci.** Under $J_\Pi$-compatibility, the first-order opening of the split is
governed
   by the $J_\Pi$-odd tilt of the locking operator transported by the Schur map to the outer generation weights; the
   locking is Schur-null when this transported tilt vanishes and Schur-transverse otherwise. The oriented metaplectic
   step has the exact $\mathfrak{sl}_2$ opening $\alpha(t, s) = ts\,(r/\sinh r) \not\equiv 0$, produced by the
   commutator $[E,F] = H$. That the transported tilt equals this opening up to a non-zero factor is supplied by no
   source; under that hypothesis the locking is Schur-transverse.

Neither the sign of the Born–Infeld genus of the A4 companion note nor the non-vanishing of $u$ follows from this
note. The open deliverables are that hypothesis, the explicit Lorentzian eliminated block $1 - P(s)$, the
absolute normalisation $|u|$, and the projected Yukawa sector.

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
