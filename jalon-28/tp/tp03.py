from tp01 import mat_add, mat_scale, mat_id
from tp02 import trace, determinant_2x2

def inverse_via_cayley_hamilton_2x2(A):
    det = determinant_2x2(A)
    if det == 0:
        raise ValueError("Matrice non inversible.")

    tr = trace(A)
    term1 = mat_scale(tr, mat_id(2))
    term2 = mat_scale(-1, A)

    somme = mat_add(term1, term2)
    return mat_scale(1.0 / det, somme)

# --- TESTS DE VALIDATION MATHÉMATIQUE ---
if __name__ == "__main__":
    A = [[4, 7],
         [2, 6]]

    inv_A = inverse_via_cayley_hamilton_2x2(A)

    # Validation du produit A * A^-1 = I_2
    from tp01 import mat_mul
    prod = mat_mul(A, inv_A)

    for i in range(2):
        for j in range(2):
            expected = 1.0 if i == j else 0.0
            assert abs(prod[i][j] - expected) < 1e-9, "Erreur d'inversion."

    print("TP 3 : Validation mathématique réussie. Inverse calculé formellement.")