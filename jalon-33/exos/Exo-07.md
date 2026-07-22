# Exercice 7 : Cône isotrope d'une forme quadratique

## Énoncé
Soit $E$ un espace vectoriel réel de dimension $n$ et $q$ une forme quadratique de signature $(s, t)$.
Le **cône isotrope** de $q$ est l'ensemble $C(q) = \{ x \in E \mid q(x) = 0 \}$.
Montrer que $C(q)$ est un sous-espace vectoriel de $E$ si et seulement si $s=0$ ou $t=0$ (c'est-à-dire si la forme garde un signe constant).

## Correction Détaillée (Zéro Ellipse)

Nous devons procéder par double implication.

**Sens $\Leftarrow$ :**
Supposons que $s=0$ ou $t=0$. Sans perte de généralité, supposons $t=0$.
La forme $q$ a pour signature $(s, 0)$, donc dans sa décomposition de Gauss, elle n'a que des carrés affectés d'un signe $+$.
Pour tout $x \in E$, $q(x) = \sum_{i=1}^s \ell_i(x)^2 \ge 0$. La forme est positive.
Nous avons prouvé dans un exercice précédent que pour une forme quadratique positive, le cône isotrope $N(q) = \{x \mid q(x) = 0\}$ est exactement égal au noyau de la forme polaire $\ker(b)$.
Or, le noyau d'une forme bilinéaire, par définition de la linéarité, est toujours un sous-espace vectoriel de $E$.
Donc $C(q) = \ker(b)$ est un sous-espace vectoriel. Le même raisonnement s'applique pour $s=0$ (en considérant $-q$).

**Sens $\Rightarrow$ :**
Supposons par l'absurde que $C(q)$ est un sous-espace vectoriel, mais que ni $s=0$ ni $t=0$ (donc $s \ge 1$ et $t \ge 1$).
Puisque $s \ge 1$ et $t \ge 1$, la décomposition de Gauss de $q$ contient au moins un terme avec un coefficient positif et un terme avec un coefficient négatif.
Par le théorème de réduction simultanée ou d'inertie de Sylvester, on peut trouver une base $B = (e_1, \dots, e_n)$ telle que la matrice de $q$ soit diagonale avec au moins un $1$ et au moins un $-1$ sur la diagonale.
Quitte à réordonner la base, supposons que $q(e_1) = 1$ et $q(e_2) = -1$.
Soit le vecteur $u = e_1 + e_2$. Évaluons $q$ sur ce vecteur. Puisque la base est orthogonale pour $b$ (forme polaire associée, matrice diagonale) :
$$ q(u) = q(e_1 + e_2) = q(e_1) + q(e_2) + 2b(e_1, e_2) $$
Comme la matrice est diagonale, l'élément hors diagonale $b(e_1, e_2)$ est nul.
$$ q(u) = 1 + (-1) + 0 = 0 $$
Donc $u \in C(q)$.
De même, posons le vecteur $v = e_1 - e_2$.
$$ q(v) = q(e_1 - e_2) = q(e_1) + q(-e_2) + 2b(e_1, -e_2) = q(e_1) + (-1)^2 q(e_2) - 2b(e_1, e_2) $$
$$ q(v) = 1 - 1 - 0 = 0 $$
Donc $v \in C(q)$.
Si $C(q)$ était un sous-espace vectoriel, la somme de deux vecteurs de $C(q)$ devrait appartenir à $C(q)$.
Regardons $w = u + v = (e_1 + e_2) + (e_1 - e_2) = 2e_1$.
Évaluons $q$ sur $w$ :
$$ q(w) = q(2e_1) = 2^2 q(e_1) = 4(1) = 4 $$
Comme $4 \neq 0$, le vecteur $w \notin C(q)$.
La somme de deux éléments de $C(q)$ n'est pas dans $C(q)$, ce qui contredit l'hypothèse que $C(q)$ est un sous-espace vectoriel.
L'hypothèse ($s \ge 1$ et $t \ge 1$) est donc absurde.
On conclut que nécessairement, $s=0$ ou $t=0$. $\blacksquare$
