# Exercice 6 : La distance de Hausdorff
**Difficulté :** $\bigstar\bigstar\bigstar\bigstar\star$

## Énoncé formel
Soit $(X,d)$ un espace métrique. Pour un point $x \in X$ et une partie $A \subset X$ non vide, la distance de $x$ à $A$ est définie par $d(x, A) = \inf_{a \in A} d(x, a)$. Montrer que l'application $x \mapsto d(x, A)$ est $1$-lipschitzienne.

## Résolution pas à pas
**Étape 1 : Traduction avec l'inégalité triangulaire**

Soient $x, y \in X$. Pour tout $a \in A$, par l'inégalité triangulaire de $d$ :
$d(x, a) \le d(x, y) + d(y, a)$.

**Étape 2 : Passage à l'infimum**

L'inégalité ci-dessus implique que pour tout $a \in A$ :
$d(x, A) \le d(x, a) \le d(x, y) + d(y, a)$.
Ainsi, $d(x, A) - d(x, y) \le d(y, a)$ pour tout $a \in A$.
Le terme de gauche est un minorant de l'ensemble $\left\lbrace d(y, a) \mid a \in A\right\rbrace$. Par définition, l'infimum est le plus grand des minorants, d'où :
$d(x, A) - d(x, y) \le d(y, A)$, c'est-à-dire $d(x, A) - d(y, A) \le d(x, y)$.

**Étape 3 : Symétrie et conclusion**

En échangeant le rôle de $x$ et de $y$, on obtient de même $d(y, A) - d(x, A) \le d(y, x) = d(x, y)$.
Les deux inégalités se résument en la valeur absolue :
$|d(x, A) - d(y, A)| \le d(x, y)$.
Ceci prouve formellement que la fonction de distance à un ensemble est 1-lipschitzienne (et donc uniformément continue). $\blacksquare$
