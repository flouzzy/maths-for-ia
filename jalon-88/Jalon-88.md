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

## 1. Introduction : La mesure de l'absence d'influence

L'émergence du concept d'indépendance en probabilités est intrinsèquement liée à la formalisation des jeux de hasard et à l'analyse de séquences d'événements répétitifs. Historiquement, des mathématiciens comme Blaise Pascal, Pierre de Fermat ou Christiaan Huygens manipulaient intuitivement cette notion sans disposer d'un formalisme rigoureux. L'idée physique sous-jacente est celle d'une absence d'influence causale ou informationnelle : la réalisation d'un phénomène ne modifie en rien la vraisemblance de l'occurrence d'un autre phénomène.

Ce n'est qu'avec l'axiomatisation de Kolmogorov au début du XXe siècle que l'indépendance trouve sa définition mathématique stricte, s'inscrivant naturellement dans le cadre de la théorie de la mesure. Au-delà de la simple définition ensembliste, l'indépendance permet de structurer les espaces de probabilité complexes par des constructions produits, réduisant l'étude de lois multivariées à celle de leurs composantes marginales. L'importance de ce concept est capitale : il constitue la pierre angulaire des grands théorèmes limites (Loi Forte des Grands Nombres, Théorème Central Limite) et fonde l'hypothèse majeure (i.i.d.) sur laquelle repose la quasi-totalité de la théorie de l'apprentissage statistique.

## 2. Formalisation, structures et exemples concrets

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace probabilisé.

### A. Indépendance de deux événements

> **Définition (Indépendance de deux événements) :**
> Deux événements $A, B \in \mathcal{F}$ sont dits **indépendants** vis-à-vis de la mesure de probabilité $\mathbb{P}$ si :
> $$ \mathbb{P}(A \cap B) = \mathbb{P}(A) \mathbb{P}(B) $$

Si $\mathbb{P}(B) > 0$, cette définition équivaut à affirmer que la probabilité conditionnelle de $A$ sachant $B$ est égale à la probabilité a priori de $A$ : $\mathbb{P}(A|B) = \mathbb{P}(A)$. La survenue de $B$ n'apporte donc aucune information permettant de réviser la probabilité de $A$.

**Exemple concret calculatoire :**
Considérons le jet de deux dés équilibrés à 6 faces. L'univers est $\Omega = \{1, 2, 3, 4, 5, 6\}^2$, muni de la tribu $\mathcal{F} = \mathcal{P}(\Omega)$ et de la probabilité uniforme $\mathbb{P}$.
Soient les événements :
- $A$ : "Le premier dé donne un résultat pair", $A = \{(x,y) \in \Omega \mid x \in \{2, 4, 6\}\}$
- $B$ : "La somme des deux dés vaut 7", $B = \{(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\}$

On a $\mathbb{P}(A) = \frac{18}{36} = \frac{1}{2}$ et $\mathbb{P}(B) = \frac{6}{36} = \frac{1}{6}$.
L'intersection est $A \cap B = \{(2,5), (4,3), (6,1)\}$. Sa probabilité est $\mathbb{P}(A \cap B) = \frac{3}{36} = \frac{1}{12}$.
On vérifie bien que $\mathbb{P}(A \cap B) = \frac{1}{12} = \frac{1}{2} \times \frac{1}{6} = \mathbb{P}(A) \mathbb{P}(B)$. Les événements $A$ et $B$ sont indépendants.

### B. Indépendance mutuelle d'une famille d'événements

La généralisation à plus de deux événements requiert une précaution majeure.

> **Définition (Indépendance mutuelle) :**
> Une famille d'événements $(A_i)_{i \in I}$ (où $I$ est un ensemble quelconque d'indices) est dite **mutuellement indépendante** si, pour toute partie finie non vide $J \subset I$, on a :
> $$ \mathbb{P}\left(\bigcap_{j \in J} A_j\right) = \prod_{j \in J} \mathbb{P}(A_j) $$

**Remarque fondamentale et contre-exemple (Indépendance deux à deux) :**
L'indépendance mutuelle est une propriété strictement plus forte que l'indépendance deux à deux.
Considérons une urne contenant quatre boules numérotées 1, 2, 3 et 4, tirées de manière équiprobable.
Soient les événements :
- $A = \{1, 2\}$
- $B = \{1, 3\}$
- $C = \{1, 4\}$

On a $\mathbb{P}(A) = \mathbb{P}(B) = \mathbb{P}(C) = \frac{1}{2}$.
On vérifie aisément que $\mathbb{P}(A \cap B) = \mathbb{P}(\{1\}) = \frac{1}{4} = \mathbb{P}(A)\mathbb{P}(B)$. De même pour $A$ et $C$, et pour $B$ et $C$. Les événements sont indépendants deux à deux.
Cependant, $\mathbb{P}(A \cap B \cap C) = \mathbb{P}(\{1\}) = \frac{1}{4}$, tandis que $\mathbb{P}(A)\mathbb{P}(B)\mathbb{P}(C) = \frac{1}{8}$.
L'égalité $\mathbb{P}(A \cap B \cap C) = \mathbb{P}(A)\mathbb{P}(B)\mathbb{P}(C)$ n'est pas vérifiée. La famille $\{A, B, C\}$ n'est donc pas mutuellement indépendante.

### C. Indépendance de tribus et de variables aléatoires

> **Définition (Indépendance de tribus) :**
> Soit une famille $(\mathcal{A}_i)_{i \in I}$ de sous-tribus de $\mathcal{F}$. Cette famille est **indépendante** si, pour tout choix d'événements $(A_i)_{i \in I}$ tels que $A_i \in \mathcal{A}_i$ pour tout $i$, la famille d'événements $(A_i)_{i \in I}$ est mutuellement indépendante.

L'indépendance des variables aléatoires découle naturellement de celle des tribus qu'elles engendrent.

> **Définition (Indépendance de variables aléatoires) :**
> Soit une famille $(X_i)_{i \in I}$ de variables aléatoires définies sur $(\Omega, \mathcal{F}, \mathbb{P})$, à valeurs dans des espaces mesurables $(E_i, \mathcal{E}_i)$. Elles sont dites **indépendantes** si les tribus qu'elles engendrent, $\sigma(X_i) = \{ X_i^{-1}(B_i) \mid B_i \in \mathcal{E}_i \}$, sont indépendantes.

De manière opérationnelle, pour une famille finie $(X_1, \ldots, X_n)$, cela signifie que pour toute famille de boréliens $B_1 \in \mathcal{E}_1, \ldots, B_n \in \mathcal{E}_n$, on a :
$$ \mathbb{P}(X_1 \in B_1, \ldots, X_n \in B_n) = \prod_{k=1}^n \mathbb{P}(X_k \in B_k) $$

### D. Le Lemme de regroupement (Coalition Lemma)

> **Lemme (Regroupement) :**
> Soit $(X_1, \ldots, X_n)$ des variables aléatoires indépendantes. Si l'on partitionne cet ensemble en plusieurs paquets disjoints, alors toute fonction mesurable appliquée aux paquets respectifs produit de nouvelles variables aléatoires qui restent indépendantes.
> Par exemple, si $X_1, X_2, X_3, X_4$ sont indépendantes, et si $f$ et $g$ sont boréliennes, alors $Y = f(X_1, X_2)$ et $Z = g(X_3, X_4)$ sont indépendantes.

## 3. Démonstrations rigoureuses

### Théorème 1 : Indépendance et espérance d'un produit

> **Théorème :**
> Soient $X$ et $Y$ deux variables aléatoires réelles indépendantes sur $(\Omega, \mathcal{F}, \mathbb{P})$. Si $X$ et $Y$ sont intégrables (ou si elles sont presque sûrement positives), alors leur produit $XY$ est intégrable (resp. d'espérance bien définie) et :
> $$ \mathbb{E}[XY] = \mathbb{E}[X] \mathbb{E}[Y] $$

**Démonstration exhaustive :**

La démonstration se fonde sur l'approche standard en théorie de l'intégration, en procédant par étapes selon la nature des variables.

**Étape 1 : Cas des fonctions indicatrices.**
Supposons qu'il existe $A, B \in \mathcal{F}$ tels que $X = \mathbf{1}_A$ et $Y = \mathbf{1}_B$.
Puisque $X$ et $Y$ sont indépendantes, les événements $A$ et $B$ sont indépendants (car $A \in \sigma(X)$ et $B \in \sigma(Y)$).
On calcule directement :
$$ \mathbb{E}[XY] = \mathbb{E}[\mathbf{1}_A \mathbf{1}_B] = \mathbb{E}[\mathbf{1}_{A \cap B}] = \mathbb{P}(A \cap B) $$
Par indépendance de $A$ et $B$ :
$$ \mathbb{P}(A \cap B) = \mathbb{P}(A) \mathbb{P}(B) = \mathbb{E}[\mathbf{1}_A] \mathbb{E}[\mathbf{1}_B] = \mathbb{E}[X] \mathbb{E}[Y] $$

**Étape 2 : Cas des variables étagées positives.**
Supposons $X = \sum_{i=1}^n x_i \mathbf{1}_{A_i}$ et $Y = \sum_{j=1}^m y_j \mathbf{1}_{B_j}$, avec $x_i, y_j \ge 0$, les $A_i$ formant une partition $\sigma(X)$-mesurable et les $B_j$ une partition $\sigma(Y)$-mesurable.
Leur produit s'écrit :
$$ XY = \left( \sum_{i=1}^n x_i \mathbf{1}_{A_i} \right) \left( \sum_{j=1}^m y_j \mathbf{1}_{B_j} \right) = \sum_{i=1}^n \sum_{j=1}^m x_i y_j \mathbf{1}_{A_i} \mathbf{1}_{B_j} = \sum_{i=1}^n \sum_{j=1}^m x_i y_j \mathbf{1}_{A_i \cap B_j} $$
Par linéarité de l'espérance :
$$ \mathbb{E}[XY] = \sum_{i=1}^n \sum_{j=1}^m x_i y_j \mathbb{P}(A_i \cap B_j) $$
Puisque $A_i \in \sigma(X)$ et $B_j \in \sigma(Y)$ qui sont des tribus indépendantes, $\mathbb{P}(A_i \cap B_j) = \mathbb{P}(A_i)\mathbb{P}(B_j)$.
$$ \mathbb{E}[XY] = \sum_{i=1}^n \sum_{j=1}^m x_i y_j \mathbb{P}(A_i) \mathbb{P}(B_j) = \left( \sum_{i=1}^n x_i \mathbb{P}(A_i) \right) \left( \sum_{j=1}^m y_j \mathbb{P}(B_j) \right) = \mathbb{E}[X] \mathbb{E}[Y] $$

**Étape 3 : Cas des variables aléatoires positives intégrables.**
Soient $X, Y \ge 0$ mesurables. Par théorème d'approximation, il existe des suites croissantes $(X_n)_{n \in \mathbb{N}}$ et $(Y_n)_{n \in \mathbb{N}}$ de variables étagées positives convergeant ponctuellement vers $X$ et $Y$. De plus, $X_n$ est $\sigma(X)$-mesurable et $Y_n$ est $\sigma(Y)$-mesurable, elles sont donc indépendantes.
La suite $(X_n Y_n)_{n \in \mathbb{N}}$ est une suite croissante de variables aléatoires positives qui converge ponctuellement vers $XY$.
D'après le Théorème de Convergence Monotone (Beppo-Levi) :
$$ \mathbb{E}[XY] = \mathbb{E}\left[ \lim_{n \to \infty} (X_n Y_n) \right] = \lim_{n \to \infty} \mathbb{E}[X_n Y_n] $$
D'après l'Étape 2, $\mathbb{E}[X_n Y_n] = \mathbb{E}[X_n] \mathbb{E}[Y_n]$.
Puisque les suites $(\mathbb{E}[X_n])$ et $(\mathbb{E}[Y_n])$ sont convergentes (vers $\mathbb{E}[X]$ et $\mathbb{E}[Y]$ respectivement, encore par Beppo-Levi), la limite de leur produit est le produit de leurs limites :
$$ \lim_{n \to \infty} \mathbb{E}[X_n] \mathbb{E}[Y_n] = \left( \lim_{n \to \infty} \mathbb{E}[X_n] \right) \left( \lim_{n \to \infty} \mathbb{E}[Y_n] \right) = \mathbb{E}[X] \mathbb{E}[Y] $$
Ainsi, l'égalité est démontrée pour les variables positives.

**Étape 4 : Cas général des variables intégrables.**
Soient $X$ et $Y$ intégrables de signe quelconque. On décompose en parties positive et négative : $X = X^+ - X^-$ et $Y = Y^+ - Y^-$.
Les variables $X^+$ et $X^-$ sont $\sigma(X)$-mesurables, $Y^+$ et $Y^-$ sont $\sigma(Y)$-mesurables. Donc les paires $(X^+, Y^+)$, $(X^+, Y^-)$, $(X^-, Y^+)$, $(X^-, Y^-)$ sont formées de variables indépendantes et positives.
Le produit s'écrit :
$$ XY = (X^+ - X^-)(Y^+ - Y^-) = X^+ Y^+ - X^+ Y^- - X^- Y^+ + X^- Y^- $$
En prenant l'espérance de la valeur absolue :
$$ \mathbb{E}[|XY|] \le \mathbb{E}[X^+ Y^+] + \mathbb{E}[X^+ Y^-] + \mathbb{E}[X^- Y^+] + \mathbb{E}[X^- Y^-] $$
Par l'Étape 3, chaque terme est un produit d'espérances finies (puisque $X$ et $Y$ sont intégrables, leurs parties positives et négatives le sont aussi). La somme est donc finie, ce qui prouve que $XY$ est intégrable.
Enfin, par linéarité de l'espérance et en appliquant l'Étape 3 à chaque terme :
$$ \mathbb{E}[XY] = \mathbb{E}[X^+]\mathbb{E}[Y^+] - \mathbb{E}[X^+]\mathbb{E}[Y^-] - \mathbb{E}[X^-]\mathbb{E}[Y^+] + \mathbb{E}[X^-]\mathbb{E}[Y^-] $$
En factorisant, on obtient bien :
$$ \mathbb{E}[XY] = (\mathbb{E}[X^+] - \mathbb{E}[X^-])(\mathbb{E}[Y^+] - \mathbb{E}[Y^-]) = \mathbb{E}[X] \mathbb{E}[Y] $$
La démonstration est complète. $\blacksquare$

### Corollaire : Somme de variances pour des variables indépendantes

> **Corollaire :**
> Si $X_1, \ldots, X_n$ sont des variables aléatoires indépendantes de carré intégrable, alors :
> $$ \text{Var}\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i) $$

**Démonstration :**
Rappelons que la covariance de deux variables $X$ et $Y$ est donnée par $\text{Cov}(X,Y) = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y]$.
Puisque $X$ et $Y$ sont indépendantes, $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$, donc $\text{Cov}(X,Y) = 0$. Les variables indépendantes sont non-corrélées.
On développe la variance de la somme :
$$ \text{Var}\left(\sum_{i=1}^n X_i\right) = \sum_{i=1}^n \text{Var}(X_i) + \sum_{1 \le i \neq j \le n} \text{Cov}(X_i, X_j) $$
Tous les termes de covariance étant nuls par indépendance croisée, il ne reste que la somme des variances. $\blacksquare$

## 4. Applications en Physique, Logique et Intelligence Artificielle

### L'hypothèse I.I.D. en Apprentissage Statistique
Le socle théorique du Machine Learning et des statistiques modernes repose presque exclusivement sur l'hypothèse que les données d'apprentissage $\mathcal{D} = \{(x_1, y_1), \ldots, (x_N, y_N)\}$ sont **I.I.D. (Indépendantes et Identiquement Distribuées)**.
L'indépendance mutuelle garantit que la fonction de vraisemblance conjointe (Likelihood) du jeu de données se factorise :
$$ L(\theta; \mathcal{D}) = \mathbb{P}_\theta(x_1, y_1, \ldots, x_N, y_N) = \prod_{i=1}^N \mathbb{P}_\theta(x_i, y_i) $$
En optimisant la log-vraisemblance (qui transforme le produit en somme), l'hypothèse d'indépendance permet l'utilisation d'algorithmes de descente de gradient stochastique (SGD), car l'espérance du gradient empirique correspond parfaitement à l'espérance du gradient réel, chaque point apportant une information non-redondante.

### Variational Autoencoders (VAE) et Indépendance Latente
Dans l'architecture des Autoencodeurs Variationnels, la distribution a priori (prior) de l'espace latent $Z \in \mathbb{R}^d$ est typiquement choisie comme une gaussienne standard isotrope : $\mathcal{N}(0, I_d)$.
La matrice de covariance identité $I_d$ stipule formellement que les dimensions latentes $Z_1, \ldots, Z_d$ sont indépendantes.
$$ \mathbb{P}(z_1, \ldots, z_d) = \prod_{j=1}^d \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{1}{2} z_j^2\right) $$
Cette indépendance structurelle contraint le réseau de neurones à apprendre des représentations *démêlées* (disentangled representations). En IA générative, modifier une composante latente (par exemple l'âge du visage généré) n'influencera pas les autres composantes (la couleur des cheveux, l'orientation du visage), grâce à l'indépendance imposée a priori.

### Régularisation par Dropout
Le Dropout est une technique cruciale de régularisation dans les réseaux de neurones profonds. Lors de chaque itération d'entraînement, on applique à chaque neurone $i$ un masque multiplicatif $M_i \sim \mathcal{B}(p)$ (loi de Bernoulli de paramètre $p$).
Les variables aléatoires $M_i$ sont tirées de manière **mutuellement indépendantes**.
Cette indépendance empêche la "co-adaptation" des neurones. Un neurone ne peut plus se reposer avec certitude sur la présence de ses voisins pour corriger ses propres erreurs. Il est forcé d'apprendre des caractéristiques robustes et généralisables par lui-même.
