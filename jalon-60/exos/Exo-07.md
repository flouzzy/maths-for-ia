---
title: "Exercice 7 : Approximation de la fonction carrée en norme infinie"
difficulty: $\bigstar\bigstar\bigstar\bigstar\star$
---

# Exercice 7 : Approximation de la fonction carrée en norme infinie

## Énoncé

En utilisant la base de fonctions chapeaux $\Delta_k(x)$ introduite dans le cours, majorer précisément l'erreur d'approximation uniforme $\sup_{x \in [-1, 1]} |x^2 - G_N(x)|$ où $G_N$ est l'interpolateur linéaire aux points nodaux équirépartis de pas $h = \frac{2}{N}$.

## Correction Rigoureuse

**Étape 1 : Expression de l'interpolateur**
Soit $f(x) = x^2$. L'interpolateur linéaire sur le segment $I_k = [x_k, x_{k+1}]$ est la droite passant par $(x_k, x_k^2)$ et $(x_{k+1}, x_{k+1}^2)$.
L'équation de cette droite est :
$$L_k(x) = x_k^2 + \frac{x_{k+1}^2 - x_k^2}{x_{k+1} - x_k} (x - x_k) = x_k^2 + (x_{k+1} + x_k)(x - x_k)$$

**Étape 2 : Étude de l'erreur d'interpolation locale**
Sur l'intervalle $I_k$, l'erreur est $E_k(x) = x^2 - L_k(x)$.
$E_k(x) = x^2 - x_k^2 - (x_{k+1} + x_k)(x - x_k) = (x - x_k)(x + x_k) - (x_{k+1} + x_k)(x - x_k) = (x - x_k)(x - x_{k+1})$

**Étape 3 : Maximisation de l'erreur**
La fonction $E_k(x)$ est une parabole dont les racines sont $x_k$ et $x_{k+1}$. Son maximum absolu sur l'intervalle est atteint au milieu $x_m = \frac{x_k + x_{k+1}}{2}$.
La valeur absolue de ce maximum est :
$$|E_k(x_m)| = \left| \left(\frac{x_{k+1} - x_k}{2}\right) \left(\frac{x_k - x_{k+1}}{2}\right) \right| = \left| -\frac{h^2}{4} \right| = \frac{h^2}{4}$$

**Étape 4 : Erreur globale**
Puisque le pas est $h = \frac{2}{N}$, on obtient :
$$\sup_{x \in [-1, 1]} |f(x) - G_N(x)| = \frac{1}{4} \left(\frac{2}{N}\right)^2 = \frac{1}{N^2}$$
Le théorème est validé par cette borne asymptotique $\mathcal{O}(N^{-2})$. $\blacksquare$
