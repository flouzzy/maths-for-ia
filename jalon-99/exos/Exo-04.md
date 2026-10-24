# Exercice 4 : $\bigstar\bigstar\star\star\star$

## Énoncé

Dans $\mathbb{R}^n$, montrer que l'enveloppe convexe d'un ensemble fini de points $S = \{x_1, \dots, x_k\}$ est égale à l'intersection de tous les demi-espaces fermés la contenant.

## Correction

**Étape 1 : Inclusion évidente**
Soit $C = \text{Conv}(S)$. Un demi-espace fermé contenant $C$ est de la forme $H^+ = \{x \in \mathbb{R}^n \mid f(x) \le \alpha\}$. L'intersection de tous ces demi-espaces fermés contient évidemment $C$.

**Étape 2 : L'autre inclusion via Hahn-Banach**
Soit $y \notin C$. $C$ est l'enveloppe convexe d'un ensemble fini, donc $C$ est un polyèdre compact (et donc convexe fermé).
Le singleton $\{y\}$ est compact.
Par le théorème de Hahn-Banach géométrique (séparation stricte), il existe une forme linéaire $f$ et des réels $\alpha, \epsilon > 0$ tels que :
$\forall c \in C, f(c) \le \alpha - \epsilon < \alpha \le f(y)$.
Ainsi, le demi-espace fermé $H^+ = \{x \mid f(x) \le \alpha - \epsilon\}$ contient $C$.
Cependant, $f(y) \ge \alpha > \alpha - \epsilon$, donc $y \notin H^+$.
Par conséquent, $y$ n'appartient pas à l'intersection de tous les demi-espaces fermés contenant $C$.
Ainsi, $C$ est exactement égal à cette intersection. $\blacksquare$
