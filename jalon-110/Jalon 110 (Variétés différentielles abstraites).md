---
uuid: "jalon-110"
title: "Variétés différentielles abstraites"
year: 3
trimester: 10
tags:
  - math/geometrie
  - ia/fondations
prev: "[[Jalon 109 (Topologie des sous-variétés de Rn).md]]"
next: "[[Jalon 111 (Applications différentiables entre variétés).md]]"
---

# Jalon 110 : Variétés différentielles abstraites

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous soyez un marin au XVème siècle. Vous voulez explorer toute la Terre.
    - Vous n'avez pas de vue d'ensemble (pas de satellite).
    - Pour naviguer, vous utilisez un **Atlas** : un recueil de cartes papier. Chaque carte représente un petit morceau de mer ou de côte.
    - Quand vous arrivez au bord d'une carte, vous devez passer à la suivante. Pour que le voyage soit fluide, il faut que les deux cartes se recouvrent et que les dessins correspondent parfaitement à l'endroit de la jonction (ce sont les **fonctions de transition**).
    - Une **Variété différentielle**, c'est un monde qui peut être très complexe et courbé, mais qui est entièrement descriptible par un tel Atlas de cartes plates et cohérentes.
- **Le "Pourquoi on a inventé ça" :** Parfois, un objet n'est pas "dans" un espace plus grand. L'univers tout entier, ou l'espace des configurations d'un robot, sont des objets qui existent par eux-mêmes. On a besoin d'une définition intrinsèque qui ne dépend pas d'un "mur" extérieur. C'est la base de la relativité générale et de la robotique moderne.
- **Visualisation :** Un patchwork de tissus. Chaque morceau est plat, mais en les cousant ensemble avec soin, on peut créer une forme en 3D complexe.

## 2. Formalisation & Rigueur Académique

### A. Définition d'une Variété Topologique

Soit $M$ un espace topologique (séparé et à base dénombrable).

> **Définition 1 (Carte locale) :**
> On appelle **carte locale** sur $M$ un couple $(U, \phi)$ où $U$ est un ouvert de $M$ et $\phi$ est un homéomorphisme de $U$ vers un ouvert de $\mathbb{R}^n$. L'entier $n$ est la **dimension** de la variété.

> **Définition 2 (Atlas) :**
> Un **atlas** sur $M$ est une famille de cartes $(U_i, \phi_i)_{i \in I}$ telles que les $U_i$ recouvrent $M$ ($\bigcup U_i = M$).

### B. Structure Différentielle

> **Définition 3 (Changement de cartes) :**
> Pour deux cartes $(U_i, \phi_i)$ and $(U_j, \phi_j)$ dont les domaines se recoupent, l'application de transition est :
> $$\psi_{ij} = \phi_j \circ \phi_i^{-1} : \phi_i(U_i \cap U_j) \to \phi_j(U_i \cap U_j)$$
> C'est une application entre deux ouverts de $\mathbb{R}^n$.

> **Définition 4 (Variété Différentielle) :**
> $M$ est une **variété de classe $\mathcal{C}^k$** si elle possède un atlas dont tous les changements de cartes sont des difféomorphismes de classe $\mathcal{C}^k$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Exemple : Structure de variété sur le cercle $S^1$

Montrons que le cercle unité $S^1$ est une variété de dimension 1 sans utiliser son immersion dans $\mathbb{R}^2$.

1. **Atlas à 2 cartes :** On utilise la projection stéréographique (Jalon 109).
   - Carte 1 ($U_1$) : Le cercle privé du pôle Nord $N(0, 1)$. $\phi_1(x, y) = \frac{x}{1-y}$.
   - Carte 2 ($U_2$) : Le cercle privé du pôle Sud $S(0, -1)$. $\phi_2(x, y) = \frac{x}{1+y}$.
2. **Calcul de l'inverse :** $\phi_1^{-1}(u) = \left( \frac{2u}{u^2+1}, \frac{u^2-1}{u^2+1} \right)$.
3. **Application de transition :** On calcule $\phi_2 \circ \phi_1^{-1}(u)$.
   $\phi_2(\phi_1^{-1}(u)) = \frac{2u/(u^2+1)}{1 + (u^2-1)/(u^2+1)} = \frac{2u}{u^2+1+u^2-1} = \frac{2u}{2u^2} = \frac{1}{u}$.
4. **Conclusion :** L'application de transition est $\psi_{12}(u) = 1/u$, définie sur $\mathbb{R} \setminus \{0\}$. Elle est infiniment dérivable.
   Le cercle est donc une variété différentielle de dimension 1.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : L'espace projectif $\mathbb{P}^n(\mathbb{R})$
**Énoncé :** On définit l'espace projectif comme l'ensemble des droites passant par l'origine dans $\mathbb{R}^{n+1}$. Montrer qu'il s'agit d'une variété.
**Correction Détaillée :**
Une droite est caractérisée par un vecteur $(x_0, \dots, x_n) \neq 0$. On définit $n+1$ cartes $U_i$ où $x_i \neq 0$. Sur $U_i$, on pose $\phi_i(x) = (x_0/x_i, \dots, x_n/x_i)$ (en omettant la $i$-ème composante qui vaut 1). On vérifie que les changements de coordonnées sont des fractions rationnelles lisses.

### Exercice 2 : Niveau Avancé (Somme connexe)
**Énoncé :** Peut-on toujours recoller deux variétés pour en former une nouvelle ?
**Correction Détaillée :**
Oui, c'est l'opération de **somme connexe**. On retire une petite boule dans chaque variété et on recolle les bords (des sphères) par un difféomorphisme. Cela montre que l'on peut construire des mondes topologiques extrêmement riches à partir de briques simples.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, nous manipulons des **Espaces de Représentation**. Parfois, ces espaces ont une topologie non-triviale (des trous, des boucles).
- **Example Concret :**
    - **Rotation Averaging (Vision 3D) :** L'espace des rotations en 3D, $SO(3)$, est une variété de dimension 3 (homéomorphe à l'espace projectif $\mathbb{P}^3$). On ne peut pas faire une moyenne classique (arithmétique) de deux rotations car on sortirait de la variété. Il faut faire de la géométrie sur la variété (moyenne de Fréchet).
    - **Manifold Regularization :** Pour forcer une IA à être cohérente, on impose que sa sortie ne change pas si on se déplace le long de la variété des données. On utilise le Laplacien de Beltrami (Jalon 143), qui est l'équivalent de la dérivée seconde mais sur une variété abstraite.
    - **Topologie des réseaux de neurones :** On étudie la variété formée par l'ensemble des réseaux de neurones ayant la même architecture. Cette variété possède des singularités (endroits où la dimension change) qui expliquent pourquoi l'apprentissage peut parfois ralentir brusquement.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 109 (Topologie des sous-variétés de Rn).md]], [[Jalon 52 (Applications continues et Homéomorphismes).md]]
- **Concepts Futurs dépendants :** [[Jalon 111 (Applications différentiables entre variétés).md]], [[Jalon 119 (Connexions avec les groupes de Lie).md]]
