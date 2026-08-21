# Exercice 2 : Intégrale de la fonction partie entière \quad $\bigstar\bigstar\star\star\star$

**Énoncé :**
Calculer $\int_{[0, 3]} \lfloor x \rfloor \, d\lambda$, où $\lambda$ est la mesure de Lebesgue sur $\mathbb{R}$.

**Correction :**
La fonction $s(x) = \lfloor x \rfloor$ sur $[0,3]$ est une fonction simple. Elle prend les valeurs 0, 1, 2, et 3.

Précisément :
$A_0 = \{x \in [0,3] \mid \lfloor x \rfloor = 0\} = [0, 1[$
$A_1 = \{x \in [0,3] \mid \lfloor x \rfloor = 1\} = [1, 2[$
$A_2 = \{x \in [0,3] \mid \lfloor x \rfloor = 2\} = [2, 3[$
$A_3 = \{x \in [0,3] \mid \lfloor x \rfloor = 3\} = \{3\}$

La forme canonique est $s = 0 \cdot \mathbf{1}_{A_0} + 1 \cdot \mathbf{1}_{A_1} + 2 \cdot \mathbf{1}_{A_2} + 3 \cdot \mathbf{1}_{A_3}$.

On calcule les mesures :
$\lambda(A_0) = 1 - 0 = 1$
$\lambda(A_1) = 2 - 1 = 1$
$\lambda(A_2) = 3 - 2 = 1$
$\lambda(A_3) = 0$ (un point est de mesure nulle).

L'intégrale est :
$\int_{[0,3]} \lfloor x \rfloor \, d\lambda = 0 \cdot 1 + 1 \cdot 1 + 2 \cdot 1 + 3 \cdot 0 = 3$.
