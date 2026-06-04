---
uuid: "jalon-50"
title: "Opérateurs topologiques : Intérieur, Adhérence, Frontière"
year: 2
trimester: 5
tags:
  - math/topologie
  - ia/abstraction
prev: "[[Jalon 49 (Espaces topologiques généraux).md]]"
next: "[[Jalon 51 (Espaces métriques).md]]"
---

# Jalon 50 : Opérateurs topologiques : Intérieur, Adhérence, Frontière

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez une île au milieu de l'océan.
    - L'**Intérieur**, c'est le cœur de l'île : si vous y êtes, vous pouvez faire quelques pas dans n'importe quelle direction et vous resterez toujours au sec sur la terre ferme.
    - L'**Adhérence**, c'est l'île entière, y compris le sable mouillé sur la plage. Même si vous n'êtes pas sur la terre ferme, vous êtes "juste à côté".
    - La **Frontière**, c'est la ligne précise où l'eau touche le sable. À cet endroit, n'importe quel petit pas peut vous mettre soit dans l'eau, soit sur l'île.
    - Un ensemble **Dense**, c'est comme des grains de poussière partout dans une pièce : peu importe où vous posez le doigt, il y aura toujours un grain de poussière juste à côté.
- **Le "Pourquoi on a inventé ça" :** Pour découper proprement l'espace. En IA, on veut souvent séparer les "bons" exemples des "mauvais". Ces opérateurs permettent de définir mathématiquement ce qu'est une "marge de sécurité" (l'intérieur) ou une "zone d'incertitude" (la frontière).
- **Visualisation :** Un disque plein (adhérence), un disque sans son bord (intérieur), et le cercle qui l'entoure (frontière).

## 2. Formalisation & Rigueur Académique

Soit $(X, \mathcal{T})$ un espace topologique et $A$ une partie de $X$.

### A. Définitions des Opérateurs

> **Définition 1 (Intérieur) :**
> L'**intérieur** de $A$, noté $\mathring{A}$ ou $\text{int}(A)$, est la réunion de tous les ouverts inclus dans $A$. C'est le plus grand ouvert contenu dans $A$.
> $$x \in \mathring{A} \iff \exists V \in \mathcal{V}(x), V \subset A$$

> **Définition 2 (Adhérence) :**
> L'**adhérence** (ou fermeture) de $A$, notée $\bar{A}$ ou $\text{cl}(A)$, est l'intersection de tous les fermés contenant $A$. C'est le plus petit fermé contenant $A$.
> $$x \in \bar{A} \iff \forall V \in \mathcal{V}(x), V \cap A \neq \emptyset$$

> **Définition 3 (Frontière) :**
> La **frontière** de $A$, notée $\partial A$ ou $\text{fr}(A)$, est l'ensemble des points qui ne sont ni dans l'intérieur de $A$, ni dans l'intérieur de son complémentaire.
> $$\partial A = \bar{A} \setminus \mathring{A} = \bar{A} \cap \overline{X \setminus A}$$

### B. Densité

> **Définition 4 (Ensemble Dense) :**
> On dit que $A$ est **dense** dans $X$ si son adhérence est l'espace tout entier : $\bar{A} = X$.
> Cela signifie qu'on peut approcher n'importe quel point de $X$ aussi près qu'on veut par des points de $A$.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : $x \in \bar{A} \iff$ tout voisinage de $x$ rencontre $A$

1. **Sens direct ($\implies$) :** Supposons $x \in \bar{A}$. Par l'absurde, supposons qu'il existe un voisinage $V$ de $x$ tel que $V \cap A = \emptyset$. Par définition du voisinage, il existe un ouvert $U$ tel que $x \in U \subset V$. Alors $U \cap A = \emptyset$, donc $A \subset X \setminus U$. Comme $U$ est ouvert, $X \setminus U$ est fermé. Mais $\bar{A}$ est le plus petit fermé contenant $A$, donc $\bar{A} \subset X \setminus U$. Comme $x \in U$, alors $x \notin X \setminus U$, donc $x \notin \bar{A}$. Contradiction.
2. **Sens réciproque ($\impliedby$) :** Supposons que tout voisinage de $x$ rencontre $A$. Soit $F$ un fermé quelconque contenant $A$. Montrons que $x \in F$. Si $x \notin F$, alors $x \in X \setminus F$. Or $X \setminus F$ est un ouvert, c'est donc un voisinage de $x$. Par hypothèse, $(X \setminus F) \cap A \neq \emptyset$. Mais c'est impossible car $A \subset F$. Donc $x$ appartient à tous les fermés contenant $A$, donc $x \in \bar{A}$.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Topologie de $\mathbb{Q}$ dans $\mathbb{R}$
**Énoncé :** Déterminer l'intérieur, l'adhérence et la frontière de $\mathbb{Q}$ dans $\mathbb{R}$.
**Correction Détaillée :**
1. **Intérieur :** Soit $x \in \mathbb{Q}$. Tout intervalle ouvert $]x-\epsilon, x+\epsilon[$ contient des nombres irrationnels (densité de $\mathbb{R} \setminus \mathbb{Q}$). Donc aucun intervalle n'est inclus dans $\mathbb{Q}$. $\mathring{\mathbb{Q}} = \emptyset$.
2. **Adhérence :** Tout intervalle ouvert $]x-\epsilon, x+\epsilon[$ contient des nombres rationnels (densité de $\mathbb{Q}$). Donc tout point de $\mathbb{R}$ est adhérent à $\mathbb{Q}$. $\bar{\mathbb{Q}} = \mathbb{R}$.
3. **Frontière :** $\partial \mathbb{Q} = \bar{\mathbb{Q}} \setminus \mathring{\mathbb{Q}} = \mathbb{R} \setminus \emptyset = \mathbb{R}$.

### Exercice 2 : Niveau Avancé (Adhérence d'un produit)
**Énoncé :** Montrer que $\overline{A \times B} = \bar{A} \times \bar{B}$.
**Correction Détaillée :**
On utilise la caractérisation par les voisinages. Un voisinage de $(x, y)$ dans l'espace produit contient un produit de voisinages $V_x \times V_y$.
$(V_x \times V_y) \cap (A \times B) \neq \emptyset \iff (V_x \cap A) \neq \emptyset \text{ et } (V_y \cap B) \neq \emptyset$.
Ceci est vrai pour tous $V_x, V_y$ si et seulement si $x \in \bar{A}$ et $y \in \bar{B}$.

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** En classification, on cherche une **Frontière de Décision** (Decision Boundary). C'est l'ensemble des points où le modèle hésite entre deux classes. Topologiquement, c'est la frontière des deux ensembles de points classés "A" ou "B".
- **Exemple Concret :**
    - **SVM (Support Vector Machines) :** L'objectif est de trouver l'hyperplan qui maximise la distance entre la frontière et les points les plus proches (les vecteurs supports). On travaille ici sur l'intérieur des marges.
    - **Robustesse Adversaire :** Une "attaque adversaire" consiste à prendre un point $x$ dans l'intérieur de la classe "Chat" et à lui ajouter un petit bruit pour le pousser de l'autre côté de la **frontière** de décision, dans la classe "Chien", tout en restant dans l'**adhérence** visuelle de l'image originale. Comprendre la topologie de ces frontières permet de créer des modèles plus robustes.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 49 (Espaces topologiques généraux).md]], [[Jalon 13 (Structure de R).md]]
- **Concepts Futurs dépendants :** [[Jalon 51 (Espaces métriques).md]], [[Jalon 52 (Applications continues entre espaces topologiques et définition fine des homéomorphismes.).md]]
