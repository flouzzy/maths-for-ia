---
uuid: "jalon-27"
title: "Endomorphismes symétriques, adjoint d'un opérateur et matrices orthogonales"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/matrices-symetriques
prev: "[[Jalon-26.md]]"
next: "[[Jalon-28.md]]"
---
# Jalon 27 : Endomorphismes symétriques, adjoint d'un opérateur et matrices orthogonales

## 1. L'Échafaudage Cognitif & Traçabilité Historique

L'étude des transformations de l'espace est au cœur de l'algèbre linéaire, mais toutes les transformations ne se valent pas. Historiquement, l'évolution de la physique classique vers la mécanique quantique a mis en évidence le rôle singulier des opérateurs qui préservent certaines structures fondamentales. Au XIXe siècle, les travaux de mathématiciens comme Augustin-Louis Cauchy et Karl Weierstrass sur les formes quadratiques et la géométrie des surfaces (comme les ellipsoïdes) ont révélé une connexion profonde entre la symétrie algébrique et l'orthogonalité géométrique.

Pourquoi s'intéresser spécifiquement aux endomorphismes symétriques et aux matrices orthogonales ? Le problème initial était de comprendre comment trouver un système d'axes naturels pour étudier une déformation de l'espace. Si vous étirez une feuille de caoutchouc de manière hétérogène, existe-t-il des directions qui ne font que s'allonger ou se contracter sans tourner ? Cauchy a démontré que pour une déformation "symétrique", il existe toujours un ensemble de directions mutuellement perpendiculaires (une base orthonormée) qui restent inchangées en direction. Ce résultat spectaculaire, connu aujourd'hui sous le nom de théorème spectral, est la clé de voûte de l'analyse en composantes principales (PCA) en intelligence artificielle et de la mécanique quantique (où les observables sont des opérateurs auto-adjoints).

L'opérateur adjoint, quant à lui, est né de la nécessité de "renverser" la perspective lors de l'évaluation du travail d'une transformation sur un produit scalaire. Si un opérateur $f$ agit sur un vecteur $x$, comment pouvons-nous reporter cette action sur le vecteur $y$ avec lequel on le compare ? L'adjoint est cette construction duale qui équilibre la balance du produit scalaire.

## 2. Le Protocole d'Exégèse Conceptuelle

### A. Énoncé Symbolique Strict

**Définition 1 : Adjoint d'un endomorphisme**
Soit $(E, \langle \cdot, \cdot \rangle)$ un espace euclidien (donc de dimension finie). Pour tout endomorphisme $f \in \mathcal{L}(E)$, il existe un unique endomorphisme, noté $f^*$ et appelé adjoint de $f$, tel que :
$$ \forall (x, y) \in E \times E, \quad \langle f(x), y \rangle = \langle x, f^*(y) \rangle $$

**Définition 2 : Endomorphisme symétrique**
Un endomorphisme $f \in \mathcal{L}(E)$ est dit symétrique (ou auto-adjoint) si $f = f^*$, ce qui équivaut à :
$$ \forall (x, y) \in E \times E, \quad \langle f(x), y \rangle = \langle x, f(y) \rangle $$

**Définition 3 : Matrice Orthogonale**
Une matrice $P \in \mathcal{M}_n(\mathbb{R})$ est dite orthogonale si elle vérifie :
$$ P^T P = I_n $$

### B. Anatomie et Typage Chirurgical

- $E$ est un espace vectoriel sur le corps $\mathbb{R}$, muni d'un produit scalaire défini positif $\langle \cdot, \cdot \rangle$.
- $f \in \mathcal{L}(E)$ : $f$ est une application linéaire de $E$ dans $E$.
- $x, y \in E$ : Ce sont des vecteurs de l'espace, représentant n'importe quelle paire de points.
- $f^*$ : L'adjoint est également un endomorphisme. La garantie de son existence et de son unicité repose sur le théorème de représentation de Riesz.
- $P^T P = I_n$ : L'opération $P^T$ désigne la transposée de la matrice $P$. Cette équation implique que les colonnes de $P$ forment une base orthonormée de $\mathbb{R}^n$ pour le produit scalaire canonique, car le coefficient d'indice $(i, j)$ de $P^T P$ est exactement le produit scalaire de la colonne $i$ avec la colonne $j$. De plus, comme les matrices sont carrées, on a aussi $P P^T = I_n$, donc les lignes forment également une base orthonormée.

### C. Exemples de Validation

**Exemple trivial :** L'endomorphisme identité $\operatorname{Id}_E$.
On a $\langle \operatorname{Id}_E(x), y \rangle = \langle x, y \rangle = \langle x, \operatorname{Id}_E(y) \rangle$. Ainsi $\operatorname{Id}_E^* = \operatorname{Id}_E$, c'est un endomorphisme symétrique. La matrice identité $I_n$ est également orthogonale car $I_n^T I_n = I_n^2 = I_n$.

**Exemple complexe :** Soit $E = \mathbb{R}^2$ avec le produit scalaire usuel, et $f$ l'application dont la matrice dans la base canonique est $A = \begin{pmatrix} 2 & 3 \\ 3 & -1 \end{pmatrix}$.
Puisque $A^T = A$, $f$ est un endomorphisme symétrique. L'image de $x = (x_1, x_2)$ est $(2x_1+3x_2, 3x_1-x_2)$. On peut vérifier manuellement que le produit scalaire $\langle f(x), y \rangle = \langle x, f(y) \rangle$.

### D. Cas Pathologiques et Contre-exemples

- **Espace de dimension infinie :** Si $E$ n'est pas de dimension finie, un opérateur n'admet pas toujours un adjoint. Le théorème de Riesz s'applique aux espaces de Hilbert, mais pour un espace préhilbertien général, $f^*$ peut ne pas exister pour tous les opérateurs continus.
- **Produit scalaire dégénéré :** Si la forme bilinéaire n'est pas définie positive (comme dans l'espace de Minkowski en relativité), la notion d'adjoint devient plus complexe et peut conduire à des espaces propres isotropes (de norme nulle), ruinant l'orthogonalité.
- **Base non orthonormée :** Attention, si $B$ est une base quelconque de $E$, la matrice de $f^*$ dans $B$ n'est **pas** la transposée de la matrice de $f$ dans $B$. L'égalité $\operatorname{Mat}_B(f^*) = (\operatorname{Mat}_B(f))^T$ n'est vraie que si la base $B$ est orthonormée.

## 3. Zéro Ellipse dans les Démonstrations à Blanc

### Théorème : Les sous-espaces propres d'un endomorphisme symétrique sont orthogonaux deux à deux.

**Hypothèses :** Soit $f \in \mathcal{L}(E)$ un endomorphisme symétrique. Soient $\lambda$ et $\mu$ deux valeurs propres distinctes de $f$.
Soit $E_\lambda = \ker(f - \lambda \operatorname{Id})$ et $E_\mu = \ker(f - \mu \operatorname{Id})$ les sous-espaces propres associés.

**Démonstration :**
Nous devons montrer que pour tout $x \in E_\lambda$ et pour tout $y \in E_\mu$, on a $\langle x, y \rangle = 0$.

1. Soit $x \in E_\lambda$. Par définition de la valeur propre et du vecteur propre associé, nous avons la relation :
   $$ f(x) = \lambda x $$
2. Soit $y \in E_\mu$. De même, nous avons :
   $$ f(y) = \mu y $$
3. Évaluons le produit scalaire $\langle f(x), y \rangle$. En remplaçant $f(x)$ par son expression :
   $$ \langle f(x), y \rangle = \langle \lambda x, y \rangle $$
4. Par linéarité à gauche du produit scalaire réel, nous pouvons extraire le scalaire $\lambda$ :
   $$ \langle f(x), y \rangle = \lambda \langle x, y \rangle \quad \text{(Équation 1)} $$
5. D'autre part, comme $f$ est un endomorphisme symétrique, nous pouvons transférer l'opérateur $f$ sur le deuxième argument :
   $$ \langle f(x), y \rangle = \langle x, f(y) \rangle $$
6. En remplaçant $f(y)$ par $\mu y$ :
   $$ \langle f(x), y \rangle = \langle x, \mu y \rangle $$
7. Par linéarité à droite (ou symétrie) du produit scalaire euclidien :
   $$ \langle f(x), y \rangle = \mu \langle x, y \rangle \quad \text{(Équation 2)} $$
8. En égalant l'Équation 1 et l'Équation 2, nous obtenons :
   $$ \lambda \langle x, y \rangle = \mu \langle x, y \rangle $$
9. En soustrayant $\mu \langle x, y \rangle$ de chaque côté et en factorisant par $\langle x, y \rangle$ :
   $$ (\lambda - \mu) \langle x, y \rangle = 0 $$
10. Par hypothèse, $\lambda \neq \mu$, ce qui implique que $\lambda - \mu \neq 0$.
11. Puisque le produit de deux réels est nul et que le premier est non nul, il en résulte nécessairement que le second est nul :
    $$ \langle x, y \rangle = 0 $$
12. Les vecteurs $x$ et $y$ sont donc orthogonaux. Les sous-espaces $E_\lambda$ et $E_\mu$ sont complètement orthogonaux. $\blacksquare$

### Théorème Spectral en dimension finie
Tout endomorphisme symétrique d'un espace euclidien $E$ possède une base de vecteurs propres qui est orthonormée. De manière équivalente, toute matrice symétrique réelle est diagonalisable dans une base orthonormée (il existe $P$ orthogonale telle que $P^T A P$ soit diagonale).

## 4. Exercices d'Application
*(Les exercices complets sont disponibles dans le dossier `exos/`, numérotés de 01 à 10, avec des démonstrations exhaustives sans la moindre ellipse mathématique).*

## 5. Travaux Pratiques en Python pur
*(Les implémentations formelles des algorithmes en Python depuis zéro, sans aucun framework, se trouvent dans le dossier `tp/`).*

## 6. Liens Obsidian
- [[Jalon-26.md]]
- [[Jalon-28.md]]
