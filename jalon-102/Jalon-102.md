---
uuid: "jalon-102"
title: "Topologies faibles et faibles-*"
year: 3
trimester: 9
tags:
  - math/topologie
  - ia/abstraction
prev: "[[Jalon-101.md]]"
next: "[[Jalon-103.md]]"
---

# Jalon 102 : Topologies faibles et faibles-*

## 1. Introduction géométrique et historique

L'analyse mathématique en dimension infinie se heurte très tôt à un obstacle fondamental : la perte de la compacité locale. Le théorème de Riesz (1912) stipule que la boule unité fermée d'un espace normé n'est compacte que si sa dimension est finie. Ainsi, on ne peut plus extraire de sous-suites convergentes de suites bornées.

Pour pallier ce manque, les mathématiciens ont affaibli la notion de proximité. Au lieu de regarder l'écart absolu en norme, on "observe" l'espace via un ensemble de capteurs : les formes linéaires continues. Une suite converge faiblement si, pour tout capteur, la mesure converge. L'espace se "tasse", regagnant une certaine forme de compacité au prix de limites moins strictes, ce qui est essentiel en calcul des variations et apprentissage automatique.

## 2. Définitions et Théorèmes fondamentaux

### A. Topologie faible $\sigma(E, E^*)$

> **Définition (Convergence faible) :**
> Soit $E$ un espace de Banach. Une suite $(x_n)_{n \in \mathbb{N}}$ de $E$ converge faiblement vers $x \in E$, noté $x_n \rightharpoonup x$, si pour toute forme linéaire $L \in E^*$ :
> $\lim_{n \to \infty} L(x_n) = L(x)$

**Exemple Concret Immédiat :**
Dans $\ell^2$, la base canonique $(e_n)$ est bornée ($\|e_n\|_2 = 1$) mais ne possède aucune sous-suite fortement convergente ($\|e_m - e_n\|_2 = \sqrt{2}$).
Pourtant, pour tout vecteur test $x = (x_k) \in \ell^2$, la forme linéaire associée est $L_x(y) = \langle x, y \rangle$.
On a $L_x(e_n) = x_n$. Or $x \in \ell^2$ implique que la série $\sum x_k^2$ converge, donc $x_n \to 0$.
Ainsi, $L_x(e_n) \to 0 = L_x(0)$. La suite $(e_n)$ converge faiblement vers $0$.

### B. Topologie faible-* $\sigma(E^*, E)$ et Théorème de Banach-Alaoglu

> **Définition (Convergence faible-*) :**
> Une suite $(L_n)$ de $E^*$ converge faiblement-* vers $L$, noté $L_n \rightharpoonup^* L$, si pour tout $x \in E$ :
> $\lim_{n \to \infty} L_n(x) = L(x)$

> **Théorème (Banach-Alaoglu) :**
> La boule unité fermée de $E^*$ est compacte pour la topologie faible-*.

**Exemple Concret Immédiat :**
Considérons $E = L^1([0, 1])$ et son dual $E^* = L^\infty([0, 1])$.
La suite de fonctions $f_n(x) = \sin(2\pi nx)$ vérifie $\|f_n\|_\infty = 1$. Elle ne converge pas fortement.
Cependant, par le lemme de Riemann-Lebesgue, pour tout $g \in L^1$, $\int_0^1 \sin(2\pi nx) g(x) dx \to 0$.
Ainsi, $(f_n)$ converge faiblement-* vers la fonction nulle $0 \in L^\infty$.

## 3. Démonstrations

### Démonstration : Toute suite faiblement convergente est bornée

Soit $x_n \rightharpoonup x$.
On utilise le plongement canonique $J : E \to E^{**}$ défini par $J(x)(L) = L(x)$.
Pour chaque $L \in E^*$, la suite scalaire $J(x_n)(L) = L(x_n)$ converge vers $L(x)$, donc est bornée par une constante $C_L$.
Nous avons donc une famille d'opérateurs $\{J(x_n)\}$ de $E^*$ vers $\mathbb{K}$ simplement bornée.
Par le théorème de Banach-Steinhaus, cette famille est uniformément bornée : il existe $M > 0$ tel que $\|J(x_n)\|_{E^{**}} \le M$.
Comme l'injection canonique préserve la norme, on a $\|x_n\|_E \le M$. La suite est bornée.

## 4. Applications en IA et Physique

- **Optimisation et réseaux de neurones :** La topologie faible garantit l'existence de minimiseurs dans des espaces fonctionnels larges (comme les espaces de noyaux RKHS).
- **Théorie des GANs :** L'espace des probabilités muni de la topologie faible-* est compact, assurant l'existence d'équilibres de Nash.
