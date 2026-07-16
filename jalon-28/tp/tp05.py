from tp01 import mat_add, mat_scale, mat_id

def puissance_matrice_racine_double(A, lamb, n):
    """
    Calcule A^n sachant que le polynôme caractéristique est (X - lamb)^2.
    R(X) = a_n X + b_n
    En X = lamb : lamb^n = a_n lamb + b_n
    Dérivée en X = lamb : n lamb^{n-1} = a_n
    """
    if n == 0:
        return mat_id(len(A))

    a_n = n * (lamb ** (n - 1))
    b_n = (lamb ** n) - a_n * lamb

    terme_A = mat_scale(a_n, A)
    terme_I = mat_scale(b_n, mat_id(len(A)))

    return mat_add(terme_A, terme_I)

# --- TESTS DE VALIDATION MATHÉMATIQUE ---
if __name__ == "__main__":
    # Matrice A de l'exercice 5 : chi_A = (X-1)^2 -> lamb=1
    A = [[0, -1],
         [1,  2]]
    lamb = 1
    n = 10

    # Calcul via notre formule analytique du reste
    A_n_analytique = puissance_matrice_racine_double(A, lamb, n)

    # Calcul par multiplication naïve pour comparer
    from tp01 import mat_mul
    A_n_naive = mat_id(2)
    for _ in range(n):
        A_n_naive = mat_mul(A_n_naive, A)

    for i in range(2):
        for j in range(2):
            assert abs(A_n_analytique[i][j] - A_n_naive[i][j]) < 1e-9, "Divergence de calcul."

    print("TP 5 : Validation mathématique réussie. Formule via division euclidienne exacte.")