---
uuid: "jalon-26"
title: "Espaces euclidiens, orthogonalité, théorème de la projection orthogonale et algorithme de Gram-Schmidt"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/projection-donnees
prev: "[[Jalon 25 (Formes bilinéaires).md]]"
next: "[[Jalon 27 (Endomorphismes symétriques).md]]"
---

# Jalon 26 : Espaces euclidiens, orthogonalité, théorème de la projection orthogonale et algorithme de Gram-Schmidt

## 1. Échafaudage Cognitif & Genèse du Concept

L'algèbre linéaire, dans ses fondements les plus abstraits (espaces vectoriels, bases, applications linéaires), nous offre un cadre algébrique robuste, mais singulièrement dénué de propriétés métriques. Dans un espace vectoriel abstrait $E$, les notions de « longueur », d'« angle », ou de « proximité » n'existent tout simplement pas. On peut additionner des vecteurs et les multiplier par des scalaires, mais on ne peut pas mesurer la distance qui les sépare ni vérifier s'ils sont perpendiculaires.

Pourtant, notre intuition du monde physique euclidien, formalisée dès l'Antiquité par Euclide, repose intrinsèquement sur ces grandeurs métriques. Le théorème de Pythagore, la plus célèbre des propriétés géométriques, exige une notion bien définie de l'angle droit. Le défi des mathématiciens du XIXe siècle, notamment Hermann Grassmann et Giuseppe Peano, fut de réintégrer cette géométrie riche au cœur de l'algèbre linéaire, sans en sacrifier la pureté axiomatique.

La solution ne fut pas d'ajouter des longueurs et des angles comme des concepts primitifs, mais plutôt de doter l'espace vectoriel abstrait d'une structure algébrique supplémentaire : le **produit scalaire**. C'est cette forme bilinéaire symétrique définie positive qui induit naturellement une norme (mesurant les longueurs) et permet de définir rigoureusement l'orthogonalité (mesurant les angles).

Un espace euclidien est ainsi la quintessence de la géométrie classique : un espace vectoriel réel de dimension finie, enrichi d'un produit scalaire. C'est dans ce cadre que la projection orthogonale trouve tout son sens, offrant une méthode optimale pour approximer un vecteur par des éléments d'un sous-espace donné. Cette idée d'approximation orthogonale est la clef de voûte de l'analyse de données moderne : de la régression des moindres carrés en apprentissage automatique aux décompositions spectaculaires comme l'ACP, toutes reposent sur le socle solide de la géométrie euclidienne.

## 2. Protocole d'Exégèse Conceptuelle : Définitions et Structures

### 2.1 Espace préhilbertien réel et Espace Euclidien

**A. Énoncé Symbolique Strict**

Soit $E$ un $\mathbb{R}$-espace vectoriel. Un **produit scalaire** sur $E$ est une application :
$$ \langle \cdot, \cdot \rangle : E \times E \to \mathbb{R} $$
qui est :
1. **Bilinéaire** : Pour tous $x, y, z \in E$ et tout $\lambda \in \mathbb{R}$,
   $$ \langle \lambda x + y, z \rangle = \lambda \langle x, z \rangle + \langle y, z \rangle \quad \text{et} \quad \langle x, \lambda y + z \rangle = \lambda \langle x, y \rangle + \langle x, z \rangle $$
2. **Symétrique** : Pour tous $x, y \in E$,
   $$ \langle x, y \rangle = \langle y, x \rangle $$
3. **Définie positive** : Pour tout $x \in E$,
   $$ \langle x, x \rangle \ge 0 $$
   $$ \langle x, x \rangle = 0 \iff x = 0_E $$

Un **espace préhilbertien réel** est un couple $(E, \langle \cdot, \cdot \rangle)$ où $E$ est un $\mathbb{R}$-espace vectoriel et $\langle \cdot, \cdot \rangle$ un produit scalaire sur $E$.
Un **espace euclidien** est un espace préhilbertien réel de **dimension finie**.

**B. Anatomie et Typage Chirurgical**
- $E$ est un espace vectoriel sur le corps des réels $\mathbb{K} = \mathbb{R}$. La théorie sur $\mathbb{C}$ nécessiterait une forme sesquilinéaire (hermitienne), aboutissant aux espaces préhilbertiens complexes.
- $\langle \cdot, \cdot \rangle$ est la forme bilinéaire. La notation à crochets est la plus répandue en analyse hilbertienne et en mécanique quantique (notation de Dirac).
- La condition de symétrie (2) rend la bilinéarité (1) redondante d'un côté. Si l'application est linéaire à gauche et symétrique, elle est automatiquement linéaire à droite.
- La positivité stipule que le scalaire $\langle x, x \rangle$ est toujours positif ou nul.
- Le caractère "défini" est crucial : le seul vecteur de "carré scalaire" nul est le vecteur nul. C'est ce qui assurera que la norme induite est une véritable norme et pas seulement une semi-norme.

**C. Exemples de Validation**
- **Exemple 1 (Le produit scalaire canonique sur $\mathbb{R}^n$)** :
  Pour $x = (x_1, \ldots, x_n)$ et $y = (y_1, \ldots, y_n)$ dans $\mathbb{R}^n$, l'application $\langle x, y \rangle = \sum_{i=1}^n x_i y_i$ est un produit scalaire. $(\mathbb{R}^n, \langle \cdot, \cdot \rangle)$ est l'archétype de l'espace euclidien.
- **Exemple 2 (Espace de polynômes, préhilbertien mais non euclidien)** :
  Sur $E = \mathbb{R}[X]$ (espace des polynômes à coefficients réels), l'application $\langle P, Q \rangle = \int_0^1 P(t)Q(t)dt$ est un produit scalaire. Cependant, $E$ étant de dimension infinie, cet espace est un espace préhilbertien réel, mais *non* euclidien.

**D. Cas Pathologiques et Contre-exemples**
- **Forme indéfinie** : L'espace de Minkowski en relativité restreinte, modélisé par $\mathbb{R}^4$ avec la forme $\langle x, y \rangle = -x_0 y_0 + x_1 y_1 + x_2 y_2 + x_3 y_3$. Cette forme est bilinéaire et symétrique, mais pas positive. Un vecteur non nul $x = (1, 0, 0, 0)$ donne $\langle x, x \rangle = -1 < 0$. Ce n'est donc pas un produit scalaire, et la géométrie induite n'est pas euclidienne (géométrie lorentzienne).

### 2.2 Norme induite et Inégalité de Cauchy-Schwarz

**A. Énoncé Symbolique Strict**

Soit $(E, \langle \cdot, \cdot \rangle)$ un espace préhilbertien réel. On définit l'application norme :
$$ \|\cdot\| : E \to \mathbb{R}_+ $$
$$ x \mapsto \sqrt{\langle x, x \rangle} $$

**Théorème (Inégalité de Cauchy-Schwarz)** :
Pour tous $x, y \in E$, on a :
$$ |\langle x, y \rangle| \le \|x\| \cdot \|y\| $$
L'égalité a lieu si et seulement si la famille $(x, y)$ est liée (les vecteurs sont colinéaires).

**B. Anatomie et Typage Chirurgical**
- La racine carrée est bien définie car, par l'axiome de positivité, $\langle x, x \rangle \ge 0$.
- $\|x\|$ représente la "longueur" euclidienne du vecteur $x$.
- L'inégalité de Cauchy-Schwarz borne le produit scalaire par le produit des normes. Elle est la source fondamentale de toute l'analyse hilbertienne.

**C. Exemples de Validation**
- Dans $\mathbb{R}^n$, l'inégalité se traduit par $|\sum x_i y_i| \le \sqrt{\sum x_i^2} \sqrt{\sum y_i^2}$.
- Dans $C([0,1], \mathbb{R})$, elle donne $|\int_0^1 f(t)g(t)dt| \le \sqrt{\int_0^1 f(t)^2 dt} \sqrt{\int_0^1 g(t)^2 dt}$.

### 2.3 Orthogonalité et Bases Orthonormées

**A. Énoncé Symbolique Strict**

Deux vecteurs $x, y \in E$ sont dits **orthogonaux** (noté $x \perp y$) si :
$$ \langle x, y \rangle = 0 $$

Un sous-espace $F$ et un vecteur $x$ sont orthogonaux ($x \perp F$) si $\forall y \in F, \langle x, y \rangle = 0$.
Deux sous-espaces $F, G \subset E$ sont orthogonaux si $\forall x \in F, \forall y \in G, \langle x, y \rangle = 0$.

L'**orthogonal** d'un sous-espace $F$, noté $F^\perp$, est défini par :
$$ F^\perp = \{x \in E \mid \forall y \in F, \langle x, y \rangle = 0\} $$

Une famille $(e_1, \ldots, e_p)$ de $E$ est dite **orthogonale** si $\forall i \neq j, \langle e_i, e_j \rangle = 0$.
Elle est **orthonormée** si elle est orthogonale et si de plus, pour tout $i$, $\|e_i\| = 1$ (équivalent à $\langle e_i, e_j \rangle = \delta_{ij}$, où $\delta$ est le symbole de Kronecker).

**B. Anatomie et Typage Chirurgical**
- L'orthogonalité est la généralisation rigoureuse de la notion d'angle droit. Par l'inégalité de Cauchy-Schwarz, on peut définir l'angle $\theta$ entre deux vecteurs non nuls par $\cos(\theta) = \frac{\langle x, y \rangle}{\|x\| \|y\|}$. L'orthogonalité correspond au cas $\cos(\theta) = 0$, soit $\theta = \frac{\pi}{2} \pmod \pi$.
- $F^\perp$ est un sous-espace vectoriel de $E$, même si $F$ n'est qu'un simple sous-ensemble non structuré.
- Une base orthonormée (BON) est le repère optimal : la géométrie y est isométrique à celle de l'espace canonique $\mathbb{R}^n$.

## 3. Démonstrations Complètes à Blanc (Zéro Ellipse)

### 3.1 Preuve du Théorème de Pythagore

**Théorème** :
Soient $x, y \in E$. Si $x$ et $y$ sont orthogonaux, alors :
$$ \|x + y\|^2 = \|x\|^2 + \|y\|^2 $$

**Preuve, étape par étape :**
1. Soient $x, y \in E$ tels que $\langle x, y \rangle = 0$.
2. Développons $\|x + y\|^2$ en utilisant la définition de la norme induite :
   $$ \|x + y\|^2 = \langle x + y, x + y \rangle $$
3. Par bilinéarité du produit scalaire, nous distribuons les termes :
   $$ \langle x + y, x + y \rangle = \langle x, x \rangle + \langle x, y \rangle + \langle y, x \rangle + \langle y, y \rangle $$
4. Par symétrie du produit scalaire, $\langle y, x \rangle = \langle x, y \rangle$. Ainsi :
   $$ \|x + y\|^2 = \|x\|^2 + 2\langle x, y \rangle + \|y\|^2 $$
5. Puisque $x$ et $y$ sont orthogonaux par hypothèse, le terme $\langle x, y \rangle$ est nul.
6. Il reste donc l'expression recherchée :
   $$ \|x + y\|^2 = \|x\|^2 + \|y\|^2 $$
   $\blacksquare$

### 3.2 Preuve de l'inégalité de Cauchy-Schwarz

**Preuve, étape par étape :**
1. Soient $x, y \in E$. Si $y = 0_E$, l'inégalité devient $|0| \le \|x\| \cdot 0$, ce qui est vrai et l'égalité est vérifiée. La famille $(x, 0_E)$ est liée. Supposons désormais $y \neq 0_E$.
2. Considérons le polynôme réel du second degré en $\lambda \in \mathbb{R}$ défini par l'expression algébrique de la norme carrée d'une combinaison linéaire :
   $$ P(\lambda) = \|x + \lambda y\|^2 $$
3. Par l'axiome de positivité du produit scalaire, $P(\lambda) \ge 0$ pour tout réel $\lambda$.
4. Développons l'expression de $P(\lambda)$ en utilisant la bilinéarité et la symétrie :
   $$ P(\lambda) = \langle x + \lambda y, x + \lambda y \rangle $$
   $$ P(\lambda) = \langle x, x \rangle + \lambda \langle x, y \rangle + \lambda \langle y, x \rangle + \lambda^2 \langle y, y \rangle $$
   $$ P(\lambda) = \|y\|^2 \lambda^2 + 2\langle x, y \rangle \lambda + \|x\|^2 $$
5. $P(\lambda)$ est un trinôme du second degré en $\lambda$ de la forme $a\lambda^2 + b\lambda + c$ avec $a = \|y\|^2 > 0$ (car $y \neq 0_E$), $b = 2\langle x, y \rangle$ et $c = \|x\|^2$.
6. Puisque ce trinôme est toujours positif ou nul sur $\mathbb{R}$, il ne peut pas posséder deux racines réelles distinctes. Par conséquent, son discriminant réduit (ou son discriminant classique) est négatif ou nul :
   $$ \Delta = b^2 - 4ac \le 0 $$
   $$ (2\langle x, y \rangle)^2 - 4\|y\|^2 \|x\|^2 \le 0 $$
   $$ 4\langle x, y \rangle^2 \le 4\|y\|^2 \|x\|^2 $$
7. En divisant par 4 et en prenant la racine carrée (la fonction racine carrée étant croissante sur $\mathbb{R}_+$), on obtient :
   $$ |\langle x, y \rangle| \le \|x\| \cdot \|y\| $$
   Ceci établit l'inégalité.
8. Étudions le cas d'égalité. L'égalité a lieu si et seulement si $\Delta = 0$.
9. Si $\Delta = 0$, le trinôme possède une racine réelle double $\lambda_0$.
   $$ P(\lambda_0) = 0 \iff \|x + \lambda_0 y\|^2 = 0 $$
10. Par le caractère "défini" de la norme, ceci implique $x + \lambda_0 y = 0_E$, ce qui équivaut à $x = -\lambda_0 y$. Les vecteurs $x$ et $y$ sont donc colinéaires (liés). Réciproquement, s'ils sont liés, on vérifie trivialement que l'égalité est satisfaite.
    $\blacksquare$

### 3.3 L'algorithme d'orthonormalisation de Gram-Schmidt

L'algorithme de Gram-Schmidt prouve de manière constructive que tout sous-espace euclidien admet une base orthonormée.

**Théorème** :
Soit $(e_1, \ldots, e_p)$ une famille libre de $E$. Il existe une unique famille orthonormée $(u_1, \ldots, u_p)$ telle que :
1. Pour tout $k \in \{1, \ldots, p\}$, $\text{Vect}(u_1, \ldots, u_k) = \text{Vect}(e_1, \ldots, e_k)$.
2. Pour tout $k \in \{1, \ldots, p\}$, $\langle e_k, u_k \rangle > 0$.

**Construction explicite étape par étape :**
1. **Initialisation (k=1)** : On pose $v_1 = e_1$. Puisque la famille initiale est libre, $e_1 \neq 0_E$. On normalise pour obtenir $u_1$ :
   $$ u_1 = \frac{v_1}{\|v_1\|} = \frac{e_1}{\|e_1\|} $$
   Il est évident que $\text{Vect}(u_1) = \text{Vect}(e_1)$ et $\langle e_1, u_1 \rangle = \frac{\|e_1\|^2}{\|e_1\|} = \|e_1\| > 0$.

2. **Étape k** : Supposons construite la famille orthonormée $(u_1, \ldots, u_{k-1})$ vérifiant les conditions jusqu'au rang $k-1$. On cherche $v_k$ en soustrayant de $e_k$ sa projection orthogonale sur le sous-espace $F_{k-1} = \text{Vect}(u_1, \ldots, u_{k-1})$ :
   $$ v_k = e_k - \sum_{i=1}^{k-1} \langle e_k, u_i \rangle u_i $$
3. **Vérification de l'orthogonalité** : Pour tout $j \in \{1, \ldots, k-1\}$, calculons $\langle v_k, u_j \rangle$ :
   $$ \langle v_k, u_j \rangle = \langle e_k - \sum_{i=1}^{k-1} \langle e_k, u_i \rangle u_i, u_j \rangle $$
   Par bilinéarité :
   $$ \langle v_k, u_j \rangle = \langle e_k, u_j \rangle - \sum_{i=1}^{k-1} \langle e_k, u_i \rangle \langle u_i, u_j \rangle $$
   Puisque la famille $(u_i)$ est orthonormée, $\langle u_i, u_j \rangle = \delta_{ij}$. La somme se réduit au seul terme pour $i=j$ :
   $$ \langle v_k, u_j \rangle = \langle e_k, u_j \rangle - \langle e_k, u_j \rangle \cdot 1 = 0 $$
   Donc $v_k$ est orthogonal à tous les $(u_1, \ldots, u_{k-1})$.

4. **Vérification de non-nullité** : Si $v_k = 0_E$, alors $e_k = \sum_{i=1}^{k-1} \langle e_k, u_i \rangle u_i$. Or $u_i \in \text{Vect}(e_1, \ldots, e_{i}) \subset \text{Vect}(e_1, \ldots, e_{k-1})$. Cela impliquerait $e_k \in \text{Vect}(e_1, \ldots, e_{k-1})$, ce qui contredit l'hypothèse de liberté de la famille $(e_1, \ldots, e_p)$. Donc $v_k \neq 0_E$.

5. **Normalisation** : On pose :
   $$ u_k = \frac{v_k}{\|v_k\|} $$
   Par construction, $(u_1, \ldots, u_k)$ est orthonormée, génère le même sous-espace que $(e_1, \ldots, e_k)$, et la positivité du produit scalaire final est garantie. Le processus se termine à $k=p$.
   $\blacksquare$

### 3.4 Le Théorème de la Projection Orthogonale

C'est le théorème central pour l'approximation.

**Théorème** :
Soit $E$ un espace préhilbertien et $F$ un sous-espace de dimension finie de $E$. Pour tout $x \in E$, il existe un unique vecteur de $F$, noté $p_F(x)$, tel que $x - p_F(x) \in F^\perp$.
De plus, $p_F(x)$ réalise la distance minimale entre $x$ et $F$ :
$$ \|x - p_F(x)\| = \min_{y \in F} \|x - y\| = d(x, F) $$

**Preuve, étape par étape :**
1. **Existence** : Puisque $F$ est de dimension finie, il admet une base orthonormée $(u_1, \ldots, u_r)$ (obtenue par Gram-Schmidt).
2. Posons $p = \sum_{i=1}^r \langle x, u_i \rangle u_i$. Par définition, $p$ est une combinaison linéaire des $u_i$, donc $p \in F$.
3. Vérifions que $x - p \in F^\perp$. Soit $j \in \{1, \ldots, r\}$.
   $$ \langle x - p, u_j \rangle = \langle x, u_j \rangle - \langle \sum_{i=1}^r \langle x, u_i \rangle u_i, u_j \rangle $$
   $$ \langle x - p, u_j \rangle = \langle x, u_j \rangle - \sum_{i=1}^r \langle x, u_i \rangle \langle u_i, u_j \rangle $$
   $$ \langle x - p, u_j \rangle = \langle x, u_j \rangle - \langle x, u_j \rangle \cdot 1 = 0 $$
   Le vecteur $x-p$ est orthogonal à tous les vecteurs de la base de $F$, il est donc orthogonal à $F$. L'existence de la projection est prouvée.
4. **Unicité** : Supposons l'existence d'un autre vecteur $q \in F$ tel que $x - q \in F^\perp$.
   Puisque $F^\perp$ est un sous-espace vectoriel, la différence $(x-q) - (x-p) = p - q$ appartient à $F^\perp$.
   Cependant, puisque $p, q \in F$ et que $F$ est un sous-espace vectoriel, $p - q \in F$.
   Le vecteur $p-q$ appartient à $F \cap F^\perp$. Or $\forall v \in F \cap F^\perp, \langle v, v \rangle = 0 \implies v = 0_E$.
   Donc $p-q = 0_E$, ce qui implique $p=q$.
5. **Propriété de minimisation de la distance** : Soit $y \in F$ un vecteur quelconque. Écrivons la différence $x-y$ :
   $$ x - y = (x - p_F(x)) + (p_F(x) - y) $$
6. Notons que le premier terme $(x - p_F(x)) \in F^\perp$.
7. Le second terme $(p_F(x) - y)$ est la différence de deux éléments de $F$, donc il appartient à $F$.
8. Les deux termes sont orthogonaux. Nous pouvons appliquer le théorème de Pythagore :
   $$ \|x - y\|^2 = \|x - p_F(x)\|^2 + \|p_F(x) - y\|^2 $$
9. Par la positivité de la norme, $\|p_F(x) - y\|^2 \ge 0$. Par conséquent :
   $$ \|x - y\|^2 \ge \|x - p_F(x)\|^2 $$
   $$ \|x - y\| \ge \|x - p_F(x)\| $$
10. L'égalité n'est atteinte que si $\|p_F(x) - y\|^2 = 0$, ce qui implique $y = p_F(x)$. Ainsi, $p_F(x)$ est l'unique élément minimisant la distance.
    $\blacksquare$
