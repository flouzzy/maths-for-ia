---
uuid: "jalon-65"
title: "Fonctions mesurables"
year: 2
trimester: 6
tags:
  - math/mesure
  - ia/abstraction
prev: "[[Jalon 64 (Construction pas à pas de la mesure de Lebesgue sur Rn via la mesure extérieure.).md]]"
next: "[[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]]"
---

# Jalon 65 : Fonctions mesurables

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous soyez un douanier. Vous avez une liste officielle des objets autorisés à passer (votre **Tribu**). Une fonction, c'est comme une machine qui transforme un objet A en un objet B. Pour que la machine soit "mesurable", il faut qu'elle soit transparente : si je vous donne un critère sur le résultat final (ex: "est-ce que le résultat pèse plus de 1kg ?"), vous devez être capable de me dire quels objets au départ satisfont ce critère, et ces objets de départ doivent être dans votre liste officielle (ils doivent être mesurables). Si la machine mélange les choses de manière si complexe que vous ne pouvez plus identifier les coupables dans votre liste, alors la fonction n'est pas mesurable.
- **Le "Pourquoi on a inventé ça" :** On ne peut pas intégrer n'importe quelle fonction. Pour pouvoir calculer $\int f d\mu$, il faut que la fonction $f$ "respecte" la structure de la tribu $\mathcal{F}$. C'est la condition de base pour que la théorie des probabilités et de l'intégration fonctionne sans bugs logiques.
- **Visualisation :** Les **fonctions simples** (ou étagées). Ce sont des fonctions qui ressemblent à des escaliers : elles ne prennent qu'un nombre fini de valeurs. On construit toutes les autres fonctions complexes en empilant ces Lego bricks.

## 2. Formalisation

Soient $(X, \mathcal{F})$ et $(Y, \mathcal{G})$ deux espaces mesurables.

### A. Définition de la Mesurabilité

> **Définition 1 (Fonction mesurable) :**
> Une application $f : X \to Y$ est dite **mesurable** si l'image réciproque de tout ensemble mesurable de $Y$ est un ensemble mesurable de $X$ :
> $$\forall B \in \mathcal{G}, \quad f^{-1}(B) \in \mathcal{F}$$

> **Définition 2 (Fonction Borélienne) :**
> Si $Y = \mathbb{R}$ muni de sa tribu de Borel $\mathcal{B}(\mathbb{R})$, $f$ est dite **borélienne** si l'image réciproque de tout ouvert (ou de tout intervalle) est dans $\mathcal{F}$.

### B. Opérations sur les fonctions mesurables

> **Théorème (Stabilité) :**
> Soient $f, g : X \to \mathbb{R}$ deux fonctions mesurables. Alors :
> 1. $f+g$, $f \cdot g$, $\lambda f$ sont mesurables.
> 2. $\max(f, g)$ and $\min(f, g)$ sont mesurables.
> 3. Si $(f_n)$ est une suite de fonctions mesurables, alors $\sup f_n$, $\inf f_n$, $\limsup f_n$ et $\liminf f_n$ sont mesurables.

### C. Fonctions Simples (Étagées)

> **Définition 3 (Fonction simple) :**
> Une fonction $s : X \to \mathbb{R}$ est dite **simple** si elle est mesurable et si elle ne prend qu'un nombre fini de valeurs $\{a_1, \dots, a_n\}$. Elle s'écrit sous la forme :
> $$s(x) = \sum_{i=1}^n a_i \mathbf{1}_{A_i}(x)$$
> où $A_i = f^{-1}(\{a_i\}) \in \mathcal{F}$ sont des ensembles disjoints.

## 3. Démonstrations

### Démonstration : Le supremum d'une suite est mesurable

1. **Cadre :** Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $X$ dans $\mathbb{R}$. Posons $h(x) = \sup_{n} f_n(x)$.
2. **Critère de mesurabilité :** Il suffit de montrer que pour tout $a \in \mathbb{R}$, l'ensemble $h^{-1}(]a, +\infty[)$ est mesurable.
3. **Analyse logique :**
   $h(x) > a \iff \sup_n f_n(x) > a$.
   Par définition du supremum, cela arrive si et seulement s'**il existe au moins un** $n$ tel que $f_n(x) > a$.
4. **Traduction ensembliste :**
   $$h^{-1}(]a, +\infty[) = \bigcup_{n \in \mathbb{N}} f_n^{-1}(]a, +\infty[)$$
5. **Conclusion :**
   - Comme chaque $f_n$ est mesurable, chaque ensemble $f_n^{-1}(]a, +\infty[)$ appartient à la tribu $\mathcal{F}$.
   - Comme une tribu est stable par union dénombrable (Axiome 3), leur réunion appartient à $\mathcal{F}$.
   - Donc $h$ est mesurable.

## 4. Exercices d'Application

### Exercice 1 : La fonction indicatrice
**Énoncé :** Soit $A \subset X$. Montrer que la fonction indicatrice $\mathbf{1}_A$ est mesurable si et seulement si $A \in \mathcal{F}$.
**Correction Détaillée :**
1. **Sens ($\implies$) :** Si $\mathbf{1}_A$ est mesurable, alors $A = \mathbf{1}_A^{-1}(\{1\})$. Comme $\{1\}$ est un borélien de $\mathbb{R}$, son image réciproque $A$ doit être dans $\mathcal{F}$.
2. **Sens ($\impliedby$) :** Si $A \in \mathcal{F}$, alors pour tout borélien $B$ de $\mathbb{R}$, $\mathbf{1}_A^{-1}(B)$ peut être $X$ (si $0, 1 \in B$), $\emptyset$ (si aucun), $A$ (si $1 \in B, 0 \notin B$) ou $X \setminus A$ (si $0 \in B, 1 \notin B$). Dans tous les cas, le résultat est dans $\mathcal{F}$.

### Exercice 2 : Niveau Avancé (Approximation)
**Énoncé :** Montrer que toute fonction mesurable positive $f$ est la limite simple d'une suite croissante de fonctions simples.
**Correction Détaillée :**
On découpe l'axe des ordonnées (les $y$) en tranches de largeur $1/2^n$. On définit $s_n(x) = k/2^n$ si $k/2^n \le f(x) < (k+1)/2^n$ (pour $k < n 2^n$) et $n$ sinon. C'est l'analogue horizontal des sommes de Riemann. On vérifie que $s_n \le s_{n+1}$ et $s_n \to f$.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, les **Variables Aléatoires** sont par définition des fonctions mesurables. De même, les **Classifieurs** et les **Régresseurs** sont des fonctions dont on doit garantir la mesurabilité pour pouvoir calculer leur erreur moyenne (le risque).
- **Example Concret :**
    - **Activations :** Les fonctions ReLU, Sigmoïde, Tanh sont continues, donc boréliennes. Leurs compositions (les réseaux de neurones) sont donc aussi mesurables.
    - **Seuillage (Thresholding) :** Un classifieur binaire $h(x) = \mathbf{1}_{f(x) > 0.5}$ est mesurable si la fonction de score $f$ l'est. C'est ce qui permet de définir la tribu des "décisions".
    - **Calcul de l'espérance :** Pour calculer $\mathbb{E}[f(X)]$, il faut que la composition $f \circ X$ soit mesurable. La stabilité par composition garantit que l'on peut manipuler des transformations complexes de données sans perdre le cadre probabiliste.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 62 (Algèbres).md]], [[Jalon 52 (Applications continues entre espaces topologiques et définition fine des homéomorphismes.).md]]
- **Concepts Futurs dépendants :** [[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]], [[Jalon 86 (Variables aléatoires vues comme des applications mesurables).md]]
