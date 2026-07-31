
# Jalon 11 : Formes linéaires, hyperplans, espace dual et orthogonalité en dimension finie

## 1. Présentation du concept clé

La genèse des formes linéaires trouve ses racines dans le besoin inhérent à l'être humain de mesurer, quantifier et extraire une information scalaire (unidimensionnelle) à partir d'objets multidimensionnels complexes. Imaginez une vaste plaine topographique, où chaque position est déterminée par une multitude de coordonnées complexes. Un explorateur cherchant à quantifier l'altitude de son terrain de progression effectue sans le savoir une projection de ce monde multidimensionnel vers l'axe des réels : il applique une forme linéaire.

Historiquement, cette idée d'associer un unique scalaire à un vecteur s'est cristallisée lorsque les mathématiciens ont cherché à comprendre la structure intime des espaces eux-mêmes, non pas à travers les vecteurs qui les composent, mais à travers le prisme de toutes les "mesures" possibles sur ces vecteurs. C'est l'essence de la dualité, une notion formellement structurée au début du XXe siècle par des figures comme Stefan Banach et David Hilbert. Si l'on considère un espace vectoriel $E$ comme un univers de points, l'espace dual $E^*$ représente l'univers de tous les instruments de mesure, ou observateurs, capables de scruter $E$. Un hyperplan, concept fondamental de séparation, émerge naturellement : il s'agit de l'horizon, la frontière parfaitement plate (de dimension $n-1$) où une mesure spécifique s'annule, séparant l'espace en deux demi-espaces stricts.

## 2. Formalisation

L'intuition de la mesure laisse place à une rigueur algébrique implacable. Nous posons ici les fondations algébriques de la dualité en dimension finie.

### A. Anatomie et Typage Chirurgical

Soit $E$ un espace vectoriel sur un corps commutatif $\mathbb{K}$ (typiquement $\mathbb{R}$ ou $\mathbb{C}$), de dimension finie $\dim(E) = n \in \mathbb{N}^*$.

1. **Forme linéaire :**
   Une forme linéaire est une application $\phi : E \to \mathbb{K}$ satisfaisant la propriété de linéarité stricte :
   $$ \forall (x, y) \in E^2, \forall (\lambda, \mu) \in \mathbb{K}^2, \quad \phi(\lambda x + \mu y) = \lambda \phi(x) + \mu \phi(y) $$
   Le typage est fondamental : la source est l'espace vectoriel $E$, et le but est le corps de base $\mathbb{K}$ (considéré lui-même comme un $\mathbb{K}$-espace vectoriel de dimension 1).

2. **Espace Dual ($E^*$) :**
   L'ensemble de toutes les formes linéaires sur $E$, noté $E^* = \mathcal{L}(E, \mathbb{K})$, est l'espace dual de $E$. Il hérite d'une structure naturelle de $\mathbb{K}$-espace vectoriel.

3. **Hyperplan :**
   Un sous-espace vectoriel $H \subset E$ est appelé un hyperplan si et seulement s'il existe une forme linéaire **non nulle** $\phi \in E^* \setminus \{0_{E^*}\}$ telle que :
   $$ H = \ker(\phi) = \{ x \in E \mid \phi(x) = 0_{\mathbb{K}} \} $$
   L'exigence $\phi \neq 0_{E^*}$ est impérative pour exclure le cas trivial où $H = E$.

4. **Base Duale :**
   Si l'on fixe une base $\mathcal{B} = (e_1, e_2, \dots, e_n)$ de l'espace vectoriel $E$, on définit l'unique base duale $\mathcal{B}^* = (e_1^*, e_2^*, \dots, e_n^*)$ de $E^*$ par la relation de dualité de Kronecker :
   $$ \forall (i, j) \in \llbracket 1, n \rrbracket^2, \quad e_i^*(e_j) = \delta_{i,j} = \begin{cases} 1_{\mathbb{K}} & \text{si } i = j \\ 0_{\mathbb{K}} & \text{si } i \neq j \end{cases} $$

5. **Orthogonalité Duale :**
   Soit $A$ une partie non vide de $E$. Son orthogonal dans l'espace dual $E^*$ est le sous-espace :
   $$ A^\perp = \{ \phi \in E^* \mid \forall x \in A, \phi(x) = 0_{\mathbb{K}} \} $$
   Réciproquement, si $B \subset E^*$, son orthogonal prédual dans $E$ est $B^\circ = \{ x \in E \mid \forall \phi \in B, \phi(x) = 0_{\mathbb{K}} \}$.

### B. Théorèmes Fondamentaux

**Théorème 1 (Dimension de l'espace dual) :**
Si $E$ est de dimension finie, alors $E$ et son dual $E^*$ ont la même dimension :
$$ \dim(E) < +\infty \implies \dim(E^*) = \dim(E) $$

**Théorème 2 (Isomorphisme Canonique au Bidual) :**
Le bidual est défini comme $E^{**} = (E^*)^*$. L'application d'évaluation $J : E \to E^{**}$ définie par $\forall x \in E, J(x)(\phi) = \phi(x)$ (souvent noté $\langle \phi, x \rangle$) est un isomorphisme canonique. Cet isomorphisme est naturel car il ne dépend d'aucun choix de base, contrairement aux isomorphismes entre $E$ et $E^*$.

## 3. Démonstrations

Nous détaillons ici intégralement la preuve de l'isomorphisme canonique entre l'espace $E$ et son bidual $E^{**}$, pierre angulaire de l'algèbre linéaire en dimension finie.

**Théorème :** Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension finie $n$. L'application $J : E \to E^{**}$ définie par $\forall x \in E, \forall \phi \in E^*, J(x)(\phi) = \phi(x)$ est un isomorphisme de $\mathbb{K}$-espaces vectoriels.

**Preuve pas-à-pas :**

1. **Typage et bonne définition de $J$ :**
   Fixons $x \in E$. L'application $J(x)$ prend en argument une forme linéaire $\phi \in E^*$ et renvoie un scalaire $\phi(x) \in \mathbb{K}$.
   Vérifions que $J(x)$ est linéaire (c'est-à-dire $J(x) \in E^{**}$). Soient $\phi, \psi \in E^*$ et $\lambda \in \mathbb{K}$ :
   $$ J(x)(\lambda \phi + \psi) = (\lambda \phi + \psi)(x) $$
   Par définition des opérations sur $\mathcal{L}(E, \mathbb{K})$ :
   $$ (\lambda \phi + \psi)(x) = \lambda \phi(x) + \psi(x) = \lambda J(x)(\phi) + J(x)(\psi) $$
   Donc $J(x)$ est bien une forme linéaire sur $E^*$. L'application globale $J$ est donc bien typée : $J : E \to E^{**}$.

2. **Linéarité de $J$ :**
   Montrons que $J$ est une application linéaire. Soient $x, y \in E$ et $\alpha \in \mathbb{K}$.
   Il faut montrer l'égalité fonctionnelle dans $E^{**}$ : $J(\alpha x + y) = \alpha J(x) + J(y)$.
   Pour toute forme $\phi \in E^*$, évaluons les deux membres :
   $$ J(\alpha x + y)(\phi) = \phi(\alpha x + y) $$
   Par linéarité de $\phi$ (car $\phi \in E^*$) :
   $$ \phi(\alpha x + y) = \alpha \phi(x) + \phi(y) $$
   D'autre part, la définition des opérations dans $E^{**}$ donne :
   $$ (\alpha J(x) + J(y))(\phi) = \alpha J(x)(\phi) + J(y)(\phi) = \alpha \phi(x) + \phi(y) $$
   L'égalité sur chaque $\phi \in E^*$ prouve que $J(\alpha x + y) = \alpha J(x) + J(y)$. L'application $J$ est donc linéaire.

3. **Injectivité de $J$ :**
   Étudions le noyau $\ker(J)$.
   Soit $x \in \ker(J)$. Cela signifie que $J(x) = 0_{E^{**}}$, c'est-à-dire que pour toute $\phi \in E^*, J(x)(\phi) = 0_{\mathbb{K}}$.
   Donc, $\forall \phi \in E^*, \phi(x) = 0_{\mathbb{K}}$.
   Supposons par l'absurde que $x \neq 0_E$.
   Puisque $x$ est un vecteur non nul d'un espace de dimension finie, le théorème de la base incomplète autorise à étendre le vecteur unique $(x)$ en une base de $E$ : $\mathcal{B} = (x, e_2, \dots, e_n)$.
   Considérons alors la première forme linéaire coordonnée $e_1^*$ de la base duale $\mathcal{B}^*$. Par construction, $e_1^*(x) = 1_{\mathbb{K}}$.
   Or, nous avions déduit que pour toute forme $\phi$, $\phi(x) = 0_{\mathbb{K}}$. En appliquant cela à $\phi = e_1^*$, on obtient $1_{\mathbb{K}} = 0_{\mathbb{K}}$, ce qui est une contradiction manifeste dans un corps.
   L'hypothèse $x \neq 0_E$ est donc fausse. On en déduit que $x = 0_E$, d'où $\ker(J) = \{0_E\}$. $J$ est injective.

4. **Bijectivité par argument dimensionnel :**
   Nous savons que si $\dim(E) = n$, alors $\dim(E^*) = n$.
   En appliquant ce même théorème à l'espace vectoriel $E^*$ (qui est aussi de dimension finie $n$), on obtient $\dim(E^{**}) = \dim((E^*)^*) = \dim(E^*) = n$.
   Ainsi, $\dim(E) = \dim(E^{**}) = n$.
   Puisque $J : E \to E^{**}$ est une application linéaire injective entre deux espaces de même dimension finie, c'est obligatoirement un isomorphisme.
   La démonstration est achevée. $\blacksquare$

## 4. Exercices d'Application

*(Les exercices et corrections exhaustives sont répartis dans le répertoire `exos/`.)*

## 5. Application en Intelligence Artificielle

La dualité n'est pas qu'une abstraction algébrique ; c'est le langage géométrique fondamental de la classification supervisée en apprentissage automatique. Dans l'algorithme des Séparateurs à Vaste Marge (Support Vector Machines - SVM), la séparation de données linéairement séparables dans $\mathbb{R}^n$ se formule précisément comme la recherche d'un hyperplan optimal.

Un hyperplan de décision affine est défini par une équation de la forme $\phi(x) + b = 0$, où $x \in \mathbb{R}^n$ est le vecteur de caractéristiques, $\phi \in (\mathbb{R}^n)^*$ est une forme linéaire (qui, par le théorème de représentation de Riesz s'identifie au produit scalaire avec un vecteur normal $w$, $\phi(x) = \langle w, x \rangle$), et $b \in \mathbb{R}$ un biais.

La phase d'apprentissage d'un SVM consiste à trouver la forme linéaire $\phi$ qui maximise la marge, c'est-à-dire la distance entre l'hyperplan $\ker(\phi) - b$ et les points d'entraînement les plus proches (les vecteurs de support). Le théorème d'isomorphisme dual est exploité lors de la transformation du problème d'optimisation primal complexe (minimisation de $\|w\|^2$ sous contraintes) vers sa formulation duale de Lagrange. C'est dans cet espace dual que le fameux "Kernel Trick" (astuce du noyau) opère, permettant d'évaluer indirectement des formes linéaires dans des espaces de Hilbert de dimension infinie sans jamais calculer explicitement les coordonnées des vecteurs dans ces espaces.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon-7.md|Jalon 7 (Espaces vectoriels abstraits)]], [[Jalon-8.md|Jalon 8 (Applications linéaires)]]
- **Concepts Futurs dépendants :** [[Jalon 12 (Livrable IA).md|Jalon 12 (Livrable IA)]], [[Jalon-25.md|Jalon 25 (Formes bilinéaires)]], [[Jalon-123.md|Jalon 123 (Problèmes d'optimisation sous contraintes)]]


# Exercices d'Application

# Exercice 1: Espace dual en dimension 2
## Énoncé
Soit $E = \mathbb{R}^2$. On considère la base canonique $(e_1, e_2)$. Déterminer la base duale $(e_1^*, e_2^*)$ et calculer $e_1^*(3e_1 - 2e_2)$.

## Correction détaillée
1. **Définition de la base duale :** Par définition, la base duale $(e_1^*, e_2^*)$ d'une base $(e_1, e_2)$ vérifie $e_i^*(e_j) = \delta_{ij}$.
2. **Explicitation des formes linéaires :**
   - $e_1^*(x, y) = e_1^*(xe_1 + ye_2) = x e_1^*(e_1) + y e_1^*(e_2) = x \cdot 1 + y \cdot 0 = x$.
   - $e_2^*(x, y) = e_2^*(xe_1 + ye_2) = x e_2^*(e_1) + y e_2^*(e_2) = x \cdot 0 + y \cdot 1 = y$.
3. **Calcul de l'évaluation :** On cherche à évaluer $e_1^*$ sur le vecteur $v = 3e_1 - 2e_2$.
4. **Développement complet :**
   $$e_1^*(3e_1 - 2e_2) = 3 e_1^*(e_1) - 2 e_1^*(e_2)$$
   $$= 3 \times 1 - 2 \times 0$$
   $$= 3$$
5. **Conclusion :** La valeur de la forme linéaire $e_1^*$ sur le vecteur $3e_1 - 2e_2$ est $3$.

$\blacksquare$
# Exercice 2: Noyau d'une forme linéaire
## Énoncé
Soit $\phi : \mathbb{R}^3 \to \mathbb{R}$ définie par $\phi(x, y, z) = 2x - y + 3z$. Déterminer une base de $\ker \phi$.

## Correction détaillée
1. **Définition du noyau :** Le noyau de $\phi$ est l'ensemble des vecteurs sur lesquels la forme linéaire s'annule.
   $$\ker \phi = \{ (x,y,z) \in \mathbb{R}^3 \mid 2x - y + 3z = 0 \}$$
2. **Résolution de l'équation cartésienne :** L'équation $2x - y + 3z = 0$ équivaut à exprimer une variable en fonction des autres. Isolons $y$ :
   $$y = 2x + 3z$$
3. **Paramétrisation des vecteurs du noyau :** Un vecteur $v \in \ker \phi$ s'écrit donc :
   $$v = (x, 2x+3z, z)$$
4. **Décomposition en combinaison linéaire :** On sépare les paramètres libres $x$ et $z$ :
   $$v = (x, 2x, 0) + (0, 3z, z) = x(1, 2, 0) + z(0, 3, 1)$$
5. **Famille génératrice :** Les vecteurs $u_1 = (1, 2, 0)$ et $u_2 = (0, 3, 1)$ engendrent donc $\ker \phi$.
6. **Indépendance linéaire :** Supposons $\lambda u_1 + \mu u_2 = 0$.
   $$\lambda(1, 2, 0) + \mu(0, 3, 1) = (\lambda, 2\lambda+3\mu, \mu) = (0, 0, 0)$$
   On obtient immédiatement $\lambda = 0$ et $\mu = 0$. La famille $(u_1, u_2)$ est libre.
7. **Conclusion :** La famille $((1,2,0), (0,3,1))$ est une base de $\ker \phi$, qui est bien un hyperplan (dimension $3 - 1 = 2$).

$\blacksquare$
# Exercice 3: Orthogonal d'un sous-espace
## Énoncé
Soit $F$ un sous-espace vectoriel d'un $\mathbb{K}$-espace vectoriel $E$ de dimension finie $n$. Démontrer le théorème de la dimension de l'orthogonal : $\dim F + \dim F^\perp = n$.

## Correction détaillée
1. **Définition de l'application restriction :** On considère l'application linéaire $\rho : E^* \to F^*$ définie par $\rho(\phi) = \phi_{|F}$, c'est-à-dire que pour toute forme linéaire $\phi$ sur $E$, $\rho(\phi)$ est sa restriction au sous-espace $F$.
2. **Étude du noyau de $\rho$ :** Par définition,
   $$\ker \rho = \{ \phi \in E^* \mid \rho(\phi) = 0 \} = \{ \phi \in E^* \mid \forall x \in F, \phi(x) = 0 \}$$
   Or, l'ensemble des formes linéaires qui s'annulent sur $F$ est exactement la définition de l'orthogonal $F^\perp$. Donc $\ker \rho = F^\perp$.
3. **Étude de l'image de $\rho$ :** L'application $\rho$ est surjective. En effet, soit $\psi \in F^*$. On peut compléter une base $(e_1, \dots, e_p)$ de $F$ en une base $(e_1, \dots, e_p, e_{p+1}, \dots, e_n)$ de $E$. On définit alors une forme $\phi \in E^*$ par $\phi(e_i) = \psi(e_i)$ pour $1 \le i \le p$ et $\phi(e_i) = 0$ pour $i > p$. Ainsi $\phi_{|F} = \psi$.
   Donc $\text{Im}(\rho) = F^*$.
4. **Application du théorème du rang :** Le théorème du rang appliqué à $\rho : E^* \to F^*$ donne :
   $$\dim E^* = \dim \ker \rho + \dim \text{Im}(\rho)$$
5. **Substitutions des dimensions :**
   - $\dim E^* = \dim E = n$
   - $\dim \ker \rho = \dim F^\perp$
   - $\dim \text{Im}(\rho) = \dim F^* = \dim F$
   On obtient : $n = \dim F^\perp + \dim F$.
6. **Conclusion :** L'égalité $\dim F + \dim F^\perp = n$ est rigoureusement démontrée.

$\blacksquare$
# Exercice 4: Hyperplans et formes proportionnelles
## Énoncé
Montrer que deux formes linéaires non nulles $\phi$ et $\psi$ ont le même noyau si et seulement si elles sont proportionnelles.

## Correction détaillée
1. **Sens direct (proportionnalité implique même noyau) :**
   Supposons qu'il existe un scalaire $\lambda \neq 0$ tel que $\phi = \lambda \psi$.
   Soit $x \in \ker \phi$. Alors $\phi(x) = 0$, donc $\lambda \psi(x) = 0$. Comme $\lambda \neq 0$, on a $\psi(x) = 0$, donc $x \in \ker \psi$. Ainsi $\ker \phi \subset \ker \psi$.
   Symétriquement, $\psi = \frac{1}{\lambda} \phi$, ce qui donne $\ker \psi \subset \ker \phi$. Donc $\ker \phi = \ker \psi$.
2. **Sens réciproque (même noyau implique proportionnalité) :**
   Supposons que $\ker \phi = \ker \psi = H$. Comme $\phi \neq 0$, il existe un vecteur $e_0 \in E$ tel que $\phi(e_0) \neq 0$. Quitte à diviser par $\phi(e_0)$, on peut choisir $e_0$ tel que $\phi(e_0) = 1$.
3. **Décomposition d'un vecteur :** Soit $x \in E$ quelconque. Posons $x' = x - \phi(x)e_0$.
4. **Évaluation de $x'$ :** Évaluons $\phi$ en $x'$ :
   $$\phi(x') = \phi(x - \phi(x)e_0) = \phi(x) - \phi(x)\phi(e_0) = \phi(x) - \phi(x)(1) = 0$$
   Donc $x' \in \ker \phi$.
5. **Utilisation de l'égalité des noyaux :** Puisque $\ker \phi = \ker \psi$, on a nécessairement $x' \in \ker \psi$, ce qui implique $\psi(x') = 0$.
6. **Relation de proportionnalité :**
   $$\psi(x - \phi(x)e_0) = 0 \implies \psi(x) - \phi(x)\psi(e_0) = 0 \implies \psi(x) = \psi(e_0)\phi(x)$$
   Ceci étant vrai pour tout $x \in E$, en posant $\lambda = \psi(e_0)$, on obtient l'égalité des formes linéaires $\psi = \lambda \phi$.
7. **Conclusion :** Les deux formes linéaires sont proportionnelles.

$\blacksquare$
# Exercice 5: Équation d'un hyperplan en dimension n
## Énoncé
Soit $E$ un espace vectoriel de dimension $n$ et $(e_1, \dots, e_n)$ une base de $E$. Montrer qu'un hyperplan $H$ est caractérisé par une équation cartésienne de la forme $\sum_{i=1}^n a_i x_i = 0$ où les $(a_i)$ ne sont pas tous nuls.

## Correction détaillée
1. **Caractérisation par une forme linéaire :** Par définition, un hyperplan $H$ est le noyau d'une forme linéaire non nulle, notons-la $\phi : E \to \mathbb{K}$.
   $$H = \{ x \in E \mid \phi(x) = 0 \}$$
2. **Décomposition dans la base :** Soit un vecteur quelconque $x \in E$. Il admet une unique décomposition dans la base $(e_1, \dots, e_n)$ :
   $$x = \sum_{i=1}^n x_i e_i$$
   où les $x_i$ sont les coordonnées de $x$.
3. **Application de la linéarité :** Appliquons $\phi$ au vecteur $x$ :
   $$\phi(x) = \phi\left(\sum_{i=1}^n x_i e_i\right)$$
   Par linéarité de $\phi$, la somme et les scalaires sortent :
   $$\phi(x) = \sum_{i=1}^n x_i \phi(e_i)$$
4. **Identification des coefficients :** Posons pour tout $i \in \{1, \dots, n\}$, $a_i = \phi(e_i)$. L'équation d'appartenance à $H$ devient alors :
   $$\sum_{i=1}^n a_i x_i = 0$$
5. **Non-nullité des coefficients :** Comme $\phi$ est une forme linéaire non nulle, il existe au moins un vecteur de base $e_{i_0}$ tel que $\phi(e_{i_0}) \neq 0$. Donc, il existe au moins un $a_i$ tel que $a_i \neq 0$.
6. **Conclusion :** Tout hyperplan est rigoureusement caractérisé par une équation linéaire homogène dont les coefficients ne sont pas tous nuls.

$\blacksquare$
# Exercice 6: Bidual d'un espace vectoriel
## Énoncé
Pour tout $x \in E$, on définit l'application d'évaluation $\text{ev}_x : E^* \to \mathbb{K}$ par $\text{ev}_x(\phi) = \phi(x)$. Montrer que l'application $\Psi : x \mapsto \text{ev}_x$ est linéaire et injective.

## Correction détaillée
1. **Étape 1:** $\text{ev}_x$ est bien une forme linéaire sur $E^*$ car $\text{ev}_x(\phi_1 + \lambda \phi_2) = (\phi_1 + \lambda \phi_2)(x) = \phi_1(x) + \lambda \phi_2(x) = \text{ev}_x(\phi_1) + \lambda \text{ev}_x(\phi_2)$.
2. **Étape 2:** L'application $\Psi$ est linéaire. Soit $x, y \in E$ et $\lambda, \mu \in \mathbb{K}$. Évaluons $\Psi(\lambda x + \mu y)$ sur un élément quelconque $\phi \in E^*$ :
   $$\Psi(\lambda x + \mu y)(\phi) = \phi(\lambda x + \mu y) = \lambda \phi(x) + \mu \phi(y) = \lambda \Psi(x)(\phi) + \mu \Psi(y)(\phi)$$
   Ce qui démontre la linéarité.
3. **Étape 3:** Montrons que $\Psi$ est injective. Soit $x \in \ker \Psi$. Alors pour toute forme linéaire $\phi \in E^*$, on a $\phi(x) = 0$.
4. **Étape 4:** Si $x \neq 0$, on pourrait le compléter en une base $(x, e_2, \dots, e_n)$ et définir la forme coordonnée $\phi=x^*$ telle que $x^*(x)=1$, ce qui contredit $\phi(x)=0$.
5. **Conclusion:** Par conséquent $x=0$, d'où $\ker \Psi = \{0\}$. $\Psi$ est injective.

$\blacksquare$
# Exercice 7: Trace comme forme linéaire
## Énoncé
L'application $\text{Tr} : M_n(\mathbb{K}) \to \mathbb{K}$ est une forme linéaire. Montrer que tout hyperplan $H$ de $M_n(\mathbb{K})$ contient au moins une matrice inversible (pour $n \ge 2$).

## Correction détaillée
1. **Étape 1:** Un hyperplan de $M_n(\mathbb{K})$ est le noyau d'une forme linéaire non nulle $\phi$. Il est connu que toute forme linéaire sur $M_n(\mathbb{K})$ s'écrit $\phi(M) = \text{Tr}(AM)$ pour une unique matrice $A \in M_n(\mathbb{K})$. Ainsi, $H = \{ M \in M_n(\mathbb{K}) \mid \text{Tr}(AM) = 0 \}$.
2. **Étape 2:** On cherche $M \in H$ telle que $\det(M) \neq 0$. Si $A=0$, $\phi=0$ ce qui est exclu. Supposons par l'absurde que $H$ ne contient aucune matrice inversible.
3. **Étape 3:** L'hyperplan $H$ est un sous-espace vectoriel de dimension $n^2-1$. Si $H$ ne contient que des matrices singulières, on a une contradiction avec les résultats de la théorie des espaces de matrices de rang borné (théorème de Dieudonné), car la dimension maximale d'un sous-espace de matrices non-inversibles est $n(n-1)$, et pour $n \ge 2$, $n^2-1 > n(n-1)$.
4. **Conclusion:** L'hypothèse de départ est fausse, donc on en déduit formellement qu'un hyperplan contient toujours des éléments inversibles.

$\blacksquare$
# Exercice 8: Orthogonalité croisée
## Énoncé
Soient $F_1, F_2$ deux sous-espaces de $E$. Montrer que $(F_1 + F_2)^\perp = F_1^\perp \cap F_2^\perp$.

## Correction détaillée
1. **Étape 1 :** Soit $\phi \in (F_1 + F_2)^\perp$. Alors pour tout $x \in F_1 + F_2, \phi(x)=0$.
   En particulier, pour tout $x_1 \in F_1$, $\phi(x_1)=0$ (car $F_1 \subset F_1+F_2$), donc $\phi \in F_1^\perp$.
   De même $\phi \in F_2^\perp$. Ainsi $(F_1 + F_2)^\perp \subset F_1^\perp \cap F_2^\perp$.
2. **Étape 2 :** Réciproquement, soit $\phi \in F_1^\perp \cap F_2^\perp$. Pour tout $x \in F_1+F_2$, on peut écrire $x = x_1 + x_2$ avec $x_1 \in F_1, x_2 \in F_2$.
3. **Étape 3 :** On a par linéarité $\phi(x) = \phi(x_1+x_2) = \phi(x_1) + \phi(x_2)$.
4. **Étape 4 :** Puisque $\phi \in F_1^\perp$, $\phi(x_1)=0$. Puisque $\phi \in F_2^\perp$, $\phi(x_2)=0$. Donc $\phi(x) = 0 + 0 = 0$. Ainsi $\phi \in (F_1+F_2)^\perp$. On a l'inclusion réciproque.
5. **Conclusion:** Par double inclusion, l'égalité $(F_1 + F_2)^\perp = F_1^\perp \cap F_2^\perp$ est strictement démontrée.

$\blacksquare$
# Exercice 9: Indépendance linéaire de formes linéaires
## Énoncé
Soient $\phi_1, \dots, \phi_p \in E^*$. Montrer qu'elles sont linéairement indépendantes si et seulement si l'intersection de leurs noyaux $\bigcap_{i=1}^p \ker \phi_i$ est de dimension $n-p$.

## Correction détaillée
1. **Étape 1:** On définit l'application linéaire $\Phi : E \to \mathbb{K}^p$ par $\Phi(x) = (\phi_1(x), \dots, \phi_p(x))$.
2. **Étape 2:** Le noyau de $\Phi$ est exactement l'intersection des noyaux : $\ker \Phi = \bigcap_{i=1}^p \ker \phi_i$.
3. **Étape 3:** D'après le théorème du rang, $\dim E = \dim \ker \Phi + \dim \text{Im}(\Phi)$. Donc $\dim \bigcap \ker \phi_i = n - \dim \text{Im}(\Phi)$.
4. **Étape 4:** L'image de la transposée $\Phi^t : (\mathbb{K}^p)^* \to E^*$ est le sous-espace engendré par les $\phi_i$. Or $\text{rg}(\Phi) = \text{rg}(\Phi^t) = \dim \text{Vect}(\phi_1, \dots, \phi_p)$.
5. **Étape 5:** Ainsi, $\dim \text{Vect}(\phi_1, \dots, \phi_p) = p$ (c'est-à-dire que la famille est libre) si et seulement si $\text{rg}(\Phi) = p$, ce qui équivaut à $\dim \bigcap \ker \phi_i = n - p$.
6. **Conclusion:** L'équivalence est rigoureusement prouvée via l'application associée et le théorème du rang.

$\blacksquare$
# Exercice 10: Polynômes de Lagrange et dualité
## Énoncé
Dans $E = \mathbb{R}_{n-1}[X]$, on se donne $n$ scalaires distincts $a_1, \dots, a_n$. Montrer que les formes linéaires d'évaluation $\phi_i(P) = P(a_i)$ forment une base de $E^*$.

## Correction détaillée
1. **Étape 1:** La dimension de $E$ est $n$, donc $\dim E^* = n$. Pour démontrer qu'une famille de $n$ vecteurs forme une base, il suffit de montrer que la famille $(\phi_1, \dots, \phi_n)$ est libre.
2. **Étape 2:** Supposons une combinaison linéaire nulle: $\sum_{i=1}^n \lambda_i \phi_i = 0$. Cela signifie que pour tout polynôme $P \in E$, $\sum_{i=1}^n \lambda_i P(a_i) = 0$.
3. **Étape 3:** On introduit les polynômes interpolateurs de Lagrange $L_j(X) = \prod_{k \neq j} \frac{X-a_k}{a_j-a_k}$. Ce sont des éléments de $E$ car leur degré est exactement $n-1$.
4. **Étape 4:** Par construction, $L_j(a_i) = \delta_{ij}$ (vaut 1 si $i=j$, 0 sinon).
5. **Étape 5:** Évaluons la combinaison linéaire nulle sur le polynôme $L_j$ :
   $$0 = \sum_{i=1}^n \lambda_i \phi_i(L_j) = \sum_{i=1}^n \lambda_i L_j(a_i) = \lambda_j$$
6. **Conclusion:** Pour tout indice $j$, on obtient $\lambda_j = 0$. La famille est donc libre, et c'est par conséquent une base. Les polynômes $(L_j)$ forment précisément la base antéduale associée.

$\blacksquare$


# Travaux Pratiques et Simulations Algorithmiques

# TP 1: Implémentation pure Python d'une forme linéaire

## Objectif mathématique
Mise en pratique algorithmique de l'espace dual, de l'hyperplan et des notions fondamentales de l'algèbre linéaire, structurée en Python absolu sans bibliothèques de haut niveau.

## Code Python
```python
def apply_linear_form(form_coeffs, vector):
    if len(form_coeffs) != len(vector):
        raise ValueError("Dimensions mismatch")

    # Implémentation mathématique de la somme des produits (produit scalaire)
    resultat = 0
    for i in range(len(vector)):
        resultat += form_coeffs[i] * vector[i]
    return resultat

# Validation avec un calcul manuel: 2(1) - 1(2) + 3(0) = 0
assert apply_linear_form([2, -1, 3], [1, 2, 0]) == 0
assert apply_linear_form([1, 1], [3, 4]) == 7
```

## Validation Rigoureuse
Ce code vérifie le calcul algorithmique fondamental d'une forme linéaire $\phi(x) = \sum a_i x_i$ par une boucle itérative stricte, sans artifice de bibliothèque externe.
# TP 2: Recherche de l'équation d'un hyperplan affine

## Objectif mathématique
Mise en pratique algorithmique de l'espace dual, de l'hyperplan et des notions fondamentales de l'algèbre linéaire, structurée en Python absolu sans bibliothèques de haut niveau.

## Code Python
```python
def hyperplane_equation_from_normal(normal_vector, point_on_plane):
    # L'équation de l'hyperplan est sum(n_i * x_i) = d
    # Pour trouver d, on évalue la forme linéaire sur le point appartenant au plan.
    d = 0
    for i in range(len(normal_vector)):
        d += normal_vector[i] * point_on_plane[i]
    return normal_vector, d

normal, constante_d = hyperplane_equation_from_normal([1, -1, 2], [1, 1, 1])
# Calcul formel: 1(1) - 1(1) + 2(1) = 2
assert normal == [1, -1, 2]
assert constante_d == 2
```

## Validation Rigoureuse
Ce code calcule rigoureusement la constante affine $d$ de l'hyperplan en traduisant l'égalité $\phi(x_0) = d$ en Python pur.
# TP 3: Génération algorithmique d'une base de noyau (Dimension 3)

## Objectif mathématique
Mise en pratique algorithmique de l'espace dual, de l'hyperplan et des notions fondamentales de l'algèbre linéaire, structurée en Python absolu sans bibliothèques de haut niveau.

## Code Python
```python
def find_hyperplane_basis_3d(coeffs):
    a, b, c = coeffs
    # Recherche systématique d'une base libre
    if a != 0:
        # On exprime x en fonction de y et z: x = (-b/a)y + (-c/a)z
        return [(-b/a, 1, 0), (-c/a, 0, 1)]
    elif b != 0:
        return [(1, -a/b, 0), (0, -c/b, 1)]
    elif c != 0:
        return [(1, 0, -a/c), (0, 1, -b/c)]
    else:
        raise ValueError("La forme linéaire ne peut être identiquement nulle")

basis = find_hyperplane_basis_3d([2, -1, 3])
# Validation mathématique: la forme linéaire s'annule bien sur les vecteurs de base
assert sum(c*v for c, v in zip([2, -1, 3], basis[0])) == 0
assert sum(c*v for c, v in zip([2, -1, 3], basis[1])) == 0
```

## Validation Rigoureuse
La fonction construit explicitement une famille génératrice libre pour le noyau (sous-espace de dimension $n-1$), validée par assertion.
# TP 4: Intersection analytique de deux hyperplans dans R^2

## Objectif mathématique
Mise en pratique algorithmique de l'espace dual, de l'hyperplan et des notions fondamentales de l'algèbre linéaire, structurée en Python absolu sans bibliothèques de haut niveau.

## Code Python
```python
def intersect_2d_lines(a1, b1, d1, a2, b2, d2):
    # Calcul du déterminant du système
    det = a1b1
    if det == 0:
        return None # Les hyperplans (droites) sont parallèles ou confondus

    # Résolution exacte par la règle de Cramer
    x = (d1b1) / det
    y = (a1d1) / det
    return (x, y)

# Intersection de x - y = 0 et x + y = 2
assert intersect_2d_lines(1, -1, 0, 1, 1, 2) == (1.0, 1.0)
```

## Validation Rigoureuse
L'intersection de deux hyperplans dans $\mathbb{R}^2$ est résolue de manière algorithmique absolue par la formule de Cramer.
# TP 5: Dualité : Translation Vecteur-Forme (Théorème de Riesz discret)

## Objectif mathématique
Mise en pratique algorithmique de l'espace dual, de l'hyperplan et des notions fondamentales de l'algèbre linéaire, structurée en Python absolu sans bibliothèques de haut niveau.

## Code Python
```python
def riesz_representation(form_eval_func, dimension):
    # La forme linéaire est entièrement déterminée par ses valeurs sur la base canonique.
    # On reconstruit le vecteur représentant `u` tel que phi(x) = <u, x>

    representing_vector = []
    for i in range(dimension):
        # Création du i-ème vecteur de la base canonique e_i
        e_i = [0] * dimension
        e_i[i] = 1

        # Le coefficient a_i est l'évaluation de la forme sur e_i
        a_i = form_eval_func(e_i)
        representing_vector.append(a_i)

    return representing_vector

def custom_form(v):
    # Une forme linéaire quelconque agissant sur un vecteur 3D
    return 3v[1] + 5*v[2]

repr_vec = riesz_representation(custom_form, 3)
assert repr_vec == [3, -2, 5]
```

## Validation Rigoureuse
Démontre en Python pur la construction de l'isomorphisme de Riesz : extraction rigoureuse du vecteur représentatif en évaluant la forme sur la base canonique.
