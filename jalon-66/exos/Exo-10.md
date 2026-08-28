---
uuid: "jalon-66-exo-10"
title: "Exercice 10 - Jalon 66"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 10 : Lemme de Borel-Cantelli via l'intégrale de Lebesgue

**Énoncé :**
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. Soit $(A_n)_{n \ge 1}$ une suite de sous-ensembles mesurables de $X$.
On suppose que la série des mesures converge : $\sum_{n=1}^{+\infty} \mu(A_n) < +\infty$.
On définit l'ensemble $A = \limsup_{n \to +\infty} A_n$, c'est-à-dire l'ensemble des $x \in X$ qui appartiennent à une infinité d'ensembles $A_n$.
En utilisant la fonction positive $f(x) = \sum_{n=1}^{+\infty} \mathbf{1}_{A_n}(x)$, démontrer que $\mu(A) = 0$.

**Corrigé :**
C'est la première partie du célèbre lemme de Borel-Cantelli, central en probabilités. La puissance de l'intégrale de Lebesgue pour les séries de fonctions positives rend sa preuve d'une élégance absolue.

**1. Interprétation de la fonction $f$ :**
Pour chaque $x \in X$, la valeur de $\mathbf{1}_{A_n}(x)$ est soit 0, soit 1.
La somme $f(x) = \sum_{n=1}^{+\infty} \mathbf{1}_{A_n}(x)$ compte exactement le nombre d'ensembles $A_n$ auxquels $x$ appartient.
$f$ est une fonction mesurable à valeurs dans $[0, +\infty]$ (comme limite de la suite croissante de sommes partielles de fonctions mesurables).

**2. Caractérisation de l'ensemble $\limsup A_n$ :**
Si $x \in A = \limsup A_n$, cela signifie que $x$ appartient à une infinité d'ensembles $A_n$.
Donc la somme $f(x)$ contient une infinité de termes égaux à 1.
Par conséquent, $f(x) = +\infty$.
Ainsi, $A \subset \{ x \in X \mid f(x) = +\infty \}$.

**3. Calcul de l'intégrale de $f$ :**
Par le théorème d'interversion pour les séries à termes positifs (corollaire direct du théorème de convergence monotone), l'intégrale de la somme infinie est la somme infinie des intégrales :
$$\int_X f \, d\mu = \int_X \left( \sum_{n=1}^{+\infty} \mathbf{1}_{A_n} \right) d\mu = \sum_{n=1}^{+\infty} \int_X \mathbf{1}_{A_n} \, d\mu$$
L'intégrale d'une indicatrice est la mesure de l'ensemble :
$$\int_X f \, d\mu = \sum_{n=1}^{+\infty} \mu(A_n)$$
Par hypothèse, cette série est convergente, donc sa somme est finie.
$$\int_X f \, d\mu < +\infty$$

**4. Conclusion sur la mesure de $A$ :**
Nous avons trouvé une fonction positive $f$ dont l'intégrale est finie.
Une fonction d'intégrale finie ne peut valoir $+\infty$ que sur un ensemble de mesure nulle.
Prouvons-le formellement :
Pour tout entier $M > 0$, soit $E_\infty = \{ x \in X \mid f(x) = +\infty \}$.
On a $f(x) \ge M \cdot \mathbf{1}_{E_\infty}(x)$ pour tout $x$.
En intégrant :
$$\int_X f \, d\mu \ge M \cdot \mu(E_\infty)$$
Puisque l'intégrale est finie (notons-la $I$), on a $\mu(E_\infty) \le I / M$.
En faisant tendre $M \to +\infty$, on obtient $\mu(E_\infty) = 0$.

Comme $A \subset E_\infty$, par monotonie de la mesure :
$\mu(A) \le \mu(E_\infty) = 0$.
Donc $\mu(A) = 0$.
La probabilité qu'une infinité d'événements se réalisent est nulle si la somme de leurs probabilités est finie.
