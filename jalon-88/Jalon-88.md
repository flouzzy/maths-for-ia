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

## 1. Introduction : Genèse historique et physique de l'indépendance

La notion d'indépendance est au cœur de la théorie des probabilités et trouve ses origines dans les jeux de hasard étudiés par Pascal et Fermat au XVIIe siècle. Historiquement, il s'agissait de formaliser l'intuition physique selon laquelle certains phénomènes n'ont aucune influence causale ou d'information les uns sur les autres.

Par exemple, considérons deux lancers successifs d'un dé parfait. Le résultat du premier lancer ne modifie en rien la configuration physique ni les conditions du second lancer. Si l'on obtient un « 6 » au premier lancer, cette information ne confère aucun avantage pour prédire le résultat du second lancer. L'indépendance traduit cette séparation absolue des informations. Mathématiquement, cela se traduit par une factorisation des probabilités, reflétant le fait que les événements se produisent simultanément selon le produit de leurs fréquences respectives d'apparition.

Cette factorisation est fondamentale car elle permet de décomposer l'étude de systèmes complexes en sous-systèmes simples et isolés. Sans cette notion, l'analyse probabiliste des grands systèmes (comme un gaz parfait en physique statistique ou un réseau de neurones en intelligence artificielle) serait incalculable.

## 2. Définitions, Théorèmes et Exemples

Soit $(\Omega, \mathcal{F}, \mathbb{P})$ un espace de probabilité.

### Indépendance de deux événements

**Définition (Indépendance de deux événements).** Deux événements $A, B \in \mathcal{F}$ sont dits indépendants par rapport à la probabilité $\mathbb{P}$ si :
$$ \mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B) $$
Si $\mathbb{P}(B) > 0$, cette définition équivaut à la probabilité conditionnelle : $\mathbb{P}(A|B) = \mathbb{P}(A)$.

**Exemple concret (Jet de deux dés).**
Lançons deux dés équilibrés à 6 faces. L'univers est $\Omega = \{1, 2, 3, 4, 5, 6\}^2$, de cardinal $36$, muni de la probabilité uniforme $\mathbb{P}$.
Considérons les événements :
- $A$ : "Le premier dé donne un nombre pair" = $\{(2,y), (4,y), (6,y) \mid y \in \{1..6\}\}$. On a $|A| = 18$, donc $\mathbb{P}(A) = \frac{18}{36} = \frac{1}{2}$.
- $B$ : "La somme des deux dés est 7" = $\{(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\}$. On a $|B| = 6$, donc $\mathbb{P}(B) = \frac{6}{36} = \frac{1}{6}$.
L'événement $A \cap B$ est l'ensemble des cas où le premier dé est pair ET la somme est 7 : $\{(2,5), (4,3), (6,1)\}$.
On a $|A \cap B| = 3$, donc $\mathbb{P}(A \cap B) = \frac{3}{36} = \frac{1}{12}$.
Calculons le produit : $\mathbb{P}(A) \cdot \mathbb{P}(B) = \frac{1}{2} \cdot \frac{1}{6} = \frac{1}{12}$.
Puisque $\mathbb{P}(A \cap B) = \mathbb{P}(A) \cdot \mathbb{P}(B)$, les événements $A$ et $B$ sont **indépendants**.

### Indépendance d'une famille d'événements

**Définition (Indépendance mutuelle).** Une famille d'événements $(A_i)_{i \in I}$ est dite mutuellement indépendante si, pour toute partie finie $J \subset I$, on a :
$$ \mathbb{P}\left( \bigcap_{j \in J} A_j \right) = \prod_{j \in J} \mathbb{P}(A_j) $$

*Remarque :* L'indépendance deux à deux n'implique pas l'indépendance mutuelle.

**Exemple concret (Contre-exemple de Bernstein).**
On lance un tétraèdre régulier dont les 4 faces sont numérotées $1, 2, 3, 4$. Chaque face a une probabilité $1/4$ d'apparaître sur la base.
Soit $A$ l'événement "le résultat est pair" : $A = \{2, 4\}$, $\mathbb{P}(A) = 2/4 = 1/2$.
Soit $B$ l'événement "le résultat est premier" : $B = \{2, 3\}$, $\mathbb{P}(B) = 1/2$.
Soit $C$ l'événement "le résultat est inférieur ou égal à 2" : $C = \{1, 2\}$, $\mathbb{P}(C) = 1/2$.
Vérifions l'indépendance deux à deux :
$A \cap B = \{2\} \implies \mathbb{P}(A \cap B) = 1/4 = \mathbb{P}(A)\mathbb{P}(B)$. (indépendants)
$B \cap C = \{2\} \implies \mathbb{P}(B \cap C) = 1/4 = \mathbb{P}(B)\mathbb{P}(C)$. (indépendants)
$A \cap C = \{2\} \implies \mathbb{P}(A \cap C) = 1/4 = \mathbb{P}(A)\mathbb{P}(C)$. (indépendants)
Cependant, l'intersection des trois est $A \cap B \cap C = \{2\}$. Sa probabilité est $\mathbb{P}(\{2\}) = 1/4$.
Or, $\mathbb{P}(A)\mathbb{P}(B)\mathbb{P}(C) = (1/2)^3 = 1/8$.
Puisque $1/4 \neq 1/8$, les événements ne sont pas mutuellement indépendants.

### Indépendance de Tribus et de Variables Aléatoires

**Définition (Indépendance de tribus).** Deux sous-tribus $\mathcal{A}, \mathcal{B} \subset \mathcal{F}$ sont indépendantes si, pour tout $A \in \mathcal{A}$ et tout $B \in \mathcal{B}$, $A$ et $B$ sont indépendants.

**Définition (Indépendance de variables aléatoires).** Deux variables aléatoires $X$ et $Y$ sont indépendantes si les tribus qu'elles engendrent, $\sigma(X)$ et $\sigma(Y)$, sont indépendantes. Concrètement, pour tous boréliens $B_1, B_2 \in \mathcal{B}(\mathbb{R})$ :
$$ \mathbb{P}(X \in B_1, Y \in B_2) = \mathbb{P}(X \in B_1) \cdot \mathbb{P}(Y \in B_2) $$

**Exemple concret (Variables de Bernoulli indépendantes).**
Soit $X \sim \mathcal{B}(p_1)$ et $Y \sim \mathcal{B}(p_2)$ deux variables aléatoires de Bernoulli indépendantes représentant le résultat de deux lancers de pièces truquées avec probabilités de succès respectives $p_1$ et $p_2$.
L'indépendance implique par exemple que la probabilité d'obtenir deux succès (1 et 1) est :
$\mathbb{P}(X = 1, Y = 1) = \mathbb{P}(X = 1)\mathbb{P}(Y = 1) = p_1 p_2$.
De même, $\mathbb{P}(X = 1, Y = 0) = \mathbb{P}(X = 1)\mathbb{P}(Y = 0) = p_1 (1 - p_2)$.


**Exemple concret (Tirage avec et sans remise).**
Une urne contient 3 boules rouges et 2 boules noires. On tire deux boules.
Soit $A$ : "La première boule est rouge" et $B$ : "La deuxième boule est rouge".
- **Avec remise :** Les tirages sont physiquement séparés. $\mathbb{P}(A) = 3/5$, $\mathbb{P}(B) = 3/5$. $\mathbb{P}(A \cap B) = 9/25 = \mathbb{P}(A)\mathbb{P}(B)$. Les événements sont **indépendants**.
- **Sans remise :** La première boule est retirée. $\mathbb{P}(A) = 3/5$. Si $A$ se réalise, il reste 2 rouges et 2 noires, donc $\mathbb{P}(B|A) = 2/4 = 1/2$. $\mathbb{P}(A \cap B) = \mathbb{P}(A)\mathbb{P}(B|A) = 3/10 \neq 9/25$. Les événements **ne sont pas indépendants**.

**Exemple concret (Indépendance de fonctions sur un espace de probabilité géométrique).**
Soit l'intervalle $\Omega = [0, 1]$ muni de la mesure de Lebesgue $\mathbb{P}$. Considérons les variables aléatoires $X(\omega) = \mathbf{1}_{[0, 1/2]}(\omega)$ et $Y(\omega) = \mathbf{1}_{[1/4, 3/4]}(\omega)$.
$\mathbb{P}(X = 1) = \mathbb{P}([0, 1/2]) = 1/2$.
$\mathbb{P}(Y = 1) = \mathbb{P}([1/4, 3/4]) = 1/2$.
L'événement $\{X=1 \text{ et } Y=1\}$ correspond à l'intersection des intervalles, soit $[1/4, 1/2]$. Sa mesure est $1/4$.
Puisque $1/4 = (1/2) \cdot (1/2)$, les événements $\{X=1\}$ et $\{Y=1\}$ sont indépendants. Les variables aléatoires $X$ et $Y$ sont **indépendantes**.


**Théorème (Espérance du produit).** Si $X$ et $Y$ sont deux variables aléatoires réelles indépendantes et intégrables (admettant une espérance finie), alors leur produit $XY$ est intégrable et on a :
$$ \mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y] $$

## 3. Démonstrations

### Démonstration du Théorème de l'Espérance du produit

**Énoncé :** Soient $X, Y : (\Omega, \mathcal{F}, \mathbb{P}) \to (\mathbb{R}, \mathcal{B}(\mathbb{R}))$ deux variables aléatoires indépendantes et intégrables. Alors $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y]$.

**Preuve rigoureuse :**

1. L'indépendance de $X$ et $Y$ signifie par définition que la loi du couple $(X,Y)$ sur $\mathbb{R}^2$ est exactement la mesure produit des lois marginales $\mathbb{P}_X$ et $\mathbb{P}_Y$. Ainsi, $\mathbb{P}_{(X,Y)} = \mathbb{P}_X \otimes \mathbb{P}_Y$.
2. Supposons d'abord que $X \geq 0$ et $Y \geq 0$. La fonction $g(x,y) = xy$ est mesurable et positive de $\mathbb{R}^2$ dans $\mathbb{R}$. Par le théorème de transfert, nous pouvons écrire l'espérance de $X Y$ sous forme d'une intégrale par rapport à la mesure jointe :
   $$ \mathbb{E}[XY] = \int_{\mathbb{R}^2} xy \, d\mathbb{P}_{(X,Y)}(x,y) $$
3. Comme $\mathbb{P}_{(X,Y)} = \mathbb{P}_X \otimes \mathbb{P}_Y$ et que l'intégrande $(x,y) \mapsto xy$ est positive, nous pouvons appliquer le théorème de Tonelli. Celui-ci autorise la décomposition de l'intégrale double en deux intégrales simples successives :
   $$ \int_{\mathbb{R}^2} xy \, d(\mathbb{P}_X \otimes \mathbb{P}_Y)(x,y) = \int_{\mathbb{R}} \left( \int_{\mathbb{R}} xy \, d\mathbb{P}_Y(y) \right) d\mathbb{P}_X(x) $$
4. Dans l'intégrale interne par rapport à $d\mathbb{P}_Y(y)$, la variable $x$ est constante et peut être factorisée hors de l'intégrale :
   $$ \int_{\mathbb{R}} x \left( \int_{\mathbb{R}} y \, d\mathbb{P}_Y(y) \right) d\mathbb{P}_X(x) $$
5. Par définition de l'espérance de $Y$, $\int_{\mathbb{R}} y \, d\mathbb{P}_Y(y) = \mathbb{E}[Y]$. Substituons cette valeur :
   $$ \int_{\mathbb{R}} x \mathbb{E}[Y] \, d\mathbb{P}_X(x) $$
6. $\mathbb{E}[Y]$ est une constante déterministe qui peut être factorisée hors de l'intégrale externe :
   $$ \mathbb{E}[Y] \int_{\mathbb{R}} x \, d\mathbb{P}_X(x) = \mathbb{E}[Y]\mathbb{E}[X] $$
7. Le résultat est ainsi prouvé pour $X \geq 0$ et $Y \geq 0$.
8. Pour le cas général de variables aléatoires intégrables de signe quelconque, on décompose $X = X^+ - X^-$ et $Y = Y^+ - Y^-$, où $X^+, X^-, Y^+, Y^-$ sont les parties positives et négatives respectives (qui sont positives et intégrables). L'indépendance de $X$ et $Y$ implique l'indépendance des parties positives et négatives (puisque ces opérations sont mesurables).
9. On développe le produit : $XY = (X^+ - X^-)(Y^+ - Y^-) = X^+ Y^+ - X^+ Y^- - X^- Y^+ + X^- Y^-$.
10. Par linéarité de l'espérance et en appliquant le résultat démontré à l'étape 7 à chacun des quatre termes (qui sont tous des produits de variables aléatoires positives, indépendantes et intégrables) :
    $$ \mathbb{E}[XY] = \mathbb{E}[X^+]\mathbb{E}[Y^+] - \mathbb{E}[X^+]\mathbb{E}[Y^-] - \mathbb{E}[X^-]\mathbb{E}[Y^+] + \mathbb{E}[X^-]\mathbb{E}[Y^-] $$
11. On factorise cette expression :
    $$ \mathbb{E}[XY] = (\mathbb{E}[X^+] - \mathbb{E}[X^-])(\mathbb{E}[Y^+] - \mathbb{E}[Y^-]) $$
12. Par définition de l'espérance d'une variable intégrable de signe quelconque, on retrouve bien :
    $$ \mathbb{E}[XY] = \mathbb{E}[X] \cdot \mathbb{E}[Y] $$

La démonstration est complète.

## 4. Applications en Physique, Logique et Intelligence Artificielle

L'hypothèse d'indépendance et d'identique distribution (I.I.D.) est le socle sur lequel repose une très large part de l'apprentissage statistique. Elle stipule que chaque observation d'un jeu de données de taille $N$ est un tirage aléatoire indépendant selon la même loi de probabilité sous-jacente.

**Fonction de Vraisemblance (Likelihood) en Apprentissage Supervisé.**
En intelligence artificielle, lorsqu'on entraîne un modèle paramétrique avec des poids $\theta$ (par exemple un réseau de neurones ou une régression logistique), on cherche à maximiser la probabilité d'observer les données $D = \{x_1, \dots, x_N\}$ sachant les paramètres du modèle.
Grâce à l'hypothèse d'indépendance (I.I.D.), la vraisemblance conjointe se factorise en un produit de probabilités marginales :
$$ P(x_1, x_2, \dots, x_N \mid \theta) = \prod_{i=1}^N P(x_i \mid \theta) $$
Pour des raisons de stabilité numérique (éviter l'underflow lié au produit de probabilités très petites) et de simplification calculatoire (la dérivée d'une somme est plus simple que celle d'un produit), on applique systématiquement la fonction logarithme népérien, strictement croissante, ce qui transforme ce produit en une somme :
$$ \log P(D \mid \theta) = \sum_{i=1}^N \log P(x_i \mid \theta) $$
Cette décomposition en somme de variables indépendantes permet par la suite l'application de la Loi Forte des Grands Nombres et du Théorème Central Limite, justifiant l'usage d'algorithmes comme la descente de gradient stochastique (Stochastic Gradient Descent).

**Mécanismes de Régularisation (Dropout).**
Dans les réseaux de neurones profonds, la technique du Dropout consiste à désactiver aléatoirement, à chaque itération d'entraînement, une proportion de neurones avec une probabilité $p$. La désactivation de chaque neurone est traitée comme une variable aléatoire de Bernoulli indépendante des autres. Cette indépendance forcée empêche les neurones de développer des "co-adaptations" complexes, forçant le réseau à répartir la représentation des connaissances de manière robuste sur l'ensemble de ses poids.
