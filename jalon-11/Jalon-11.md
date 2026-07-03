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

La genèse de la notion de dualité puise ses racines dans l'observation fondamentale que tout objet géométrique ou algébrique gagne à être étudié non seulement de l'intérieur, par sa constitution atomique (ses coordonnées dans une base), mais aussi de l'extérieur, par la manière dont il interagit avec des instruments de mesure. Imaginez un espace tridimensionnel comme une salle emplie de particules. Un vecteur représente la position ou la vitesse d'une de ces particules. Une forme linéaire n'est pas un objet spatial de même nature ; c'est un détecteur, un regard posé sur l'espace. Si l'on conçoit la température comme variant linéairement dans la pièce, le thermomètre évalue chaque position et lui attribue un scalaire unique. L'ensemble de ces "regards" possibles, de ces instruments d'évaluation, forme un nouvel univers : l'espace dual.

L'hyperplan, dans cette optique, s'impose comme la frontière naturelle. En deux dimensions, c'est la ligne parfaite tranchant le plan ; en trois dimensions, le feuillet infiniment mince scindant l'espace. Structurellement, l'hyperplan est le lieu géométrique de silence absolu pour une forme linéaire donnée, c'est-à-dire l'ensemble exact des vecteurs que l'instrument de mesure évalue à zéro, le "niveau de la mer" de notre topographie abstraite. C'est cette interaction entre l'objet mesuré (le primal) et l'instrument de mesure (le dual) qui donne naissance à la notion profonde d'orthogonalité, généralisant la perpendicularité euclidienne au-delà des structures dotées d'un produit scalaire usuel.

## 2. Formalisation

### A. Définitions Formelles et Typage Rigoureux

Soit $E$ un espace vectoriel sur un corps commutatif $\mathbb{K}$ (typiquement $\mathbb{R}$ ou $\mathbb{C}$). On suppose dans la suite que la dimension de $E$ est finie, notée $n \in \mathbb{N}^*$.

**Forme linéaire :**
Une forme linéaire sur $E$ est une application $\phi : E \to \mathbb{K}$ qui est strictement linéaire sur le corps $\mathbb{K}$. Formellement, on requiert :
$$\forall x, y \in E, \forall \lambda, \mu \in \mathbb{K}, \quad \phi(\lambda x + \mu y) = \lambda \phi(x) + \mu \phi(y)$$

**Espace Dual ($E^*$) :**
L'espace dual de $E$, noté $E^*$, est l'espace vectoriel constitué de l'ensemble de toutes les formes linéaires sur $E$. Il s'identifie à l'espace des applications linéaires $\mathcal{L}(E, \mathbb{K})$. L'addition et la multiplication par un scalaire dans $E^*$ sont héritées point par point :
$$(\phi_1 + \phi_2)(x) = \phi_1(x) + \phi_2(x) \quad \text{et} \quad (\lambda \phi)(x) = \lambda \phi(x)$$

**Hyperplan :**
Un sous-espace vectoriel $H$ de $E$ est un hyperplan si et seulement s'il existe une forme linéaire non nulle $\phi \in E^*$ (soit $\phi \neq 0_{E^*}$) telle que $H = \ker \phi$. Le noyau de $\phi$, défini par $\{x \in E \mid \phi(x) = 0_\mathbb{K}\}$, caractérise entièrement cet espace frontière.

**Base Duale :**
Soit $\mathcal{B} = (e_1, \dots, e_n)$ une base de $E$. On définit la famille d'applications $\mathcal{B}^* = (e^*_1, \dots, e^*_n)$ de $E^*$ par leurs évaluations sur les vecteurs de base :
$$e^*_i(e_j) = \delta_{i,j}$$
où $\delta_{i,j}$ est le symbole de Kronecker (valant $1$ si $i=j$ et $0$ sinon). Par prolongement linéaire, $e^*_i(x)$ renvoie la $i$-ème coordonnée de $x$ dans la base $\mathcal{B}$. La famille $\mathcal{B}^*$ constitue une base de l'espace dual $E^*$, appelée base duale.

**Orthogonalité (Dualité) :**
Pour toute partie $A \subseteq E$, on définit l'orthogonal de $A$ (dans le dual) comme l'ensemble des annihilateurs de $A$ :
$$A^\perp = \{ \phi \in E^* \mid \forall x \in A, \phi(x) = 0 \}$$
Symétriquement, pour $B \subseteq E^*$, on définit $B^\circ = \{ x \in E \mid \forall \phi \in B, \phi(x) = 0 \}$.

### B. Théorèmes Fondamentaux

**Théorème de la dimension du Dual :**
Si $\dim(E) = n$, alors l'espace dual $E^*$ est de dimension finie et $\dim(E^*) = n$.
*Corollaire structural :* Si $H$ est un hyperplan de $E$, alors $\dim(H) = n - 1$.

**Théorème du Bidual et Isomorphisme Canonique :**
Soit $E^{**} = (E^*)^*$ l'espace bidual. L'application d'évaluation $\Psi : E \to E^{**}$ définie par $\Psi(x)(\phi) = \phi(x)$ pour tout $x \in E$ et $\phi \in E^*$ est un isomorphisme canonique (indépendant du choix d'une base) dès lors que $E$ est de dimension finie. On a ainsi $E \cong E^{**}$.

### C. Exemples et Cas Pathologiques

**Exemple de validation (Formes coordonnées) :**
Dans $\mathbb{R}^3$, pour un vecteur $x = (x_1, x_2, x_3)$, l'application $\phi(x) = 2x_1 - 3x_2 + x_3$ est une forme linéaire. Son noyau définit l'hyperplan vectoriel d'équation $2x_1 - 3x_2 + x_3 = 0$, qui est un plan passant par l'origine.

**Cas pathologique (Dimension infinie) :**
Si $E = \mathbb{R}[X]$ (l'espace des polynômes, de dimension infinie), la famille $(X^k)_{k \in \mathbb{N}}$ est une base. On peut définir les formes coordonnées $e_k^*$ par $e_k^*(X^j) = \delta_{k,j}$. Toutefois, la famille $(e_k^*)_{k \in \mathbb{N}}$ n'engendre pas $E^*$ ! En effet, la forme linéaire $\phi(P) = P(1) = \sum a_k$ ne peut s'écrire comme une combinaison linéaire finie des $e_k^*$. En dimension infinie, $E$ et $E^*$ ne sont pas isomorphes ($E^*$ a une dimension strictement "plus grande" que $E$).

## 3. Démonstrations

### Démonstration de la Dimension d'un Hyperplan

Soit $H$ un hyperplan de $E$, un $\mathbb{K}$-espace vectoriel de dimension $n$. Montrons que $\dim(H) = n - 1$.

1. Par la définition formelle d'un hyperplan, il existe une forme linéaire $\phi \in E^*$ telle que $\phi$ n'est pas l'application nulle ($\phi \neq 0_{E^*}$) et $H = \ker \phi$.
2. Considérons l'application linéaire $\phi : E \to \mathbb{K}$. Le théorème du rang nous assure l'égalité structurelle :
   $$\dim(E) = \dim(\ker \phi) + \text{rg}(\phi)$$
   En substituant $H$ et $n$, nous obtenons $n = \dim(H) + \dim(\text{Im }\phi)$.
3. Le sous-espace $\text{Im }\phi$ est un sous-espace vectoriel du corps $\mathbb{K}$ (considéré comme $\mathbb{K}$-espace vectoriel de dimension $1$). Les seuls sous-espaces de $\mathbb{K}$ sont $\{0_\mathbb{K}\}$ et $\mathbb{K}$.
4. Puisque la forme linéaire $\phi$ n'est pas identiquement nulle, il existe nécessairement au moins un vecteur $v \in E$ tel que $\phi(v) \neq 0_\mathbb{K}$. L'image $\text{Im }\phi$ n'est donc pas réduite à $\{0_\mathbb{K}\}$.
5. Conséquemment, $\text{Im }\phi = \mathbb{K}$, ce qui implique que $\dim(\text{Im }\phi) = \dim(\mathbb{K}) = 1$. $\phi$ est donc surjective.
6. L'équation issue du théorème du rang devient :
   $$n = \dim(H) + 1$$
7. En isolant la dimension de l'hyperplan, on déduit irréfutablement :
   $$\dim(H) = n - 1$$

### Démonstration de l'Isomorphisme Canonique vers le Bidual

Soit $\Psi : E \to E^{**}$ l'application définie pour tout $x \in E$ par $\Psi(x) = \text{ev}_x$, où $\text{ev}_x(\phi) = \phi(x)$ pour toute forme $\phi \in E^*$. Montrons que $\Psi$ est un isomorphisme lorsque $\dim(E) = n$.

1. **Vérification de la nature de l'application :**
   Pour tout $x \in E$, $\Psi(x)$ est bien une forme linéaire sur $E^*$. En effet, pour $\phi_1, \phi_2 \in E^*$ et $\alpha, \beta \in \mathbb{K}$ :
   $$\Psi(x)(\alpha \phi_1 + \beta \phi_2) = (\alpha \phi_1 + \beta \phi_2)(x) = \alpha \phi_1(x) + \beta \phi_2(x) = \alpha \Psi(x)(\phi_1) + \beta \Psi(x)(\phi_2)$$
   Ainsi, $\Psi(x) \in (E^*)^* = E^{**}$.

2. **Linéarité de $\Psi$ :**
   Montrons que $\Psi$ est elle-même linéaire. Soient $x, y \in E$ et $\lambda, \mu \in \mathbb{K}$. Il faut démontrer que $\Psi(\lambda x + \mu y) = \lambda \Psi(x) + \mu \Psi(y)$ dans $E^{**}$.
   Évaluons ces deux membres sur une forme quelconque $\phi \in E^*$ :
   $$\Psi(\lambda x + \mu y)(\phi) = \phi(\lambda x + \mu y)$$
   Par la stricte linéarité de $\phi$ sur $E$, nous déployons :
   $$\phi(\lambda x + \mu y) = \lambda \phi(x) + \mu \phi(y) = \lambda \Psi(x)(\phi) + \mu \Psi(y)(\phi) = (\lambda \Psi(x) + \mu \Psi(y))(\phi)$$
   Cette égalité étant vraie pour toute forme $\phi \in E^*$, on conclut que $\Psi(\lambda x + \mu y) = \lambda \Psi(x) + \mu \Psi(y)$. L'application $\Psi$ est donc linéaire.

3. **Injectivité de $\Psi$ :**
   Caractérisons le noyau de $\Psi$. Soit $x \in \ker \Psi$. Cela signifie que $\Psi(x) = 0_{E^{**}}$, soit pour toute forme linéaire $\phi \in E^*$, $\phi(x) = 0_\mathbb{K}$.
   Supposons par l'absurde que $x \neq 0_E$. Comme $E$ est de dimension finie $n$, et $x$ est un vecteur non nul, le théorème de la base incomplète nous autorise à construire une base de $E$ de la forme $\mathcal{B} = (e_1, e_2, \dots, e_n)$ où le premier vecteur est posé comme $e_1 = x$.
   Considérons la base duale $\mathcal{B}^* = (e_1^*, e_2^*, \dots, e_n^*)$. Par définition, la forme linéaire $e_1^*$ vérifie $e_1^*(e_1) = 1_\mathbb{K}$.
   Mais puisque $e_1 = x$, nous aurions $e_1^*(x) = 1_\mathbb{K}$.
   Or, l'hypothèse $x \in \ker \Psi$ impose que $\phi(x) = 0_\mathbb{K}$ pour absolument toute forme $\phi$, y compris $e_1^*$. Nous obtenons la contradiction $1_\mathbb{K} = 0_\mathbb{K}$.
   L'hypothèse $x \neq 0_E$ est donc erronée. Le noyau est réduit au vecteur nul : $\ker \Psi = \{0_E\}$. L'application $\Psi$ est strictement injective.

4. **Conclusion par argument de dimension :**
   Nous savons que $\dim(E^*) = \dim(E) = n$. Par application successive du même théorème, la dimension de l'espace bidual est $\dim(E^{**}) = \dim(E^*) = n$.
   Puisque $\Psi : E \to E^{**}$ est une application linéaire injective entre deux espaces vectoriels de même dimension finie $n$, le théorème de l'isomorphisme en dimension finie stipule que $\Psi$ est nécessairement surjective, et donc bijective. C'est un isomorphisme canonique.

## 4. Exercices d'Application

### Exercice 1 : Explicitation d'une Base Duale
**Énoncé :**
Soit $E = \mathbb{R}^3$. On considère la famille de vecteurs $\mathcal{B} = (v_1, v_2, v_3)$ avec $v_1 = (1, 1, 0)$, $v_2 = (0, 1, 1)$ et $v_3 = (1, 0, 1)$. Démontrer que $\mathcal{B}$ est une base de $\mathbb{R}^3$ et construire explicitement la base duale associée $\mathcal{B}^* = (v_1^*, v_2^*, v_3^*)$ exprimée en fonction des coordonnées canoniques $(x, y, z)$.

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

Dans le cadre du Machine Learning et particulièrement de l'apprentissage statistique géométrique, la notion d'hyperplan est le socle de l'algorithme des machines à vecteurs de support (Support Vector Machines, SVM). L'objectif est de trouver un classifieur linéaire capable de discriminer deux catégories de données (par exemple des vecteurs $x_i \in \mathbb{R}^n$ étiquetés $+1$ et $-1$). Ce séparateur optimal est géométriquement décrit comme un hyperplan, dont l'équation caractéristique est modélisée par une forme linéaire $\phi(x) + b = 0$.
La puissance de la modélisation réside dans l'exploitation du théorème de bidualité. La minimisation de la norme du classifieur (le problème primal) est transformée, via le Lagrangien, en un problème de maximisation sur l'espace dual. Dans ce cadre dual, les variables d'optimisation (les multiplicateurs de Lagrange) agissent exactement comme des composantes de formes linéaires évaluant le poids critique (le "support") de chaque donnée d'apprentissage, réduisant ainsi drastiquement la complexité calculatoire pour les espaces de très haute dimension.

## 6. Liens Sémantiques
- **Concepts Précédents requis :** [[Jalon 7 (Espaces vectoriels abstraits)]], [[Jalon 8 (Applications linéaires)]]
- **Concepts Futurs dépendants :** [[Jalon 12 (Livrable IA)]], [[Jalon 25 (Formes bilinéaires)]], [[Jalon 123 (Problèmes d'optimisation sous contraintes)]]
