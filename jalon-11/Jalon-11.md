---
uuid: "jalon-11"
title: "Formes linéaires, hyperplans, espace dual et orthogonalité en dimension finie"
year: 1
trimester: 1
tags:
  - math/algebre-lineaire
  - ia/dualite
prev: "[[Jalon 10 (Changements de base).md]]"
next: "[[Jalon 12 (Livrable IA).md]]"
---
# Jalon 11 : Formes linéaires, hyperplans, espace dual et orthogonalité en dimension finie

## 1. Présentation du concept clé
L'essence du concept peut être approchée par l'analogie suivante :
  - **Forme linéaire :** Imaginez que vous soyez un inspecteur de qualité. Un vecteur est un objet complexe (un produit avec poids, taille, prix). Une **forme linéaire**, c'est votre test : vous donnez une note unique (un nombre) à cet objet. Si vous testez deux produits ensemble, la note est la somme des notes. C'est un instrument de mesure simple et puissant.
  - **Hyperplan :** C'est la frontière parfaite. En 2D, c'est une ligne qui sépare le plan en deux. En 3D, c'est une feuille de papier infinie qui sépare l'espace. Un hyperplan, c'est l'ensemble de tous les vecteurs qui reçoivent la note "zéro" par votre test.
  - **Dualité :** C'est le monde des instruments de mesure. Si les vecteurs sont les "points", les formes linéaires sont les "regards" portés sur ces points.
Nécessité historique et mathématique : Parfois, il est plus facile de décrire un objet par la manière dont il réagit à des tests (le dual) plutôt que par sa structure interne. C'est fondamental pour définir la notion de "perpendiculaire" ou pour séparer des données.
Représentation géométrique : Imaginez une montagne. La hauteur en chaque point est une fonction (peut-être linéaire localement). L'hyperplan, c'est le "niveau de la mer" (altitude 0). L'espace dual, c'est l'ensemble de tous les plans inclinés possibles qui pourraient toucher la montagne.

## 2. Formalisation
### A. Définitions Formelles
Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension $n$.
1. **Forme linéaire :** Une application $\phi : E \to \mathbb{K}$ est une forme linéaire si elle est un morphisme de $\mathbb{K}$-espaces vectoriels. Le typage chirurgical est le suivant : l'espace de départ $E$ est le domaine des objets vectoriels abstraits, tandis que l'espace d'arrivée $\mathbb{K}$ (un corps commutatif, usuellement $\mathbb{R}$ ou $\mathbb{C}$) représente la quantification scalaire. Formellement :
   $$\forall (x, y) \in E \times E, \forall (\lambda, \mu) \in \mathbb{K} \times \mathbb{K}, \quad \phi(\lambda x + \mu y) = \lambda \phi(x) + \mu \phi(y)$$
2. **Espace Dual ($E^*$) :** L'espace vectoriel $\mathcal{L}(E, \mathbb{K})$ de toutes les formes linéaires sur $E$.
3. **Hyperplan :** Un sous-espace vectoriel $H$ de $E$ est un hyperplan s'il existe une forme linéaire non nulle $\phi \in E^*$ telle que $H = \ker \phi$.
4. **Base Duale :** Soit $\mathcal{B} = (e_1, ..., e_n)$ une base de $E$. La base duale $\mathcal{B}^* = (e^*_1, ..., e^*_n)$ est définie par :
   $$e^*_i(e_j) = \delta_{i,j} \quad (\text{symbole de Kronecker})$$
5. **Orthogonalité (au sens de la dualité) :** Soit $A \subseteq E$. On définit l'orthogonal de $A$ dans $E^*$ par $A^\perp = \{ \phi \in E^* \mid \forall x \in A, \phi(x) = 0 \}$.

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


### C. Exemples et Cas Pathologiques
- **Exemple Trivial :** La forme linéaire nulle $\phi(x) = 0$ pour tout $x$. Son noyau est $E$ entier. L'image est $\{0\}$. Elle ne définit pas un hyperplan.
- **Cas Limite (Dimension Infinie) :** Le théorème de la dimension du dual ($\dim E^* = \dim E$) est **absolument faux** en dimension infinie. Par exemple, l'espace des polynômes $\mathbb{R}[X]$ a une base dénombrable, mais son dual abstrait a une base de cardinalité indénombrable. L'isomorphisme canonique vers le bidual s'effondre (l'application $\Psi$ est seulement injective, plus surjective).

## 3. Démonstrations
### Démonstration du Théorème Pivot : Dimension d'un hyperplan
Soit $H$ un hyperplan de $E$ (dimension $n$). Montrons que $\dim H = n-1$.

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
### Exercice 1 : Application Directe (Base Duale)
**Énoncé :** Dans $\mathbb{R}^2$, soit $\mathcal{B} = (e_1, e_2)$ avec $e_1 = (1, 1)$ et $e_2 = (1, 0)$. Exprimer les formes linéaires $e^*_1$ et $e^*_2$ en fonction des coordonnées canoniques $(x, y)$.
**Correction Détaillée :**
1. Soit $\phi(x, y) = ax + by$ une forme linéaire.
2. Pour $e^*_1$ :
   - $e^*_1(e_1) = 1 \implies e^*_1(1, 1) = a+b = 1$
   - $e^*_1(e_2) = 0 \implies e^*_1(1, 0) = a = 0$
   - On en tire $a=0$ et $b=1$. Donc $e^*_1(x, y) = y$.
3. Pour $e^*_2$ :
   - $e^*_2(e_1) = 0 \implies e^*_2(1, 1) = a+b = 0$
   - $e^*_2(e_2) = 1 \implies e^*_2(1, 0) = a = 1$
   - On en tire $a=1$ et $b=-1$. Donc $e^*_2(x, y) = x - y$.
**Conclusion :** $\mathcal{B}^* = (y, x-y)$.

**Correction exhaustive :**
1. **Démonstration de la nature de base de $\mathcal{B}$ :**
   Il suffit de montrer que la famille est libre. Posons $\alpha_1 v_1 + \alpha_2 v_2 + \alpha_3 v_3 = 0$.
   $\alpha_1(1, 1, 0) + \alpha_2(0, 1, 1) + \alpha_3(1, 0, 1) = (0, 0, 0)$
   Cela induit le système :
   (i) $\alpha_1 + \alpha_3 = 0$
   (ii) $\alpha_1 + \alpha_2 = 0$
   (iii) $\alpha_2 + \alpha_3 = 0$
   De (i), $\alpha_3 = -\alpha_1$. De (ii), $\alpha_2 = -\alpha_1$. En remplaçant dans (iii) : $-\alpha_1 - \alpha_1 = 0 \implies -2\alpha_1 = 0 \implies \alpha_1 = 0$.
   Par conséquent, $\alpha_1 = \alpha_2 = \alpha_3 = 0$. La famille est libre, et possédant 3 vecteurs en dimension 3, elle constitue une base de $E$.

2. **Construction de $v_1^*$ :**
   Cherchons $v_1^*$ sous la forme $v_1^*(x, y, z) = ax + by + cz$. Les relations de dualité exigent :
   - $v_1^*(v_1) = 1 \implies a + b = 1$
   - $v_1^*(v_2) = 0 \implies b + c = 0 \implies c = -b$
   - $v_1^*(v_3) = 0 \implies a + c = 0 \implies a = -c = b$
   En substituant $a = b$ dans la première équation : $b + b = 1 \implies b = \frac{1}{2}$. On tire $a = \frac{1}{2}$ et $c = -\frac{1}{2}$.
   Ainsi, $v_1^*(x, y, z) = \frac{1}{2}x + \frac{1}{2}y - \frac{1}{2}z$.

3. **Construction de $v_2^*$ :**
   Cherchons $v_2^*(x, y, z) = a'x + b'y + c'z$.
   - $v_2^*(v_1) = 0 \implies a' + b' = 0 \implies a' = -b'$
   - $v_2^*(v_2) = 1 \implies b' + c' = 1$
   - $v_2^*(v_3) = 0 \implies a' + c' = 0 \implies c' = -a' = b'$
   Dans la deuxième : $b' + b' = 1 \implies b' = \frac{1}{2}$. D'où $c' = \frac{1}{2}$ et $a' = -\frac{1}{2}$.
   Ainsi, $v_2^*(x, y, z) = -\frac{1}{2}x + \frac{1}{2}y + \frac{1}{2}z$.

4. **Construction de $v_3^*$ :**
   Cherchons $v_3^*(x, y, z) = a''x + b''y + c''z$.
   - $v_3^*(v_1) = 0 \implies a'' + b'' = 0 \implies b'' = -a''$
   - $v_3^*(v_2) = 0 \implies b'' + c'' = 0 \implies c'' = -b'' = a''$
   - $v_3^*(v_3) = 1 \implies a'' + c'' = 1 \implies a'' + a'' = 1 \implies a'' = \frac{1}{2}$.
   D'où $c'' = \frac{1}{2}$ et $b'' = -\frac{1}{2}$.
   Ainsi, $v_3^*(x, y, z) = \frac{1}{2}x - \frac{1}{2}y + \frac{1}{2}z$.

### Exercice 2 : Orthogonal d'un Sous-espace
**Énoncé :**
Soit $E$ un espace vectoriel de dimension $n$. Montrer que si $F$ et $G$ sont deux sous-espaces de $E$ tels que $F \subseteq G$, alors au sens de la dualité, $G^\perp \subseteq F^\perp$. Montrer ensuite que $\dim(F) + \dim(F^\perp) = n$.

**Correction exhaustive :**
1. **Inclusion des orthogonaux :**
   Soit $\phi \in G^\perp$. Par la définition de l'orthogonal dans le dual, cela signifie que pour tout vecteur $x \in G$, nous avons $\phi(x) = 0$.
   Puisque l'hypothèse garantit que $F \subseteq G$, tout vecteur $y \in F$ est aussi un élément de $G$.
   Par conséquent, l'évaluation de $\phi$ sur tout vecteur de $F$ donne $\phi(y) = 0$.
   Ceci certifie que $\phi$ annule entièrement $F$. Ainsi, $\phi \in F^\perp$. L'inclusion $G^\perp \subseteq F^\perp$ est rigoureusement prouvée.

2. **Équation de dimension (Théorème d'isomorphisme canonique) :**
   Considérons l'application de restriction $\rho : E^* \to F^*$ définie par $\rho(\phi) = \phi_{|F}$, qui à une forme linéaire sur $E$ associe sa restriction au sous-espace $F$.
   L'application $\rho$ est clairement linéaire.
   Identifions son noyau. Une forme $\phi$ appartient à $\ker \rho$ si et seulement si sa restriction à $F$ est l'application nulle, c'est-à-dire que pour tout $x \in F, \phi(x) = 0$. C'est l'exacte définition de $F^\perp$. Donc $\ker \rho = F^\perp$.
   Démontrons la surjectivité de $\rho$. Soit $\psi \in F^*$ une forme linéaire définie uniquement sur $F$. Soit un supplémentaire $S$ de $F$ dans $E$ (tel que $E = F \oplus S$). Tout vecteur $x \in E$ se décompose de manière unique en $x = y + z$ avec $y \in F, z \in S$. On définit $\tilde{\psi} \in E^*$ par $\tilde{\psi}(x) = \psi(y) + 0$. Cette forme $\tilde{\psi}$ prolonge $\psi$ à l'espace total $E$, ce qui prouve que toute forme de $F^*$ admet un antécédent. L'application $\rho$ est donc surjective, et $\text{Im }\rho = F^*$.
   Par l'application rigoureuse du théorème du rang à l'application $\rho$ :
   $$\dim(E^*) = \dim(\ker \rho) + \dim(\text{Im }\rho)$$
   Nous savons que $\dim(E^*) = n$ et $\dim(F^*) = \dim(F)$ (puisque la dimension du dual est égale à celle du primal).
   En substituant : $n = \dim(F^\perp) + \dim(F)$.

## 5. Application en Intelligence Artificielle
- **Le Pont Théorique :** Les hyperplans sont les **Séparateurs Linéaires** fondamentaux de l'apprentissage automatique.
- **Exemple Concret :** Dans les **SVM (Support Vector Machines)**, l'algorithme cherche l'hyperplan optimal qui sépare deux classes de données (ex: Spam vs Non-Spam). L'équation de l'hyperplan $\phi(x) + b = 0$ (où $\phi$ est une forme linéaire) définit la frontière de décision. La **Dualité de Lagrange**, utilisée pour résoudre ce problème d'optimisation, repose entièrement sur le passage de l'espace des données (primal) à l'espace des contraintes (dual).

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon-7.md|Jalon 7 (Espaces vectoriels abstraits)]], [[Jalon-8.md|Jalon 8 (Applications linéaires)]]
- **Concepts Futurs dépendants :** [[Jalon 12 (Livrable IA).md|Jalon 12 (Livrable IA)]], [[Jalon-25.md|Jalon 25 (Formes bilinéaires)]], [[Jalon-123.md|Jalon 123 (Problèmes d'optimisation sous contraintes)]]
