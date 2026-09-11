# Exercice 4 : Intégration d'une fraction

**Difficulté :** $\bigstar$$\bigstar$$\star$$\star$$\star$

## Énoncé
Calculer $\int_0^1 \frac{\ln(1-x)}{x} dx$ en utilisant le développement en série entière et le théorème de convergence monotone.

## Correction Détaillée
1. $\frac{-\ln(1-x)}{x} = \sum_{n=1}^\infty \frac{x^{n-1}}{n}$. C'est une série à termes positifs.
2. Par Beppo-Levi, l'intégrale de la somme est la somme des intégrales : $\sum \int_0^1 \frac{x^{n-1}}{n} dx = \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$.
3. L'intégrale demandée vaut $-\pi^2/6$.
