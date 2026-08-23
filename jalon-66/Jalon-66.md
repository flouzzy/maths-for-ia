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

## Introduction

L'intégrale de Riemann, bien que fondamentalement intuitive, souffre de limitations sévères liées aux passages à la limite et à l'intégration de fonctions fortement discontinues. L'approche de Lebesgue repose sur une construction diamétralement opposée : plutôt que de subdiviser le domaine de départ, on partitionne l'espace d'arrivée. Cette méthode, fondée sur la théorie de la mesure, permet d'intégrer des fonctions complexes en les approchant par des fonctions dites "étagées" (ou simples). La construction est descendante et garantit une robustesse analytique exceptionnelle, généralisant le concept d'aire ou d'espérance.

## Définitions, Théorèmes & Exemples Concrets

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### Intégrale des Fonctions Simples

Soit $\mathcal{S}_+$ l'ensemble des fonctions simples (étagées) positives sur $X$.
Une fonction $s \in \mathcal{S}_+$ s'écrit $s = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$ avec $a_i \ge 0$.

> **Définition 1 :** L'intégrale de la fonction simple $s$ par rapport à $\mu$ est :
> $$\int_X s d\mu = \sum_{i=1}^n a_i \mu(A_i)$$
> (On utilise la convention $0 \cdot \infty = 0$).

### Intégrale des Fonctions Mesurables Positives

Soit $\mathcal{M}_+$ l'ensemble des fonctions mesurables de $X$ dans $[0, +\infty]$.

> **Définition 2 (Intégrale de Lebesgue) :**
> Pour tout $f \in \mathcal{M}_+$, on définit :
> $$\int_X f d\mu = \sup \left\lbrace \int_X s d\mu \mid s \in \mathcal{S}_+, 0 \le s \le f \right\rbrace$$
> Cette valeur appartient à $[0, +\infty]$. Si elle est finie, on dit que $f$ est **intégrable**.


**Exemple Concret 1 : Fonction de Dirichlet**
Soit $f = \mathbf{1}_{\mathbb{Q} \cap [0,1]}$. C'est une fonction simple (elle ne prend que les valeurs 0 et 1).
Son intégrale est $1 \cdot \\mu(\mathbb{Q} \cap [0,1]) + 0 \cdot \\mu([0,1] \setminus \mathbb{Q}) = 1 \cdot 0 + 0 \cdot 1 = 0$.

**Exemple Concret 2 : Fonction de Heaviside**
Soit $H(x) = 1$ si $x \ge 0$, et $0$ si $x < 0$. $H \in \mathcal{M}_+$.
Sur l'espace $(\mathbb{R}, \mathcal{B}(\mathbb{R}), \lambda)$, l'intégrale de $H$ sur $[-1, 1]$ est $\int_{[-1,1]} H d\lambda = \lambda([0,1]) = 1$.

**Exemple Concret 3 : Limite de fonctions simples**
Soit $f(x) = x$ sur $[0,1]$. On peut approcher $f$ par la suite de fonctions simples $s_n(x) = \sum_{k=0}^{n-1} \frac{k}{n} \mathbf{1}_{[\frac{k}{n}, \frac{k+1}{n})}(x)$.
Alors $\int_{[0,1]} s_n d\lambda = \sum_{k=0}^{n-1} \frac{k}{n} \cdot \frac{1}{n} = \frac{1}{n^2} \frac{(n-1)n}{2} = \frac{n-1}{2n}$.
La limite quand $n \to \infty$ est $\frac{1}{2}$. Par le théorème de convergence monotone, $\int_0^1 x d\lambda = \frac{1}{2}$.

**Exemple Concret 4 : Intégrale infinie**
Soit $f(x) = \frac{1}{\sqrt{x}} \mathbf{1}_{(0,1]}(x)$. $f \in \mathcal{M}_+$.
On peut utiliser le TCM avec $f_n(x) = f(x) \mathbf{1}_{[\frac{1}{n}, 1]}(x)$. L'intégrale de Riemann de $f_n$ est $2(1 - \frac{1}{\sqrt{n}}) \to 2$. L'intégrale de Lebesgue est 2.

**Exemple Concret 5 : Un atome**
Soit $\delta_0$ la mesure de Dirac en $0$. Pour toute fonction $f \in \mathcal{M}_+$, l'intégrale est $\int f d\delta_0 = f(0)$.


\begin{tikzpicture}[scale=1.5]
  % Axes
  \draw[->] (-0.5,0) -- (5,0) node[right] {$x$};
  \draw[->] (0,-0.5) -- (0,3) node[above] {$f(x)$};

  % Courbe de f
  \draw[thick, blue] (0,0.5) .. controls (1,1.5) and (3,0.5) .. (4.5,2.5) node[right] {$f$};

  % Fonction etagée s <= f
  \fill[red!20, opacity=0.5] (0,0) rectangle (1.5,0.5);
  \draw[red, thick] (0,0.5) -- (1.5,0.5);
  \draw[dashed] (1.5,0) -- (1.5,0.5);

  \fill[red!20, opacity=0.5] (1.5,0) rectangle (2.5,1.0);
  \draw[red, thick] (1.5,1.0) -- (2.5,1.0);
  \draw[dashed] (1.5,0.5) -- (1.5,1.0);
  \draw[dashed] (2.5,0) -- (2.5,1.0);

  \fill[red!20, opacity=0.5] (2.5,0) rectangle (4,0.8);
  \draw[red, thick] (2.5,0.8) -- (4,0.8);
  \draw[dashed] (2.5,1.0) -- (2.5,0.8);
  \draw[dashed] (4,0) -- (4,0.8);

  % Annotations
  \node at (0.75, 0.25) {$a_1$};
  \node at (2, 0.5) {$a_2$};
  \node at (3.25, 0.4) {$a_3$};
\end{tikzpicture}


### Propriétés Immédiates

> **Théorème :**
> 1. **Positivité :** $\int f d\mu \ge 0$.
> 2. **Croissance :** Si $f \le g$, alors $\int f \le \int g$.
> 3. **Homogénéité :** $\int \alpha f d\mu = \alpha \int f d\mu$ pour $\alpha \ge 0$.

## Démonstrations

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

## Applications

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

### Applications en IA

 L'intégrale de Lebesgue permet de définir l'**Espérance mathématique** de manière universelle, que la variable soit discrète, continue ou mixte. $\mathbb{E}[X] = \int_\Omega X(\omega) dP(\omega)$.

    - **Calcul de la Perte Attendue (Expected Loss) :** En IA, on minimise $L(\theta) = \int \ell(x, y, \theta) d\mathbb{P}(x, y)$. La mesure $\mathbb{P}$ représente nos données. Lebesgue nous permet de calculer cette intégrale même si nos données sont un mélange de catégories (discret) et de mesures physiques (continu).
    - **Mesures de similarité entre distributions :** La divergence de Jensen-Shannon ou la divergence KL sont définies par des intégrales de Lebesgue. Ces mesures sont le cœur des modèles génératifs et du clustering.
    - **Filtrage de Kalman :** La mise à jour des croyances dans un système dynamique repose sur l'intégration de fonctions de vraisemblance, souvent sur des espaces de grande dimension.

## Liens Sémantiques

- **Concepts Précédents requis :** [[Jalon 65 (Fonctions mesurables).md]], [[Jalon 63 (Définition axiomatique d'une mesure).md]]
- **Concepts Futurs dépendants :** [[Jalon 67 (Démonstration du théorème de convergence monotone).md]], [[Jalon 73 (Définition des espaces Lp).md]]
