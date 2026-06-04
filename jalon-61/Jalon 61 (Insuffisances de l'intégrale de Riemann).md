---
uuid: "jalon-61"
title: "Insuffisances de l'intégrale de Riemann"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 60 (Livrable IA).md]]"
next: "[[Jalon 62 (Algèbres).md]]"
---

# Jalon 61 : Insuffisances de l'intégrale de Riemann

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous soyez un caissier et que vous deviez compter l'argent dans une boîte remplie de pièces de monnaie mélangées.
    - **La méthode de Riemann**, c'est de prendre les pièces dans l'ordre où elles viennent dans la boîte, une par une, et de faire l'addition. Si les pièces sont bien rangées, ça va. Mais si elles sont éparpillées au hasard, vous risquez de vous perdre.
    - **La méthode de Lebesgue**, c'est de d'abord trier les pièces par valeur : vous faites une pile de 1€, une pile de 2€, etc. Puis vous mesurez la "taille" de chaque pile (combien il y a de pièces) et vous multipliez par la valeur. C'est beaucoup plus robuste !
- **Le "Pourquoi on a inventé ça" :** L'intégrale de Riemann (découper en petits rectangles verticaux) marche très bien pour les fonctions lisses. Mais dès que la fonction devient "sauvage" (elle saute tout le temps, comme un signal avec beaucoup de bruit), la méthode des rectangles échoue. On avait besoin d'une intégrale plus puissante pour traiter des cas limites et construire des espaces de fonctions "complets" (sans trous).
- **Visualisation :** La fonction de Dirichlet. Imaginez un nuage de points où chaque nombre rationnel vaut 1 et chaque nombre irrationnel vaut 0. Si vous essayez de dessiner des rectangles en dessous, vous ne saurez jamais s'ils doivent avoir une hauteur de 0 ou de 1. L'aire semble impossible à définir avec Riemann.

## 2. Formalisation & Rigueur Académique

### A. Rappel : Intégrabilité au sens de Riemann

Une fonction $f : [a, b] \to \mathbb{R}$ est Riemann-intégrable si ses sommes de Darboux inférieure ($s$) et supérieure ($S$) convergent vers la même valeur (voir Jalon 37).
- $s(f, \sigma) = \sum \inf_{t \in I_k} f(t) \cdot \Delta x_k$
- $S(f, \sigma) = \sum \sup_{t \in I_k} f(t) \cdot \Delta x_k$

### B. La fonction de Dirichlet : Le premier échec

Soit $f : [0, 1] \to \mathbb{R}$ définie par :
$$f(x) = \begin{cases} 1 & \text{si } x \in \mathbb{Q} \\ 0 & \text{si } x \notin \mathbb{Q} \end{cases}$$

> **Proposition :** La fonction de Dirichlet n'est pas Riemann-intégrable sur $[0, 1]$.

### C. Défaut de complétude des espaces de Riemann

L'ensemble des fonctions Riemann-intégrables muni de la norme $\|f\|_1 = \int |f|$ n'est pas un espace complet (pas un Banach). On peut construire une suite de fonctions "gentilles" dont la limite est "sauvage" et non intégrable par Riemann.

## 3. Le Noyau Dur : Démonstrations Pas-à-Pas

### Démonstration : Non-intégrabilité de la fonction de Dirichlet

1. **Cadre :** Soit $\sigma = (x_0, \dots, x_n)$ une subdivision quelconque de $[0, 1]$.
2. **Étude des infimums :** Sur chaque intervalle $I_k = [x_{i-1}, x_i]$, il existe une infinité de nombres irrationnels (densité de $\mathbb{R} \setminus \mathbb{Q}$).
   Donc $\inf_{t \in I_k} f(t) = 0$.
   La somme de Darboux inférieure est $s(f, \sigma) = \sum 0 \cdot \Delta x_i = 0$.
3. **Étude des supremums :** Sur chaque intervalle $I_k$, il existe une infinité de nombres rationnels (densité de $\mathbb{Q}$).
   Donc $\sup_{t \in I_k} f(t) = 1$.
   La somme de Darboux supérieure est $S(f, \sigma) = \sum 1 \cdot \Delta x_i = \text{longueur du segment} = 1$.
4. **Conclusion :** Pour toute subdivision, $s(f, \sigma) = 0$ et $S(f, \sigma) = 1$.
   Comme $0 \neq 1$, l'intégrale inférieure et l'intégrale supérieure ne coïncident jamais. La fonction n'est pas Riemann-intégrable.

## 4. Exercices d'Application & Pratique de Concours

### Exercice 1 : Limite de fonctions intégrables
**Énoncé :** Soit $q_1, q_2, \dots$ une énumération des rationnels de $[0, 1]$. On définit $f_n(x) = 1$ si $x \in \{q_1, \dots, q_n\}$ et $0$ sinon.
1. Montrer que chaque $f_n$ est Riemann-intégrable et calculer son intégrale.
2. Quelle est la limite simple $f$ de cette suite ? $f$ est-elle Riemann-intégrable ?
**Correction Détaillée :**
1. $f_n$ est une fonction en escalier (avec des paliers de largeur nulle). Son intégrale est $\int f_n = 0$.
2. $\lim f_n = f$, où $f$ est la fonction de Dirichlet.
3. On a vu que $f$ n'est pas Riemann-intégrable.
**Conclusion :** On ne peut pas intervertir la limite et l'intégrale de Riemann de manière générale ($\lim \int f_n \neq \int \lim f_n$), ce qui est une grave faiblesse théorique.

### Exercice 2 : Niveau Avancé (Ensembles négligeables)
**Énoncé :** On dit qu'une fonction est Riemann-intégrable si et seulement si l'ensemble de ses points de discontinuité est "négligeable" (Théorème de Lebesgue-Vitali). Pourquoi la fonction de Dirichlet échoue-t-elle ici ?
**Correction Détaillée :**
La fonction de Dirichlet est discontinue en **tout point** de $[0, 1]$. L'ensemble des points de discontinuité est donc $[0, 1]$, qui n'est absolument pas négligeable (sa longueur est 1).

## 5. Ancrage & Application en Intelligence Artificielle

- **Le Pont Théorique :** En IA, nous manipulons des **variables aléatoires**. La définition moderne d'une probabilité repose sur l'intégrale de Lebesgue. Sans elle, on ne pourrait pas traiter proprement les distributions qui mélangent du continu et du discret (ex: un capteur qui donne une valeur précise 0.5 avec une probabilité 0.1, et une valeur continue ailleurs).
- **Example Concret :**
    - **Théorie de l'Information :** L'entropie et la divergence KL pour des distributions complexes nécessitent le cadre de Lebesgue pour être bien définies.
    - **Processus Stochastiques :** Le mouvement Brownien (utilisé en finance ou pour modéliser le bruit) a des trajectoires qui sont continues presque partout mais dérivables nulle part. L'intégrale de Riemann explose face à de tels objets, alors que la théorie de Lebesgue les gère parfaitement.
    - **Loi de probabilité de Dirac :** En traitement du signal ou en IA, on utilise souvent des "pics" de probabilité ($\delta$). C'est une mesure de Lebesgue, mais ce n'est pas une fonction intégrable au sens de Riemann.

## 6. Liens Sémantiques & Maillage Obsidian

- **Concepts Précédents requis :** [[Jalon 37 (Intégrale de Riemann sur un segment).md]], [[Jalon 13 (Structure de R).md]]
- **Concepts Futurs dépendants :** [[Jalon 63 (Définition axiomatique d'une mesure).md]], [[Jalon 66 (Construction de l'intégrale de Lebesgue pour les fonctions mesurables positives.).md]]
