---
uuid: "jalon-67-exo-02"
title: "Exercice 02 - Interversion série-intégrale classique"
difficulty: "\bigstar\bigstar\star\star\star"
---

# Exercice 02 - Interversion série-intégrale classique

## Énoncé

Calculer rigoureusement l'intégrale suivante :
$$\int_0^1 \sum_{k=1}^\infty \frac{x^{k-1}}{(1+x)^k} dx$$

## Correction Détaillée

1. **Identification de la série :**
La série $\sum_{k=1}^\infty \frac{x^{k-1}}{(1+x)^k}$ peut s'écrire comme $\frac{1}{1+x} \sum_{k=0}^\infty \left( \frac{x}{1+x} \right)^k$.
Les fonctions sont mesurables et strictement positives sur $(0, 1)$, on peut appliquer le corollaire du TCM.

2. **Somme de la série géométrique :**
Pour $x \in (0, 1)$, la raison $q = \frac{x}{1+x}$ est strictement comprise entre 0 et 1.
La somme de la série géométrique est $\frac{1}{1 - \frac{x}{1+x}} = \frac{1}{\frac{1}{1+x}} = 1+x$.

3. **Calcul de la limite simple :**
La fonction limite (la somme totale) $f(x)$ est donc $f(x) = \frac{1}{1+x} \times (1+x) = 1$.

4. **Conclusion par le TCM :**
Par le corollaire du TCM (sommation de fonctions positives), l'intégrale de la série est l'intégrale de la limite :
$$\int_0^1 \left( \sum_{k=1}^\infty \frac{x^{k-1}}{(1+x)^k} \right) dx = \int_0^1 1 dx = 1.$$
