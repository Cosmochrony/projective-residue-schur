# Projective Residue Schur — Reduction of the Generation Split to the Chiral Asymmetry of Projection Locking

J. Beau, Independent Researcher, France

## Status

Preprint, v1.0. DOI: [10.5281/zenodo.20601040](https://doi.org/10.5281/zenodo.20601040)

## Abstract

The fermionic sub-programme of Cosmochrony locates the three-generation mass split in the
$J_3$-odd part of the squared projective endomorphism $E_\Pi^2$ restricted to the gauge-singlet
generation triplet $C^3_{\mathrm{gen}}$, parametrised by a single real number $u$ through
$E_\Pi^2|_{C^3_{\mathrm{gen}}} = \mathrm{diag}(1, \tfrac{1}{2} + u, \tfrac{1}{2} - u)$, with the
even sector $\mathrm{diag}(1, \tfrac{1}{2}, \tfrac{1}{2})$ already closed by Born–Infeld parity.

This note fixes the structural status of $u$ before any explicit construction of $E_\Pi$.

1. **Schur complement form.** The projected Dirac square admits a universal Feshbach/Schur form
   $E_\Pi = -\Pi_S \, D \, (1-P) \, D \, \Pi_S^{*} = -M^{\dagger} M$ with $P = \Pi_S^{*} \Pi_S$,
   exhibiting $E_\Pi$ as the Schur complement of the spinorial directions eliminated by the
   non-injective projection. It is negative semi-definite, zero-order, and vanishes in the
   injective limit.

2. **Chiral block reduction.** The chiral block decomposition shows that $u$ is controlled by
   the $\mathcal{D}^{\pm}$-transported, generation-projected part of the antiunitary chiral
   equivariance defect
   $$\Delta_\chi(P) = \pi_{LL} - \tau \, \overline{\pi_{RR}} \, \tau^{-1}$$
   of the eliminated block $1 - P$, rather than by a naive block difference.

3. **Stratification.** The minimal non-injectivity $c \leftrightarrow q - c$ is chirally
   symmetric, so $u = 0$ at the level of axioms A1–A3. A non-zero $u$ requires a chiral
   symmetry-breaking that can originate only in the projection-locking axiom A4.

4. **Seeley–DeWitt lock.** The conventions are locked so that the operator-level and
   spectral-level definitions of $u$ coincide on the flat effective metric; $u$ is
   normalisation-independent in the ratio.

5. **No finite chiral label.** A no-go result establishes that $u$ is not accessible to any
   finite front observable: chirality is a Lorentzian rather than a finite-fibre datum.

6. **Finite/Lorentzian separation.** Finite projection locking is $J_\Pi$-equivariant
   ($u_{\mathrm{fin}} = 0$); a non-zero generation split can arise only in the Lorentzian
   completion of the Born–Infeld saturation.

The remaining open deliverable is reduced to three sharp questions about A4: define the
Lorentzian saturation functional $\mathcal{B}(s)$ along the $J_\Pi$-odd modulus, compute the
chiral curvature $\mu_\chi^2 := \partial_s^2 \mathcal{B}(0)$, and handle the marginal case via
the leading non-vanishing even coefficient.

## Position in the programme

This note belongs to the **fermionic matter sub-programme** (Presentation Note 6). It refines
Q14's open deliverable on the inter-generation splitting by reducing the magnitude $|u|$ to a
single Lorentzian A4-level question (the chiral curvature $\mu_\chi^2$), and identifies the
front observables of the companion oriented-frontier note as null controls rather than carriers
of $u$.

## Compilation

```bash
bash compile.sh
```

Runs `pdflatex → bibtex → pdflatex → pdflatex` on `tex/ProjectiveResidueSchur.tex` and produces
`out/ProjectiveResidueSchur.pdf`.
