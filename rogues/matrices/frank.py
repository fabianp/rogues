import numpy as np


def frank(n, k=0):
    """
    frank(n, k = 0) Frank matrix---ill conditioned eigenvalues.
        f = frank(n, k) is the Frank matrix of order N.  It is upper
        Hessenberg with determinant 1.  K = 0 is the default; if K = 1 the
        elements are reflected about the anti-diagonal (1,N)--(N,1).
        F has all positive eigenvalues and they occur in reciprocal pairs
        (so that 1 is an eigenvalue if N is odd).
        The eigenvalues of F may be obtained in terms of the zeros of the
        Hermite polynomials.
        The FLOOR(N/2) smallest eigenvalues of F are ill conditioned,
        the more so for bigger N.

        DET(FRANK(N)') comes out far from 1 for large N---see Frank (1958)
        and Wilkinson (1960) for discussions.

        This version incorporates improvements suggested by W. Kahan.

        References:
        W.L. Frank, Computing eigenvalues of complex matrices by determinant
           evaluation and by methods of Danilewski and Wielandt, J. Soc.
           Indust. Appl. Math., 6 (1958), pp. 378-392 (see pp. 385, 388).
        G.H. Golub and J.H. Wilkinson, Ill-conditioned eigensystems and the
           computation of the Jordan canonical form, SIAM Review, 18 (1976),
             pp. 578-619 (Section 13).
        H. Rutishauser, On test matrices, Programmation en Mathematiques
           Numeriques, Editions Centre Nat. Recherche Sci., Paris, 165,
           1966, pp. 349-365.  Section 9.
        J.H. Wilkinson, Error analysis of floating-point computation,
           Numer. Math., 2 (1960), pp. 319-340 (Section 8).
        J.H. Wilkinson, The Algebraic Eigenvalue Problem, Oxford University
           Press, 1965 (pp. 92-93).
        The next two references give details of the eigensystem, as does
        Rutishauser (see above).
        P.J. Eberlein, A note on the matrices denoted by B_n, SIAM J. Appl.
           Math., 20 (1971), pp. 87-92.
        J.M. Varah, A generalization of the Frank matrix, SIAM J. Sci. Stat.
           Comput., 7 (1986), pp. 835-839.

    NOTE: This is a slightly different implementation from Version 3.  It
    loosely follows the TOMS694 version, _except_ that it directly computes
    the frank matrix, instead of its anti-transposed version.  Therefore,
    we take the anti-transpose if k == 1
    """

    f = np.ones((n, n)) * np.arange(n, 0, -1)
    f = np.minimum(f, f.T)
    #   take upper Hessenberg part.
    f = np.triu(f, -1)
    if k == 1:
        f = f[::-1, ::-1].T

    return f
