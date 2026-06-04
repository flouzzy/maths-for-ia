---
uuid: "jalon-93"
title: "Fonctions caractéristiques"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/abstraction
prev: "[[Jalon 92 (Loi forte des grands nombres (LFGN)).md]]"
next: "[[Jalon 94 (Démonstration du théorème central limite).md]]"
---

# Jalon 93 : Fonctions caractéristiques

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que chaque loi de probabilité soit une chanson.
    - La **Loi (densité)** est le son que vous entendez seconde par seconde.
    - La **Fonction caractéristique**, c'est la partition de musique ou le spectrogramme de cette chanson.
    - Pour comparer deux chansons, au lieu d'écouter chaque note, vous pouvez simplement comparer leurs partitions. Si les partitions sont identiques, les chansons le sont aussi.
    - Mieux encore : si vous faites jouer deux chanteurs indépendants en même temps (somme de variables), la partition du duo est simplement le produit des partitions de chaque chanteur. C'est l'outil ultime pour simplifier les calculs de mélanges complexes.
- **Le "Pourquoi on a inventé ça" :** Sommer des variables aléatoires est très difficile avec les densités (il faut faire des calculs de convolution compliqués). En passant dans le "monde fréquentiel" (Fourier), la somme devient une simple multiplication. Cela a permis de prouver les plus grands théorèmes des probabilités (comme le TCL, Jalon 94).
- **Visualisation :** Une courbe dans le plan complexe qui tourne autour de l'origine. Sa forme et sa vitesse de rotation capturent tous les secrets de la variable aléatoire (moyenne, écart-type, etc.).

## 2. Formalisation & Rigueur Académique

Soit $X$ une variable aléatoire réelle sur $(\Omega, \mathcal{F}, P)$.

### A. Définition

> **Définition (Fonction caractéristique) :**
> On appelle fonction caractéristique de $X$ l'application $\phi_X : \mathbb{R} \to \mathbb{C}$ définie par :
> $$\forall t \in \mathbb{R}, \quad \phi_X(t) = \mathbb{E}[e^{itX}] = \int_{\mathbb{R}} e^{itx} dP_X(x)$$
> C'est la transformée de Fourier de la mesure de probabilité $P_X$ (avec un changement de signe de la convention usuelle).

### B. Propriétés Fondamentales

> **Théorème (Propriétés algébriques) :**
> 1. **Normalisation :** $\phi_X(0) = 1$.
> 2. **Bornitude :** $|\phi_X(t)| \le 1$ pour tout $t$.
> 3. **Continuité :** $\phi_X$ est uniformément continue sur $\mathbb{R}$.
> 4. **Injectivité :** Deux variables aléatoires ont la même fonction caractéristique si et seulement si elles ont la même loi.

### C. Lien avec les moments

> **Théorème (Moments) :**
> Si $X$ admet un moment d'ordre $n$ fini ($\mathbb{E}[|X|^n] < \infty$), alors $\phi_X$ est de classe $\mathcal{C}^n$ et :
> $$\phi_X^{(k)}(0) = i^k \mathbb{E}[X^k] \quad \text{pour } k \le n$$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Loi d'une somme de variables indépendantes

Soient $X$ et $Y$ deux V.A. indépendantes. Posons $S = X+Y$.

1. **Définition :** $\phi_S(t) = \mathbb{E}[e^{it(X+Y)}]$.
2. **Propriété de l'exponentielle :** $e^{it(X+Y)} = e^{itX} \cdot e^{itY}$.
3. **Utilisation de l'indépendance :** D'après le Jalon 88, si deux variables $U$ and $V$ sont indépendantes, alors $\mathbb{E}[UV] = \mathbb{E}[U]\mathbb{E}[V]$.
   I.ici, $U = e^{itX}$ and $V = e^{itY}$ sont indépendantes (car fonctions boréliennes de variables indépendantes).
4. **Calcul :**
   $$\phi_S(t) = \mathbb{E}[e^{itX} \cdot e^{itY}] = \mathbb{E}[e^{itX}] \cdot \mathbb{E}[e^{itY}]$$
5. **Conclusion :**
   $$\phi_{X+Y}(t) = \phi_X(t) \cdot \phi_Y(t)$$
   La transformée de Fourier transforme la convolution des lois en produit des fonctions caractéristiques.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Fonction caractéristique de la loi Normale
**Énoncé :** Calculer $\phi_X(t)$ pour $X \sim \mathcal{N}(0, 1)$.
**Correction Détaillée :**
1. **Intégrale :** $\phi_X(t) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{+\infty} e^{itx} e^{-x^2/2} dx$.
2. **Complétion du carré :** $itx - x^2/2 = - \frac{1}{2} (x^2 - 2itx) = - \frac{1}{2} [ (x-it)^2 - (it)^2 ] = - \frac{1}{2}(x-it)^2 - t^2/2$.
3. **Sortie de la constante :** $\phi_X(t) = e^{-t^2/2} \left( \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{+\infty} e^{-(x-it)^2/2} dx \right)$.
4. **Intégrale de Gauss :** L'intégrale dans la parenthèse vaut 1 (via un décalage de contour dans le plan complexe).
5. **Résultat :** $\phi_X(t) = e^{-t^2/2}$.
La loi Normale est son propre "miroir" en Fourier.

### Exercice 2 : Niveau Avancé (Loi de Poisson)
**Énoncé :** Calculer $\phi_X(t)$ pour $X \sim \mathcal{P}(\lambda)$.
**Correction Détaillée :**
$\phi_X(t) = \sum_{k=0}^\infty e^{itk} e^{-\lambda} \frac{\lambda^k}{k!} = e^{-\lambda} \sum_{k=0}^\infty \frac{(\lambda e^{it})^k}{k!}$.
On reconnaît la série de l'exponentielle : $e^{-\lambda} \cdot \exp(\lambda e^{it})$.
**Résultat :** $\phi_X(t) = \exp(\lambda(e^{it} - 1))$.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** La fonction caractéristique est utilisée pour prouver la convergence en loi (Jalon 90). D'après le **Théorème de continuité de Lévy**, $X_n \xrightarrow{\mathcal{L}} X$ si et seulement si $\phi_{X_n}(t) \to \phi_X(t)$ pour tout $t$.
- **Example Concret :**
    - **Stability of Training :** En analysant la fonction caractéristique des gradients, on peut détecter si la distribution des mises à jour a des "queues lourdes" (Heavy Tails), ce qui nécessite des algorithmes comme Adam pour stabiliser l'apprentissage.
    - **Maximum Mean Discrepancy (MMD) :** Pour comparer deux jeux de données en IA (ex: images réelles vs images générées), on calcule la distance entre leurs "moyennes" dans un espace de Hilbert (RKHS). Mathématiquement, c'est une généralisation de la comparaison de leurs fonctions caractéristiques.
    - **Différentiation automatique :** Certains outils avancés utilisent les fonctions caractéristiques pour calculer des moments de haute importance dans des réseaux de neurones stochastiques.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 80 (Transformée de Fourier dans L1).md]], [[Jalon 87 (Intégration et Espérance mathématique).md]]
- **Concepts Futurs dépendants :** [[Jalon 94 (Démonstration du théorème central limite).md]], [[Jalon 95 (Vecteurs gaussiens).md]]
