---
uuid: "jalon-66"
title: "Intégrale de Lebesgue pour les fonctions positives"
year: 2
trimester: 6
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon-65.md]]"
next: "[[Jalon-67.md]]"
---

# Jalon 66 : Intégrale de Lebesgue pour les fonctions positives

## Introduction

Imaginez que vous vouliez calculer le volume total d'une colline irrégulière à l'aide de blocs de construction.
L'approche de Riemann consiste à découper la base (le sol) en une grille régulière et, pour chaque petit carré, à empiler des blocs jusqu'à atteindre la surface de la colline. Si la colline a des pics très fins ou des trous profonds sur des espaces minuscules, la largeur fixe de la base nous empêchera d'être précis sans faire exploser le nombre de carrés.

L'approche de Lebesgue inverse la logique : on ne découpe plus le sol, on découpe l'altitude.
On prend une tranche de colline située exactement entre $0$ et $1$ mètre d'altitude. On cherche partout sur le terrain la "zone" où la colline a au moins cette altitude, et on calcule l'aire de cette zone (la mesure de l'ensemble de niveau). On multiplie cette aire par la hauteur de la tranche. Ensuite, on prend la tranche entre $1$ et $2$ mètres, et on fait pareil.
Le volume de la colline est la somme de toutes ces tranches horizontales.

Cette inversion conceptuelle, où l'on intègre "selon l'axe des y" (les valeurs de la fonction) plutôt que "selon l'axe des x" (le domaine de départ), permet de traiter des fonctions extrêmement chaotiques. Si une fonction prend la valeur $1$ sur les nombres rationnels et $0$ sur les irrationnels, Riemann est incapable de l'intégrer car son graphe ne ressemble à rien. Lebesgue s'en moque : il regarde simplement l'ensemble des points où la fonction vaut $1$, et demande "quelle est la mesure (la taille) de cet ensemble ?". Si la mesure est nulle, alors le "volume" correspondant est nul.

## Définitions, Théorèmes et Exemples

L'intégration de Lebesgue procède de manière ascendante et constructiviste. On définit d'abord l'intégrale pour les fonctions les plus basiques possibles (les fonctions dites "étagées" ou "simples"), puis on généralise aux fonctions mesurables positives par une procédure de supremum (limite supérieure).

Soit $(X, \mathcal{F}, \mu)$ un espace mesuré.

### Les Fonctions Étagées (ou Simples) Positives

Une fonction étagée positive est une fonction qui ne prend qu'un nombre fini de valeurs réelles positives.

> **Définition :** Soit $s : X \to [0, +\infty[$. On dit que $s$ est une **fonction étagée (ou simple) positive**, notée $s \in \mathcal{E}_+$ (ou $\mathcal{S}_+$), si elle peut s'écrire sous la forme canonique :
> $$s(x) = \sum_{i=1}^n a_i \mathbf{1}_{A_i}(x)$$
> où :
> - $n \in \mathbb{N}^*$.
> - $a_1, \dots, a_n$ sont des nombres réels positifs ou nuls deux à deux distincts.
> - $A_1, \dots, A_n$ forment une partition finie de $X$ constituée d'ensembles mesurables ($A_i \in \mathcal{F}$).
> - $\mathbf{1}_{A_i}$ est la fonction indicatrice de l'ensemble $A_i$.

**Exemple Concret 1 : L'intégrale d'une fonction constante par morceaux.**
Plaçons-nous sur l'espace mesurable $(\mathbb{R}, \mathcal{B}(\mathbb{R}))$ muni de la mesure de Lebesgue $\lambda$.
Considérons la fonction $s(x)$ qui vaut :
- $2$ si $x \in [0, 1]$
- $5$ si $x \in ]1, 3]$
- $0$ ailleurs.

La décomposition canonique de $s$ est :
$$s = 0 \cdot \mathbf{1}_{\mathbb{R} \setminus [0, 3]} + 2 \cdot \mathbf{1}_{[0, 1]} + 5 \cdot \mathbf{1}_{]1, 3]}$$

Ici, $A_1 = \mathbb{R} \setminus [0, 3]$, $A_2 = [0, 1]$, et $A_3 = ]1, 3]$. Ce sont tous des boréliens, donc $s \in \mathcal{E}_+$.

### Intégrale des Fonctions Étagées Positives

> **Définition :** L'intégrale par rapport à $\mu$ de la fonction étagée positive $s = \sum_{i=1}^n a_i \mathbf{1}_{A_i}$ est le nombre (éventuellement infini) défini par :
> $$\int_X s \, d\mu = \sum_{i=1}^n a_i \mu(A_i)$$
>
> *Convention cruciale :* Si pour un indice $i$, $a_i = 0$ et $\mu(A_i) = +\infty$, on pose $0 \times (+\infty) = 0$.

**Exemple Concret 2 : Calcul de l'intégrale de l'exemple 1.**
En reprenant la fonction $s$ définie précédemment :
$$\int_{\mathbb{R}} s \, d\lambda = 0 \cdot \lambda(\mathbb{R} \setminus [0, 3]) + 2 \cdot \lambda([0, 1]) + 5 \cdot \lambda(]1, 3])$$
$$\int_{\mathbb{R}} s \, d\lambda = 0 + 2 \times (1 - 0) + 5 \times (3 - 1)$$
$$\int_{\mathbb{R}} s \, d\lambda = 2 + 10 = 12$$

**Cas Pathologique :** Soit la fonction $s(x) = 0$ sur $\mathbb{R}$. Bien que la mesure de Lebesgue de $\mathbb{R}$ soit infinie, l'intégrale est $\int_{\mathbb{R}} 0 \, d\lambda = 0 \times (+\infty) = 0$. Cela traduit l'idée géométrique évidente qu'un "rectangle" de hauteur strictement nulle a une aire nulle, même s'il est de longueur infinie.

\begin{center}
\begin{tikzpicture}[scale=1.5]
  % Axes
  \draw[->] (-1,0) -- (4,0) node[right] {$x$};
  \draw[->] (0,-0.5) -- (0,6) node[above] {$s(x)$};

  % Fonction étagée
  \draw[very thick, blue] (-1,0) -- (0,0);
  \draw[dashed, blue] (0,0) -- (0,2);
  \draw[very thick, blue] (0,2) -- (1,2);
  \draw[dashed, blue] (1,2) -- (1,5);
  \draw[very thick, blue] (1,5) -- (3,5);
  \draw[dashed, blue] (3,5) -- (3,0);
  \draw[very thick, blue] (3,0) -- (4,0);

  % Remplissage
  \fill[blue, opacity=0.2] (0,0) rectangle (1,2);
  \fill[blue, opacity=0.2] (1,0) rectangle (3,5);

  % Ticks
  \draw (1,0.1) -- (1,-0.1) node[below] {$1$};
  \draw (3,0.1) -- (3,-0.1) node[below] {$3$};
  \draw (0.1,2) -- (-0.1,2) node[left] {$2$};
  \draw (0.1,5) -- (-0.1,5) node[left] {$5$};

  \node at (0.5, 1) {Aire $= 2$};
  \node at (2, 2.5) {Aire $= 10$};
\end{tikzpicture}
\end{center}

### Approximation par des fonctions étagées

Pour étendre l'intégrale à toute fonction mesurable positive, nous utilisons un résultat fondamental d'approximation.

> **Théorème d'Approximation :** Soit $f : X \to [0, +\infty]$ une fonction mesurable. Alors il existe une suite croissante $(s_n)_{n \in \mathbb{N}}$ de fonctions étagées positives, c'est-à-dire $0 \leq s_0 \leq s_1 \leq \dots \leq s_n \leq \dots \leq f$, telle que $(s_n)$ converge simplement vers $f$ sur $X$.
>
> $$\forall x \in X, \quad \lim_{n \to +\infty} s_n(x) = f(x)$$

**Exemple Concret 3 : Approximation d'une exponentielle.**
Considérons $f(x) = e^{-x}$ sur $\mathbb{R}_+$. On peut construire $s_n$ en découpant l'axe des ordonnées en intervalles de taille $\frac{1}{2^n}$.
Pour un $x$ donné, si $f(x) \in [\frac{k}{2^n}, \frac{k+1}{2^n}[$, on pose $s_n(x) = \frac{k}{2^n}$.
Pour $n=1$, les valeurs de $s_1$ sont $0, \frac{1}{2}, 1, \dots$
Ainsi, si $x = 0.5$, $f(0.5) = e^{-0.5} \approx 0.606$.
Pour $n=1$, l'intervalle d'ordonnées contenant $0.606$ est $[\frac{1}{2}, \frac{2}{2}[$, donc $s_1(0.5) = 0.5$.
Pour $n=2$, l'intervalle est $[\frac{2}{4}, \frac{3}{4}[$, donc $s_2(0.5) = 0.5$.
Pour $n=3$, l'intervalle est $[\frac{4}{8}, \frac{5}{8}[$, donc $s_3(0.5) = 0.5$.
Pour $n=4$, l'intervalle est $[\frac{9}{16}, \frac{10}{16}[$, donc $s_4(0.5) = 0.5625$.
On voit que la suite $s_n(0.5)$ est croissante et converge bien vers $e^{-0.5}$.

\begin{center}
\begin{tikzpicture}[scale=1.5]
  % Axes
  \draw[->] (0,0) -- (4,0) node[right] {$x$};
  \draw[->] (0,0) -- (0,2.5) node[above] {$y$};

  % Courbe exp(-x)
  \draw[thick, red, domain=0:3.5, samples=100] plot (\x, {2*exp(-\x)});
  \node[red, above right] at (0.2, 1.8) {$f(x) = e^{-x}$};

  % Approximation étagée (n grossier)
  \draw[very thick, blue] (0, 1.5) -- (0.287, 1.5);
  \draw[dashed, blue] (0.287, 1.5) -- (0.287, 1.0);
  \draw[very thick, blue] (0.287, 1.0) -- (0.693, 1.0);
  \draw[dashed, blue] (0.693, 1.0) -- (0.693, 0.5);
  \draw[very thick, blue] (0.693, 0.5) -- (1.386, 0.5);
  \draw[dashed, blue] (1.386, 0.5) -- (1.386, 0.0);
  \draw[very thick, blue] (1.386, 0.0) -- (3.5, 0.0);

  \node[blue] at (2, 0.5) {$s_n \le f$};
\end{tikzpicture}
\end{center}

### L'Intégrale de Lebesgue des Fonctions Mesurables Positives

Soit $\mathcal{M}_+(X, \mathcal{F})$ l'ensemble des fonctions mesurables positives (à valeurs dans $[0, +\infty]$).

> **Définition (Intégrale de Lebesgue) :** Pour toute fonction $f \in \mathcal{M}_+(X, \mathcal{F})$, on définit l'intégrale de $f$ par rapport à $\mu$ comme le supremum des intégrales de toutes les fonctions étagées positives minorant $f$ :
> $$\int_X f \, d\mu = \sup \left\lbrace \int_X s \, d\mu \ \mid \ s \in \mathcal{E}_+(X, \mathcal{F}), \quad 0 \leq s \leq f \right\rbrace$$
>
> Cette valeur existe toujours dans $[0, +\infty]$. Si $\int_X f \, d\mu < +\infty$, on dit que la fonction $f$ est **intégrable** (ou $\mu$-intégrable).

**Exemple Concret 4 : Intégrale de la fonction indicatrice de $\mathbb{Q}$ (Fonction de Dirichlet).**
Soit $f = \mathbf{1}_{\mathbb{Q} \cap [0,1]}$ sur le segment $[0, 1]$ muni de la mesure de Lebesgue $\lambda$.
La fonction $f$ vaut $1$ sur les rationnels, $0$ sur les irrationnels.
C'est une fonction étagée positive de décomposition canonique : $f = 1 \cdot \mathbf{1}_{\mathbb{Q} \cap [0,1]} + 0 \cdot \mathbf{1}_{[0,1] \setminus \mathbb{Q}}$.
Son intégrale de Lebesgue est immédiate (puisque $f \in \mathcal{E}_+$) :
$$\int_{[0,1]} f \, d\lambda = 1 \times \lambda(\mathbb{Q} \cap [0,1]) + 0 \times \lambda([0,1] \setminus \mathbb{Q})$$
Or, l'ensemble des rationnels est dénombrable, donc sa mesure de Lebesgue est stricte nulle : $\lambda(\mathbb{Q}) = 0$.
Ainsi, $\int_{[0,1]} f \, d\lambda = 1 \times 0 + 0 = 0$.
L'intégrale de Riemann, elle, est incapable de donner un résultat (la fonction est partout discontinue et ni les sommes de Darboux inférieures ni les supérieures ne convergent).

## Démonstrations

### Démonstration : Relation entre intégrale et ensembles de mesure nulle

Un résultat crucial affirme qu'une fonction positive dont l'intégrale est nulle est nécessairement nulle "presque partout" (p.p.), c'est-à-dire que l'ensemble des points où elle n'est pas nulle est de mesure strictement nulle.

**Théorème :** Soit $f \in \mathcal{M}_+(X, \mathcal{F})$.
$$ \int_X f \, d\mu = 0 \iff f = 0 \text{ } \mu\text{-presque partout.}$$

**Preuve :**

*Sens direct ($\implies$) : Supposons $\int_X f \, d\mu = 0$.*
1. **Initialisation / Cadre :** Soit $A = \{x \in X \mid f(x) > 0\}$. On veut démontrer que $\mu(A) = 0$.
2. **Étape 1 (Stratégie de découpage discret) :** L'astuce fondamentale de la théorie de la mesure consiste à écrire un ensemble strictement positif comme une union dénombrable de seuils stricts.
   Pour tout entier $n \ge 1$, posons $A_n = \{x \in X \mid f(x) \ge \frac{1}{n}\}$.
   L'ensemble $A$ s'écrit formellement comme l'union croissante de ces ensembles :
   $$A = \bigcup_{n=1}^\infty A_n$$
3. **Étape 2 (Minoration par des indicatrices) :** Fixons un entier $n \ge 1$. Par construction de $A_n$, pour tout $x \in X$, on a :
   $$f(x) \ge \frac{1}{n} \mathbf{1}_{A_n}(x)$$
   (Si $x \notin A_n$, l'inégalité est $f(x) \ge 0$, ce qui est vrai car $f \in \mathcal{M}_+$. Si $x \in A_n$, l'inégalité est $f(x) \ge \frac{1}{n}$, ce qui est vrai par définition de $A_n$).
4. **Étape 3 (Passage à l'intégrale) :** La croissance de l'intégrale de Lebesgue impose que :
   $$\int_X f \, d\mu \ge \int_X \left( \frac{1}{n} \mathbf{1}_{A_n} \right) \, d\mu$$
   Or la fonction à droite est une fonction étagée de base. Donc :
   $$\int_X f \, d\mu \ge \frac{1}{n} \mu(A_n)$$
5. **Étape 4 (Utilisation de l'hypothèse) :** Par hypothèse, l'intégrale de $f$ est nulle. Donc :
   $$0 \ge \frac{1}{n} \mu(A_n)$$
   Comme $\mu$ est positive par définition, la seule possibilité est que $\mu(A_n) = 0$ pour tout entier $n$.
6. **Étape 5 (Conclusion par sous-additivité) :** La mesure d'une union dénombrable est majorée par la somme des mesures ($\sigma$-sous-additivité) :
   $$\mu(A) = \mu\left( \bigcup_{n=1}^\infty A_n \right) \le \sum_{n=1}^\infty \mu(A_n) = \sum_{n=1}^\infty 0 = 0$$
   Donc $\mu(\{x \in X \mid f(x) > 0\}) = 0$. La fonction $f$ est bien nulle presque partout.

*Sens réciproque ($\impliedby$) : Supposons que $f = 0$ presque partout.*
1. Cela signifie que $\mu(A) = 0$, avec $A = \{x \in X \mid f(x) > 0\}$.
2. Soit $s \in \mathcal{E}_+$ telle que $0 \le s \le f$. Soit $s = \sum_{i=1}^k a_i \mathbf{1}_{B_i}$ sa forme canonique, avec les $a_i > 0$.
3. Pour chaque $i$, si $x \in B_i$, alors $s(x) = a_i > 0$. Comme $s \le f$, on a $f(x) > 0$, donc $x \in A$.
4. Ainsi, $B_i \subseteq A$. Par monotonie de la mesure, $\mu(B_i) \le \mu(A) = 0$, donc $\mu(B_i) = 0$.
5. L'intégrale de $s$ est $\int s \, d\mu = \sum a_i \mu(B_i) = \sum a_i \cdot 0 = 0$.
6. L'intégrale de $f$ étant le supremum sur toutes ces fonctions étagées $s$, elle est nécessairement $\sup \{0\} = 0$.

## Applications en Physique, Logique et Intelligence Artificielle

L'intégrale de Lebesgue est la fondation indissociable de la **Théorie des Probabilités Modernes** (l'axiomatisation de Kolmogorov).

Dans les algorithmes de **Machine Learning**, en particulier l'Apprentissage par Renforcement et les Processus Décisionnels de Markov Continus (MDP), nous devons calculer la fonction de valeur d'un état (Value Function), qui se définit comme une Espérance conditionnelle de gains futurs.

$$\mathbb{E}[R_t \mid S_t = s] = \int_{\mathcal{R}} r \, dP(r \mid s)$$

L'espace des récompenses $\mathcal{R}$ peut être hybride : il peut contenir des valeurs discrètes (une pénalité fixe $-100$ si le robot tombe) et des valeurs continues (le temps écoulé ou l'énergie dépensée). La théorie de Riemann exigerait de diviser la formule en une somme d'un côté et une intégrale de l'autre.
L'intégrale de Lebesgue permet d'utiliser une seule notation unifiée $\int$ et traite parfaitement les atomes de mesure (les impulsions de Dirac) et les densités lisses sous le même formalisme.

Un autre cas majeur est la théorie de l'Information. La minimisation de l'Entropie Croisée (Cross-Entropy Loss) pour entraîner les réseaux de neurones repose sur la Divergence de Kullback-Leibler. Sa définition est purement abstraite : $D_{KL}(P \parallel Q) = \int_{\mathcal{X}} \log\left(\frac{dP}{dQ}\right) dP$. La dérivée de Radon-Nikodym ($\frac{dP}{dQ}$) et l'intégrale externe n'existent rigoureusement qu'à travers le formalisme de Lebesgue.
