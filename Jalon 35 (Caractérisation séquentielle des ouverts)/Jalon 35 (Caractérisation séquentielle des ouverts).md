---
uuid: "jalon-35"
title: "Caractérisation séquentielle des ouverts, des fermés et des compacts"
year: 1
trimester: 3
tags:
  - math/topologie
  - ia/convergence
prev: "[[Jalon 34 (Topologie élémentaire des espaces vectoriels normés).md]]"
next: "[[Jalon 36 (Livrable IA).md]]"
---

# Jalon 35 : Caractérisation séquentielle des ouverts, des fermés et des compacts

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez un parc entouré d'une clôture.
    - Un ensemble **ouvert**, c'est comme être à l'intérieur du parc : peu importe où vous êtes, vous pouvez toujours faire un petit pas dans n'importe quelle direction sans sortir du parc.
    - Un ensemble **fermé**, c'est le parc *avec* sa clôture. Si vous vous approchez de la clôture aussi près que vous voulez, vous finissez par la toucher, et elle fait partie du parc.
    - Un ensemble **compact**, c'est comme un sac à dos bien rangé : il est limité (il ne s'étend pas à l'infini) et il contient toutes ses limites (il est fermé). Dans un sac compact, si vous cherchez quelque chose (une suite), vous finirez forcément par trouver un point d'accumulation.
- **Le "Pourquoi on a inventé ça" :** Les mathématiciens voulaient traduire des concepts géométriques flous ("bord", "intérieur", "limité") en un langage logique basé sur les **suites**. C'est beaucoup plus facile de manipuler une liste de points $(x_n)$ qui bougent que d'essayer de visualiser des formes abstraites dans des espaces à 1000 dimensions.
- **Visualisation :** Un disque sans son bord est ouvert. Un disque avec son bord est fermé. Le disque entier est compact car il est "petit" (borné) et "complet" (fermé).

## 2. Formalisation

### A. Définitions Formelles

Soit $(E, \| \cdot \|)$ un espace vectoriel normé.

> **Définition 1 (Ouvert) :**
> Une partie $U \subset E$ est un **ouvert** si pour tout $x \in U$, il existe un rayon $r > 0$ tel que la boule ouverte $B(x, r) \subset U$.
> *Caractérisation séquentielle :* $U$ est ouvert si et seulement si pour toute suite $(x_n)$ convergeant vers $x \in U$, les termes $x_n$ sont dans $U$ à partir d'un certain rang.

> **Définition 2 (Fermé) :**
> Une partie $F \subset E$ est un **fermé** si son complémentaire $E \setminus F$ est un ouvert.
> *Caractérisation séquentielle :* $F$ est fermé si et seulement si pour toute suite $(x_n)$ d'éléments de $F$ qui converge vers $x \in E$, alors $x \in F$. (Le fermé "ne laisse pas s'échapper" ses limites).

> **Définition 3 (Compact - Propriété de Bolzano-Weierstrass) :**
> Une partie $K \subset E$ est **compacte** si de toute suite $(x_n)$ d'éléments de $K$, on peut extraire une sous-suite $(x_{\phi(n)})$ qui converge vers un élément de $K$.

### B. Théorèmes Fondamentaux

> **Théorème de Heine-Borel (en dimension finie) :**
> Dans un espace vectoriel normé de dimension finie, une partie $K$ est compacte si et seulement si elle est **fermée et bornée**.

> **Théorème des Bornes Atteintes :**
> Toute application continue $f : K \to \mathbb{R}$ sur un compact $K$ est bornée et atteint ses bornes. (Il existe $x_{min}, x_{max} \in K$ tels que $f(x_{min}) = \inf f$ et $f(x_{max}) = \sup f$).

## 3. Démonstrations

### Démonstration : Fermé $\iff$ Caractérisation séquentielle

1. **Sens direct ($\implies$) :** Soit $F$ un fermé. Soit $(x_n)$ une suite de $F$ convergeant vers $x$. Supposons par l'absurde que $x \notin F$. Alors $x \in E \setminus F$. Comme $E \setminus F$ est ouvert, il existe $r > 0$ tel que $B(x, r) \subset E \setminus F$. Mais comme $x_n \to x$, il existe $N$ tel que pour $n \ge N$, $x_n \in B(x, r)$. Donc $x_n \notin F$, ce qui contredit l'hypothèse. Donc $x \in F$.

2. **Sens réciproque ($\impliedby$) :** Supposons que $F$ vérifie la propriété séquentielle. Montrons que $E \setminus F$ est ouvert. Soit $x \in E \setminus F$. Par l'absurde, supposons qu'aucune boule $B(x, 1/n)$ n'est incluse dans $E \setminus F$. Alors pour chaque $n \in \mathbb{N}^*$, il existe $x_n \in B(x, 1/n) \cap F$. La suite $(x_n)$ est dans $F$ et $\|x_n - x\| < 1/n \to 0$, donc $x_n \to x$. Par hypothèse, $x \in F$. Contradiction car $x \in E \setminus F$. Donc $E \setminus F$ est ouvert, donc $F$ est fermé.

### Démonstration du Théorème de Heine-Borel (Idée en dimension finie)

1. **Nécessité :** Si $K$ est compact, il est fermé (caractérisation séquentielle) et borné (sinon on construit une suite $x_n$ avec $\|x_n\| \to \infty$ sans sous-suite convergente).
2. **Suffisance :** Si $K \subset E$ est borné, ses coordonnées dans une base sont bornées. Par le théorème de Bolzano-Weierstrass sur $\mathbb{R}$ appliqué successivement à chaque coordonnée, on extrait une sous-suite convergente dans $E$. Comme $K$ est fermé, la limite est dans $K$.

## 4. Exercices d'Application

### Exercice 1 : Fermeture de l'ensemble des matrices orthogonales
**Énoncé :** Montrer que $\mathcal{O}_n(\mathbb{R}) = \{ M \in \mathcal{M}_n(\mathbb{R}) \mid M^T M = I_n \}$ est un compact de $\mathcal{M}_n(\mathbb{R})$.

**Correction Détaillée :**
* *Fermé :* Soit $M_k \to M$ une suite de matrices orthogonales. L'application $\phi : M \mapsto M^T M$ est continue (produit de matrices). Donc $\phi(M_k) \to \phi(M)$. Or $\phi(M_k) = I_n$ pour tout $k$, donc la limite $\phi(M) = I_n$. Ainsi $M^T M = I_n$, donc $M \in \mathcal{O}_n(\mathbb{R})$. L'ensemble est fermé.
* *Borné :* Pour $M \in \mathcal{O}_n(\mathbb{R})$, les colonnes $C_j$ forment une base orthonormée, donc $\|C_j\|_2 = 1$. La norme de Frobenius $\|M\|_F = \sqrt{\sum \|C_j\|^2} = \sqrt{n}$. L'ensemble est borné par $\sqrt{n}$.
* *Conclusion :* Fermé et borné en dimension finie $\implies$ Compact.

### Exercice 2 : Niveau Avancé (Distance à un fermé)
**Énoncé :** Soit $F$ un fermé non vide de $E$ et $x \in E$. Montrer qu'il existe $y \in F$ tel que $\|x - y\| = \text{dist}(x, F) = \inf_{z \in F} \|x - z\|$.

**Correction Détaillée :**
Soit $d = \text{dist}(x, F)$. Par définition de l'infimum, il existe une suite $(z_n)$ de $F$ telle que $\|x - z_n\| \to d$.
La suite $(z_n)$ est bornée (car $\|z_n\| \le \|x\| + \|x - z_n\| \to \|x\| + d$).
Considérons l'intersection de $F$ avec une grande boule fermée autour de $x$. Cet ensemble est fermé et borné, donc compact.
On peut extraire une sous-suite $z_{\phi(n)} \to y$.
Comme $F$ est fermé, $y \in F$.
Par continuité de la norme, $\|x - z_{\phi(n)}\| \to \|x - y\|$. Or la limite est $d$.
Donc $\|x - y\| = d$. Le minimum est atteint.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** En optimisation (entraînement de modèles), on veut minimiser une fonction de coût $J(\theta)$. Pour être sûr qu'un minimum **existe**, on invoque souvent le théorème des bornes atteintes sur un ensemble de paramètres **compact**.
- **Exemple Concret :**
    - **Poids bornés :** Dans certains réseaux de neurones, on impose une contrainte $\|w\| \le C$ (Weight Clipping). L'ensemble des poids devient alors un compact (boule fermée). Cela garantit mathématiquement que l'algorithme ne divergera pas vers l'infini et qu'il existe une configuration "optimale" dans cette zone.
    - **Stabilité de GANs :** La compacité de l'espace des paramètres aide à prouver l'existence d'équilibres de Nash dans les jeux de minimax utilisés pour les réseaux antagonistes (GANs).

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 34 (Topologie élémentaire des espaces vectoriels normés).md]], [[Jalon 15 (Sous-suites).md]]
- **Concepts Futurs dépendants :** [[Jalon 54 (Compacité générale).md]], [[Jalon 123 (Problèmes d'optimisation sous contraintes).md]]
