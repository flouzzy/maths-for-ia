---
title: "Exercice 5 : TCM"
difficulty: "★★★☆☆"
---
# Exercice 5 : Lemme de Borel-Cantelli via Beppo-Levi

**Niveau :** $\bigstar\bigstar\bigstar\star\star$

**Énoncé :**
Soit $(A_n)_{n \in \mathbb{N}}$ une suite de parties mesurables d'un espace de probabilité $(X, \mathcal{A}, \mathbb{P})$ telles que $\sum_{n=0}^{+\infty} \mathbb{P}(A_n) < +\infty$. En appliquant le TCM à $u_n(x) = \mathbf{1}_{A_n}(x)$, prouver que la probabilité de l'ensemble $\limsup A_n$ (les $x$ appartenant à une infinité de $A_n$) est nulle.

**Correction détaillée :**
1. Posons la série des indicatrices : $S(x) = \sum_{n=0}^{+\infty} \mathbf{1}_{A_n}(x)$. Cette fonction compte à combien d'ensembles $A_n$ l'élément $x$ appartient.
2. L'ensemble limite supérieure est $A = \limsup A_n = \{x \in X \mid S(x) = +\infty\}$.
3. Appliquons le corollaire du TCM : $\int_X S(x) d\mathbb{P} = \sum_{n=0}^{+\infty} \int_X \mathbf{1}_{A_n}(x) d\mathbb{P} = \sum_{n=0}^{+\infty} \mathbb{P}(A_n)$.
4. Par hypothèse, cette somme est finie (disons $M < \infty$). Donc $S \in \mathcal{L}^1$.
5. Si l'intégrale d'une fonction positive est finie, alors l'ensemble où elle vaut l'infini est de mesure nulle. Donc $\mathbb{P}(A) = \mathbb{P}(\{x \mid S(x) = +\infty\}) = 0$.
