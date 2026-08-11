---
uuid: "jalon-55"
title: "Connexité et Connexité par arcs"
year: 2
trimester: 5
tags:
  - math/topologie
  - ia/topologie
prev: "[[Jalon 54 (Compacité générale).md]]"
next: "[[Jalon 56 (Espaces métriques complets).md]]"
---

# Jalon 55 : Connexité et Connexité par arcs

## Introduction

La théorie naissante de la topologie à la fin du XIXe siècle, poussée par les travaux de Cantor et Poincaré, cherchait à capturer l'essence de la continuité et de l'intégrité d'un espace. L'intuition géométrique d'un objet "d'un seul tenant" (un segment, un disque) s'opposait à celle d'un objet morcelé (la réunion de deux disques disjoints). Cependant, dans des espaces abstraits où la notion de "chemin" continu n'est pas toujours claire (ou suffisante), une définition purement topologique, basée sur la théorie des ensembles ouverts, devenait impérative. La connexité a donc été définie non pas par ce qui relie les points, mais par l'impossibilité de scinder l'espace en morceaux disjoints de nature topologique semblable. Cette formalisation permet de généraliser le théorème des valeurs intermédiaires de Cauchy, fondamental en analyse, à des espaces de dimension arbitraire et à des topologies non métriques.

## Définitions, Théorèmes et Propriétés Fondamentales

### 1. Espaces Topologiques Connexes

Soit $(X, \mathcal{T})$ un espace topologique.

> **Définition (Connexité) :**
> Un espace topologique $X$ est dit **connexe** s'il est impossible de le partitionner en deux ouverts non vides disjoints.
> De manière équivalente, $X$ est connexe si et seulement si les seules parties de $X$ à la fois ouvertes et fermées (clopens) sont $\emptyset$ et $X$.

**Exemple Concret 1 :**
Considérons l'espace $X = [0, 1] \cup [2, 3]$ muni de la topologie induite par la topologie usuelle de $\mathbb{R}$. Les sous-ensembles $U = [0, 1]$ et $V = [2, 3]$ sont non vides, disjoints, et vérifient $X = U \cup V$. De plus, $U = X \cap ]-1, 1.5[$ est ouvert dans $X$ (par définition de la topologie induite) et $V = X \cap ]1.5, 4[$ est ouvert dans $X$. $X$ est donc partitionné par deux ouverts non vides disjoints : $X$ n'est pas connexe.

**Configurations Pathologiques :**
L'espace des nombres rationnels $\mathbb{Q}$ muni de la topologie usuelle induite par $\mathbb{R}$ est totalement discontinu. Pour tout $a \notin \mathbb{Q}$ (par exemple $a = \sqrt{2}$), les ensembles $U = \mathbb{Q} \cap ]-\infty, a[$ et $V = \mathbb{Q} \cap ]a, +\infty[$ sont ouverts dans $\mathbb{Q}$, non vides et partitionnent $\mathbb{Q}$. Ainsi, non seulement $\mathbb{Q}$ n'est pas connexe, mais aucune de ses parties (à part les singletons) n'est connexe.

### 2. Connexité par Arcs

> **Définition (Chemin continu) :**
> Un chemin reliant $x \in X$ à $y \in X$ est une application continue $\gamma : [0, 1] \to X$ telle que $\gamma(0) = x$ et $\gamma(1) = y$.

> **Définition (Connexité par arcs) :**
> Un espace topologique $X$ est dit **connexe par arcs** si pour tout couple $(x, y) \in X^2$, il existe un chemin continu dans $X$ reliant $x$ à $y$.

**Exemple Concret 2 :**
Dans l'espace euclidien $\mathbb{R}^n$, toute partie convexe $C$ est connexe par arcs. En effet, pour tout couple $(x, y) \in C^2$, le segment de droite défini par $\gamma(t) = (1-t)x + ty$ pour $t \in [0, 1]$ est entièrement contenu dans $C$. L'application $\gamma$ est clairement continue (polynôme en $t$), $\gamma(0) = x$ et $\gamma(1) = y$.

### 3. Relations entre Connexité et Connexité par Arcs

> **Théorème (Implication fondamentale) :**
> Tout espace topologique connexe par arcs est connexe.

La réciproque est *fausse* en général. Il existe des espaces connexes qui ne sont pas connexes par arcs. L'exemple canonique est la "courbe sinus du topologue" définie par :
$S = \left\{ \left(x, \sin\left(\frac{1}{x}\right)\right) \in \mathbb{R}^2 \mid x \in ]0, 1] \right\} \cup \left\{ (0, y) \in \mathbb{R}^2 \mid y \in [-1, 1] \right\}$
L'adhérence d'un connexe (la première partie) est connexe, donc $S$ est connexe. Cependant, il est impossible de relier continûment un point de la première partie à un point de la seconde en raison des oscillations infinies au voisinage de $x=0$.

> **Théorème (Invariance par continuité) :**
> Soit $f : X \to Y$ une application continue entre deux espaces topologiques.
> - Si $X$ est connexe, alors l'image $f(X)$ est connexe dans $Y$.
> - Si $X$ est connexe par arcs, alors $f(X)$ est connexe par arcs dans $Y$.

## Démonstrations

### Preuve : Un espace connexe par arcs est connexe

1. **Hypothèse :** Soit $X$ un espace topologique connexe par arcs. Raisonnons par l'absurde en supposant que $X$ n'est pas connexe.
2. **Étape 1 : Partition de l'espace.** Par définition, il existe deux ouverts $U$ et $V$ de $X$, non vides, tels que $U \cap V = \emptyset$ et $U \cup V = X$.
3. **Étape 2 : Choix des points.** Comme $U$ et $V$ sont non vides, il existe $x \in U$ et $y \in V$.
4. **Étape 3 : Construction du chemin.** $X$ étant connexe par arcs, il existe une fonction continue $\gamma : [0, 1] \to X$ telle que $\gamma(0) = x$ et $\gamma(1) = y$.
5. **Étape 4 : Analyse de l'image réciproque.** Considérons les ensembles $A = \gamma^{-1}(U)$ et $B = \gamma^{-1}(V)$ dans $[0, 1]$.
   - La continuité de $\gamma$ assure que $A$ et $B$ sont des ouverts de $[0, 1]$ (pour la topologie induite usuelle).
   - Puisque $U$ et $V$ partitionnent $X$, $A$ et $B$ partitionnent $[0, 1]$ : $A \cup B = \gamma^{-1}(U \cup V) = \gamma^{-1}(X) = [0, 1]$ et $A \cap B = \gamma^{-1}(U \cap V) = \gamma^{-1}(\emptyset) = \emptyset$.
   - $0 \in A$ (car $\gamma(0) = x \in U$) donc $A \neq \emptyset$.
   - $1 \in B$ (car $\gamma(1) = y \in V$) donc $B \neq \emptyset$.
6. **Étape 5 : Contradiction.** Nous avons construit une partition de l'intervalle $[0, 1]$ en deux ouverts non vides et disjoints. Or, il est un résultat fondamental que les intervalles de $\mathbb{R}$ sont connexes. L'existence de cette partition contredit la connexité de $[0, 1]$.
7. **Conclusion :** L'hypothèse initiale est fausse. $X$ est donc nécessairement connexe.

### Preuve : Les connexes de $\mathbb{R}$ sont les intervalles

*Rappelons qu'une partie $I \subset \mathbb{R}$ est un intervalle si et seulement si : $\forall x, y \in I, \forall z \in \mathbb{R}, (x < z < y \implies z \in I)$.*

Soit $C$ une partie connexe de $\mathbb{R}$.
1. **Raisonnement par contraposée :** Supposons que $C$ ne soit pas un intervalle.
2. **Caractérisation de la non-intervalle :** Il existe $x, y \in C$ et $z \notin C$ tels que $x < z < y$.
3. **Construction des ouverts :** Posons $U = C \cap ]-\infty, z[$ et $V = C \cap ]z, +\infty[$.
4. **Propriétés de $U$ et $V$ :**
   - $U$ et $V$ sont des ouverts de la topologie induite sur $C$.
   - $x \in U$ et $y \in V$, donc $U$ et $V$ sont non vides.
   - $U \cap V = C \cap \emptyset = \emptyset$.
   - Puisque $z \notin C$, tout élément $c \in C$ vérifie soit $c < z$, soit $c > z$. Ainsi, $C = U \cup V$.
5. **Conclusion partielle :** $C$ admet une partition par deux ouverts non vides, donc $C$ n'est pas connexe. Par contraposée, tout connexe de $\mathbb{R}$ est un intervalle.

*(La preuve réciproque, montrant que tout intervalle est connexe, repose sur l'axiome de la borne supérieure et complète le résultat).*

## Applications en Physique, Logique et Intelligence Artificielle

### Topologie du Paysage de Perte (Loss Landscapes) en Deep Learning
En apprentissage profond, la fonction de perte $\mathcal{L}(\theta)$ pour des paramètres $\theta \in \mathbb{R}^d$ définit une surface très complexe. Une question majeure est la **connectivité des minima**. Les recherches récentes (Mode Connectivity) montrent que les minima locaux de $\mathcal{L}$ trouvés par la descente de gradient stochastique (SGD) sur des réseaux très paramétrés appartiennent souvent à la même composante connexe par arcs d'ensembles de sous-niveaux. Autrement dit, il existe des chemins continus dans l'espace des poids reliant deux minima le long desquels la perte reste presque constante, évitant ainsi les barrières d'énergie.

### Analyse des Composantes Connexes et GNN
Dans le domaine des Graph Neural Networks (GNN) et de l'analyse de données topologiques (TDA), la détection de composantes connexes est fondamentale pour le partitionnement des données. Un algorithme de clustering tel que DBSCAN identifie intrinsèquement des régions denses maximalement connectées (les composantes connexes d'un graphe de proximité sous-jacent). La caractérisation rigoureuse de ces amas repose sur les définitions topologiques de la connexité sur des variétés échantillonnées.

### Théorème du Point Fixe et Stabilité en Contrôle Linéaire
Dans la théorie du contrôle continu et les systèmes dynamiques définissant des variétés invariantes, la connexité de l'espace des phases garantit que l'évolution d'un état initial (qui décrit un chemin continu par rapport au temps) ne sautera pas de manière discontinue. C'est la connexité de l'espace de configuration qui permet aux algorithmes de planification de mouvement en robotique d'affirmer l'existence d'une trajectoire admissible d'un état A vers un état B en évitant les obstacles.
