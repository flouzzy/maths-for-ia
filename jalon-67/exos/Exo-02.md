# Exercice 2 : Série de fonctions et Beppo-Levi

**Difficulté :** $\bigstar$$\star$$\star$$\star$$\star$

## Énoncé
Montrer que $\int_0^1 \left( \sum_{n=1}^\infty x^n \right) dx = \sum_{n=1}^\infty \frac{1}{n+1} = +\infty$ en justifiant soigneusement chaque étape.

## Correction Détaillée
1. Soit $u_n(x) = x^n$. Ces fonctions sont positives ou nulles sur $[0, 1]$.
2. Par le corollaire du TCM (sommation de Beppo-Levi), $\int \sum u_n = \sum \int u_n$.
3. On calcule $\int_0^1 x^n dx = \frac{1}{n+1}$. La série harmonique diverge.
