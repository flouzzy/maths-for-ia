# Théorème de Hahn-Banach : Séparation Géométrique des Convexes

## 1. Origines Géométriques et Algébriques

La genèse du théorème de Hahn-Banach géométrique repose sur une question fondamentale de la géométrie des espaces vectoriels topologiques : étant donné deux objets géométriques disjoints (des ensembles convexes), est-il possible de glisser un hyperplan (un sous-espace affine de codimension 1) entre eux pour les séparer strictement ?

Dans un espace euclidien de dimension finie $\mathbb{R}^n$, l'intuition spatiale rend ce résultat presque immédiat visuellement. Si l'on dessine deux patatoïdes convexes qui ne se touchent pas sur une feuille de papier, on peut tracer une droite (hyperplan en dimension 2) qui laisse le premier patatoïde d'un côté et le second de l'autre. Le triomphe de l'analyse fonctionnelle moderne a été d'élever cette intuition géométrique aux espaces de dimension infinie, comme les espaces de Banach ou de Fréchet.

## 2. Définitions et Structures Fondamentales

Soit $E$ un espace vectoriel sur $\mathbb{R}$.

**Définition (Hyperplan et forme linéaire).**
Un hyperplan affine $H$ dans $E$ est un sous-espace affine de codimension $1$. Il est toujours défini comme une ligne de niveau d'une forme linéaire non nulle. Il existe $f \in E^* \setminus \{0\}$ (le dual algébrique de $E$) et $\alpha \in \mathbb{R}$ tels que :
$$H = \{ x \in E \mid f(x) = \alpha \}$$

L'hyperplan sépare l'espace en deux demi-espaces fermés :
$$E_1 = \{ x \in E \mid f(x) \leq \alpha \} \quad \text{et} \quad E_2 = \{ x \in E \mid f(x) \geq \alpha \}$$

**Exemple Concret Immédiat :**
Plaçons-nous dans l'espace fonctionnel continu $E = C([0,1], \mathbb{R})$. Considérons la forme linéaire $L(u) = \int_0^1 u(t) dt$. L'ensemble des fonctions de moyenne nulle $H = \{ u \in E \mid L(u) = 0 \}$ est un hyperplan fermé. La fonction constante $u_0(t) = 1$ n'appartient pas à $H$ puisque $L(u_0) = 1$. L'hyperplan translaté $H_1 = \{ u \in E \mid L(u) = 1 \}$ sépare l'espace : la fonction $v(t) = 2t$ a pour intégrale $1$ et appartient à $H_1$.

## 3. Les Théorèmes de Séparation de Hahn-Banach

**Théorème (Hahn-Banach, Première forme géométrique - Séparation large).**
Soit $E$ un espace vectoriel normé réel. Soient $A$ et $B$ deux parties convexes non vides et disjointes de $E$ ($A \cap B = \emptyset$). Si l'un des deux ensembles, disons $A$, est un ouvert de $E$, alors il existe un hyperplan fermé séparant $A$ et $B$ au sens large.
Il existe une forme linéaire continue $f \in E'$ (dual topologique) non nulle et un réel $\alpha \in \mathbb{R}$ tels que :
$$\forall a \in A, f(a) < \alpha \quad \text{et} \quad \forall b \in B, f(b) \geq \alpha$$

**Démonstration Complète :**
Posons $C = A - B = \{ a - b \mid a \in A, b \in B \}$.
Puisque $A$ et $B$ sont convexes, on vérifie que $C$ est convexe. Pour $t \in [0,1]$ et $x, y \in C$ avec $x = a_1 - b_1$ et $y = a_2 - b_2$,
$$tx + (1-t)y = t(a_1 - b_1) + (1-t)(a_2 - b_2) = (ta_1 + (1-t)a_2) - (tb_1 + (1-t)b_2)$$
L'élément de gauche appartient à $A$ et celui de droite à $B$ par convexité, donc le résultat est dans $C$.
De plus, $C = \bigcup_{b \in B} (A - b)$. Puisque $A$ est ouvert, chaque translaté $A - b$ est ouvert, donc $C$ est ouvert.
Puisque $A \cap B = \emptyset$, le vecteur nul $0$ n'appartient pas à $C$.
Puisque $C$ est un ouvert non vide, translatons-le pour qu'il contienne l'origine. Fixons $x_0 \in C$ et considérons $U = C - x_0$. $U$ est un voisinage ouvert convexe de $0$.
On associe à $U$ sa jauge de Minkowski $p(x) = \inf \{ \lambda > 0 \mid x \in \lambda U \}$.
Parce que $U$ est ouvert, $p$ est une fonctionnelle sous-linéaire partout finie, et $x \in U \iff p(x) < 1$.
Le point $-x_0$ n'est pas dans $U$ (car $0 \notin C$), donc $p(-x_0) \geq 1$.
Considérons la droite $D = \mathbb{R}x_0$. On y définit la forme linéaire $g(t x_0) = t p(x_0)$. On vérifie que $g(y) \leq p(y)$ pour tout $y \in D$.
Par le théorème de Hahn-Banach analytique, on prolonge $g$ en une forme linéaire $f$ sur $E$ telle que $f(x) \leq p(x)$ pour tout $x \in E$.
Puisque $U$ est un voisinage de $0$, $p$ est bornée sur une boule, donc $f$ est continue ($f \in E'$).
Pour $x \in U$, on a $f(x) \leq p(x) < 1$.
Puisque $U = C - x_0$, pour tout $c \in C$, $c - x_0 \in U$, donc $f(c - x_0) < 1$, soit $f(c) < 1 + f(x_0)$.
Posons $\alpha = 1 + f(x_0)$. Ainsi pour $a \in A, b \in B$, on a $f(a - b) < \alpha$, donc $f(a) < f(b) + \alpha$.
Considérons l'image de $A$ par $f$, soit $f(A)$. C'est un intervalle de $\mathbb{R}$. Comme $A$ est ouvert et $f$ continue et non nulle, $f(A)$ est un intervalle ouvert.
Étape 1 : $C = A - B$ est convexe, ouvert, et $0 \notin C$.
Étape 2 : L'origine n'étant pas dans l'ouvert $C$, on peut séparer le point $0$ et le convexe ouvert $C$.
Soit $x_0 \in C$. Posons $U = C - x_0$. Alors $U$ est un voisinage ouvert convexe de $0$.
Soit $p$ la jauge de Minkowski de $U$.
Étape 3 : $0 \notin C \implies -x_0 \notin U$. Donc $p(-x_0) \geq 1$.
Étape 4 : Définissons $g$ sur $D = \mathbb{R}(-x_0)$ par $g(-t x_0) = t$.
Pour $t \geq 0$, $g(-t x_0) = t \leq t p(-x_0) = p(-t x_0)$.
Pour $t < 0$, $g(-t x_0) = t < 0 \leq p(-t x_0)$.
Donc $g \leq p$ sur $D$.
Étape 5 : D'après le théorème de Hahn-Banach analytique, on prolonge $g$ en $f \in E^*$ telle que $f \leq p$ sur $E$.
Étape 6 : $f$ est continue. En effet, $U$ contient une boule $B(0, r)$. Pour $x \in B(0, r)$, $p(x) \leq 1$, donc $f(x) \leq 1$, ce qui prouve la continuité.
Étape 7 : Soit $x \in C$. Alors $x - x_0 \in U$. Donc $p(x - x_0) < 1$ (car $U$ ouvert).
Ainsi $f(x - x_0) < 1 \implies f(x) - f(x_0) < 1 \implies f(x) < 1 + f(x_0)$.
Or $f(-x_0) = g(-x_0) = 1 \implies f(x_0) = -1$.
Donc $f(x) < 1 - 1 = 0$.
Étape 8 : Pour tout $a \in A$ et $b \in B$, $a - b \in C$, donc $f(a - b) < 0$, d'où $f(a) < f(b)$.
Soit $\alpha = \sup_{a \in A} f(a)$. On a $\alpha \in \mathbb{R}$ car majoré par $f(b)$.
Alors $\forall a \in A, f(a) \leq \alpha$ et $\forall b \in B, f(b) \geq \alpha$.
Puisque $A$ est ouvert et $f \neq 0$, $f(A)$ est un ouvert de $\mathbb{R}$, donc $f(a)$ ne peut atteindre $\alpha$. Ainsi $f(a) < \alpha$. $\blacksquare$

## 4. Applications en Intelligence Artificielle : Les Séparateurs à Vaste Marge (SVM)

Le théorème de séparation stricte est la pierre angulaire de la théorie de la classification linéaire.

Soit un ensemble d'entraînement constitué de vecteurs $x_i \in \mathbb{R}^n$ étiquetés $y_i \in \{-1, 1\}$.
Définissons les ensembles $X^+ = \{ x_i \mid y_i = 1 \}$ et $X^- = \{ x_i \mid y_i = -1 \}$.
Leurs enveloppes convexes respectives, $C^+$ et $C^-$, sont des polyèdres convexes compacts.
Si les données sont linéairement séparables, alors $C^+ \cap C^- = \emptyset$.
Par le théorème de Hahn-Banach (deuxième forme géométrique stricte, car on sépare un fermé et un compact), il existe un hyperplan d'équation $\langle w, x \rangle + b = 0$ qui sépare strictement $C^+$ et $C^-$.

**Exemple Numérique de Séparation SVM :**
Dans $\mathbb{R}^2$, soient les points de classe positive $A = (1,1)$ et de classe négative $B = (-1,-1)$.
Les ensembles sont des singletons (fermés compacts).
La différence est le vecteur $A-B = (2,2)$. L'hyperplan optimal est orthogonal à ce vecteur.
Posons le vecteur normal $w = (1,1)$. Le milieu est $(0,0)$.
L'équation de l'hyperplan séparateur (la frontière de décision) est $\langle w, x \rangle = x_1 + x_2 = 0$.
Vérifions : pour $A$, $1+1 = 2 > 0$. Pour $B$, $-1-1 = -2 < 0$. La séparation stricte est réalisée.
