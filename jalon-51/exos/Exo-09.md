---
title: "Exercice 9 : Complétude et suite de Cauchy"
---

### Exercice 9 : Complétude et suite de Cauchy \quad $\bigstar\bigstar\bigstar\bigstar\bigstar$

**Énoncé :**
Dans un espace métrique $(X, d)$, on considère une suite $(x_n)$ telle que la série $\sum d(x_n, x_{n+1})$ est convergente. Démontrer que la suite $(x_n)$ est une suite de Cauchy.

**Correction Détaillée :**
Pour montrer que la suite $(x_n)$ est de Cauchy, nous devons prouver que la distance entre $x_p$ et $x_q$ tend vers zéro lorsque $p$ et $q$ tendent vers l'infini indépendamment. Soit $\epsilon > 0$.
Soient $p, q$ deux entiers naturels avec $q > p$. En appliquant itérativement l'inégalité triangulaire de l'espace métrique, nous avons :
$$d(x_p, x_q) \le d(x_p, x_{p+1}) + d(x_{p+1}, x_{p+2}) + \dots + d(x_{q-1}, x_q)$$
Ce qui peut s'écrire formellement comme une somme partielle :
$$d(x_p, x_q) \le \sum_{k=p}^{q-1} d(x_k, x_{k+1})$$
Or, par hypothèse, la série de terme général positif $u_n = d(x_n, x_{n+1})$ est convergente. Soit $S$ sa somme totale. Les sommes partielles $S_n = \sum_{k=0}^{n} u_k$ convergent vers $S$.
La somme $\sum_{k=p}^{q-1} d(x_k, x_{k+1})$ correspond exactement à la différence de deux sommes partielles : $S_{q-1} - S_{p-1}$.
Puisque la suite des sommes partielles $(S_n)$ est convergente, elle est elle-même une suite de Cauchy réelle. Il existe donc un rang $N$ tel que pour tous entiers $q > p > N$, on ait :
$$|S_{q-1} - S_{p-1}| < \epsilon$$
Comme les termes sont positifs, cela implique que la somme entre $p$ et $q-1$ est strictement inférieure à $\epsilon$.
Par conséquent, pour tous $q > p > N$ :
$$d(x_p, x_q) \le \sum_{k=p}^{q-1} d(x_k, x_{k+1}) < \epsilon$$
Ceci est exactement la définition d'une suite de Cauchy dans l'espace métrique $(X, d)$. La finitude de la somme des distances de sauts (analogue à la longueur finie d'une courbe en analyse métrique discrète) garantit le caractère de Cauchy de la suite.
