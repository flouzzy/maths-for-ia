---
uuid: "exo-7-7"
title: "Exo 7 - Jalon 7"
---

# Exercice 7 : Familles de polynômes

## Énoncé
Dans l'espace $\mathbb{R}_2[X]$, on considère les polynômes :
$P_1 = 1 + X + X^2$, $P_2 = 1 - X + X^2$, $P_3 = 1 + X - X^2$.
Montrer que $(P_1, P_2, P_3)$ est une base de $\mathbb{R}_2[X]$ et trouver les coordonnées du polynôme $P = 1$ dans cette base.

## Correction
**Preuve de base :**
L'espace $\mathbb{R}_2[X]$ est de dimension 3. La famille comportant 3 vecteurs, il suffit de montrer qu'elle est libre.
Soient $a, b, c \in \mathbb{R}$ tels que $aP_1 + bP_2 + cP_3 = 0$.
$a(1+X+X^2) + b(1-X+X^2) + c(1+X-X^2) = 0$
En regroupant les termes :
$(a+b+c) + (a-b+c)X + (a+b-c)X^2 = 0$
Par identification des coefficients avec le polynôme nul :
1. $a+b+c = 0$
2. $a-b+c = 0$
3. $a+b-c = 0$

(1) - (2) donne $2b = 0 \implies b = 0$.
(1) - (3) donne $2c = 0 \implies c = 0$.
On déduit $a = 0$. La famille est libre, c'est donc une base.

**Coordonnées de P=1 :**
On cherche $x, y, z$ tels que $xP_1 + yP_2 + zP_3 = 1$.
1. $x+y+z = 1$
2. $x-y+z = 0$
3. $x+y-z = 0$

(1) - (2) $\implies 2y = 1 \implies y = 1/2$.
(1) - (3) $\implies 2z = 1 \implies z = 1/2$.
En reportant dans (1) : $x + 1/2 + 1/2 = 1 \implies x = 0$.
Les coordonnées de $P$ dans la base $(P_1, P_2, P_3)$ sont $(0, 1/2, 1/2)$.
