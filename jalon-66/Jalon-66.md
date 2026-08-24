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

# Intégrale de Lebesgue pour les fonctions positives

## Introduction (Genèse conceptuelle et limite de Riemann)

L'intégrale de Riemann, bien qu'intuitive, souffre d'un défaut majeur : elle partitionne l'axe des abscisses. Cela exige une certaine régularité de la fonction (continuité presque partout). Si une fonction oscille trop violemment, comme la fonction indicatrice des rationnels $\mathbf{1}_\mathbb{Q}$, la somme de Riemann ne converge pas car sur tout intervalle, le supremum est 1 et l'infimum est 0.

L'idée géniale de Lebesgue, issue des travaux sur la théorie de la mesure de Borel, est de changer d'axe de partitionnement. Au lieu de découper le domaine de départ, on partitionne l'espace d'arrivée. On regroupe les points du domaine qui ont à peu près la même image. Pour ce faire, on s'appuie sur des "tampons" : les fonctions étagées.

## Définitions, Théorèmes et Exemples

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### Intégrale des Fonctions Simples

Soit $\mathcal{S}_+$ l'ensemble des fonctions simples (étagées) positives sur $X$.
Une fonction $s \in \mathcal{S}_+$ s'écrit canoniquement $s = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$ avec $a_i \ge 0$ distincts et les $A_i$ formant une partition finie de $X$ constituée d'ensembles mesurables.

> **Définition (Intégrale d'une fonction simple) :** L'intégrale de la fonction simple $s$ par rapport à $\mu$ est :
> $$\int_X s \, d\mu = \sum_{i=1}^n a_i \mu(A_i)$$
> *(On utilise la convention $0 \cdot \infty = 0$ pour traiter les ensembles de mesure infinie où la fonction s'annule).*

**Exemples Concrets :**
1. Soit $X = \mathbb{R}$, avec la mesure de Lebesgue $\lambda$. Soit $s(x) = 3 \cdot \mathbf{1}_{[0, 2]}(x) + 5 \cdot \mathbf{1}_{[4, 5]}(x)$.
   $\int_\mathbb{R} s \, d\lambda = 3 \cdot \lambda([0, 2]) + 5 \cdot \lambda([4, 5]) = 3 \cdot (2-0) + 5 \cdot (5-4) = 6 + 5 = 11$.
2. Si $X = \mathbb{N}$ avec la mesure de comptage $\mu$, et $s(n) = 2$ si $n \in \{1,2,3\}$ et $0$ sinon.
   $\int_\mathbb{N} s \, d\mu = 2 \cdot \mu(\{1,2,3\}) = 2 \cdot 3 = 6$.
3. Espace des lancers de dés : $\Omega = \{1,2,3,4,5,6\}$ avec $\mathbb{P}(\{\omega\}) = 1/6$. Variable aléatoire $X(\omega) = 10$ si $\omega$ pair, $0$ sinon.
   $\int_\Omega X \, d\mathbb{P} = 10 \cdot \mathbb{P}(\{2,4,6\}) = 10 \cdot \frac{3}{6} = 5$. (Ceci est l'espérance mathématique).
4. La fonction de Dirichlet modifiée : $f = 7 \cdot \mathbf{1}_{\mathbb{Q} \cap [0,1]} + 2 \cdot \mathbf{1}_{([0,1] \setminus \mathbb{Q})}$.
   $\int_\mathbb{R} f \, d\lambda = 7 \cdot \lambda(\mathbb{Q} \cap [0,1]) + 2 \cdot \lambda([0,1] \setminus \mathbb{Q}) = 7 \cdot 0 + 2 \cdot 1 = 2$.
5. Fonction constante sur $\mathbb{R}$ : $s = 2 \cdot \mathbf{1}_{\mathbb{R}}$. $\int_\mathbb{R} s \, d\lambda = 2 \cdot \lambda(\mathbb{R}) = 2 \cdot \infty = \infty$.

### Intégrale des Fonctions Mesurables Positives

Soit $\mathcal{M}_+$ l'ensemble des fonctions mesurables de $X$ dans $[0, +\infty]$.
On sait qu'une telle fonction est limite d'une suite croissante de fonctions simples.

> **Définition (Intégrale de Lebesgue) :**
> Pour tout $f \in \mathcal{M}_+$, on définit :
> $$\int_X f \, d\mu = \sup \left\lbrace \int_X s \, d\mu \mid s \in \mathcal{S}_+, 0 \le s \le f \right\rbrace$$
> Cette valeur appartient à $[0, +\infty]$. Si elle est finie, on dit que $f$ est **intégrable**.

\begin{center}
\begin{tikzpicture}[scale=0.8]
\draw[->] (-0.5, 0) -- (6, 0) node[right] {$x$};
\draw[->] (0, -0.5) -- (0, 4) node[above] {$y$};
\draw[thick, blue] (0, 0.5) to[out=20,in=180] (3, 3) to[out=0,in=160] (5.5, 1);
\node[blue] at (4, 3.5) {$f(x)$};

\filldraw[fill=red!20, draw=red, thick] (0, 0) rectangle (1, 0.5);
\filldraw[fill=red!20, draw=red, thick] (1, 0) rectangle (2, 1);
\filldraw[fill=red!20, draw=red, thick] (2, 0) rectangle (3.5, 2.5);
\filldraw[fill=red!20, draw=red, thick] (3.5, 0) rectangle (4.5, 1.5);
\filldraw[fill=red!20, draw=red, thick] (4.5, 0) rectangle (5.5, 0.8);
\node[red] at (2.5, -0.5) {Approximation par $s \le f$};
\end{tikzpicture}
\end{center}

**Propriétés Fondamentales (Linéarité positive, Monotonie) :**
Pour $f, g \in \mathcal{M}_+$ et $\alpha \ge 0$ :
1. **Positivité absolue :** $\int_X f \, d\mu \ge 0$.
2. **Croissance :** Si $f \le g$ presque partout (p.p.), alors $\int_X f \, d\mu \le \int_X g \, d\mu$.
3. **Homogénéité positive :** $\int_X \alpha f \, d\mu = \alpha \int_X f \, d\mu$.
4. **Additivité :** $\int_X (f + g) \, d\mu = \int_X f \, d\mu + \int_X g \, d\mu$ (La preuve complète de l'additivité nécessite le théorème de convergence monotone, abordé au prochain jalon).

**Exemples Concrets :**
6. Soit $f(x) = x^2$ sur $[0,1]$ pour $\lambda$. L'intégrale de Lebesgue coïncide avec celle de Riemann ici. $\int_{[0,1]} x^2 d\lambda = [x^3/3]_0^1 = 1/3$.
7. Soit $\mu$ la mesure de Dirac en $0$, notée $\delta_0$ sur $\mathbb{R}$. Soit $f(x) = \cos(x) + 4$.
   $\int_\mathbb{R} f \, d\delta_0 = f(0) = \cos(0) + 4 = 5$. L'intégrale par rapport à Dirac est l'évaluation en ce point.
8. Soit $\mu$ la mesure de comptage sur $\mathbb{N}$. Soit $f(n) = \frac{1}{2^n}$.
   $\int_\mathbb{N} f \, d\mu = \sum_{n=0}^\infty \frac{1}{2^n} = \frac{1}{1 - 1/2} = 2$.
9. Soit $f(x) = 1/\sqrt{x}$ sur $]0, 1]$. Bien que non bornée, $f \in \mathcal{M}_+$ et $\int_{]0,1]} x^{-1/2} d\lambda = 2$. Donc $f$ est intégrable.
10. Soit $f(x) = 1/x$ sur $[1, +\infty[$. $\int_{[1, +\infty[} (1/x) d\lambda = \lim_{M \to \infty} \ln(M) = +\infty$. $f$ n'est pas intégrable.

## Démonstrations

### Démonstration : Relation entre intégrale nulle et nullité presque partout

> **Proposition :** Si $f \in \mathcal{M}_+$ et $\int_X f \, d\mu = 0$, alors $f = 0$ $\mu$-presque partout. Inversement, si $f=0$ p.p., $\int_X f \, d\mu = 0$.

1. **Partie 1 : Implication directe.**
   Soit $A = \{x \in X \mid f(x) > 0\}$. Nous devons prouver que $\mu(A) = 0$.
   Écrivons $A$ comme l'union dénombrable d'ensembles mesurables : $A_n = \{x \in X \mid f(x) \ge 1/n\}$ pour $n \in \mathbb{N}^*$.
   Clairement, $A = \bigcup_{n=1}^\infty A_n$.
   Sur chaque ensemble $A_n$, nous avons la minoration $f \ge \frac{1}{n} \mathbf{1}_{A_n}$.
   Puisque l'intégrale préserve l'ordre (croissance) :
   $$\int_X f \, d\mu \ge \int_X \frac{1}{n} \mathbf{1}_{A_n} \, d\mu = \frac{1}{n} \mu(A_n)$$
   Puisque, par hypothèse, $\int_X f \, d\mu = 0$, il s'ensuit que pour tout $n \ge 1$, $\frac{1}{n} \mu(A_n) \le 0$.
   La mesure étant positive, on conclut rigoureusement que $\mu(A_n) = 0$ pour tout $n \ge 1$.
   Par la propriété de sous-additivité dénombrable de la mesure $\mu$ :
   $$\mu(A) = \mu\left( \bigcup_{n=1}^\infty A_n \right) \le \sum_{n=1}^\infty \mu(A_n) = \sum_{n=1}^\infty 0 = 0$$
   Par conséquent, $\mu(\{f > 0\}) = 0$, ce qui signifie exactement que $f = 0$ presque partout.

2. **Partie 2 : Implication réciproque.**
   Supposons $f = 0$ p.p., soit $A = \{f > 0\}$ avec $\mu(A) = 0$.
   Soit $s$ une fonction simple positive telle que $0 \le s \le f$. On peut écrire $s = \sum_{i=1}^k a_i \mathbf{1}_{E_i}$.
   Pour que $s(x) > 0$, il faut que $f(x) > 0$, donc $E_i \subset A$ pour tout $i$ tel que $a_i > 0$.
   Par croissance de la mesure, $\mu(E_i) \le \mu(A) = 0$, donc $\mu(E_i) = 0$.
   Ainsi, $\int_X s \, d\mu = \sum_{i=1}^k a_i \cdot 0 = 0$.
   En passant au supremum sur toutes ces fonctions simples $s \le f$, on obtient $\int_X f \, d\mu = 0$.

\begin{center}
\begin{tikzpicture}
\draw[->] (-1, 0) -- (6, 0) node[right] {$X$};
\draw[thick, blue] (-1, 0) -- (1, 0) (1, 2) circle (0.05) (1,0) circle (0.05) (1.2, 0) -- (3, 0) (3, 1.5) circle (0.05) (3.2, 0) -- (5, 0);
\fill[blue] (1, 2) circle (0.05);
\fill[blue] (3, 1.5) circle (0.05);
\draw[blue] (1.1,0) -- (1.2,0);
\draw[blue] (3.1,0) -- (3.2,0);

\node at (2.5, -0.8) {Fonction nulle presque partout : les "pics" ont une largeur (mesure) nulle.};
\node at (2.5, -1.3) {L'aire sous la courbe (intégrale) reste donc 0.};
\end{tikzpicture}
\end{center}


## Applications en Probabilités, Physique et IA

- **Espérance Universelle en Probabilités :** L'intégrale de Lebesgue est l'outil canonique pour définir l'espérance mathématique d'une variable aléatoire $X \ge 0$, notée $\mathbb{E}[X] = \int_\Omega X \, d\mathbb{P}$. L'approche unifie les variables discrètes (sommes de séries) et continues (intégrales) sous le même formalisme.
- **Fonctions de Risque en Apprentissage (Machine Learning) :** En IA, minimiser une perte (Loss) $L(\theta) = \int_{\mathcal{X} \times \mathcal{Y}} \ell(f_\theta(x), y) \, dP(x,y)$ nécessite ce cadre, car la distribution des données réelles $P$ est souvent empirique (combinaison de masses de Dirac), rendant l'intégrale de Riemann totalement inopérante.
- **Entropie Différentielle (Théorie de l'Information) :** L'entropie d'une distribution continue est définie par $- \int p(x) \ln(p(x)) \, dx$. Les propriétés de l'intégrale de Lebesgue garantissent la robustesse de cette notion face aux singularités locales de la densité de probabilité.
