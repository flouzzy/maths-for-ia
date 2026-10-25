# Exercice 9 : Hahn-Banach analytique sur $\mathbb{R}^n$ $\bigstar\bigstar\bigstar\bigstar\bigstar$

## Énoncé
Prouver le théorème de Hahn-Banach analytique pour l'espace $E = \mathbb{R}^n$ avec une preuve algébrique pure (par induction).

## Correction Complète
Soit $E = \mathbb{R}^n$, $p$ une fonctionnelle sous-linéaire sur $E$, $F$ un sous-espace, et $f$ une forme linéaire sur $F$ telle que $f \leq p$.
On raisonne par récurrence sur la codimension $k$ de $F$ dans $E$.
Si $k=0$, $F=E$, c'est terminé.
Si $k>0$, soit $x_0 \in E \setminus F$. On va prolonger $f$ sur $G = F \oplus \mathbb{R}x_0$ (qui est de dimension $\dim F + 1$).
Tout point de $G$ s'écrit $y = x + t x_0$ avec $x \in F, t \in \mathbb{R}$.
On veut trouver $c \in \mathbb{R}$ tel que le prolongement $g(x + t x_0) = f(x) + t c$ vérifie $g \leq p$ sur $G$.
Il faut donc :
1) Si $t > 0$, $f(x) + tc \leq p(x + t x_0) \iff c \leq \frac{1}{t}(p(x + t x_0) - f(x)) \iff c \leq p(x/t + x_0) - f(x/t)$.
2) Si $t < 0$, posons $t = -s$ ($s>0$). $f(x) - sc \leq p(x - s x_0) \iff -c \leq p(x/s - x_0) - f(x/s) \iff c \geq f(y) - p(y - x_0)$ (en posant $y = -x/s$).
Il faut donc trouver $c$ tel que pour tous $x_1, x_2 \in F$ :
$f(x_2) - p(x_2 - x_0) \leq c \leq p(x_1 + x_0) - f(x_1)$.
Cette condition est réalisable si et seulement si pour tous $x_1, x_2$ :
$f(x_2) - p(x_2 - x_0) \leq p(x_1 + x_0) - f(x_1)$
$\iff f(x_1) + f(x_2) = f(x_1 + x_2) \leq p(x_1 + x_0) + p(x_2 - x_0)$.
Or, $p(x_1 + x_0) + p(x_2 - x_0) \geq p((x_1 + x_0) + (x_2 - x_0)) = p(x_1 + x_2)$.
Puisque par hypothèse initiale $f(x_1 + x_2) \leq p(x_1 + x_2)$, l'inégalité est vérifiée.
La borne supérieure des membres de gauche est donc inférieure ou égale à la borne inférieure des membres de droite.
L'intervalle des valeurs possibles pour $c$ est non vide. On en choisit une, ce qui prolonge $f$ à $G$.
Par récurrence finie, on prolonge jusqu'à ce que $G = E$. $\blacksquare$
