---
uuid: "jalon-88"
title: "Indépendance d'événements et de variables aléatoires"
year: 2
trimester: 8
tags:
  - math/probabilites
  - ia/fondations
prev: "[[Jalon 87 (Intégration des variables aléatoires).md]]"
next: "[[Jalon 89 (Lemmes de Borel-Cantelli).md]]"
---

# Jalon 88 : Indépendance d'événements et de variables aléatoires

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous lanciez deux dés à deux endroits différents de la Terre.
    - Ce que fait le premier dé n'influence absolument pas ce que fait le second dé. Ils sont **Indépendants**.
    - Si vous savez que le premier dé a fait un "6", cela ne vous donne aucun indice, aucun avantage pour deviner le résultat du second.
    - Mathématiquement, être indépendant, c'est quand les "chances" se multiplient : si vous avez 1 chance sur 6 de faire un "6" avec le premier dé, et 1 chance sur 2 d'avoir un nombre pair avec le second, vous avez $1/6 \times 1/2 = 1/12$ d'avoir les deux en même temps.
- **Le "Pourquoi on a inventé ça" :** Pour simplifier le monde. Si tout dépendait de tout, on ne pourrait rien calculer. En identifiant ce qui est indépendant, on peut découper un problème géant en plein de petits problèmes simples que l'on traite séparément.
- **Visualisation :** Deux événements $A$ et $B$ sont indépendants si la proportion de $A$ à l'intérieur de $B$ est la même que la proportion de $A$ dans l'univers entier.

## 2. Formalisation & Rigueur Académique

Soit $(\Omega, \mathcal{F}, P)$ un espace de probabilité.

### A. Indépendance d'Événements

> **Définition 1 :**
> Deux événements $A$ et $B$ sont **indépendants** si :
> $$P(A \cap B) = P(A) \cdot P(B)$$
> *Note :* Si $P(B) > 0$, cela équivaut à $P(A|B) = P(A)$.

> **Généralisation :** Une famille $(A_i)_{i \in I}$ est mutuellement indépendante si pour toute sous-famille finie $J \subset I$, la probabilité de l'intersection est le produit des probabilités.

### B. Indépendance de Tribus

> **Définition 2 :**
> Deux tribus $\mathcal{A}, \mathcal{B} \subset \mathcal{F}$ sont indépendantes si pour tout $A \in \mathcal{A}$ and $B \in \mathcal{B}$, $A$ et $B$ sont indépendants.

### C. Indépendance de Variables Aléatoires

> **Définition 3 :**
> Deux variables aléatoires $X$ et $Y$ sont **indépendantes** si les tribus qu'elles engendrent ($\sigma(X)$ and $\sigma(Y)$) sont indépendantes.
> Cela revient à dire que pour tous boréliens $B_1, B_2$ :
> $$P(X \in B_1 \text{ et } Y \in B_2) = P(X \in B_1) \cdot P(Y \in B_2)$$

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Indépendance $\implies \mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$

1. **Cadre :** Soient $X$ and $Y$ deux V.A. indépendantes et intégrables.
2. **Utilisation de la mesure produit :** L'indépendance de $X$ et $Y$ équivaut au fait que la loi du couple $(X, Y)$ est la mesure produit des lois marginales : $P_{(X,Y)} = P_X \otimes P_Y$.
3. **Théorème de Transfert et Fubini :**
   $$\mathbb{E}[XY] = \int_{\mathbb{R}^2} xy dP_{(X,Y)}(x, y) = \int_{\mathbb{R}^2} xy d(P_X \otimes P_Y)(x, y)$$
4. **Calcul :**
   Par le théorème de Fubini-Tonelli (Jalon 71) :
   $$\mathbb{E}[XY] = \int_{\mathbb{R}} \left( \int_{\mathbb{R}} xy dP_Y(y) \right) dP_X(x)$$
   $$\mathbb{E}[XY] = \int_{\mathbb{R}} x \left( \int_{\mathbb{R}} y dP_Y(y) \right) dP_X(x) = \int_{\mathbb{R}} x \mathbb{E}[Y] dP_X(x)$$
   $$\mathbb{E}[XY] = \mathbb{E}[Y] \int_{\mathbb{R}} x dP_X(x) = \mathbb{E}[Y] \mathbb{E}[X]$$
5. **Conclusion :** Le produit des espérances est l'espérance du produit. *Attention :* La réciproque est fausse (des variables peuvent avoir une covariance nulle sans être indépendantes).

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Indépendance et Incompatibilité
**Énoncé :** Soient $A$ et $B$ deux événements de probabilité non nulle. Peuvent-ils être à la fois indépendants et incompatibles ($A \cap B = \emptyset$) ?
**Correction Détaillée :**
1. Si ils sont incompatibles, $P(A \cap B) = P(\emptyset) = 0$.
2. Si ils sont indépendants, $P(A \cap B) = P(A)P(B)$.
3. Comme $P(A) > 0$ and $P(B) > 0$, alors $P(A)P(B) > 0$.
4. On aboutit à $0 > 0$, ce qui est impossible.
**Conclusion :** Des événements qui ne peuvent pas arriver ensemble s'influencent forcément (si l'un arrive, l'autre a 0 chance d'arriver). Ils ne sont donc jamais indépendants.

### Exercice 2 : Niveau Avancé (Somme de variables indépendantes)
**Énoncé :** Soient $X, Y$ deux variables indépendantes de loi de Poisson $\mathcal{P}(\lambda_1)$ and $\mathcal{P}(\lambda_2)$. Quelle est la loi de $X+Y$ ?
**Correction Détaillée :**
On calcule $P(X+Y = n) = \sum_{k=0}^n P(X=k \text{ et } Y=n-k)$.
Par indépendance : $\sum_{k=0}^n P(X=k) P(Y=n-k)$.
En remplaçant par les formules de Poisson et en utilisant le binôme de Newton, on trouve que $X+Y$ suit une loi $\mathcal{P}(\lambda_1 + \lambda_2)$.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** L'hypothèse **I.I.D.** (Independent and Identically Distributed) est le fondement de 99% des algorithmes d'IA. Elle stipule que chaque exemple de votre base de données est un tirage indépendant de la même loi de probabilité.
- **Example Concret :**
    - **Calcul de la Vraisemblance (Likelihood) :** Pour entraîner un modèle, on cherche à maximiser $P(Dataset | \theta)$. Grâce à l'indépendance des données, cela devient un simple produit : $\prod P(x_i | \theta)$. En passant au log, cela devient une somme $\sum \ln P(x_i | \theta)$, ce qui est beaucoup plus facile à optimiser.
    - **DropOut :** Dans un réseau de neurones, on désactive aléatoirement des neurones de manière indépendante pendant l'entraînement. Cela force le réseau à ne pas trop compter sur une seule connexion (éviter la co-adaptation) et améliore la robustesse.
    - **Algorithmes Génératifs :** Dans les VAE, on force l'espace latent à être une Gaussienne à matrice de covariance diagonale. Cela signifie que chaque dimension du vecteur latent est **indépendante** des autres, ce qui permet de modifier un seul trait de l'image (ex: la couleur des yeux) sans changer le reste (ex: la forme du visage).

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 85 (Axiomes de Kolmogorov).md]], [[Jalon 70 (Espaces mesurés produits).md]]
- **Concepts Futurs dépendants :** [[Jalon 92 (Démonstration rigoureuse de la loi forte des grands nombres.).md]], [[Jalon 94 (Démonstration du théorème central limite).md]]
