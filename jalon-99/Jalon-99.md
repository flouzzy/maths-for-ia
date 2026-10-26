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

# Jalon 99 : Théorème de Hahn-Banach (forme géométrique)

## Présentation du concept clé




## Formalisation

Soit $E$ un espace vectoriel normé (ou un espace topologique localement convexe).

### Séparation au sens large

> **Théorème (Hahn-Banach - 1ère forme géométrique) :**
> Soient $A$ et $B$ deux ensembles **convexes** non vides et **disjoints** de $E$.
> Si $A$ est **ouvert**, alors il existe une forme linéaire continue $L \in E^*$ non nulle et un réel $\alpha$ tels que :
> $$\forall a \in A, \forall b \in B, \quad L(a) < \alpha \le L(b)$$
> On dit que l'hyperplan $\{ x \mid L(x) = \alpha \}$ sépare $A$ et $B$ au sens large.


**Exemple 1 : Séparation au sens large en 1D**
Soit $E=\mathbb{R}$. Soit $A = ]-\infty, 0[$ (un ouvert convexe) et $B = [0, +\infty[$ (un convexe). $A$ et $B$ sont disjoints.
D'après le théorème de séparation au sens large, il existe $L \in \mathbb{R}^*$ et $\alpha \in \mathbb{R}$ tels que $L(a) < \alpha \le L(b)$ pour $a\in A, b\in B$.
Une forme linéaire sur $\mathbb{R}$ est de la forme $L(x) = kx$.
Prenons $k=1$, donc $L(x) = x$. Si on choisit $\alpha = 0$, on a :
$\forall a < 0, L(a) = a < 0$
$\forall b \ge 0, L(b) = b \ge 0$.
L'hyperplan est ici le point $\{0\}$ qui sépare les deux ensembles.

**Exemple 2 : Séparation au sens large dans $\mathbb{R}^2$**
Soit $A = \{ (x,y) \mid x < 0 \}$ et $B = \{ (x,y) \mid x \ge 0 \}$. $A$ est ouvert. $A \cap B = \emptyset$. L'axe des ordonnées $x=0$ est un hyperplan séparateur (forme linéaire $L(x,y)=x$, $\alpha=0$).


\begin{center}
\begin{tikzpicture}[scale=1.2]
  % Convex set A
  \fill[blue!20] (-2,0) ellipse (1.5 and 1);
  \draw[blue, thick] (-2,0) ellipse (1.5 and 1);
  \node[blue] at (-2,0) {$A$ (Ouvert)};

  % Convex set B
  \fill[red!20] (2,1) -- (3,-1) -- (4,2) -- cycle;
  \draw[red, thick] (2,1) -- (3,-1) -- (4,2) -- cycle;
  \node[red] at (3,0.5) {$B$};

  % Separating Hyperplane
  \draw[thick, dashed, black] (0.5, -2) -- (0.5, 2) node[above] {$L(x) = \alpha$};

  % Annotations
  \node at (-0.5, 1.5) {$L(x) < \alpha$};
  \node at (1.5, 1.5) {$L(x) \ge \alpha$};
\end{tikzpicture}
\end{center}


### Séparation stricte

> **Théorème (Hahn-Banach - 2ème forme géométrique) :**
> Soient $A$ et $B$ deux ensembles **convexes** non vides et **disjoints**.
> Si $A$ est **fermé** et $B$ est **compact**, alors il existe $L \in E^*$ et deux réels $\alpha, \epsilon > 0$ tels que :
> $$\forall a \in A, \forall b \in B, \quad L(a) \le \alpha - \epsilon < \alpha + \epsilon \le L(b)$$
> Ici, il existe une "marge de sécurité" entre les deux ensembles et l'hyperplan.


**Exemple 3 : Séparation stricte dans le plan**
Soit $E=\mathbb{R}^2$. Soit $A$ le disque unité fermé $A = \{ (x,y) \mid x^2+y^2 \le 1 \}$ (compact et convexe).
Soit $B$ la demi-droite fermée $B = \{ (x,y) \mid x \ge 2, y=0 \}$ (fermé et convexe). $A$ et $B$ sont disjoints.
Puisque l'un est compact et l'autre fermé, on peut les séparer strictement.
On cherche $L(x,y) = w_1 x + w_2 y$ et $\alpha$.
L'hyperplan vertical $x = 1.5$ sépare $A$ et $B$.
La forme linéaire correspondante est $L(x,y) = x$.
Pour $a = (x,y) \in A$, on a $L(a) = x \le 1$.
Pour $b = (x,0) \in B$, on a $L(b) = x \ge 2$.
En prenant $\alpha = 1.5$ et $\epsilon = 0.5$, on a :
$L(a) \le 1 = \alpha - \epsilon < \alpha + \epsilon = 2 \le L(b)$.
La séparation stricte est démontrée, et la "marge" de séparation est matérialisée par $\epsilon$.

**Exemple 4 : SVM (Support Vector Machine) et Hahn-Banach**
En classification binaire, si on a un nuage de points "rouges" et un nuage de points "bleus" dans $\mathbb{R}^n$, on considère l'enveloppe convexe des rouges ($A$) et l'enveloppe convexe des bleus ($B$).
Si l'échantillon est linéairement séparable, $A$ et $B$ sont des polygones convexes disjoints (donc compacts).
La 2ème forme géométrique de Hahn-Banach garantit l'existence d'un hyperplan (et donc d'un classifieur linéaire $w^Tx+b=0$) séparant strictement les classes avec une marge $\epsilon > 0$. L'algorithme SVM trouve l'hyperplan qui maximise cet $\epsilon$.


\begin{center}
\begin{tikzpicture}[scale=1.5]
  % Convex Set A (Compact)
  \fill[blue!20] (-1.5, 0) circle (0.8);
  \draw[blue, thick] (-1.5, 0) circle (0.8);
  \node[blue] at (-1.5, 0) {$A$ (Compact)};

  % Point x_0 (Fermé)
  \fill[red] (1, 0.5) circle (1.5pt);
  \node[red, right] at (1, 0.5) {$x_0$};
  \node[red, below] at (1, 0.4) {$B = \{x_0\}$ (Fermé)};

  % Strict Separating Hyperplanes
  \draw[thick, dashed, black] (-0.2, -1.5) -- (-0.2, 1.5) node[above] {$L(x) = \alpha - \epsilon$};
  \draw[thick, black] (0.2, -1.5) -- (0.2, 1.5) node[above] {$L(x) = \alpha$};
  \draw[thick, dashed, black] (0.6, -1.5) -- (0.6, 1.5) node[above] {$L(x) = \alpha + \epsilon$};

  \draw[<->] (-0.2, -1) -- (0.2, -1) node[midway, below] {$\epsilon$};
  \draw[<->] (0.2, -1) -- (0.6, -1) node[midway, below] {$\epsilon$};

\end{tikzpicture}
\end{center}


## Démonstrations

### Lien avec la forme analytique : La Jauge de Minkowski

Pour prouver la forme géométrique, on transforme un ensemble convexe en une fonction sous-linéaire.

1. **La Jauge :** Soit $C$ un convexe ouvert contenant 0. On définit la jauge de $C$ par :
   $$j_C(x) = \inf \{ t > 0 \mid x/t \in C \}$$


**Exemple 5 : Jauge de Minkowski pour la boule unité**
Considérons l'espace normé usuel $\mathbb{R}^2$ et soit $C$ la boule ouverte de rayon $R=2$, centrée en l'origine $C = \{ (x,y) \in \mathbb{R}^2 \mid \sqrt{x^2+y^2} < 2 \}$. $C$ est un ouvert convexe contenant $0$.
Calculons la jauge $j_C(u)$ pour le vecteur $u=(3,4)$.
On cherche $t > 0$ tel que $u/t \in C$.
La norme de $u$ est $\sqrt{3^2+4^2} = 5$.
La condition s'écrit $\left\| \frac{1}{t}(3,4) \right\| < 2$, ce qui donne $\frac{5}{t} < 2 \implies t > 2.5$.
L'infimum de ces $t$ est $2.5$. Donc, $j_C(3,4) = 2.5$.
On remarque que $j_C(u) = \frac{\|u\|}{2}$. Puisque $j_C(3,4) > 1$, $u \notin C$.

2. **Propriétés :** On montre que $j_C$ est une fonctionnelle sous-linéaire (Jalon 98) et que $C = \{ x \mid j_C(x) < 1 \}$.
3. **Application de Hahn-Banach analytique :**
   - On définit une forme linéaire sur un petit espace (ex: une droite passant par un point hors de $C$).
   - On l'étend à tout l'espace en restant sous la jauge $j_C$.

**Démonstration détaillée de la 1ère forme géométrique :**

1. Fixons un point $a_0 \in A$ et $b_0 \in B$. Posons $x_0 = b_0 - a_0$. Remarquons que $x_0 \neq 0$ car $A \cap B = \emptyset$.
2. Considérons l'ensemble $C = A - B + x_0$. C'est-à-dire l'ensemble des vecteurs de la forme $a - b + x_0$ pour $a \in A, b \in B$.
3. $C$ est convexe car c'est une combinaison linéaire d'ensembles convexes.
4. $C$ est un voisinage ouvert de $0$ (car $A$ est ouvert, la translation d'un ouvert par $-b+x_0$ est un ouvert, et une union d'ouverts est ouverte).
5. Remarquons que $x_0 \notin C$. Si on avait $x_0 \in C$, alors $x_0 = a - b + x_0 \implies a=b$, ce qui contredit $A \cap B = \emptyset$.
6. Introduisons la jauge de Minkowski $j_C$ associée au convexe $C$. Puisque $C$ est un voisinage ouvert de 0, $j_C$ est bien définie et vérifie l'inégalité triangulaire (sous-linéarité).
7. Comme $x_0 \notin C$, par définition de la jauge, on a $j_C(x_0) \ge 1$.
8. On définit une forme linéaire $f$ sur la droite vectorielle $D = \mathbb{R}x_0$ par $f(t x_0) = t$.
9. Montrons que sur cette droite, $f \le j_C$.
   - Si $t > 0$, $f(tx_0) = t$. Or, $j_C(tx_0) = t j_C(x_0) \ge t = f(tx_0)$.
   - Si $t \le 0$, $f(tx_0) = t \le 0 \le j_C(tx_0)$ car la jauge est à valeurs positives.
10. D'après le théorème de Hahn-Banach sous sa forme analytique, il existe un prolongement linéaire $L$ de $f$ à $E$ tout entier tel que $\forall x \in E, L(x) \le j_C(x)$.
11. Remarquons que pour tout $x \in C$, $j_C(x) < 1$. Donc, $L(x) \le j_C(x) < 1$ sur $C$.
12. Soit $a \in A$ et $b \in B$. Le vecteur $a - b + x_0 \in C$, d'où $L(a - b + x_0) < 1$.
13. Par linéarité, $L(a) - L(b) + L(x_0) < 1$. Comme $L(x_0) = f(x_0) = 1$, cela donne $L(a) - L(b) + 1 < 1 \implies L(a) < L(b)$.
14. L'image $L(A)$ est un sous-ensemble convexe de $\mathbb{R}$ (un intervalle). L'image $L(B)$ l'est également. D'après ce qui précède, tout élément de $L(A)$ est strictement inférieur à tout élément de $L(B)$.
15. Il suffit de poser $\alpha = \sup_{a \in A} L(a)$ pour obtenir $L(a) < \alpha \le L(b)$. L'inégalité stricte à gauche vient du fait que $A$ est ouvert (l'image d'un ouvert par une application linéaire non nulle sur $\mathbb{R}$ est un intervalle ouvert).



## Exercices d'Application

### Exercice 1 : Séparation d'un point et d'un fermé
**Énoncé :** Soit $C$ un convexe fermé et $x_0 \notin C$. Montrer qu'on peut séparer strictement $x_0$ de $C$.
**Correction Détaillée :**
1. $\{x_0\}$ est un ensemble compact (car fini).
2. $C$ est un ensemble fermé.
3. Les deux sont disjoints et convexes.
4. Par la 2ème forme géométrique de Hahn-Banach, il existe un hyperplan séparateur strict.
**Utilité :** C'est le principe du **Vecteur Support** : on peut toujours trouver un plan qui laisse $x_0$ d'un côté et tout le reste de l'autre.

### Exercice 2 : Niveau Avancé (Théorème du point fixe de Kakutani)
**Énoncé :** Pourquoi la convexité est-elle indispensable ?
**Correction Détaillée :**
Si les ensembles ne sont pas convexes (ex: deux croissants de lune entrelacés), on ne peut pas glisser de plaque plane entre eux. On pourrait avoir besoin d'une surface courbe. Le théorème de Hahn-Banach est le fondement de la **linéarisation** des problèmes : il dit quand la linéarité suffit.

## Application en Intelligence Artificielle

- **Le Pont Théorique :** Le succès des **Support Vector Machines (SVM)** repose entièrement sur ce jalon. Trouver la "marge maximale" est exactement ce que décrit la 2ème forme géométrique.
- **Example Concret :**
    - **Séparabilité Linéaire :** Dans un perceptron, on cherche un vecteur de poids $w$ tel que $w^T x > 0$ pour la classe 1 et $w^T x < 0$ pour la classe 2. Hahn-Banach garantit que si les enveloppes convexes des deux classes ne se touchent pas, un tel $w$ existe.
    - **Dualité forte en Deep Learning :** Pour analyser les paysages de perte, on regarde si un minimum local est "séparable" des autres par un hyperplan dans l'espace des fonctions. Cela aide à comprendre la géométrie des réseaux de neurones.
    - **Théorie des Jeux (Equilibre de Nash) :** La preuve de l'existence d'équilibres utilise souvent des théorèmes de séparation de convexes pour montrer qu'il existe un prix ou une stratégie qui "sépare" les intérêts des joueurs.

## Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 98 (Théorème de Hahn-Banach (forme analytique)).md]], [[Jalon 121 (Ensembles convexes).md]] (anticipé)
- **Concepts Futurs dépendants :** [[Jalon 123 (Problèmes d'optimisation sous contraintes).md]], [[Jalon 124 (Conditions de Karush-Kuhn-Tucker).md]]
