---
uuid: "exo-7-9"
title: "Exo 9 - Jalon 7"
---

# Exercice 9 : Espaces de suites

## Énoncé
Soit $E$ l'espace des suites réelles. On considère l'ensemble $F$ des suites $(u_n)$ vérifiant la relation de récurrence :
$\forall n \in \mathbb{N}, u_{n+2} = 5u_{n+1} - 6u_n$.
Montrer que $F$ est un espace vectoriel et déterminer sa dimension.

## Correction
**Structure d'espace vectoriel :**
La suite nulle vérifie la relation, donc $0_E \in F$.
Soient $u, v \in F$ et $\lambda \in \mathbb{R}$. Posons $w = \lambda u + v$.
$\forall n, w_{n+2} = \lambda u_{n+2} + v_{n+2}$
$= \lambda(5u_{n+1} - 6u_n) + (5v_{n+1} - 6v_n)$
$= 5(\lambda u_{n+1} + v_{n+1}) - 6(\lambda u_n + v_n)$
$= 5w_{n+1} - 6w_n$.
Donc $w \in F$. $F$ est un sous-espace vectoriel de $E$.

**Dimension et base :**
Il s'agit d'une récurrence linéaire d'ordre 2. Son équation caractéristique est :
$r^2 - 5r + 6 = 0$.
Les racines sont $r_1 = 2$ et $r_2 = 3$.
On sait (théorie des suites récurrentes) que toute solution s'écrit sous la forme :
$u_n = \lambda 2^n + \mu 3^n$ avec $\lambda, \mu \in \mathbb{R}$.
Posons $e_1$ la suite définie par $e_{1,n} = 2^n$ et $e_2$ la suite $e_{2,n} = 3^n$.
La formule montre que $(e_1, e_2)$ engendre $F$.
Montrons qu'elle est libre. Soient $\lambda, \mu$ tels que $\lambda e_1 + \mu e_2 = 0$.
Cela doit valoir 0 pour tout $n$.
Pour $n=0$ : $\lambda + \mu = 0$
Pour $n=1$ : $2\lambda + 3\mu = 0$
La résolution de ce système s'effectue ainsi : de la première équation on déduit $\mu = -\lambda$. En substituant dans la seconde, on obtient $2\lambda - 3\lambda = 0$, soit $-\lambda = 0$ et donc $\lambda = 0$. Il s'ensuit rigoureusement que $\mu = 0$.
La famille $(e_1, e_2)$ est une base de $F$, qui est donc de dimension 2.
