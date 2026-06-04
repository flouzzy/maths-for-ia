---
uuid: "jalon-109"
title: "Topologie des sous-variétés de Rn"
year: 3
trimester: 10
tags:
  - math/geometrie
  - ia/abstraction
prev: "[[Jalon 108 (Livrable IA).md]]"
next: "[[Jalon 110 (Variétés différentielles abstraites).md]]"
---

# Jalon 109 : Topologie des sous-variétés de $\mathbb{R}^n$

## 1. L'Intuition Première (Niveau 12 ans)

- **La Métaphore :** Imaginez que vous soyez une fourmi sur un immense ballon de baudruche.
    - Pour vous, le monde semble plat : vous pouvez avancer, reculer, aller à gauche ou à droite. Vous avez l'impression de vivre dans un plan ($\mathbb{R}^2$).
    - Pourtant, vue de l'espace, votre "maison" est une sphère courbée dans un espace à 3 dimensions.
    - Une **Sous-variété**, c'est exactement cela : c'est un objet (une courbe, une surface) qui est "tordu" dans un grand espace, mais qui, si on le regarde de très près avec une loupe, ressemble exactement à un espace plat classique.
    - Une **Carte locale**, c'est comme une page d'un atlas : c'est un petit morceau de l'objet que l'on a "aplati" pour pouvoir le dessiner sur une feuille de papier.
- **Le "Pourquoi on a inventé ça" :** Pour pouvoir faire du calcul (dérivées, intégrales) sur des formes courbes. On ne veut pas être limité aux lignes droites. Les sous-variétés sont le cadre naturel pour la physique (la Terre, l'espace-temps) et pour l'IA (la forme des données).
- **Visualisation :** Un fil de fer entortillé dans l'air (variété de dimension 1) ou une nappe de tissu froissée (variété de dimension 2).

## 2. Formalisation & Rigueur Académique

Soit $M$ un sous-ensemble de $\mathbb{R}^n$.

### A. Trois Définitions Équivalentes

On dit que $M$ est une **sous-variété de $\mathbb{R}^n$ de dimension $k$** et de classe $\mathcal{C}^p$ si pour tout point $x \in M$, il existe un voisinage ouvert $V$ de $x$ dans $\mathbb{R}^n$ tel que l'une des propriétés suivantes soit vraie :

1. **Par paramétrage local :** Il existe un ouvert $U \subset \mathbb{R}^k$ and un homéomorphisme $\phi : U \to M \cap V$ qui est une **immersion** (sa différentielle est injective partout).
2. **Par équation locale (Submersion) :** Il existe un ouvert $V$ et une application $f : V \to \mathbb{R}^{n-k}$ qui est une **submersion** (sa différentielle est surjective partout) telle que :
   $$M \cap V = \{ y \in V \mid f(y) = 0 \}$$
3. **Par graphe local :** $M \cap V$ est le graphe d'une fonction de classe $\mathcal{C}^p$ de $k$ variables vers $n-k$ variables (après une éventuelle rotation des axes).

### B. Espace Tangent

> **Définition (Espace Tangent) :**
> L'espace tangent à $M$ au point $x$, noté $T_x M$, est le sous-espace vectoriel de $\mathbb{R}^n$ de dimension $k$ constitué de toutes les vitesses possibles des courbes tracées sur $M$ passant par $x$.
> - Si $M$ est défini par $f(y)=0$, alors $T_x M = \ker(df_x)$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : La sphère unité est une sous-variété

Soit $S^n = \{ x \in \mathbb{R}^{n+1} \mid \sum_{i=1}^{n+1} x_i^2 = 1 \}$.

1. **Choix de la fonction :** Posons $f(x) = (\sum x_i^2) - 1$. On a $S^n = f^{-1}(\{0\})$.
2. **Calcul de la différentielle :**
   $\nabla f(x) = (2x_1, 2x_2, \dots, 2x_{n+1})^T$.
   La différentielle $df_x$ est l'application linéaire $h \mapsto 2 \langle x, h \rangle$.
3. **Condition de submersion :** Pour que $f$ soit une submersion, il faut que sa différentielle soit surjective, donc que le gradient soit non nul.
   $\nabla f(x) = 0 \iff x = (0, \dots, 0)$.
4. **Conclusion :** Comme le point $(0, \dots, 0)$ n'appartient pas à $S^n$ (car $0 \neq 1$), le gradient est toujours non nul sur la sphère.
   Par le théorème des fonctions implicites (Jalon 46/47), $S^n$ est une sous-variété de dimension $(n+1) - 1 = n$ de $\mathbb{R}^{n+1}$.
5. **Espace tangent :** $T_x S^n = \ker(df_x) = \{ h \in \mathbb{R}^{n+1} \mid \langle x, h \rangle = 0 \}$. C'est l'hyperplan perpendiculaire au rayon passant par $x$.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Le groupe orthogonal
**Énoncé :** Montrer que $\mathcal{O}_n(\mathbb{R}) = \{ M \in \mathcal{M}_n \mid M^T M = I_n \}$ est une sous-variété. Quelle est sa dimension ?
**Correction Détaillée :**
1. On définit $f(M) = M^T M - I_n$. $f$ va de $\mathcal{M}_n$ vers $\mathcal{S}_n$ (matrices symétriques).
2. On calcule la différentielle : $df_M(H) = H^T M + M^T H$.
3. On montre qu'en tout point $M \in \mathcal{O}_n$, $df_M$ est surjective.
4. **Dimension :** $\dim(\mathcal{M}_n) - \dim(\mathcal{S}_n) = n^2 - \frac{n(n+1)}{2} = \frac{n(n-1)}{2}$.
**Résultat :** Le groupe des rotations est une variété lisse. Ses éléments sont des matrices, mais ils forment un espace courbe.

### Exercice 2 : Niveau Avancé (Cartes stéréographiques)
**Énoncé :** Construire un paramétrage (une carte) de la sphère $S^2$ privée du pôle Nord.
**Correction Détaillée :**
On trace une droite passant par le pôle Nord $N(0, 0, 1)$ et un point $P(x, y, z)$ de la sphère. Cette droite coupe le plan $z=0$ en un point $(u, v, 0)$. L'application $(u, v) \mapsto (x, y, z)$ est un paramétrage local (une carte). On vérifie qu'elle est lisse et que son inverse aussi.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** L'**Hypothèse de Variété (Manifold Hypothesis)** postule que les données réelles de haute dimension (comme les images de visages) se concentrent près d'une sous-variété de dimension beaucoup plus faible.
- **Example Concret :**
    - **Dimensionality Reduction (t-SNE, Isomap) :** Ces algorithmes essaient de "déplier" la sous-variété des données pour les projeter dans un plan $\mathbb{R}^2$ sans déchirer la structure topologique (en préservant les voisinages).
    - **Geodesic Distances :** Sur une variété (ex: la Terre), la distance en ligne droite à travers le volume n'a pas de sens. On utilise des **Géodésiques** (le chemin le plus court en restant sur la surface). En IA, pour transformer une image de chat en image de chien, on cherche un chemin (une géodésique) sur la variété des images "plausibles".
    - **Normalizing Flows :** On apprend des transformations qui sont des difféomorphismes (homéomorphismes lisses) entre une variété de données complexe et un espace latent simple.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 45 (Différentiabilité et Gradient).md]], [[Jalon 46 (Matrice jacobienne et Règle de la chaîne).md]], [[Jalon 52 (Applications continues et Homéomorphismes).md]]
- **Concepts Futurs dépendants :** [[Jalon 110 (Variétés différentielles abstraites).md]], [[Jalon 116 (Variétés riemanniennes).md]]
