---
title: "Exercice 05 : Limite d'une suite de mesures"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 05 : Limite d'une suite de mesures

**Difficulté :** $\bigstar\bigstar\bigstar\star\star$

## Énoncé

Soit $f \in \mathcal{M}^+$ sur $(X, \mathcal{A})$. On définit $\nu(A) = \int_A f \, d\mu = \int_X f \mathbf{1}_A \, d\mu$ pour tout $A \in \mathcal{A}$. Si $f$ est une fonction simple, prouver que $\nu$ est une mesure (la $\sigma$-additivité).

---

## Correction détaillée

1. **Cas de la fonction simple :**
Supposons que $f = \sum_{i=1}^n a_i \mathbf{1}_{B_i}$ sous forme canonique ($a_i \ge 0$, les $B_i$ disjoints).

2. **Définition de $\nu$ :**
Pour $A \in \mathcal{A}$, la fonction $f \mathbf{1}_A = \sum_{i=1}^n a_i \mathbf{1}_{B_i} \mathbf{1}_A = \sum_{i=1}^n a_i \mathbf{1}_{B_i \cap A}$.
Cette fonction est simple. Son intégrale est :
$$ \nu(A) = \sum_{i=1}^n a_i \mu(B_i \cap A) $$

3. **$\sigma$-additivité :**
Soit $(A_k)_{k \ge 1}$ une suite d'ensembles mesurables deux à deux disjoints de $\mathcal{A}$, et $A = \bigcup_{k=1}^\infty A_k$.
On évalue $\nu(A)$ :
$$ \nu(A) = \sum_{i=1}^n a_i \mu\left( B_i \cap \bigcup_{k=1}^\infty A_k \right) = \sum_{i=1}^n a_i \mu\left( \bigcup_{k=1}^\infty (B_i \cap A_k) \right) $$
Pour chaque $i$, la suite d'ensembles $(B_i \cap A_k)_{k \ge 1}$ est composée d'ensembles disjoints. Puisque $\mu$ est une mesure, elle est $\sigma$-additive :
$$ \mu\left( \bigcup_{k=1}^\infty (B_i \cap A_k) \right) = \sum_{k=1}^\infty \mu(B_i \cap A_k) $$
En substituant dans $\nu(A)$ :
$$ \nu(A) = \sum_{i=1}^n a_i \sum_{k=1}^\infty \mu(B_i \cap A_k) $$
Toutes les quantités étant positives (ou $+\infty$), on peut intervertir les sommes finie et infinie :
$$ \nu(A) = \sum_{k=1}^\infty \left( \sum_{i=1}^n a_i \mu(B_i \cap A_k) \right) = \sum_{k=1}^\infty \nu(A_k) $$
$\nu(\emptyset) = 0$ est évident, donc $\nu$ est bien une mesure.
