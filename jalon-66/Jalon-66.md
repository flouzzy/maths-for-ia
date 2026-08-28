---
uuid: "jalon-66"
title: "Intégrale de Lebesgue pour les fonctions mesurables positives"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 65 (Fonctions mesurables).md]]"
next: "[[Jalon 67 (Démonstration du théorème de convergence monotone).md]]"
---

# Jalon 66 : Intégrale de Lebesgue pour les fonctions mesurables positives

## 1. Genèse de l'Intégrale de Lebesgue

À la fin du XIXe siècle, les mathématiciens ont poussé la théorie de l'intégration de Riemann dans ses derniers retranchements. L'intégrale de Riemann, formellement construite par des subdivisions de l'intervalle de départ (l'axe des abscisses), fonctionnait remarquablement bien pour les fonctions continues ou continues par morceaux. Cependant, elle se heurtait à un mur conceptuel et analytique majeur : l'impossibilité d'intégrer des fonctions hautement discontinues, à l'image de la célèbre fonction de Dirichlet, qui vaut 1 sur les rationnels et 0 sur les irrationnels. Riemann, en découpant le domaine de définition, condamnait son approche, car sur tout intervalle aussi petit soit-il, on trouvera toujours à la fois des points où la fonction de Dirichlet vaut 0 et des points où elle vaut 1, rendant les sommes de Darboux inférieure et supérieure irréconciliables.

Henri Lebesgue, au début du XXe siècle, va opérer un renversement de perspective fulgurant, une véritable révolution copernicienne en mathématiques. Plutôt que de découper l'axe des abscisses, il eut l'idée de découper l'axe des ordonnées. Cette idée est d'une grande profondeur physique. Imaginez un caissier qui doit compter la somme d'une caisse. Le caissier de Riemann prendrait les pièces une par une dans l'ordre où elles se présentent (l'abscisse). Le caissier de Lebesgue, lui, regrouperait d'abord toutes les pièces de 1 euro, puis toutes celles de 2 euros, et enfin les billets (l'ordonnée), et multiplierait simplement la valeur de chaque monnaie par le nombre de pièces correspondantes (la mesure de l'ensemble).

Ce renversement d'approche requiert une nouvelle notion mathématique : la mesure. Lebesgue étendit le concept de longueur d'un intervalle pour mesurer des ensembles très complexes (la théorie de la mesure, vue au Jalon 63). Grâce à cela, nous pouvons maintenant mesurer les ensembles où la fonction prend une certaine valeur, et ainsi intégrer des fonctions d'une complexité vertigineuse, fondations indispensables pour les probabilités modernes (Kolmogorov) et, par extension, pour la théorie de l'apprentissage statistique.

Nous allons ici construire rigoureusement l'intégrale de Lebesgue, non pas d'un coup, mais par une approche ascendante (bottom-up), d'abord pour les fonctions les plus simples, dites "étagées", puis pour toute fonction mesurable positive par une approximation par valeurs inférieures.

\begin{center}
\begin{tikzpicture}[scale=1.5]
  % Axe des abscisses et ordonnées
  \draw[->] (-0.5, 0) -- (4, 0) node[right] {$x$};
  \draw[->] (0, -0.2) -- (0, 3) node[above] {$y$};

  % Courbe arbitraire f(x)
  \draw[thick, blue] (0.2, 0.5) .. controls (1, 2) and (2, 0.5) .. (3.5, 2.5) node[right] {$y = f(x)$};

  % Découpage sur l'axe des ordonnées (Lebesgue)
  \draw[dashed] (0, 1) -- (4, 1) node[right] {$y_i$};
  \draw[dashed] (0, 1.5) -- (4, 1.5) node[right] {$y_{i+1}$};

  % Représentation de l'ensemble image inverse
  \draw[thick, red] (0.5, 0) -- (1.5, 0);
  \node[red, below] at (1, 0) {$\{x \mid y_i \le f(x) < y_{i+1}\}$};

  % Les rectangles horizontaux
  \draw[fill=blue, opacity=0.2] (0.5, 0) rectangle (1.5, 1);
  \draw[fill=blue, opacity=0.2] (2.5, 0) rectangle (3.1, 1);
  \draw[thick, red] (2.5, 0) -- (3.1, 0);

\end{tikzpicture}
\end{center}

## 2. Intégrale des Fonctions Simples (Étagées) Positives

Avant de définir l'intégrale pour des fonctions mesurables quelconques, nous devons poser les briques fondamentales : les fonctions simples, qui ne prennent qu'un nombre fini de valeurs.

**Définition 1 (Fonction Simple Positive).**
Soit $(X, \mathcal{A}, \mu)$ un espace mesuré. Une fonction $s : X \to [0, +\infty[$ est dite simple (ou étagée) positive si son image $s(X)$ est un ensemble fini de réels positifs.
Elle peut s'écrire sous forme canonique :
$$s(x) = \sum_{i=1}^{n} a_i \mathbf{1}_{A_i}(x)$$
où :
- $a_1, \dots, a_n$ sont des réels positifs deux à deux distincts ($a_i \ge 0$).
- $A_1, \dots, A_n$ forment une partition finie de $X$, avec $A_i \in \mathcal{A}$ pour tout $i$.
- $\mathbf{1}_{A_i}$ est la fonction indicatrice de l'ensemble $A_i$, qui vaut 1 si $x \in A_i$, et 0 sinon.

Nous noterons $\mathcal{E}^+$ l'ensemble des fonctions simples positives mesurables sur $(X, \mathcal{A})$.

**Définition 2 (Intégrale d'une Fonction Simple).**
Pour $s \in \mathcal{E}^+$ de forme canonique $s = \sum_{i=1}^{n} a_i \mathbf{1}_{A_i}$, on définit son intégrale par rapport à la mesure $\mu$ par :
$$\int_X s \, d\mu = \sum_{i=1}^{n} a_i \mu(A_i)$$
Cette valeur appartient à $[0, +\infty]$.

**Convention cruciale de la théorie de la mesure :** On adopte toujours la convention $0 \times (+\infty) = 0$. Cela signifie que si une fonction est identiquement nulle sur un ensemble de mesure infinie, l'intégrale sur cet ensemble est nulle. Cela traduit l'idée géométrique qu'un rectangle de hauteur nulle a une aire nulle, même si sa base s'étend à l'infini.

**Exemple Concret Immédiat :**
Plaçons-nous sur $\mathbb{R}$ muni de sa tribu borélienne $\mathcal{B}(\mathbb{R})$ et de la mesure de Lebesgue $\lambda$.
Considérons la fonction $s(x) = 3 \cdot \mathbf{1}_{[0, 2]}(x) + 5 \cdot \mathbf{1}_{[4, 5]}(x)$.
Calculons son intégrale :
$\int_{\mathbb{R}} s \, d\lambda = 3 \times \lambda([0, 2]) + 5 \times \lambda([4, 5])$.
Puisque la mesure de Lebesgue d'un intervalle est sa longueur, $\lambda([0, 2]) = 2 - 0 = 2$ et $\lambda([4, 5]) = 5 - 4 = 1$.
Ainsi, $\int_{\mathbb{R}} s \, d\lambda = 3 \times 2 + 5 \times 1 = 6 + 5 = 11$.

**Proposition 1 (Propriétés de l'intégrale des fonctions simples).**
Soient $s, t \in \mathcal{E}^+$ et $c \ge 0$.
1. **Linéarité positive :** $\int_X (s + t) \, d\mu = \int_X s \, d\mu + \int_X t \, d\mu$ et $\int_X (cs) \, d\mu = c \int_X s \, d\mu$.
2. **Monotonie :** Si $s \le t$ (c'est-à-dire $s(x) \le t(x)$ pour tout $x \in X$), alors $\int_X s \, d\mu \le \int_X t \, d\mu$.

## 3. Intégrale de Lebesgue pour les Fonctions Mesurables Positives

Forts de la définition pour les fonctions simples, nous pouvons l'étendre aux fonctions mesurables positives quelconques. L'idée géniale est de définir l'aire sous la courbe d'une fonction $f$ comme le supremum des aires de tous les "histogrammes" formés par des fonctions simples qui restent toujours sous la courbe de $f$.

**Définition 3 (Intégrale de Lebesgue pour les fonctions positives).**
Soit $f : (X, \mathcal{A}) \to \overline{\mathbb{R}}_+$ une fonction mesurable à valeurs dans $[0, +\infty]$. L'intégrale de Lebesgue de $f$ par rapport à $\mu$ est définie par :
$$\int_X f \, d\mu = \sup \left\lbrace \int_X s \, d\mu \mid s \in \mathcal{E}^+, \, 0 \le s \le f \right\rbrace$$

Cette définition garantit que l'intégrale existe toujours dans $\overline{\mathbb{R}}_+$.
- Si $\int_X f \, d\mu < +\infty$, on dit que $f$ est $\mu$-intégrable (ou simplement intégrable).

**Théorème 1 (Propriétés fondamentales de l'intégrale).**
Soient $f, g : X \to [0, +\infty]$ mesurables.
1. **Croissance (Monotonie) :** Si $0 \le f \le g$ sur $X$, alors $\int_X f \, d\mu \le \int_X g \, d\mu$.
2. **Positivité de la nullité :** Si $\int_X f \, d\mu = 0$, alors $f = 0$ presque partout (p.p.), c'est-à-dire $\mu(\{x \in X \mid f(x) > 0\}) = 0$.
3. **Invariance presque partout :** Si $f = g$ p.p. (c'est-à-dire $\mu(\{x \mid f(x) \neq g(x)\}) = 0$), alors $\int_X f \, d\mu = \int_X g \, d\mu$.

**Exemple Concret Immédiat : Fonction de Dirichlet.**
Soit la fonction de Dirichlet $f = \mathbf{1}_{\mathbb{Q} \cap [0, 1]}$, étudiée sur l'espace $([0, 1], \mathcal{B}([0, 1]), \lambda)$.
La fonction de Dirichlet vaut 1 sur les rationnels et 0 sur les irrationnels de l'intervalle $[0, 1]$.
Elle n'est pas intégrable au sens de Riemann. Mais avec l'intégrale de Lebesgue, $f$ est une fonction simple positive.
Calculons son intégrale :
$\int_{[0, 1]} f \, d\lambda = 1 \times \lambda(\mathbb{Q} \cap [0, 1]) + 0 \times \lambda(([0, 1] \setminus \mathbb{Q}))$.
Or, l'ensemble des rationnels est dénombrable, donc sa mesure de Lebesgue est nulle (la mesure d'une réunion dénombrable de singletons de mesure nulle est nulle). Donc $\lambda(\mathbb{Q} \cap [0, 1]) = 0$.
Ainsi, $\int_{[0, 1]} f \, d\lambda = 1 \times 0 + 0 = 0$.
La puissance de l'intégrale de Lebesgue balaye l'impossibilité riemannienne en une ligne.

## 4. Démonstrations

**Démonstration du Théorème 1 (Propriété 2 : $\int_X f \, d\mu = 0 \implies f = 0$ p.p.)**

Soit $f : X \to [0, +\infty]$ une fonction mesurable. Supposons que $\int_X f \, d\mu = 0$. Nous voulons montrer que $\mu(\{x \in X \mid f(x) > 0\}) = 0$.

Définissons l'ensemble $A = \{x \in X \mid f(x) > 0\}$. Puisque $f$ est mesurable, $A \in \mathcal{A}$.
Nous pouvons décomposer cet ensemble en une union dénombrable d'ensembles croissants.
Posons $A_n = \{x \in X \mid f(x) \ge \frac{1}{n}\}$ pour $n \in \mathbb{N}^*$.
Il est clair que pour tout $x \in A$, il existe un entier $n$ suffisamment grand tel que $f(x) \ge \frac{1}{n}$.
Ainsi, $A = \bigcup_{n=1}^{+\infty} A_n$.

Maintenant, sur chaque sous-ensemble $A_n$, nous avons la majoration explicite :
$f(x) \ge \frac{1}{n} \mathbf{1}_{A_n}(x)$ pour tout $x \in X$.
En effet, si $x \in A_n$, $f(x) \ge \frac{1}{n}$ et $\frac{1}{n} \mathbf{1}_{A_n}(x) = \frac{1}{n}$. Si $x \notin A_n$, $f(x) \ge 0$ et $\frac{1}{n} \mathbf{1}_{A_n}(x) = 0$.

Par la propriété de croissance de l'intégrale, nous pouvons intégrer cette inégalité :
$$\int_X f \, d\mu \ge \int_X \frac{1}{n} \mathbf{1}_{A_n} \, d\mu$$
L'intégrale de la fonction simple $\frac{1}{n} \mathbf{1}_{A_n}$ se calcule immédiatement par définition :
$$\int_X f \, d\mu \ge \frac{1}{n} \mu(A_n)$$
Mais par hypothèse de départ, $\int_X f \, d\mu = 0$.
Par conséquent :
$$0 \ge \frac{1}{n} \mu(A_n)$$
Puisque $\mu$ est une mesure positive et $n > 0$, cela force $\mu(A_n) = 0$ pour tout $n \in \mathbb{N}^*$.

Nous avons donc exprimé $A$ comme l'union dénombrable d'ensembles de mesure nulle. Par la propriété de sous-additivité dénombrable d'une mesure :
$$\mu(A) = \mu\left( \bigcup_{n=1}^{+\infty} A_n \right) \le \sum_{n=1}^{+\infty} \mu(A_n) = \sum_{n=1}^{+\infty} 0 = 0$$
Puisque la mesure est toujours positive ou nulle, nous concluons fermement que $\mu(A) = 0$.
La fonction $f$ est donc nulle presque partout. $\blacksquare$

## 5. Applications en Probabilités et Intelligence Artificielle

### Fondations des Espaces Probabilisés de Kolmogorov
L'intégrale de Lebesgue pour les fonctions positives est le roc sur lequel Andreï Kolmogorov a axiomatisé la théorie des probabilités en 1933. L'espérance mathématique d'une variable aléatoire positive $X : (\Omega, \mathcal{F}, \mathbb{P}) \to \mathbb{R}_+$ est purement et simplement définie comme son intégrale de Lebesgue par rapport à la mesure de probabilité :
$$\mathbb{E}[X] = \int_\Omega X \, d\mathbb{P}$$
Contrairement à la théorie de Riemann qui distinguait les variables discrètes (traitées avec des séries $\sum p_i x_i$) des variables continues (traitées avec des intégrales $\int x f(x) dx$), l'approche de Lebesgue unifie de manière splendide la théorie discrète et la théorie continue sous un formalisme unique universel.

### Entropie Croisée et Divergence de Kullback-Leibler (KL)
En apprentissage automatique, notamment dans l'entraînement des réseaux de neurones (Deep Learning), nous cherchons souvent à minimiser la distance entre une distribution de probabilité vraie $\mathbb{P}$ (les données) et une distribution prédite $\mathbb{Q}_\theta$ paramétrée par les poids $\theta$ du modèle.
L'une des mesures de dissemblance les plus cruciales est la divergence de Kullback-Leibler. Pour des mesures quelconques, elle requiert impérativement le cadre de l'intégration de Lebesgue :
$$D_{KL}(\mathbb{P} \parallel \mathbb{Q}_\theta) = \int \log\left(\frac{d\mathbb{P}}{d\mathbb{Q}_\theta}\right) \, d\mathbb{P}$$
L'existence même de la dérivée de Radon-Nikodym $\frac{d\mathbb{P}}{d\mathbb{Q}_\theta}$ et la capacité à intégrer de manière robuste sur des espaces d'une dimensionalité colossale (comme l'espace des images $256 \times 256$ pixels, qui est un espace à 65536 dimensions) nécessitent la flexibilité et la rigueur de la théorie de la mesure et de l'intégration de Lebesgue.
