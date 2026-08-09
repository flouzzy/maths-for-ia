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

## 1. La Genèse de la Métrique

Les espaces topologiques introduisent la notion de proximité et de voisinage avec une grande élégance qualitative, en se basant sur les ensembles ouverts. Cependant, dans de nombreux problèmes d'analyse, de géométrie ou de physique, nous avons besoin d'une quantification rigoureuse de cette proximité. Il ne suffit plus de dire que deux points sont "proches", il faut mesurer "à quel point" ils le sont.

L'idée de distance est profondément ancrée dans notre intuition de l'espace physique cartésien. Maurice Fréchet, en 1906, a formalisé cette notion dans sa thèse en introduisant les "espaces métriques". L'objectif était d'abstraire la notion de distance usuelle de $\mathbb{R}^n$ ou $\mathbb{C}^n$ à des ensembles abstraits, comme des espaces de fonctions, de suites, ou des graphes, tout en conservant les propriétés fondamentales qui permettent d'y faire de l'analyse : la séparation des points, l'absence de direction privilégiée (symétrie), et l'idée géométrique fondamentale que la ligne droite est le chemin le plus court (inégalité triangulaire). Ce cadre formel permet de transposer des concepts comme la convergence, la continuité et la complétude dans des univers mathématiques insoupçonnés, jetant un pont vital entre l'intuition géométrique et l'analyse fonctionnelle abstraite.

## 2. Définitions, Théorèmes et Structures Métriques

Soit $X$ un ensemble non vide.

### Définition 1 : Distance (ou métrique)

On appelle **distance** (ou métrique) sur l'ensemble $X$ toute application $d : X \times X \to \mathbb{R}_+$ vérifiant les trois axiomes suivants :

1. **Séparation :** $\forall x, y \in X, \quad d(x, y) = 0 \iff x = y$.
2. **Symétrie :** $\forall x, y \in X, \quad d(x, y) = d(y, x)$.
3. **Inégalité triangulaire :** $\forall x, y, z \in X, \quad d(x, z) \le d(x, y) + d(y, z)$.

Le couple $(X, d)$ est alors appelé un **espace métrique**.
Les éléments de $X$ sont usuellement appelés des "points".

#### Exemple immédiat : La distance euclidienne sur $\mathbb{R}^2$

Dans le plan cartésien $X = \mathbb{R}^2$, pour deux points $x = (x_1, x_2)$ et $y = (y_1, y_2)$, on définit la distance euclidienne canonique :
$$d_2(x, y) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2}$$
Considérons $x = (1, 1)$, $y = (4, 5)$ et $z = (4, 1)$.
Calculons les distances :
- $d_2(x, y) = \sqrt{(4-1)^2 + (5-1)^2} = \sqrt{3^2 + 4^2} = \sqrt{25} = 5$.
- $d_2(x, z) = \sqrt{(4-1)^2 + (1-1)^2} = \sqrt{3^2 + 0} = 3$.
- $d_2(z, y) = \sqrt{(4-4)^2 + (5-1)^2} = \sqrt{0 + 4^2} = 4$.
On vérifie l'inégalité triangulaire $d_2(x, y) \le d_2(x, z) + d_2(z, y)$, soit $5 \le 3 + 4 = 7$.

#### Contre-exemple : Ce qui n'est pas une distance

Soit sur $\mathbb{R}$, la fonction $f(x, y) = (x - y)^2$.
Vérifions l'inégalité triangulaire avec $x = 0, y = 1, z = 2$.
$f(0, 2) = (0-2)^2 = 4$.
$f(0, 1) + f(1, 2) = (0-1)^2 + (1-2)^2 = 1 + 1 = 2$.
Ici, $f(x, z) > f(x, y) + f(y, z)$ puisque $4 > 2$. L'application au carré ne respecte pas l'inégalité triangulaire, ce n'est pas une distance.

### Définition 2 : Boules ouvertes et fermées

Dans un espace métrique $(X, d)$, on définit pour un point $a \in X$ (le centre) et un réel $r > 0$ (le rayon) :

- **La boule ouverte** de centre $a$ et de rayon $r$ :
  $$B(a, r) = \left\lbrace x \in X \mid d(a, x) < r \right\rbrace$$
- **La boule fermée** de centre $a$ et de rayon $r$ :
  $$\bar{B}(a, r) = \left\lbrace x \in X \mid d(a, x) \le r \right\rbrace$$

### Théorème 1 : Topologie induite par une distance

Dans tout espace métrique $(X, d)$, on peut définir une topologie $\mathcal{T}_d$ où un ensemble $U \subset X$ est un **ouvert** si, et seulement si, pour tout point $x \in U$, il existe un rayon $r > 0$ tel que la boule ouverte $B(x, r)$ soit entièrement contenue dans $U$ :
$$U \in \mathcal{T}_d \iff \forall x \in U, \exists r > 0, B(x, r) \subset U$$

#### Exemple immédiat : Topologie sur $\mathbb{R}$ usuel

Dans $(\mathbb{R}, d)$ avec $d(x,y) = |x-y|$, l'intervalle $]0, 1[$ est un ouvert.
Pour tout point $x \in ]0, 1[$, on pose $r = \min(x, 1-x)$.
La boule $B(x, r)$ est l'intervalle $]x-r, x+r[$, qui est strictement inclus dans $]0, 1[$.
En revanche, $[0, 1[$ n'est pas un ouvert car pour le point $0$, toute boule $B(0, r) = ]-r, r[$ contiendra des points strictement négatifs (comme $-r/2$), qui ne sont pas dans $[0, 1[$.

### Définition 3 : Distances équivalentes

Deux distances $d_1$ et $d_2$ sur un même ensemble $X$ sont dites **topologiquement équivalentes** si elles induisent exactement la même topologie $\mathcal{T}_{d_1} = \mathcal{T}_{d_2}$.
Un critère suffisant (mais non nécessaire) est l'équivalence **métrique** : il existe des constantes $C_1 > 0$ et $C_2 > 0$ telles que :
$$\forall x, y \in X, \quad C_1 d_1(x, y) \le d_2(x, y) \le C_2 d_1(x, y)$$

## 3. Démonstrations Fondamentales

### Proposition : Une boule ouverte est un ouvert pour la topologie induite

Nous démontrons rigoureusement que la définition topologique de l'ouvert s'applique à la boule ouverte elle-même.

**Démonstration :**
Soit $(X, d)$ un espace métrique.
Fixons un point $a \in X$ et un rayon $R > 0$.
Considérons la boule ouverte $U = B(a, R)$.
Nous voulons montrer que $U$ est un ouvert, c'est-à-dire : $\forall x \in U, \exists r > 0, B(x, r) \subset U$.

1. Soit un point arbitraire $x \in B(a, R)$.
2. Par définition de la boule ouverte, nous avons $d(a, x) < R$.
3. Définissons un rayon $r = R - d(a, x)$. Comme $d(a, x) < R$, il est clair que $r > 0$.
4. Prenons maintenant un point quelconque $y \in B(x, r)$.
   Par définition, $d(x, y) < r$.
5. Appliquons l'inégalité triangulaire de la distance $d$ pour les points $a, x, y$ :
   $$d(a, y) \le d(a, x) + d(x, y)$$
6. Comme $d(x, y) < r$, nous obtenons une inégalité stricte :
   $$d(a, y) < d(a, x) + r$$
7. En remplaçant $r$ par sa définition :
   $$d(a, y) < d(a, x) + (R - d(a, x)) = R$$
8. Nous avons donc montré que $d(a, y) < R$, ce qui signifie exactement que $y \in B(a, R) = U$.
9. Ainsi, nous avons établi l'inclusion $B(x, r) \subset B(a, R)$.
La boule ouverte est donc bien un ensemble ouvert. $\blacksquare$

### Proposition : L'inégalité triangulaire inversée

Un outil analytique fondamental pour l'étude de la continuité de la fonction distance est l'inégalité triangulaire inversée.

**Démonstration :**
Soient $x, y, z \in X$.
Par l'inégalité triangulaire classique, on a :
$$d(x, z) \le d(x, y) + d(y, z)$$
Isolons $d(x, z) - d(y, z)$ :
$$d(x, z) - d(y, z) \le d(x, y) \quad \text{(Éq. 1)}$$

En permutant les rôles de $x$ et $y$, et en utilisant la symétrie de la distance $d(y, z) \le d(y, x) + d(x, z)$, on obtient :
$$d(y, z) - d(x, z) \le d(y, x) = d(x, y) \quad \text{(Éq. 2)}$$

Les équations 1 et 2 impliquent que la quantité $d(x, z) - d(y, z)$ est encadrée par $-d(x, y)$ et $d(x, y)$. On en déduit l'inégalité en valeur absolue :
$$|d(x, z) - d(y, z)| \le d(x, y)$$
Cette inégalité démontre que la fonction $x \mapsto d(x, z)$ (pour $z$ fixé) est une fonction 1-lipschitzienne, et par conséquent uniformément continue. $\blacksquare$

## 4. Applications en Intelligence Artificielle et Informatique

### Algorithmes de classification et clustering
Dans les architectures d'IA, les espaces métriques sont la structure géométrique par excellence pour évaluer les similarités.
L'algorithme des $K$-Nearest Neighbors (K-NN) cherche les $K$ points d'entraînement qui minimisent la distance $d(x, x_i)$ par rapport à une nouvelle entrée $x$.
Dans le partitionnement K-Means, l'objectif d'optimisation est de minimiser l'inertie intra-classe, qui n'est autre que la somme des distances (au carré) des points à leur centroïde. Le choix de la métrique $d$ (souvent euclidienne, mais parfois Manhattan ou de Mahalanobis) dicte entièrement la topologie des clusters trouvés.

### Traitement Automatique du Langage Naturel (NLP)
Dans les espaces de plongement (embeddings comme Word2Vec ou BERT), les mots et les phrases sont représentés comme des vecteurs dans un espace métrique dense de haute dimension. La distance euclidienne ou la distance associée à la similarité cosinus ($d(u,v) = 1 - \frac{u \cdot v}{\|u\| \|v\|}$) structurent l'espace sémantique. Les théorèmes de topologie métrique s'appliquent pour garantir que de petites perturbations dans le sens induisent de petits déplacements continus dans l'espace latent.

### Espaces Latents et Modèles Génératifs (GANs)
Les Wasserstein-GANs (WGAN) utilisent la "Distance de la Terre (Earth Mover's Distance)", qui est la distance métrique de Wasserstein-1 entre deux distributions de probabilités. Contrairement à la divergence de Kullback-Leibler, la distance de Wasserstein respecte une structure d'espace métrique complet, ce qui fournit des gradients lisses et continus lors de l'entraînement par descente de gradient, évitant le problème majeur de l'évanouissement du gradient (vanishing gradient).
