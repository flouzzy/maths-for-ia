# Exercice 9

**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Montrer que si $X$ est une variable aléatoire mesurable par rapport à une tribu contenant uniquement des atomes disjoints $A_1, \dots, A_n$ (formant une partition de $\Omega$), alors $X$ est constante sur chaque atome $A_i$.

## Correction Détaillée

**Correction de l'exercice 9 :**

1. Soit $\mathcal{F} = \sigma(\{A_1, \dots, A_n\})$. Les ensembles de $\mathcal{F}$ sont exactement les unions d'ensembles $A_i$.
2. Soit $X$ une variable aléatoire $\mathcal{F}$-mesurable.
3. Raisonnons par l'absurde. Supposons qu'il existe un atome $A_k$ sur lequel $X$ n'est pas constante.
4. Cela signifie qu'il existe $\omega_1, \omega_2 \in A_k$ tels que $X(\omega_1) = c_1 \neq c_2 = X(\omega_2)$.
5. Prenons un intervalle ouvert $I$ centré sur $c_1$ mais ne contenant pas $c_2$. $I$ est un borélien.
6. Puisque $X$ est mesurable, l'image réciproque $X^{-1}(I) \in \mathcal{F}$.
7. L'ensemble $X^{-1}(I)$ contient $\omega_1$ (car $X(\omega_1) = c_1 \in I$), mais ne contient pas $\omega_2$ (car $X(\omega_2) = c_2 \notin I$).
8. Or, tout ensemble de $\mathcal{F}$ est une union d'atomes entiers. Si $X^{-1}(I)$ contient un point $\omega_1 \in A_k$, il doit contenir tout l'atome $A_k$.
9. Par conséquent, $\omega_2 \in A_k$ devrait aussi appartenir à $X^{-1}(I)$, ce qui contredit le point 7.
10. L'hypothèse de non-constance est fausse. $X$ est donc constante sur chaque $A_i$.
$\blacksquare$
