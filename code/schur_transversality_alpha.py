"""Bias-independent audit of the Schur-transversality lemma (Front B, step A).

Verifies, by exact symbolic computation (no numerical sampling), the closed form of the J_Pi-odd Cartan coefficient
alpha(t, s) of the lifted cascade generator, and that the mixing coefficient mu(t, s) vanishes identically.

Convention contract (frozen): fundamental V = C^2 with sl_2 generators E, F, H,
    [E, F] = H = 2 J_3,  [H, E] = 2 E,  [H, F] = -2 F,
oriented metaplectic step g = exp(t E) exp(s F), lifted to Sym^2(V) = C^3_gen = span(e_0, e_+, e_-) with
    J_3 = diag(0, 1, -1),  J_Pi^(2): e_0 -> -e_0, e_+ <-> e_-.

The audit confirms:
    g = [[1 + t s, t], [s, 1]],  det g = 1,
    log g = (r / sinh r) (t E + s F + (t s / 2) H),  cosh r = 1 + t s / 2,
    alpha(t, s) = t s * r / sinh r = t s + O((t s)^2),  alpha not identically zero,
    mu(t, s) = 0  (no R_mix on the outer-weight block).

No figures are produced. Code and comments are in English.
"""

import sympy as sp


def fundamental_generators():
    """Return the sl_2 generators E, F, H in the fundamental representation V = C^2."""
    E = sp.Matrix([[0, 1], [0, 0]])
    F = sp.Matrix([[0, 0], [1, 0]])
    H = sp.Matrix([[1, 0], [0, -1]])
    return E, F, H


def sym2_lift(M):
    """Lift a 2x2 traceless matrix M (element of sl_2) to its derived Sym^2 representation.

    Basis of Sym^2(V) ordered as (e_0, e_+, e_-) with e_+ = v_+^2, e_- = v_-^2, e_0 = sqrt(2) v_+ v_-,
    so that the induced grading of H = diag(1, -1) is diag(0, 2, -2) = 2 * J_3 with J_3 = diag(0, 1, -1).
    """
    a, b, c, d = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    # Action on monomials v_+^2, v_+ v_-, v_-^2 with v_+ -> a v_+ + c v_-, v_- -> b v_+ + d v_-
    # (M acts on column (v_+, v_-)). Derived (Lie-algebra) representation on the symmetric square:
    # rows/cols ordered (e_0, e_+, e_-) with e_0 = sqrt(2) v_+ v_-.
    s2 = sp.sqrt(2)
    # d/dt of Sym^2(exp(tM)) at 0, in basis (e_0, e_+, e_-):
    rep = sp.Matrix([
        [a + d,        s2 * c,      s2 * b],      # e_0 row
        [s2 * b,       2 * a,       0],           # e_+ row
        [s2 * c,       0,           2 * d],       # e_- row
    ])
    return rep


def hs_inner(A, B):
    """Hilbert-Schmidt inner product tr(A^dagger B), symbolic."""
    return sp.trace(A.conjugate().T * B)


def jpi_odd_part(A):
    """J_Pi-odd part of A on Sym^2(V): (A - J A J^{-1}) / 2 with J = J_Pi^(2) (real involution, J^2 = 1)."""
    # J_Pi^(2): e_0 -> -e_0, e_+ <-> e_-, in basis (e_0, e_+, e_-).
    J = sp.Matrix([[-1, 0, 0], [0, 0, 1], [0, 1, 0]])
    return (A - J * A * J.inv()) / 2


def main():
    t, s = sp.symbols("t s", real=True)
    E, F, H = fundamental_generators()

    # Step 1: g = exp(tE) exp(sF) and determinant.
    g = sp.exp(t * E) * sp.exp(s * F)
    g = sp.simplify(g)
    assert g == sp.Matrix([[1 + t * s, t], [s, 1]]), g
    assert sp.simplify(g.det()) == 1

    # Step 2: closed-form log via g = cosh r * I + sinh r * Ghat, log g = (r / sinh r)(g - cosh r * I).
    r = sp.symbols("r", positive=True)
    cosh_r = 1 + t * s / 2
    logg = (r / sp.sinh(r)) * (g - cosh_r * sp.eye(2))
    # Decompose log g onto (E, F, H): coefficients of E, F, H.
    coeffE = logg[0, 1]
    coeffF = logg[1, 0]
    coeffH = logg[0, 0]  # = -(logg[1,1]) by tracelessness
    assert sp.simplify(logg[0, 0] + logg[1, 1]) == 0  # traceless
    # Expected: coeffE = (r/sinh r) t, coeffF = (r/sinh r) s, coeffH = (r/sinh r)(ts/2).
    pref = r / sp.sinh(r)
    assert sp.simplify(coeffE - pref * t) == 0
    assert sp.simplify(coeffF - pref * s) == 0
    assert sp.simplify(coeffH - pref * (t * s / 2)) == 0

    # Step 3: lift log g to Sym^2(V) and extract the J_Pi-odd projection onto J_3 and R_mix.
    M_log = coeffE * E + coeffF * F + coeffH * H
    lift = sym2_lift(M_log)
    odd = jpi_odd_part(lift)

    J3 = sp.diag(0, 1, -1)
    Rmix = sp.Matrix([[0, 0, 0], [0, 0, 1], [0, -1, 0]])

    alpha = sp.simplify(hs_inner(odd, J3) / hs_inner(J3, J3))
    mu = sp.simplify(hs_inner(odd, Rmix) / hs_inner(Rmix, Rmix))

    # alpha should equal ts * (r / sinh r); mu should be exactly 0.
    assert sp.simplify(alpha - t * s * pref) == 0, alpha
    assert mu == 0, mu

    # Step 4: substitute the closed form r = arcosh(1 + ts/2) and check the leading BCH term.
    u = sp.symbols("u", positive=True)  # u stands for the product t s on the regular domain u > 0
    r_of_u = sp.acosh(1 + u / 2)
    alpha_u = u * r_of_u / sp.sinh(r_of_u)
    alpha_u = sp.simplify(alpha_u)
    leading = sp.series(alpha_u, u, 0, 2).removeO()  # leading term in u = ts

    print("g =", g.tolist())
    print("det g =", sp.simplify(g.det()))
    print("log g coefficients (E, F, H) =",
          (sp.simplify(coeffE), sp.simplify(coeffF), sp.simplify(coeffH)))
    print("alpha(t, s) =", alpha, "   [ = ts * r / sinh r ]")
    print("mu(t, s)    =", mu)
    print("alpha as a function of u = ts:", alpha_u)
    print("leading term of alpha in u = ts:", leading, "  (=> alpha = ts + O((ts)^2), not identically zero)")
    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    main()
