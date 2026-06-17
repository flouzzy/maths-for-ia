# Exercice 3 : Relation d'équivalence sur le plan euclidien via la distance au carré à l'origine
**Difficulté :** ⭐⭐

## Énoncé
Soit $E = \mathbb{R}^2$ l'ensemble des points du plan euclidien.
On définit une relation $\mathcal{R}$ sur $E$ par :
Pour tout $(x_1, y_1) \in E$ et tout $(x_2, y_2) \in E$,
$$ (x_1, y_1) \mathcal{R} (x_2, y_2) \iff x_1^2 + y_1^2 = x_2^2 + y_2^2 $$

1.  Démontrer que $\mathcal{R}$ est une relation d'équivalence sur $E$.
2.  Décrire précisément les classes d'équivalence de $\mathcal{R}$.
3.  Décrire l'ensemble quotient $E/\mathcal{R}$.

## Correction Détaillée

Nous allons utiliser les propriétés fondamentales des nombres réels et de l'égalité pour justifier chaque étape.

### 1. Démonstration que $\mathcal{R}$ est une relation d'équivalence sur $E$

Pour qu'une relation soit une relation d'équivalence, elle doit satisfaire trois propriétés : la réflexivité, la symétrie et la transitivité.

#### a) Réflexivité
Une relation $\mathcal{R}$ est réflexive si, pour tout élément $A \in E$, on a $A \mathcal{R} A$.
Soit $(x, y)$ un point quelconque de l'ensemble $E = \mathbb{R}^2$.
Pour vérifier la réflexivité, nous devons montrer que $(x, y) \mathcal{R} (x, y)$.
D'après la définition de la relation $\mathcal{R}$, cela signifie que nous devons vérifier l'égalité suivante :
$$ x^2 + y^2 = x^2 + y^2 $$
Cette égalité est une identité, elle est toujours vraie pour tout $x, y \in \mathbb{R}$.
Par conséquent, la relation $\mathcal{R}$ est réflexive sur $E$.

#### b) Symétrie
Une relation $\mathcal{R}$ est symétrique si, pour tous éléments $A, B \in E$, si $A \mathcal{R} B$, alors $B \mathcal{R} A$.
Soient $(x_1, y_1)$ et $(x_2, y_2)$ deux points quelconques de l'ensemble $E = \mathbb{R}^2$.
Supposons que $(x_1, y_1) \mathcal{R} (x_2, y_2)$.
D'après la définition de la relation $\mathcal{R}$, cette hypothèse signifie que :
$$ x_1^2 + y_1^2 = x_2^2 + y_2^2 \quad (\text{Égalité 1}) $$
Nous devons montrer que $(x_2, y_2) \mathcal{R} (x_1, y_1)$.
D'après la définition de la relation $\mathcal{R}$, cela signifie que nous devons vérifier l'égalité suivante :
$$ x_2^2 + y_2^2 = x_1^2 + y_1^2 $$
L'égalité est une relation symétrique. Si $A=B$, alors $B=A$. En appliquant cette propriété à l'Égalité 1, nous pouvons écrire :
$$ x_2^2 + y_2^2 = x_1^2 + y_1^2 $$
Cette dernière égalité est exactement la condition pour que $(x_2, y_2) \mathcal{R} (x_1, y_1)$ soit vraie.
Par conséquent, la relation $\mathcal{R}$ est symétrique sur $E$.

#### c) Transitivité
Une relation $\mathcal{R}$ est transitive si, pour tous éléments $A, B, C \in E$, si $A \mathcal{R} B$ et $B \mathcal{R} C$, alors $A \mathcal{R} C$.
Soient $(x_1, y_1)$, $(x_2, y_2)$ et $(x_3, y_3)$ trois points quelconques de l'ensemble $E = \mathbb{R}^2$.
Supposons que $(x_1, y_1) \mathcal{R} (x_2, y_2)$ et $(x_2, y_2) \mathcal{R} (x_3, y_3)$.
D'après la définition de la relation $\mathcal{R}$ :
L'hypothèse $(x_1, y_1) \mathcal{R} (x_2, y_2)$ signifie que :
$$ x_1^2 + y_1^2 = x_2^2 + y_2^2 \quad (\text{Égalité 2}) $$
L'hypothèse $(x_2, y_2) \mathcal{R} (x_3, y_3)$ signifie que :
$$ x_2^2 + y_2^2 = x_3^2 + y_3^2 \quad (\text{Égalité 3}) $$
Nous devons montrer que $(x_1, y_1) \mathcal{R} (x_3, y_3)$.
D'après la définition de la relation $\mathcal{R}$, cela signifie que nous devons vérifier l'égalité suivante :
$$ x_1^2 + y_1^2 = x_3^2 + y_3^2 $$
En combinant l'Égalité 2 et l'Égalité 3, nous observons que la quantité $x_2^2 + y_2^2$ est égale à $x_1^2 + y_1^2$ et aussi à $x_3^2 + y_3^2$.
Par la propriété de transitivité de l'égalité (si $A=B$ et $B=C$, alors $A=C$), nous pouvons déduire que :
$$ x_1^2 + y_1^2 = x_3^2 + y_3^2 $$
Cette dernière égalité est exactement la condition pour que $(x_1, y_1) \mathcal{R} (x_3, y_3)$ soit vraie.
Par conséquent, la relation $\mathcal{R}$ est transitive sur $E$.

Puisque la relation $\mathcal{R}$ est réflexive, symétrique et transitive, nous concluons que $\mathcal{R}$ est une relation d'équivalence sur $E = \mathbb{R}^2$.

### 2. Description des classes d'équivalence de $\mathcal{R}$

Soit $(x_0, y_0)$ un point arbitraire de $E = \mathbb{R}^2$. La classe d'équivalence de $(x_0, y_0)$, notée $[(x_0, y_0)]$, est l'ensemble de tous les points $(x, y) \in E$ qui sont en relation avec $(x_0, y_0)$.
Par définition de $\mathcal{R}$, un point $(x, y)$ appartient à $[(x_0, y_0)]$ si et seulement si :
$$ x^2 + y^2 = x_0^2 + y_0^2 $$
Soit $k = x_0^2 + y_0^2$. Puisque $x_0$ et $y_0$ sont des nombres réels, $x_0^2 \ge 0$ et $y_0^2 \ge 0$. Par conséquent, $k$ est un nombre réel positif ou nul ($k \ge 0$).
La classe d'équivalence de $(x_0, y_0)$ est donc l'ensemble des points $(x, y) \in \mathbb{R}^2$ tels que $x^2 + y^2 = k$.

Nous devons distinguer deux cas pour la valeur de $k$:

#### a) Cas où $k = 0$
Si $k = 0$, cela signifie que $x_0^2 + y_0^2 = 0$. Puisque $x_0^2 \ge 0$ et $y_0^2 \ge 0$, la seule manière pour que leur somme soit nulle est que $x_0^2 = 0$ et $y_0^2 = 0$. Cela implique $x_0 = 0$ et $y_0 = 0$.
Dans ce cas, la classe d'équivalence de $(0, 0)$ est l'ensemble des points $(x, y)$ tels que $x^2 + y^2 = 0$.
La seule solution réelle à cette équation est $x=0$ et $y=0$.
Donc, la classe d'équivalence de $(0, 0)$ est l'ensemble qui contient uniquement le point $(0, 0)$ :
$$ [(0, 0)] = \{ (0, 0) \} $$
C'est le point d'origine du plan.

#### b) Cas où $k > 0$
Si $k > 0$, cela signifie que $x_0^2 + y_0^2 > 0$, donc $(x_0, y_0) \neq (0, 0)$.
Dans ce cas, la classe d'équivalence de $(x_0, y_0)$ est l'ensemble des points $(x, y)$ tels que $x^2 + y^2 = k$.
En posant $r = \sqrt{k}$, où $r > 0$, l'équation devient $x^2 + y^2 = r^2$.
Cette équation est la définition géométrique d'un cercle dans le plan euclidien. Ce cercle est centré à l'origine $(0, 0)$ et a un rayon $r = \sqrt{x_0^2 + y_0^2}$.
Donc, pour tout point $(x_0, y_0) \neq (0, 0)$, sa classe d'équivalence est le cercle centré à l'origine et passant par $(x_0, y_0)$.

En résumé, les classes d'équivalence de $\mathcal{R}$ sont :
*   Le point d'origine $(0, 0)$ lui-même.
*   Tous les cercles centrés à l'origine $(0, 0)$ et ayant un rayon strictement positif. Chaque cercle de rayon $r > 0$ représente une unique classe d'équivalence.

### 3. Description de l'ensemble quotient $E/\mathcal{R}$

L'ensemble quotient $E/\mathcal{R}$ est l'ensemble de toutes les classes d'équivalence distinctes de $\mathcal{R}$.
Nous avons vu que chaque classe d'équivalence est caractérisée de manière unique par la valeur de $k = x^2 + y^2$, où $k$ est un nombre réel positif ou nul.
La fonction $f: \mathbb{R}^2 \to [0, +\infty[$ définie par $f((x, y)) = x^2 + y^2$ associe à chaque point du plan un nombre réel positif ou nul.
Deux points $(x_1, y_1)$ et $(x_2, y_2)$ sont en relation si et seulement si $f((x_1, y_1)) = f((x_2, y_2))$.
L'ensemble des classes d'équivalence est en bijection avec l'ensemble des valeurs possibles de $k$.
L'ensemble des valeurs possibles pour $x^2 + y^2$ lorsque $(x, y) \in \mathbb{R}^2$ est l'ensemble de tous les nombres réels positifs ou nuls, c'est-à-dire l'intervalle $[0, +\infty[$.
Chaque valeur $k \in [0, +\infty[$ correspond à une unique classe d'équivalence :
*   Si $k=0$, la classe est le point $\{(0,0)\}$.
*   Si $k>0$, la classe est le cercle de rayon $\sqrt{k}$ centré à l'origine.

Ainsi, l'ensemble quotient $E/\mathcal{R}$ peut être identifié à l'ensemble des nombres réels positifs ou nuls.
$$ E/\mathcal{R} \cong [0, +\infty[ $$
Chaque élément de $[0, +\infty[$ représente une "orbite" de points dans le plan qui sont à la même distance (au carré) de l'origine.