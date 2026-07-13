---
uuid: "jalon-26-exo-02"
title: "Famille de polynômes orthogonaux"
difficulty: 2
---

# Exercice 2 : Famille de polynômes orthogonaux (Difficulté ★★☆☆☆)

Soit $E = \mathbb{R}[X]$. On munit $E$ du produit scalaire $\langle P, Q \rangle = \int_{-1}^1 P(t)Q(t)dt$.
1. Montrer qu'il s'agit bien d'un produit scalaire sur $E$.
2. Appliquer l'algorithme de Gram-Schmidt à la famille $(1, X, X^2)$ pour trouver une base orthogonale de $\mathbb{R}_2[X]$. Ces polynômes sont proportionnels aux polynômes de Legendre.

## Démonstration Rigoureuse à Blanc

1. Soit $\langle P, Q \rangle = \int_{-1}^1 P(t)Q(t)dt$.
   - **Bilinéarité** : L'intégrale est linéaire par rapport à ses bornes et fonctions intégrées.
     $$ \langle \lambda P_1 + P_2, Q \rangle = \int_{-1}^1 (\lambda P_1(t) + P_2(t))Q(t)dt = \lambda \int_{-1}^1 P_1(t)Q(t)dt + \int_{-1}^1 P_2(t)Q(t)dt = \lambda \langle P_1, Q \rangle + \langle P_2, Q \rangle $$
   - **Symétrie** : $$ \langle P, Q \rangle = \int_{-1}^1 P(t)Q(t)dt = \int_{-1}^1 Q(t)P(t)dt = \langle Q, P \rangle $$
   - **Définie positive** :
     - Pour tout $P$, $\langle P, P \rangle = \int_{-1}^1 P(t)^2 dt$. L'intégrande $P(t)^2$ est positive ou nulle sur $[-1, 1]$, donc l'intégrale est positive ou nulle : $\langle P, P \rangle \ge 0$.
     - Si $\langle P, P \rangle = \int_{-1}^1 P(t)^2 dt = 0$, puisque la fonction $t \mapsto P(t)^2$ est continue et positive, son intégrale nulle sur $[-1, 1]$ implique que la fonction est nulle sur $[-1, 1]$.
     - Un polynôme $P$ ayant une infinité de racines (tout l'intervalle $[-1, 1]$) est nécessairement le polynôme nul. Donc $P = 0$.

2. Appliquons Gram-Schmidt pour trouver une base orthogonale (on ne demande pas de la normer ici, l'orthogonalité suffit). Notons $e_1 = 1$, $e_2 = X$, $e_3 = X^2$.
   - **Étape 1** : On pose $v_1 = e_1 = 1$.
   - **Étape 2** : $v_2 = e_2 - \frac{\langle e_2, v_1 \rangle}{\langle v_1, v_1 \rangle} v_1$.
     $$ \langle e_2, v_1 \rangle = \int_{-1}^1 t \cdot 1 dt = [\frac{t^2}{2}]_{-1}^1 = 0 $$
     Donc $v_2 = X$.
   - **Étape 3** : $v_3 = e_3 - \frac{\langle e_3, v_1 \rangle}{\langle v_1, v_1 \rangle} v_1 - \frac{\langle e_3, v_2 \rangle}{\langle v_2, v_2 \rangle} v_2$.
     $$ \langle e_3, v_1 \rangle = \int_{-1}^1 t^2 \cdot 1 dt = [\frac{t^3}{3}]_{-1}^1 = \frac{2}{3} $$
     $$ \langle v_1, v_1 \rangle = \int_{-1}^1 1^2 dt = 2 $$
     $$ \langle e_3, v_2 \rangle = \int_{-1}^1 t^2 \cdot t dt = \int_{-1}^1 t^3 dt = 0 $$
     Donc $v_3 = X^2 - \frac{2/3}{2} \cdot 1 = X^2 - \frac{1}{3}$.
   - La base orthogonale est $(1, X, X^2 - \frac{1}{3})$.
   $\blacksquare$
