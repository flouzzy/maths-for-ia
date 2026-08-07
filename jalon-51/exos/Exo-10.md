## Exercice 10 : Convergence de suites dans un espace métrique \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Dans un espace métrique $(X, d)$, on dit qu'une suite $(x_n)$ converge vers $L$ si $d(x_n, L) \to 0$.
Montrer que si $x_n \to L$, alors l'unicité de la limite est garantie.

**Correction :**
Supposons par l'absurde qu'une suite $(x_n)$ admette deux limites distinctes $L_1$ et $L_2$ avec $L_1 \neq L_2$.
Alors $d(L_1, L_2) > 0$ par l'axiome de séparation. Posons $\epsilon = \frac{d(L_1, L_2)}{2} > 0$.
Puisque $x_n \to L_1$, il existe $N_1$ tel que pour $n \ge N_1$, $d(x_n, L_1) < \epsilon$.
Puisque $x_n \to L_2$, il existe $N_2$ tel que pour $n \ge N_2$, $d(x_n, L_2) < \epsilon$.
Soit $N = \max(N_1, N_2)$. Pour $n \ge N$, évaluons la distance entre $L_1$ et $L_2$ avec l'inégalité triangulaire en passant par $x_n$ :
$$ d(L_1, L_2) \le d(L_1, x_n) + d(x_n, L_2) $$
$$ d(L_1, L_2) < \epsilon + \epsilon = 2\epsilon $$
Or, par définition, $2\epsilon = d(L_1, L_2)$. Nous aboutissons donc à la contradiction stricte :
$$ d(L_1, L_2) < d(L_1, L_2) $$
L'hypothèse initiale est fausse. La limite d'une suite dans un espace métrique, lorsqu'elle existe, est unique. $\blacksquare$
