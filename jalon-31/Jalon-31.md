---
uuid: "jalon-31"
title: "Introduction à la réduction de Jordan et structure des nilpotents"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/recherche-theorique
prev: "[[Jalon 30 (Trigonalisation d'endomorphismes et décomposition de Dunford.).md]]"
next: "[[Jalon 32 (Preuve complète du théorème spectral pour les endomorphismes symétriques.).md]]"
---

# Introduction à la réduction de Jordan et structure des nilpotents

## Introduction

L'algèbre linéaire commence souvent par une promesse séduisante : celle de la diagonalisation. L'idée que l'on puisse trouver un système de coordonnées dans lequel un endomorphisme complexe agit comme une simple dilatation indépendante le long de chaque axe. Cependant, très tôt, on découvre que cette promesse est fragile. Toutes les matrices ne sont pas diagonalisables. Que se passe-t-il alors lorsque l'espace refuse de se scinder en directions purement indépendantes ? Que faire des endomorphismes qui recèlent en eux une forme d'asymétrie structurelle, une force de cisaillement que de simples vecteurs propres ne peuvent capturer ?

C'est ici qu'intervient le concept de nilpotence, puis de réduction de Jordan. Historiquement, Camille Jordan, à la fin du XIXe siècle, cherchait à comprendre la structure fine des équations différentielles linéaires. Lorsqu'un système présente des racines multiples dans son polynôme caractéristique, la solution ne s'exprime plus seulement comme une somme d'exponentielles pures, mais fait apparaître des termes de la forme $t^k e^{\lambda t}$. Cet effet de résonance est la signature spectrale d'un bloc de Jordan.

Pour comprendre la réduction de Jordan, il faut visualiser l'endomorphisme non pas comme un ensemble de ressorts indépendants, mais comme une cascade ou une chaîne de montage. Un opérateur nilpotent agit comme un broyeur : peu importe le vecteur que vous y insérez, si vous le passez assez de fois à travers la machine, il finira broyé et réduit au vecteur nul. Les vecteurs ne sont plus des entités autonomes mais forment des chaînes de dépendance, où chaque itération de l'endomorphisme pousse un vecteur vers le suivant, jusqu'à l'annihilation finale.

La forme de Jordan est ainsi le compromis ultime : c'est la matrice la plus diagonale possible. Elle révèle que tout opérateur se décompose en deux actions simultanées et qui commutent : une dilatation pure et un cisaillement nilpotent.

## Définitions, Théorèmes et Exemples

### Endomorphismes Nilpotents

Soit $E$ un $\mathbb{K}$-espace vectoriel. Un endomorphisme $u \in \mathcal{L}(E)$ est dit nilpotent s'il existe un entier $k \in \mathbb{N}^*$ tel que $u^k = 0_{\mathcal{L}(E)}$. L'entier minimal $p \in \mathbb{N}^*$ vérifiant $u^p = 0_{\mathcal{L}(E)}$ est appelé l'indice de nilpotence de $u$.

- $E$ : Un espace vectoriel sur le corps $\mathbb{K}$.
- $u \in \mathcal{L}(E)$ : Un opérateur linéaire de $E$ dans $E$.
- $k \in \mathbb{N}^*$ : Un entier naturel non nul, représentant le nombre d'itérations.
- $u^k = u \circ u \circ \dots \circ u$ : La composition de l'endomorphisme $u$ avec lui-même $k$ fois.
- $0_{\mathcal{L}(E)}$ : L'endomorphisme nul.
- L'indice $p$ : Il vérifie $u^{p-1} \neq 0$ et $u^p = 0$. Il quantifie la longueur maximale de survie d'un vecteur sous l'action de $u$.

Exemple trivial : L'endomorphisme nul $u = 0_{\mathcal{L}(E)}$. Son indice de nilpotence est $p=1$.

Exemple complexe : Dans l'espace des polynômes de degré au plus $n$, $E = \mathbb{R}_n[X]$, l'opérateur de dérivation $D(P) = P'$. Puisque chaque dérivation diminue le degré d'au moins 1, la dérivée $(n+1)$-ème d'un polynôme de degré $\leq n$ est nulle. Ainsi, $D^{n+1} = 0$. L'opérateur de dérivation est nilpotent d'indice $n+1$.

Rotation de $\pi/2$ : Dans $\mathbb{R}^2$, la rotation $R$ d'angle $\pi/2$ vérifie $R^4 = \text{Id}$. Elle n'est pas nilpotente car ses itérées forment une suite périodique.

Dimension infinie : L'opérateur de décalage à droite $S(x_0, x_1, x_2, \dots) = (0, x_0, x_1, \dots)$ sur l'espace des suites n'est pas nilpotent, bien que son opérateur adjoint, le décalage à gauche $L(x_0, x_1, x_2, \dots) = (x_1, x_2, x_3, \dots)$, soit tel que $L^k$ s'annule sur le sous-espace des suites nulles à partir du rang $k$.

\begin{center}
\begin{tikzpicture}[>=stealth, auto, node distance=2cm, main node/.style={circle,draw,font=\sffamily\Large\bfseries}]
  \node[main node] (1) {$x$};
  \node[main node] (2) [right of=1] {$u(x)$};
  \node[main node] (3) [right of=2] {$u^2(x)$};
  \node (4) [right of=3] {$\dots$};
  \node[main node] (5) [right of=4] {$0$};
  \draw[->] (1) edge node {$u$} (2);
  \draw[->] (2) edge node {$u$} (3);
  \draw[->] (3) edge node {$u$} (4);
  \draw[->] (4) edge node {$u$} (5);
\end{tikzpicture}
\end{center}

### Caractérisation des Nilpotents

Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension finie $n$. Soit $u \in \mathcal{L}(E)$.
Les propositions suivantes sont équivalentes :
1. $u$ est nilpotent.
2. Le polynôme caractéristique de $u$ est $\chi_u(X) = X^n$.
3. La seule valeur propre de $u$ dans la clôture algébrique de $\mathbb{K}$ est $0$.

La matrice $U = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$ vérifie $\chi_U(X) = X^3$. On calcule $U^2 = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$ et $U^3 = 0_3$. $U$ est bien nilpotente.

L'équivalence $\chi_u(X) = X^n \iff u$ nilpotent repose sur la dimension finie. En dimension infinie, on ne peut pas utiliser le polynôme caractéristique.

### Blocs de Jordan

Un bloc de Jordan de taille $k \in \mathbb{N}^*$ associé à la valeur propre $\lambda \in \mathbb{K}$ est une matrice carrée $J_k(\lambda) \in \mathcal{M}_k(\mathbb{K})$ de la forme :
$$ J_k(\lambda) = \begin{pmatrix} \lambda & 1 & 0 & \dots & 0 \\ 0 & \lambda & 1 & \ddots & \vdots \\ \vdots & \ddots & \ddots & \ddots & 0 \\ \vdots & & \ddots & \lambda & 1 \\ 0 & \dots & \dots & 0 & \lambda \end{pmatrix} $$
Autrement dit, $[J_k(\lambda)]_{i,j} = \lambda$ si $i=j$, $1$ si $j = i+1$, et $0$ sinon.

$J_1(3) = \begin{pmatrix} 3 \end{pmatrix}$, $J_2(0) = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $J_3(-2) = \begin{pmatrix} -2 & 1 & 0 \\ 0 & -2 & 1 \\ 0 & 0 & -2 \end{pmatrix}$.

\begin{center}
\begin{tikzpicture}
    \node (O) at (0,0) {};
    \node (X) at (3,0) {};
    \node (Y) at (0,3) {};
    \draw[->, thick] (O) -- (X) node[right] {$e_1$};
    \draw[->, thick] (O) -- (Y) node[above] {$e_2$};
    \draw[->, dashed, red, thick] (1, 1) -- (1, 0) node[midway, right] {$N(e_2)=e_1$};
    \draw[->, dashed, red, thick] (2, 2) -- (2, 0);
    \node at (2.5, 1) {Cisaillement nilpotent};
\end{tikzpicture}
\end{center}

## Démonstrations

### Théorème de structure nilpotente et polynôme caractéristique

Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension $n \ge 1$ et $u \in \mathcal{L}(E)$.

Sens direct : Supposons $u$ nilpotent.
1. Par définition, il existe $k \in \mathbb{N}^*$ tel que $u^k = 0$.
2. Soit $\lambda \in \mathbb{K}$ une valeur propre de $u$ et $x \in E \setminus \{0_E\}$ un vecteur propre associé. Ainsi $u(x) = \lambda x$.
3. Montrons par récurrence sur $j$ que $u^j(x) = \lambda^j x$.
4. Appliquons ceci pour $j=k$ : $u^k(x) = \lambda^k x$.
5. Or nous savons que $u^k = 0$, donc $u^k(x) = 0_E$.
6. Ainsi, $\lambda^k x = 0_E$.
7. Comme $x \neq 0_E$, la nullité implique que $\lambda^k = 0$.
8. Dans le corps $\mathbb{K}$, cela implique nécessairement $\lambda = 0$.
9. Le polynôme caractéristique $\chi_u(X)$ de $u$ est de degré $n$.
10. La seule racine possible dans tout corps de décomposition est $0$.
11. On déduit que $\chi_u(X) = X^n$.

Sens réciproque : Supposons $\chi_u(X) = X^n$.
1. D'après le théorème de Cayley-Hamilton, tout endomorphisme $u$ annule son polynôme caractéristique : $\chi_u(u) = 0_{\mathcal{L}(E)}$.
2. Remplaçons $\chi_u$ par son expression : $\chi_u(u) = u^n = 0_{\mathcal{L}(E)}$.
3. Par définition, $u$ est donc nilpotent, d'indice de nilpotence $p \le n$.

### Indice de nilpotence et sous-espaces emboîtés

Si $u$ est nilpotent d'indice $p$, alors la suite des noyaux vérifie :
$\{0_E\} = \ker(u^0) \subsetneq \ker(u^1) \subsetneq \ker(u^2) \subsetneq \dots \subsetneq \ker(u^p) = E$.

1. Inclusion $\ker(u^i) \subseteq \ker(u^{i+1})$ :
   Soit $x \in \ker(u^i)$. Par définition, $u^i(x) = 0_E$.
   Appliquons $u$ : $u(u^i(x)) = u(0_E) = 0_E$.
   Donc $u^{i+1}(x) = 0_E$, ce qui signifie $x \in \ker(u^{i+1})$.
2. Caractère strict des inclusions avant l'indice $p$ :
   Supposons qu'il existe un entier $k < p$ tel que $\ker(u^k) = \ker(u^{k+1})$.
   La suite des noyaux stationne à partir du rang $k$.
3. Comme $u$ est d'indice $p$, $\ker(u^p) = E$.
4. Si la suite stationnait à $k < p$, on aurait $\ker(u^p) = \ker(u^k) = E$, ce qui signifierait que $u^k = 0$.
5. Or $p$ est le plus petit entier annulant $u$, ce qui contredit $u^k=0$ pour $k < p$.
6. Donc toutes les inclusions jusqu'à $p$ sont strictes.

## Applications

En intelligence artificielle, la théorie des endomorphismes nilpotents et de la forme de Jordan est fondamentale pour analyser la dynamique des Réseaux de Neurones Récurrents (RNN).

Dans un RNN sans activation, l'état caché évolue selon $h_t = W h_{t-1}$.
L'analyse de la stabilité de cette dynamique sur de longues séquences dépend de $W^t$.

Si $W$ n'est pas diagonalisable et possède des blocs de Jordan associés à des valeurs propres de module 1, la matrice $J_k(1)^t$ génère des termes polynomiaux en $t$. Plus précisément, la composante sur la sur-diagonale du $j$-ème niveau croît en $\approx t^j$.

Cette croissance polynomiale d'un système qui paraissait spectralement stable peut engendrer le phénomène d'explosion du gradient ou sa version nilpotente : un bloc de Jordan pour $\lambda=0$ agit comme un filtre FIR pur, anéantissant toute information du passé après exactement $k$ pas de temps, empêchant le réseau d'apprendre des dépendances à long terme. C'est l'essence même du problème que les architectures LSTM ont été conçues pour résoudre en court-circuitant cette multiplication matricielle itérée.
