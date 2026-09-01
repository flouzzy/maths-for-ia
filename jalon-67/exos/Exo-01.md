---
title: "Exercice 1 : Application directe : Intégrale d'une série entière"
difficulty: "$\bigstar\star\star\star\star$"
---

# Exercice 1 : Application directe : Intégrale d'une série entière

**Difficulté :** $\bigstar\star\star\star\star$

## Énoncé

Calculer l'intégrale $\int_0^1 \sum_{n=1}^\infty x^n dx$ en justifiant rigoureusement l'interversion série-intégrale.

## Correction Détaillée

1. Posons pour tout $n \ge 1$ et pour tout $x \in [0, 1]$, $u_n(x) = x^n$.
2. Chaque fonction $u_n$ est continue, donc mesurable (et borélienne) sur $[0, 1]$.
3. Pour tout $x \in [0, 1]$ et tout $n \ge 1$, $u_n(x) \ge 0$. La suite de fonctions est donc positive.
4. D'après le corollaire du théorème de convergence monotone de Beppo Levi pour les séries de fonctions positives, on peut permuter la somme et l'intégrale :
   $$\int_0^1 \left( \sum_{n=1}^\infty x^n \right) dx = \sum_{n=1}^\infty \int_0^1 x^n dx$$
5. Calculons l'intégrale de $u_n$ :
   $$\int_0^1 x^n dx = \left[ \frac{x^{n+1}}{n+1} \right]_0^1 = \frac{1}{n+1}$$
6. La somme devient :
   $$\sum_{n=1}^\infty \frac{1}{n+1} = \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \dots$$
7. On reconnaît la série harmonique (amputée de son premier terme). Or, la série harmonique $\sum \frac{1}{n}$ diverge vers $+\infty$.
8. Par conséquent, $\int_0^1 \sum_{n=1}^\infty x^n dx = +\infty$.
