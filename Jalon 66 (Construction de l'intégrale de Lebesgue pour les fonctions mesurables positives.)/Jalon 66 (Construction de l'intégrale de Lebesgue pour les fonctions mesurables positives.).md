---
uuid: "jalon-66"
title: "Intégrale de Lebesgue pour les fonctions positives"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 65 (Fonctions mesurables).md]]"
next: "[[Jalon 67 (Démonstration du théorème de convergence monotone).md]]"
---

# Jalon 66 : Intégrale de Lebesgue pour les fonctions positives

## 1. Présentation du concept clé

- **La Métaphore :** Imaginez que vous vouliez calculer l'aire totale de confiture étalée sur une table.
    - La confiture n'est pas étalée de manière régulière : il y a des endroits où elle est épaisse et d'autres où elle est très fine.
    - Au lieu de découper la table en carrés (méthode de Riemann), vous décidez d'utiliser des **tampons** de différentes tailles. Chaque tampon a une épaisseur de confiture précise (une valeur $a_i$).
    - Vous cherchez tous les endroits où l'épaisseur est exactement $a_i$ (l'ensemble $A_i$), vous mesurez la surface de ces endroits ($\mu(A_i)$), et vous multipliez par l'épaisseur.
    - En faisant cela pour toutes les épaisseurs possibles et en additionnant, vous obtenez le volume total de confiture.
- **Le "Pourquoi on a inventé ça" :** Pour pouvoir intégrer des fonctions qui "sautent" partout (comme la fonction de Dirichlet). La construction de Lebesgue est descendante : on définit l'intégrale pour des briques très simples, puis on généralise par un passage au supremum.
- **Visualisation :** On remplit l'espace sous la courbe par des "rectangles horizontaux" de plus en plus nombreux et de plus en plus fins.

## 2. Formalisation

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### A. Intégrale des Fonctions Simples

Soit $\mathcal{S}_+$ l'ensemble des fonctions simples (étagées) positives sur $X$.
Une fonction $s \in \mathcal{S}_+$ s'écrit $s = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$ avec $a_i \ge 0$.

> **Définition 1 :** L'intégrale de la fonction simple $s$ par rapport à $\mu$ est :
> $$\int_X s d\mu = \sum_{i=1}^n a_i \mu(A_i)$$
> (On utilise la convention $0 \cdot \infty = 0$).

### B. Intégrale des Fonctions Mesurables Positives

Soit $\mathcal{M}_+$ l'ensemble des fonctions mesurables de $X$ dans $[0, +\infty]$.

> **Définition 2 (Intégrale de Lebesgue) :**
> Pour tout $f \in \mathcal{M}_+$, on définit :
> $$\int_X f d\mu = \sup \left\{ \int_X s d\mu \mid s \in \mathcal{S}_+, 0 \le s \le f \right\}$$
> Cette valeur appartient à $[0, +\infty]$. Si elle est finie, on dit que $f$ est **intégrable**.

### C. Propriétés Immédiates

> **Théorème :**
> 1. **Positivité :** $\int f d\mu \ge 0$.
> 2. **Croissance :** Si $f \le g$, alors $\int f \le \int g$.
> 3. **Homogénéité :** $\int \alpha f d\mu = \alpha \int f d\mu$ pour $\alpha \ge 0$.

## 3. Démonstrations

### Démonstration : Relation entre intégrale et ensembles de mesure nulle

Montrons que si $f \in \mathcal{M}_+$ et $\int f d\mu = 0$, alors $f = 0$ presque partout (c'est-à-dire $\mu(\{x \mid f(x) > 0\}) = 0$).

1. **Cadre :** Soit $A = \{x \in X \mid f(x) > 0\}$. On veut montrer $\mu(A) = 0$.
2. **Décomposition de l'ensemble :** Posons $A_n = \{x \in X \mid f(x) \ge 1/n\}$ pour $n \in \mathbb{N}^*$.
   Alors $A = \bigcup_{n=1}^\infty A_n$.
3. **Inégalité sur chaque morceau :** On remarque que $f \ge \frac{1}{n} \mathbf{1}_{A_n}$.
   Par croissance de l'intégrale :
   $$\int_X f d\mu \ge \int_X \frac{1}{n} \mathbf{1}_{A_n} d\mu = \frac{1}{n} \mu(A_n)$$
4. **Utilisation de l'hypothèse :** Comme $\int f d\mu = 0$, alors pour tout $n$, $\frac{1}{n} \mu(A_n) = 0$, donc $\mu(A_n) = 0$.
5. **Conclusion :** Par $\sigma$-sous-additivité de la mesure :
   $$\mu(A) = \mu\left( \bigcup_{n=1}^\infty A_n \right) \le \sum_{n=1}^\infty \mu(A_n) = 0$$
   Donc $f$ est nulle presque partout.

## 4. Exercices d'Application

### Exercice 1 : Intégrale de la fonction de Dirichlet
**Énoncé :** Calculer l'intégrale de Lebesgue de $f = \mathbf{1}_\mathbb{Q}$ sur $[0, 1]$ pour la mesure de Lebesgue $\lambda$.
**Correction Détaillée :**
1. $f$ est une fonction simple car elle ne prend que les valeurs 0 et 1.
2. Par définition : $\int_{[0,1]} f d\lambda = 1 \cdot \lambda(\mathbb{Q}) + 0 \cdot \lambda([0,1] \setminus \mathbb{Q})$.
3. On sait que $\lambda(\mathbb{Q}) = 0$ (Jalon 64).
4. Donc $\int f d\lambda = 1 \cdot 0 + 0 = 0$.
**Remarque :** Lebesgue réussit là où Riemann échouait (Jalon 61).

### Exercice 2 : Niveau Avancé (Mesure de comptage)
**Énoncé :** Soit $\mu$ la mesure de comptage sur $\mathbb{N}$ ($\mu(A) = \text{card}(A)$). Que vaut $\int_{\mathbb{N}} f d\mu$ pour une fonction $f : \mathbb{N} \to \mathbb{R}_+$ ?
**Correction Détaillée :**
Toute fonction sur $\mathbb{N}$ est limite de fonctions simples (sommes finies). L'intégrale de Lebesgue par rapport à la mesure de comptage est exactement la somme de la série :
$$\int_{\mathbb{N}} f d\mu = \sum_{n=0}^\infty f(n)$$
La théorie de Lebesgue unifie donc le calcul intégral et le calcul des séries.

## 5. Application en Intelligence Artificielle

- **Le Pont Théorique :** L'intégrale de Lebesgue permet de définir l'**Espérance mathématique** de manière universelle, que la variable soit discrète, continue ou mixte. $\mathbb{E}[X] = \int_\Omega X(\omega) dP(\omega)$.
- **Example Concret :**
    - **Calcul de la Perte Attendue (Expected Loss) :** En IA, on minimise $L(\theta) = \int \ell(x, y, \theta) d\mathbb{P}(x, y)$. La mesure $\mathbb{P}$ représente nos données. Lebesgue nous permet de calculer cette intégrale même si nos données sont un mélange de catégories (discret) et de mesures physiques (continu).
    - **Mesures de similarité entre distributions :** La divergence de Jensen-Shannon ou la divergence KL sont définies par des intégrales de Lebesgue. Ces mesures sont le cœur des modèles génératifs et du clustering.
    - **Filtrage de Kalman :** La mise à jour des croyances dans un système dynamique repose sur l'intégration de fonctions de vraisemblance, souvent sur des espaces de grande dimension.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 65 (Fonctions mesurables).md]], [[Jalon 63 (Définition axiomatique d'une mesure).md]]
- **Concepts Futurs dépendants :** [[Jalon 67 (Démonstration du théorème de convergence monotone).md]], [[Jalon 73 (Définition des espaces Lp).md]]
