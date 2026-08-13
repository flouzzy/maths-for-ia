---
uuid: "jalon-58-exo-01"
title: "Exercice 01 : Un ouvert dense n'est pas nécessairement de mesure pleine"
---

## Un ouvert dense n'est pas nécessairement de mesure pleine \quad $\bigstar\star\star\star\star$

Soit $X = \mathbb{R}$ muni de sa métrique usuelle. Montrer qu'il existe un ouvert dense $U \subset \mathbb{R}$ de mesure de Lebesgue arbitrairement petite, c'est-à-dire tel que pour tout $\epsilon > 0$, $\lambda(U) < \epsilon$.

## Correction Détaillée (Zéro Ellipse)


Soit $\epsilon > 0$. L'ensemble des rationnels $\mathbb{Q}$ est dénombrable. On peut donc l'écrire comme une suite $(q_n)_{n \in \mathbb{N}}$.
Pour chaque $n \in \mathbb{N}$, définissons l'intervalle ouvert $I_n = \left] q_n - \frac{\epsilon}{2^{n+2}}, q_n + \frac{\epsilon}{2^{n+2}} \right[$.
Soit $U = \bigcup_{n \in \mathbb{N}} I_n$.
1. $U$ est une réunion d'ouverts, donc $U$ est un ouvert.
2. Pour tout $n \in \mathbb{N}$, $q_n \in I_n \subset U$. Ainsi, $\mathbb{Q} \subset U$. Comme $\mathbb{Q}$ est dense dans $\mathbb{R}$, $U$ est également dense dans $\mathbb{R}$.
3. Par sous-additivité de la mesure de Lebesgue $\lambda$, on a :
   $$ \lambda(U) \leq \sum_{n=0}^{\infty} \lambda(I_n) = \sum_{n=0}^{\infty} \frac{\epsilon}{2^{n+1}} = \epsilon \sum_{n=1}^{\infty} \frac{1}{2^n} = \epsilon $$
Ainsi, $U$ est un ouvert dense de mesure strictement bornée par $\epsilon$.
