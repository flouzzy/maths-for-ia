---
title: "Exercice 1 : Série Alternée (Semi-convergence)"
difficulty: ★☆☆☆☆
---
# Exercice 1 : Série Alternée (Semi-convergence)

## Énoncé
Étudier la convergence et la convergence absolue de la série harmonique alternée $\sum_{n=1}^\infty \frac{(-1)^n}{n}$.

## Correction
1. **Convergence Absolue :** La série des valeurs absolues est $\sum |\frac{(-1)^n}{n}| = \sum \frac{1}{n}$.
   - C'est la série harmonique (Riemann $\alpha=1$). On sait que cette série diverge (minorée par une intégrale divergente, ou par regroupement de termes).
   - La série initiale ne converge donc **pas absolument**.
2. **Convergence Simple (Critère des séries alternées) :** Soit $u_n = \frac{(-1)^n}{n}$.
   - Posons $a_n = |u_n| = 1/n$.
   - La suite $(a_n)_{n\ge 1}$ est positive.
   - Elle est décroissante : pour tout $n \ge 1$, $n+1 > n \implies \frac{1}{n+1} < \frac{1}{n} \implies a_{n+1} < a_n$.
   - Elle converge vers 0 : $\lim_{n\to\infty} \frac{1}{n} = 0$.
   - D'après le théorème de Leibniz (critère spécial des séries alternées), la série $\sum u_n$ converge.
**Conclusion :** La série converge mais pas absolument, elle est donc **semi-convergente**.
