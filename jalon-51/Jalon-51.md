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

# Espaces métriques et topologies induites

La notion de distance est le fondement géométrique de l'analyse moderne. Issue des travaux de Maurice Fréchet et Felix Hausdorff au début du XXe siècle, elle permet d'étendre la rigueur des limites et de la continuité (définies sur $\mathbb{R}$) à des ensembles abstraits arbitraires (fonctions, matrices, graphes). En s'affranchissant de toute structure algébrique sous-jacente, l'espace métrique constitue la structure topologique la plus naturelle et la plus intuitive pour modéliser la proximité, l'approximation et la convergence.

## Distances et axiomes fondamentaux

Soit $X$ un ensemble non vide.

\textbf{Définition (Distance) :}
Une application $d : X \times X \to \mathbb{R}_+$ est une distance sur $X$ si elle vérifie les trois axiomes suivants pour tout $(x, y, z) \in X^3$ :
1. \textbf{Séparation :} $d(x, y) = 0 \iff x = y$.
2. \textbf{Symétrie :} $d(x, y) = d(y, x)$.
3. \textbf{Inégalité triangulaire :} $d(x, z) \le d(x, y) + d(y, z)$.

Le couple $(X, d)$ est alors appelé un espace métrique.

\textbf{Exemple géométrique immédiat (Distance euclidienne sur $\mathbb{R}^2$) :}
Pour $x = (x_1, x_2)$ et $y = (y_1, y_2)$ dans $\mathbb{R}^2$, l'application $d_2(x, y) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2}$ est une distance. La séparation et la symétrie sont triviales, et l'inégalité triangulaire découle de l'inégalité de Cauchy-Schwarz sur le produit scalaire canonique.

\textbf{Exemple pathologique (Distance discrète) :}
Sur un ensemble arbitraire $X$, définissons $d(x, y) = 1$ si $x \neq y$ et $d(x, x) = 0$. Il s'agit d'une métrique valide. En effet, l'inégalité triangulaire $d(x, z) \le d(x, y) + d(y, z)$ est satisfaite car si $x \neq z$, alors $d(x, z) = 1$. Or, $y$ ne peut être simultanément égal à $x$ et à $z$. Ainsi, $d(x, y)$ ou $d(y, z)$ vaut $1$, et la somme est supérieure ou égale à $1$.

\begin{center}
\begin{tikzpicture}[scale=1.5]
  % Triangle points
  \coordinate (X) at (0,0);
  \coordinate (Y) at (3,1);
  \coordinate (Z) at (2,3);

  % Draw points
  \fill[black] (X) circle (2pt) node[below left] {$x$};
  \fill[black] (Y) circle (2pt) node[below right] {$y$};
  \fill[black] (Z) circle (2pt) node[above] {$z$};

  % Draw lines
  \draw[thick, blue] (X) -- (Z) node[midway, left] {$d(x,z)$};
  \draw[dashed, red] (X) -- (Y) node[midway, below] {$d(x,y)$};
  \draw[dashed, red] (Y) -- (Z) node[midway, right] {$d(y,z)$};
\end{tikzpicture}
\\
\textit{Illustration géométrique de l'inégalité triangulaire : le chemin direct (bleu) est toujours plus court ou égal au chemin avec détour (rouge).}
\end{center}

## Topologie induite par une métrique

La puissance des espaces métriques réside dans leur capacité à engendrer canoniquement une structure topologique.

\textbf{Définition (Boules) :}
Soit $(X, d)$ un espace métrique, $a \in X$ et $r > 0$.
- La boule ouverte de centre $a$ et de rayon $r$ est : $B(a, r) = \{ x \in X \mid d(a, x) < r \}$.
- La boule fermée de centre $a$ et de rayon $r$ est : $\overline{B}(a, r) = \{ x \in X \mid d(a, x) \le r \}$.

\textbf{Théorème (Génération de la topologie) :}
Soit $(X, d)$ un espace métrique. L'ensemble $\mathcal{T}_d$ des parties $O \subset X$ telles que pour tout $x \in O$, il existe $r > 0$ vérifiant $B(x, r) \subset O$, forme une topologie sur $X$.

\textbf{Démonstration détaillée :}
Montrons d'abord qu'une boule ouverte est un ouvert de $\mathcal{T}_d$. Soit $B(a, R)$ une boule ouverte. Considérons un point arbitraire $x \in B(a, R)$. Par définition, $d(a, x) < R$. Posons $r = R - d(a, x) > 0$.
Soit $y \in B(x, r)$. Nous devons prouver que $y \in B(a, R)$.
Par l'inégalité triangulaire :
$$ d(a, y) \le d(a, x) + d(x, y) < d(a, x) + r = d(a, x) + R - d(a, x) = R $$
Donc $d(a, y) < R$, ce qui implique $y \in B(a, R)$. Ainsi $B(x, r) \subset B(a, R)$, et la boule ouverte est bien un ouvert topologique.

Les axiomes de la topologie (stabilité par union quelconque et intersection finie) découlent ensuite directement de cette caractérisation par les boules locales.

\begin{center}
\begin{tikzpicture}[scale=2]
  % Main ball B(a, R)
  \draw[blue, thick] (0,0) circle (1.5cm);
  \fill[blue, opacity=0.1] (0,0) circle (1.5cm);
  \fill[black] (0,0) circle (1pt) node[below] {$a$};

  % Radius R
  \draw[->, blue, dashed] (0,0) -- (1.06, 1.06) node[midway, above left] {$R$};

  % Sub-ball B(x, r)
  \coordinate (X) at (0.8, 0.3);
  \draw[red, thick] (X) circle (0.6cm);
  \fill[red, opacity=0.2] (X) circle (0.6cm);
  \fill[black] (X) circle (1pt) node[below] {$x$};

  % Radius r
  \draw[->, red, dashed] (X) -- +(0.6, 0) node[midway, below] {$r$};

  % Line from a to x
  \draw[dashed] (0,0) -- (X) node[midway, above] {$d(a,x)$};
\end{tikzpicture}
\\
\textit{Construction géométrique prouvant qu'une boule ouverte est un ouvert : pour tout point $x$, on peut inscrire une sous-boule de rayon $r = R - d(a,x)$.}
\end{center}

## Distances équivalentes

\textbf{Définition (Équivalence) :}
Deux distances $d_1$ et $d_2$ sur $X$ sont dites (topologiquement) équivalentes s'il existe des constantes $C_1 > 0, C_2 > 0$ telles que pour tout $x, y \in X$ :
$$ C_1 d_1(x, y) \le d_2(x, y) \le C_2 d_1(x, y) $$

\textbf{Proposition :}
Si deux distances sont équivalentes, elles induisent exactement la même topologie sur $X$ (les mêmes ouverts, les mêmes fermés, les mêmes suites convergentes).

\textbf{Exemple (Normes sur $\mathbb{R}^n$) :}
Sur $\mathbb{R}^n$, la distance de Manhattan $d_1(x,y) = \sum |x_i - y_i|$, la distance euclidienne $d_2(x,y) = \sqrt{\sum (x_i - y_i)^2}$, et la distance infinie $d_\infty(x,y) = \max |x_i - y_i|$ sont toutes équivalentes, car $\mathbb{R}^n$ est de dimension finie. Par exemple, $d_\infty(x,y) \le d_2(x,y) \le \sqrt{n} d_\infty(x,y)$.

## Applications en Physique et Intelligence Artificielle

En apprentissage automatique, le choix de la métrique définit la géométrie de l'espace de représentation. Par exemple, l'algorithme des $k$-plus proches voisins (k-NN) s'appuie directement sur un espace métrique. De même, les distances de Wasserstein (issues du transport optimal de Monge-Kantorovich) permettent de quantifier la proximité entre des distributions de probabilité dans les réseaux antagonistes génératifs (WGAN), surmontant les limites de la divergence de Kullback-Leibler qui ne satisfait pas l'inégalité triangulaire ni la symétrie.
