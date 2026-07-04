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
