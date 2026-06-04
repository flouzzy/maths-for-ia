---
uuid: "jalon-51"
title: "Espaces métriques"
year: 2
trimester: 5
tags:
  - math/topologie
  - ia/algorithmes
prev: "[[Jalon 50 (Opérateurs topologiques).md]]"
next: "[[Jalon 52 (Applications continues entre espaces topologiques et définition fine des homéomorphismes.).md]]"
---

# Jalon 51 : Espaces métriques

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous soyez un explorateur dans un monde inconnu. Pour vous repérer, vous avez besoin d'un instrument de mesure (une règle ou un GPS) qui vous dit à quelle distance vous êtes d'un objectif. Un **Espace métrique**, c'est simplement un ensemble d'objets où l'on a défini une règle de calcul pour la "distance" entre n'importe quelle paire d'objets. Cette règle doit être honnête : la distance pour aller de A vers B doit être la même que pour revenir (symétrie), et faire un détour par C ne peut pas être plus court que d'y aller directement (inégalité triangulaire).
- **Le "Pourquoi on a inventé ça" :** La topologie générale (Jalon 49) est très puissante mais parfois trop abstraite. En sciences, on a souvent besoin de quantifier "à quel point" deux choses sont proches. Les espaces métriques permettent de ramener la rigueur du calcul numérique (les nombres réels) au sein de la topologie.
- **Visualisation :** Un réseau de villes reliées par des routes. La distance est le nombre de kilomètres. Dans un espace métrique, on peut dessiner des "cercles" parfaits (tous les points à une distance donnée).

## 2. Formalisation & Rigueur Académique

### A. Définition d'une Distance

Soit $X$ un ensemble non vide.

> **Définition 1 (Distance) :**
> On appelle **distance** (ou métrique) sur $X$ une application $d : X \times X \to \mathbb{R}_+$ vérifiant :
> 1. **Séparation :** $d(x, y) = 0 \iff x = y$.
> 2. **Symétrie :** $d(x, y) = d(y, x)$.
> 3. **Inégalité Triangulaire :** $d(x, z) \le d(x, y) + d(y, z)$.
> Le couple $(X, d)$ est appelé un **espace métrique**.

### B. Topologie induite par une distance

> **Définition 2 (Boules) :**
> - Boule ouverte : $B(a, r) = \{ x \in X \mid d(a, x) < r \}$.
> - Boule fermée : $\bar{B}(a, r) = \{ x \in X \mid d(a, x) \le r \}$.

> **Théorème (Topologie induite) :**
> L'ensemble des réunions quelconques de boules ouvertes forme une topologie sur $X$. C'est la topologie usuelle associée à la distance. Dans ce cadre, un ensemble $U$ est ouvert si pour tout $x \in U$, il existe une boule centrée en $x$ incluse dans $U$.

### C. Distances équivalentes

> **Définition 3 (Équivalence) :**
> Deux distances $d_1$ et $d_2$ sont dites **équivalentes** s'il existe $C_1, C_2 > 0$ tels que :
> $$\forall (x, y) \in X^2, \quad C_1 d_1(x, y) \le d_2(x, y) \le C_2 d_1(x, y)$$
> *Propriété :* Deux distances équivalentes induisent la **même topologie** (les mêmes ouverts, les mêmes limites).

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Une boule ouverte est un ouvert au sens topologique

1. **Cadre :** Soit $B(a, r)$ une boule ouverte. Montrons que pour tout $x \in B(a, r)$, il existe une petite boule $B(x, \epsilon)$ contenue dans $B(a, r)$.
2. **Choix du rayon :** Soit $x \in B(a, r)$. Par définition, $d(a, x) < r$.
   Posons $\epsilon = r - d(a, x)$. Comme $d(a, x) < r$, on a $\epsilon > 0$.
3. **Inclusion :** Montrons que $B(x, \epsilon) \subset B(a, r)$.
   Soit $y \in B(x, \epsilon)$. On a $d(x, y) < \epsilon$.
   Par l'inégalité triangulaire :
   $d(a, y) \le d(a, x) + d(x, y) < d(a, x) + \epsilon$.
4. **Conclusion :**
   $d(a, y) < d(a, x) + (r - d(a, x)) = r$.
   Donc $y \in B(a, r)$. La boule ouverte $B(a, r)$ contient un voisinage de chacun de ses points, c'est donc un ouvert.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : La distance discrète
**Énoncé :** On définit $d(x, y) = 1$ si $x \neq y$ et $d(x, x) = 0$. Vérifier qu'il s'agit d'une distance et décrire la topologie induite.
**Correction Détaillée :**
1. **Axiomes :** Séparation et symétrie sont évidentes. Triangulaire : $d(x, z) \le d(x, y) + d(y, z)$. Si $x=z$, $0 \le \dots$ (vrai). Si $x \neq z$, alors $d(x, z)=1$. On ne peut pas avoir $x=y$ et $y=z$ en même temps, donc au moins l'une des distances à droite vaut 1. $1 \le 1$ ou $1 \le 2$ (vrai).
2. **Topologie :** Pour $r=0.5$, $B(x, r) = \{x\}$. Comme chaque singleton est une boule ouverte, chaque singleton est un ouvert. Par réunion, toutes les parties de $X$ sont des ouverts. C'est la **topologie discrète**.

### Exercice 2 : Niveau Avancé (Distance sur les fonctions)
**Énoncé :** Sur $E = \mathcal{C}([0, 1], \mathbb{R})$, on pose $d(f, g) = \int_0^1 |f(t) - g(t)| dt$. Pourquoi l'axiome de séparation est-il vérifié ?
**Correction Détaillée :**
Si $d(f, g) = 0$, alors $\int_0^1 |f-g| = 0$. Comme $|f-g|$ est une fonction **continue** et **positive**, son intégrale n'est nulle que si la fonction est identiquement nulle. Donc $f-g=0 \implies f=g$. (C'est pour cela que la continuité est cruciale ici).

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** En Machine Learning, "apprendre" revient souvent à minimiser la **distance** entre la prédiction du modèle et la réalité. Le choix de la métrique définit ce que le modèle considère comme une "petite" erreur.
- **Exemple Concret :**
    - **Recherche du plus proche voisin (k-NN) :** Pour classer un nouvel exemple, l'algorithme cherche les $k$ points les plus "proches" dans l'espace des caractéristiques. Le résultat dépend entièrement de la métrique choisie (Euclidienne, Cosinus, Minkowski).
    - **Auto-encodeurs et Espaces Latents :** Un auto-encodeur compresse une image en un vecteur dans un "espace latent". On veut que dans cet espace, la distance métrique reflète la ressemblance sémantique (ex: deux photos du même chien doivent être proches métriquement, même si leurs pixels sont différents).
    - ** Wasserstein Distance (Optimal Transport) :** Utilisée dans les GANs (WGAN) pour mesurer la distance entre deux distributions de probabilités. C'est une métrique beaucoup plus robuste que la divergence KL pour entraîner des modèles génératifs.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 34 (Topologie élémentaire des espaces vectoriels normés).md]], [[Jalon 49 (Espaces topologiques généraux).md]]
- **Concepts Futurs dépendants :** [[Jalon 56 (Espaces métriques complets).md]], [[Jalon 126 (Noyaux définis positifs).md]]
