---
uuid: "jalon-115"
title: "Démonstration du théorème de Stokes généralisé"
year: 3
trimester: 10
tags:
  - math/geometrie
  - ia/abstraction
prev: "[[Jalon 114 (Orientation et Intégration sur variétés).md]]"
next: "[[Jalon 116 (Variétés riemanniennes).md]]"
---

# Jalon 115 : Démonstration du théorème de Stokes généralisé

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez que vous comptiez les entrées et les sorties dans un centre commercial.
    - Il y a deux manières de connaître le nombre total de personnes qui sont entrées dans le bâtiment :
        1. Rester à toutes les portes (la **frontière $\partial M$**) et compter chaque personne qui franchit le seuil.
        2. Faire le tour de tous les magasins à l'intérieur (le **volume $M$**) et regarder si les gens bougent d'un rayon à l'autre (la **dérivée extérieure $d\omega$**).
    - Le **Théorème de Stokes** dit que le résultat est identique : le bilan net aux frontières est égal à la somme de tous les petits changements internes. C'est l'outil qui relie le "bord" d'un objet à son "cœur".
- **Le "Pourquoi on a inventé ça" :** C'est la version "grand luxe" du théorème fondamental de l'analyse (celui qui dit que $\int_a^b f' = f(b) - f(a)$). Il permet de transformer des intégrales de volume très compliquées en simples intégrales de surface, ou vice-versa. C'est le pilier de l'électromagnétisme (équations de Maxwell) et de la mécanique des fluides.
- **Visualisation :** Un filet de pêche. La quantité de poissons attrapés par le filet dépend uniquement de ce qui se passe sur le contour (le cercle de métal du filet) et de la force du courant à cet endroit.

## 2. Formalisation & Rigueur Académique

Soit $M$ une variété différentielle de dimension $n$ orientée, compacte, à bord $\partial M$.

### A. Énoncé du Théorème de Stokes

> **Théorème de Stokes :**
> Soit $\omega$ une $(n-1)$-forme différentielle de classe $\mathcal{C}^1$ sur $M$ à support compact. Alors :
> $$\int_M d\omega = \int_{\partial M} \omega$$
> Ici, $\partial M$ est muni de l'orientation induite par celle de $M$, et l'intégrale de droite est celle de la restriction de $\omega$ au bord.

### B. Cas Particuliers Célèbres

1. **Dimension 1 :** Théorème fondamental de l'analyse. $\partial [a, b] = \{b\} - \{a\}$.
2. **Dimension 2 :** Théorème de Green (plan) ou de Kelvin-Stokes (surface dans $\mathbb{R}^3$).
3. **Dimension 3 :** Théorème de la divergence (Ostrogradski).

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Cas du demi-espace $\mathbb{H}^n$

Toute la preuve repose sur ce cas local. Soit $\mathbb{H}^n = \{ (x_1, \dots, x_n) \in \mathbb{R}^n \mid x_n \le 0 \}$. Le bord est l'hyperplan $\{ x_n = 0 \}$.

1. **Expression de la forme :** Une $(n-1)$-forme $\omega$ s'écrit comme une somme :
   $\omega = \sum_{i=1}^n f_i dx_1 \wedge \dots \wedge \widehat{dx_i} \wedge \dots \wedge dx_n$.
2. **Calcul de $d\omega$ :**
   $d\omega = \sum_{i=1}^n (-1)^{i-1} \frac{\partial f_i}{\partial x_i} dx_1 \wedge \dots \wedge dx_n$.
3. **Intégration sur le volume :**
   $\int_{\mathbb{H}^n} d\omega = \sum_{i=1}^n (-1)^{i-1} \int_{\mathbb{H}^n} \frac{\partial f_i}{\partial x_i} dx_1 \dots dx_n$.
4. **Analyse pour $i < n$ :**
   $\int \frac{\partial f_i}{\partial x_i} dx_i = [f_i]_{x_i = -\infty}^{x_i = +\infty} = 0$ car $\omega$ est à support compact.
5. **Analyse pour $i = n$ :**
   L'intégrale devient $(-1)^{n-1} \int_{\mathbb{R}^{n-1}} \left( \int_{-\infty}^0 \frac{\partial f_n}{\partial x_n} dx_n \right) dx_1 \dots dx_{n-1}$.
   Le terme interne vaut $f_n(x_1, \dots, x_{n-1}, 0) - f_n(x_1, \dots, -\infty) = f_n(x', 0)$.
6. **Lien avec le bord :**
   Sur le bord ($x_n=0$), les formes $dx_n$ sont nulles. La restriction de $\omega$ au bord est donc réduite au terme $f_n dx_1 \wedge \dots \wedge dx_{n-1}$.
   Avec l'orientation sortante (normale), on vérifie que les signes correspondent.
7. **Conclusion :** Par linéarité et partition de l'unité, on étend ce résultat local à n'importe quelle variété globale.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Théorème de Green
**Énoncé :** Soit $D$ un disque dans le plan. Calculer $\oint_{\partial D} (x dy - y dx)$.
**Correction Détaillée :**
1. On pose $\omega = x dy - y dx$.
2. $d\omega = dx \wedge dy - (dy \wedge dx) = 2 dx \wedge dy$.
3. Par Stokes : $\oint_{\partial D} \omega = \int_D 2 dA = 2 \times \text{Aire}(D) = 2\pi r^2$.

### Exercice 2 : Niveau Avancé (Flux magnétique)
**Énoncé :** Montrer que le flux d'un champ dont le rotationnel est nul à travers une surface fermée est nul.
**Correction Détaillée :**
Le flux est $\int_S \mathbf{B} \cdot \mathbf{n} dA$. Si $\mathbf{B} = \text{rot } \mathbf{A}$, alors le flux est $\int_S d\alpha$ où $\alpha$ est la 1-forme associée à $\mathbf{A}$. Par Stokes, c'est $\int_{\partial S} \alpha$. Comme la surface est fermée, son bord $\partial S$ est vide. L'intégrale est donc nulle.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** Le théorème de Stokes est l'outil qui permet de passer des **Lois de Conservation locales** (équations différentielles) aux **Bilan Globaux** (intégrales).
- **Example Concret :**
    - **Normalizing Flows (Invariance de masse) :** Pour garantir que la probabilité totale reste égale à 1 pendant que l'IA déforme les données, on utilise l'équation de continuité. La preuve que la masse est conservée repose sur le théorème de la divergence (Stokes).
    - **Optimization on Manifolds :** Lorsqu'on calcule le gradient d'une fonction sur une variété complexe, Stokes aide à simplifier les intégrales de perte, notamment pour les méthodes de "Boundary Integrals" en vision par ordinateur.
    - **Graph Signal Processing :** On définit un opérateur de "Divergence" sur les graphes qui vérifie une version discrète du théorème de Stokes. Cela permet de modéliser des flux d'information cohérents entre les nœuds d'un réseau social.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 114 (Orientation et Intégration sur variétés).md]], [[Jalon 113 (Tenseurs et Formes différentielles).md]]
- **Concepts Futurs dépendants :** [[Jalon 116 (Variétés riemanniennes).md]], [[Jalon 117 (Calcul des variations).md]]
