# Exercice 1 : Limite d'une intégrale simple

**Difficulté :** $\bigstar$$\star$$\star$$\star$$\star$

## Énoncé
Soit $f_n(x) = x^n$ sur $[0, 1[$. Calculer $\lim_{n \to \infty} \int_{[0, 1[} f_n(x) dx$ sans intervertir, puis vérifier que le théorème de Beppo-Levi s'applique bien.

## Correction Détaillée
1. On a $f_n(x) = x^n$. L'intégrale est $\int_0^1 x^n dx = \frac{1}{n+1}$, dont la limite est 0.
2. La suite $(f_n)$ est décroissante, donc Beppo-Levi (pour les suites croissantes) ne s'applique pas directement. C'est le théorème de convergence dominée (ou Lebesgue) qui s'applique, car $f_n \le 1$.
