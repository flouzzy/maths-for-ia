---
uuid: "jalon-104"
title: "Bases hilbertiennes"
year: 3
trimester: 9
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 103 (Espaces de Hilbert généraux).md]]"
next: "[[Jalon 105 (Opérateurs adjoints).md]]"
---

# Jalon 104 : Bases hilbertiennes

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous soyez un peintre et que vous ayez une infinité de tubes de peinture, mais chaque tube contient une couleur "pure" qui ne peut pas être fabriquée en mélangeant les autres (elles sont **orthogonales**).
    - Une **Base Hilbertienne**, c'est la collection minimale de tubes de peinture dont vous avez besoin pour pouvoir reproduire n'importe quel tableau du monde (n'importe quelle fonction du Hilbert).
    - Pour reproduire un tableau, il vous suffit de noter la quantité exacte de peinture que vous prenez dans chaque tube (ce sont les **coefficients de Fourier**).
    - Comme l'espace est un Hilbert, vous avez la garantie que si vous suivez la recette, votre copie sera parfaite (convergence dans $L^2$).
- **Le "Pourquoi on a inventé ça" :** Travailler avec des fonctions est difficile. Travailler avec des listes de nombres (des suites) est beaucoup plus simple. Les bases hilbertiennes permettent de transformer n'importe quel espace de Hilbert compliqué (comme $L^2$) en un espace de suites simple (comme $\ell^2$). C'est la numérisation universelle de l'analyse.
- **Visualisation :** Un repère $(x, y, z)$ avec une infinité d'axes, tous à angle droit les uns des autres. Chaque fonction est un point dans ce repère géant.

## 2. Formalisation & Rigueur Académique

Soit $H$ un espace de Hilbert.

### A. Familles Orthonormées

> **Définition 1 :** Une famille $(e_i)_{i \in I}$ d'éléments de $H$ est dite **orthonormée** si :
> $$\forall i, j \in I, \quad \langle e_i, e_j \rangle = \delta_{ij} = \begin{cases} 1 & \text{si } i=j \\ 0 & \text{si } i \neq j \end{cases}$$

### B. Bases Hilbertiennes

> **Définition 2 (Base Hilbertienne) :**
> Une famille orthonormée $(e_n)_{n \in \mathbb{N}}$ est une **base hilbertienne** de $H$ si elle est **totale**, c'est-à-dire que l'espace vectoriel qu'elle engendre est dense dans $H$ ($\overline{\text{vect}(e_n)} = H$).
> Dans ce cas, tout vecteur $x \in H$ s'écrit de manière unique :
> $$x = \sum_{n=0}^\infty \langle x, e_n \rangle e_n$$

### C. Théorèmes de Caractérisation

> **Théorème (Équivalences) :** Soit $(e_n)$ une famille orthonormée. Les points suivants sont équivalents :
> 1. $(e_n)$ est une base hilbertienne.
> 2. Pour tout $x \in H$, si $\forall n, \langle x, e_n \rangle = 0$, alors $x=0$.
> 3. **Identité de Parseval :** $\forall x \in H, \|x\|^2 = \sum_{n=0}^\infty |\langle x, e_n \rangle|^2$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Existence d'une base dans un espace séparable

Un Hilbert est **séparable** s'il contient une partie dénombrable dense.

1. **Choix d'une famille génératrice :** Soit $(x_n)_{n \in \mathbb{N}}$ une famille dénombrable dont l'adhérence est $H$.
2. **Élimination des dépendances :** On retire les $x_n$ qui sont combinaisons linéaires des précédents pour obtenir une famille libre $(v_n)$.
3. **Procédé de Gram-Schmidt :** On construit la famille $(e_n)$ par récurrence :
   - $e_0 = v_0 / \|v_0\|$.
   - $u_{n+1} = v_{n+1} - \sum_{k=0}^n \langle v_{n+1}, e_k \rangle e_k$.
   - $e_{n+1} = u_{n+1} / \|u_{n+1}\|$.
4. **Propriétés de la construction :**
   - Par construction, chaque $e_n$ est orthogonal à tous les précédents et de norme 1.
   - L'espace engendré par $\{e_0, \dots, e_n\}$ est le même que celui engendré par $\{x_0, \dots, x_n\}$.
5. **Conclusion :** Comme l'union des $\text{vect}(x_0, \dots, x_n)$ est dense dans $H$, l'espace engendré par la famille orthonormée $(e_n)$ est dense. C'est donc une base hilbertienne.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Les polynômes de Legendre
**Énoncé :** On considère $H = L^2([-1, 1], \lambda)$. Appliquer Gram-Schmidt à la famille des monômes $(1, x, x^2, \dots)$.
**Correction Détaillée :**
1. $e_0(x) = \frac{1}{\sqrt{2}}$.
2. $u_1(x) = x - \langle x, e_0 \rangle e_0 = x - 0 = x$. $\|u_1\|^2 = \int_{-1}^1 x^2 dx = 2/3$.
   $e_1(x) = \sqrt{\frac{3}{2}} x$.
3. On obtient ainsi une suite de polynômes orthogonaux.
**Utilité :** En IA, on utilise ces polynômes pour faire de la régression polynomiale stable (les monômes classiques sont trop corrélés entre eux numériquement).

### Exercice 2 : Niveau Avancé (Isomorphisme avec $\ell^2$)
**Énoncé :** Montrer que tout espace de Hilbert séparable de dimension infinie est isométrique à $\ell^2(\mathbb{N})$.
**Correction Détaillée :**
Soit $(e_n)$ une base hilbertienne de $H$. On définit $\Phi : H \to \ell^2(\mathbb{N})$ par $\Phi(x) = (\langle x, e_n \rangle)_{n \in \mathbb{N}}$.
Par l'identité de Parseval, $\|\Phi(x)\|_{\ell^2} = \|x\|_H$. $\Phi$ est donc une isométrie linéaire. Comme elle est bijective (on peut reconstruire $x$ à partir des coefficients), c'est un isomorphisme d'espaces de Hilbert.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Les bases hilbertiennes sont la version continue et de dimension infinie de la **SVD** (Jalon 36) et de la **Diagonalisation** (Jalon 32).
- **Example Concret :**
    - **Analyse en Composantes Principales (PCA) :** On cherche une base hilbertienne de l'espace des données telle que les premiers vecteurs de la base capturent le maximum de variance. En dimension infinie (ex: signaux temporels), cela s'appelle la **Décomposition de Karhunen-Loève**.
    - **Compression d'image (Ondelettes) :** Au lieu d'utiliser la base de Fourier (sinus/cosinus), on utilise une base d'ondelettes (Wavelets). Cette base hilbertienne est "localisée", ce qui permet de compresser les détails d'une image de manière beaucoup plus efficace que Fourier.
    - **Représentation de Graphes :** Pour les réseaux de neurones sur graphes (GNN), on utilise la base hilbertienne formée par les vecteurs propres du Laplacien du graphe pour définir des "convolutions spectrales".

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 103 (Espaces de Hilbert généraux).md]], [[Jalon 78 (Séries de Fourier).md]]
- **Concepts Futurs dépendants :** [[Jalon 106 (Théorème spectral pour les opérateurs compacts autoadjoints).md]], [[Jalon 143 (Théorie spectrale des graphes).md]]
