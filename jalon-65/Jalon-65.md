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

## Introduction

La théorie de l'intégration nécessite une classe de fonctions pour lesquelles la notion d'aire sous la courbe (ou d'intégrale) ait un sens rigoureux par rapport à une mesure donnée. Si l'intégrale de Riemann s'appuie sur la subdivision de l'espace de départ (l'axe des abscisses), l'intégrale de Lebesgue procède par une subdivision de l'espace d'arrivée (l'axe des ordonnées). Cette inversion de perspective impose que l'image réciproque d'un intervalle de l'espace d'arrivée soit un ensemble dont on sait mesurer la taille dans l'espace de départ.

Ainsi émerge le concept de fonction mesurable. Une fonction est dite mesurable si elle préserve la structure mesurable : elle transporte la tribu d'arrivée vers la tribu de départ par image réciproque. Cette condition garantit l'absence de paradoxes lors de la quantification des probabilités et le calcul des espérances.

## Définitions, Théorèmes et Exemples

### Définition formelle de la mesurabilité

Soient $(X, \mathcal{F})$ et $(Y, \mathcal{G})$ deux espaces mesurables, où $\mathcal{F}$ et $\mathcal{G}$ sont des tribus sur $X$ et $Y$ respectivement.

Une application $f : X \to Y$ est dite mesurable de $(X, \mathcal{F})$ dans $(Y, \mathcal{G})$, ou simplement $\mathcal{F}/\mathcal{G}$-mesurable, si pour tout ensemble $B \in \mathcal{G}$, son image réciproque par $f$ appartient à $\mathcal{F}$ :
$$ \forall B \in \mathcal{G}, \quad f^{-1}(B) = \{ x \in X \mid f(x) \in B \} \in \mathcal{F} $$

Dans le cas fondamental où $Y = \mathbb{R}$ muni de sa tribu borélienne $\mathcal{B}(\mathbb{R})$, on dit que $f$ est une fonction borélienne (si $X$ est aussi topologique et $\mathcal{F}$ est sa tribu borélienne) ou plus généralement simplement mesurable. La définition se réduit à : pour tout intervalle $I \subset \mathbb{R}$, $f^{-1}(I) \in \mathcal{F}$.

### Exemples concrets et immédiats

1. \textbf{Fonction constante :} Soit $c \in Y$. La fonction $f(x) = c$ pour tout $x \in X$ est mesurable. Pour tout $B \in \mathcal{G}$, $f^{-1}(B)$ est soit $X$ (si $c \in B$), soit $\emptyset$ (si $c \notin B$). Comme $X, \emptyset \in \mathcal{F}$, $f$ est mesurable.
2. \textbf{Fonction indicatrice :} Pour un sous-ensemble $A \subset X$, sa fonction indicatrice $\mathbf{1}_A : X \to \mathbb{R}$ est définie par $\mathbf{1}_A(x) = 1$ si $x \in A$ et $0$ sinon. $\mathbf{1}_A$ est mesurable si et seulement si $A \in \mathcal{F}$. En effet, $\mathbf{1}_A^{-1}(\{1\}) = A$, qui doit donc être dans la tribu $\mathcal{F}$.
3. \textbf{Fonction continue :} Si $X, Y$ sont des espaces topologiques munis de leurs tribus boréliennes respectives $\mathcal{B}(X)$ et $\mathcal{B}(Y)$, toute application continue $f : X \to Y$ est mesurable. L'image réciproque d'un ouvert de $Y$ est un ouvert de $X$, et les ouverts engendrent les tribus boréliennes.
4. \textbf{Fonction monotone :} Toute fonction croissante ou décroissante $f : \mathbb{R} \to \mathbb{R}$ est mesurable pour la tribu borélienne. L'image réciproque d'un intervalle du type $]a, +\infty[$ est un intervalle ou une demi-droite, qui est un borélien.
5. \textbf{Fonction en escalier :} La fonction signe $\text{sgn}(x)$ (qui vaut $1$ si $x > 0$, $0$ si $x = 0$, et $-1$ si $x < 0$) est une fonction mesurable. L'image réciproque de tout borélien est une combinaison d'intervalles comme $]0, +\infty[$, $\{0\}$ et $]-\infty, 0[$.
6. \textbf{Fonction de Dirichlet :} La fonction indicatrice des rationnels $f = \mathbf{1}_{\mathbb{Q}}$ est borélienne. $\mathbb{Q}$ est une union dénombrable de singletons, donc un borélien.
7. \textbf{Maximum de deux fonctions mesurables :} Si $f, g$ sont mesurables, $h(x) = \max(f(x), g(x))$ l'est. Par exemple, si $f(x) = x$ et $g(x) = 0$, la fonction partie positive $x^+$ (ReLU en IA) est mesurable.
8. \textbf{Fonction partie entière :} La fonction $f(x) = \lfloor x \rfloor$ est constante par morceaux et borélienne. $f^{-1}(\{k\}) = [k, k+1[$ qui est un borélien.
9. \textbf{Distance à un fermé :} Soit $F \subset \mathbb{R}^n$ fermé. La fonction $x \mapsto d(x, F) = \inf_{y \in F} \|x - y\|$ est continue (1-lipschitzienne) donc borélienne.
10. \textbf{Pathologie (Fonction non mesurable) :} Soit $V$ l'ensemble de Vitali (un ensemble non mesurable au sens de Lebesgue). La fonction indicatrice $\mathbf{1}_V$ n'est pas mesurable, car $\mathbf{1}_V^{-1}(\{1\}) = V \notin \mathcal{L}(\mathbb{R})$.

### Opérations sur les fonctions mesurables

Soient $f, g : (X, \mathcal{F}) \to (\mathbb{R}, \mathcal{B}(\mathbb{R}))$ deux fonctions mesurables.
Les opérations algébriques usuelles préservent la mesurabilité. Les fonctions $f+g$, $fg$, $|f|$, $\max(f, g)$ et $\min(f, g)$ sont mesurables.

\textbf{Théorème de stabilité par passage à la limite :}
Soit $(f_n)_{n \in \mathbb{N}}$ une suite de fonctions mesurables de $(X, \mathcal{F})$ dans $\overline{\mathbb{R}}$. Alors, les fonctions suivantes sont mesurables :
$$ \sup_{n} f_n, \quad \inf_{n} f_n, \quad \limsup_{n} f_n, \quad \liminf_{n} f_n $$
Si la suite converge simplement, sa limite $\lim_{n \to \infty} f_n$ est mesurable.

## Demonstrations

### Démonstration de la mesurabilité du supremum

Nous devons montrer que si $f_n : X \to \overline{\mathbb{R}}$ sont mesurables, alors $h = \sup_n f_n$ est mesurable.

1. La tribu borélienne sur $\overline{\mathbb{R}}$ est engendrée par les intervalles de la forme $]a, +\infty]$ pour tout $a \in \mathbb{R}$. Il suffit de montrer que $h^{-1}(]a, +\infty]) \in \mathcal{F}$.
2. Par définition du supremum, $h(x) > a$ si et seulement s'il existe au moins un entier $n \in \mathbb{N}$ tel que $f_n(x) > a$.
3. Nous pouvons exprimer l'image réciproque en termes d'opérations ensemblistes :
   $$ h^{-1}(]a, +\infty]) = \{ x \in X \mid \sup_n f_n(x) > a \} = \bigcup_{n \in \mathbb{N}} \{ x \in X \mid f_n(x) > a \} $$
   $$ h^{-1}(]a, +\infty]) = \bigcup_{n \in \mathbb{N}} f_n^{-1}(]a, +\infty]) $$
4. Puisque chaque $f_n$ est mesurable, $f_n^{-1}(]a, +\infty]) \in \mathcal{F}$.
5. Comme $\mathcal{F}$ est une tribu, elle est stable par union dénombrable. Ainsi, $h^{-1}(]a, +\infty]) \in \mathcal{F}$.
La fonction $h = \sup_n f_n$ est donc mesurable.

## Approximation par des fonctions simples

Une \textbf{fonction simple} (ou étagée) est une combinaison linéaire finie d'indicatrices d'ensembles mesurables :
$$ \varphi(x) = \sum_{i=1}^k a_i \mathbf{1}_{A_i}(x) $$
où $a_i \in \mathbb{R}$ et $A_i \in \mathcal{F}$. Les ensembles $A_i$ peuvent toujours être choisis disjoints, formant une partition de $X$.

\textbf{Théorème fondamental d'approximation :}
Toute fonction mesurable positive $f : X \to [0, +\infty]$ est la limite simple d'une suite croissante $(\varphi_n)$ de fonctions simples positives :
$$ 0 \leq \varphi_1 \leq \varphi_2 \leq \dots \leq f, \quad \text{et} \quad \lim_{n \to \infty} \varphi_n(x) = f(x) \quad \forall x \in X $$

\textbf{Construction de la suite d'approximation :}
Pour chaque entier $n \geq 1$, on partitionne l'axe des ordonnées $[0, n]$ en intervalles de longueur $1/2^n$. On définit :
$$ E_{n,k} = f^{-1}\left( \left[ \frac{k}{2^n}, \frac{k+1}{2^n} \right[ \right) \quad \text{pour } k=0, \dots, n2^n-1 $$
$$ F_n = f^{-1}([n, +\infty]) $$
La fonction simple approchante est définie par :
$$ \varphi_n = \sum_{k=0}^{n2^n-1} \frac{k}{2^n} \mathbf{1}_{E_{n,k}} + n \mathbf{1}_{F_n} $$

\begin{center}
\begin{tikzpicture}[scale=1.5]
    % Axes
    \draw[->, thick] (-0.2, 0) -- (4, 0) node[right] {$x$};
    \draw[->, thick] (0, -0.2) -- (0, 3) node[above] {$f(x)$};

    % Fonction continue
    \draw[thick, blue, smooth, domain=0:3.5] plot (\x, {0.2*exp(\x*0.6)}) node[right] {$f$};

    % Intervalles sur Y
    \draw[dashed, gray] (0, 0.5) -- (3.5, 0.5);
    \draw[dashed, gray] (0, 1.0) -- (3.5, 1.0);
    \draw[dashed, gray] (0, 1.5) -- (3.5, 1.5);
    \draw[dashed, gray] (0, 2.0) -- (3.5, 2.0);

    \node[left] at (0, 0.5) {$\frac{1}{2^n}$};
    \node[left] at (0, 1.0) {$\frac{2}{2^n}$};
    \node[left] at (0, 1.5) {$\frac{3}{2^n}$};
    \node[left] at (0, 2.0) {$\frac{4}{2^n}$};

    % Rectangles d'approximation
    \draw[fill=red, opacity=0.3] (0, 0) rectangle (1.52, 0.5);
    \draw[fill=red, opacity=0.3] (1.52, 0) rectangle (2.68, 1.0);
    \draw[fill=red, opacity=0.3] (2.68, 0) rectangle (3.35, 1.5);

    \draw[thick, red] (0, 0) -- (1.52, 0);
    \draw[thick, red] (1.52, 0.5) -- (2.68, 0.5);
    \draw[thick, red] (2.68, 1.0) -- (3.35, 1.0);
    \draw[thick, red] (3.35, 1.5) -- (3.5, 1.5);

    \node[red] at (2.5, 0.25) {$\varphi_n$};
\end{tikzpicture}
\end{center}

## Applications en Physique, Logique et IA

Dans la théorie des probabilités et l'intelligence artificielle, l'espace des données ou l'espace probabilisé de base $(\Omega, \mathcal{F}, P)$ représente les échantillons possibles.
Une variable aléatoire n'est rien d'autre qu'une application mesurable $X : \Omega \to \mathbb{R}$. La mesurabilité est la propriété structurelle minimale permettant de calculer la probabilité qu'un algorithme prenne une certaine décision : $P(X \in B) = P(X^{-1}(B))$.

Lors de l'apprentissage profond, un réseau de neurones représente une fonction $f_{\theta} : \mathbb{R}^d \to \mathbb{R}$. Composé d'opérations matricielles et de fonctions d'activation continues (ReLU, Sigmoïde), $f_{\theta}$ est continu, donc strictement mesurable. Cela permet de définir le risque espéré (l'intégrale de la fonction de perte) $\mathcal{R}(f_{\theta}) = \mathbb{E}[L(f_{\theta}(X), Y)]$. Si le modèle n'était pas mesurable, ce risque théorique serait indéfinissable. De plus, la fonction de décision d'un classifieur $h(x) = \mathbf{1}_{f_{\theta}(x) > 0}$ est une fonction étagée construite à partir du modèle continu $f_{\theta}$, et la préservation de la mesurabilité par composition et indicatrice garantit la validité théorique du cadre PAC (Probably Approximately Correct).
