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

# Théorème de Hahn-Banach (forme géométrique)

## Introduction et Contexte Géométrique

Le théorème de Hahn-Banach est l'un des piliers fondamentaux de l'analyse fonctionnelle. Si sa forme analytique permet de prolonger des formes linéaires, sa forme géométrique offre une interprétation puissante : la séparation d'ensembles convexes par des hyperplans fermés. Historiquement, ce résultat a émergé de la volonté de comprendre la structure géométrique des espaces vectoriels de dimension infinie, en particulier comment on peut "isoler" ou "découper" des régions de l'espace à l'aide d'applications linéaires continues.

L'intuition physique est immédiate : dans l'espace euclidien usuel $\mathbb{R}^3$, si l'on dispose de deux objets solides (sans creux) qui ne se touchent pas, il est toujours possible de glisser une feuille de papier plane (un plan affine) entre les deux sans toucher aucun des objets. Le théorème de Hahn-Banach généralise cette idée à des espaces vectoriels topologiques, même en dimension infinie.

\begin{center}
\begin{tikzpicture}
    % Convex set A (Open)
    \draw[blue, thick, fill=blue!10] (-2, 0) ellipse (1.5cm and 1cm);
    \node[blue] at (-2, 0) {$A$ (ouvert)};

    % Convex set B (Closed/Compact)
    \draw[red, thick, fill=red!10] (3, 1) circle (1.2cm);
    \node[red] at (3, 1) {$B$};

    % Separating Hyperplane
    \draw[black, thick, dashed] (0, -2) -- (1, 3) node[above right] {Hyperplan séparateur $H$};

    % Normal vector
    \draw[->, thick] (0.5, 0.5) -- (1.5, 0.3) node[right] {$L \in E^*$};
\end{tikzpicture}
\end{center}

Cette capacité de séparation est le fondement de la linéarisation de nombreux problèmes, justifiant que la linéarité est suffisante pour séparer des concepts distincts à condition que la convexité soit respectée.

## Structures Mathématiques et Théorèmes de Séparation

Soit $E$ un espace vectoriel normé sur $\mathbb{R}$ (le résultat s'étend aux espaces localement convexes). On note $E^*$ son dual topologique, c'est-à-dire l'espace des formes linéaires continues sur $E$.

Un **hyperplan affine** fermé dans $E$ est un sous-ensemble de la forme $H = \{ x \in E \mid L(x) = \alpha \}$, où $L \in E^*$ est non nulle et $\alpha \in \mathbb{R}$.

### Séparation au sens large (Première forme géométrique)

**Théorème (Hahn-Banach géométrique - 1ère forme).**
Soient $A$ et $B$ deux parties convexes non vides et disjointes de $E$.
On suppose que $A$ est ouvert.
Alors, il existe un hyperplan fermé séparant $A$ et $B$ au sens large. Autrement dit, il existe une forme linéaire continue $L \in E^*$ non nulle et une constante $\alpha \in \mathbb{R}$ telles que :
$$ \forall a \in A,\ \forall b \in B, \quad L(a) < \alpha \le L(b) $$

**Exemple concret immédiat :**
Plaçons-nous dans $E = \mathbb{R}^2$. Soit $A = \{ (x,y) \in \mathbb{R}^2 \mid x^2 + (y-1)^2 < 1 \}$ (le disque ouvert centré en $(0,1)$ de rayon 1) et $B = \{ (x,y) \in \mathbb{R}^2 \mid y \le 0 \}$ (le demi-plan inférieur fermé).
Ces deux ensembles sont convexes et disjoints, et $A$ est ouvert.
La forme linéaire $L(x,y) = y$ est continue.
Pour tout $a = (x_a, y_a) \in A$, on a $y_a > 0$ et $y_a < 2$. En fait, le disque $A$ a ses ordonnées strictement positives.
Cependant, pour séparer $A$ et $B$, on peut prendre $L(x,y) = -y$.
Ainsi pour $a = (x,y) \in A$, $L(a) = -y < 0$.
Et pour $b = (x,y) \in B$, $L(b) = -y \ge 0$.
En choisissant $\alpha = 0$, on a $L(a) < 0 \le L(b)$. L'hyperplan est la droite d'équation $y = 0$.

### Séparation stricte (Deuxième forme géométrique)

**Théorème (Hahn-Banach géométrique - 2ème forme).**
Soient $A$ et $B$ deux parties convexes non vides et disjointes de $E$.
On suppose que $A$ est fermée et $B$ est compacte.
Alors, il existe un hyperplan fermé séparant strictement $A$ et $B$. C'est-à-dire qu'il existe $L \in E^*$ non nulle et des réels $\alpha, \epsilon > 0$ tels que :
$$ \forall a \in A,\ \forall b \in B, \quad L(a) \le \alpha - \epsilon < \alpha < \alpha + \epsilon \le L(b) $$

**Exemple concret immédiat :**
Toujours dans $E = \mathbb{R}^2$. Considérons la branche d'hyperbole $A = \{ (x,y) \in \mathbb{R}^2 \mid x > 0,\ y \ge 1/x \}$ (ensemble convexe fermé) et le point $B = \{ (0,0) \}$ (ensemble compact).
Les deux ensembles sont disjoints.
Choisissons la forme linéaire $L(x,y) = x + y$.
Pour $b \in B$, $L(b) = 0$.
Pour $a = (x,y) \in A$, $L(a) = x + y \ge x + 1/x$. La fonction $x \mapsto x + 1/x$ pour $x>0$ atteint son minimum en $x=1$, qui vaut 2. Donc $L(a) \ge 2$.
Ainsi, en prenant $\alpha = 1$ et $\epsilon = 0.5$, on a :
$L(b) = 0 \le 0.5 = \alpha - \epsilon < \alpha = 1 < 1.5 = \alpha + \epsilon \le L(a)$.
On a une séparation stricte avec une marge d'au moins 0.5 de chaque côté de l'hyperplan d'équation $x+y = 1$.

### Conséquences immédiates

Un corollaire fondamental est que tout ensemble convexe fermé $C$ de $E$ est l'intersection de tous les demi-espaces fermés qui le contiennent. Si $x_0 \notin C$, on peut toujours séparer strictement $x_0$ de $C$.

\begin{center}
\begin{tikzpicture}[scale=0.8]
    % Convex set C (Closed)
    \filldraw[fill=green!20, draw=green!60!black, thick] (-1, -1) -- (2, -1) -- (3, 1) -- (0, 2) -- cycle;
    \node[green!40!black] at (1, 0) {$C$ (fermé)};

    % Point x_0
    \filldraw[black] (4, -0.5) circle (2pt) node[right] {$x_0 \notin C$};

    % Separating lines
    \draw[blue, thick] (2.5, -2) -- (2.5, 2) node[above] {$H_1$};
    \draw[red, thick, dashed] (3.5, 1.5) -- (3, -2) node[below] {$H_2$};
\end{tikzpicture}
\end{center}

## Démonstrations Exhaustives

### Preuve de la première forme géométrique

Nous nous appuyons sur la jauge de Minkowski et le théorème de Hahn-Banach analytique.

1. **Translation :** On choisit $a_0 \in A$ et $b_0 \in B$. On pose $x_0 = b_0 - a_0$. On définit l'ensemble $C = A - B + x_0$.
   Alors $C$ est l'ensemble des éléments de la forme $a - b + x_0$ pour $a \in A, b \in B$.
   $C$ est un ouvert car il s'écrit $C = \bigcup_{b \in B} (A - b + x_0)$, qui est une union d'ouverts (translatés de l'ouvert $A$).
   De plus, $C$ est convexe comme somme d'ensembles convexes.
   Par construction, $a_0 - b_0 + x_0 = 0 \in C$.

2. **Utilisation de la jauge :** Puisque $C$ est un voisinage convexe de $0$, sa jauge de Minkowski $p(x) = \inf\{ \lambda > 0 \mid \frac{x}{\lambda} \in C \}$ est bien définie, partout finie, et sous-linéaire (sous-additive et positivement homogène).
   De plus, comme $C$ est ouvert, on a l'équivalence exacte : $x \in C \iff p(x) < 1$.

3. **Disjonction et point $x_0$ :** On sait que $x_0 \notin C$. En effet, si $x_0 \in C$, alors $x_0 = a - b + x_0$ pour certains $a \in A, b \in B$, ce qui impliquerait $a = b$, contredisant l'hypothèse de disjonction $A \cap B = \emptyset$.
   Puisque $x_0 \notin C$, la propriété de la jauge donne $p(x_0) \ge 1$.

4. **Forme linéaire sur une droite :** Considérons le sous-espace $G = \mathbb{R}x_0$. On définit sur $G$ la forme linéaire $f(t x_0) = t p(x_0)$.
   Pour $t \ge 0$, $f(t x_0) = t p(x_0) = p(t x_0)$.
   Pour $t < 0$, $f(t x_0) = t p(x_0) \le 0 \le p(t x_0)$ (car $p \ge 0$).
   Ainsi, pour tout $x \in G$, $f(x) \le p(x)$.

5. **Prolongement par Hahn-Banach analytique :** D'après le théorème de Hahn-Banach analytique, il existe une forme linéaire $L$ sur $E$ qui prolonge $f$ et telle que $\forall x \in E, L(x) \le p(x)$.

6. **Continuité de $L$ :** L'ouvert $C$ contient une boule ouverte $B(0, r)$. Pour $x \in B(0, r)$, $x \in C$ donc $p(x) < 1$. Par conséquent, $L(x) \le p(x) < 1$. Puisque $L(-x) \le p(-x) < 1$, on a $|L(x)| < 1$ sur la boule $B(0,r)$, ce qui prouve que $L$ est continue sur un voisinage de 0, donc continue partout ($L \in E^*$).

7. **Séparation :** Pour tout $a \in A$ et $b \in B$, regardons l'élément $x = a - b + x_0 \in C$.
   On a $p(x) < 1$, donc $L(x) < 1$.
   Par linéarité, $L(a) - L(b) + L(x_0) < 1$.
   Or, $L(x_0) = f(x_0) = p(x_0) \ge 1$.
   Donc $L(a) - L(b) + 1 \le L(a) - L(b) + L(x_0) < 1$, ce qui implique $L(a) - L(b) < 0$, soit $L(a) < L(b)$.

8. **Fixation de la constante :** L'ensemble $L(A)$ est un intervalle de $\mathbb{R}$ (image d'un connexe par une application continue). Comme $L(A) < L(B)$, la borne supérieure de $L(A)$ existe et est majorée par tout élément de $L(B)$.
   De plus, $A$ est ouvert et $L$ est linéaire continue non nulle, donc $L(A)$ est un ouvert de $\mathbb{R}$. Par conséquent, sa borne supérieure n'est pas atteinte.
   Soit $\alpha = \sup L(A)$. Pour tout $a \in A$, on a $L(a) < \alpha$. Pour tout $b \in B$, on a $\alpha \le L(b)$. La preuve est complète.

### Preuve de la deuxième forme géométrique

Supposons $A$ fermé et $B$ compact disjoints.

1. **Élargissement :** Puisque $A$ est fermé et $B$ est compact et $A \cap B = \emptyset$, la distance entre $A$ et $B$ est strictement positive (dans un espace normé). Plus généralement dans un espace localement convexe, il existe un voisinage ouvert convexe de l'origine $V$ tel que $(A + V) \cap B = \emptyset$.
   L'ensemble $A' = A + V$ est ouvert (union d'ouverts $a+V$), convexe (somme de convexes), et disjoint de $B$.

2. **Application de la 1ère forme :** Par le théorème de séparation au sens large, il existe $L \in E^*$ et un réel $\alpha'$ tels que :
   $\forall x \in A', \forall b \in B, \quad L(x) < \alpha' \le L(b)$.
   En particulier, pour tout $a \in A$ et $v \in V$, $L(a) + L(v) < \alpha'$.

3. **Marge stricte :** L'ensemble $L(V)$ est un voisinage ouvert de $0$ dans $\mathbb{R}$, donc il contient un intervalle $[-\epsilon, \epsilon]$ pour un $\epsilon > 0$.
   On peut donc trouver $v \in V$ tel que $L(v) = \epsilon$.
   Ainsi, $\forall a \in A, \quad L(a) + \epsilon < \alpha'$.
   En posant $\alpha = \alpha' - \epsilon$, on obtient $L(a) \le \alpha < \alpha + \epsilon = \alpha' \le L(b)$.
   L'inégalité stricte est démontrée.



**Exemple concret supplémentaire 1 (Orthogonalité dans Hilbert) :**
Soit $E = \ell^2(\mathbb{R})$ l'espace des suites de carré sommable. Considérons le sous-espace fermé $C = \{ x \in \ell^2 \mid x_1 = x_2 \}$. C'est un convexe fermé. Le point $x_0 = (1, 0, 0, \dots) \notin C$.
Le point de $C$ le plus proche de $x_0$ est sa projection orthogonale $p = (\frac{1}{2}, \frac{1}{2}, 0, \dots)$.
L'hyperplan séparateur strict garanti par Hahn-Banach a pour vecteur normal $x_0 - p = (\frac{1}{2}, -\frac{1}{2}, 0, \dots)$.
La forme linéaire est $L(x) = \frac{1}{2}x_1 - \frac{1}{2}x_2$. Pour $c \in C$, $L(c) = 0$. Pour $x_0$, $L(x_0) = \frac{1}{2} > 0$. L'hyperplan affine $H = \{ x \mid L(x) = \frac{1}{4} \}$ sépare strictement $x_0$ de $C$.

**Exemple concret supplémentaire 2 (Séparation de boules) :**
Dans $E = \mathbb{R}^n$, soient $B_1$ la boule fermée de centre $c_1$ et de rayon $r_1$, et $B_2$ la boule fermée de centre $c_2$ et de rayon $r_2$. Supposons $\|c_1 - c_2\| > r_1 + r_2$, c'est-à-dire que les boules sont disjointes.
La forme linéaire $L(x) = \langle c_2 - c_1, x \rangle$ sépare strictement $B_1$ et $B_2$.
Le supremum de $L$ sur $B_1$ est atteint au point $x_1 = c_1 + r_1 \frac{c_2 - c_1}{\|c_2 - c_1\|}$.
L'infimum de $L$ sur $B_2$ est atteint au point $x_2 = c_2 - r_2 \frac{c_2 - c_1}{\|c_2 - c_1\|}$.
La séparation stricte est géométriquement l'hyperplan médiateur du segment $[x_1, x_2]$.

**Exemple concret supplémentaire 3 (Non-séparabilité de non-convexes) :**
Prenons dans $\mathbb{R}^2$ l'ensemble $A = \{ (x,y) \mid x^2 + y^2 = 1 \}$ (le cercle) et l'ensemble $B = \{ (0,0) \}$ (le centre). $A$ et $B$ sont fermés et disjoints, mais $A$ n'est pas convexe.
Il n'existe aucune droite séparant $A$ et $B$, illustrant que la convexité est une condition nécessaire absolue de Hahn-Banach géométrique.


## Applications

### 1. Théorie de l'Optimisation et Conditions KKT
En optimisation sous contraintes, le théorème de Hahn-Banach géométrique est la pierre angulaire pour l'existence des multiplicateurs de Lagrange (et les conditions de Karush-Kuhn-Tucker). On sépare l'ensemble des directions de descente admissibles de l'ensemble des directions où la fonction objectif décroît, garantissant l'existence d'un hyperplan (défini par les multiplicateurs) qui équilibre les gradients.

**Exemple Numérique de projection sur un convexe :**
Soit $C = \{ (x,y) \in \mathbb{R}^2 \mid x^2 + y^2 \le 1 \}$ (disque unité fermé) et $x_0 = (2,2)$.
Le point de $C$ le plus proche de $x_0$ est $p_0 = (\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}})$.
Le théorème garantit qu'il existe un hyperplan séparant strictement $C$ de $x_0$. En prenant la tangente à $C$ en $p_0$, d'équation $x + y = \sqrt{2}$, on a pour tout $(x,y) \in C$, $x+y \le \sqrt{2}$ (car $(x+y)/\sqrt{2} = \langle (x,y), p_0 \rangle \le \|(x,y)\|\|p_0\| \le 1$).
Pour le point $x_0$, on a $2+2 = 4 > \sqrt{2}$. La séparation est donc stricte avec le plan affine orthogonal au segment $[p_0, x_0]$.

### 2. Intelligence Artificielle : Les Support Vector Machines (SVM)
En apprentissage supervisé, le problème de la classification binaire linéaire consiste exactement à trouver un hyperplan séparateur entre deux nuages de points.
Si les deux nuages d'entraînement (de classes $+1$ et $-1$) ont des enveloppes convexes disjointes, le théorème de séparation stricte assure qu'il existe un hyperplan $H = \{ x \mid \langle w, x \rangle + b = 0 \}$ qui sépare ces deux ensembles avec une marge positive stricte.
Le SVM à marge maximale trouve parmi tous ces hyperplans séparateurs garantis par Hahn-Banach celui qui maximise $\epsilon$.

### 3. Logique et dualité forte
En théorie des jeux (par exemple le théorème du minimax de von Neumann) et en économie (équilibres de Walras), on utilise la séparation de convexes pour montrer l'existence de systèmes de prix ou de stratégies mixtes. Le fait que deux ensembles d'opportunités ne s'intersectent pas garantit l'existence d'un système de prix (la forme linéaire) tel qu'un acteur préfère toujours un ensemble à l'autre.
