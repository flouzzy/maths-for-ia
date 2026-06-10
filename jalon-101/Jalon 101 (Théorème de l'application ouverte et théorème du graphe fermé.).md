---
uuid: "jalon-101"
title: "Application ouverte et Graphe fermé"
year: 3
trimester: 9
tags:
  - math/analyse
  - ia/fondations
prev: "[[Jalon 100 (Théorème de Banach-Steinhaus).md]]"
next: "[[Jalon 102 (Topologies faibles et faibles-).md]]"
---

# Jalon 101 : Application ouverte et Graphe fermé

## 1. Présentation du concept clé

- **La Métaphore :**
    - **L'Application Ouverte :** Imaginez que vous projetiez la lumière d'une lampe de poche à travers un pochoir sur un mur. Si le mur est "solide" (espace de Banach) et que votre lumière couvre tout le mur (surjectivité), alors n'importe quelle petite zone du pochoir doit projeter une petite zone visible sur le mur. On ne peut pas "écraser" un disque ouvert en un simple point ou une ligne invisible.
    - **Le Graphe Fermé :** Imaginez que vous dessiniez une fonction. Normalement, pour savoir si elle est continue, il faut vérifier qu'elle ne fait pas de sauts brusques. Le théorème du graphe fermé dit : s'il est impossible de s'approcher d'un point $(x, y)$ sur le dessin sans que ce point appartienne vraiment à la courbe, alors la fonction est **automatiquement** continue. La "solidité" du dessin garantit la fluidité du mouvement.
- **Le "Pourquoi on a inventé ça" :** Pour s'épargner des calculs. En dimension finie, si une matrice est inversible, son inverse est toujours continue. En dimension infinie, ce n'est pas automatique. Ces théorèmes prouvent que dans les "bons" espaces (Banach), la structure algébrique (bijection) entraîne la structure topologique (continuité).
- **Visualisation :** L'image d'une boule ouverte est encore une boule ouverte. Une fonction dont on ne peut pas "sortir" du graphe par passage à la limite.

## 2. Formalisation

Soient $E$ et $F$ deux espaces de **Banach**.

### A. Théorème de l'Application Ouverte

> **Théorème (Banach-Schauder) :**
> Soit $T : E \to F$ un opérateur linéaire continu et **surjectif**.
> Alors $T$ est une **application ouverte** : l'image de tout ouvert de $E$ est un ouvert de $F$.
> En particulier, il existe $M > 0$ tel que la boule unité de $F$ soit incluse dans l'image de la boule de rayon $M$ de $E$.

### B. Théorème de l'Inverse Borné

> **Corollaire :**
> Si $T : E \to F$ est une bijection linéaire continue entre deux espaces de Banach, alors son inverse $T^{-1}$ est **automatiquement continu**.

### C. Théorème du Graphe Fermé

> **Théorème :**
> Soit $T : E \to F$ une application linéaire. $T$ est continue si et seulement si son graphe $\Gamma(T) = \{ (x, Tx) \mid x \in E \}$ est un sous-ensemble **fermé** de l'espace produit $E \times F$.

## 3. Démonstrations

### Démonstration : $T^{-1}$ est continu $\iff$ Graphe fermé

Cette preuve montre comment le théorème de l'application ouverte simplifie la vie.

1. **Sens ($\implies$) :** Si $T$ est continu, alors $\Gamma(T)$ est fermé (vrai dans tout espace de Hausdorff, Jalon 53).
2. **Sens ($\impliedby$) :** Supposons $\Gamma(T)$ fermé.
3. **Structure de Banach :** $E \times F$ muni de la norme $\|(x, y)\| = \|x\| + \|y\|$ est un espace de Banach. Comme $\Gamma(T)$ est un sous-espace fermé d'un Banach, c'est lui-même un espace de **Banach** (Jalon 56).
4. **Opérateur de projection :** Considérons l'application $\pi : \Gamma(T) \to E$ définie par $\pi(x, Tx) = x$.
   - $\pi$ est linéaire.
   - $\pi$ est continue car $\|\pi(x, Tx)\| = \|x\| \le \|(x, Tx)\|$.
   - $\pi$ est une **bijection** entre $\Gamma(T)$ et $E$.
5. **Application du théorème de l'inverse borné :** $\pi$ est une bijection continue entre deux Banach ($\Gamma(T)$ and $E$). Donc son inverse $\pi^{-1} : E \to \Gamma(T)$ est continue.
6. **Reconstruction de T :** On peut écrire $T$ comme la composée : $x \xrightarrow{\pi^{-1}} (x, Tx) \xrightarrow{proj_F} Tx$.
7. **Conclusion :** Comme composée d'applications continues, $T$ est continu.

## 4. Exercices d'Application

### Exercice 1 : Équivalence de deux normes
**Énoncé :** Soient $\|\cdot\|_1$ et $\|\cdot\|_2$ deux normes sur $E$ telles que $E$ soit complet pour les deux. On suppose qu'il existe $C > 0$ tel que $\|x\|_1 \le C \|x\|_2$. Montrer que les deux normes sont équivalentes.
**Correction Détaillée :**
1. Considérons l'identité $Id : (E, \|\cdot\|_2) \to (E, \|\cdot\|_1)$.
2. Par hypothèse, $Id$ est continue.
3. C'est une bijection entre deux espaces de Banach.
4. Par le théorème de l'inverse borné, $Id^{-1} : (E, \|\cdot\|_1) \to (E, \|\cdot\|_2)$ est continue.
5. Il existe donc $C'$ tel que $\|x\|_2 \le C' \|x\|_1$.
6. **Conclusion :** Les normes sont équivalentes.

### Exercice 2 : Niveau Avancé (Opérateur non borné)
**Énoncé :** L'opérateur de dérivation sur un espace de fonctions peut-il avoir un graphe fermé sans être continu ?
**Correction Détaillée :**
Si on définit $D$ sur un domaine restreint (ex: fonctions $\mathcal{C}^1$ dans $L^2$), son graphe est fermé car une limite de fonctions et de leurs dérivées (au sens des distributions) est cohérente. Cependant, $D$ n'est pas continu. Le théorème du graphe fermé n'est pas contredit car le domaine de $D$ n'est pas l'espace de Banach $L^2$ entier (c'est un sous-espace dense).

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** Ces théorèmes définissent la notion de **Problème bien posé** au sens de Hadamard. Un problème est bien posé si la solution existe, est unique, et **dépend continûment des données**.
- **Example Concret :**
    - **Régularisation de Tikhonov (Ridge) :** Dans les problèmes d'inversion (ex: retrouver une image nette à partir d'un flou), l'opérateur de flou $T$ est continu mais son inverse ne l'est pas. Le théorème de l'inverse borné nous dit que c'est parce que l'image de $T$ n'est pas fermée (elle n'est pas "solide"). La régularisation consiste à forcer l'opérateur à redevenir inversible de manière continue.
    - **Stabilité des GANs :** On veut que le générateur apprenne une application surjective entre l'espace latent et l'espace des données. Le théorème de l'application ouverte aide à comprendre sous quelles conditions le générateur ne va pas "s'effondrer" sur un petit nombre de modes (Mode Collapse).
    - **Invertible Neural Networks (INN) :** Les architectures comme les Normalizing Flows imposent que le réseau soit une bijection. Ces théorèmes garantissent que si le réseau est continu, son inverse l'est aussi, ce qui est crucial pour reconstruire les données sans bruit numérique.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 100 (Théorème de Banach-Steinhaus).md]], [[Jalon 57 (Théorème du point fixe de Banach).md]]
- **Concepts Futurs dépendants :** [[Jalon 107 (Introduction à la théorie des opérateurs non bornés et résolvante.).md]], [[Jalon 125 (Opérateurs proximaux).md]]
