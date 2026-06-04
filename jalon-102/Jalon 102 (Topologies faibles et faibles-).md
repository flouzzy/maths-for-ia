---
uuid: "jalon-102"
title: "Topologies faibles et faibles-*"
year: 3
trimester: 9
tags:
  - math/topologie
  - ia/abstraction
prev: "[[Jalon 101 (Application ouverte et Graphe fermé).md]]"
next: "[[Jalon 103 (Espaces de Hilbert généraux).md]]"
---

# Jalon 102 : Topologies faibles et faibles-*

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous regardiez une hélice d'avion qui tourne de plus en plus vite.
    - Si vous mesurez la vitesse de chaque point, elle est énorme et ne s'arrête jamais (pas de convergence classique).
    - Mais si vous regardez l'hélice avec vos yeux (qui sont des capteurs lents), vous finissez par voir un disque gris immobile et transparent.
    - La **Topologie Faible**, c'est exactement cela : c'est la vue que l'on a d'un objet quand on ne peut le regarder qu'à travers des instruments de mesure (des formes linéaires). Un objet peut sembler "immobile" ou "convergent" pour tous vos instruments, même s'il s'agite frénétiquement dans l'espace réel.
- **Le "Pourquoi on a inventé ça" :** En dimension infinie, les boules ne sont jamais compactes (Théorème de Riesz). On ne peut donc pas extraire de sous-suite convergente d'une suite bornée, ce qui bloque tous les calculs d'optimisation. La topologie faible "assouplit" l'espace pour rendre les boules à nouveau compactes. C'est le prix à payer pour garantir que nos algorithmes trouvent toujours un point d'arrêt.
- **Visualisation :** Une suite de fonctions $f_n$ qui font des vagues de plus en plus serrées. Elles ne s'écrasent pas au sol, mais leur aire moyenne vue par n'importe quel "filtre" tend vers zéro.

## 2. Formalisation & Rigueur Académique

### A. Topologie Faible $\sigma(E, E^*)$

Soit $E$ un espace de Banach.

> **Définition 1 (Convergence Faible) :**
> On dit qu'une suite $(x_n)$ de $E$ converge **faiblement** vers $x$, noté $x_n \rightharpoonup x$, si pour toute forme linéaire continue $L \in E^*$ :
> $$\lim_{n \to \infty} L(x_n) = L(x)$$
> La topologie faible est la topologie la moins fine sur $E$ rendant continues toutes les formes de $E^*$.

### B. Topologie Faible-* $\sigma(E^*, E)$

Sur l'espace dual $E^*$, on peut définir une topologie encore plus "grossière".

> **Définition 2 (Convergence Faible-*) :**
> On dit qu'une suite $(L_n)$ de $E^*$ converge **faiblement-*** vers $L$, si pour tout vecteur $x \in E$ :
> $$\lim_{n \to \infty} L_n(x) = L(x)$$

### C. Théorème de Banach-Alaoglu

C'est le résultat central qui justifie l'existence de ces topologies.

> **Théorème de Banach-Alaoglu :**
> La boule unité fermée de l'espace dual $E^*$ est **compacte** pour la topologie faible-*.
> $$B_{E^*} = \{ L \in E^* \mid \|L\| \le 1 \} \text{ est } \sigma(E^*, E)\text{-compacte.}$$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Convergence faible $\neq$ Convergence forte dans $L^2$

Considérons $e_n(x) = \sin(nx)$ sur $[0, \pi]$ dans l'espace $L^2$.

1. **Calcul de la norme :** $\|e_n\|_2^2 = \int_0^\pi \sin^2(nx) dx = \pi/2$. La norme est constante, donc $e_n$ ne converge pas vers 0 au sens fort (sinon sa norme tendrait vers 0).
2. **Action d'une forme linéaire :** Toute forme linéaire sur $L^2$ est de la forme $L(f) = \int f \cdot g$ avec $g \in L^2$ (Riesz, Jalon 76).
3. **Lemme de Riemann-Lebesgue :** On a vu au Jalon 80 que pour toute fonction $g \in L^1$ (et donc $L^2$ sur un segment) :
   $$\lim_{n \to \infty} \int_0^\pi g(x) \sin(nx) dx = 0$$
4. **Conclusion :** Pour tout instrument de mesure $g$, on lit 0 à la limite. Donc $e_n \rightharpoonup 0$ (convergence faible).
   Le signal "vibre" si vite qu'il devient invisible pour tout intégrateur.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Unicité de la limite faible
**Énoncé :** Montrer que si une suite converge faiblement, sa limite est unique.
**Correction Détaillée :**
Si $x_n \rightharpoonup x$ et $x_n \rightharpoonup y$, alors pour tout $L \in E^*$, $L(x_n) \to L(x)$ et $L(x_n) \to L(y)$. Par unicité de la limite dans $\mathbb{K}$, $L(x) = L(y)$, donc $L(x-y) = 0$.
Si c'est vrai pour TOUTE forme linéaire $L$, alors par le corollaire de Hahn-Banach (Jalon 98), $x-y$ doit être nul. Donc $x=y$.

### Exercice 2 : Niveau Avancé (Lien avec la bornitude)
**Énoncé :** Montrer que toute suite faiblement convergente est bornée.
**Correction Détaillée :**
C'est une application élégante du **Théorème de Banach-Steinhaus** (Jalon 100). On voit chaque $x_n$ comme une forme linéaire sur $E^*$ définie par $J(x_n)(L) = L(x_n)$. Par hypothèse, pour chaque $L$, la suite $J(x_n)(L)$ est convergente donc bornée. Par Banach-Steinhaus, la famille d'opérateurs $\{J(x_n)\}$ est bornée en norme. Comme $\|J(x_n)\| = \|x_n\|$, la suite est bornée.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** En optimisation de grande dimension, la compacité faible est ce qui garantit qu'une suite de modèles dont l'erreur diminue finit par "converger" vers un modèle limite, même si les paramètres eux-mêmes bougent beaucoup.
- **Example Concret :**
    - **Apprentissage de Mesures (GANS) :** Dans la théorie des GANs, on cherche une mesure de probabilité. L'espace des mesures est le dual de l'espace des fonctions continues. Le théorème de Banach-Alaoglu garantit que l'ensemble des probabilités est compact pour la topologie faible-*. C'est ce qui permet de prouver qu'un équilibre de Nash existe entre le générateur et le discriminateur.
    - **Generalization Bounds :** On utilise la topologie faible pour montrer que de petites perturbations des données entraînent de petites perturbations des prédictions "en moyenne", assurant la stabilité statistique du modèle.
    - **Neural Tangent Kernel (NTK) :** L'étude de la convergence des réseaux larges repose sur la convergence faible des opérateurs associés aux couches du réseau.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 101 (Application ouverte et Graphe fermé).md]], [[Jalon 98 (Théorème de Hahn-Banach (forme analytique)).md]], [[Jalon 80 (Transformée de Fourier dans L1).md]]
- **Concepts Futurs dépendants :** [[Jalon 103 (Espaces de Hilbert généraux).md]], [[Jalon 106 (Théorème spectral pour les opérateurs compacts autoadjoints).md]]
