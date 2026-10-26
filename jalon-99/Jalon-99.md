---
uuid: "jalon-99"
title: "Théorème de Hahn-Banach (forme géométrique)"
year: 3
trimester: 9
tags:
  - math/analyse
  - ia/optimisation
prev: "[[Jalon 98 (Théorème de Hahn-Banach (forme analytique)).md]]"
next: "[[Jalon 100 (Démonstration du théorème de Banach-Steinhaus).md]]"
---

# Théorème de Hahn-Banach (Formes Géométriques)

## 1. Origines et Intuition Géométrique

Au cœur de l'analyse fonctionnelle et de la géométrie convexe se trouve une question d'une apparente simplicité, mais aux implications profondes : étant donnés deux corps disjoints dans un espace, est-il toujours possible de glisser une paroi plane stricte entre eux ? Dans un espace vectoriel de dimension 2 ou 3, l'intuition physique répond immédiatement par l'affirmative pour des corps qui ne s'entrelacent pas. Cette paroi n'est autre qu'une droite dans le plan, ou un plan dans l'espace à trois dimensions. Plus généralement, dans un espace vectoriel de dimension quelconque, fini ou infini, il s'agit d'un **hyperplan affine**.

L'invention, ou plutôt la découverte, du théorème de Hahn-Banach dans ses formes géométriques répond à cette interrogation géométrique fondamentale. Hans Hahn et Stefan Banach ont, dans les années 1920, jeté les bases d'une théorie rigoureuse permettant de s'affranchir de la restriction aux dimensions finies. Le besoin s'est fait sentir lorsque les mathématiciens ont commencé à manipuler des espaces de fonctions (dimension infinie), où l'intuition géométrique classique devient rapidement caduque.

L'exigence cruciale pour que cette séparation soit réalisable est la **convexité** des corps en question. Si l'un des ensembles possède une "cavité" ou s'ils s'entrelacent comme deux anneaux, une paroi plane ne peut les séparer sans en sectionner au moins un. La convexité, propriété algébrico-géométrique affirmant que le segment reliant deux points quelconques de l'ensemble reste entièrement inclus dans cet ensemble, devient la pierre angulaire de ce théorème. Les conséquences de cette prouesse d'abstraction se répercutent de manière spectaculaire dans l'optimisation moderne, la théorie des jeux et l'intelligence artificielle, où "séparer des ensembles" équivaut souvent à "trouver une règle de décision optimale".

## 2. Définitions et Structures Géométriques Fondamentales

Avant d'énoncer le théorème, fixons le cadre topologique et algébrique rigoureux.

Soit $E$ un espace vectoriel topologique sur le corps $\mathbb{R}$. Dans la majorité des applications en apprentissage automatique, $E$ est un espace de Hilbert ou de Banach, et sa topologie est induite par une norme $\| \cdot \|$. Le dual topologique de $E$, noté $E^*$, désigne l'espace vectoriel des formes linéaires continues sur $E$.

**Définition (Hyperplan Affine) :**
Un hyperplan affine $H$ dans $E$ est défini par le lieu d'annulation translaté d'une forme linéaire continue non nulle $f \in E^*$ :
$$H = \{ x \in E \mid f(x) = \alpha \}$$
où $\alpha \in \mathbb{R}$.

**Définition (Demi-Espaces) :**
L'hyperplan affine $H$ partitionne l'espace $E \setminus H$ en deux composantes connexes, appelées demi-espaces stricts :
$$H_< = \{ x \in E \mid f(x) < \alpha \} \quad \text{et} \quad H_> = \{ x \in E \mid f(x) > \alpha \}$$
Les demi-espaces larges sont obtenus en incluant l'hyperplan :
$$H_{\le} = \{ x \in E \mid f(x) \le \alpha \} \quad \text{et} \quad H_{\ge} = \{ x \in E \mid f(x) \ge \alpha \}$$

### La Première Forme Géométrique : Séparation au Sens Large

Ce premier théorème énonce les conditions minimales pour s'assurer que deux convexes ne se chevauchent pas de manière fatale.

**Théorème (Hahn-Banach, Première Forme Géométrique) :**
Soient $A$ et $B$ deux parties de $E$, convexes, non vides et disjointes ($A \cap B = \emptyset$). On suppose que l'une des deux parties, par exemple $A$, est un **ouvert**. Alors, il existe un hyperplan fermé séparant $A$ et $B$ au sens large. Autrement dit, il existe une forme linéaire continue non nulle $f \in E^*$ et un scalaire $\alpha \in \mathbb{R}$ tels que :
$$ \forall x \in A, \, f(x) < \alpha $$
$$ \forall y \in B, \, f(y) \ge \alpha $$

**Exemple Concret Immédiat : Séparation dans le Plan**
Considérons l'espace $E = \mathbb{R}^2$ muni de la norme euclidienne usuelle.
Définissons $A = \{ (x_1, x_2) \in \mathbb{R}^2 \mid x_1^2 + x_2^2 < 1 \}$ (le disque unité ouvert).
Définissons $B = \{ (x_1, x_2) \in \mathbb{R}^2 \mid x_1 \ge 2 \}$ (un demi-plan fermé).
$A$ et $B$ sont manifestement disjoints, convexes et $A$ est ouvert.
Cherchons la forme linéaire continue (qui s'écrit $f(x) = w_1 x_1 + w_2 x_2$ car en dimension finie) et la constante $\alpha$.
Si l'on choisit $f(x) = x_1$ (donc $w_1 = 1, w_2 = 0$), nous avons pour tout $x \in A$, $x_1 < 1$, et pour tout $y \in B$, $y_1 \ge 2$.
En prenant $\alpha = 1.5$, nous vérifions strictement l'énoncé du théorème :
$$ \forall x \in A, \, f(x) = x_1 < 1 < 1.5 = \alpha $$
$$ \forall y \in B, \, f(y) = y_1 \ge 2 > 1.5 = \alpha $$
L'hyperplan affine séparateur est la droite verticale d'équation $x_1 = 1.5$.

### La Deuxième Forme Géométrique : Séparation Stricte

Souvent, on désire une séparation avec une marge de sécurité. Cela requiert des hypothèses topologiques plus fortes.

**Théorème (Hahn-Banach, Deuxième Forme Géométrique) :**
Soient $A$ et $B$ deux parties de $E$, convexes, non vides et disjointes. On suppose de plus que $A$ est **fermé** et $B$ est **compact**. Alors, il existe un hyperplan fermé séparant strictement $A$ et $B$. Autrement dit, il existe une forme linéaire continue non nulle $f \in E^*$, et deux réels $\alpha \in \mathbb{R}$ et $\varepsilon > 0$ tels que :
$$ \forall x \in A, \, f(x) \le \alpha - \varepsilon $$
$$ \forall y \in B, \, f(y) \ge \alpha + \varepsilon $$

**Exemple Concret Immédiat : Le Rôle Crucial de la Compacité**
Considérons à nouveau $E = \mathbb{R}^2$.
Prenons $A = \{ (x_1, x_2) \in \mathbb{R}^2 \mid x_2 \ge \frac{1}{x_1}, x_1 > 0 \}$ (l'épigraphe de l'hyperbole). $A$ est convexe et fermé.
Prenons $B = \{ (x_1, x_2) \in \mathbb{R}^2 \mid x_2 \le 0, x_1 > 0 \}$ (le quart de plan inférieur droit). $B$ est convexe et fermé, mais **non compact**.
$A$ et $B$ sont disjoints. Les axes de l'hyperbole s'approchent infiniment de l'axe des abscisses.
Pouvons-nous les séparer strictement ?
Toute droite séparant $A$ de $B$ doit nécessairement être l'axe des abscisses lui-même, d'équation $x_2 = 0$ (soit $f(x) = x_2$ avec $\alpha = 0$).
Pour $y \in B$, $f(y) = y_2 \le 0$. Pour $x \in A$, $f(x) = x_2 > 0$. La séparation au sens large est possible, mais aucune marge de sécurité $\varepsilon > 0$ ne peut exister car la distance entre $A$ et $B$ tend vers zéro (infimum nul).
Cet exemple pathologique justifie pleinement l'hypothèse qu'un des deux ensembles (ici $B$ si l'on voulait appliquer le théorème) doive impérativement être compact pour garantir une séparation stricte. Si $B$ était, par exemple, le segment reliant $(1, -1)$ à $(2, -1)$, la séparation stricte serait alors trivialement acquise.

## 3. Démonstration du Théorème (Première Forme Géométrique)

La démonstration est un modèle d'élégance mathématique, reposant sur l'introduction de la jauge (ou fonctionnelle de Minkowski) et l'utilisation de la forme analytique du théorème de Hahn-Banach, établie dans le Jalon précédent.

**Preuve pas-à-pas de la première forme :**

Étape 1 : Ramenons le problème à un seul convexe.
Considérons l'ensemble différence de Minkowski : $C = A - B = \{ a - b \mid a \in A, b \in B \}$.
Puisque $A$ et $B$ sont convexes, $C$ l'est aussi.
En effet, soient $x_1, x_2 \in C$ et $t \in [0,1]$. $x_1 = a_1 - b_1$ et $x_2 = a_2 - b_2$.
$t x_1 + (1-t) x_2 = t(a_1 - b_1) + (1-t)(a_2 - b_2) = (ta_1 + (1-t)a_2) - (tb_1 + (1-t)b_2)$.
Comme $A$ et $B$ sont convexes, $ta_1 + (1-t)a_2 \in A$ et $tb_1 + (1-t)b_2 \in B$, d'où $t x_1 + (1-t) x_2 \in A - B = C$.

Étape 2 : Propriétés topologiques de $C$.
Puisque $A$ est ouvert, on peut écrire $C = \bigcup_{b \in B} (A - \{b\})$. C'est une réunion d'ouverts (les translatés de $A$), donc $C$ est un convexe ouvert.
L'hypothèse cruciale de disjonction, $A \cap B = \emptyset$, équivaut algébriquement à affirmer que le vecteur nul n'appartient pas à $C$ : $0 \notin C$.

Étape 3 : Translation pour utiliser la jauge.
Soit $x_0 \in C$ (possible car $A, B$ non vides). Définissons $U = C - x_0$. L'ensemble $U$ est désormais un convexe ouvert qui contient le vecteur nul $0$. L'origine est un point intérieur de $U$.
Mais $0 \notin C$, ce qui implique que $-x_0 \notin U$.

Étape 4 : Utilisation de la jauge de Minkowski.
Soit $p$ la jauge de Minkowski associée au convexe ouvert $U$ contenant l'origine :
$$ p(x) = \inf \{ \lambda > 0 \mid x \in \lambda U \} $$
Propriétés fondamentales de la jauge pour un convexe ouvert contenant 0 :
1. $p(x + y) \le p(x) + p(y)$ pour tous $x, y \in E$ (sous-additivité due à la convexité).
2. $p(\lambda x) = \lambda p(x)$ pour tout $\lambda \ge 0$ et $x \in E$ (positivement homogène).
3. L'appartenance à $U$ est caractérisée par : $x \in U \iff p(x) < 1$.
Puisque $-x_0 \notin U$, nous déduisons de la troisième propriété que $p(-x_0) \ge 1$.

Étape 5 : Construction de la forme linéaire et application de Hahn-Banach Analytique.
Considérons le sous-espace vectoriel de dimension 1 engendré par $-x_0$ : $G = \mathbb{R}(-x_0) = \{ t(-x_0) \mid t \in \mathbb{R} \}$.
Définissons une forme linéaire $g$ sur $G$ par $g(t(-x_0)) = t$.
Vérifions que $g$ est majorée par la jauge $p$ sur le sous-espace $G$ :
- Si $t \ge 0$, alors $g(t(-x_0)) = t$. Or, $p(t(-x_0)) = t p(-x_0)$. Puisque $p(-x_0) \ge 1$, nous avons $t \le t p(-x_0)$, donc $g(t(-x_0)) \le p(t(-x_0))$.
- Si $t < 0$, alors $g(t(-x_0)) = t < 0 \le p(t(-x_0))$ (la jauge est toujours positive).
Ainsi, $\forall y \in G, \, g(y) \le p(y)$.
Nous sommes dans les conditions d'application de la forme analytique du théorème de Hahn-Banach : la forme linéaire $g$, définie sur le sous-espace $G$ et dominée par la fonction sous-linéaire $p$, peut être prolongée en une forme linéaire $f$ sur tout l'espace $E$, telle que :
$$ \forall x \in E, \, f(x) \le p(x) $$

Étape 6 : Conclusion géométrique.
Revenons à l'ensemble $U$. Pour tout $u \in U$, nous savons que $p(u) < 1$.
Par le prolongement de Hahn-Banach, $f(u) \le p(u) < 1$.
De plus, par définition sur $G$, $f(-x_0) = g(-x_0) = 1$.
Rappelons que $U = C - x_0$. Donc tout $u \in U$ s'écrit $c - x_0$ pour un certain $c \in C$.
L'inégalité $f(u) < 1$ devient $f(c - x_0) < 1$, soit $f(c) - f(x_0) < 1$.
Or, $f(-x_0) = -f(x_0) = 1$, d'où $f(x_0) = -1$.
Nous obtenons alors $f(c) - (-1) < 1 \implies f(c) < 0$ pour tout $c \in C$.
En remplaçant $c$ par son expression $a - b$, nous avons pour tout $a \in A$ et $b \in B$ :
$f(a - b) < 0 \implies f(a) < f(b)$.
La forme linéaire $f$ sépare bien l'image de $A$ de celle de $B$ sur la droite réelle. En posant $\alpha = \sup_{a \in A} f(a)$, l'inégalité large est démontrée.

## 4. Applications en Intelligence Artificielle et Logique

La puissance d'abstraction du théorème de Hahn-Banach géométrique prend tout son sens dans les fondements mathématiques de l'apprentissage automatique, où la notion géométrique de "séparation" est un synonyme rigoureux du concept de "classification".

### Machines à Vecteurs de Support (Support Vector Machines - SVM)

L'un des algorithmes de classification les plus mathématiquement purs, le SVM linéaire, est une incarnation computationnelle directe de la deuxième forme géométrique de Hahn-Banach.
Considérons un ensemble de données d'apprentissage composé de vecteurs en grande dimension (par exemple, des images vectorisées). Cet ensemble est composé de deux classes : $C_1$ (les images de chats) et $C_2$ (les images de chiens). Chaque classe forme, par combinaison convexe de ses représentants, un polytope convexe (l'enveloppe convexe des points). Ces polytopes, en tant que combinaisons convexes d'un nombre fini de points en dimension finie, sont **compacts**.

Si la base de données est, par nature, non contradictoire (pas d'image parfaitement identique étiquetée à la fois chien et chat, et des classes distinctes), les deux polytopes sont compacts et disjoints. La deuxième forme de Hahn-Banach affirme alors sans équivoque : il existe un hyperplan affine $f(x) = w^T x + b = 0$ et une marge stricte $\varepsilon > 0$ qui séparent rigoureusement les deux convexes.
L'objectif de l'algorithme d'optimisation du SVM n'est donc pas de s'interroger sur l'existence de cette paroi, garantie par l'analyse fonctionnelle, mais de trouver celle qui maximise la constante $\varepsilon$, rendant le modèle d'intelligence artificielle le plus robuste possible aux variations de nouvelles données.

### Théorème de Séparation dans l'Espace des Fonctions

Dans l'analyse des réseaux de neurones profonds sur-paramétrés, l'espace d'étude n'est plus l'espace des données de dimension finie, mais l'espace des fonctions engendrées par l'architecture neuronale $E = \mathcal{H}$ (souvent étudié comme un Espace de Hilbert à Noyau Reproduisant, RKHS).
Lors de la recherche d'un minimum de la fonction de perte empirique (Loss landscape), on peut chercher à isoler une région convexe de "bonnes fonctions" (dont la perte est inférieure à un certain seuil minimal acceptable) du reste des fonctions pathologiques. L'application de la forme géométrique de Hahn-Banach en dimension infinie permet d'assurer qu'un opérateur linéaire (souvent lié au gradient du modèle dans l'espace fonctionnel) peut constituer une frontière de décision entre le régime de mémorisation du réseau (sur-apprentissage) et le régime de généralisation optimale.
