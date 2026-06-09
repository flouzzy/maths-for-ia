---
uuid: "jalon-49"
title: "Espaces topologiques généraux"
year: 2
trimester: 5
tags:
  - math/topologie
  - ia/abstraction
prev: "[[Jalon 48 (Livrable IA).md]]"
next: "[[Jalon 50 (Opérateurs topologiques).md]]"
---

# Jalon 49 : Espaces topologiques généraux

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous dessiniez sur un drap en caoutchouc. Vous pouvez étirer le drap, le tordre, le déformer autant que vous voulez, mais vous n'avez pas le droit de le déchirer ni de coller deux points qui étaient éloignés. Qu'est-ce qui ne change pas ? Si deux points étaient "voisins" avant la déformation, ils le resteront après. La **Topologie**, c'est l'étude de cette notion de "voisinage" sans avoir besoin d'une règle pour mesurer les distances. C'est la géométrie du "proche" et du "lointain" dans sa forme la plus pure.
- **Le "Pourquoi on a inventé ça" :** Parfois, on veut parler de continuité ou de limite sur des ensembles bizarres où on ne peut pas mesurer de distance (comme des ensembles de fonctions ou des graphes géants). Les mathématiciens ont donc créé une règle du jeu universelle : au lieu de mesurer des mètres, on définit simplement quels sous-ensembles sont des "zones ouvertes" (les ouverts).
- **Visualisation :** Un nuage de points. On ne regarde pas la distance exacte entre les points, on regarde seulement quels points sont "dans le même quartier".

## 2. Formalisation

### A. Définition d'une Topologie

Soit $X$ un ensemble non vide.

> **Définition 1 (Topologie) :**
> On appelle **topologie** sur $X$ une famille $\mathcal{T}$ de parties de $X$ (appelées **ouverts**) vérifiant les trois axiomes suivants :
> 1. $\emptyset \in \mathcal{T}$ et $X \in \mathcal{T}$.
> 2. Toute réunion (même infinie) d'éléments de $\mathcal{T}$ est dans $\mathcal{T}$.
> 3. Toute intersection **finie** d'éléments de $\mathcal{T}$ est dans $\mathcal{T}$.
> Le couple $(X, \mathcal{T})$ est appelé un **espace topologique**.

### B. Fermés et Voisinages

> **Définition 2 (Fermé) :**
> Une partie $F$ de $X$ est dite **fermée** si son complémentaire $X \setminus F$ est un ouvert.

> **Définition 3 (Voisinage) :**
> Soit $a \in X$. On appelle **voisinage** de $a$ toute partie $V \subset X$ qui contient un ouvert $U$ contenant lui-même $a$ :
> $$\exists U \in \mathcal{T}, \quad a \in U \subset V$$

### C. Exemples fondamentaux

1. **Topologie discrète :** Tous les sous-ensembles sont des ouverts ($\mathcal{T} = \mathcal{P}(X)$).
2. **Topologie grossière :** Les seuls ouverts sont $\emptyset$ et $X$ ($\mathcal{T} = \{ \emptyset, X \}$).
3. **Topologie induite par une distance :** C'est la topologie usuelle sur $\mathbb{R}^n$ (voir Jalon 34).

## 3. Démonstrations

### Démonstration : Stabilité des fermés

Montrons que l'intersection de fermés est un fermé, et que la réunion finie de fermés est un fermé.

1. **Cadre :** Soit $(F_i)_{i \in I}$ une famille de fermés.
2. **Intersection quelconque :**
   Considérons $A = \bigcap_{i \in I} F_i$. Passons au complémentaire par les lois de De Morgan :
   $X \setminus A = X \setminus (\bigcap_{i \in I} F_i) = \bigcup_{i \in I} (X \setminus F_i)$.
   Comme chaque $F_i$ est fermé, chaque $X \setminus F_i$ est un ouvert.
   Par l'axiome 2 de la topologie, la réunion quelconque d'ouverts est un ouvert.
   Donc $X \setminus A$ est ouvert, donc $A$ est fermé.
3. **Réunion finie :**
   Soient $F_1, \dots, F_n$ des fermés. Posons $B = \bigcup_{j=1}^n F_j$.
   $X \setminus B = X \setminus (\bigcup F_j) = \bigcap_{j=1}^n (X \setminus F_j)$.
   C'est une intersection **finie** d'ouverts. Par l'axiome 3, c'est un ouvert.
   Donc $B$ est fermé.

## 4. Exercices d'Application

### Exercice 1 : Topologie Co-finie
**Énoncé :** Soit $X$ un ensemble infini. On définit $\mathcal{T} = \{ \emptyset \} \cup \{ U \subset X \mid X \setminus U \text{ est fini} \}$. Montrer que $\mathcal{T}$ est une topologie.
**Correction Détaillée :**
1. **Axiome 1 :** $\emptyset \in \mathcal{T}$ par définition. $X \setminus X = \emptyset$, qui est fini, donc $X \in \mathcal{T}$.
2. **Réunion :** Soit $(U_i)$ une famille d'ouverts. $X \setminus (\cup U_i) = \cap (X \setminus U_i)$. L'intersection d'ensembles finis est finie, donc la réunion est un ouvert.
3. **Intersection finie :** $X \setminus (U \cap V) = (X \setminus U) \cup (X \setminus V)$. L'union de deux ensembles finis est finie, donc l'intersection est un ouvert.

### Exercice 2 : Niveau Avancé (Intérieur et Adhérence)
**Énoncé :** Montrer que l'intérieur d'une partie $A$ (noté $\mathring{A}$) est le plus grand ouvert contenu dans $A$.
**Correction Détaillée :**
On définit $\mathring{A}$ comme la réunion de tous les ouverts inclus dans $A$. Par l'axiome 2, cette réunion est un ouvert. Comme tout ouvert inclus dans $A$ fait partie de cette réunion, $\mathring{A}$ est bien le plus grand.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, on travaille souvent sur des **Graphes** (réseaux sociaux, molécules). Un graphe est un ensemble discret. On peut y définir des topologies (voisinages de nœuds) pour parler de la "diffusion" de l'information sans avoir de coordonnées GPS pour les nœuds.
- **Exemple Concret :**
    - **Manifold Learning (Apprentissage de variétés) :** On suppose que des données de haute dimension (ex: des photos de visages) se situent en fait sur une "forme" de dimension plus petite (une variété) pliée dans l'espace. Des algorithmes comme **t-SNE** ou **UMAP** essaient de préserver la **topologie locale** (les voisinages) des données tout en réduisant la dimension. Si deux visages sont topologiquement proches dans l'espace 1000D, ils doivent rester proches dans l'affichage 2D.
    - **Analyse Topologique des Données (TDA) :** On utilise des outils comme l'**Homologie Persistante** pour détecter des trous ou des structures dans un nuage de points (ex: détecter une boucle dans des données de séries temporelles), ce qui donne des signatures géométriques robustes au bruit.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 4 (Théorie des ensembles).md]], [[Jalon 35 (Caractérisation séquentielle des ouverts).md]]
- **Concepts Futurs dépendants :** [[Jalon 50 (Opérateurs topologiques).md]], [[Jalon 52 (Applications continues entre espaces topologiques et définition fine des homéomorphismes.).md]]
