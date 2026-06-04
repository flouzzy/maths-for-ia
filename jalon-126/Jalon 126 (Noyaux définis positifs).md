---
uuid: "jalon-126"
title: "Noyaux définis positifs et RKHS"
year: 3
trimester: 11
tags:
  - math/analyse
  - ia/fondations
prev: "[[Jalon 125 (Opérateurs proximaux).md]]"
next: "[[Jalon 127 (Démonstration du théorème du représentant dans les RKHS).md]]"
---

# Jalon 126 : Noyaux définis positifs et RKHS

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez que vous ayez deux objets très complexes, comme deux nuages ou deux chansons. Vous voulez savoir s'ils se ressemblent.
    - Une manière de faire est de les transformer en une liste de millions de caractéristiques (la taille, la couleur, les pics de fréquence) et de faire un produit scalaire. C'est très long.
    - Le **Noyau (Kernel)**, c'est un raccourci magique : c'est une fonction $K(A, B)$ qui vous donne directement le score de ressemblance, comme si vous aviez fait tout le travail de transformation dans une pièce secrète, sans jamais avoir besoin d'entrer dans cette pièce.
    - Un **Noyau Défini Positif**, c'est un noyau qui est "honnête" : il garantit que le score qu'il donne correspond bien à une vraie géométrie dans une pièce secrète (l'**RKHS**).
- **Le "Pourquoi on a inventé ça" :** Pour rendre les modèles simples (linéaires) incroyablement puissants. Au lieu de tordre les données pour qu'elles rentrent dans une ligne droite, on change notre manière de mesurer la distance pour que la ligne droite devienne une courbe complexe dans le monde réel.
- **Visualisation :** On projette des points d'une feuille de papier plate sur une montagne courbe (l'espace des caractéristiques). Sur la montagne, on peut séparer les points par un plan droit, alors que sur la feuille, il aurait fallu dessiner une boucle compliquée.

## 2. Formalisation & Rigueur Académique

Soit $\mathcal{X}$ un ensemble (l'espace des entrées).

### A. Noyaux Définis Positifs

> **Définition 1 (Noyau Défini Positif) :**
> Une application $K : \mathcal{X} \times \mathcal{X} \to \mathbb{R}$ est un **noyau défini positif** si elle est symétrique ($K(x, y) = K(y, x)$) et si pour tout $n \in \mathbb{N}^*$, pour tous $x_1, \dots, x_n \in \mathcal{X}$ and $c_1, \dots, x_n \in \mathbb{R}$ :
> $$\sum_{i=1}^n \sum_{j=1}^n c_i c_j K(x_i, x_j) \ge 0$$
> Cela signifie que la matrice de Gram $\mathbf{K}$ associée est semi-définie positive.

### B. Espaces de Hilbert à Noyau Reproduisant (RKHS)

> **Définition 2 (RKHS) :**
> Un espace de Hilbert $H$ de fonctions de $\mathcal{X}$ dans $\mathbb{R}$ est un **RKHS** si pour tout $x \in \mathcal{X}$, l'application d'évaluation $L_x : f \mapsto f(x)$ est une forme linéaire continue sur $H$.

> **Théorème de Moore-Aronszajn :**
> À tout noyau défini positif $K$ est associé un unique RKHS $H$ tel que :
> 1. $\forall x \in \mathcal{X}, \quad K(x, \cdot) \in H$.
> 2. **Propriété de Reproduction :** $\forall x \in \mathcal{X}, \forall f \in H, \quad f(x) = \langle f, K(x, \cdot) \rangle_H$.
> En particulier, $K(x, y) = \langle K(x, \cdot), K(y, \cdot) \rangle_H$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : La propriété de reproduction implique que K est PD

Supposons qu'il existe un Hilbert $H$ et une application $\phi : \mathcal{X} \to H$ telle que $K(x, y) = \langle \phi(x), \phi(y) \rangle_H$.

1. **Symétrie :** $K(x, y) = \langle \phi(x), \phi(y) \rangle = \langle \phi(y), \phi(x) \rangle = K(y, x)$. (Vrai pour un Hilbert réel).
2. **Positivité de la forme quadratique :** Soient $c_1, \dots, c_n \in \mathbb{R}$ et $x_1, \dots, x_n \in \mathcal{X}$.
   $$\sum_{i,j} c_i c_j K(x_i, x_j) = \sum_{i,j} c_i c_j \langle \phi(x_i), \phi(x_j) \rangle_H$$
3. **Utilisation de la linéarité du produit scalaire :**
   $$\sum_{i,j} \langle c_i \phi(x_i), c_j \phi(x_j) \rangle_H = \left\langle \sum_{i} c_i \phi(x_i), \sum_{j} c_j \phi(x_j) \right\rangle_H$$
4. **Propriété de la norme :**
   Le terme de droite est exactement $\|\sum_{i=1}^n c_i \phi(x_i)\|_H^2$.
5. **Conclusion :** Une norme au carré est toujours $\ge 0$.
   Donc $\sum_{i,j} c_i c_j K(x_i, x_j) \ge 0$. Le noyau est défini positif.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Le noyau Gaussien (RBF)
**Énoncé :** Pourquoi le noyau $K(x, y) = \exp(-\|x-y\|^2)$ est-il défini positif ?
**Correction Détaillée :**
1. On sait que le noyau produit $K_1 K_2$ de deux noyaux PD est PD.
2. On développe le carré : $\|x-y\|^2 = \|x\|^2 + \|y\|^2 - 2x^T y$.
3. $K(x, y) = e^{-\|x\|^2} e^{-\|y\|^2} e^{2x^T y}$.
4. $e^{-\|x\|^2} e^{-\|y\|^2}$ est un noyau PD (de la forme $f(x)f(y)$).
5. $e^{2x^T y}$ est la limite d'une série de puissances de $x^T y$. Comme le noyau linéaire $x^T y$ est PD et que les sommes/produits/limites de noyaux PD sont PD, alors $e^{2x^T y}$ est PD.
**Résultat :** Le noyau RBF est PD. Son espace de caractéristiques associé est de dimension **infinie**.

### Exercice 2 : Niveau Avancé (Noyau de Sobolev)
**Énoncé :** Soit $H = H^1([0, 1])$. Le noyau $K(x, y) = 1 + \min(x, y)$ est-il un noyau reproduisant ?
**Correction Détaillée :**
Oui, c'est le noyau associé au produit scalaire $\langle f, g \rangle = f(0)g(0) + \int f' g'$. On vérifie par IPP que $\langle f, 1 + \min(x, \cdot) \rangle = f(x)$.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Le **Kernel Trick** permet d'utiliser des algorithmes linéaires (comme la régression ou les SVM) dans des espaces de caractéristiques de dimension infinie sans jamais en payer le prix computationnel.
- **Example Concret :**
    - **Support Vector Machines (SVM) :** Au lieu de chercher un plan séparateur dans l'espace des pixels, on le cherche dans l'RKHS. Le noyau RBF permet de séparer n'importe quel ensemble de points, car en dimension infinie, il y a toujours "assez de place" pour glisser un hyperplan entre les classes.
    - **Gaussian Processes (GP) :** La fonction de covariance d'un processus gaussien est un noyau défini positif. L'RKHS associé définit l'espace des fonctions "probables" pour le modèle.
    - **Neural Tangent Kernel (NTK) :** On a découvert que les réseaux de neurones très larges se comportent comme des modèles à noyaux. Le noyau (NTK) est défini par l'architecture du réseau et détermine la vitesse d'apprentissage de chaque composante du signal.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 103 (Espaces de Hilbert généraux).md]], [[Jalon 76 (Propriétés géométriques de l'espace de Hilbert L2).md]]
- **Concepts Futurs dépendants :** [[Jalon 127 (Démonstration du théorème du représentant dans les RKHS).md]], [[Jalon 143 (Théorie spectrale des graphes).md]]
