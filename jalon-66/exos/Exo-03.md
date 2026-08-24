---
title: "Exercice 03 : Intégrabilité de l'indicatrice de Cantor"
difficulty: "$\bigstar\bigstar\star\star\star$"
---

# Exercice 03 : Intégrabilité de l'indicatrice de Cantor

**Difficulté :** $\bigstar\bigstar\star\star\star$

## Énoncé

Soit $C$ l'ensemble triadique de Cantor dans $[0,1]$. Montrer que la fonction indicatrice $\mathbf{1}_C$ est mesurable, calculer son intégrale de Lebesgue par rapport à $\lambda$, et conclure quant à son intégrabilité.

---

## Correction détaillée

1. **Mesurabilité de $\mathbf{1}_C$ :**
L'ensemble de Cantor $C$ est un compact de $[0, 1]$ (car fermé et borné). En tant que fermé, $C$ est un borélien. L'indicatrice d'un ensemble mesurable est une fonction mesurable.

2. **Calcul de l'intégrale :**
La fonction $\mathbf{1}_C$ est elle-même une fonction simple positive. Par définition :
$$ \int_{[0,1]} \mathbf{1}_C \, d\lambda = 1 \cdot \lambda(C) + 0 \cdot \lambda([0,1] \setminus C) = \lambda(C) $$

3. **Mesure de l'ensemble de Cantor :**
L'ensemble de Cantor est construit par suppression successive du tiers central ouvert. Au $n$-ième pas, il reste $2^n$ intervalles de longueur $(1/3)^n$. La mesure de Lebesgue totale au $n$-ième pas est $(2/3)^n$.
Comme $C$ est l'intersection de ces compacts emboîtés, sa mesure est la limite : $\lambda(C) = \lim_{n \to \infty} \left(\frac{2}{3}\right)^n = 0$.

4. **Conclusion :**
L'intégrale vaut 0. La fonction est intégrable (intégrale finie), et comme l'intégrale d'une fonction positive est nulle, $\mathbf{1}_C = 0$ presque partout.
