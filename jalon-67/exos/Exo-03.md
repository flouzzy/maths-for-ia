---
title: "Exercice 3 : TCM"
difficulty: "★★☆☆☆"
---
# Exercice 3 : Limite d'exponentielles tronquées

**Niveau :** $\bigstar\bigstar\star\star\star$

**Énoncé :**
Soit $f_n(x) = \left(1 + \frac{x}{n}\right)^n e^{-2x}$ pour $x > 0$. Évaluer $\lim_{n \to +\infty} \int_0^{+\infty} f_n(x) \mathbf{1}_{[0, n]}(x) dx$.

**Correction détaillée :**
1. Soit $g_n(x) = f_n(x) \mathbf{1}_{[0, n]}(x)$. On sait que pour $x > 0$, la suite $u_n(x) = \left(1 + \frac{x}{n}\right)^n$ est croissante (par l'inégalité de Bernoulli ou l'étude de la dérivée) et converge vers $e^x$.
2. Ainsi, la suite de fonctions $g_n(x)$ est positive et croissante. Sa limite simple est $g(x) = e^x e^{-2x} = e^{-x}$.
3. Le théorème de convergence monotone s'applique : $\lim_{n \to \infty} \int_0^{+\infty} g_n(x) dx = \int_0^{+\infty} e^{-x} dx$.
4. Le calcul donne $\int_0^{+\infty} e^{-x} dx = \left[-e^{-x}\right]_0^{+\infty} = 1$.
