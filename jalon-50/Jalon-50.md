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

## 1. Genèse et Intuition Géométrique

La nécessité d'introduire des opérateurs topologiques tels que l'intérieur, l'adhérence et la frontière découle historiquement du besoin de formaliser rigoureusement les notions intuitives de "bord" et de "proximité" dans des espaces généraux, sans nécessairement s'appuyer sur une distance (comme dans les espaces métriques). Dans la seconde moitié du XIXe siècle et au début du XXe siècle, des mathématiciens comme Georg Cantor (avec ses travaux sur les ensembles de points) et Felix Hausdorff (qui a axiomatisé la topologie générale en 1914) ont cherché à capturer l'essence de la continuité et de la limite.

Dans un espace euclidien, il est facile de voir qu'un disque ouvert n'a pas de "bord" propre, tandis qu'un disque fermé inclut son cercle limite. Mais comment définir cela dans des espaces abstraits, comme des espaces de fonctions en dimension infinie ? C'est là qu'interviennent ces opérateurs purement ensemblistes et topologiques. Ils permettent de stratifier n'importe quel sous-ensemble d'un espace topologique en trois régions mutuellement exclusives (l'intérieur, l'extérieur, et la frontière), offrant ainsi des outils chirurgicaux pour analyser la structure fine de l'espace.

## 2. Définitions Topologiques et Propriétés Fondamentales

Soit $\left(X, \mathcal{T}\right)$ un espace topologique et $A$ une partie de $X$. Nous rappelons qu'un voisinage d'un point $x$ est un sous-ensemble $V \subset X$ contenant un ouvert $O$ tel que $x \in O \subset V$.

### L'Intérieur d'un Ensemble

**Définition 1 (Intérieur) :**
L'intérieur de $A$, noté $\mathring{A}$ ou $\text{Int}(A)$, est le plus grand ouvert contenu dans $A$. Formellement, il est défini comme l'union de tous les ouverts de $X$ qui sont inclus dans $A$ :
$$ \mathring{A} = \bigcup_{O \in \mathcal{T}, O \subset A} O $$
Une caractérisation locale immédiate est qu'un point $x$ appartient à $\mathring{A}$ si et seulement si $A$ est un voisinage de $x$ :
$$ x \in \mathring{A} \iff \exists O \in \mathcal{T}, x \in O \subset A $$

**Exemple Concret (Intérieur dans $\mathbb{R}$) :**
Considérons l'espace topologique usuel $\mathbb{R}$ et l'intervalle semi-ouvert $A = [0, 1[$.
Les points $x \in ]0, 1[$ possèdent tous un voisinage ouvert $]x - \epsilon, x + \epsilon[ \subset A$ (pour $\epsilon > 0$ assez petit, par exemple $\epsilon = \min(x, 1-x)$).
Cependant, pour $x = 0$, tout intervalle ouvert $]-\epsilon, \epsilon[$ contenant $0$ déborde sur les réels strictement négatifs, et n'est donc pas inclus dans $A$.
Par conséquent, $\mathring{A} = ]0, 1[$.

### L'Adhérence d'un Ensemble

**Définition 2 (Adhérence) :**
L'adhérence (ou fermeture) de $A$, notée $\bar{A}$ ou $\text{Cl}(A)$, est le plus petit fermé contenant $A$. Formellement, il est défini comme l'intersection de tous les fermés de $X$ contenant $A$ :
$$ \bar{A} = \bigcap_{F \text{ fermé}, A \subset F} F $$
Une caractérisation locale est qu'un point $x$ appartient à $\bar{A}$ si et seulement si tout voisinage de $x$ rencontre $A$ :
$$ x \in \bar{A} \iff \forall V \in \mathcal{V}(x), V \cap A \neq \emptyset $$

**Exemple Concret (Adhérence dans $\mathbb{R}$) :**
Reprenons $A = [0, 1[$. Tout point $x \in [0, 1[$ est évidemment dans $\bar{A}$. Pour $x = 1$, tout intervalle ouvert $]1-\epsilon, 1+\epsilon[$ rencontre $A$ (il contient par exemple $1 - \frac{\epsilon}{2}$). Donc $1 \in \bar{A}$.
Pour tout $x < 0$ ou $x > 1$, on peut trouver un intervalle ouvert disjoint de $A$.
Par conséquent, $\bar{A} = [0, 1]$.

### La Frontière d'un Ensemble

**Définition 3 (Frontière) :**
La frontière de $A$, notée $\partial A$ ou $\text{Fr}(A)$, est l'ensemble des points qui sont dans l'adhérence de $A$ mais pas dans son intérieur. C'est donc l'intersection de l'adhérence de $A$ et de l'adhérence de son complémentaire :
$$ \partial A = \bar{A} \setminus \mathring{A} = \bar{A} \cap \overline{X \setminus A} $$
Un point $x$ appartient à la frontière si et seulement si tout voisinage de $x$ rencontre à la fois $A$ et son complémentaire $X \setminus A$.

**Exemple Concret (Frontière dans $\mathbb{R}$) :**
Toujours pour $A = [0, 1[$, nous avons $\bar{A} = [0, 1]$ et $\mathring{A} = ]0, 1[$.
Ainsi, $\partial A = [0, 1] \setminus ]0, 1[ = \left\lbrace 0, 1 \right\rbrace$.
Les points $0$ et $1$ sont précisément les points de basculement entre l'appartenance à l'ensemble et son extérieur.

### Ensembles Denses

**Définition 4 (Densité) :**
Un sous-ensemble $A \subset X$ est dit dense dans $X$ si son adhérence est l'espace tout entier :
$$ \bar{A} = X $$
De manière équivalente, $A$ est dense dans $X$ si tout ouvert non vide de $X$ rencontre $A$.

**Exemple Concret (Densité de $\mathbb{Q}$ dans $\mathbb{R}$) :**
L'ensemble des nombres rationnels $\mathbb{Q}$ est dense dans $\mathbb{R}$. En effet, entre deux réels quelconques distincts $a < b$, on peut toujours trouver un nombre rationnel. Ainsi, tout intervalle ouvert non vide de $\mathbb{R}$ contient au moins un rationnel, ce qui implique que l'adhérence de $\mathbb{Q}$ est $\mathbb{R}$ tout entier, soit $\bar{\mathbb{Q}} = \mathbb{R}$.
Par conséquent, l'intérieur de $\mathbb{Q}$ est vide ($\mathring{\mathbb{Q}} = \emptyset$) car aucun intervalle ouvert n'est constitué uniquement de rationnels. Sa frontière est donc $\partial \mathbb{Q} = \mathbb{R}$.

## 3. Démonstrations Explicites

Démontrons formellement la caractérisation locale de l'adhérence.

**Théorème :**
Soit $A \subset X$ et $x \in X$.
$$ x \in \bar{A} \iff \forall V \in \mathcal{V}(x), V \cap A \neq \emptyset $$

**Démonstration :**
Procédons par double implication.

1. **Sens direct ($\implies$) :**
Supposons que $x \in \bar{A}$. Procédons par l'absurde en supposant qu'il existe un voisinage $V$ de $x$ tel que $V \cap A = \emptyset$.
Par définition d'un voisinage, il existe un ouvert $O \in \mathcal{T}$ tel que $x \in O \subset V$.
Puisque $O \subset V$ et $V \cap A = \emptyset$, alors $O \cap A = \emptyset$.
Ceci équivaut à dire que $A \subset X \setminus O$.
Comme $O$ est ouvert, son complémentaire $X \setminus O$ est fermé.
Nous avons donc un fermé $X \setminus O$ qui contient $A$.
Par définition de l'adhérence (plus petit fermé contenant $A$), on doit avoir $\bar{A} \subset X \setminus O$.
Or, nous avons supposé $x \in \bar{A}$, ce qui impliquerait $x \in X \setminus O$, c'est-à-dire $x \notin O$.
C'est une contradiction flagrante avec le fait que $x \in O$.
L'hypothèse initiale est donc fausse, et tout voisinage de $x$ doit rencontrer $A$.

2. **Sens réciproque ($\impliedby$) :**
Supposons que pour tout voisinage $V$ de $x$, nous avons $V \cap A \neq \emptyset$.
Montrons que $x \in \bar{A}$.
Soit $F$ un fermé arbitraire tel que $A \subset F$.
Procédons par l'absurde en supposant que $x \notin F$.
Alors $x \in X \setminus F$.
Puisque $F$ est fermé, $X \setminus F$ est un ouvert.
Étant un ouvert contenant $x$, $X \setminus F$ est un voisinage de $x$.
Par notre hypothèse de départ, tout voisinage de $x$ rencontre $A$, donc $(X \setminus F) \cap A \neq \emptyset$.
Cependant, nous savons par définition de $F$ que $A \subset F$, ce qui implique $(X \setminus F) \cap A = \emptyset$.
Nous obtenons à nouveau une contradiction.
Par conséquent, $x$ doit appartenir à tous les fermés $F$ contenant $A$.
Il appartient donc à leur intersection, ce qui signifie que $x \in \bar{A}$.

## 4. Applications en Apprentissage Automatique (Machine Learning)

Les concepts d'intérieur, d'adhérence et de frontière ont des répercussions fondamentales dans la théorie de l'apprentissage automatique, en particulier dans la classification et l'étude de la robustesse.

1. **Frontière de Décision (Decision Boundary) :**
En classification binaire, un modèle (comme un réseau de neurones ou une SVM) partitionne l'espace des entrées $X$ en deux régions, par exemple $C_1$ (les chats) et $C_2$ (les chiens). La frontière de décision est exactement la frontière topologique $\partial C_1$ (qui est souvent partagée avec $\partial C_2$). Sur cette frontière, la probabilité prédite par le modèle pour chaque classe est de $0.5$ ; le modèle est dans un état d'incertitude maximale.

2. **Robustesse et Marge (Adversarial Robustness) :**
Lorsqu'une donnée $x$ est correctement classifiée, elle se trouve dans l'intérieur $\mathring{C_1}$ de la région de sa vraie classe.
Une attaque adversaire (Adversarial Attack) cherche à trouver une perturbation minimale $\delta$ telle que $x + \delta$ traverse la frontière $\partial C_1$ pour atterrir dans $C_2$.
La distance de $x$ à la frontière $\partial C_1$ représente la "marge" ou le rayon du plus grand voisinage (ouvert) centré en $x$ qui reste entièrement inclus dans $\mathring{C_1}$. Maximiser cette marge, c'est précisément s'assurer que les données se trouvent profondément dans l'intérieur de leur classe, garantissant ainsi une forte robustesse face aux bruits topologiques.
