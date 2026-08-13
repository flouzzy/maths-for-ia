# Exercice 2 : Théorème de conservation de la continuité

## Énoncé
Soit $f_n(x) = x^n$ sur $[0, 1]$.
En utilisant le théorème de conservation de la continuité, prouver que la convergence n'est pas uniforme.

## Correction Détaillée

1. **Limite simple :**
Pour $x \in [0, 1[$, $\lim_{n\to\infty} x^n = 0$.
Pour $x = 1$, $\lim_{n\to\infty} 1^n = 1$.
Donc, la limite simple $f$ est définie par $f(x) = 0$ si $x \in [0, 1[$ et $f(1) = 1$.

2. **Continuité :**
Les fonctions $f_n$ sont des polynômes, donc continues sur $[0, 1]$.
Cependant, la fonction limite $f$ n'est pas continue en $x = 1$, car $\lim_{x \to 1^-} f(x) = 0 \neq f(1) = 1$.

3. **Application du théorème :**
Le théorème énonce que la limite uniforme d'une suite de fonctions continues est continue.
Par contraposée, comme $f$ n'est pas continue, la convergence des $f_n$ continues vers $f$ ne peut pas être uniforme sur $[0, 1]$.
