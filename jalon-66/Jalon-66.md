---
uuid: "jalon-66"
title: "Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives"
year: 2
trimester: 6
tags:
  - math/theorie-mesure
  - ia/fondations
prev: "[[jalon-65/Jalon-65.md]]"
next: "[[jalon-67/Jalon-67.md]]"
---

# Jalon 66 : Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives

## 1. De Riemann à Lebesgue : Le renversement de perspective

L'intégrale de Riemann, construite au XIXe siècle, repose sur un découpage du domaine de départ (l'axe des abscisses). On subdivise l'intervalle d'intégration en petits segments, sur lesquels on approche la fonction par des rectangles. Si cette méthode est redoutablement efficace pour les fonctions continues ou continues par morceaux, elle s'effondre face à des fonctions sauvagement discontinues. Le cas d'école est la fonction caractéristique des rationnels sur $[0,1]$ (fonction de Dirichlet). Riemann cherche à encadrer l'aire, mais les sommes de Darboux inférieures valent toujours 0 (chaque intervalle contient un irrationnel) et les sommes supérieures toujours 1 (chaque intervalle contient un rationnel). L'intégrale n'existe pas au sens de Riemann.

Henri Lebesgue, dans sa thèse fondatrice de 1902, opère un renversement géométrique radical. Au lieu de découper l'axe des $x$, il propose de découper l'axe des $y$ (l'ensemble d'arrivée). On regroupe ensemble tous les $x$ tels que $f(x)$ vaut à peu près $y$.
Ce changement de paradigme permet d'agréger des ensembles de points complètement éparpillés (comme les rationnels), à condition de savoir mesurer la "taille" de ces ensembles (ce que fournit la mesure de Lebesgue). L'intégrale devient alors une somme pondérée de la forme "Valeur $\times$ Mesure de l'ensemble où la fonction prend cette valeur".

Pour construire rigoureusement cet édifice, la méthode standard procède par approximation par le bas. On définit d'abord l'intégrale pour des fonctions en escalier très générales appelées "fonctions étagées", puis on étend la définition à toute fonction mesurable positive par un passage au supremum.

## 2. Intégration des fonctions étagées positives

Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. Rappelons qu'une fonction $s: X \to \mathbb{R}_+$ est étagée si elle est mesurable et ne prend qu'un nombre fini de valeurs distinctes $a_1, a_2, \dots, a_n$.

### Énoncé formel

> **Définition (Forme canonique et intégrale d'une fonction étagée positive) :**
> Soit $s$ une fonction étagée positive sur $X$. Soient $a_1, \dots, a_n$ les valeurs distinctes non nulles prises par $s$, et $A_i = \{x \in X \mid s(x) = a_i\} = s^{-1}(\{a_i\})$.
> La représentation $s = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$ est appelée forme canonique de $s$.
> On définit l'intégrale de $s$ par rapport à $\mu$ par :
> $$\int_X s \, d\mu = \sum_{i=1}^n a_i \mu(A_i)$$
> Cette valeur appartient à $[0, +\infty]$.

**Typage strict :**
- $a_i \in \mathbb{R}_+^*$
- $A_i \in \mathcal{A}$ sont des ensembles mesurables disjoints.
- $\mu(A_i) \in [0, +\infty]$.
- Par convention absolue en théorie de la mesure, $0 \cdot (+\infty) = 0$. Ainsi, si une fonction prend la valeur $0$ sur un ensemble de mesure infinie, la contribution à l'intégrale est nulle.

### Dissection et Propriétés

Cette définition semble très naturelle, mais pour la rendre opératoire, il faut s'assurer qu'elle est bien définie même si l'on écrit la fonction étagée autrement que sous sa forme canonique.

> **Lemme (Indépendance de la représentation) :**
> Si une fonction étagée positive s'écrit sous la forme $s = \sum_{j=1}^m b_j \mathbf{1}_{B_j}$ où les $B_j \in \mathcal{A}$ forment une partition de $X$ et $b_j \ge 0$, alors :
> $$\int_X s \, d\mu = \sum_{j=1}^m b_j \mu(B_j)$$

**Exemple concret calculatoire :**
Considérons l'espace $X = [0, 5]$ muni de la tribu borélienne et de la mesure de Lebesgue $\lambda$.
Soit la fonction étagée $s(x)$ définie par :
- $s(x) = 3$ si $x \in [0, 1[ \cup [3, 4]$
- $s(x) = 7$ si $x \in [2, 2.5]$
- $s(x) = 0$ ailleurs.

La forme canonique est $s = 3 \mathbf{1}_{A_1} + 7 \mathbf{1}_{A_2}$ avec $A_1 = [0, 1[ \cup [3, 4]$ et $A_2 = [2, 2.5]$.
Calculons les mesures :
$\lambda(A_1) = \lambda([0, 1[) + \lambda([3, 4]) = 1 + 1 = 2$.
$\lambda(A_2) = 2.5 - 2 = 0.5$.

L'intégrale vaut alors :
$$\int_{[0,5]} s \, d\lambda = 3 \times 2 + 7 \times 0.5 = 6 + 3.5 = 9.5$$

**Configurations limites :**
Si $X = \mathbb{R}$ et $s(x) = 2$ sur $A = [0, +\infty[$, alors $\int_{\mathbb{R}} s \, d\lambda = 2 \times (+\infty) = +\infty$.

## 3. L'intégrale des fonctions mesurables positives

Ayant défini l'intégrale pour le squelette des fonctions étagées, nous pouvons "remplir" l'aire sous le graphe de toute fonction mesurable positive en prenant la borne supérieure de toutes les aires des fonctions étagées qui la minorent.

### Énoncé formel

> **Définition (Intégrale d'une fonction mesurable positive) :**
> Soit $f: X \to [0, +\infty]$ une fonction mesurable. On définit l'intégrale de $f$ par rapport à $\mu$ par :
> $$\int_X f \, d\mu = \sup \left\lbrace \int_X s \, d\mu \ \bigg| \ s \text{ est étagée positive et } \forall x \in X, \ 0 \le s(x) \le f(x) \right\rbrace$$
> On note souvent l'ensemble des fonctions étagées positives minorant $f$ par $\mathcal{E}_+(f)$.

**Typage strict :**
- $f \in \mathcal{M}^+(X, \mathcal{A})$ (l'ensemble des fonctions mesurables à valeurs dans $\overline{\mathbb{R}_+}$).
- Le supremum est pris dans $\overline{\mathbb{R}_+}$, donc l'intégrale peut valoir $+\infty$.
- Si $\int_X f \, d\mu < +\infty$, on dit que la fonction $f$ est **intégrable** (ou $\mu$-intégrable).

### Dissection et propriétés géométriques

Cette définition abstraite par le supremum garantit intrinsèquement la positivité et la monotonie de l'intégrale :
1. **Positivité :** Si $f \ge 0$, alors la fonction nulle $s=0$ minore $f$, donc $\int_X f \, d\mu \ge 0$.
2. **Croissance :** Si $f \le g$, tout $s \in \mathcal{E}_+(f)$ est aussi dans $\mathcal{E}_+(g)$, donc $\int_X f \, d\mu \le \int_X g \, d\mu$.

**Exemple concret calculatoire : La fonction de Dirichlet**
Sur $X = [0,1]$ avec la mesure de Lebesgue $\lambda$.
$f(x) = \mathbf{1}_{\mathbb{Q} \cap [0,1]}(x)$.
Cette fonction est mesurable (car l'ensemble des rationnels est borélien) et positive.
De plus, elle ne prend que les valeurs $0$ et $1$, c'est donc elle-même une fonction étagée !
On peut utiliser la formule directe :
$$\int_{[0,1]} f \, d\lambda = 1 \times \lambda(\mathbb{Q} \cap [0,1]) + 0 \times \lambda([0,1] \setminus \mathbb{Q})$$
Or, l'ensemble $\mathbb{Q}$ est dénombrable, donc de mesure de Lebesgue nulle.
$$\int_{[0,1]} \mathbf{1}_{\mathbb{Q}} \, d\lambda = 1 \times 0 = 0$$
L'aire sous la courbe de la fonction de Dirichlet est strictement nulle au sens de Lebesgue.

## 4. Démonstrations : Linéarité de l'intégrale pour les fonctions étagées

Pour manipuler sereinement l'intégrale, nous devons prouver qu'elle est linéaire. C'est l'étape la plus délicate de cette construction élémentaire. Démontrons la linéarité sur l'espace des fonctions étagées positives.

> **Théorème :**
> Soient $s, t$ deux fonctions étagées positives sur $(X, \mathcal{A}, \mu)$ et $\alpha \ge 0$. Alors :
> 1. $\int_X (\alpha s) \, d\mu = \alpha \int_X s \, d\mu$
> 2. $\int_X (s + t) \, d\mu = \int_X s \, d\mu + \int_X t \, d\mu$

**Démonstration pas à pas de l'additivité :**

1. **Initialisation et Cadre :**
   Exprimons $s$ et $t$ sous forme de sommes sur des partitions mesurables.
   Soit $s = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$ la forme canonique de $s$, avec les $A_i$ formant une partition de $X$.
   Soit $t = \sum_{j=1}^m b_j \mathbf{1}_{B_j}$ la forme canonique de $t$, avec les $B_j$ formant une partition de $X$.

2. **Étape 1 : Construction d'une partition commune (le raffinement croisé) :**
   Pour additionner $s$ et $t$, nous devons travailler sur des ensembles où *les deux* fonctions sont constantes.
   Posons $E_{i,j} = A_i \cap B_j$ pour tout $1 \le i \le n$ et $1 \le j \le m$.
   Les ensembles $E_{i,j}$ sont mesurables et forment une nouvelle partition de $X$.
   Sur l'ensemble $E_{i,j}$, la fonction $s$ vaut exactement $a_i$ et la fonction $t$ vaut exactement $b_j$.
   Donc, sur $E_{i,j}$, la somme $s+t$ vaut $a_i + b_j$.

3. **Étape 2 : Réécriture des fonctions sur la nouvelle partition :**
   Nous pouvons réécrire les fonctions ainsi :
   $$s = \sum_{i=1}^n \sum_{j=1}^m a_i \mathbf{1}_{E_{i,j}}$$
   $$t = \sum_{i=1}^n \sum_{j=1}^m b_j \mathbf{1}_{E_{i,j}}$$
   $$s + t = \sum_{i=1}^n \sum_{j=1}^m (a_i + b_j) \mathbf{1}_{E_{i,j}}$$

4. **Étape 3 : Calcul des intégrales via le lemme d'indépendance :**
   Par définition (et le lemme d'indépendance de la représentation), nous avons :
   $$\int_X (s+t) \, d\mu = \sum_{i=1}^n \sum_{j=1}^m (a_i + b_j) \mu(E_{i,j})$$
   En distribuant la somme :
   $$= \sum_{i=1}^n \sum_{j=1}^m a_i \mu(E_{i,j}) + \sum_{i=1}^n \sum_{j=1}^m b_j \mu(E_{i,j})$$

5. **Étape 4 : Reconstitution par additivité de la mesure :**
   Factorisons $a_i$ dans la première double somme :
   $$= \sum_{i=1}^n a_i \left( \sum_{j=1}^m \mu(E_{i,j}) \right) + \sum_{j=1}^m b_j \left( \sum_{i=1}^n \mu(E_{i,j}) \right)$$
   Or, à $i$ fixé, les $E_{i,j} = A_i \cap B_j$ forment une partition de $A_i$ lorsque $j$ varie.
   Puisque $\mu$ est une mesure (donc additive), $\sum_{j=1}^m \mu(A_i \cap B_j) = \mu \left( \bigcup_{j=1}^m (A_i \cap B_j) \right) = \mu(A_i)$.
   De même, $\sum_{i=1}^n \mu(E_{i,j}) = \mu(B_j)$.

6. **Conclusion :**
   En substituant ces relations, nous obtenons :
   $$= \sum_{i=1}^n a_i \mu(A_i) + \sum_{j=1}^m b_j \mu(B_j)$$
   $$= \int_X s \, d\mu + \int_X t \, d\mu$$
   L'additivité est rigoureusement prouvée.

## 5. Pertinence pour l'Intelligence Artificielle et la Modélisation

L'intégration de Lebesgue sur un espace mesuré abstrait est la pierre de Rosette permettant de réunir les probabilités discrètes et les probabilités continues sous un même formalisme.

En théorie statistique de l'apprentissage (PAC Learning, gestion du risque empirique), la fonction de perte (Loss) attendue (le risque vrai) est définie comme l'espérance de la perte sur toute la distribution des données :
$$L(h) = \int_{X \times Y} \ell(h(x), y) \, d\mathbb{P}(x, y)$$
Ici, $\mathbb{P}$ est la mesure de probabilité jointe sur l'espace des caractéristiques $X$ et des étiquettes $Y$.
- Les étiquettes $Y$ peuvent être discrètes (classification, chats/chiens).
- Les caractéristiques $X$ peuvent être un mélange de données continues (pixels) et catégorielles.

L'intégrale de Riemann est impuissante face à cet espace hétérogène. L'intégrale de Lebesgue, définie par un passage au supremum des fonctions étagées, permet de quantifier rigoureusement cette perte attendue sans avoir à écrire des cas séparés (sommes vs intégrales) et permet de prouver que les algorithmes convergent (par exemple via le théorème de convergence dominée, que nous aborderons plus tard) indépendamment de la structure intime des données.
