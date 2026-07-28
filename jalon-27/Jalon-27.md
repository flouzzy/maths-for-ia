---
uuid: "jalon-27"
title: "Endomorphismes symétriques, adjoint d'un opérateur et matrices orthogonales"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/matrices-symetriques
prev: "[[Jalon 26 (Espaces euclidiens).md]]"
next: "[[Jalon 28 (Polynômes d'endomorphismes).md]]"
---
# Jalon 27 : Endomorphismes symétriques, adjoint d'un opérateur et matrices orthogonales

## 1. Échafaudage Cognitif & Traçabilité Historique

L'algèbre linéaire a longtemps été considérée comme l'étude des transformations de l'espace abstrait. Mais lorsque l'on munit cet espace d'une géométrie stricte par le biais d'un produit scalaire (une "métrique"), de nouvelles questions vertigineuses émergent. Si je dispose d'une transformation (un endomorphisme) qui déforme l'espace, comment cette déformation interagit-elle avec la géométrie sous-jacente ? Existe-t-il des transformations qui "respectent" parfaitement l'angle et la distance, ou qui se déforment d'une manière si harmonieuse qu'elles conservent des directions privilégiées immuables ?

Historiquement, l'étude des endomorphismes symétriques trouve ses racines dans la mécanique céleste et l'étude des quadriques (coniques en dimension 2, ellipsoïdes en dimension 3). Augustin-Louis Cauchy, au début du XIXe siècle, cherchait à comprendre les axes principaux d'inertie des solides. Pourquoi un objet en rotation a-t-il toujours des axes naturels autour desquels il tourne sans "vaciller" ? La réponse mathématique est éblouissante de pureté : la matrice d'inertie est symétrique, et toute matrice symétrique, par un miracle algébrique, possède un ensemble de directions orthogonales qu'elle se contente d'étirer ou de compresser, sans jamais les faire pivoter. C'est l'essence même du célèbre théorème spectral.

Pour y parvenir, les mathématiciens ont dû inventer un concept miroir : l'adjoint d'un opérateur. L'adjoint, souvent noté $f^*$, est une construction intellectuelle fascinante. Imaginez que vous appliquez une transformation $f$ à un vecteur $x$, puis que vous mesurez sa "projection" (produit scalaire) sur un vecteur test $y$. L'opérateur adjoint $f^*$ est la machine qui vous permet d'obtenir *exactement le même résultat de mesure* en laissant $x$ tranquille, mais en appliquant au préalable $f^*$ à $y$. C'est une dualité fondamentale. Un opérateur "symétrique" est simplement un opérateur qui est son propre miroir : l'effet qu'il a sur le monde est indiscernable de l'effet que le monde a sur lui. En Intelligence Artificielle, cette symétrie se retrouve partout, des matrices de covariance dans l'Analyse en Composantes Principales (PCA) aux matrices hessiennes de la fonction de coût, régissant la courbure de l'espace d'optimisation.

## 2. Protocole d'Exégèse Conceptuelle

### 2.1. L'Adjoint d'un Opérateur (Endomorphisme)

**A. Énoncé Symbolique Strict**

Soit $(E, \langle \cdot, \cdot \rangle)$ un espace euclidien (donc de dimension finie sur $\mathbb{R}$).
Pour tout endomorphisme $f \in \mathcal{L}(E)$, il existe un unique endomorphisme, noté $f^*$, appelé l'adjoint de $f$, tel que :
$$ \forall (x,y) \in E \times E, \quad \langle f(x), y \rangle = \langle x, f^*(y) \rangle $$

**B. Anatomie et Typage Chirurgical**
- $E$ : Un espace vectoriel sur le corps des réels $\mathbb{R}$, de dimension finie, muni d'un produit scalaire défini positif. L'hypothèse de dimension finie garantit l'existence de l'adjoint par le théorème de représentation de Riesz.
- $\langle \cdot, \cdot \rangle : E \times E \to \mathbb{R}$ : La forme bilinéaire symétrique définie positive équipant $E$.
- $f \in \mathcal{L}(E)$ : Un opérateur linéaire transformant les vecteurs de $E$ en d'autres vecteurs de $E$.
- $x, y \in E$ : Deux vecteurs quelconques sur lesquels s'opère la "mesure" d'interaction via le produit scalaire.
- L'égalité traduit un transfert de l'action de $f$ d'un côté du produit scalaire vers l'autre.

**C. Exemples de Validation**
- *Exemple trivial :* Si $f = \text{Id}_E$ (l'identité), on a $\langle \text{Id}_E(x), y \rangle = \langle x, y \rangle = \langle x, \text{Id}_E(y) \rangle$. Donc l'adjoint de l'identité est elle-même : $\text{Id}_E^* = \text{Id}_E$.
- *Exemple matriciel :* Si $E = \mathbb{R}^n$ muni du produit scalaire canonique $\langle X, Y \rangle = X^T Y$, et $f$ est représentée par la matrice $A$. Alors $\langle AX, Y \rangle = (AX)^T Y = X^T A^T Y = \langle X, A^T Y \rangle$. L'adjoint de $f$ est représenté par la matrice transposée $A^T$.

**D. Cas Pathologiques et Contre-exemples**
- *Dimension infinie :* Si $E$ est un espace préhilbertien de dimension infinie, l'existence de l'adjoint n'est pas garantie pour un endomorphisme continu quelconque. Il faut se placer dans un espace de Hilbert (complet) pour s'appuyer sur le théorème de Riesz, et même là, l'adjoint d'opérateurs non bornés devient un sujet extrêmement subtil nécessitant la définition précise du domaine de définition $\mathcal{D}(f^*)$.

### 2.2. Endomorphismes Symétriques

**A. Énoncé Symbolique Strict**

Un endomorphisme $f \in \mathcal{L}(E)$ d'un espace euclidien est dit symétrique (ou autoadjoint) si :
$$ f = f^* \iff \forall (x,y) \in E^2, \quad \langle f(x), y \rangle = \langle x, f(y) \rangle $$
Dans une base orthonormée $\mathcal{B}$, la matrice $A = \text{Mat}_{\mathcal{B}}(f)$ est symétrique, c'est-à-dire $A^T = A$.

**B. Anatomie et Typage Chirurgical**
- $f = f^*$ : Égalité dans l'espace $\mathcal{L}(E)$. L'opérateur coïncide parfaitement avec son adjoint.
- Base orthonormée : Il est crucial de noter que la correspondance entre "endomorphisme symétrique" et "matrice symétrique" n'est vraie que si la base de projection est orthonormée. Dans une base quelconque, la transposée ne représente pas l'adjoint !

**C. Exemples de Validation**
- *Exemple trivial :* L'endomorphisme nul et l'identité sont symétriques.
- *Exemple géométrique :* La projection orthogonale $p$ sur un sous-espace $F$. On a $x = x_F + x_{F^\perp}$ et $y = y_F + y_{F^\perp}$.
$\langle p(x), y \rangle = \langle x_F, y_F + y_{F^\perp} \rangle = \langle x_F, y_F \rangle$.
De même $\langle x, p(y) \rangle = \langle x_F + x_{F^\perp}, y_F \rangle = \langle x_F, y_F \rangle$. Donc $p = p^*$.

**D. Cas Pathologiques et Contre-exemples**
- Une projection oblique (non orthogonale) n'est jamais symétrique. L'asymétrie de la projection (qui "pousse" l'espace de biais) détruit la propriété miroir vis-à-vis du produit scalaire canonique.

### 2.3. Matrices et Transformations Orthogonales (Isométries)

**A. Énoncé Symbolique Strict**

Un endomorphisme $u \in \mathcal{L}(E)$ est orthogonal (ou une isométrie vectorielle) si :
$$ \forall x \in E, \quad \|u(x)\| = \|x\| $$
Une matrice $O \in \mathcal{M}_n(\mathbb{R})$ est orthogonale si :
$$ O^T O = O O^T = I_n $$

**B. Anatomie et Typage Chirurgical**
- $\| \cdot \|$ : La norme induite par le produit scalaire. La conservation de la norme implique (par identité de polarisation) la conservation du produit scalaire : $\langle u(x), u(y) \rangle = \langle x, y \rangle$.
- $O^T O = I_n$ : Les colonnes (et les lignes) de $O$ forment une base orthonormée de $\mathbb{R}^n$.

**C. Exemples de Validation**
- *Rotations et Réflexions :* En dimension 2, la matrice $R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ satisfait $R_\theta^T R_\theta = I_2$. C'est une isométrie qui conserve les distances et les angles.

**D. Cas Pathologiques et Contre-exemples**
- Matrice orthogonale vs matrice symétrique : Attention à ne pas confondre. $R_{\pi/2}$ est orthogonale mais pas symétrique. Inversement, $2I_n$ est symétrique mais pas orthogonale (elle étire les vecteurs). Les matrices à la fois symétriques et orthogonales sont les symétries orthogonales ($s^2 = Id$ et $s^* = s$).

## 3. Zéro Ellipse : Preuves Exhaustives

### 3.1. Théorème d'existence et unicité de l'adjoint

**Énoncé :** Pour tout $f \in \mathcal{L}(E)$, il existe un unique $f^*$ tel que $\forall x, y, \langle f(x), y \rangle = \langle x, f^*(y) \rangle$.

**Démonstration :**
1. Fixons un vecteur $y \in E$.
2. Considérons l'application $\varphi_y : E \to \mathbb{R}$ définie par $\varphi_y(x) = \langle f(x), y \rangle$.
3. Montrons que $\varphi_y$ est une forme linéaire sur $E$.
   Soient $x_1, x_2 \in E$ et $\lambda \in \mathbb{R}$.
   $\varphi_y(\lambda x_1 + x_2) = \langle f(\lambda x_1 + x_2), y \rangle$.
   Par linéarité de $f$, $f(\lambda x_1 + x_2) = \lambda f(x_1) + f(x_2)$.
   Par bilinéarité (linéarité à gauche) du produit scalaire,
   $\langle \lambda f(x_1) + f(x_2), y \rangle = \lambda \langle f(x_1), y \rangle + \langle f(x_2), y \rangle = \lambda \varphi_y(x_1) + \varphi_y(x_2)$.
   Donc $\varphi_y \in E^*$.
4. D'après le théorème de représentation de Riesz (qui stipule que l'application $z \mapsto \langle \cdot, z \rangle$ est un isomorphisme de $E$ sur $E^*$), il existe un unique vecteur $z_y \in E$ tel que pour tout $x \in E$, $\varphi_y(x) = \langle x, z_y \rangle$.
5. On définit alors l'application $f^* : E \to E$ par $f^*(y) = z_y$. Par construction, $\langle f(x), y \rangle = \langle x, f^*(y) \rangle$.
6. Montrons que $f^*$ est linéaire. Soient $y_1, y_2 \in E$ et $\alpha \in \mathbb{R}$. Pour tout $x \in E$, évaluons le produit scalaire :
   $\langle x, f^*(\alpha y_1 + y_2) \rangle = \langle f(x), \alpha y_1 + y_2 \rangle$.
   Par linéarité à droite du produit scalaire (rappelons que sur $\mathbb{R}$, bilinéaire implique linéaire des deux côtés),
   $\langle f(x), \alpha y_1 + y_2 \rangle = \alpha \langle f(x), y_1 \rangle + \langle f(x), y_2 \rangle$.
   En appliquant la définition de $f^*$ aux deux termes :
   $\alpha \langle f(x), y_1 \rangle + \langle f(x), y_2 \rangle = \alpha \langle x, f^*(y_1) \rangle + \langle x, f^*(y_2) \rangle = \langle x, \alpha f^*(y_1) + f^*(y_2) \rangle$.
   Ainsi, $\forall x \in E, \langle x, f^*(\alpha y_1 + y_2) - (\alpha f^*(y_1) + f^*(y_2)) \rangle = 0$.
   Le seul vecteur orthogonal à tout l'espace étant le vecteur nul, on en déduit formellement $f^*(\alpha y_1 + y_2) = \alpha f^*(y_1) + f^*(y_2)$.
   $f^*$ est donc bien un endomorphisme.

### 3.2. Propriété d'orthogonalité des sous-espaces propres (Symétriques)

**Énoncé :** Si $f$ est un endomorphisme symétrique, alors les sous-espaces propres associés à des valeurs propres distinctes sont deux à deux orthogonaux.

**Démonstration :**
1. Soient $\lambda, \mu \in \mathbb{R}$ deux valeurs propres distinctes de $f$ ($\lambda \neq \mu$).
2. Soient $x \in E_\lambda$ et $y \in E_\mu$ deux vecteurs propres associés, c'est-à-dire $f(x) = \lambda x$ et $f(y) = \mu y$.
3. Calculons la quantité $\langle f(x), y \rangle$.
   D'une part, en remplaçant $f(x)$ :
   $\langle f(x), y \rangle = \langle \lambda x, y \rangle$.
   Par linéarité à gauche du produit scalaire :
   $\langle \lambda x, y \rangle = \lambda \langle x, y \rangle$.
4. D'autre part, en utilisant la symétrie de l'endomorphisme $f$ ($f = f^*$) :
   $\langle f(x), y \rangle = \langle x, f^*(y) \rangle = \langle x, f(y) \rangle$.
   En remplaçant $f(y)$ par $\mu y$ :
   $\langle x, \mu y \rangle = \mu \langle x, y \rangle$ (par symétrie et linéarité à gauche du produit scalaire).
5. En égalisant les deux résultats obtenus :
   $\lambda \langle x, y \rangle = \mu \langle x, y \rangle$.
   En soustrayant :
   $(\lambda - \mu) \langle x, y \rangle = 0$.
6. Puisque par hypothèse les valeurs propres sont distinctes ($\lambda - \mu \neq 0$), l'intégrité du corps des réels impose nécessairement que le second facteur soit nul :
   $\langle x, y \rangle = 0$.
7. Les vecteurs $x$ et $y$ sont donc orthogonaux. Par extension, tous les vecteurs de $E_\lambda$ sont orthogonaux à tous les vecteurs de $E_\mu$, ce qui prouve l'orthogonalité des sous-espaces.

### 3.3. Théorème Spectral (Diagonalisabilité des Endomorphismes Symétriques)

**Énoncé :** Tout endomorphisme symétrique d'un espace euclidien $E$ possède une base orthonormée de vecteurs propres. En d'autres termes, toute matrice réelle symétrique est diagonalisable en base orthonormée : $A = P D P^T$ avec $P$ orthogonale.

*(La preuve complète requiert l'existence d'au moins une valeur propre réelle, généralement démontrée par l'analyse sur les polynômes caractéristiques ou la compacité de la sphère unité, détaillée dans le jalon suivant. Nous admettons ici l'existence d'au moins une valeur propre $\lambda_1$ et d'un vecteur propre unitaire $e_1$).*

**Démonstration par récurrence sur la dimension $n$ :**
1. **Initialisation ($n=1$) :** L'espace est de dimension 1. Tout endomorphisme est représenté par un scalaire, et toute base unitaire $(e_1)$ est orthogonale. La propriété est triviale.
2. **Hérédité :** Supposons le théorème vrai pour tout espace de dimension $n-1$. Soit $E$ un espace de dimension $n$, et $f$ un endomorphisme symétrique sur $E$.
3. On admet que $f$ possède au moins un vecteur propre $e_1$ associé à la valeur propre $\lambda_1$. On normalise ce vecteur tel que $\|e_1\| = 1$.
4. Posons $H = (\text{Vect}(e_1))^\perp$, l'hyperplan orthogonal à $e_1$. $\dim(H) = n - 1$.
5. Montrons que $H$ est stable par $f$.
   Soit $x \in H$. On veut montrer que $f(x) \in H$, c'est-à-dire $\langle f(x), e_1 \rangle = 0$.
   Calculons : $\langle f(x), e_1 \rangle$.
   Par symétrie de $f$ : $\langle f(x), e_1 \rangle = \langle x, f(e_1) \rangle$.
   Puisque $e_1$ est vecteur propre de $f$ : $f(e_1) = \lambda_1 e_1$.
   Donc $\langle x, \lambda_1 e_1 \rangle = \lambda_1 \langle x, e_1 \rangle$.
   Or, $x \in H = (\text{Vect}(e_1))^\perp$, ce qui signifie par définition que $\langle x, e_1 \rangle = 0$.
   Ainsi, $\langle f(x), e_1 \rangle = \lambda_1 \times 0 = 0$.
   Le vecteur $f(x)$ est bien orthogonal à $e_1$, donc $f(x) \in H$. $H$ est stable par $f$.
6. Considérons l'endomorphisme restreint $f_H : H \to H$ défini par $f_H(x) = f(x)$.
   $f_H$ est clairement linéaire et symétrique (car $f$ l'est sur tout $E$, donc sur $H$).
7. Par hypothèse de récurrence, puisque $\dim(H) = n-1$, l'endomorphisme $f_H$ possède une base orthonormée de vecteurs propres dans $H$, notons-la $(e_2, e_3, \dots, e_n)$.
8. En rassemblant ces vecteurs avec $e_1$, la famille $(e_1, e_2, \dots, e_n)$ est constituée de vecteurs propres de $f$.
   Par construction, les $e_2, \dots, e_n$ appartiennent à $H = \{e_1\}^\perp$, donc ils sont tous orthogonaux à $e_1$.
   De plus, $(e_2, \dots, e_n)$ est une famille orthonormée.
   Donc la famille totale $(e_1, e_2, \dots, e_n)$ est orthonormée.
9. C'est une famille orthonormée de $n$ vecteurs dans un espace de dimension $n$, c'est donc une base orthonormée.
10. La récurrence est établie, et le théorème spectral est rigoureusement prouvé.
