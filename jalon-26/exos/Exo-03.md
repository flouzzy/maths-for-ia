---
uuid: "jalon-26-exo-03"
title: "Distance à un sous-espace"
difficulty: 2
---

# Exercice 3 : Distance à un sous-espace (Difficulté ★★☆☆☆)

Dans l'espace euclidien $\mathbb{R}^4$ muni du produit scalaire canonique, on considère le sous-espace $F$ défini par le système d'équations :
$$ \begin{cases} x_1 + x_2 + x_3 + x_4 = 0 \\ x_1 - x_2 + x_3 - x_4 = 0 \end{cases} $$
1. Déterminer une base orthogonale de $F$.
2. Calculer la distance du point $A(1, 2, 3, 4)$ au sous-espace $F$ en utilisant le théorème de la projection orthogonale.

## Démonstration Rigoureuse à Blanc

1. Commençons par trouver une base de $F$. Le système est :
   $$ \begin{cases} x_1 + x_3 = -(x_2 + x_4) \\ x_1 + x_3 = x_2 + x_4 \end{cases} $$
   En sommant et soustrayant, on obtient :
   $$ 2(x_1 + x_3) = 0 \implies x_3 = -x_1 $$
   $$ 2(x_2 + x_4) = 0 \implies x_4 = -x_2 $$
   Un vecteur générique de $F$ s'écrit $x = (x_1, x_2, -x_1, -x_2) = x_1(1, 0, -1, 0) + x_2(0, 1, 0, -1)$.
   Posons $v_1 = (1, 0, -1, 0)$ et $v_2 = (0, 1, 0, -1)$.
   Calculons leur produit scalaire : $\langle v_1, v_2 \rangle = (1)(0) + (0)(1) + (-1)(0) + (0)(-1) = 0$.
   Les vecteurs $v_1$ et $v_2$ sont déjà orthogonaux ! La famille $(v_1, v_2)$ est donc une base orthogonale de $F$.

2. La distance de $x = (1, 2, 3, 4)$ à $F$ est donnée par $d(x, F) = \|x - p_F(x)\|$, où $p_F(x)$ est la projection orthogonale de $x$ sur $F$.
   - Puisque $(v_1, v_2)$ est une base orthogonale de $F$, on a la formule :
     $$ p_F(x) = \frac{\langle x, v_1 \rangle}{\|v_1\|^2} v_1 + \frac{\langle x, v_2 \rangle}{\|v_2\|^2} v_2 $$
   - Calculons les termes :
     $$ \langle x, v_1 \rangle = (1)(1) + (2)(0) + (3)(-1) + (4)(0) = 1 - 3 = -2 $$
     $$ \|v_1\|^2 = 1^2 + 0^2 + (-1)^2 + 0^2 = 2 $$
     $$ \langle x, v_2 \rangle = (1)(0) + (2)(1) + (3)(0) + (4)(-1) = 2 - 4 = -2 $$
     $$ \|v_2\|^2 = 0^2 + 1^2 + 0^2 + (-1)^2 = 2 $$
   - La projection est :
     $$ p_F(x) = \frac{-2}{2} (1, 0, -1, 0) + \frac{-2}{2} (0, 1, 0, -1) = -1(1, 0, -1, 0) - 1(0, 1, 0, -1) = (-1, -1, 1, 1) $$
   - Le vecteur différence est :
     $$ x - p_F(x) = (1, 2, 3, 4) - (-1, -1, 1, 1) = (2, 3, 2, 3) $$
   - La distance cherchée est la norme de ce vecteur :
     $$ d(x, F)^2 = \|x - p_F(x)\|^2 = 2^2 + 3^2 + 2^2 + 3^2 = 4 + 9 + 4 + 9 = 26 $$
     $$ d(x, F) = \sqrt{26} $$
   $\blacksquare$
