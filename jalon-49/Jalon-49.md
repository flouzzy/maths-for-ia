---
uuid: "jalon-49"
title: "Espaces topologiques généraux"
year: 2
trimester: 5
tags:
  - math/topologie
  - ia/abstraction
prev: "[[Jalon 48 (Livrable IA).md]]"
next: "[[Jalon 50 (Opérateurs topologiques).md]]"
---
# Jalon 49 : Espaces topologiques généraux

\section{Introduction : Genèse et intuition géométrique}

La géométrie euclidienne et la théorie des espaces métriques reposent sur la notion de distance : on peut mesurer rigoureusement l'écart entre deux points. Toutefois, de nombreuses situations mathématiques exigent d'étudier la continuité, la convergence ou les propriétés globales d'espaces où aucune distance naturelle ne peut être définie (comme des espaces de fonctions très vastes, ou la topologie de Zariski en géométrie algébrique).

L'intuition fondatrice de la topologie générale, initiée par Felix Hausdorff et Maurice Fréchet, est de s'abstraire de la distance pour ne conserver que la notion pure de "voisinage" ou de "proximité". Imaginez une membrane élastique infiniment déformable : tant qu'on ne la déchire pas et qu'on ne recolle pas des points distincts, les éléments initialement voisins restent voisins. La topologie est l'étude mathématique rigoureuse de ces déformations continues. Au lieu de s'appuyer sur des boules de rayon $\epsilon$, on se base axiomatiquement sur la donnée d'une collection d'ensembles privilégiés appelés "ouverts".

\begin{center}
\begin{tikzpicture}[scale=1]
  \draw[thick, fill=blue!10] (0,0) ellipse (2cm and 1cm);
  \node at (0,0) {$\bullet$};
  \node[above] at (0,0) {$x$};
  \node[right] at (1, 0.5) {$U$};
  \node[below] at (0, -1.2) {Un ouvert $U$ contenant $x$};

  \draw[->, thick, shorten >=5pt, shorten <=5pt] (2.5,0) -- (4.5,0) node[midway, above] {Déformation continue};

  \draw[thick, fill=red!10] (6,0) to[out=90,in=180] (7,1.5) to[out=0,in=90] (8,-0.5) to[out=270,in=0] (7,-1) to[out=180,in=270] (6,0);
  \node at (6.8,0.2) {$\bullet$};
  \node[above] at (6.8,0.2) {$f(x)$};
  \node[right] at (7.5, 0.8) {$f(U)$};
  \node[below] at (7, -1.2) {L'image est toujours un voisinage};
\end{tikzpicture}
\end{center}

\section{Définitions et théorèmes fondamentaux}

\subsection{Topologie et Ouverts}

Soit $X$ un ensemble.

\textbf{Définition (Topologie) :}
Une topologie sur $X$ est une collection $\mathcal{T}$ de sous-ensembles de $X$ (appelés les ouverts) satisfaisant les trois axiomes suivants :
1. L'ensemble vide $\emptyset$ et l'espace entier $X$ appartiennent à $\mathcal{T}$.
2. L'intersection d'un nombre \textbf{fini} d'ouverts est un ouvert : si $O_1, \dots, O_n \in \mathcal{T}$, alors $\bigcap_{i=1}^n O_i \in \mathcal{T}$.
3. La réunion d'une famille \textbf{quelconque} d'ouverts est un ouvert : si $(O_i)_{i \in I}$ est une famille d'éléments de $\mathcal{T}$, alors $\bigcup_{i \in I} O_i \in \mathcal{T}$.

Le couple $(X, \mathcal{T})$ est appelé un espace topologique.

\textbf{Exemple concret (Topologie discrète) :}
Si $X = \{a, b, c\}$, la topologie discrète est $\mathcal{T}_{discr\grave{e}te} = \mathcal{P}(X) = \{\emptyset, \{a\}, \{b\}, \{c\}, \{a,b\}, \{a,c\}, \{b,c\}, X\}$. Tous les sous-ensembles sont ouverts.

\textbf{Exemple concret (Topologie grossière) :}
Sur le même $X$, la topologie grossière est $\mathcal{T}_{grossi\grave{e}re} = \{\emptyset, X\}$. Seuls l'ensemble vide et $X$ sont ouverts.

\textbf{Exemple concret (Topologie usuelle sur $\mathbb{R}$) :}
La topologie usuelle sur $\mathbb{R}$ est définie en disant qu'un ensemble $U$ est ouvert si pour tout $x \in U$, il existe $\epsilon > 0$ tel que l'intervalle ouvert $]x-\epsilon, x+\epsilon[$ soit inclus dans $U$.

\subsection{Fermés et Voisinages}

\textbf{Définition (Fermé) :}
Un sous-ensemble $F$ de $X$ est dit fermé si son complémentaire $X \setminus F$ est un ouvert.

\textbf{Définition (Voisinage) :}
Soit $x \in X$. Un sous-ensemble $V \subset X$ est un voisinage de $x$ s'il existe un ouvert $U \in \mathcal{T}$ tel que $x \in U \subset V$.
L'ensemble des voisinages de $x$ est noté $\mathcal{V}(x)$.

\textbf{Théorème (Caractérisation des ouverts par les voisinages) :}
Un sous-ensemble $U$ de $X$ est ouvert si et seulement si, pour tout $x \in U$, $U$ est un voisinage de $x$.

\textbf{Cas pathologique (Topologie cofinie) :}
Soit $X$ infini (par exemple $X = \mathbb{R}$). On définit $\mathcal{T}_{cofinie} = \{\emptyset\} \cup \{U \subset X \mid X \setminus U \text{ est fini}\}$. Dans cette topologie, deux ouverts non vides ont toujours une intersection non vide. Il n'est donc pas possible de "séparer" deux points par des voisinages disjoints (cet espace n'est pas séparé au sens de Hausdorff).

\section{Démonstrations}

\subsection{Démonstration de la stabilité des fermés}

Nous allons démontrer que l'intersection d'une famille quelconque de fermés est un fermé, et que la réunion finie de fermés est un fermé.

\textbf{Preuve pas à pas :}
1. Soit $(F_i)_{i \in I}$ une famille quelconque de fermés de $X$. Par définition, pour tout $i \in I$, le complémentaire $O_i = X \setminus F_i$ est un ouvert ($O_i \in \mathcal{T}$).
2. Considérons l'intersection $F = \bigcap_{i \in I} F_i$.
3. En utilisant les lois de De Morgan, le complémentaire de $F$ est :
   $$ X \setminus F = X \setminus \left( \bigcap_{i \in I} F_i \right) = \bigcup_{i \in I} (X \setminus F_i) = \bigcup_{i \in I} O_i $$
4. Puisque $(O_i)_{i \in I}$ est une famille d'ouverts, l'axiome 3 des topologies assure que leur réunion quelconque est un ouvert. Donc $X \setminus F \in \mathcal{T}$.
5. Ainsi, $F$ est le complémentaire d'un ouvert, donc $F$ est fermé.
6. Considérons maintenant une famille \textbf{finie} de fermés $F_1, \dots, F_n$. Leurs complémentaires $O_k = X \setminus F_k$ sont ouverts.
7. Soit la réunion $G = \bigcup_{k=1}^n F_k$. Son complémentaire est, par les lois de De Morgan :
   $$ X \setminus G = X \setminus \left( \bigcup_{k=1}^n F_k \right) = \bigcap_{k=1}^n (X \setminus F_k) = \bigcap_{k=1}^n O_k $$
8. Par l'axiome 2, l'intersection finie d'ouverts est un ouvert. Donc $X \setminus G \in \mathcal{T}$.
9. Ainsi, $G$ est fermé. $\blacksquare$

\section{Applications en Physique, Logique et Intelligence Artificielle}

En intelligence artificielle, les topologies générales interviennent dans la modélisation des graphes discrets (Graph Neural Networks). Un graphe peut être vu comme un espace topologique où les voisinages sont définis par la connectivité des nœuds.

De plus, l'apprentissage de variétés (Manifold Learning, comme t-SNE ou UMAP) vise explicitement à trouver un plongement de données de haute dimension dans un espace de basse dimension tout en préservant la topologie locale. L'algorithme UMAP (Uniform Manifold Approximation and Projection) construit d'ailleurs explicitement un complexe simplicial et une topologie floue (fuzzy topology) sur les données pour approximer la variété sous-jacente. L'étude de ces voisinages sans recourir à la stricte distance euclidienne globale permet de capturer la géométrie intrinsèque des données complexes.
