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

## 1. Introduction (Genèse Physique et Historique)

Le concept d'indépendance est au cœur de la théorie des probabilités modernes. Historiquement, l'idée intuitive qu'un événement n'a aucune influence sur un autre (comme les lancers successifs d'une pièce de monnaie) a préexisté à sa formalisation mathématique. Andreï Kolmogorov, dans ses fondements axiomatiques de 1933, a traduit cette absence d'influence par une structure purement multiplicative des mesures de probabilité.

Si tout dépendait de tout, le calcul des probabilités de systèmes complexes (comme en physique statistique moléculaire ou en génétique des populations) serait impossible. L'indépendance permet de décomposer l'analyse d'un système gigantesque en l'étude de ses composants individuels, fournissant l'hypothèse de base (Indépendantes et Identiquement Distribuées, i.i.d.) indispensable aux théorèmes limites fondamentaux (Loi des Grands Nombres, Théorème Central Limite).

Géométriquement, dans un espace produit, l'indépendance correspond à l'orthogonalité des projections : la mesure d'un rectangle $A \times B$ devient le produit des mesures de ses côtés.

## 2. Définitions, Théorèmes et Exemples

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace de probabilité.

### A. Indépendance de deux événements

> **Définition (Indépendance de deux événements)**
> Deux événements $A, B \in \mathcal{F}$ sont dits indépendants par rapport à la probabilité $\mathbb{P}$ si :
> $$\mathbb{P}(A \cap B) = \mathbb{P}(A) \mathbb{P}(B)$$
> Si $\mathbb{P}(B) > 0$, cette définition est équivalente à $\mathbb{P}(A|B) = \mathbb{P}(A)$.

**Exemple 1 : Lancer de deux dés.**
Considérons le lancer de deux dés équilibrés à 6 faces.
- $A$ : "Le premier dé donne un résultat pair" $\implies \mathbb{P}(A) = 3/6 = 1/2$.
- $B$ : "La somme des deux dés vaut 7".
Les couples donnant 7 sont $(1,6), (2,5), (3,4), (4,3), (5,2), (6,1) \implies \mathbb{P}(B) = 6/36 = 1/6$.
- $A \cap B$ : Le premier est pair et la somme vaut 7, soit les couples $(2,5), (4,3), (6,1) \implies \mathbb{P}(A \cap B) = 3/36 = 1/12$.
On vérifie bien que $\mathbb{P}(A \cap B) = 1/12 = \mathbb{P}(A) \times \mathbb{P}(B)$. Les événements sont indépendants.

### B. Indépendance d'une famille d'événements

> **Définition (Mutuelle indépendance)**
> Une famille d'événements $(A_i)_{i \in I}$ (où $I$ est un ensemble quelconque d'indices) est dite mutuellement indépendante si, pour toute sous-famille finie d'indices $J \subset I$ :
> $$\mathbb{P}\left(\bigcap_{j \in J} A_j\right) = \prod_{j \in J} \mathbb{P}(A_j)$$

**Attention :** L'indépendance deux-à-deux n'implique pas l'indépendance mutuelle.

**Exemple 2 : Indépendance deux-à-deux vs Mutuelle.**
On lance deux pièces équilibrées.
$A$ : "La première pièce fait Face", $\mathbb{P}(A) = 1/2$.
$B$ : "La deuxième pièce fait Face", $\mathbb{P}(B) = 1/2$.
$C$ : "Les deux pièces donnent le même résultat", $\mathbb{P}(C) = 1/2$.
On a $\mathbb{P}(A \cap B) = 1/4 = \mathbb{P}(A)\mathbb{P}(B)$ (indépendants). De même pour $(B,C)$ et $(A,C)$.
Cependant, $\mathbb{P}(A \cap B \cap C) = \mathbb{P}(\text{Les deux font Face}) = 1/4$.
Or $\mathbb{P}(A)\mathbb{P}(B)\mathbb{P}(C) = 1/8$.
$A, B$ et $C$ sont indépendants deux-à-deux, mais pas mutuellement indépendants.

### C. Indépendance de classes et tribus

> **Définition (Indépendance de tribus)**
> Deux sous-tribus $\mathcal{G}_1, \mathcal{G}_2 \subset \mathcal{F}$ sont dites indépendantes si, pour tout $A \in \mathcal{G}_1$ et tout $B \in \mathcal{G}_2$, $A$ et $B$ sont indépendants.

> **Lemme (Lemme de classe monotone pour l'indépendance)**
> Si deux classes d'événements $\mathcal{C}_1$ et $\mathcal{C}_2$ stables par intersection finie ($\pi$-systèmes) sont indépendantes, alors les tribus qu'elles engendrent $\sigma(\mathcal{C}_1)$ et $\sigma(\mathcal{C}_2)$ sont indépendantes.

**Exemple 3 : Événements complémentaires.**
Si $A$ et $B$ sont indépendants, alors $A$ et $B^c$ le sont aussi.
En effet, $\mathbb{P}(A \cap B^c) = \mathbb{P}(A) - \mathbb{P}(A \cap B) = \mathbb{P}(A) - \mathbb{P}(A)\mathbb{P}(B) = \mathbb{P}(A)(1 - \mathbb{P}(B)) = \mathbb{P}(A)\mathbb{P}(B^c)$.

### D. Indépendance de variables aléatoires

> **Définition (Indépendance de V.A.)**
> Une famille de variables aléatoires $(X_i)_{i \in I}$ (définies sur $(\Omega, \mathcal{F}, \mathbb{P})$ à valeurs dans des espaces mesurables $(E_i, \mathcal{E}_i)$) est dite indépendante si les tribus qu'elles engendrent $\sigma(X_i) = \{X_i^{-1}(B) : B \in \mathcal{E}_i\}$ sont mutuellement indépendantes.

En pratique pour un nombre fini de V.A. $(X_1, \ldots, X_n)$, cela signifie :
$$\mathbb{P}(X_1 \in B_1, \ldots, X_n \in B_n) = \prod_{k=1}^n \mathbb{P}(X_k \in B_k)$$

> **Théorème (Caractérisation par la loi conjointe)**
> Les variables $X_1, \ldots, X_n$ sont indépendantes si et seulement si leur loi conjointe est le produit tensoriel de leurs lois marginales :
> $$\mathbb{P}_{(X_1, \ldots, X_n)} = \mathbb{P}_{X_1} \otimes \cdots \otimes \mathbb{P}_{X_n}$$

**Exemple 4 : Vecteur Gaussien.**
Soit un vecteur aléatoire $(X,Y)$ suivant une loi normale bidimensionnelle de matrice de covariance $\Sigma$. Si les covariances non diagonales sont nulles (i.e. $\operatorname{Cov}(X,Y) = 0$), la densité conjointe se factorise exactement en produit de densités marginales. Ainsi, pour les vecteurs gaussiens, décorrélation implique indépendance.

> **Théorème (Indépendance et Espérance)**
> Si $X$ et $Y$ sont deux variables aléatoires réelles indépendantes et intégrables, alors leur produit $XY$ est intégrable et :
> $$\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$$

**Exemple 5 : Variance d'une somme.**
Soient $X, Y$ indépendantes de carré intégrable.
$\operatorname{Var}(X+Y) = \mathbb{E}[((X+Y) - \mathbb{E}[X+Y])^2] = \operatorname{Var}(X) + \operatorname{Var}(Y) + 2\operatorname{Cov}(X,Y)$.
Puisque $X$ et $Y$ sont indépendantes, $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$, donc $\operatorname{Cov}(X,Y) = 0$.
Ainsi, la variance de la somme de V.A. indépendantes est la somme de leurs variances.

## 3. Démonstrations

### Démonstration : Stabilité de l'indépendance par passage au complémentaire

**Énoncé :** Si $A$ et $B$ sont des événements indépendants, alors $A$ et $B^c$ sont indépendants.

**Preuve :**
1. L'ensemble $A$ peut s'écrire comme l'union disjointe de $(A \cap B)$ et $(A \cap B^c)$.
   $$A = (A \cap B) \cup (A \cap B^c)$$
2. Par additivité de la mesure de probabilité $\mathbb{P}$ pour des événements disjoints, on obtient :
   $$\mathbb{P}(A) = \mathbb{P}(A \cap B) + \mathbb{P}(A \cap B^c)$$
3. Or, par hypothèse, $A$ et $B$ sont indépendants, donc $\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)$. En substituant :
   $$\mathbb{P}(A) = \mathbb{P}(A)\mathbb{P}(B) + \mathbb{P}(A \cap B^c)$$
4. On isole le terme cherché :
   $$\mathbb{P}(A \cap B^c) = \mathbb{P}(A) - \mathbb{P}(A)\mathbb{P}(B)$$
5. En factorisant par $\mathbb{P}(A)$ :
   $$\mathbb{P}(A \cap B^c) = \mathbb{P}(A) (1 - \mathbb{P}(B))$$
6. Comme $\mathbb{P}(B^c) = 1 - \mathbb{P}(B)$ :
   $$\mathbb{P}(A \cap B^c) = \mathbb{P}(A)\mathbb{P}(B^c)$$
7. Ceci prouve rigoureusement l'indépendance de $A$ et $B^c$. Le même argument s'applique pour $A^c$ et $B$, ainsi que pour $A^c$ et $B^c$. $\blacksquare$

### Démonstration : Théorème d'indépendance et espérance (Cas Positif)

**Énoncé :** Si $X$ et $Y$ sont deux variables aléatoires réelles positives et indépendantes, $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$.

**Preuve :**
1. Supposons d'abord que $X = \mathbf{1}_A$ et $Y = \mathbf{1}_B$ sont des fonctions indicatrices avec $A, B$ indépendants.
   Le produit $XY$ vaut $1$ si et seulement si $\omega \in A \cap B$, donc $XY = \mathbf{1}_{A \cap B}$.
   L'espérance donne : $\mathbb{E}[XY] = \mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B) = \mathbb{E}[X]\mathbb{E}[Y]$.
2. Par linéarité de l'espérance, la propriété s'étend aux variables étagées (combinaisons linéaires finies d'indicatrices) $X = \sum a_i \mathbf{1}_{A_i}$ et $Y = \sum b_j \mathbf{1}_{B_j}$ où les $(A_i)$ et $(B_j)$ sont indépendants.
3. Soient $X, Y$ deux variables aléatoires positives indépendantes. Il existe des suites croissantes de variables étagées positives $(X_n)$ et $(Y_n)$ telles que $X_n \uparrow X$ et $Y_n \uparrow Y$ (Théorème d'approximation).
4. La suite de variables étagées $X_n Y_n$ croît vers $XY$.
5. D'après le Théorème de Convergence Monotone de Beppo Levi,
   $$\mathbb{E}[XY] = \lim_{n \to \infty} \mathbb{E}[X_n Y_n]$$
6. Puisque $X_n$ et $Y_n$ sont étagées et indépendantes (construites sur $\sigma(X)$ et $\sigma(Y)$), $\mathbb{E}[X_n Y_n] = \mathbb{E}[X_n]\mathbb{E}[Y_n]$.
7. Par passage à la limite :
   $$\lim_{n \to \infty} \mathbb{E}[X_n]\mathbb{E}[Y_n] = \lim_{n \to \infty} \mathbb{E}[X_n] \times \lim_{n \to \infty} \mathbb{E}[Y_n] = \mathbb{E}[X]\mathbb{E}[Y]$$
8. D'où le résultat pour les variables positives. Pour des variables de signe quelconque, on décompose en parties positives et négatives ($X = X^+ - X^-$). $\blacksquare$

## 4. Applications en Physique, Logique, & AI

### Intelligence Artificielle et Machine Learning
L'indépendance conditionnelle et inconditionnelle est le socle des modèles graphiques probabilistes (Réseaux Bayésiens). Les algorithmes d'apprentissage (Maximum de Vraisemblance, Descente de Gradient Stochastique) présument que l'ensemble d'entraînement est constitué de variables i.i.d. La vraisemblance conjointe $\mathcal{L}(\theta) = \prod_{i=1}^N \mathbb{P}(x_i | \theta)$ devient une somme de logarithmes, simplifiant radicalement l'optimisation par la log-vraisemblance. Sans l'indépendance, les calculs de gradients s'effondreraient sous la complexité des covariances massives. En Deep Learning, le principe du *Dropout* introduit artificiellement des désactivations aléatoires indépendantes des neurones, forçant le réseau à apprendre des caractéristiques non corrélées.

### Mécanique Statistique
En physique des particules, l'hypothèse d'indépendance (chaos moléculaire) dans la théorie cinétique des gaz de Maxwell-Boltzmann stipule que les vitesses de différentes particules sont indépendantes avant collision. Cela permet d'écrire la fonction de distribution à deux corps comme le produit des fonctions de distribution à un corps, menant directement à l'équation de Boltzmann.

### Logique Formelle et Théorie de l'Information
En théorie de Shannon, deux sources d'information indépendantes ne partagent aucune information mutuelle. Mathématiquement, $I(X;Y) = H(X) + H(Y) - H(X,Y)$. Pour des variables indépendantes, l'entropie conjointe $H(X,Y)$ s'additionne parfaitement ($H(X)+H(Y)$), entraînant $I(X;Y) = 0$, reflétant qu'aucune connaissance sur $X$ ne réduit l'incertitude sur $Y$.
