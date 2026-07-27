---
title: "Exercice 6 : Espace des polynômes et produit scalaire avec dérivation"
difficulty: 3
---

## Énoncé Formel et Typage Rigoureux
Soit $\mathbb{K}$ un corps commutatif (typiquement $\mathbb{R}$ ou $\mathbb{C}$) et $E$ un $\mathbb{K}$-espace vectoriel. L'enjeu est d'éprouver la consistance algébrique des formes bilinéaires.
Soit $E = \mathbb{R}[X]$ l'espace vectoriel des polynômes à coefficients réels.
Pour tout $P, Q \in E$, on pose :
$$\langle P, Q \rangle = P(0)Q(0) + \int_0^1 P'(t)Q'(t) dt$$
1. Démontrer que $\langle \cdot, \cdot \rangle$ définit un produit scalaire sur $E$.
2. Soient $P_0(X) = 1$ et $P_1(X) = X$. Calculer $\langle P_0, P_1 \rangle$. Ces polynômes sont-ils orthogonaux ?

## Preuve Analytique Pas-à-Pas (Zéro Ellipse)
La démarche déductive exige une formalisation intégrale sans ellipse.
**1. Démonstration du produit scalaire :**
Il faut vérifier que l'application est une forme bilinéaire symétrique définie positive.
Soient $P, Q, R \in E$ et $\lambda \in \mathbb{R}$.

**Symétrie :**
$\langle Q, P \rangle = Q(0)P(0) + \int_0^1 Q'(t)P'(t) dt$
Par commutativité du produit de réels :
$\langle Q, P \rangle = P(0)Q(0) + \int_0^1 P'(t)Q'(t) dt = \langle P, Q \rangle$.
L'application est bien symétrique.

**Bilinéarité :**
(Puisque c'est symétrique, on vérifie seulement la linéarité à gauche).
$\langle \lambda P + R, Q \rangle = (\lambda P + R)(0)Q(0) + \int_0^1 (\lambda P + R)'(t)Q'(t) dt$
Par linéarité de l'évaluation en 0 et de la dérivation :
$\langle \lambda P + R, Q \rangle = (\lambda P(0) + R(0))Q(0) + \int_0^1 (\lambda P'(t) + R'(t))Q'(t) dt$
$\langle \lambda P + R, Q \rangle = \lambda P(0)Q(0) + R(0)Q(0) + \int_0^1 (\lambda P'(t)Q'(t) + R'(t)Q'(t)) dt$
Par linéarité de l'intégrale de Riemann :
$\langle \lambda P + R, Q \rangle = \lambda P(0)Q(0) + R(0)Q(0) + \lambda \int_0^1 P'(t)Q'(t) dt + \int_0^1 R'(t)Q'(t) dt$
En regroupant les termes en $\lambda$ :
$\langle \lambda P + R, Q \rangle = \lambda \left[ P(0)Q(0) + \int_0^1 P'(t)Q'(t) dt \right] + \left[ R(0)Q(0) + \int_0^1 R'(t)Q'(t) dt \right]$
$\langle \lambda P + R, Q \rangle = \lambda \langle P, Q \rangle + \langle R, Q \rangle$.
L'application est une forme bilinéaire.

**Positivité :**
Pour tout $P \in E$ :
$\langle P, P \rangle = (P(0))^2 + \int_0^1 (P'(t))^2 dt$
Un carré dans $\mathbb{R}$ est toujours positif ou nul. De plus, l'intégrale d'une fonction continue et positive (ici $t \mapsto (P'(t))^2$) est positive ou nulle.
Donc $\langle P, P \rangle \ge 0$. La forme est positive.

**Caractère défini :**
Supposons que $\langle P, P \rangle = 0$.
Alors $(P(0))^2 + \int_0^1 (P'(t))^2 dt = 0$.
Il s'agit d'une somme de deux termes positifs ou nuls. Pour que leur somme soit nulle, il est nécessaire que chaque terme soit nul :
- $(P(0))^2 = 0 \implies P(0) = 0$.
- $\int_0^1 (P'(t))^2 dt = 0$.
La fonction $t \mapsto (P'(t))^2$ est continue sur $[0,1]$ (car tout polynôme est de classe $C^\infty$) et positive. Son intégrale est nulle, ce qui implique que la fonction est identiquement nulle sur $[0,1]$.
Donc $\forall t \in [0, 1], (P'(t))^2 = 0 \implies P'(t) = 0$.
Si $P'(t) = 0$ sur l'intervalle $[0, 1]$, puisque $P'$ est un polynôme, il possède une infinité de racines, donc $P'$ est le polynôme nul ($P' = 0$).
Si la dérivée est le polynôme nul, alors le polynôme $P$ est une constante : $P(X) = C$.
Comme on a déjà établi que $P(0) = 0$, on en déduit que $C = 0$.
Finalement, $P(X) = 0$.
La forme est définie positive, c'est donc bien un produit scalaire.

**2. Calcul orthogonalité :**
$P_0(X) = 1 \implies P_0(0) = 1, P_0'(X) = 0$.
$P_1(X) = X \implies P_1(0) = 0, P_1'(X) = 1$.
Calcul de $\langle P_0, P_1 \rangle$ :
$\langle P_0, P_1 \rangle = P_0(0)P_1(0) + \int_0^1 P_0'(t)P_1'(t) dt$
$\langle P_0, P_1 \rangle = (1)(0) + \int_0^1 (0)(1) dt = 0 + 0 = 0$.
Leur produit scalaire est nul, donc **oui**, ces polynômes sont orthogonaux par rapport à ce produit scalaire.
