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

## 1. Origines et intuition du théorème

L'invention des formes géométriques du théorème de Hahn-Banach s'inscrit dans la volonté de formaliser la notion de "séparation" dans des espaces abstraits de dimension infinie. Le défi initial était de transposer une évidence géométrique euclidienne en dimension 2 ou 3 : si l'on dispose de deux solides convexes (sans creux) qui ne se chevauchent pas, on peut glisser un plan (ou une droite dans le plan) entre eux, de sorte que l'un se trouve strictement d'un côté du plan, et l'autre de l'autre.

Cette intuition visuelle extrêmement puissante – séparer des ensembles par des "hyperplans" – s'avère fondamentale en analyse fonctionnelle. Elle a été construite et généralisée indépendamment par Hans Hahn (1927) et Stefan Banach (1929). Dans des espaces de dimension infinie, la séparation géométrique permet de garantir l'existence de formes linéaires continues ayant des propriétés prescrites, c'est-à-dire de garantir que le dual topologique de l'espace est "suffisamment riche". Le théorème de Hahn-Banach sous sa forme géométrique n'est rien d'autre que l'assurance qu'un espace vectoriel normé (ou localement convexe) possède suffisamment d'hyperplans fermés pour séparer les ensembles convexes disjoints.

L'importance de cette séparation s'étend bien au-delà de l'analyse pure. En apprentissage automatique et en optimisation, séparer des classes de données ou distinguer le domaine d'admissibilité d'un optimum sont des problèmes canoniques qui reposent sur ce même socle géométrique.

## 2. Définitions, structures et hyperplans

Avant d'énoncer le théorème de séparation, nous devons formaliser rigoureusement les objets manipulés : les hyperplans affines fermés et la notion géométrique de séparation.

**Définition (Hyperplan affine) :**
Soit $E$ un $\mathbb{R}$-espace vectoriel. Un sous-espace affine $H \subset E$ est un **hyperplan affine** s'il existe une forme linéaire non nulle $f : E \to \mathbb{R}$ et un scalaire $\alpha \in \mathbb{R}$ tels que :
$$ H = \{x \in E \mid f(x) = \alpha\} $$
L'hyperplan affine $H$ divise l'espace $E$ en deux demi-espaces stricts : $E_< = \{x \in E \mid f(x) < \alpha\}$ et $E_> = \{x \in E \mid f(x) > \alpha\}$.

**Lemme topologique de l'hyperplan :**
Si $E$ est un espace vectoriel normé (EVN), un hyperplan affine $H = f^{-1}(\{\alpha\})$ est **fermé** si et seulement si la forme linéaire $f$ est **continue**.

*Exemple concret (Calcul matriciel direct) :*
Considérons $E = \mathbb{R}^3$. Soit $f(x, y, z) = 2x - y + 3z$. $f$ est une forme linéaire continue. L'hyperplan affine $H$ d'équation $2x - y + 3z = 5$ est fermé. Le vecteur $u = (1, 0, 1)$ a pour image $f(u) = 2(1) - 0 + 3(1) = 5$, donc $u \in H$. Le vecteur $v = (0, 0, 0)$ a pour image $f(v) = 0 < 5$, donc $v$ appartient au demi-espace inférieur strict.

**Définition (Séparation au sens large et au sens strict) :**
Soient $A$ et $B$ deux parties non vides de $E$.
On dit que l'hyperplan $H = \{x \in E \mid f(x) = \alpha\}$ sépare $A$ et $B$ :
1. **Au sens large** si :
$$ \forall a \in A, \ f(a) \le \alpha \quad \text{et} \quad \forall b \in B, \ f(b) \ge \alpha $$
2. **Au sens strict** s'il existe $\epsilon > 0$ tel que :
$$ \forall a \in A, \ f(a) \le \alpha - \epsilon \quad \text{et} \quad \forall b \in B, \ f(b) \ge \alpha + \epsilon $$

## 3. Théorèmes de séparation et exemples concrets

Nous pouvons à présent formuler les deux versions géométriques fondamentales du théorème de Hahn-Banach, souvent attribuées en partie à Eidelheit et Kakutani, bien que dérivées des formes analytiques.

### A. Séparation au sens large (Théorème d'Eidelheit)

**Théorème (Hahn-Banach géométrique - 1ère forme, séparation large) :**
Soit $E$ un $\mathbb{R}$-espace vectoriel normé. Soient $A$ et $B$ deux parties de $E$ convexes, non vides et disjointes ($A \cap B = \emptyset$).
Si l'un des deux ensembles, par exemple $A$, est **ouvert**, alors il existe un hyperplan affine fermé qui sépare $A$ et $B$ au sens large. Autrement dit, il existe une forme linéaire continue $f \in E'$ (non nulle) et une constante $\alpha \in \mathbb{R}$ telles que :
$$ \forall a \in A, \ f(a) < \alpha \le \inf_{b \in B} f(b) $$

*Exemple concret géométrique :*
Dans $E = \mathbb{R}^2$, posons $A = \{(x, y) \in \mathbb{R}^2 \mid x^2 + (y-2)^2 < 1\}$ (disque ouvert centré en $(0,2)$ de rayon 1, convexe et ouvert) et $B = \{(x, y) \in \mathbb{R}^2 \mid y \le 0\}$ (le demi-plan inférieur, fermé et convexe). $A \cap B = \emptyset$.
Considérons la forme linéaire $f(x, y) = y$.
Pour $a = (x, y) \in A$, on a $y - 2 < 1 \implies y < 3$. Plus précisément, $\sup_{A} f = \sup_{(x,y) \in A} y = 3$.
Pour $b = (x, y) \in B$, on a $y \le 0$, donc $\inf_{B} f = 0$.
L'inégalité $f(a) \le \alpha \le f(b)$ ne fonctionne pas telle quelle car $\sup A > \inf B$.
Prenons plutôt $f(x, y) = -y$.
Alors pour $a \in A$, $f(a) = -y \in (-3, -1)$.
Et pour $b \in B$, $f(b) = -y \ge 0$.
Choisissons $\alpha = -\frac{1}{2}$.
On a bien $\forall a \in A, f(a) < -1 < -1/2 = \alpha$ et $\forall b \in B, f(b) \ge 0 \ge \alpha$. L'hyperplan affine $H : -y = -1/2 \iff y = 1/2$ sépare $A$ et $B$ au sens large (et même strict ici).

### B. Séparation au sens strict

**Théorème (Hahn-Banach géométrique - 2ème forme, séparation stricte) :**
Soit $E$ un $\mathbb{R}$-espace vectoriel normé. Soient $A$ et $B$ deux parties de $E$ convexes, non vides et disjointes.
Si $A$ est **fermé** et $B$ est **compact**, alors il existe un hyperplan affine fermé qui sépare $A$ et $B$ **au sens strict**. Autrement dit, il existe $f \in E'$ (continue, non nulle), $\alpha \in \mathbb{R}$ et $\epsilon > 0$ tels que :
$$ \forall a \in A, \ f(a) \le \alpha - \epsilon < \alpha < \alpha + \epsilon \le f(b), \quad \forall b \in B $$

*Contre-exemple (Pourquoi la compacité est requise) :*
Dans $E = \mathbb{R}^2$, soient $A = \{(x, y) \in \mathbb{R}^2 \mid x \le 0\}$ (demi-plan fermé) et $B = \{(x, y) \in \mathbb{R}^2 \mid x > 0, y \ge 1/x\}$ (branche d'hyperbole avec sa zone supérieure).
$A$ et $B$ sont des convexes fermés disjoints. Cependant, $B$ n'est pas compact (il n'est pas borné).
L'axe des ordonnées ($x=0$) sépare $A$ et $B$ au sens large : pour $a \in A$, $x_a \le 0$, et pour $b \in B$, $x_b > 0$.
Mais il est impossible de les séparer strictement. La distance $\inf_{a \in A, b \in B} ||a - b||$ est nulle car les points de $B$ pour $y \to +\infty$ s'approchent infiniment de l'axe des ordonnées. L'hyperplan "optimal" est $x=0$, mais il ne sépare pas strictement au sens de Hahn-Banach, car on ne peut trouver de marge $\epsilon > 0$.

## 4. Démonstrations exhaustives

Nous allons démontrer la première forme géométrique de Hahn-Banach (séparation large), en admettant la forme analytique de Hahn-Banach.

**Preuve du Théorème de séparation au sens large :**

Soit $E$ un espace vectoriel normé sur $\mathbb{R}$. Soient $A, B \subset E$ deux ensembles convexes, non vides, disjoints, et supposons $A$ ouvert.

**Étape 1 : Se ramener à l'origine et construire la jauge d'un convexe.**
On choisit $a_0 \in A$ et $b_0 \in B$.
On définit $x_0 = b_0 - a_0$. Remarquons que $x_0 \neq 0$ car $A$ et $B$ sont disjoints.
Définissons le nouvel ensemble :
$$ C = A - B + x_0 = \{ a - b + x_0 \mid a \in A, b \in B \} $$
$C$ possède les propriétés suivantes :
1. **$C$ est ouvert :** En effet, $C = \bigcup_{b \in B} (A - b + x_0)$. Or, une translation préserve l'ouverture, donc chaque $A - b + x_0$ est un ouvert (puisque $A$ l'est). L'union d'ouverts est un ouvert.
2. **$C$ est convexe :** Soient $c_1, c_2 \in C$. $c_i = a_i - b_i + x_0$. Pour $t \in [0,1]$ :
$t c_1 + (1-t) c_2 = t(a_1 - b_1 + x_0) + (1-t)(a_2 - b_2 + x_0)$
$t c_1 + (1-t) c_2 = (ta_1 + (1-t)a_2) - (tb_1 + (1-t)b_2) + x_0$
Puisque $A$ et $B$ sont convexes, le premier terme est dans $A$ et le second dans $B$. Donc la combinaison linéaire convexe appartient à $C$.
3. **$0 \in C$ :** car $a_0 - b_0 + x_0 = a_0 - b_0 + (b_0 - a_0) = 0$.
4. **$x_0 \notin C$ :** Supposons par l'absurde que $x_0 \in C$. Alors il existe $a \in A, b \in B$ tels que $x_0 = a - b + x_0$, ce qui implique $a = b$. C'est absurde car $A \cap B = \emptyset$.

**Étape 2 : Utilisation de la jauge de Minkowski.**
Puisque $C$ est un ouvert contenant $0$, il existe une boule ouverte centrée en $0$ de rayon $r > 0$ incluse dans $C$, soit $B(0, r) \subset C$.
Pour tout $x \in E$, on définit la jauge (fonctionnelle de Minkowski) $p_C$ par :
$$ p_C(x) = \inf \{\lambda > 0 \mid x \in \lambda C \} $$
Propriétés de la jauge $p_C$ :
- $p_C(\alpha x) = \alpha p_C(x)$ pour $\alpha \ge 0$ (positivité homogène).
- $p_C(x + y) \le p_C(x) + p_C(y)$ (sous-additivité, découlant de la convexité de $C$).
- $C = \{ x \in E \mid p_C(x) < 1 \}$.
Comme $x_0 \notin C$, nous déduisons immédiatement que $p_C(x_0) \ge 1$.

**Étape 3 : Application de la forme analytique de Hahn-Banach.**
Considérons le sous-espace vectoriel de dimension 1 engendré par $x_0$ : $G = \mathbb{R}x_0$.
Définissons sur $G$ une forme linéaire $g : G \to \mathbb{R}$ par $g(t x_0) = t$.
Vérifions que $g$ est majorée par $p_C$ sur $G$. Pour tout $x = t x_0 \in G$ :
- Si $t \le 0$, $g(tx_0) = t \le 0 \le p_C(tx_0)$ (car $p_C$ est positive).
- Si $t > 0$, $g(tx_0) = t$. Or $p_C(tx_0) = t p_C(x_0)$. Puisque $p_C(x_0) \ge 1$, on a $p_C(tx_0) \ge t$. Donc $g(tx_0) \le p_C(tx_0)$.
Ainsi, sur $G$, $g(x) \le p_C(x)$.
D'après la **forme analytique de Hahn-Banach**, puisque $p_C$ est sous-linéaire, il existe une extension $f : E \to \mathbb{R}$, linéaire, telle que :
- $f$ coïncide avec $g$ sur $G$ (donc $f(x_0) = g(x_0) = 1$).
- $\forall x \in E, \ f(x) \le p_C(x)$.

**Étape 4 : Continuité de $f$ et conclusion.**
Puisque $B(0, r) \subset C$, pour tout $x$ tel que $||x|| < r$, $x \in C$, d'où $p_C(x) < 1$.
Ainsi, $\forall x \in B(0, r), \ f(x) \le p_C(x) < 1$.
Puisque $f$ est linéaire, $-x \in B(0, r)$ donne $f(-x) < 1 \implies f(x) > -1$.
D'où $\forall x \in B(0, r), \ |f(x)| < 1$. Ceci garantit que $f$ est bornée sur un voisinage de l'origine, et est donc continue.

Maintenant, exploitons $f(x) \le p_C(x)$ pour séparer $A$ et $B$.
Pour tout $a \in A, b \in B$, le vecteur $a - b + x_0 \in C$.
Comme $C = \{ x \in E \mid p_C(x) < 1 \}$, nous avons :
$f(a - b + x_0) \le p_C(a - b + x_0) < 1$
Par linéarité de $f$ et puisque $f(x_0) = 1$ :
$f(a) - f(b) + f(x_0) < 1$
$f(a) - f(b) + 1 < 1 \implies f(a) - f(b) < 0 \implies f(a) < f(b)$
Cette inégalité stricte $f(a) < f(b)$ est vraie pour tout $a \in A, b \in B$.
Ainsi, le plus petit majorant sur $A$ et le plus grand minorant sur $B$ satisfont :
$$ \sup_{a \in A} f(a) \le \inf_{b \in B} f(b) $$
Posons $\alpha = \inf_{b \in B} f(b)$.
Puisque l'image d'un convexe ouvert ($A$) par une fonction linéaire continue ($f$) est un convexe ouvert de $\mathbb{R}$ (donc un intervalle ouvert sans sa borne supérieure atteinte), on a même $f(a) < \alpha$ pour tout $a \in A$.
Ainsi : $\forall a \in A, \ f(a) < \alpha \le f(b), \forall b \in B$. L'hyperplan affine $H = f^{-1}(\{\alpha\})$ sépare $A$ et $B$ au sens large. La preuve est rigoureusement complète. $\blacksquare$

## 5. Applications en Optimisation et en Intelligence Artificielle

### A. Séparabilité linéaire et les Machines à Vecteurs de Support (SVM)

En apprentissage supervisé de classification binaire, on dispose d'un jeu de données d'entraînement : des points $x_i \in \mathbb{R}^d$ associés à des étiquettes $y_i \in \{-1, +1\}$.
Si l'enveloppe convexe des points de la classe $+1$ et l'enveloppe convexe de la classe $-1$ sont deux ensembles disjoints fermés (et comme ils sont constitués d'un nombre fini de points, ils sont compacts), alors la deuxième forme géométrique de Hahn-Banach garantit qu'il existe un hyperplan affine qui les sépare strictement.
La marge $\epsilon$ dans le théorème de Hahn-Banach correspond à la notion fondamentale de "marge" dans l'algorithme SVM. Le but du SVM à marge dure est de maximiser cet $\epsilon$, c'est-à-dire de trouver l'hyperplan optimal (parmi la multitude d'hyperplans séparateurs garantis par le théorème) qui maximise la distance aux plus proches points des deux ensembles.

### B. Algorithmes Primal-Dual et l'existence des multiplicateurs de Lagrange

Le théorème de Hahn-Banach géométrique est la pierre angulaire des théorèmes d'optimisation convexe. Lorsque l'on cherche à minimiser une fonction convexe $f_0(x)$ sous des contraintes d'inégalités convexes $f_i(x) \le 0$, l'ensemble admissible est convexe.
Si l'on considère l'ensemble des perturbations du problème dans l'espace des contraintes, l'existence d'hyperplans supports (version limite de la séparation) aux points de la frontière garantit l'existence des multiplicateurs de Lagrange optimaux (ou variables duales). Cela prouve que, sous des conditions de qualification (comme la condition de Slater), le saut de dualité (duality gap) est nul. Sans la géométrie de Hahn-Banach, la théorie de l'optimisation convexe, indispensable à l'entraînement des réseaux de neurones, n'existerait pas.
