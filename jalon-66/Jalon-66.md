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

## 1. Introduction et Genèse

La construction de l'intégrale de Lebesgue repose sur une approche fondamentale différente de celle de Riemann.
Au lieu de découper le domaine de définition (la méthode de Riemann), on découpe l'ensemble d'arrivée en considérant des "tampons" horizontaux de valeurs.
Chaque niveau de valeur $a_i$ définit un ensemble de points $A_i$ où la fonction prend cette valeur. En mesurant la "surface" de ces ensembles (grâce à la mesure $\mu(A_i)$) et en la multipliant par la valeur $a_i$, on obtient l'intégrale.

Cette approche descendante permet d'intégrer des fonctions hautement irrégulières (qui "sautent" partout, comme la fonction de Dirichlet) en définissant d'abord l'intégrale pour des fonctions en escalier très simples, puis en généralisant par passage au supremum.

## 2. Définitions, Théorèmes et Exemples Concrets

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
> $$\int_X f d\mu = \sup \left\lbrace \int_X s d\mu \mid s \in \mathcal{S}_+, 0 \le s \le f \right\rbrace$$
> Cette valeur appartient à $[0, +\infty]$. Si elle est finie, on dit que $f$ est **intégrable**.

### Exemples Concrets

**Exemple 1 : Intégrale d'une fonction simple sur un espace fini**
Soit $X = \{1, 2, 3\}$ avec la mesure de comptage $\mu$.
Considérons la fonction $s : X \to \mathbb{R}_+$ définie par $s(1) = 5$, $s(2) = 0$, $s(3) = 2$.
$s$ peut s'écrire comme $s = 5 \cdot \mathbf{1}_{\{1\}} + 0 \cdot \mathbf{1}_{\{2\}} + 2 \cdot \mathbf{1}_{\{3\}}$.
L'intégrale de $s$ par rapport à $\mu$ est :
$$\int_X s d\mu = 5 \cdot \mu(\{1\}) + 0 \cdot \mu(\{2\}) + 2 \cdot \mu(\{3\}) = 5(1) + 0(1) + 2(1) = 7.$$

**Exemple 2 : Fonction indicatrice sur $\mathbb{R}$**
Soit $X = \mathbb{R}$ muni de la mesure de Lebesgue $\lambda$. Soit $s = 3 \cdot \mathbf{1}_{[0, 2]} + 4 \cdot \mathbf{1}_{[3, 4]}$.
L'intégrale est :
$$\int_\mathbb{R} s d\lambda = 3 \cdot \lambda([0, 2]) + 4 \cdot \lambda([3, 4]) = 3(2 - 0) + 4(4 - 3) = 6 + 4 = 10.$$

**Exemple 3 : Approximation d'une fonction par une fonction étagée**
Considérons $f(x) = x$ sur $[0, 1]$. Pour $n = 2$, on peut minorer $f$ par la fonction simple $s_2 = 0 \cdot \mathbf{1}_{[0, 1/2[} + \frac{1}{2} \cdot \mathbf{1}_{[1/2, 1]}$.
L'intégrale de cette fonction simple est $\int_0^1 s_2 d\lambda = 0 \cdot \frac{1}{2} + \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$.
L'intégrale de Lebesgue de $f$ (qui vaut $1/2$) est le supremum des intégrales de telles fonctions simples minorantes.

**Exemple 4 : Intégrale infinie**
Soit $X = \mathbb{R}$ avec la mesure de Lebesgue $\lambda$. Soit $f = 1 \cdot \mathbf{1}_{[0, +\infty[}$.
L'intégrale est $\int_\mathbb{R} f d\lambda = 1 \cdot \lambda([0, +\infty[) = +\infty$.
La fonction n'est pas intégrable, bien qu'elle soit mesurable positive.

**Exemple 5 : Fonction constante sur un ensemble de mesure nulle**
Soit $X = \mathbb{R}$ avec la mesure de Lebesgue $\lambda$. Soit $f = 100 \cdot \mathbf{1}_{\{0\}}$.
La mesure de Lebesgue d'un singleton est nulle : $\lambda(\{0\}) = 0$.
L'intégrale est donc $\int_\mathbb{R} f d\lambda = 100 \cdot 0 = 0$.

### C. Propriétés Immédiates

> **Théorème :**
> 1. **Positivité :** $\int f d\mu \ge 0$.
> 2. **Croissance :** Si $f \le g$, alors $\int f \le \int g$.
> 3. **Homogénéité :** $\int \alpha f d\mu = \alpha \int f d\mu$ pour $\alpha \ge 0$.

## 3. Démonstrations Rigoureuses

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

## 4. Applications en Physique, Logique et Intelligence Artificielle

- **Le Pont Théorique :** L'intégrale de Lebesgue permet de définir l'**Espérance mathématique** de manière universelle, que la variable soit discrète, continue ou mixte. $\mathbb{E}[X] = \int_\Omega X(\omega) dP(\omega)$.
- **Exemple Concret :**
    - **Calcul de la Perte Attendue (Expected Loss) :** En IA, on minimise $L(\theta) = \int \ell(x, y, \theta) d\mathbb{P}(x, y)$. La mesure $\mathbb{P}$ représente nos données. Lebesgue nous permet de calculer cette intégrale même si nos données sont un mélange de catégories (discret) et de mesures physiques (continu).
    - **Mesures de similarité entre distributions :** La divergence de Jensen-Shannon ou la divergence KL sont définies par des intégrales de Lebesgue. Ces mesures sont le cœur des modèles génératifs et du clustering.
    - **Filtrage de Kalman :** La mise à jour des croyances dans un système dynamique repose sur l'intégration de fonctions de vraisemblance, souvent sur des espaces de grande dimension.

## 6. Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 65 (Fonctions mesurables).md]], [[Jalon 63 (Définition axiomatique d'une mesure).md]]
- **Concepts Futurs dépendants :** [[Jalon 67 (Démonstration du théorème de convergence monotone).md]], [[Jalon 73 (Définition des espaces Lp).md]]
