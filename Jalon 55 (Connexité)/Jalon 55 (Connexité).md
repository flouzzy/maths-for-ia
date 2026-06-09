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

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez un archipel d'îles.
    - Si vous pouvez marcher d'un point A à un point B sans jamais vous mouiller les pieds, c'est que A et B sont sur la même île. L'île elle-même est un ensemble **connexe**.
    - S'il y a un bras de mer infranchissable entre deux groupes de maisons, l'archipel n'est pas connexe : il est formé de plusieurs **composantes connexes**.
    - La **connexité par arcs**, c'est la version "voyageur" : pouvez-vous tracer un chemin (un arc) continu qui relie les deux points ?
- **Le "Pourquoi on a inventé ça" :** Pour formaliser l'idée d'un objet "d'un seul tenant". En analyse, cela permet de généraliser le Théorème des Valeurs Intermédiaires. Si vous savez que votre fonction est positive à un endroit et négative à un autre sur un ensemble connexe, elle doit forcément passer par zéro quelque part entre les deux.
- **Visualisation :** Une ligne continue ou un cercle (connexe). Deux cercles séparés (non connexe).

## 2. Formalisation

### A. Connexité

Soit $(X, \mathcal{T})$ un espace topologique.

> **Définition 1 (Espace Connexe) :**
> On dit que $X$ est **connexe** s'il ne peut pas être partitionné en deux ouverts non vides et disjoints.
> De manière équivalente : les seules parties de $X$ qui sont à la fois ouvertes et fermées sont $\emptyset$ et $X$.

### B. Connexité par arcs

> **Définition 2 (Chemin / Arc) :**
> Un chemin reliant $x$ à $y$ dans $X$ est une application continue $\gamma : [0, 1] \to X$ telle que $\gamma(0) = x$ et $\gamma(1) = y$.

> **Définition 3 (Espace Connexe par arcs) :**
> $X$ est **connexe par arcs** si pour tout couple $(x, y) \in X^2$, il existe un chemin reliant $x$ à $y$.

### C. Théorèmes Fondamentaux

> **Théorème (Hiérarchie) :**
> Tout espace connexe par arcs est connexe. (La réciproque est fausse en général).

> **Théorème (Image continue) :**
> L'image d'un connexe (resp. connexe par arcs) par une application continue est un connexe (resp. connexe par arcs).

## 3. Démonstrations

### Démonstration : Connexité par arcs $\implies$ Connexité

1. **Cadre :** Soit $X$ connexe par arcs. Supposons par l'absurde que $X = U \cup V$ avec $U, V$ ouverts non vides disjoints.
2. **Choix des points :** Soient $x \in U$ et $y \in V$.
3. **Construction du chemin :** Comme $X$ est connexe par arcs, il existe $\gamma : [0, 1] \to X$ continue telle que $\gamma(0)=x$ et $\gamma(1)=y$.
4. **Partition de l'intervalle :** Considérons $A = \gamma^{-1}(U)$ and $B = \gamma^{-1}(V)$.
   - Comme $\gamma$ est continue, $A$ et $B$ sont des ouverts de $[0, 1]$.
   - $A \cap B = \gamma^{-1}(U \cap V) = \emptyset$.
   - $A \cup B = \gamma^{-1}(U \cup V) = [0, 1]$.
   - $0 \in A$ (car $\gamma(0)=x \in U$) et $1 \in B$ (car $\gamma(1)=y \in V$).
5. **Conclusion :** On a partitionné $[0, 1]$ en deux ouverts non vides disjoints. Or, on sait que $[0, 1]$ est connexe (théorème admis ici, basé sur la propriété de la borne supérieure). C'est une contradiction. Donc $X$ est connexe.

## 4. Exercices d'Application

### Exercice 1 : Les connexes de $\mathbb{R}$
**Énoncé :** Montrer que les seules parties connexes de $\mathbb{R}$ sont les intervalles.
**Correction Détaillée :**
1. Soit $I$ un intervalle. Si $I = U \cup V$ (ouverts disjoints), on utilise le même raisonnement que ci-dessus avec la borne supérieure pour montrer une contradiction.
2. Soit $A$ une partie qui n'est pas un intervalle. Il existe donc $x < z < y$ tels que $x, y \in A$ mais $z \notin A$. Alors $A = (A \cap ]-\infty, z[) \cup (A \cap ]z, +\infty[)$. Ce sont deux ouverts relatifs de $A$, non vides et disjoints. Donc $A$ n'est pas connexe.

### Exercice 2 : Niveau Avancé (La courbe sinus du topologue)
**Énoncé :** Soit $X = \{ (x, \sin(1/x)) \mid x > 0 \} \cup \{ (0, y) \mid y \in [-1, 1] \}$. Montrer que $X$ est connexe mais pas connexe par arcs.
**Correction Détaillée :**
- **Connexe :** C'est l'adhérence d'un ensemble connexe par arcs (le graphe de $\sin(1/x)$ pour $x>0$), donc c'est connexe.
- **Non connexe par arcs :** On ne peut pas tracer de chemin continu qui "arrive" à l'origine depuis la droite car la fonction oscille infiniment vite en se rapprochant de 0.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** Dans l'étude des **Surfaces de Perte** (Loss Landscapes) des réseaux de neurones profonds, la connexité des minima est un sujet de recherche majeur.
- **Exemple Concret :**
    - **Mode Connectivity :** Des chercheurs ont montré que pour les réseaux de neurones assez larges, presque tous les minima locaux trouvés par SGD sont connectés entre eux par des chemins de basse énergie (où la perte reste faible). Cela signifie qu'on peut passer d'une solution à une autre sans avoir à franchir une "montagne" de haute erreur.
    - **Algorithmes de Clustering :** Le clustering basé sur la densité (comme **DBSCAN**) définit un cluster comme une composante connexe d'un ensemble de points "denses". Si deux points peuvent être reliés par une chaîne de points proches, ils appartiennent au même groupe.
    - **Générateurs de graphes :** Pour garantir qu'une molécule générée par une IA est valide, on doit souvent vérifier que son graphe chimique est connexe (tous les atomes sont liés entre eux).

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 52 (Applications continues entre espaces topologiques et définition fine des homéomorphismes.).md]], [[Jalon 13 (Structure de R).md]]
- **Concepts Futurs dépendants :** [[Jalon 109 (Topologie des sous-variétés de Rn).md]], [[Jalon 115 (Démonstration du théorème de Stokes généralisé).md]]
