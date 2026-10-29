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

- **Intuition Physique :** Imaginez que vous regardiez une hélice d'avion qui tourne de plus en plus vite.
    - Si vous mesurez la vitesse de chaque point, elle est énorme et ne s'arrête jamais (pas de convergence classique).
    - Mais si vous regardez l'hélice avec vos yeux (qui sont des capteurs lents), vous finissez par voir un disque gris immobile et transparent.
    - La **Topologie Faible**, c'est exactement cela : c'est la vue que l'on a d'un objet quand on ne peut le regarder qu'à travers des instruments de mesure (des formes linéaires). Un objet peut sembler "immobile" ou "convergent" pour tous vos instruments, même s'il s'agite frénétiquement dans l'espace réel.
- **Problématique Historique :** En dimension infinie, les boules ne sont jamais compactes (Théorème de Riesz). On ne peut donc pas extraire de sous-suite convergente d'une suite bornée, ce qui bloque tous les calculs d'optimisation. La topologie faible "assouplit" l'espace pour rendre les boules à nouveau compactes. C'est le prix à payer pour garantir que nos algorithmes trouvent toujours un point d'arrêt.
- **Perspective Géométrique :** Une suite de fonctions $f_n$ qui font des vagues de plus en plus serrées. Elles ne s'écrasent pas au sol, mais leur aire moyenne vue par n'importe quel "filtre" tend vers zéro.

## 2. Formalisation

### A. Topologie Faible $\sigma(E, E^*)$

Soit $E$ un espace de Banach.

> **Définition 1 (Convergence Faible) :**
> On dit qu'une suite $(x_n)$ de $E$ converge **faiblement** vers $x$, noté $x_n \rightharpoonup x$, si pour toute forme linéaire continue $L \in E^*$ :
> $$\lim_{n \to \infty} L(x_n) = L(x)$$
> La topologie faible est la topologie la moins fine sur $E$ rendant continues toutes les formes de $E^*$.

> **Exemple Concret :**
> Soit $E = \ell^2(\mathbb{N})$, l'espace des suites de carré sommable, et considérons la base hilbertienne canonique $(e_n)_{n \in \mathbb{N}}$, où $e_n = (0, \dots, 0, 1, 0, \dots)$ avec un $1$ à la $n$-ième position.
> La suite $(e_n)$ ne converge pas fortement (en norme) vers $0$ car $\|e_n - e_m\|_2 = \sqrt{2}$ pour tout $n \neq m$.
> Cependant, d'après le théorème de représentation de Riesz, toute forme linéaire $L \in (\ell^2)^*$ s'écrit $L(x) = \langle y, x \rangle$ pour un certain $y = (y_k) \in \ell^2$.
> Évaluons $L(e_n)$ :
> $$L(e_n) = \langle y, e_n \rangle = y_n$$
> Comme $y \in \ell^2$, la série $\sum |y_k|^2$ converge, ce qui implique que le terme général $y_n$ tend vers $0$.
> Ainsi, pour toute $L \in (\ell^2)^*$, $\lim_{n \to \infty} L(e_n) = 0$.
> La suite $(e_n)$ converge donc faiblement vers $0$ : $e_n \rightharpoonup 0$.


\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Axes
  \draw[->] (-0.5,0) -- (5,0) node[right] {Temps $t$};
  \draw[->] (0,-1.5) -- (0,1.5) node[above] {$f_n(t)$};

  % Functions fn
  \draw[blue, domain=0:4, samples=100] plot (\x, {sin(200*\x)*exp(-0.2*\x)});
  \draw[red, domain=0:4, samples=200] plot (\x, {sin(600*\x)*exp(-0.2*\x)});

  % Convergence (weak limit is 0)
  \draw[thick, dashed] (0,0) -- (4,0);

  \node[blue, right] at (5, 0.5) {$f_{10}$ (fréquence modérée)};
  \node[red, right] at (5, -0.5) {$f_{30}$ (haute fréquence)};

  \node[align=center] at (2,-2.5) {Oscillations rapides : La suite $(f_n)$ n'a pas de limite forte,\\mais son action moyenne (intégrale contre une fonction test)\\tend vers zéro (limite faible $= 0$).};
\end{tikzpicture}
\end{center}


### B. Topologie Faible-* $\sigma(E^*, E)$

Sur l'espace dual $E^*$, on peut définir une topologie encore plus "grossière".

> **Définition 2 (Convergence Faible-*) :**
> On dit qu'une suite $(L_n)$ de $E^*$ converge **faiblement-*** vers $L$, si pour tout vecteur $x \in E$ :
> $$\lim_{n \to \infty} L_n(x) = L(x)$$


> **Exemple Concret 2 : Convergence faible mais pas forte dans $L^p$**
> Considérons l'espace $E = L^p([0, 1])$ pour $1 < p < \infty$, et la suite de fonctions de Rademacher définie par $r_n(t) = \text{sgn}(\sin(2^n \pi t))$.
> Ces fonctions oscillent entre $-1$ et $1$ de plus en plus vite.
> Pour tout $n$, $\|r_n\|_p = 1$. La suite ne converge pas fortement vers $0$.
> Cependant, par le lemme de Riemann-Lebesgue, pour toute fonction test $g \in L^q$ (avec $1/p + 1/q = 1$), on a :
> $$\lim_{n \to \infty} \int_0^1 r_n(t) g(t) dt = 0$$
> Donc $r_n \rightharpoonup 0$ faiblement dans $L^p([0, 1])$.

> **Exemple Concret 3 : Espace non réflexif et topologie faible-***
> Dans l'espace $E = L^1([0, 1])$, le dual est $E^* = L^\infty([0, 1])$.
> Prenons la suite $f_n(t) = n \cdot 1_{[0, 1/n]}(t)$ dans $L^1$.
> Cette suite ne converge pas faiblement dans $L^1$ car il n'existe aucune fonction intégrable qui puisse représenter un "pic de Dirac" en $0$.
> Par contre, si l'on regarde l'espace des mesures de Radon $\mathcal{M}([0,1])$, vu comme le dual de $C^0([0,1])$, les mesures de densité $f_n(t)dt$ convergent faiblement-* vers la mesure de Dirac $\delta_0$.
> En effet, pour toute fonction continue $g \in C^0([0, 1])$ :
> $$\lim_{n \to \infty} \int_0^1 f_n(t) g(t) dt = \lim_{n \to \infty} n \int_0^{1/n} g(t) dt = g(0) = \langle \delta_0, g \rangle$$

> **Exemple Concret 4 : Compacité de la boule unité duale (Banach-Alaoglu)**
> Soit $E = c_0$, l'espace des suites tendant vers 0, muni de la norme $\| \cdot \|_\infty$. Son dual est $E^* = \ell^1$.
> La suite $e_n$ dans $\ell^1$ (où $e_n$ a un 1 à la position $n$ et 0 ailleurs) est dans la boule unité fermée de $\ell^1$.
> D'après le théorème de Banach-Alaoglu, cette boule est faiblement-* compacte.
> Extrayons une sous-suite convergente. Pour toute suite $x \in c_0$, $\langle e_n, x \rangle = x_n$.
> Comme $x \in c_0$, $\lim_{n \to \infty} x_n = 0$.
> Donc $\langle e_n, x \rangle \to 0 = \langle 0, x \rangle$.
> Ainsi, la suite $(e_n)$ converge faiblement-* vers 0 dans $\ell^1$, bien qu'elle ne possède aucune sous-suite faiblement convergente, illustrant la compacité de la topologie faible-*.

> **Exemple Concret 5 : Opérateur de décalage**
> Sur l'espace de Hilbert $E = \ell^2(\mathbb{N})$, considérons l'opérateur de décalage à droite $S(x_0, x_1, \dots) = (0, x_0, x_1, \dots)$ et l'opérateur de décalage à gauche $S^*(x_0, x_1, \dots) = (x_1, x_2, \dots)$.
> Appliquons $S^{*n}$ au vecteur fixe $v = (1, 1/2, 1/3, \dots) \in \ell^2$.
> $S^{*n} v = (1/(n+1), 1/(n+2), \dots)$.
> La norme de $S^{*n} v$ est $\|S^{*n} v\|_2^2 = \sum_{k=n+1}^\infty \frac{1}{k^2}$, qui tend vers 0. Ici on a convergence forte.
> Par contre, appliquons $S^n$ au vecteur $e_0 = (1, 0, 0, \dots)$.
> $S^n e_0 = e_n$. On a vu que $e_n \rightharpoonup 0$ faiblement.
> L'opérateur $S^n$ "pousse" l'énergie vers l'infini, menant à une perte d'information locale, modélisée par la convergence faible.

### C. Théorème de Banach-Alaoglu

C'est le résultat central qui justifie l'existence de ces topologies.

> **Théorème de Banach-Alaoglu :**
> La boule unité fermée de l'espace dual $E^*$ est **compacte** pour la topologie faible-*.
> $$B_{E^*} = \{ L \in E^* \mid \|L\| \le 1 \} \text{ est } \sigma(E^*, E)\text{-compacte.}$$

## 3. Démonstrations

### Démonstration : Convergence faible $\neq$ Convergence forte dans $L^2$

Considérons $e_n(x) = \sin(nx)$ sur $[0, \pi]$ dans l'espace $L^2$.

1. **Calcul de la norme :** $\|e_n\|_2^2 = \int_0^\pi \sin^2(nx) dx = \pi/2$. La norme est constante, donc $e_n$ ne converge pas vers 0 au sens fort (sinon sa norme tendrait vers 0).
2. **Action d'une forme linéaire :** Toute forme linéaire sur $L^2$ est de la forme $L(f) = \int f \cdot g$ avec $g \in L^2$ (Riesz, Jalon 76).
3. **Lemme de Riemann-Lebesgue :** On a vu au Jalon 80 que pour toute fonction $g \in L^1$ (et donc $L^2$ sur un segment) :
   $$\lim_{n \to \infty} \int_0^\pi g(x) \sin(nx) dx = 0$$
4. **Conclusion :** Pour tout instrument de mesure $g$, on lit 0 à la limite. Donc $e_n \rightharpoonup 0$ (convergence faible).
   Le signal "vibre" si vite qu'il devient invisible pour tout intégrateur.

## 4. Exercices d'Application

### Exercice 1 : Unicité de la limite faible
**Énoncé :** Montrer que si une suite converge faiblement, sa limite est unique.
**Correction Détaillée :**
Si $x_n \rightharpoonup x$ et $x_n \rightharpoonup y$, alors pour tout $L \in E^*$, $L(x_n) \to L(x)$ et $L(x_n) \to L(y)$. Par unicité de la limite dans $\mathbb{K}$, $L(x) = L(y)$, donc $L(x-y) = 0$.
Si c'est vrai pour TOUTE forme linéaire $L$, alors par le corollaire de Hahn-Banach (Jalon 98), $x-y$ doit être nul. Donc $x=y$.

### Exercice 2 : Niveau Avancé (Lien avec la bornitude)
**Énoncé :** Montrer que toute suite faiblement convergente est bornée.
**Correction Détaillée :**
C'est une application élégante du **Théorème de Banach-Steinhaus** (Jalon 100). On voit chaque $x_n$ comme une forme linéaire sur $E^*$ définie par $J(x_n)(L) = L(x_n)$. Par hypothèse, pour chaque $L$, la suite $J(x_n)(L)$ est convergente donc bornée. Par Banach-Steinhaus, la famille d'opérateurs $\{J(x_n)\}$ est bornée en norme. Comme $\|J(x_n)\| = \|x_n\|$, la suite est bornée.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** En optimisation de grande dimension, la compacité faible est ce qui garantit qu'une suite de modèles dont l'erreur diminue finit par "converger" vers un modèle limite, même si les paramètres eux-mêmes bougent beaucoup.
- **Example Concret :**
    - **Apprentissage de Mesures (GANS) :** Dans la théorie des GANs, on cherche une mesure de probabilité. L'espace des mesures est le dual de l'espace des fonctions continues. Le théorème de Banach-Alaoglu garantit que l'ensemble des probabilités est compact pour la topologie faible-*. C'est ce qui permet de prouver qu'un équilibre de Nash existe entre le générateur et le discriminateur.
    - **Generalization Bounds :** On utilise la topologie faible pour montrer que de petites perturbations des données entraînent de petites perturbations des prédictions "en moyenne", assurant la stabilité statistique du modèle.
    - **Neural Tangent Kernel (NTK) :** L'étude de la convergence des réseaux larges repose sur la convergence faible des opérateurs associés aux couches du réseau.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 101 (Application ouverte et Graphe fermé).md]], [[Jalon 98 (Théorème de Hahn-Banach (forme analytique)).md]], [[Jalon 80 (Transformée de Fourier dans L1).md]]
- **Concepts Futurs dépendants :** [[Jalon 103 (Espaces de Hilbert généraux).md]], [[Jalon 106 (Théorème spectral pour les opérateurs compacts autoadjoints).md]]
