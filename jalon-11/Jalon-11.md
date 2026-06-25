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
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** 
  - **Forme linéaire :** Imaginez que vous soyez un inspecteur de qualité. Un vecteur est un objet complexe (un produit avec poids, taille, prix). Une **forme linéaire**, c'est votre test : vous donnez une note unique (un nombre) à cet objet. Si vous testez deux produits ensemble, la note est la somme des notes. C'est un instrument de mesure simple et puissant.
  - **Hyperplan :** C'est la frontière parfaite. En 2D, c'est une ligne qui sépare le plan en deux. En 3D, c'est une feuille de papier infinie qui sépare l'espace. Un hyperplan, c'est l'ensemble de tous les vecteurs qui reçoivent la note "zéro" par votre test.
  - **Dualité :** C'est le monde des instruments de mesure. Si les vecteurs sont les "points", les formes linéaires sont les "regards" portés sur ces points.
- **Le "Pourquoi on a inventé ça" :** Parfois, il est plus facile de décrire un objet par la manière dont il réagit à des tests (le dual) plutôt que par sa structure interne. C'est fondamental pour définir la notion de "perpendiculaire" ou pour séparer des données.
- **Visualisation :** Imaginez une montagne. La hauteur en chaque point est une fonction (peut-être linéaire localement). L'hyperplan, c'est le "niveau de la mer" (altitude 0). L'espace dual, c'est l'ensemble de tous les plans inclinés possibles qui pourraient toucher la montagne.

## 2. Formalisation
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension $n$.
1. **Forme linéaire :** Une application $\phi : E \to \mathbb{K}$ est une forme linéaire si elle est linéaire, c'est-à-dire $\forall x, y \in E, \forall \lambda, \mu \in \mathbb{K}, \phi(\lambda x + \mu y) = \lambda \phi(x) + \mu \phi(y)$.
2. **Espace Dual ($E^*$) :** L'espace vectoriel $\mathcal{L}(E, \mathbb{K})$ de toutes les formes linéaires sur $E$.
3. **Hyperplan :** Un sous-espace vectoriel $H$ de $E$ est un hyperplan s'il existe une forme linéaire non nulle $\phi \in E^*$ telle que $H = \ker \phi$.
4. **Base Duale :** Soit $\mathcal{B} = (e_1, ..., e_n)$ une base de $E$. La base duale $\mathcal{B}^* = (e^*_1, ..., e^*_n)$ est définie par :
   $$e^*_i(e_j) = \delta_{i,j} \quad (\text{symbole de Kronecker})$$
5. **Orthogonalité (au sens de la dualité) :** Soit $A \subseteq E$. On définit l'orthogonal de $A$ dans $E^*$ par $A^\perp = \{ \phi \in E^* \mid \forall x \in A, \phi(x) = 0 \}$.

### B. Théorèmes, Propositions & Lemmes
> **Théorème de la Dimension du Dual :**
> Si $E$ est de dimension finie, alors $\dim E^* = \dim E$.
> De plus, tout hyperplan $H$ de $E$ est de dimension $n-1$.

> **Isomorphisme de Dualité :**
> L'application qui à un vecteur $x$ associe son évaluation $\text{ev}_x : \phi \mapsto \phi(x)$ définit un isomorphisme canonique entre $E$ et son bidual $E^{**}$ (en dimension finie).

## 3. Démonstrations
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Dimension d'un hyperplan
Soit $H$ un hyperplan de $E$ (dimension $n$). Montrons que $\dim H = n-1$.

1. **Initialisation / Cadre :** Par définition d'un hyperplan, il existe une forme linéaire $\phi \in E^*$ telle que $\phi \neq 0$ et $H = \ker \phi$.

2. **Étape 1 : Application du théorème du rang**
   Appliquons le théorème du rang à l'application linéaire $\phi : E \to \mathbb{K}$.
   $$\dim E = \dim(\ker \phi) + \text{rg}(\phi)$$
   On sait que $\ker \phi = H$ et $\text{rg}(\phi) = \dim(\text{Im } \phi)$.

3. **Étape 2 : Détermination de l'Image de $\phi$**
   - $\phi$ est une application de $E$ vers le corps de base $\mathbb{K}$.
   - L'image $\text{Im } \phi$ est donc un sous-espace vectoriel de $\mathbb{K}$.
   - Les seuls sous-espaces vectoriels de $\mathbb{K}$ (qui est un espace vectoriel de dimension 1 sur lui-même) sont $\{0\}$ et $\mathbb{K}$ lui-même.
   - Comme $\phi \neq 0$ par hypothèse, il existe au moins un vecteur $x$ tel que $\phi(x) \neq 0$.
   - Donc $\text{Im } \phi$ contient au moins un élément non nul, ce qui implique $\text{Im } \phi = \mathbb{K}$.

4. **Étape 3 : Calcul final**
   - On a donc $\dim(\text{Im } \phi) = \dim \mathbb{K} = 1$.
   - L'égalité du théorème du rang devient :
     $n = \dim H + 1$.
   - D'où $\dim H = n - 1$.

5. **Conclusion :** Tout hyperplan d'un espace de dimension $n$ possède une dimension égale à $n-1$.



### C. Le Bidual
L'espace bidual $E^{**}$ est l'espace dual de l'espace dual $E^*$.
Pour tout vecteur $x \in E$, on peut définir l'application d'évaluation $\text{ev}_x : E^* \to \mathbb{K}$ par :
$$\forall \phi \in E^*, \quad \text{ev}_x(\phi) = \phi(x)$$
> **Théorème de l'isomorphisme canonique :**
> Si $E$ est de dimension finie, l'application $\Psi : x \mapsto \text{ev}_x$ est un isomorphisme canonique (indépendant du choix d'une base) entre $E$ et $E^{**}$.

### Démonstration de l'isomorphisme canonique $E \cong E^{**}$
1. **Initialisation :** Montrons que l'application $\Psi : x \mapsto \text{ev}_x$ est linéaire et injective.
2. **Linéarité :** Soient $x, y \in E$ et $\lambda, \mu \in \mathbb{K}$. Pour toute $\phi \in E^*$,
   $$\Psi(\lambda x + \mu y)(\phi) = \phi(\lambda x + \mu y)$$
   Par linéarité de $\phi$, on a :
   $$\phi(\lambda x + \mu y) = \lambda \phi(x) + \mu \phi(y) = \lambda \Psi(x)(\phi) + \mu \Psi(y)(\phi)$$
   Donc $\Psi(\lambda x + \mu y) = \lambda \Psi(x) + \mu \Psi(y)$.
3. **Injectivité :** Cherchons le noyau de $\Psi$. Soit $x \in \ker \Psi$. Alors $\Psi(x) = 0_{E^{**}}$, c'est-à-dire que pour toute $\phi \in E^*$, $\phi(x) = 0$.
   Si $x \neq 0$, on peut le compléter en une base $(x, e_2, \dots, e_n)$ de $E$. Considérons la forme coordonnée $e_1^*$ associée à cette base, qui vérifie $e_1^*(x) = 1$. Ceci contredit $\phi(x) = 0$ pour toute forme. Donc $x = 0$, et $\ker \Psi = \{0\}$. $\Psi$ est injective.
4. **Conclusion :** Puisque $\dim E^{**} = \dim E^* = \dim E = n$ (la dimension finie est cruciale), et que $\Psi$ est une application linéaire injective entre deux espaces de même dimension, c'est un isomorphisme.


## 4. Exercices d'Application
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

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

### Exercice 2 : Niveau Avancé (Intersection d'hyperplans)
**Énoncé :** Montrer que l'intersection de deux hyperplans distincts $H_1$ et $H_2$ est un sous-espace de dimension $n-2$.
**Correction Détaillée :**
1. Soient $\phi_1, \phi_2$ les formes linéaires associées telles que $H_1 = \ker \phi_1$ et $H_2 = \ker \phi_2$.
2. Définissons l'application $\Phi : E \to \mathbb{K}^2$ par $\Phi(x) = (\phi_1(x), \phi_2(x))$.
3. Le noyau de $\Phi$ est $\ker \phi_1 \cap \ker \phi_2 = H_1 \cap H_2$.
4. Par le théorème du rang : $\dim E = \dim(H_1 \cap H_2) + \text{rg}(\Phi)$.
5. Comme $H_1$ et $H_2$ sont distincts, $\phi_1$ et $\phi_2$ ne sont pas proportionnelles. La famille $(\phi_1, \phi_2)$ est donc libre dans $E^*$.
6. L'image de $\Phi$ est donc de dimension 2 (surjection sur $\mathbb{K}^2$).
7. $\text{rg}(\Phi) = 2 \implies n = \dim(H_1 \cap H_2) + 2$.
**Conclusion :** $\dim(H_1 \cap H_2) = n - 2$.

## 5. Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** Les hyperplans sont les **Séparateurs Linéaires** fondamentaux de l'apprentissage automatique.
- **Exemple Concret :** Dans les **SVM (Support Vector Machines)**, l'algorithme cherche l'hyperplan optimal qui sépare deux classes de données (ex: Spam vs Non-Spam). L'équation de l'hyperplan $\phi(x) + b = 0$ (où $\phi$ est une forme linéaire) définit la frontière de décision. La **Dualité de Lagrange**, utilisée pour résoudre ce problème d'optimisation, repose entièrement sur le passage de l'espace des données (primal) à l'espace des contraintes (dual).

## 6. Liens Sémantiques
- **Concepts Précédents requis :** [[Jalon-7.md|Jalon 7 (Espaces vectoriels abstraits)]], [[Jalon-8]]
- **Concepts Futurs dépendants :** [[Jalon 12 (Livrable IA)]], [[Jalon 25 (Formes bilinéaires)]], [[Jalon 123 (Problèmes d'optimisation sous contraintes)]]
