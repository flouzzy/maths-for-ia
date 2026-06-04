---
uuid: "jalon-5"
title: "Applications, injections, surjections, bijections et composition de fonctions"
year: 1
trimester: 1
tags:
  - math/fondations
  - ia/transformation-donnees
prev: "[[Jalon 4 (Théorie des ensembles).md]]"
next: "[[Jalon 6 (Relations d'équivalence).md]]"
---

# Jalon 5 : Applications, injections, surjections, bijections et composition de fonctions

## 1. Présentation du concept clé
*Cette section doit rendre le concept physique, visuel ou métaphorique sans utiliser aucun formalisme mathématique complexe.*

- **La Métaphore :** Imaginez un archer qui tire des flèches sur des cibles.
  - L'**Application**, c'est la règle du jeu : chaque flèche *doit* être tirée et atteindre *une seule* cible (on ne peut pas rater la cible, ni toucher deux cibles avec une seule flèche).
  - L'**Injection**, c'est quand chaque cible ne reçoit *au plus qu'une* flèche (pas de jaloux, personne ne partage sa cible).
  - La **Surjection**, c'est quand *toutes* les cibles reçoivent au moins une flèche (personne n'est oublié).
  - La **Bijection**, c'est le cas parfait : chaque flèche a sa cible unique, et chaque cible a sa flèche unique. C'est comme un dictionnaire parfait entre deux mondes.
- **Le "Pourquoi on a inventé ça" :** Les mathématiques consistent souvent à transformer des objets en d'autres objets. Les fonctions sont les "machines à transformer". Comprendre si une machine est "réversible" (bijection) ou si elle "perd de l'information" (non injective) est crucial pour savoir si on peut revenir en arrière.
- **Visualisation :** Imaginez deux ensembles de points reliés par des fils. Si les fils ne s'emmêlent jamais sur le même point d'arrivée, c'est injectif. Si chaque point d'arrivée a au moins un fil qui lui arrive dessus, c'est surjectif.

## 2. Formalisation & Rigueur Académique
*Le niveau bascule ici instantanément dans l'exigence pure des mathématiques supérieures.*

### A. Définitions Formelles
Soient $E$ (ensemble de départ) et $F$ (ensemble d'arrivée) deux ensembles.
1. **Application ($f : E \to F$) :** Relation qui à chaque élément $x \in E$ associe un unique élément $y \in F$, noté $f(x)$.
2. **Injection :** $f$ est injective si $\forall x, x' \in E, f(x) = f(x') \Rightarrow x = x'$.
3. **Surjection :** $f$ est surjective si $\forall y \in F, \exists x \in E, y = f(x)$.
4. **Bijection :** $f$ est bijective si elle est à la fois injective et surjective. Cela équivaut à dire que $\forall y \in F, \exists ! x \in E, y = f(x)$.
5. **Composition ($g \circ f$) :** Soient $f : E \to F$ et $g : F \to G$. L'application $g \circ f : E \to G$ est définie par $(g \circ f)(x) = g(f(x))$.

### B. Théorèmes, Propositions & Lemmes
> **Proposition (Composition et Bijection) :**
> Si $f$ et $g$ sont bijectives, alors $g \circ f$ est bijective et $(g \circ f)^{-1} = f^{-1} \circ g^{-1}$.

> **Caractérisation de l'injectivité par la composition :**
> $f$ est injective si et seulement s'il existe une application $g : F \to E$ telle que $g \circ f = Id_E$ (rétraction).

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas
*Rappel : Écris CHAQUE ligne de calcul intermédiaire sans sauter aucune étape.*

### Démonstration du Théorème Pivot : Injection de la composée $g \circ f$
Soient $f : E \to F$ et $g : F \to G$. Montrons que si $f$ et $g$ sont injectives, alors $g \circ f$ est injective.

1. **Initialisation / Cadre :** Soient $x, x' \in E$. Supposons que $(g \circ f)(x) = (g \circ f)(x')$.
   Notre but est de montrer que $x = x'$.

2. **Étape 1 : Utilisation de la définition de la composée**
   $(g \circ f)(x) = (g \circ f)(x') \implies g(f(x)) = g(f(x'))$.

3. **Étape 2 : Utilisation de l'injectivité de $g$**
   Comme $g$ est injective, pour tous $y, y' \in F$, $g(y) = g(y') \implies y = y'$.
   Ici, posons $y = f(x)$ et $y' = f(x')$.
   Puisque $g(f(x)) = g(f(x'))$, alors par injectivité de $g$, on a :
   $$f(x) = f(x')$$

4. **Étape 3 : Utilisation de l'injectivité de $f$**
   Comme $f$ est injective, pour tous $z, z' \in E$, $f(z) = f(z') \implies z = z'$.
   Comme nous avons établi que $f(x) = f(x')$, alors par injectivité de $f$, on a :
   $$x = x'$$

5. **Conclusion :** Nous avons montré que $(g \circ f)(x) = (g \circ f)(x') \Rightarrow x = x'$.
   L'application $g \circ f$ est donc injective. La démonstration est achevée.

## 4. Exercices d'Application & Pratique de Concours
*Proposer au moins 2 exercices progressifs corrigés de façon exhaustive, sans aucune ellipse.*

### Exercice 1 : Application Directe (Fonction réelle)
**Énoncé :** Soit $f : \mathbb{R} \to \mathbb{R}$ définie par $f(x) = 2x + 3$. Démontrer que $f$ est bijective et déterminer sa réciproque $f^{-1}$.
**Correction Détaillée :**
* *Analyse de l'énoncé :* On doit montrer que pour tout $y \in \mathbb{R}$, l'équation $f(x) = y$ possède une unique solution $x \in \mathbb{R}$.
* *Résolution pas-à-pas :*
   1. Soit $y \in \mathbb{R}$. Résolvons $2x + 3 = y$.
   2. $2x = y - 3$.
   3. $x = \frac{y - 3}{2}$.
   4. Comme $y \in \mathbb{R}$, alors $\frac{y - 3}{2}$ est un nombre réel bien défini.
   5. Il existe donc une unique solution $x = \frac{1}{2}y - \frac{3}{2}$ pour chaque $y$.
   6. $f$ est donc bijective.
   7. Sa réciproque est $f^{-1} : \mathbb{R} \to \mathbb{R}$ définie par $f^{-1}(y) = \frac{1}{2}y - \frac{3}{2}$.
* *Conclusion :* La fonction est une bijection de la droite réelle sur elle-même.

### Exercice 2 : Niveau Avancé (Composition et Surjection)
**Énoncé :** Soient $f : E \to F$ et $g : F \to G$. Démontrer que si $g \circ f$ est surjective, alors $g$ est surjective.
**Correction Détaillée :**
* *Analyse de l'énoncé :* On utilise la définition de la surjectivité : atteindre tous les points de l'ensemble d'arrivée.
* *Résolution pas-à-pas :*
   1. Soit $z \in G$. Notre but est de trouver un antécédent $y \in F$ par $g$ tel que $g(y) = z$.
   2. Comme $g \circ f : E \to G$ est surjective, par définition, il existe $x \in E$ tel que $(g \circ f)(x) = z$.
   3. En utilisant la définition de la composition : $g(f(x)) = z$.
   4. Posons $y = f(x)$. Comme $x \in E$ et $f : E \to F$, alors $y$ est un élément de $F$.
   5. Nous avons trouvé un élément $y \in F$ tel que $g(y) = z$.
   6. Cela est vrai pour tout $z \in G$.
* *Conclusion :* L'application $g$ est donc surjective. (Note : On ne peut rien conclure sur la surjectivité de $f$ sans information supplémentaire).

## 5. Ancrage & Application en Intelligence Artificielle
*Démontrer la finalité technologique moderne de ce jalon théorique.*
- **Le Pont Théorique :** Les réseaux de neurones sont des **compositions massives** de fonctions élémentaires (couches).
- **Exemple Concret :** Dans les **Normalizing Flows** (modèles génératifs d'IA), on cherche à apprendre une suite de transformations $f_1, f_2, ..., f_n$ qui sont toutes des **bijections**. Pourquoi ? Parce qu'une bijection permet de transformer une distribution de probabilité simple (comme une Gaussienne) en une distribution complexe (une image), tout en étant capable de faire le calcul inverse (calculer la probabilité d'une image) de manière exacte. Si une couche n'est pas bijective, on perd de l'information et le modèle devient "aveugle" à certaines données.

## 6. Liens Sémantiques & Maillage Obsidian
- **Concepts Précédents requis :** [[Jalon 4 (Théorie des ensembles)]]
- **Concepts Futurs dépendants :** [[Jalon 6 (Relations d'équivalence)]], [[Jalon 52 (Applications continues entre espaces topologiques et définition fine des homéomorphismes.)]], [[Jalon 111 (Applications différentiables entre variétés)]]
