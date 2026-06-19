---
uuid: "exo-7-5"
title: "Exo 5 - Jalon 7"
---

# Exercice 5 : Extraction de bases

## Énoncé
Soit $E = \mathbb{R}^3$. On considère la famille de vecteurs :
$v_1 = (1, 1, 0)$, $v_2 = (0, 1, 1)$, $v_3 = (1, 2, 1)$, $v_4 = (1, 0, -1)$.
Extraire de cette famille une base de $E$.

## Correction
Il s'agit d'étudier le rang de cette famille.
On remarque que $v_3 = v_1 + v_2$. La famille $(v_1, v_2, v_3, v_4)$ est donc liée, et $Vect(v_1, v_2, v_3, v_4) = Vect(v_1, v_2, v_4)$.
Étudions la liberté de $(v_1, v_2, v_4)$.
Soient $\lambda, \mu, \gamma \in \mathbb{R}$ tels que $\lambda v_1 + \mu v_2 + \gamma v_4 = 0_E$.
Cela conduit au système :
1. $\lambda + \gamma = 0$
2. $\lambda + \mu = 0$
3. $\mu - \gamma = 0$

De (1), $\gamma = -\lambda$. De (2), $\mu = -\lambda$.
En injectant dans (3) : $-\lambda - (-\lambda) = 0$, soit $0 = 0$.
Le système admet une infinité de solutions (ex: $\lambda = 1, \mu = -1, \gamma = -1$).
En effet, $v_1 - v_2 - v_4 = (1,1,0) - (0,1,1) - (1,0,-1) = (0,0,0)$.
La famille est liée. On a $v_4 = v_1 - v_2$.
L'espace engendré est donc de dimension 2 : $Vect(v_1, v_2)$.
Comme $v_1$ et $v_2$ ne sont pas colinéaires (leurs coordonnées ne sont pas proportionnelles), ils forment une famille libre.
La sous-famille $(v_1, v_2)$ est donc une base de l'espace engendré par les 4 vecteurs (qui est un plan de $\mathbb{R}^3$, pas $\mathbb{R}^3$ tout entier).
