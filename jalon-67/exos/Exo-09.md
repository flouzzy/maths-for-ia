# Exercice 9 : Application à l'espérance de variables aléatoires (IA)
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé

Soit $X \geq 0$ une variable aléatoire continue de densité $f$. Montrer en utilisant le TCM que $\mathbb{E}[X] = \int_0^\infty \mathbb{P}(X > x) dx$.

## Correction Détaillée

On part de la définition : $\mathbb{E}[X] = \int_0^\infty x f(x) dx$.
On peut écrire $x = \int_0^x 1 dt$. Donc :
$$\mathbb{E}[X] = \int_0^\infty \left( \int_0^x dt \right) f(x) dx$$
Introduisons la fonction indicatrice $\mathbf{1}_{t < x}$.
$$\mathbb{E}[X] = \int_0^\infty \left( \int_0^\infty \mathbf{1}_{t < x} dt \right) f(x) dx$$
Les fonctions sont toutes positives. Par le théorème de Fubini-Tonelli (qui repose lui-même sur Beppo-Levi par construction), on peut intervertir les intégrales :
$$\mathbb{E}[X] = \int_0^\infty \left( \int_0^\infty \mathbf{1}_{x > t} f(x) dx \right) dt$$
Or, $\int_0^\infty \mathbf{1}_{x > t} f(x) dx = \int_t^\infty f(x) dx = \mathbb{P}(X > t)$.
En substituant, on obtient :
$$\mathbb{E}[X] = \int_0^\infty \mathbb{P}(X > t) dt$$
Ce résultat est fondamental en théorie de la fiabilité et en IA pour l'analyse de survie.
