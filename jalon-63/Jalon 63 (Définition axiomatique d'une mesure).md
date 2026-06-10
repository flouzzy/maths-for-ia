---
uuid: "jalon-63"
title: "Définition axiomatique d'une mesure"
year: 2
trimester: 6
tags:
  - math/mesure
  - ia/probabilites
prev: "[[Jalon 62 (Algèbres).md]]"
next: "[[Jalon 64 (Construction pas à pas de la mesure de Lebesgue sur Rn via la mesure extérieure.).md]]"
---

# Jalon 63 : Définition axiomatique d'une mesure

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous ayez une balance de précision. Vous voulez peser différents objets (les ensembles de votre tribu). La balance doit respecter trois règles de bon sens :
    1. Un objet ne peut pas avoir un poids négatif (positivité).
    2. Si vous n'avez rien sur la balance, elle doit afficher zéro ($\mu(\emptyset) = 0$).
    3. Si vous posez deux objets séparés sur la balance, le poids total doit être la somme des poids de chaque objet. Mieux encore : cela doit marcher même si vous posez une infinité d'objets les uns après les autres (c'est la $\sigma$-additivité).
    Une **Mesure**, c'est simplement cette balance universelle qui permet de dire "quelle place prend" un ensemble dans l'espace.
- **Le "Pourquoi on a inventé ça" :** Avant, on mesurait des longueurs, des aires ou des volumes avec des formules différentes. La théorie de la mesure unifie tout cela dans un seul concept abstrait. Que ce soit la longueur d'un segment, la probabilité d'un événement ou le nombre d'éléments dans un ensemble, tout est une mesure.
- **Visualisation :** De la pâte à modeler étalée sur une table. La mesure, c'est la quantité de pâte qu'il y a sur une zone donnée. Si vous regroupez deux zones disjointes, vous additionnez simplement la quantité de pâte.

## 2. Formalisation

Soit $(X, \mathcal{F})$ un espace mesurable.

### A. Définition d'une Mesure

> **Définition 1 (Mesure) :**
> On appelle **mesure** sur $(X, \mathcal{F})$ une application $\mu : \mathcal{F} \to [0, +\infty]$ vérifiant :
> 1. $\mu(\emptyset) = 0$.
> 2. **$\sigma$-additivité :** Pour toute suite $(A_n)_{n \in \mathbb{N}}$ d'éléments de $\mathcal{F}$ **deux à deux disjoints** :
>    $$\mu\left( \bigcup_{n \in \mathbb{N}} A_n \right) = \sum_{n=0}^{+\infty} \mu(A_n)$$
> Le triplet $(X, \mathcal{F}, \mu)$ est appelé un **espace mesuré**.

### B. Types de Mesures

1. **Mesure de Probabilité :** Si $\mu(X) = 1$. On la note souvent $P$.
2. **Mesure finie :** Si $\mu(X) < +\infty$.
3. **Mesure $\sigma$-finie :** Si $X$ peut être écrit comme une union dénombrable d'ensembles de mesure finie (ex: la mesure de Lebesgue sur $\mathbb{R}$).

### C. Propriétés Fondamentales

> **Théorème (Continuité monotone) :**
> 1. **Croissance :** Si $(A_n)$ est une suite croissante ($A_n \subset A_{n+1}$), alors $\mu(\bigcup A_n) = \lim \mu(A_n)$.
> 2. **Décroissance :** Si $(A_n)$ est une suite décroissante ($A_{n+1} \subset A_n$) ET $\mu(A_0) < +\infty$, alors $\mu(\bigcap A_n) = \lim \mu(A_n)$.

## 3. Démonstrations

### Démonstration : La continuité par le bas (croissance)

1. **Cadre :** Soit $(A_n)$ une suite croissante d'ensembles mesurables. Posons $A = \bigcup A_n$.
2. **Construction d'ensembles disjoints :**
   On définit $B_0 = A_0$ and $B_n = A_n \setminus A_{n-1}$ pour $n \ge 1$.
   Par construction, les $(B_n)$ sont deux à deux disjoints et leur union est aussi $A$. De plus, $A_n = B_0 \cup B_1 \cup \dots \cup B_n$.
3. **Utilisation de la $\sigma$-additivité :**
   $$\mu(A) = \mu\left( \bigcup_{n=0}^\infty B_n \right) = \sum_{n=0}^\infty \mu(B_n)$$
4. **Passage aux sommes partielles :**
   $$\sum_{n=0}^\infty \mu(B_n) = \lim_{N \to \infty} \sum_{n=0}^N \mu(B_n)$$
   Par additivité finie, $\sum_{n=0}^N \mu(B_n) = \mu(\bigcup_{n=0}^N B_n) = \mu(A_N)$.
5. **Conclusion :** $\mu(A) = \lim_{N \to \infty} \mu(A_N)$.

## 4. Exercices d'Application

### Exercice 1 : La mesure de Dirac
**Énoncé :** Soit $a \in X$. On définit $\delta_a(A) = 1$ si $a \in A$ et $0$ sinon. Montrer que $\delta_a$ est une mesure de probabilité.
**Correction Détaillée :**
1. $\delta_a(\emptyset) = 0$ car $a \notin \emptyset$.
2. Soit $(A_n)$ disjoints. Si $a \in \bigcup A_n$, alors $a$ appartient à exactement un seul $A_k$ (car ils sont disjoints). Donc $\delta_a(\cup A_n) = 1$ et $\sum \delta_a(A_n) = \delta_a(A_k) = 1$. Si $a$ n'est dans aucun $A_n$, les deux côtés valent 0.
3. $\delta_a(X) = 1$ car $a \in X$. C'est une mesure de probabilité.

### Exercice 2 : Niveau Avancé (Sous-additivité)
**Énoncé :** Montrer que pour toute suite $(A_n)$ (non nécessairement disjoints), $\mu(\bigcup A_n) \le \sum \mu(A_n)$.
**Correction Détaillée :**
On utilise la même technique que dans la preuve de la continuité : on définit $B_n = A_n \setminus (\cup_{i < n} A_i)$. Les $B_n$ sont disjoints, inclus dans $A_n$, et leur union est la même que celle des $A_n$.
$\mu(\cup A_n) = \mu(\cup B_n) = \sum \mu(B_n)$.
Comme $B_n \subset A_n$, par croissance de la mesure (démontrée par $\mu(A) = \mu(B) + \mu(A\setminus B) \ge \mu(B)$), on a $\mu(B_n) \le \mu(A_n)$.
D'où l'inégalité de Boole.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, nous ne manipulons pas des points, mais des **distributions**. Une distribution de données est une mesure de probabilité sur l'espace des caractéristiques.
- **Example Concret :**
    - **Data Drift (Dérive des données) :** On dit qu'il y a une dérive si la mesure de probabilité des données en production $\mu_{prod}$ est différente de celle de l'entraînement $\mu_{train}$. Pour mesurer cet écart, on utilise des outils comme la distance de Wasserstein (Jalon 51) qui sont définis sur l'espace des mesures.
    - **Noyaux de convolution :** En vision par ordinateur, on peut voir un filtre comme une mesure locale. L'opération de convolution est en fait une intégrale par rapport à cette mesure.
    - **Processus de Dirichlet :** En apprentissage Bayésien non-paramétrique, on définit une "mesure sur les mesures". Cela permet de créer des modèles dont le nombre de paramètres (ex: nombre de clusters) s'adapte automatiquement à la complexité des données.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 62 (Algèbres).md]], [[Jalon 14 (Suites réelles et complexes).md]]
- **Concepts Futurs dépendants :** [[Jalon 64 (Construction pas à pas de la mesure de Lebesgue sur Rn via la mesure extérieure.).md]], [[Jalon 85 (Axiomes de Kolmogorov).md]]
