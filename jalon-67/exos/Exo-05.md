---
title: "Exercice 5 : Interversion délicate"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 5 : Interversion délicate

## Énoncé

Montrer que pour tout espace mesuré $(X, \mathcal{F}, \mu)$, si $f_n \ge 0$ est une suite mesurable et décroissante ($f_n \ge f_{n+1}$), alors $\int \lim f_n d\mu$ n'est pas forcément égale à $\lim \int f_n d\mu$.
Que manque-t-il comme hypothèse pour avoir une "convergence monotone décroissante" valide ? Démontrez-le.

## Correction

1. **Le Contre-exemple :**
Soit l'espace $\mathbb{R}$ muni de la mesure de Lebesgue $\lambda$.
Posons $f_n(x) = \mathbf{1}_{[n, +\infty[}(x)$.
- La suite est positive et mesurable.
- Elle est décroissante : $[n+1, +\infty[ \subset [n, +\infty[$, donc $f_{n+1} \le f_n$.
- La limite ponctuelle : pour tout $x \in \mathbb{R}$, dès que $n > x$, $f_n(x) = 0$. Donc la limite est la fonction constante $f(x) = 0$.
- Calculons les intégrales : $\int_{\mathbb{R}} f_n d\lambda = \int_n^{+\infty} 1 dx = +\infty$. Donc $\lim \int f_n = +\infty$.
- Mais l'intégrale de la limite : $\int_{\mathbb{R}} 0 d\lambda = 0$.
L'égalité est fausse ($0 \neq +\infty$).

2. **Théorème de convergence décroissante :**
L'hypothèse manquante pour sauver le résultat est l'existence d'une **masse initiale finie**. Il faut supposer qu'il existe un rang $k$ tel que $\int_X f_k d\mu < +\infty$.
**Preuve :**
Supposons, sans perte de généralité, que $\int f_1 < +\infty$.
Puisque $0 \le f_n \le f_1$, on sait que $\int f_n$ est finie pour tout $n$.
On construit alors la suite de fonctions $g_n = f_1 - f_n$.
Puisque $f_n$ est décroissante, la suite $(g_n)$ est **croissante**, positive, mesurable.
De plus, $\lim_{n \to \infty} g_n = f_1 - \lim_{n \to \infty} f_n = f_1 - f$.
On peut appliquer Beppo Levi à la suite $(g_n)$ :
$$ \int_X (f_1 - f) d\mu = \lim_{n \to \infty} \int_X (f_1 - f_n) d\mu $$
Puisque $\int f_1 < +\infty$, par linéarité de l'intégrale (les quantités infinies ne créent pas de formes indéterminées $\infty - \infty$) :
$$ \int_X f_1 d\mu - \int_X f d\mu = \int_X f_1 d\mu - \lim_{n \to \infty} \int_X f_n d\mu $$
On retranche $\int f_1$ des deux côtés (opération valide car le terme est fini), ce qui donne :
$$ \int_X f d\mu = \lim_{n \to \infty} \int_X f_n d\mu. $$
La démonstration est ainsi rigoureusement établie.
