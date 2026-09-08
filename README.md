# Projective Residue Schur — Reduction of the Generation Split to the Chiral Asymmetry of Projection Locking

J. Beau, Independent Researcher, France

## Status

Working paper, v2.0. DOI: [10.5281/zenodo.20601040](https://doi.org/10.5281/zenodo.20601040)

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

7. **Schur transversality.** In the present Lorentzian spin stratum the projected A4
   commutator has the closed form $\alpha(t, s) = ts\,(r/\sinh r) \not\equiv 0$, which excludes
   the exact-zero branch; under symbol-compatibility and the timelike identification
   $Z = [X, Y] \simeq \partial_\tau$ the transported zero-mode branch is excluded too, so the
   exhaustive transverse/null dichotomy selects the Schur-transverse case.

With Schur transversality proved, the Born–Infeld genus of the A4 companion note selects the
electric branch, $\mu_\chi^2 < 0$, and the generation split opens spontaneously, $u \neq 0$. The
remaining open deliverables are the explicit Lorentzian eliminated block $1 - P(s)$ entering the
Schur complement, the absolute normalisation $|u|$ (reduced by the constrained-jet companion note
to the admissible normalisation of $\partial_s \Delta_\chi(P)|_0$, with $|u|$ remaining
dictionary-bound), and the projected Yukawa sector with its mass matrices.

## Position in the programme

This note belongs to the **fermionic matter sub-programme** (Presentation Note 6). It refines
Q14's open deliverable on the inter-generation splitting by localising $u$ in the antiunitary
chiral equivariance defect and proving the Schur transversality of the A4 direction, and identifies
the front observables of the companion angular-amplitude and oriented-frontier notes as null
controls rather than carriers of $u$.

## Compilation

```bash
bash compile.sh
```

Runs `pdflatex → bibtex → pdflatex → pdflatex` on `tex/ProjectiveResidueSchur.tex` and produces
`out/ProjectiveResidueSchur.pdf`.
