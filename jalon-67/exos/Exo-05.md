# Exercice 5 : Démonstration du Lemme de Borel-Cantelli via Beppo Levi \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Soit $(A_n)$ une suite d'ensembles mesurables telle que $\sum_{n=1}^\infty \mu(A_n) < +\infty$. Démontrer que presque tous les points de $X$ appartiennent à un nombre fini de $A_n$.

## Correction Détaillée
On définit la fonction $f(x) = \sum_{n=1}^\infty \chi_{A_n}(x)$, qui représente le nombre d'ensembles $A_n$ auxquels le point $x$ appartient.
Les fonctions $\chi_{A_n}$ sont positives et mesurables.
Par le corollaire de Beppo Levi, on peut intégrer terme à terme :
$$\int_X f d\mu = \int_X \left(\sum_{n=1}^\infty \chi_{A_n}\right) d\mu = \sum_{n=1}^\infty \int_X \chi_{A_n} d\mu = \sum_{n=1}^\infty \mu(A_n)$$
Par hypothèse, cette somme est finie (notons-la $M < +\infty$).
Ainsi, $\int_X f d\mu < +\infty$.
Or, l'intégrale d'une fonction positive est finie si et seulement si la fonction est finie presque partout.
Donc, $f(x) < +\infty$ pour presque tout $x \in X$, ce qui signifie exactement que presque tout point appartient à un nombre fini d'ensembles $A_n$.
