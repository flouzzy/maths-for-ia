---
uuid: "exo-jalon-63-03"
title: "Exercice 3 : Sous-additivité dénombrable (Inégalité de Boole)"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Sous-additivité dénombrable (Inégalité de Boole)

## Énoncé

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. Montrer que pour toute suite $(A_n)_{n \in \mathbb{N}}$ d'éléments de $\mathcal{A}$ (pas nécessairement disjoints), on a l'inégalité de sous-additivité : $$ \mu\left( \bigcup_{n=0}^{+\infty} A_n \right) \leq \sum_{n=0}^{+\infty} \mu(A_n) $$

## Correction Détaillée

Pour utiliser les propriétés de la mesure, nous devons transformer l'union arbitraire en une union d'ensembles disjoints.
Posons la suite de "disjointification" classique :
- $B_0 = A_0$
- $B_n = A_n \setminus \left( \bigcup_{k=0}^{n-1} A_k \right)$ pour $n \geq 1$.

Par construction :
1. Les ensembles $B_n$ sont mesurables car $\mathcal{A}$ est une tribu stable par union finie et complémentaire.
2. Les $(B_n)_{n \in \mathbb{N}}$ sont deux à deux disjoints.
3. On a l'égalité géométrique : $\bigcup_{n=0}^{+\infty} A_n = \bigcup_{n=0}^{+\infty} B_n$.
4. Pour tout $n \in \mathbb{N}$, on a explicitement l'inclusion $B_n \subset A_n$.

D'après le théorème de monotonie de la mesure (puisque $B_n \subset A_n$), nous avons $\mu(B_n) \leq \mu(A_n)$ pour tout $n$.
En appliquant l'axiome de $\sigma$-additivité à la suite disjointe $(B_n)$ :
$$ \mu\left( \bigcup_{n=0}^{+\infty} A_n \right) = \mu\left( \bigcup_{n=0}^{+\infty} B_n \right) = \sum_{n=0}^{+\infty} \mu(B_n) $$
Puisque toutes les quantités sont positives, nous pouvons sommer l'inégalité $\mu(B_n) \leq \mu(A_n)$ terme à terme :
$$ \sum_{n=0}^{+\infty} \mu(B_n) \leq \sum_{n=0}^{+\infty} \mu(A_n) $$
Ce qui démontre immédiatement le résultat : $\mu\left( \bigcup_{n=0}^{+\infty} A_n \right) \leq \sum_{n=0}^{+\infty} \mu(A_n)$. $\blacksquare$
