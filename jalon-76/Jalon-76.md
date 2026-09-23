---
uuid: "jalon-76"
title: "Propriétés géométriques de l'espace de Hilbert L2"
year: 2
trimester: 7
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 75 (Preuve de la complétude des espaces Lp).md]]"
next: "[[Jalon 77 (Densité des fonctions simples).md]]"
---

# Jalon 76 : Propriétés géométriques de l'espace de Hilbert $L^2$

## Présentation du concept clé

    - L'espace **$L^2$** est le seul sac de fonctions qui se comporte exactement comme notre espace 3D habituel.
    - On peut y dire que deux fonctions sont "perpendiculaires" (**orthogonales**). Par exemple, une note de musique Grave et une note Aiguë sont orthogonales : elles ne se mélangent pas, elles sont indépendantes.
    - On peut y utiliser le **Théorème de Pythagore** : l'énergie totale de deux sons orthogonaux joués ensemble est la somme des énergies de chaque son.

## Formalisation

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### Le Produit Scalaire dans $L^2$

> **Définition 1 (Produit Scalaire) :**
> Pour deux fonctions $f, g \in L^2(\mu)$ à valeurs complexes, on définit :
> $$\langle f, g \rangle = \int_X f(x) \overline{g(x)} d\mu(x)$$
> C'est une forme hermitienne positive dont la norme associée est la norme $L^2$ : $\|f\|_2 = \sqrt{\langle f, f \rangle}$.

**Exemple Concret (Produit scalaire usuel sur $[a,b]$) :**
Prenons l'espace $L^2([0,1])$ muni de la mesure de Lebesgue.
Soient $f(x) = x$ et $g(x) = x^2$. Ces deux fonctions sont de carré intégrable.
Calculons pas à pas leur produit scalaire :
$$ \langle f, g \rangle = \int_0^1 f(x) \overline{g(x)} dx = \int_0^1 x \cdot x^2 dx = \int_0^1 x^3 dx $$
$$ = \left[ \frac{x^4}{4} \right]_0^1 = \frac{1}{4} - 0 = \frac{1}{4} $$
Le produit scalaire est bien défini et vaut $\frac{1}{4}$.

> **Définition 2 (Espace de Hilbert) :**
> Un espace vectoriel muni d'un produit scalaire qui est complet pour la norme associée est appelé un **Espace de Hilbert**. $L^2(\mu)$ est l'exemple type.

### Identités Géométriques

> **Théorème (Identité du parallélogramme) :**
> Dans tout espace muni d'un produit scalaire :
> $$\|f+g\|^2 + \|f-g\|^2 = 2(\|f\|^2 + \|g\|^2)$$
> *Réciproque :* Si une norme vérifie cette identité, alors elle provient d'un produit scalaire (Théorème de Fréchet-von Neumann-Jordan).

> **Théorème de Pythagore :**
> $f \perp g \iff \langle f, g \rangle = 0 \implies \|f+g\|^2 = \|f\|^2 + \|g\|^2$.

**Exemple Concret (Vecteurs orthogonaux et Pythagore) :**
Dans $L^2([-1,1])$, considérons les fonctions paires et impaires. Soit $f(x) = 1$ et $g(x) = x$.
Vérifions leur orthogonalité :
$$ \langle f, g \rangle = \int_{-1}^1 1 \cdot x dx = \left[ \frac{x^2}{2} \right]_{-1}^1 = \frac{1}{2} - \frac{1}{2} = 0 $$
Ainsi $f \perp g$. Calculons les normes au carré :
$\|f\|^2 = \int_{-1}^1 1^2 dx = 2$.
$\|g\|^2 = \int_{-1}^1 x^2 dx = \left[ \frac{x^3}{3} \right]_{-1}^1 = \frac{2}{3}$.
$\|f+g\|^2 = \int_{-1}^1 (1+x)^2 dx = \int_{-1}^1 (1 + 2x + x^2) dx = 2 + 0 + \frac{2}{3} = \frac{8}{3}$.
On observe bien que $\|f+g\|^2 = \|f\|^2 + \|g\|^2 = 2 + \frac{2}{3} = \frac{8}{3}$. L'égalité de Pythagore est parfaitement vérifiée.

## Démonstrations

### Démonstration de l'identité du parallélogramme

1. **Développement du premier terme :**
   $\|f+g\|^2 = \langle f+g, f+g \rangle = \langle f, f \rangle + \langle f, g \rangle + \langle g, f \rangle + \langle g, g \rangle$.
   $\|f+g\|^2 = \|f\|^2 + \|g\|^2 + \langle f, g \rangle + \langle g, f \rangle$.
2. **Développement du second terme :**
   $\|f-g\|^2 = \langle f-g, f-g \rangle = \langle f, f \rangle - \langle f, g \rangle - \langle g, f \rangle + \langle g, g \rangle$.
   $\|f-g\|^2 = \|f\|^2 + \|g\|^2 - \langle f, g \rangle - \langle g, f \rangle$.
3. **Somme des deux :**
   En additionnant les deux lignes, les termes croisés $\langle f, g \rangle$ et $\langle g, f \rangle$ s'annulent exactement.
4. **Conclusion :**
   $\|f+g\|^2 + \|f-g\|^2 = 2\|f\|^2 + 2\|g\|^2$.

### Théorème de Projection sur un convexe fermé

C'est la propriété géométrique la plus puissante. Dans un Hilbert $H$, pour tout point $x$ et tout sous-espace fermé $M$, il existe un unique point $p \in M$ tel que $\|x-p\|$ soit minimal. Ce point est caractérisé par $\langle x-p, m \rangle = 0$ pour tout $m \in M$.

## Application en Intelligence Artificielle

- Le Pont Théorique : Le Machine Learning "classique" (linéaire) n'est rien d'autre que de la géométrie dans un espace de Hilbert.
- **Example Concret :**
    - **Régression Linéaire (MSE) :** Chercher les poids $w$ qui minimisent $\sum (y_i - w^T x_i)^2$, c'est exactement projeter le vecteur des étiquettes $y$ sur le sous-espace engendré par les données $x$. La solution (équations normales) est la caractérisation de la projection orthogonale.
    - **Kernel Trick (RKHS) :** Dans les SVM, on envoie les données dans un espace de dimension infinie où le produit scalaire est facile à calculer (le noyau). Cet espace est un espace de Hilbert. On y fait de la géométrie simple (séparation par un plan) pour résoudre des problèmes complexes.
    - **Analyse en Composantes Principales (PCA) :** On cherche les directions (vecteurs propres) qui capturent le maximum d'énergie (norme $L^2$) des données. C'est une décomposition orthogonale dans un espace de Hilbert.

## Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 75 (Preuve de la complétude des espaces Lp).md]], [[Jalon 26 (Espaces euclidiens).md]]
- **Concepts Futurs dépendants :** [[Jalon 103 (Espaces de Hilbert généraux).md]], [[Jalon 126 (Noyaux définis positifs).md]]
