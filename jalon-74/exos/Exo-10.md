---
title: "Exercice 10 : Inégalité de Minkowski pour les intégrales"
difficulty: "$\bigstar\bigstar\bigstar\bigstar\bigstar$"
---

# Exercice 10 : Inégalité de Minkowski pour les intégrales

## Énoncé
Soient $(X, \mu)$ et $(Y, \nu)$ deux espaces mesurés, et $f(x,y)$ une fonction positive mesurable sur $X \times Y$.
Pour $1 \le p < \infty$, montrer que :
$$ \left( \int_X \left( \int_Y f(x,y) d\nu(y) \right)^p d\mu(x) \right)^{1/p} \le \int_Y \left( \int_X f(x,y)^p d\mu(x) \right)^{1/p} d\nu(y) $$

## Corrigé
Posons $F(x) = \int_Y f(x,y) d\nu(y)$. On veut estimer $\|F\|_{L^p(X)}$.
L'intégrale vaut $\int_X F(x)^p d\mu(x) = \int_X F(x) F(x)^{p-1} d\mu(x)$.
En remplaçant $F(x)$, on a : $\int_X \left( \int_Y f(x,y) d\nu(y) \right) F(x)^{p-1} d\mu(x)$.
Par Fubini-Tonelli, on échange les intégrales :
$$ = \int_Y \left( \int_X f(x,y) F(x)^{p-1} d\mu(x) \right) d\nu(y) $$
Pour l'intégrale interne sur $X$, appliquons Hölder avec $p$ et $q$ (tq $(p-1)q = p$) :
$$ \int_X f(x,y) F(x)^{p-1} d\mu(x) \le \left( \int_X f(x,y)^p d\mu(x) \right)^{1/p} \left( \int_X F(x)^{(p-1)q} d\mu(x) \right)^{1/q} $$
$$ = \left( \int_X f(x,y)^p d\mu(x) \right)^{1/p} \|F\|_p^{p/q} $$
En réintégrant sur $Y$ :
$$ \|F\|_p^p \le \int_Y \left( \int_X f(x,y)^p d\mu(x) \right)^{1/p} \|F\|_p^{p/q} d\nu(y) = \|F\|_p^{p/q} \int_Y \left( \int_X f(x,y)^p d\mu(x) \right)^{1/p} d\nu(y) $$
On divise par $\|F\|_p^{p/q}$ (si non nul et fini, sinon on tronque). Comme $p - p/q = 1$, on obtient :
$$ \|F\|_p \le \int_Y \|f(\cdot, y)\|_p d\nu(y) $$
Ce qui est exactement l'inégalité recherchée.
