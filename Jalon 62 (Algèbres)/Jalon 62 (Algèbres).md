---
uuid: "jalon-62"
title: "Algèbres et Tribus (sigma-algèbres)"
year: 2
trimester: 6
tags:
  - math/mesure
  - ia/probabilites
prev: "[[Jalon 61 (Insuffisances de l'intégrale de Riemann).md]]"
next: "[[Jalon 63 (Définition axiomatique d'une mesure).md]]"
---

# Jalon 62 : Algèbres et Tribus ($\sigma$-algèbres)

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous soyez un inspecteur des impôts et que vous vouliez mesurer la richesse d'une ville. Vous ne pouvez pas mesurer chaque grain de poussière. Vous devez décider à quel niveau de détail vous travaillez : les maisons, les quartiers, ou la ville entière. Une **Tribu** (ou $\sigma$-algèbre), c'est simplement la liste officielle de tous les "objets" que vous avez le droit de mesurer.
    - Si vous savez mesurer la maison A, vous savez forcément mesurer tout ce qui n'est pas la maison A (le complémentaire).
    - Si vous savez mesurer plusieurs maisons séparément, vous savez mesurer leur réunion.
    - Une Tribu, c'est un catalogue d'ensembles qui est cohérent et "bouclé" sur lui-même.
- **Le "Pourquoi on a inventé ça" :** On a découvert (paradoxe de Banach-Tarski) qu'on ne peut pas mesurer n'importe quel sous-ensemble de $\mathbb{R}^n$ sans créer de contradictions logiques. On a donc dû restreindre l'usage de la "règle graduée" à une liste précise d'ensembles dits **mesurables**. La Tribu de Borel est cette liste magique qui contient tous les ensembles normaux (intervalles, cercles, etc.).
- **Visualisation :** Un puzzle. Chaque pièce est un élément de la tribu. En assemblant des pièces ou en regardant les trous qu'elles laissent, vous obtenez toujours une forme qui appartient encore au catalogue du puzzle.

## 2. Formalisation

Soit $X$ un ensemble non vide.

### A. Définition d'une Tribu

> **Définition 1 (Tribu / $\sigma$-algèbre) :**
> On appelle **tribu** sur $X$ une famille $\mathcal{F}$ de parties de $X$ vérifiant :
> 1. $X \in \mathcal{F}$ (L'ensemble entier est mesurable).
> 2. **Stabilité par passage au complémentaire :** Si $A \in \mathcal{F}$, alors $X \setminus A \in \mathcal{F}$.
> 3. **Stabilité par réunion dénombrable :** Si $(A_n)_{n \in \mathbb{N}}$ est une suite d'éléments de $\mathcal{F}$, alors $\bigcup_{n \in \mathbb{N}} A_n \in \mathcal{F}$.
> Le couple $(X, \mathcal{F})$ est appelé un **espace mesurable**.

> **Note (Algèbre) :** Une algèbre vérifie les points 1 et 2, mais seulement la réunion **finie** au point 3. Une tribu est donc une algèbre plus "robuste" face à l'infini.

### B. Tribus engendrées et Borel

> **Définition 2 (Tribu engendrée) :**
> Soit $\mathcal{E}$ une famille quelconque de parties de $X$. La tribu engendrée par $\mathcal{E}$, notée $\sigma(\mathcal{E})$, est la plus petite tribu contenant $\mathcal{E}$.

> **Définition 3 (Tribu de Borel) :**
> Sur un espace topologique $X$, on appelle **tribu borélienne** (notée $\mathcal{B}(X)$) la tribu engendrée par tous les **ouverts** de $X$. Sur $\mathbb{R}$, elle est engendrée par tous les intervalles ouverts $]a, b[$.

## 3. Démonstrations

### Démonstration : Stabilité par intersection dénombrable

Montrons que si $\mathcal{F}$ est une tribu, alors l'intersection d'une suite d'éléments de $\mathcal{F}$ appartient encore à $\mathcal{F}$.

1. **Cadre :** Soit $(A_n)_{n \in \mathbb{N}}$ une suite d'éléments de $\mathcal{F}$.
2. **Utilisation des lois de De Morgan :**
   $$\bigcap_{n \in \mathbb{N}} A_n = X \setminus \left( \bigcup_{n \in \mathbb{N}} (X \setminus A_n) \right)$$
3. **Étape par étape :**
   - Par l'axiome 2, chaque $X \setminus A_n$ est dans $\mathcal{F}$.
   - Par l'axiome 3, la réunion $\bigcup (X \setminus A_n)$ est dans $\mathcal{F}$.
   - Par l'axiome 2 à nouveau, le complémentaire de cette réunion est dans $\mathcal{F}$.
4. **Conclusion :** L'intersection dénombrable est bien un élément de la tribu.

## 4. Exercices d'Application

### Exercice 1 : La tribu la plus simple
**Énoncé :** Soit $A \subset X$. Quelle est la tribu engendrée par $\{A\}$ ?
**Correction Détaillée :**
1. Elle doit contenir $X$ et $\emptyset$ (axiome 1 et complémentaire de $X$).
2. Elle doit contenir $A$ (donné).
3. Elle doit contenir $X \setminus A$ (complémentaire).
4. On vérifie que $\mathcal{F} = \{ \emptyset, X, A, X \setminus A \}$ est bien une tribu (toutes les réunions et intersections finies ou dénombrables de ces 4 éléments retombent sur l'un d'eux).
**Résultat :** $\sigma(\{A\}) = \{ \emptyset, X, A, X \setminus A \}$.

### Exercice 2 : Niveau Avancé (Caractérisation des Boréliens)
**Énoncé :** Montrer que la tribu de Borel $\mathcal{B}(\mathbb{R})$ est aussi engendrée par la famille des intervalles fermés $[a, b]$.
**Correction Détaillée :**
1. Chaque fermé $[a, b]$ est un borélien (car complémentaire de deux ouverts $]-\infty, a[ \cup ]b, +\infty[$). Donc $\sigma(\text{fermés}) \subset \mathcal{B}(\mathbb{R})$.
2. Inversement, tout ouvert $]a, b[$ peut s'écrire comme une réunion dénombrable de fermés : $]a, b[ = \bigcup_{n=1}^\infty [a + 1/n, b - 1/n]$. Donc les ouverts appartiennent à la tribu engendrée par les fermés.
**Conclusion :** Les deux tribus sont identiques.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** C'est le fondement axiomatique de la **Théorie des Probabilités** (Axiomes de Kolmogorov, Jalon 85). En IA, chaque fois qu'on écrit $P(X \in A)$, cela n'a de sens que si $A$ appartient à la tribu $\mathcal{F}$.
- **Example Concret :**
    - **Variables Aléatoires :** Une fonction $X : \Omega \to \mathbb{R}$ est une variable aléatoire si elle est **mesurable**, c'est-à-dire que pour tout borélien $B \in \mathcal{B}(\mathbb{R})$, l'événement $\{ \omega \mid X(\omega) \in B \}$ appartient à notre catalogue d'événements $\mathcal{F}$. Si cette condition n'était pas remplie, on ne pourrait pas calculer la probabilité de $X$.
    - **Filtrations (Séries Temporelles) :** Dans l'analyse des flux de données, on utilise une suite croissante de tribus $\mathcal{F}_t$. $\mathcal{F}_t$ représente toute l'information (le "catalogue" de ce qu'on peut mesurer) disponible jusqu'au temps $t$. Cela permet de formaliser mathématiquement qu'une décision prise au temps $t$ ne peut pas dépendre d'informations futures (non mesurables dans $\mathcal{F}_t$).
    - **Modèles de Diffusion :** La théorie mathématique derrière Stable Diffusion repose sur des espérances conditionnelles définies par rapport à des tribus qui capturent le niveau de bruit injecté dans l'image.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 4 (Théorie des ensembles).md]], [[Jalon 49 (Espaces topologiques généraux).md]]
- **Concepts Futurs dépendants :** [[Jalon 63 (Définition axiomatique d'une mesure).md]], [[Jalon 85 (Axiomes de Kolmogorov).md]]
