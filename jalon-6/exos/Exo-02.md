# Exercice 2 : Relation de parité sur les entiers
**Difficulté :** ⭐

## Énoncé
Soit l'ensemble $\mathbb{Z}$ des nombres entiers relatifs.
On définit sur $\mathbb{Z}$ la relation $\mathcal{R}$ par :
$$ x \mathcal{R} y \quad \iff \quad x \text{ et } y \text{ ont la même parité} $$
Autrement dit, $x \mathcal{R} y$ si et seulement si $x$ et $y$ sont tous deux pairs, ou tous deux impairs.

Démontrer que $\mathcal{R}$ est une relation d'équivalence sur $\mathbb{Z}$.

## Correction Détaillée
Pour démontrer qu'une relation $\mathcal{R}$ définie sur un ensemble $E$ est une relation d'équivalence, nous devons prouver qu'elle satisfait trois propriétés fondamentales : la réflexivité, la symétrie et la transitivité.

**Hypothèses de structure :** L'ensemble sur lequel la relation est définie est $\mathbb{Z}$, l'ensemble des entiers relatifs, muni de ses propriétés arithmétiques usuelles. La définition de la parité repose sur la division euclidienne par 2.

Commençons par rappeler les définitions de la parité pour un entier, qui sont les fondements de cette relation :
Un entier $n \in \mathbb{Z}$ est dit **pair** s'il existe un entier $k \in \mathbb{Z}$ tel que $n = 2k$.
Un entier $n \in \mathbb{Z}$ est dit **impair** s'il existe un entier $k \in \mathbb{Z}$ tel que $n = 2k+1$.
La relation $\mathcal{R}$ est définie par $x \mathcal{R} y$ si et seulement si ( $x$ est pair ET $y$ est pair ) OU ( $x$ est impair ET $y$ est impair ).

### 1. Preuve de la Réflexivité

**Définition de la réflexivité :** Une relation $\mathcal{R}$ est réflexive sur un ensemble $E$ si, pour tout élément $x \in E$, la propriété $x \mathcal{R} x$ est vérifiée.

**Démonstration :**
Soit $x$ un entier quelconque appartenant à l'ensemble $\mathbb{Z}$.
Nous devons vérifier si la proposition $x \mathcal{R} x$ est vraie.
Selon la définition de la relation $\mathcal{R}$, la proposition $x \mathcal{R} x$ signifie que " $x$ et $x$ ont la même parité ".

Un entier $x$ donné possède nécessairement une parité spécifique :
*   **Cas 1 :** Si $x$ est un entier pair.
    Alors, $x$ est pair. Par conséquent, $x$ a la même parité que lui-même (puisqu'il est pair et lui-même est pair).
*   **Cas 2 :** Si $x$ est un entier impair.
    Alors, $x$ est impair. Par conséquent, $x$ a la même parité que lui-même (puisqu'il est impair et lui-même est impair).

Dans les deux cas possibles qui couvrent toutes les possibilités pour la parité de $x$, l'entier $x$ a toujours la même parité que lui-même.
Ainsi, la condition $x \mathcal{R} x$ est toujours satisfaite pour tout $x \in \mathbb{Z}$.
Par conséquent, la relation $\mathcal{R}$ est réflexive sur $\mathbb{Z}$.

### 2. Preuve de la Symétrie

**Définition de la symétrie :** Une relation $\mathcal{R}$ est symétrique sur un ensemble $E$ si, pour tous éléments $x, y \in E$, si $x \mathcal{R} y$ est vraie, alors $y \mathcal{R} x$ est également vraie.

**Démonstration :**
Soient $x$ et $y$ deux entiers quelconques appartenant à l'ensemble $\mathbb{Z}$.
Supposons que l'hypothèse $x \mathcal{R} y$ est vraie.
Selon la définition de la relation $\mathcal{R}$, l'hypothèse $x \mathcal{R} y$ signifie que " $x$ et $y$ ont la même parité ".

Cette condition " $x$ et $y$ ont la même parité " peut se décomposer en deux sous-cas mutuellement exclusifs et exhaustifs :
*   **Sous-cas 1 :** $x$ est pair ET $y$ est pair.
*   **Sous-cas 2 :** $x$ est impair ET $y$ est impair.

Nous devons montrer que, sous l'hypothèse $x \mathcal{R} y$, la proposition $y \mathcal{R} x$ est vraie.
La proposition $y \mathcal{R} x$ signifie que " $y$ et $x$ ont la même parité ".

Considérons le **Sous-cas 1** : $x$ est pair ET $y$ est pair.
Dans ce cas, il est évident que $y$ est pair ET $x$ est pair. Par conséquent, $y$ et $x$ ont la même parité.
Ceci implique que $y \mathcal{R} x$ est vraie dans ce sous-cas.

Considérons le **Sous-cas 2** : $x$ est impair ET $y$ est impair.
Dans ce cas, il est évident que $y$ est impair ET $x$ est impair. Par conséquent, $y$ et $x$ ont la même parité.
Ceci implique que $y \mathcal{R} x$ est vraie dans ce sous-cas.

Puisque dans tous les cas possibles découlant de l'hypothèse $x \mathcal{R} y$, nous avons démontré que $y \mathcal{R} x$ est vraie, la symétrie de la relation $\mathcal{R}$ est établie.
Par conséquent, la relation $\mathcal{R}$ est symétrique sur $\mathbb{Z}$.

### 3. Preuve de la Transitivité

**Définition de la transitivité :** Une relation $\mathcal{R}$ est transitive sur un ensemble $E$ si, pour tous éléments $x, y, z \in E$, si $x \mathcal{R} y$ est vraie ET $y \mathcal{R} z$ est vraie, alors $x \mathcal{R} z$ est également vraie.

**Démonstration :**
Soient $x, y, z$ trois entiers quelconques appartenant à l'ensemble $\mathbb{Z}$.
Supposons que les deux hypothèses suivantes sont vraies :
1.  $x \mathcal{R} y$ est vraie.
2.  $y \mathcal{R} z$ est vraie.

Selon la définition de la relation $\mathcal{R}$ :
*   L'hypothèse $x \mathcal{R} y$ signifie que " $x$ et $y$ ont la même parité ".
*   L'hypothèse $y \mathcal{R} z$ signifie que " $y$ et $z$ ont la même parité ".

Nous devons montrer que la proposition $x \mathcal{R} z$ est vraie sous ces hypothèses.
La proposition $x \mathcal{R} z$ signifie que " $x$ et $z$ ont la même parité ".

Analysons la parité de l'entier intermédiaire $y$, qui est nécessairement soit pair, soit impair :
*   **Cas 1 :** Supposons que $y$ est un entier pair.
    *   Puisque $x \mathcal{R} y$ ( $x$ et $y$ ont la même parité) ET $y$ est pair, il s'ensuit que $x$ doit également être pair.
    *   Puisque $y \mathcal{R} z$ ( $y$ et $z$ ont la même parité) ET $y$ est pair, il s'ensuit que $z$ doit également être pair.
    *   Dans ce cas, nous avons établi que $x$ est pair et $z$ est pair. Puisque $x$ et $z$ sont tous deux pairs, ils ont la même parité.
    *   Par conséquent, $x \mathcal{R} z$ est vérifiée dans ce cas.

*   **Cas 2 :** Supposons que $y$ est un entier impair.
    *   Puisque $x \mathcal{R} y$ ( $x$ et $y$ ont la même parité) ET $y$ est impair, il s'ensuit que $x$ doit également être impair.
    *   Puisque $y \mathcal{R} z$ ( $y$ et $z$ ont la même parité) ET $y$ est impair, il s'ensuit que $z$ doit également être impair.
    *   Dans ce cas, nous avons établi que $x$ est impair et $z$ est impair. Puisque $x$ et $z$ sont tous deux impairs, ils ont la même parité.
    *   Par conséquent, $x \mathcal{R} z$ est vérifiée dans ce cas.

Étant donné que l'entier $y$ est nécessairement soit pair soit impair, et que dans les deux cas nous avons démontré que la proposition $x \mathcal{R} z$ est vraie, la transitivité de la relation $\mathcal{R}$ est prouvée.
Par conséquent, la relation $\mathcal{R}$ est transitive sur $\mathbb{Z}$.

### Conclusion
Puisque la relation $\mathcal{R}$ définie sur l'ensemble $\mathbb{Z}$ a été démontrée comme étant réflexive, symétrique et transitive, elle satisfait toutes les conditions requises pour être une relation d'équivalence sur $\mathbb{Z}$.