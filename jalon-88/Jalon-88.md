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

## 1. Introduction à l'Indépendance Stochastique

L'idée d'indépendance trouve ses racines dans les premiers travaux sur les jeux de hasard, formalisés par Pascal, Fermat, et plus tard par Bernoulli, De Moivre, et Laplace. Historiquement, l'indépendance traduit une réalité physique fondamentale : l'absence de causalité ou d'influence mutuelle entre deux expériences distinctes. Si deux dés sont lancés simultanément à des kilomètres de distance, le résultat du premier n'a matériellement aucune influence sur le résultat du second.

La formalisation moderne de l'indépendance s'intègre naturellement dans l'axiomatique de Kolmogorov (1933). Dans ce cadre de théorie de la mesure, l'indépendance n'est plus seulement une intuition physique, mais une propriété purement algébrique sur la mesure de probabilité des intersections d'ensembles. L'indépendance permet de construire des modèles probabilistes complexes par composition d'expériences simples, justifiant des résultats fondamentaux tels que la Loi des Grands Nombres et le Théorème Central Limite. C'est l'outil mathématique par excellence pour lutter contre la "malédiction de la dimensionnalité", en réduisant l'étude de l'espace global à ses composantes marginales.

\begin{center}
\begin{tikzpicture}[scale=0.8]
  % Univers
  \draw[thick] (0,0) rectangle (8,5);
  \node at (0.3,4.7) {$\Omega$};

  % Event B
  \draw[thick, fill=blue!10] (2,2.5) circle (1.5);
  \node at (2,2.5) {$B$};

  % Event A
  \draw[thick, fill=red!10, fill opacity=0.7] (5,2.5) circle (1.5);
  \node at (5,2.5) {$A$};

  % Intersection empty (incompatible) vs Independent visualization
  % Let's draw an independent visualization
\end{tikzpicture}
\end{center}

Pour visualiser l'indépendance, on peut représenter l'espace des probabilités comme un carré de côté 1, où l'événement $A$ occupe une bande verticale de largeur $P(A)$ et l'événement $B$ une bande horizontale de hauteur $P(B)$. L'intersection $A \cap B$ forme un rectangle d'aire $P(A)P(B)$.

\begin{center}
\begin{tikzpicture}[scale=1]
  \draw[thick] (0,0) rectangle (4,4);
  \node at (-0.3, 4.3) {$\Omega$};

  % A (vertical band)
  \draw[thick, fill=red!20] (1,0) rectangle (2.5,4);
  \node at (1.75, 4.3) {$A$};

  % B (horizontal band)
  \draw[thick, fill=blue!20, opacity=0.5] (0,1) rectangle (4,3);
  \node at (-0.3, 2) {$B$};

  % Intersection
  \node at (1.75, 2) {$A \cap B$};

  % Labels
  \node at (1.75, -0.3) {$P(A)$};
  \node at (4.6, 2) {$P(B)$};
\end{tikzpicture}
\end{center}

## 2. Définitions, Théorèmes & Exemples

Soit $(\Omega, \mathcal{F}, P)$ un espace probabilisé.

### A. Indépendance d'Événements

> **Définition 1 : Indépendance de deux événements**
> Deux événements $A, B \in \mathcal{F}$ sont dits indépendants (pour la probabilité $P$) si :
> $$P(A \cap B) = P(A)P(B)$$

Si $P(B) > 0$, l'indépendance équivaut à affirmer que la probabilité conditionnelle $P(A|B) = \frac{P(A \cap B)}{P(B)}$ est égale à $P(A)$. Le fait que $B$ soit réalisé ne modifie pas la probabilité de réalisation de $A$.

**Exemple Concret 1 (Tirage de cartes) :**
On tire une carte au hasard dans un jeu de 52 cartes.
- $A$ : "La carte tirée est un As" $\implies P(A) = \frac{4}{52} = \frac{1}{13}$
- $B$ : "La carte tirée est un Cœur" $\implies P(B) = \frac{13}{52} = \frac{1}{4}$
- $A \cap B$ : "La carte tirée est l'As de Cœur" $\implies P(A \cap B) = \frac{1}{52}$
On vérifie que $P(A)P(B) = \frac{1}{13} \times \frac{1}{4} = \frac{1}{52} = P(A \cap B)$.
Les événements $A$ et $B$ sont indépendants. La proportion d'As parmi les cœurs est la même que la proportion d'As dans le jeu entier.

**Exemple Concret 2 (Indépendance vs Incompatibilité) :**
Deux événements $A$ et $B$ incompatibles (disjoints, $A \cap B = \emptyset$) et de probabilités non nulles ne sont *jamais* indépendants. En effet, $P(A \cap B) = 0$, mais $P(A)P(B) > 0$. Si $A$ se réalise, on a la certitude que $B$ ne s'est pas réalisé. Ils sont donc fortement dépendants.

> **Définition 2 : Mutuelle indépendance**
> Une famille d'événements $(A_i)_{i \in I}$ est mutuellement indépendante si pour toute sous-famille finie $J \subset I$ :
> $$P\left( \bigcap_{j \in J} A_j \right) = \prod_{j \in J} P(A_j)$$

**Exemple Concret 3 (Indépendance deux à deux $\neq$ mutuelle indépendance) :**
On lance deux pièces équilibrées indépendantes. $\Omega = \{(P,P), (P,F), (F,P), (F,F)\}$. Chaque issue a une probabilité de $1/4$.
- $A_1$ : "La première pièce donne Face" $\implies P(A_1) = 1/2$.
- $A_2$ : "La deuxième pièce donne Face" $\implies P(A_2) = 1/2$.
- $A_3$ : "Les deux pièces donnent le même résultat" $\implies \{(P,P), (F,F)\}$, $P(A_3) = 2/4 = 1/2$.
Vérifions l'indépendance deux à deux :
$P(A_1 \cap A_2) = P(\{(F,F)\}) = 1/4 = P(A_1)P(A_2)$.
$P(A_1 \cap A_3) = P(\{(F,F)\}) = 1/4 = P(A_1)P(A_3)$.
$P(A_2 \cap A_3) = P(\{(F,F)\}) = 1/4 = P(A_2)P(A_3)$.
Les événements sont indépendants deux à deux.
Cependant, pour l'intersection globale : $A_1 \cap A_2 \cap A_3 = \{(F,F)\}$, donc $P(A_1 \cap A_2 \cap A_3) = 1/4$.
Mais le produit donne $P(A_1)P(A_2)P(A_3) = 1/8 \neq 1/4$.
La famille n'est donc *pas* mutuellement indépendante.

### B. Indépendance de Tribus et de Variables Aléatoires

> **Définition 3 : Indépendance de tribus**
> Des tribus $\mathcal{B}_1, \ldots, \mathcal{B}_n$ incluses dans $\mathcal{F}$ sont indépendantes si pour tout choix d'événements $B_i \in \mathcal{B}_i$, la famille d'événements $(B_1, \ldots, B_n)$ est mutuellement indépendante.

> **Définition 4 : Indépendance de variables aléatoires**
> Des variables aléatoires $X_1, \ldots, X_n$ (à valeurs dans des espaces mesurables $(E_i, \mathcal{E}_i)$) sont indépendantes si les tribus qu'elles engendrent, $\sigma(X_i) = \{X_i^{-1}(B) \mid B \in \mathcal{E}_i\}$, sont indépendantes.
> De façon équivalente, pour tous boréliens $B_1, \ldots, B_n$ :
> $$P(X_1 \in B_1, \ldots, X_n \in B_n) = \prod_{i=1}^n P(X_i \in B_i)$$

**Exemple Concret 4 (Variables discrètes) :**
Soit $X$ et $Y$ deux variables de loi de Bernoulli de paramètre $p$ et $q$. Elles sont indépendantes si et seulement si pour tout $x,y \in \{0,1\}$, $P(X=x, Y=y) = P(X=x)P(Y=y)$.

**Exemple Concret 5 (Loi conjointe et produit tensoriel) :**
L'indépendance de $X$ et $Y$ signifie que la loi du couple $(X,Y)$ est la mesure produit des lois marginales : $P_{(X,Y)} = P_X \otimes P_Y$.
Si $X$ et $Y$ admettent des densités de probabilité respectives $f_X$ et $f_Y$, elles sont indépendantes si et seulement si la densité du couple $(X,Y)$ est donnée par le produit $f_{(X,Y)}(x,y) = f_X(x)f_Y(y)$ presque partout.

> **Théorème (Indépendance et Espérance) :**
> Soient $X$ et $Y$ deux variables aléatoires réelles indépendantes et intégrables (ou positives). Alors le produit $XY$ est intégrable (ou d'espérance bien définie) et :
> $$\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$$

**Exemple Concret 6 (Covariance nulle) :**
La covariance de $X$ et $Y$ est définie par $\text{Cov}(X,Y) = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]$. Si $X$ et $Y$ sont indépendantes, leur covariance est strictement nulle. Elles sont dites non corrélées.

**Exemple Concret 7 (Covariance nulle $\nRightarrow$ Indépendance) :**
Soit $X$ une variable uniformément distribuée sur $\{-1, 0, 1\}$, de sorte que $P(X=-1) = P(X=0) = P(X=1) = 1/3$. Soit $Y = X^2$. $Y$ prend les valeurs $\{0, 1\}$.
Évidemment, $X$ et $Y$ sont dépendantes (puisque $Y$ est une fonction déterministe de $X$).
Calculons la covariance. $XY = X^3 = X$.
$\mathbb{E}[X] = (-1) \cdot \frac{1}{3} + 0 \cdot \frac{1}{3} + 1 \cdot \frac{1}{3} = 0$.
Ainsi, $\mathbb{E}[XY] = \mathbb{E}[X] = 0$.
Par ailleurs, $\mathbb{E}[X]\mathbb{E}[Y] = 0 \cdot \mathbb{E}[Y] = 0$.
Donc $\text{Cov}(X,Y) = 0$, mais les variables ne sont pas indépendantes. L'absence de corrélation linéaire ne signifie pas l'absence de dépendance.

> **Théorème (Lemme des coalitions) :**
> Soit $(X_1, \ldots, X_n)$ des variables indépendantes. Soit $1 \le k < n$. Si $f$ et $g$ sont des fonctions mesurables, alors $Y = f(X_1, \ldots, X_k)$ et $Z = g(X_{k+1}, \ldots, X_n)$ sont des variables indépendantes.

## 3. Démonstrations

### Démonstration 1 : Indépendance et Produit des Espérances

**Théorème :** Si $X, Y$ sont deux variables aléatoires réelles indépendantes et intégrables, alors $XY$ est intégrable et $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$.

**Preuve pas à pas :**
Nous allons démontrer le théorème par étapes, en utilisant la construction standard de l'intégrale de Lebesgue : d'abord pour les indicatrices, puis les fonctions étagées, puis les fonctions mesurables positives, et enfin pour les fonctions intégrables.

**Étape 1 : Cas des indicatrices**
Supposons que $X = \mathbf{1}_A$ et $Y = \mathbf{1}_B$ avec $A$ et $B$ deux événements indépendants (puisque $X$ et $Y$ sont indépendantes).
Le produit $XY = \mathbf{1}_A \mathbf{1}_B = \mathbf{1}_{A \cap B}$.
L'espérance d'une indicatrice est la probabilité de l'événement associé :
$$\mathbb{E}[XY] = \mathbb{E}[\mathbf{1}_{A \cap B}] = P(A \cap B)$$
Par indépendance de $A$ et $B$ :
$$P(A \cap B) = P(A)P(B) = \mathbb{E}[\mathbf{1}_A]\mathbb{E}[\mathbf{1}_B] = \mathbb{E}[X]\mathbb{E}[Y]$$
Le résultat est établi pour les fonctions indicatrices.

**Étape 2 : Cas des fonctions étagées positives**
Soient $X$ et $Y$ deux variables étagées positives indépendantes. Elles s'écrivent $X = \sum_{i=1}^n x_i \mathbf{1}_{A_i}$ et $Y = \sum_{j=1}^m y_j \mathbf{1}_{B_j}$, où $(A_i)$ et $(B_j)$ sont des partitions de $\Omega$ formées d'événements respectivement générés par $X$ et $Y$. Comme $X$ et $Y$ sont indépendantes, pour tous $i, j$, les événements $A_i$ et $B_j$ sont indépendants.
Le produit s'écrit $XY = \sum_{i=1}^n \sum_{j=1}^m x_i y_j \mathbf{1}_{A_i \cap B_j}$.
Par linéarité de l'espérance :
$$\mathbb{E}[XY] = \sum_{i=1}^n \sum_{j=1}^m x_i y_j \mathbb{E}[\mathbf{1}_{A_i \cap B_j}] = \sum_{i=1}^n \sum_{j=1}^m x_i y_j P(A_i \cap B_j)$$
Par indépendance :
$$\mathbb{E}[XY] = \sum_{i=1}^n \sum_{j=1}^m x_i y_j P(A_i)P(B_j) = \left( \sum_{i=1}^n x_i P(A_i) \right) \left( \sum_{j=1}^m y_j P(B_j) \right) = \mathbb{E}[X]\mathbb{E}[Y]$$

**Étape 3 : Cas des fonctions mesurables positives**
Soient $X, Y \ge 0$ indépendantes. D'après le théorème d'approximation, il existe des suites croissantes de variables étagées positives $(X_n)_{n \in \mathbb{N}}$ et $(Y_n)_{n \in \mathbb{N}}$ convergeant respectivement vers $X$ et $Y$ presque sûrement.
Pour tout $n$, $X_n$ et $Y_n$ sont indépendantes, donc $\mathbb{E}[X_n Y_n] = \mathbb{E}[X_n]\mathbb{E}[Y_n]$.
Le produit $X_n Y_n$ est une suite croissante de variables positives convergeant vers $XY$.
D'après le Théorème de Convergence Monotone (Beppo-Levi) appliqué aux trois suites :
$$\mathbb{E}[XY] = \lim_{n \to \infty} \mathbb{E}[X_n Y_n] = \lim_{n \to \infty} \mathbb{E}[X_n]\mathbb{E}[Y_n]$$
Les limites des produits étant le produit des limites (lorsque celles-ci existent dans $\mathbb{R} \cup \{+\infty\}$) :
$$\mathbb{E}[XY] = \left(\lim_{n \to \infty} \mathbb{E}[X_n]\right) \left(\lim_{n \to \infty} \mathbb{E}[Y_n]\right) = \mathbb{E}[X]\mathbb{E}[Y]$$

**Étape 4 : Cas général (variables intégrables)**
Soient $X$ et $Y$ intégrables et indépendantes. On les décompose en leurs parties positives et négatives : $X = X^+ - X^-$ et $Y = Y^+ - Y^-$.
L'indépendance de $X$ et $Y$ implique (par le lemme des coalitions) l'indépendance des paires de variables positives $(X^+, Y^+)$, $(X^+, Y^-)$, $(X^-, Y^+)$, $(X^-, Y^-)$.
De plus :
$$|XY| = |X||Y| = (X^+ + X^-)(Y^+ + Y^-)$$
D'après l'étape 3, l'espérance de $|XY|$ est :
$$\mathbb{E}[|XY|] = \mathbb{E}[|X|]\mathbb{E}[|Y|]$$
Comme $X$ et $Y$ sont intégrables, $\mathbb{E}[|X|] < \infty$ et $\mathbb{E}[|Y|] < \infty$, ce qui prouve que $XY$ est intégrable (l'espérance de la valeur absolue est finie).
Enfin, par développement et linéarité de l'espérance :
$$\mathbb{E}[XY] = \mathbb{E}[(X^+ - X^-)(Y^+ - Y^-)] = \mathbb{E}[X^+Y^+] - \mathbb{E}[X^+Y^-] - \mathbb{E}[X^-Y^+] + \mathbb{E}[X^-Y^-]$$
Par l'étape 3 sur les parties positives indépendantes :
$$\mathbb{E}[XY] = \mathbb{E}[X^+]\mathbb{E}[Y^+] - \mathbb{E}[X^+]\mathbb{E}[Y^-] - \mathbb{E}[X^-]\mathbb{E}[Y^+] + \mathbb{E}[X^-]\mathbb{E}[Y^-]$$
Factorisons :
$$\mathbb{E}[XY] = (\mathbb{E}[X^+] - \mathbb{E}[X^-])(\mathbb{E}[Y^+] - \mathbb{E}[Y^-]) = \mathbb{E}[X]\mathbb{E}[Y]$$
La preuve est exhaustive et complète.

## 4. Applications en Mathématiques, Physique et Intelligence Artificielle

### A. Modélisation en Mécanique Statistique

En physique statistique, l'indépendance est au cœur de l'hypothèse du chaos moléculaire (Stosszahlansatz) introduite par Boltzmann pour dériver l'équation d'évolution d'un gaz. Elle postule que, avant une collision, les vitesses des deux particules sont des variables aléatoires indépendantes. C'est cette hypothèse d'indépendance microscopique qui permet de justifier l'émergence d'un comportement irréversible macroscopique (le second principe de la thermodynamique et le théorème H de Boltzmann) à partir de dynamiques microscopiques réversibles, en factorisant les fonctions de distribution des paires de particules.

### B. Hypothèse I.I.D. en Apprentissage Automatique

Le paradigme dominant en machine learning repose sur l'hypothèse I.I.D. (Indépendantes et Identiquement Distribuées). Un jeu de données d'apprentissage $\mathcal{D} = \{ (x_1, y_1), \ldots, (x_N, y_N) \}$ est vu comme une suite de réalisations de variables aléatoires indépendantes, toutes issues de la même distribution conjointe inconnue $P(X,Y)$.
L'indépendance est ce qui permet de définir la fonction de coût empirique et d'appliquer la Loi Forte des Grands Nombres. La fonction de vraisemblance, $L(\theta) = P(x_1, \ldots, x_N \mid \theta)$, se factorise grâce à l'indépendance :
$$L(\theta) = \prod_{i=1}^N P(x_i \mid \theta)$$
Le passage au logarithme (log-vraisemblance) transforme ce produit en somme, simplifiant drastiquement les calculs de gradients lors de la descente de gradient, puisque le gradient de la somme est la somme des gradients calculés sur chaque échantillon.

### C. Dropout dans les Réseaux de Neurones

Le Dropout est une technique de régularisation inventée pour réduire le surapprentissage dans les réseaux de neurones profonds. L'algorithme annule de manière aléatoire et *indépendante* l'activation de certains neurones pendant l'entraînement (par exemple avec une probabilité $p=0.5$). Cette indépendance forcée empêche les neurones de co-s'adapter (co-adaptation). Chaque sous-réseau échantillonné étant indépendant des autres itérations, le Dropout agit implicitement comme une méthode d'ensemble massique sur un très grand nombre de modèles exponentiellement différents.

### D. Algorithme de Naïve Bayes

Le classifieur de Bayes Naïf tire son nom de l'hypothèse (souvent "naïve" en pratique) que les différentes caractéristiques d'observation $X_1, \ldots, X_d$ sont *conditionnellement indépendantes* sachant la classe $Y$.
La règle de Bayes donne $P(Y=k \mid X_1, \ldots, X_d) \propto P(Y=k)P(X_1, \ldots, X_d \mid Y=k)$.
Par l'hypothèse d'indépendance conditionnelle, le terme complexe factorise :
$$P(X_1, \ldots, X_d \mid Y=k) = \prod_{j=1}^d P(X_j \mid Y=k)$$
Cela réduit un problème d'estimation d'une densité de dimension $d$ (souvent intraitable à cause du manque de données) à $d$ problèmes unidimensionnels triviaux à résoudre séparément.
