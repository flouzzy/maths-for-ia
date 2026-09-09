---
title: "Exercice 2 : TCM"
difficulty: "★☆☆☆☆"
---
# Exercice 2 : Série géométrique et TCM

**Niveau :** $\bigstar\star\star\star\star$

**Énoncé :**
Calculer $\int_0^1 \sum_{n=0}^{+\infty} (x/2)^n dx$ en justifiant rigoureusement le calcul.

**Correction détaillée :**
1. Posons $u_n(x) = (x/2)^n$. Pour $x \in [0, 1]$, on a $u_n(x) \ge 0$.
2. D'après le corollaire du théorème de convergence monotone pour les séries à termes positifs, on peut intervertir série et intégrale.
3. $\int_0^1 \sum_{n=0}^{+\infty} (x/2)^n dx = \sum_{n=0}^{+\infty} \int_0^1 (x/2)^n dx$.
4. Calculons l'intégrale : $\int_0^1 (x/2)^n dx = \frac{1}{2^n} \left[ \frac{x^{n+1}}{n+1} \right]_0^1 = \frac{1}{2^n(n+1)}$.
5. La série devient $\sum_{n=0}^{+\infty} \frac{1}{2^n(n+1)} = 2 \sum_{n=0}^{+\infty} \frac{(1/2)^{n+1}}{n+1} = -2 \ln(1 - 1/2) = 2\ln(2)$.
