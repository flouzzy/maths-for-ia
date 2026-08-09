---
uuid: "jalon-51"
title: "Espaces métriques"
year: 2
trimester: 5
tags:
  - math/topologie
  - ia/algorithmes
prev: "[[Jalon 50 (Opérateurs topologiques).md]]"
next: "[[Jalon 52 (Applications continues entre espaces topologiques et définition fine des homéomorphismes.).md]]"
---
# Espaces métriques

## Genèse et Intuition Géométrique

La notion d'espace métrique émerge de la volonté de généraliser et de formaliser le concept de distance géométrique, intuitivement compris dans le plan euclidien, à des espaces abstraits plus généraux. L'idée fondatrice est de dégager les propriétés essentielles qui caractérisent l'écart entre deux éléments. Historiquement, le développement de l'analyse fonctionnelle au début du XXe siècle a nécessité la comparaison entre des fonctions ou des suites, imposant ainsi la création d'une structure capable d'évaluer quantitativement la proximité dans des ensembles arbitraires.

Dans un espace usuel, la distance permet de définir ce qu'est une boule, une convergence, ou une continuité. L'objectif est ici de s'abstraire de la structure vectorielle ou algébrique pour ne conserver que la fonction de mesure, garantissant une robustesse topologique universelle.

## Définitions, Théorèmes et Exemples Concrets

### Formalisation d'une Distance

Soit $X$ un ensemble non vide.

**Définition (Distance) :**
On appelle distance, ou métrique, sur $X$, toute application $d : X \times X \to \mathbb{R}_+$ vérifiant les trois axiomes suivants pour tous $x, y, z \in X$ :
1. Séparation : $d(x, y) = 0 \iff x = y$.
2. Symétrie : $d(x, y) = d(y, x)$.
3. Inégalité triangulaire : $d(x, z) \le d(x, y) + d(y, z)$.

Le couple $(X, d)$ est alors appelé un espace métrique.

**Exemple Numérique Immédiat :**
Sur l'ensemble des réels $\mathbb{R}$, l'application définie par $d(x, y) = |x - y|$ est une distance. Par exemple, pour $x = 3$ et $y = -2$, la distance est $d(3, -2) = |3 - (-2)| = 5$. L'inégalité triangulaire reflète le fait que la distance la plus courte entre deux points est la ligne droite : $d(3, 5) \le d(3, 0) + d(0, 5)$, soit $2 \le 3 + 5$, ce qui est strictement respecté.

**Cas Pathologique :**
Si l'on considère la fonction $d(x, y) = (x - y)^2$ sur $\mathbb{R}$, elle vérifie la séparation et la symétrie. Cependant, l'inégalité triangulaire fait défaut. En effet, pour $x=0$, $y=1$ et $z=2$, on a $d(0, 2) = 4$, tandis que $d(0, 1) + d(1, 2) = 1 + 1 = 2$. Comme $4 > 2$, $d(x,y) = (x-y)^2$ ne définit pas une distance.

\begin{tikzpicture}
\draw[thick, ->] (-1,0) -- (4,0) node[anchor=north west] {$x$};
\draw[thick, ->] (0,-1) -- (0,4) node[anchor=south east] {$y$};
\fill (1,1) circle (2pt) node[below right] {$A$};
\fill (3,3) circle (2pt) node[below right] {$B$};
\fill (1,3) circle (2pt) node[above left] {$C$};
\draw[dashed] (1,1) -- (3,3) node[midway, below right] {$d(A,B)$};
\draw[dashed] (1,1) -- (1,3) node[midway, left] {$d(A,C)$};
\draw[dashed] (1,3) -- (3,3) node[midway, above] {$d(C,B)$};
\end{tikzpicture}

### Boules et Topologie Induite

**Définition (Boules) :**
Dans un espace métrique $(X, d)$, pour $a \in X$ et un rayon $r > 0$, on définit :
- La boule ouverte de centre $a$ et de rayon $r$ : $B(a, r) = \{ x \in X \mid d(a, x) < r \}$.
- La boule fermée de centre $a$ et de rayon $r$ : $\bar{B}(a, r) = \{ x \in X \mid d(a, x) \le r \}$.

**Théorème (Topologie Métrique) :**
L'ensemble des parties de $X$ qui sont des réunions quelconques de boules ouvertes forme une topologie sur $X$. Un sous-ensemble $U$ est donc un ouvert pour cette topologie si, pour tout point $x \in U$, il existe un réel $r > 0$ tel que $B(x, r) \subset U$.

**Exemple Géométrique :**
Sur $\mathbb{R}^2$ muni de la distance euclidienne $d_2(x, y) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2}$, la boule ouverte $B((0,0), 1)$ est le disque strictement intérieur au cercle unité. Un point $A(0.5, 0)$ appartient à ce disque, et l'on peut trouver une boule ouverte centrée en $A$, par exemple de rayon $0.4$, entièrement incluse dans le disque initial.

### Distances Équivalentes

**Définition :**
Deux distances $d_1$ et $d_2$ sur un même ensemble $X$ sont dites topologiquement équivalentes si elles induisent la même topologie. Elles sont dites fortement équivalentes s'il existe des constantes $C_1, C_2 > 0$ telles que pour tous $x, y \in X$ :
$$C_1 d_1(x, y) \le d_2(x, y) \le C_2 d_1(x, y)$$

## Démonstrations Pas-à-Pas

### Une boule ouverte est un ouvert au sens de la topologie

**Énoncé :** Dans tout espace métrique $(X, d)$, une boule ouverte $B(a, r)$ est un sous-ensemble ouvert.

**Démonstration :**
Soit $B(a, r)$ une boule ouverte de rayon $r > 0$ centrée en $a$.
Considérons un point quelconque $x \in B(a, r)$. Par définition, la distance entre $a$ et $x$ vérifie :
$$d(a, x) < r$$
Nous devons trouver un rayon $\epsilon > 0$ tel que la boule ouverte $B(x, \epsilon)$ soit entièrement incluse dans $B(a, r)$.
Posons :
$$\epsilon = r - d(a, x)$$
Puisque $d(a, x) < r$, il s'ensuit que $\epsilon > 0$.
Soit maintenant un point $y \in B(x, \epsilon)$. Par définition, on a :
$$d(x, y) < \epsilon$$
Appliquons l'inégalité triangulaire aux points $a$, $x$ et $y$ :
$$d(a, y) \le d(a, x) + d(x, y)$$
En injectant la majoration de $d(x, y)$, nous obtenons strictement :
$$d(a, y) < d(a, x) + \epsilon$$
Remplaçons $\epsilon$ par sa valeur $r - d(a, x)$ :
$$d(a, y) < d(a, x) + (r - d(a, x))$$
Ce qui se simplifie en :
$$d(a, y) < r$$
Par conséquent, $y \in B(a, r)$.
Puisque cela est vrai pour tout $y \in B(x, \epsilon)$, nous avons bien l'inclusion :
$$B(x, \epsilon) \subset B(a, r)$$
La boule $B(a, r)$ contient un voisinage de chacun de ses points ; elle est donc un ouvert topologique.

## Applications en Physique, Logique et Intelligence Artificielle

En intelligence artificielle, la notion d'espace métrique est le socle de l'apprentissage non supervisé et de l'évaluation de la similarité. Le regroupement de données (clustering) repose intrinsèquement sur le choix d'une métrique. Par exemple, l'algorithme des k-moyennes (k-means) cherche à minimiser la variance intra-classe, s'appuyant souvent sur la distance euclidienne.

La reconnaissance des formes et le traitement du langage naturel utilisent massivement des distances. Dans les espaces de plongement vectoriel (word embeddings comme Word2Vec), la proximité sémantique entre deux mots est évaluée par une métrique de similarité, souvent dérivée de la distance cosinus ou euclidienne, transformant des concepts linguistiques en entités d'un espace métrique abstrait.

En physique théorique, la structure de l'espace-temps repose sur des concepts apparentés. Bien que la relativité utilise des espaces pseudo-métriques (où la "distance" entre des événements distincts peut être nulle), la rigueur de la formulation métrique permet de concevoir et d'étudier la courbure et la géométrie de l'univers, fondant ainsi la relativité générale sur des bases d'analyse fonctionnelle solide.
