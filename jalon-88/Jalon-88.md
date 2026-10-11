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

## 1. Genèse et Intuition Physique

L'indépendance est le pilier central sur lequel repose toute la théorie des probabilités et la statistique moderne. Historiquement, les premiers mathématiciens comme Blaise Pascal et Pierre de Fermat (vers 1654), lors de leur correspondance sur le problème des partis, manipulaient déjà de manière implicite l'indépendance des lancers de dés successifs. Plus tard, au début du XXe siècle, Andrey Kolmogorov a formalisé ce concept de manière rigoureuse dans son système axiomatique.

Le sens profond de l'indépendance est l'absence d'information mutuelle. Si deux expériences physiques sont indépendantes, observer le résultat de la première ne modifie absolument pas notre prédiction quant au résultat de la seconde.

En physique statistique, l'indépendance microscopique (les particules d'un gaz parfait n'interagissent pas) donne naissance à des lois macroscopiques déterministes (thermodynamique). Géométriquement, l'indépendance se traduit par l'orthogonalité des variables dans des espaces de Hilbert appropriés (pour des variables centrées).

## 2. Définitions, Théorèmes et Exemples

### A. Indépendance de deux événements

**Définition 1 :** Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace probabilisé. Deux événements $A, B \in \mathcal{F}$ sont dits **indépendants** par rapport à $\mathbb{P}$ si :
$$ \mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B) $$

*Exemple Concret 1 :*
Considérons le lancer d'un dé équilibré à 6 faces. $\Omega = \{1, 2, 3, 4, 5, 6\}$, $\mathcal{F} = \mathcal{P}(\Omega)$, et $\mathbb{P}$ la probabilité uniforme.
Soit $A$ = "Obtenir un résultat pair" = $\{2, 4, 6\}$. $\mathbb{P}(A) = 3/6 = 1/2$.
Soit $B$ = "Obtenir un multiple de 3" = $\{3, 6\}$. $\mathbb{P}(B) = 2/6 = 1/3$.
L'événement $A \cap B$ = "Obtenir un nombre pair et multiple de 3" = $\{6\}$.
$\mathbb{P}(A \cap B) = 1/6$.
Calculons le produit : $\mathbb{P}(A) \times \mathbb{P}(B) = (1/2) \times (1/3) = 1/6$.
Donc $\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)$. Les événements $A$ et $B$ sont indépendants.

*Contre-exemple 1 (Cas limite) :*
Soit $A$ = "Obtenir un résultat pair" = $\{2, 4, 6\}$. $\mathbb{P}(A) = 1/2$.
Soit $C$ = "Obtenir un multiple de 2" = $\{2, 4, 6\}$. $\mathbb{P}(C) = 1/2$.
$A \cap C = \{2, 4, 6\}$. $\mathbb{P}(A \cap C) = 1/2$.
$\mathbb{P}(A) \times \mathbb{P}(C) = 1/4 \neq 1/2$. Les événements ne sont pas indépendants.

### B. Indépendance d'une famille d'événements

L'indépendance deux à deux n'implique pas l'indépendance mutuelle d'une collection plus grande.

**Définition 2 :** Une famille d'événements $(A_i)_{i \in I}$ est dite **mutuellement indépendante** si pour toute sous-famille finie $J \subset I$, on a :
$$ \mathbb{P}\left(\bigcap_{j \in J} A_j\right) = \prod_{j \in J} \mathbb{P}(A_j) $$

*Exemple Concret 2 : (Indépendance 2 à 2 vs Mutuelle)*
On lance deux pièces de monnaie équilibrées de manière indépendante. $\Omega = \{PP, PF, FP, FF\}$ avec probabilité $1/4$ pour chaque événement élémentaire.
Soit $A$ : "La 1ère pièce fait Pile" = $\{PP, PF\}$, $\mathbb{P}(A) = 1/2$.
Soit $B$ : "La 2ème pièce fait Pile" = $\{PP, FP\}$, $\mathbb{P}(B) = 1/2$.
Soit $C$ : "Les deux pièces donnent le même résultat" = $\{PP, FF\}$, $\mathbb{P}(C) = 1/2$.
Vérifions l'indépendance deux à deux :
$\mathbb{P}(A \cap B) = \mathbb{P}(\{PP\}) = 1/4 = \mathbb{P}(A)\mathbb{P}(B)$.
$\mathbb{P}(A \cap C) = \mathbb{P}(\{PP\}) = 1/4 = \mathbb{P}(A)\mathbb{P}(C)$.
$\mathbb{P}(B \cap C) = \mathbb{P}(\{PP\}) = 1/4 = \mathbb{P}(B)\mathbb{P}(C)$.
Les événements sont indépendants deux à deux.
Cependant, pour les trois événements en même temps :
$\mathbb{P}(A \cap B \cap C) = \mathbb{P}(\{PP\}) = 1/4$.
Mais $\mathbb{P}(A)\mathbb{P}(B)\mathbb{P}(C) = (1/2)^3 = 1/8 \neq 1/4$.
La famille $\{A, B, C\}$ **n'est pas** mutuellement indépendante.

### C. Indépendance de tribus

**Définition 3 :** Deux tribus (ou $\sigma$-algèbres) $\mathcal{A}$ et $\mathcal{B}$, sous-tribus de $\mathcal{F}$, sont dites **indépendantes** si pour tout $A \in \mathcal{A}$ et pour tout $B \in \mathcal{B}$, les événements $A$ et $B$ sont indépendants, c'est-à-dire :
$$ \forall A \in \mathcal{A}, \forall B \in \mathcal{B}, \mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B) $$

### D. Indépendance de variables aléatoires

Rappelons que la tribu engendrée par une variable aléatoire $X$, notée $\sigma(X)$, est la plus petite tribu rendant $X$ mesurable. C'est l'information générée par $X$.

**Définition 4 :** Deux variables aléatoires réelles $X$ et $Y$ définies sur le même espace probabilisé $(\Omega, \mathcal{F}, \mathbb{P})$ sont **indépendantes** si les tribus qu'elles engendrent, $\sigma(X)$ et $\sigma(Y)$, sont indépendantes.
De manière équivalente, pour tout choix de boréliens $B_1, B_2 \in \mathcal{B}(\mathbb{R})$ :
$$ \mathbb{P}(X \in B_1, Y \in B_2) = \mathbb{P}(X \in B_1)\mathbb{P}(Y \in B_2) $$

*Exemple Concret 3 : (Variables indicatrices)*
Soit $A$ et $B$ deux événements indépendants de probabilité non nulle ou un.
Considérons les variables aléatoires $X = \mathbb{1}_A$ et $Y = \mathbb{1}_B$.
Calculons la loi du couple $(X,Y)$. Les valeurs possibles sont $\{0,1\}^2$.
- $\mathbb{P}(X=1, Y=1) = \mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B) = \mathbb{P}(X=1)\mathbb{P}(Y=1)$ (car $A$ et $B$ sont indépendants).
- $\mathbb{P}(X=1, Y=0) = \mathbb{P}(A \cap B^c)$. Or $A = (A \cap B) \cup (A \cap B^c)$, union disjointe. Donc $\mathbb{P}(A) = \mathbb{P}(A \cap B) + \mathbb{P}(A \cap B^c)$. Ainsi, $\mathbb{P}(A \cap B^c) = \mathbb{P}(A) - \mathbb{P}(A)\mathbb{P}(B) = \mathbb{P}(A)(1 - \mathbb{P}(B)) = \mathbb{P}(A)\mathbb{P}(B^c) = \mathbb{P}(X=1)\mathbb{P}(Y=0)$.
Les calculs sont analogues pour les autres cas. Les variables aléatoires indicatrices sont donc indépendantes.

**Théorème 1 (Caractérisation par la fonction de répartition) :**
Deux variables aléatoires réelles $X$ et $Y$ sont indépendantes si et seulement si pour tout $x, y \in \mathbb{R}$ :
$$ F_{X,Y}(x,y) = F_X(x)F_Y(y) $$
où $F_{X,Y}(x,y) = \mathbb{P}(X \leq x, Y \leq y)$ est la fonction de répartition conjointe.

*Exemple Concret 4 : (Loi Exponentielle Bivariée de Gumbel)*
Soit la fonction de répartition conjointe $F_{X,Y}(x,y) = (1-e^{-x})(1-e^{-y})$ pour $x>0, y>0$, et $0$ sinon.
Les densités marginales s'obtiennent par limite :
$F_X(x) = \lim_{y \to +\infty} F_{X,Y}(x,y) = 1-e^{-x}$ (pour $x>0$).
$F_Y(y) = \lim_{x \to +\infty} F_{X,Y}(x,y) = 1-e^{-y}$ (pour $y>0$).
On constate que $F_{X,Y}(x,y) = F_X(x)F_Y(y)$ pour tout $x,y$. Les variables $X$ et $Y$ sont donc des lois exponentielles standard indépendantes.

### E. Lemme des coalitions

**Théorème 2 (Lemme des coalitions) :**
Si les variables aléatoires $X_1, X_2, \dots, X_n$ sont mutuellement indépendantes, et si on partitionne l'ensemble des indices $\{1, \dots, n\}$ en sous-ensembles disjoints $I_1, I_2, \dots, I_k$, alors toute fonction mesurable $f_j$ de la famille de variables aléatoires associées à $I_j$ crée une nouvelle famille de variables aléatoires $Y_1, \dots, Y_k$ (où $Y_j = f_j((X_i)_{i \in I_j})$) qui sont mutuellement indépendantes.

*Exemple Concret 5 :*
Si $X_1, X_2, X_3, X_4$ sont 4 variables indépendantes. Alors $Y_1 = X_1 + X_2$ et $Y_2 = X_3 X_4$ sont des variables aléatoires indépendantes. La coalition des blocs disjoints maintient l'indépendance.

### F. Indépendance, Espérance et Variance

**Théorème 3 (Espérance du produit) :**
Soient $X$ et $Y$ deux variables aléatoires réelles indépendantes et intégrables (c.-à-d. admettant une espérance). Alors le produit $XY$ est intégrable et on a :
$$ \mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y] $$

*Exemple Concret 6 : (Covariance nulle)*
Soit $X$ suivant une loi Normale standard $\mathcal{N}(0,1)$, donc $\mathbb{E}[X]=0$.
Soit $Y$ suivant une loi Normale standard $\mathcal{N}(0,1)$, indépendante de $X$.
Calculons la covariance : $\text{Cov}(X,Y) = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]$.
Par indépendance, $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y] = 0 \times 0 = 0$.
Donc $\text{Cov}(X,Y) = 0$.
Attention à la réciproque fausse : si $X \sim \mathcal{N}(0,1)$ et $Y = X^2$, alors $Y$ n'est absolument pas indépendante de $X$. Pourtant $\mathbb{E}[XY] = \mathbb{E}[X^3] = 0$ (moment impair d'une gaussienne centrée), et $\mathbb{E}[X]\mathbb{E}[Y] = 0 \times 1 = 0$. Donc $\text{Cov}(X,Y) = 0$, bien que $X$ et $Y$ soient fortement dépendantes. L'indépendance est donc une condition suffisante mais pas nécessaire pour une covariance nulle.

**Théorème 4 (Variance de la somme - Identité de Bienaymé) :**
Si $X$ et $Y$ sont deux variables aléatoires indépendantes et de carré intégrable, alors :
$$ \text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) $$

*Exemple Concret 7 :*
Soit $X_1 \sim \text{Poisson}(\lambda_1)$ et $X_2 \sim \text{Poisson}(\lambda_2)$ indépendantes.
$\text{Var}(X_1) = \lambda_1$ et $\text{Var}(X_2) = \lambda_2$.
$\text{Var}(X_1 + X_2) = \text{Var}(X_1) + \text{Var}(X_2) = \lambda_1 + \lambda_2$.
(Ceci est cohérent avec le fait que $X_1 + X_2 \sim \text{Poisson}(\lambda_1 + \lambda_2)$).

### G. Densités et Indépendance

**Théorème 5 (Variables à densité) :**
Soit $(X, Y)$ un couple de variables aléatoires réelles admettant une densité conjointe $f_{X,Y}(x,y)$ par rapport à la mesure de Lebesgue sur $\mathbb{R}^2$.
Les variables $X$ et $Y$ sont indépendantes si et seulement si, presque partout (pour la mesure de Lebesgue) :
$$ f_{X,Y}(x,y) = f_X(x) f_Y(y) $$
où $f_X$ et $f_Y$ sont les densités marginales respectives.

*Exemple Concret 8 :*
Soit le vecteur aléatoire $(X,Y)$ de densité conjointe $f_{X,Y}(x,y) = \frac{1}{2\pi} e^{-\frac{x^2+y^2}{2}}$ sur $\mathbb{R}^2$.
On peut écrire $f_{X,Y}(x,y) = \left( \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}} \right) \left( \frac{1}{\sqrt{2\pi}} e^{-\frac{y^2}{2}} \right) = f_X(x) f_Y(y)$.
Les marginales $f_X(x) = \int_{\mathbb{R}} f_{X,Y}(x,y) dy = \frac{1}{\sqrt{2\pi}} e^{-\frac{x^2}{2}}$ sont bien celles de lois Normales standards centrées réduites. Puisque la densité conjointe factorise en produit des densités marginales, $X$ et $Y$ sont indépendantes.

## 3. Démonstrations

### Démonstration du Théorème 3 : $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$ pour $X, Y$ indépendantes

**Étape 1 : Cas des fonctions indicatrices**
Supposons que $X = \mathbb{1}_A$ et $Y = \mathbb{1}_B$ où $A \in \mathcal{F}$ et $B \in \mathcal{F}$ sont des événements indépendants.
La variable $XY = \mathbb{1}_A \mathbb{1}_B = \mathbb{1}_{A \cap B}$.
Par définition de l'espérance pour les fonctions indicatrices :
$$ \mathbb{E}[XY] = \mathbb{P}(A \cap B) $$
Par hypothèse d'indépendance de $A$ et $B$ :
$$ \mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B) = \mathbb{E}[\mathbb{1}_A]\mathbb{E}[\mathbb{1}_B] = \mathbb{E}[X]\mathbb{E}[Y] $$
La relation est donc vraie pour les indicatrices d'événements indépendants.

**Étape 2 : Cas des variables étagées positives**
Soient $X$ et $Y$ deux variables aléatoires étagées positives et indépendantes.
On peut les écrire sous la forme normale :
$$ X = \sum_{i=1}^n x_i \mathbb{1}_{A_i} $$
$$ Y = \sum_{j=1}^m y_j \mathbb{1}_{B_j} $$
où les ensembles $(A_i)_{1 \leq i \leq n}$ forment une partition de $\Omega$, de même pour $(B_j)_{1 \leq j \leq m}$, et par indépendance de $X$ et $Y$, pour tous $i, j$, les événements $A_i = \{X = x_i\}$ et $B_j = \{Y = y_j\}$ sont indépendants.
Le produit s'écrit :
$$ XY = \left(\sum_{i=1}^n x_i \mathbb{1}_{A_i}\right) \left(\sum_{j=1}^m y_j \mathbb{1}_{B_j}\right) = \sum_{i=1}^n \sum_{j=1}^m x_i y_j \mathbb{1}_{A_i} \mathbb{1}_{B_j} = \sum_{i=1}^n \sum_{j=1}^m x_i y_j \mathbb{1}_{A_i \cap B_j} $$
Par linéarité de l'espérance :
$$ \mathbb{E}[XY] = \sum_{i=1}^n \sum_{j=1}^m x_i y_j \mathbb{E}[\mathbb{1}_{A_i \cap B_j}] $$
En utilisant le résultat de l'étape 1 :
$$ \mathbb{E}[XY] = \sum_{i=1}^n \sum_{j=1}^m x_i y_j \mathbb{E}[\mathbb{1}_{A_i}] \mathbb{E}[\mathbb{1}_{B_j}] $$
On factorise :
$$ \mathbb{E}[XY] = \left( \sum_{i=1}^n x_i \mathbb{E}[\mathbb{1}_{A_i}] \right) \left( \sum_{j=1}^m y_j \mathbb{E}[\mathbb{1}_{B_j}] \right) = \mathbb{E}[X]\mathbb{E}[Y] $$
La relation est donc vraie pour les variables étagées positives.

**Étape 3 : Cas des variables aléatoires positives quelconques (par convergence monotone)**
Soient $X, Y \geq 0$ deux variables aléatoires indépendantes.
Il existe deux suites croissantes $(X_n)_{n \in \mathbb{N}}$ et $(Y_n)_{n \in \mathbb{N}}$ de variables étagées positives telles que :
$X_n \uparrow X$ et $Y_n \uparrow Y$ presque sûrement.
Pour chaque $n$, $X_n$ est une fonction mesurable de $X$, et $Y_n$ de $Y$. D'après le lemme des coalitions, $X_n$ et $Y_n$ sont indépendantes pour chaque $n$.
D'après l'étape 2 : $\mathbb{E}[X_n Y_n] = \mathbb{E}[X_n]\mathbb{E}[Y_n]$.
La suite $(X_n Y_n)_{n \in \mathbb{N}}$ est une suite croissante de variables positives qui converge presque sûrement vers $XY$.
D'après le théorème de convergence monotone de Beppo-Levi (Jalon 67) :
$$ \lim_{n \to \infty} \mathbb{E}[X_n Y_n] = \mathbb{E}[XY] $$
D'autre part, en appliquant à nouveau le TCM aux suites $(X_n)$ et $(Y_n)$ :
$$ \lim_{n \to \infty} \mathbb{E}[X_n] = \mathbb{E}[X] $$
$$ \lim_{n \to \infty} \mathbb{E}[Y_n] = \mathbb{E}[Y] $$
En passant à la limite dans $\mathbb{E}[X_n Y_n] = \mathbb{E}[X_n]\mathbb{E}[Y_n]$, on obtient :
$$ \mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y] $$

**Étape 4 : Cas général (décomposition en parties positive et négative)**
Pour $X$ et $Y$ intégrables et indépendantes de signe quelconque.
On décompose $X = X^+ - X^-$ et $Y = Y^+ - Y^-$, où $X^+, X^-, Y^+, Y^-$ sont positives et intégrables.
Par le lemme des coalitions, la famille $\{X^+, X^-\}$ est indépendante de la famille $\{Y^+, Y^-\}$.
Le produit s'écrit $XY = (X^+ - X^-)(Y^+ - Y^-) = X^+ Y^+ - X^+ Y^- - X^- Y^+ + X^- Y^-$.
Par linéarité de l'espérance (valable pour des sommes de variables intégrables) :
$$ \mathbb{E}[XY] = \mathbb{E}[X^+ Y^+] - \mathbb{E}[X^+ Y^-] - \mathbb{E}[X^- Y^+] + \mathbb{E}[X^- Y^-] $$
Puisque chaque terme est le produit de deux variables positives indépendantes, on applique l'étape 3 :
$$ \mathbb{E}[XY] = \mathbb{E}[X^+]\mathbb{E}[Y^+] - \mathbb{E}[X^+]\mathbb{E}[Y^-] - \mathbb{E}[X^-]\mathbb{E}[Y^+] + \mathbb{E}[X^-]\mathbb{E}[Y^-] $$
On factorise :
$$ \mathbb{E}[XY] = (\mathbb{E}[X^+] - \mathbb{E}[X^-])(\mathbb{E}[Y^+] - \mathbb{E}[Y^-]) = \mathbb{E}[X]\mathbb{E}[Y] $$
La démonstration est ainsi complète et rigoureuse.

## 4. Applications en Physique, Logique et Intelligence Artificielle

### En Physique : Mécanique Statistique et Gaz Idéal
L'hypothèse d'indépendance est au cœur de la distribution de Maxwell-Boltzmann décrivant un gaz idéal. Si l'on suppose qu'une particule est dans un état non influencé par les autres, l'entropie globale du système $S = k_B \ln(W)$ repose sur le fait que le nombre de micro-états $W$ d'un système composite constitué de sous-systèmes indépendants est le produit des micro-états des sous-systèmes, transformant ainsi la probabilité jointe (produit) en une grandeur thermodynamique additive (la somme, via le logarithme).

### En Logique et Théorie de l'Information
Dans la théorie de l'information de Claude Shannon, la quantité d'information apportée par l'observation simultanée de deux événements indépendants $A$ et $B$ est strictement la somme des informations individuelles. En posant $I(A) = - \log_2 \mathbb{P}(A)$, l'indépendance $\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B)$ entraîne immédiatement $I(A \cap B) = I(A) + I(B)$. C'est le socle du codage source, car si les symboles générés par une source sont indépendants, aucun taux de compression n'est possible en exploitant les corrélations entre les symboles.

### En Intelligence Artificielle : Le paradigme I.I.D. et le classifieur Naive Bayes
L'ensemble de l'apprentissage statistique repose sur l'hypothèse que les données d'entraînement composant notre dataset $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^N$ sont tirées de manière **Indépendante et Identiquement Distribuée (i.i.d.)** depuis la loi jointe réelle $\mathcal{P}_{X,Y}$. Cette hypothèse d'indépendance permet à la fonction de risque empirique $\hat{R}(\theta) = \frac{1}{N} \sum_{i=1}^N \mathcal{L}(y_i, f_\theta(x_i))$ d'être un estimateur sans biais du risque véritable, convergent grâce à la loi des grands nombres.

Un cas d'application explicite est le **Classifieur Naive Bayes**. Pour estimer $\mathbb{P}(Y | X_1, \dots, X_p)$ en grande dimension $p$, on utilise la règle de Bayes : $\mathbb{P}(Y | X) = \frac{\mathbb{P}(X | Y)\mathbb{P}(Y)}{\mathbb{P}(X)}$.
L'astuce "naïve" consiste à poser l'hypothèse très forte que, *conditionnellement à la classe $Y$*, les caractéristiques $X_1, \dots, X_p$ sont mutuellement indépendantes.
Ainsi, la vraisemblance conjointe complexe se factorise de manière triviale :
$$ \mathbb{P}(X_1, \dots, X_p | Y) = \prod_{j=1}^p \mathbb{P}(X_j | Y) $$
Cette factorisation grâce à l'indépendance transforme un problème d'estimation d'une densité de dimension $p$ (sujet au fléau de la dimension nécessitant des données exponentielles en taille) en $p$ problèmes unidimensionnels distincts, ce qui rend l'algorithme extrêmement robuste et rapide, justifiant son utilisation massive, notamment dans les filtres anti-spam.
