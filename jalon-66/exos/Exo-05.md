---
uuid: "jalon-66-exo-05"
title: "Exercice 5 - Jalon 66"
difficulty: "$\bigstar\bigstar\bigstar\star\star$"
---

# Exercice 5 : Croissance stricte presque partout

**Énoncé :**
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré.
Soient $f, g \in \mathcal{M}_+$ telles que $f \le g$ sur $X$.
Montrer que si $\int_X f \, d\mu = \int_X g \, d\mu < +\infty$, alors $f = g$ presque partout.

**Corrigé :**
Puisque $f, g \in \mathcal{M}_+$ et $f \le g$, la fonction différence $h = g - f$ est bien définie (car l'intégrale est finie, donc les valeurs infinies sont sur un ensemble de mesure nulle, qu'on exclut), positive ($h \ge 0$) et mesurable.

Démontrons que $\int_X h \, d\mu = 0$.
Par la propriété d'additivité de l'intégrale pour les fonctions positives (qui sera pleinement démontrée via Beppo-Levi au Jalon 67, mais assumée ici par linéarité) :
$$\int_X g \, d\mu = \int_X (f + (g-f)) \, d\mu = \int_X f \, d\mu + \int_X (g-f) \, d\mu$$
Puisque $\int_X f \, d\mu < +\infty$, nous pouvons soustraire cette quantité finie de part et d'autre :
$$\int_X (g-f) \, d\mu = \int_X g \, d\mu - \int_X f \, d\mu$$
Or par hypothèse, $\int_X f \, d\mu = \int_X g \, d\mu$.
Ainsi :
$$\int_X (g-f) \, d\mu = 0$$

Appliquons maintenant le Théorème 1 (propriété 2 de la nullité) vu dans le cours : l'intégrale d'une fonction mesurable positive est nulle si et seulement si cette fonction est nulle presque partout.
Puisque $g - f$ est positive et son intégrale est nulle, nous avons :
$g - f = 0$ presque partout.
C'est-à-dire :
$\mu(\{x \in X \mid g(x) - f(x) \neq 0\}) = 0$.
Soit $\mu(\{x \in X \mid f(x) \neq g(x)\}) = 0$.
Donc $f = g$ presque partout.
