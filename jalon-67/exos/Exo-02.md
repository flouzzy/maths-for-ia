# Exercice 2 : Somme de probabilités géométriques \quad $\bigstar\bigstar\star\star\star$

## Énoncé
Soit $\mu$ la mesure de comptage sur $\mathbb{N}$. Calculer $\int_{\mathbb{N}} f d\mu$ où $f(n) = p(1-p)^n$ avec $p \in ]0, 1[$.

## Correction Détaillée
On a $f(n) = p(1-p)^n > 0$. L'intégrale par rapport à la mesure de comptage est la série numérique $\sum_{n=0}^\infty f(n)$.
Ainsi, $\int_{\mathbb{N}} f d\mu = \sum_{n=0}^\infty p(1-p)^n = p \frac{1}{1-(1-p)} = p \times \frac{1}{p} = 1$.
On retrouve le fait que c'est une distribution de probabilité.
