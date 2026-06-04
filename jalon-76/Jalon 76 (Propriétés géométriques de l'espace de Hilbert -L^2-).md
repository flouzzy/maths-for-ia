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

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous soyez dans un simulateur de vol. Votre avion (une fonction $f$) peut se déplacer dans une infinité de directions. Même si cet espace est "infini", vous aimeriez pouvoir utiliser votre boussole et votre règle comme dans le monde réel.
    - L'espace **$L^2$** est le seul sac de fonctions qui se comporte exactement comme notre espace 3D habituel.
    - On peut y dire que deux fonctions sont "perpendiculaires" (**orthogonales**). Par exemple, une note de musique Grave et une note Aiguë sont orthogonales : elles ne se mélangent pas, elles sont indépendantes.
    - On peut y utiliser le **Théorème de Pythagore** : l'énergie totale de deux sons orthogonaux joués ensemble est la somme des énergies de chaque son.
- **Le "Pourquoi on a inventé ça" :** La plupart des outils de l'ingénieur (Fourier, ondelettes, filtrage) reposent sur l'idée de "projeter" un signal compliqué sur des briques de base simples. Pour faire une projection propre (trouver le chemin le plus court), on a besoin d'un produit scalaire. $L^2$ est le cadre naturel pour cela.
- **Visualisation :** Un cercle dans un plan. Dans $L^2$, la "sphère unité" est parfaitement ronde, contrairement aux autres espaces $L^p$ qui peuvent être pointus (L1) ou carrés (L-infini).

## 2. Formalisation & Rigueur Académique

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### A. Le Produit Scalaire dans $L^2$

> **Définition 1 (Produit Scalaire) :**
> Pour deux fonctions $f, g \in L^2(\mu)$ à valeurs complexes, on définit :
> $$\langle f, g \rangle = \int_X f(x) \overline{g(x)} d\mu(x)$$
> C'est une forme hermitienne positive dont la norme associée est la norme $L^2$ : $\|f\|_2 = \sqrt{\langle f, f \rangle}$.

> **Définition 2 (Espace de Hilbert) :**
> Un espace vectoriel muni d'un produit scalaire qui est complet pour la norme associée est appelé un **Espace de Hilbert**. $L^2(\mu)$ est l'exemple type.

### B. Identités Géométriques

> **Théorème (Identité du parallélogramme) :**
> Dans tout espace muni d'un produit scalaire :
> $$\|f+g\|^2 + \|f-g\|^2 = 2(\|f\|^2 + \|g\|^2)$$
> *Réciproque :* Si une norme vérifie cette identité, alors elle provient d'un produit scalaire (Théorème de Fréchet-von Neumann-Jordan).

> **Théorème de Pythagore :**
> $f \perp g \iff \langle f, g \rangle = 0 \implies \|f+g\|^2 = \|f\|^2 + \|g\|^2$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

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

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Orthogonalité de fonctions sinus/cosinus
**Énoncé :** Sur $[0, 2\pi]$, montrer que $f(x) = \sin(x)$ et $g(x) = \cos(x)$ sont orthogonales dans $L^2$.
**Correction Détaillée :**
$\langle f, g \rangle = \int_0^{2\pi} \sin(x) \cos(x) dx$.
On utilise l'identité $\sin(2x) = 2 \sin(x) \cos(x)$.
$\langle f, g \rangle = \frac{1}{2} \int_0^{2\pi} \sin(2x) dx = \frac{1}{2} [ -\frac{1}{2} \cos(2x) ]_0^{2\pi} = -\frac{1}{4} (1 - 1) = 0$.
Les deux fonctions sont orthogonales. C'est la base des séries de Fourier.

### Exercice 2 : Niveau Avancé (Inégalité de Bessel)
**Énoncé :** Soit $(e_n)$ une famille orthonormée. Montrer que pour tout $f$, $\sum |\langle f, e_n \rangle|^2 \le \|f\|^2$.
**Correction Détaillée :**
On considère la projection $p_N$ sur l'espace engendré par les $N$ premiers vecteurs. Par Pythagore, $\|f\|^2 = \|p_N\|^2 + \|f-p_N\|^2 \ge \|p_N\|^2$. Or $\|p_N\|^2 = \sum_{n=1}^N |\langle f, e_n \rangle|^2$. En faisant tendre $N \to \infty$, on obtient l'inégalité de Bessel.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Le Machine Learning "classique" (linéaire) n'est rien d'autre que de la géométrie dans un espace de Hilbert.
- **Example Concret :**
    - **Régression Linéaire (MSE) :** Chercher les poids $w$ qui minimisent $\sum (y_i - w^T x_i)^2$, c'est exactement projeter le vecteur des étiquettes $y$ sur le sous-espace engendré par les données $x$. La solution (équations normales) est la caractérisation de la projection orthogonale.
    - **Kernel Trick (RKHS) :** Dans les SVM, on envoie les données dans un espace de dimension infinie où le produit scalaire est facile à calculer (le noyau). Cet espace est un espace de Hilbert. On y fait de la géométrie simple (séparation par un plan) pour résoudre des problèmes complexes.
    - **Analyse en Composantes Principales (PCA) :** On cherche les directions (vecteurs propres) qui capturent le maximum d'énergie (norme $L^2$) des données. C'est une décomposition orthogonale dans un espace de Hilbert.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 75 (Preuve de la complétude des espaces Lp).md]], [[Jalon 26 (Espaces euclidiens).md]]
- **Concepts Futurs dépendants :** [[Jalon 103 (Espaces de Hilbert généraux).md]], [[Jalon 126 (Noyaux définis positifs).md]]
