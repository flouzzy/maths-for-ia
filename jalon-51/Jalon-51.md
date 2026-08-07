---
uuid: "jalon-51"
title: "Espaces métriques"
year: 2
trimester: 5
tags:
  - math/topologie
  - ia/algorithmes
prev: "[[Jalon 50 (Opérateurs topologiques).md]]"
next: "[[Jalon 52 (Applications continues entre espaces topologiques et définition fine des homéomorphismes.).md]]"
---
# Jalon 51 : Espaces métriques

## Genèse et Intuition Géométrique

La topologie générale (étudiée précédemment) fournit un cadre abstrait pour définir les voisinages et la continuité via les ouverts. Cependant, cette abstraction est parfois insuffisante pour capturer la notion quantitative de proximité. Historiquement, la formalisation de la distance a émergé du besoin d'étendre la rigueur du calcul géométrique euclidien à des espaces plus complexes, tels que les espaces de fonctions ou les espaces de suites.

Maurice Fréchet, en 1906, a introduit le concept d'espace métrique pour unifier diverses théories naissantes de l'analyse fonctionnelle. En dotant un ensemble d'une fonction mesurant la "distance" entre deux points, il devient possible de quantifier la convergence d'une suite, la continuité d'une application ou la compacité d'un domaine. L'inégalité triangulaire, clé de voûte de cette structure, garantit que les distances respectent l'intuition géométrique du chemin le plus court.

## Définitions, Théorèmes et Exemples Concrets

### Définition d'une Distance

Soit $X$ un ensemble non vide.

\textbf{Définition (Distance) :}
Une \textit{distance} (ou métrique) sur $X$ est une application $d : X \times X \to \mathbb{R}_+$ vérifiant les trois axiomes suivants pour tous $x, y, z \in X$ :
1. \textbf{Séparation :} $d(x, y) = 0 \iff x = y$.
2. \textbf{Symétrie :} $d(x, y) = d(y, x)$.
3. \textbf{Inégalité Triangulaire :} $d(x, z) \le d(x, y) + d(y, z)$.

Le couple $(X, d)$ est alors appelé un \textbf{espace métrique}.

\textbf{Exemple Numérique Immédiat :}
Sur $\mathbb{R}^n$, la distance euclidienne canonique est définie par :
$$ d_2(x, y) = \sqrt{\sum_{i=1}^n (x_i - y_i)^2} $$
Si $x = (1, 0)$ et $y = (4, 4)$ dans $\mathbb{R}^2$, alors $d_2(x, y) = \sqrt{(4-1)^2 + (4-0)^2} = \sqrt{9 + 16} = 5$.

### Topologie Induite et Boules

\textbf{Définition (Boules) :}
Dans un espace métrique $(X, d)$, pour $a \in X$ et $r > 0$ :
- La \textbf{boule ouverte} de centre $a$ et de rayon $r$ est $B(a, r) = \{ x \in X \mid d(a, x) < r \}$.
- La \textbf{boule fermée} de centre $a$ et de rayon $r$ est $\bar{B}(a, r) = \{ x \in X \mid d(a, x) \le r \}$.

\textbf{Théorème (Topologie induite) :}
L'ensemble des parties de $X$ pouvant s'écrire comme une réunion quelconque de boules ouvertes forme une topologie sur $X$. On dit que c'est la topologie induite par la distance $d$.

\begin{center}
\begin{tikzpicture}
    % Boule euclidienne
    \draw[blue, thick] (0,0) circle (1.5cm);
    \filldraw[black] (0,0) circle (1.5pt) node[anchor=north] {$a$};
    \draw[->, dashed] (0,0) -- (1.06, 1.06) node[anchor=south west] {$r$};
    \node at (0, -2) {Norme 2 ($L^2$)};

    % Boule norme 1 (losange)
    \draw[red, thick, xshift=4cm] (0, 1.5) -- (1.5, 0) -- (0, -1.5) -- (-1.5, 0) -- cycle;
    \filldraw[black, xshift=4cm] (0,0) circle (1.5pt) node[anchor=north] {$a$};
    \node at (4, -2) {Norme 1 ($L^1$)};

    % Boule norme infini (carré)
    \draw[green!60!black, thick, xshift=8cm] (-1.5, -1.5) rectangle (1.5, 1.5);
    \filldraw[black, xshift=8cm] (0,0) circle (1.5pt) node[anchor=north] {$a$};
    \node at (8, -2) {Norme $\infty$ ($L^\infty$)};
\end{tikzpicture}
\end{center}

### Distances Équivalentes

\textbf{Définition (Équivalence) :}
Deux distances $d_1$ et $d_2$ sur $X$ sont dites \textit{équivalentes} s'il existe des constantes $C_1 > 0$ et $C_2 > 0$ telles que :
$$ \forall x, y \in X, \quad C_1 d_1(x, y) \le d_2(x, y) \le C_2 d_1(x, y) $$

\textbf{Propriété Fondamentale :}
Deux distances équivalentes induisent strictement la même topologie. Elles définissent les mêmes ouverts, les mêmes suites convergentes et les mêmes fonctions continues.

## Démonstrations

\textbf{Théorème :} Dans un espace métrique $(X, d)$, toute boule ouverte $B(a, r)$ est un ouvert pour la topologie induite.

\textit{Démonstration rigoureuse pas-à-pas :}
Soit $B(a, r)$ une boule ouverte. Il faut montrer que pour tout point $x \in B(a, r)$, il existe un rayon $\epsilon > 0$ tel que $B(x, \epsilon) \subset B(a, r)$.

1. Soit $x \in B(a, r)$. Par définition, nous savons que $d(a, x) < r$.
2. Posons $\epsilon = r - d(a, x)$. Puisque $d(a, x) < r$, nous avons bien $\epsilon > 0$.
3. Montrons l'inclusion. Soit $y \in B(x, \epsilon)$. Par définition, cela signifie que $d(x, y) < \epsilon$.
4. Évaluons la distance de $y$ au centre $a$. Par l'inégalité triangulaire de la distance $d$ :
   $$ d(a, y) \le d(a, x) + d(x, y) $$
5. En utilisant l'inégalité $d(x, y) < \epsilon$, nous obtenons :
   $$ d(a, y) < d(a, x) + \epsilon $$
6. Remplaçons $\epsilon$ par sa valeur :
   $$ d(a, y) < d(a, x) + (r - d(a, x)) $$
   $$ d(a, y) < r $$
7. Par conséquent, $y \in B(a, r)$. L'inclusion $B(x, \epsilon) \subset B(a, r)$ est démontrée. La boule ouverte est donc bien un voisinage de chacun de ses points. \hfill $\blacksquare$

## Applications en Physique, Logique et Apprentissage Automatique

- \textbf{Optimisation et Descente de Gradient :} Dans les algorithmes d'optimisation, la notion de distance est fondamentale pour évaluer la convergence d'une suite d'itérés $(x_n)_{n \in \mathbb{N}}$ vers un minimum local. Le critère d'arrêt est souvent formulé comme $d(x_{n+1}, x_n) < \epsilon$.
- \textbf{K-Plus Proches Voisins (K-NN) :} L'algorithme K-NN, très utilisé en classification, repose entièrement sur la métrique choisie pour l'espace des descripteurs. Le choix entre une distance de Manhattan ($L^1$), euclidienne ($L^2$) ou de Tchebychev ($L^\infty$) modifie la frontière de décision géométrique du classifieur.
- \textbf{Analyse des signaux et de l'audio :} Dans l'espace des fonctions $\mathcal{C}([a,b], \mathbb{R})$, l'utilisation de distances intégrales permet de comparer deux signaux continus. Par exemple, $d(f, g) = \int_a^b |f(t) - g(t)| dt$ quantifie l'erreur moyenne de reconstruction d'un signal filtré.
