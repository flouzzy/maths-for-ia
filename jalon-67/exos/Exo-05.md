---
uuid: "jalon-67-exo-05"
title: "Exercice 05 - Intégrale de Gauss modifiée"
difficulty: "\bigstar\bigstar\bigstar\star\star"
---

# Exercice 05 - Intégrale de Gauss modifiée

## Énoncé

Montrer que $\int_0^\infty \sum_{n=1}^\infty \frac{x^{2n}}{(2n)!} e^{-x} dx$ est divergente.

## Correction Détaillée

1. **Identification de la série :**
La série des $u_n(x) = \frac{x^{2n}}{(2n)!} e^{-x}$ est une série de fonctions positives et mesurables.
On peut appliquer le corollaire du TCM et intervertir somme et intégrale :
$$\int_0^\infty \sum_{n=1}^\infty u_n(x) dx = \sum_{n=1}^\infty \int_0^\infty \frac{x^{2n}}{(2n)!} e^{-x} dx$$

2. **Calcul de l'intégrale individuelle :**
On reconnaît l'intégrale Gamma : $\int_0^\infty x^{k} e^{-x} dx = \Gamma(k+1) = k!$.
Ici, pour $k = 2n$, l'intégrale vaut $(2n)!$.
Ainsi, $\int_0^\infty u_n(x) dx = \frac{(2n)!}{(2n)!} = 1$.

3. **Conclusion :**
La somme de la série des intégrales est $\sum_{n=1}^\infty 1 = +\infty$.
La fonction somme (qui est $\cosh(x) - 1$) multipliée par $e^{-x}$ se comporte asymptotiquement comme $\frac{1}{2} e^{x} e^{-x} = 1/2$, dont l'intégrale sur $\mathbb{R}^+$ diverge.
Le TCM confirme formellement que l'intégrale de cette somme infinie est bien $+\infty$.
