---
title: "Exercice 01 : Calcul d'intégrale pour une fonction simple basique"
difficulty: "$\bigstar\star\star\star\star$"
---

# Exercice 01 : Calcul d'intégrale pour une fonction simple basique

**Difficulté :** $\bigstar\star\star\star\star$

## Énoncé

Soit l'espace mesuré $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$. Soit $f$ la fonction définie par $f(x) = 3$ si $x \in [-1, 2]$, $f(x) = 4$ si $x \in [3, 5]$, et $f(x) = 0$ sinon. Expliciter sa forme canonique de fonction simple et calculer son intégrale de Lebesgue.

---

## Correction détaillée

1. **Forme canonique :**
La fonction $f$ ne prend que trois valeurs : 3, 4 et 0. Les ensembles associés aux valeurs strictement positives sont $A_1 = [-1, 2]$ et $A_2 = [3, 5]$.
Ainsi, la forme canonique est $f = 3 \cdot \mathbf{1}_{A_1} + 4 \cdot \mathbf{1}_{A_2}$.

2. **Mesure des ensembles :**
La mesure de Lebesgue de ces intervalles est :
$\lambda(A_1) = 2 - (-1) = 3$
$\lambda(A_2) = 5 - 3 = 2$

3. **Calcul de l'intégrale :**
Par définition de l'intégrale d'une fonction simple positive :
$$ \int_{\mathbb{R}} f \, d\lambda = 3 \cdot \lambda(A_1) + 4 \cdot \lambda(A_2) = 3 \cdot 3 + 4 \cdot 2 = 9 + 8 = 17 $$
