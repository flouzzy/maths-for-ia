---
uuid: "jalon-54"
title: "Compacité générale"
year: 2
trimester: 5
tags:
  - math/topologie
  - ia/convergence
prev: "[[Jalon 53 (Axiomes de séparation).md]]"
next: "[[Jalon 55 (Connexité).md]]"
---
# Compacité Générale

## Introduction

La compacité est l'un des concepts les plus profonds et puissants de la topologie générale et de l'analyse moderne. Elle constitue la clé de voûte permettant de transférer les propriétés de finitude à des espaces continus infinis. Essentiellement, un espace compact est un espace qui, bien que potentiellement infini, ne contient pas suffisamment de "place" pour qu'une suite puisse s'y échapper sans accumuler ses valeurs autour d'un point limite. Historiquement, la formalisation de la compacité a émergé des travaux de Borel et Lebesgue sur le recouvrement des intervalles réels fermés et bornés, avant d'être généralisée par Alexandrov, Urysohn et Tychonoff aux espaces topologiques abstraits.

## Définitions, Théorèmes et Exemples

### La Propriété de Borel-Lebesgue

Soit $(X, \mathcal{T})$ un espace topologique.

Un recouvrement ouvert de $X$ est une famille d'ouverts $(U_i)_{i \in I}$ telle que $X = \bigcup_{i \in I} U_i$.

Un espace $X$ est dit compact s'il est séparé (au sens de Hausdorff, c'est-à-dire que deux points distincts admettent des voisinages disjoints) et si, de tout recouvrement ouvert de $X$, on peut extraire un sous-recouvrement fini. Autrement dit :
$$ \forall (U_i)_{i \in I} \in \mathcal{T}^I, \quad X = \bigcup_{i \in I} U_i \implies \exists J \subset I, J \text{ fini, } X = \bigcup_{j \in J} U_j $$

**Exemple Concret :**
Considérons le segment réel $X = [0, 1]$. Prenons le recouvrement ouvert infini constitué des intervalles $U_n = \left( \frac{1}{n}, 1 \right]$ pour $n \ge 2$, auquel on adjoint $U_0 = \left[ 0, \frac{1}{4} \right)$.
Clairement, $\bigcup_{n \ge 2} U_n \cup U_0 = [0, 1]$. Puisque $[0, 1]$ est compact (théorème de Borel-Lebesgue usuel), on peut en extraire un sous-recouvrement fini. Ici, il suffit de prendre $U_0$ et $U_5 = \left( \frac{1}{5}, 1 \right]$, car $U_0 \cup U_5 = \left[ 0, \frac{1}{4} \right) \cup \left( \frac{1}{5}, 1 \right] = [0, 1]$.

**Cas Pathologique :**
L'intervalle ouvert $Y = (0, 1)$ n'est pas compact. En effet, considérons le recouvrement ouvert donné par les ensembles $V_n = \left( \frac{1}{n}, 1 \right)$ pour $n \ge 2$. La réunion de tous ces $V_n$ recouvre bien $(0, 1)$. Cependant, toute sous-famille finie de ce recouvrement possède un plus grand indice $N$, et sa réunion sera simplement $V_N = \left( \frac{1}{N}, 1 \right)$, ce qui laisse le sous-intervalle $\left( 0, \frac{1}{N} \right]$ non recouvert.

\begin{tikzpicture}[scale=1.5]
  % Axe réel
  \draw[->] (-0.5,0) -- (4,0) node[right] {$\mathbb{R}$};
  \draw (0,0.1) -- (0,-0.1) node[below] {$0$};
  \draw (3,0.1) -- (3,-0.1) node[below] {$1$};

  % Ouverts Un
  \draw[thick, blue] (1.5,0.2) -- (3,0.2) node[above, pos=0.5] {$U_2$};
  \draw[blue, fill=white] (1.5,0.2) circle (0.05);
  \draw[blue, fill=blue] (3,0.2) circle (0.05);

  \draw[thick, red] (1,0.4) -- (3,0.4) node[above, pos=0.5] {$U_3$};
  \draw[red, fill=white] (1,0.4) circle (0.05);
  \draw[red, fill=red] (3,0.4) circle (0.05);

  \draw[thick, green!70!black] (0.6,0.6) -- (3,0.6) node[above, pos=0.5] {$U_5$};
  \draw[green!70!black, fill=white] (0.6,0.6) circle (0.05);
  \draw[green!70!black, fill=green!70!black] (3,0.6) circle (0.05);

  \draw[thick, orange] (0,0.8) -- (0.75,0.8) node[above, pos=0.5] {$U_0$};
  \draw[orange, fill=orange] (0,0.8) circle (0.05);
  \draw[orange, fill=white] (0.75,0.8) circle (0.05);
\end{tikzpicture}

### Caractérisation par les Fermés et Intersection Finie

Une formulation duale et équivalente de la compacité s'exprime en termes de fermés et de la propriété de l'intersection finie.

Une famille de parties $(A_i)_{i \in I}$ possède la propriété d'intersection finie si pour toute sous-famille finie $J \subset I$, l'intersection $\bigcap_{j \in J} A_j$ est non vide.

Un espace topologique $X$ est compact si et seulement si toute famille de fermés de $X$ possédant la propriété d'intersection finie a une intersection globale non vide : $\bigcap_{i \in I} F_i \neq \emptyset$.

**Exemple Concret :**
Prenons $X = [0, 1]$ et la suite de fermés emboîtés $F_n = \left[ 0, \frac{1}{n} \right]$ pour $n \ge 1$. Toute sous-famille finie a une intersection qui est simplement le "plus petit" des intervalles (celui correspondant au plus grand $n$), qui est non vide. La compacité assure que l'intersection globale $\bigcap_{n \ge 1} F_n$ est non vide. Ici, cette intersection contient exactement le point $\{0\}$.

\begin{tikzpicture}[scale=1.5]
  % Axe réel
  \draw[->] (-0.5,0) -- (4,0) node[right] {$\mathbb{R}$};
  \draw (0,0.1) -- (0,-0.1) node[below] {$0$};
  \draw (3,0.1) -- (3,-0.1) node[below] {$1$};

  \draw[thick, purple] (0,0.2) -- (3,0.2) node[above, pos=1] {$F_1$};
  \draw[purple, fill=purple] (0,0.2) circle (0.05);
  \draw[purple, fill=purple] (3,0.2) circle (0.05);

  \draw[thick, purple] (0,0.4) -- (1.5,0.4) node[above, pos=1] {$F_2$};
  \draw[purple, fill=purple] (0,0.4) circle (0.05);
  \draw[purple, fill=purple] (1.5,0.4) circle (0.05);

  \draw[thick, purple] (0,0.6) -- (1,0.6) node[above, pos=1] {$F_3$};
  \draw[purple, fill=purple] (0,0.6) circle (0.05);
  \draw[purple, fill=purple] (1,0.6) circle (0.05);
\end{tikzpicture}

## Démonstrations

### L'image continue d'un compact est compacte

**Théorème :** Soit $f : X \to Y$ une application continue. Si $X$ est compact, alors son image $f(X)$ est un espace compact (pour la topologie induite).

**Démonstration :**
Soit $(V_i)_{i \in I}$ un recouvrement ouvert de $f(X)$ par des ouverts de $Y$.
Puisque $f(X) \subset \bigcup_{i \in I} V_i$, on a en prenant l'image réciproque :
$X = f^{-1}(f(X)) \subset f^{-1}\left( \bigcup_{i \in I} V_i \right) = \bigcup_{i \in I} f^{-1}(V_i)$.
L'application $f$ étant continue, pour chaque $i \in I$, l'ensemble $U_i = f^{-1}(V_i)$ est un ouvert de $X$.
La famille $(U_i)_{i \in I}$ forme donc un recouvrement ouvert de l'espace compact $X$.
Par définition de la compacité de $X$, il existe une sous-famille finie $J \subset I$ telle que $X = \bigcup_{j \in J} U_j$.
En appliquant $f$ aux deux membres de l'égalité, on obtient :
$f(X) = f\left( \bigcup_{j \in J} U_j \right) = \bigcup_{j \in J} f(U_j)$.
Or, par construction, $f(U_j) = f(f^{-1}(V_j)) \subset V_j$.
Par conséquent, $f(X) \subset \bigcup_{j \in J} V_j$.
Nous avons ainsi extrait un sous-recouvrement fini $(V_j)_{j \in J}$ du recouvrement ouvert initial. L'espace $f(X)$ satisfait la propriété de Borel-Lebesgue, il est donc compact. $\blacksquare$

### Compacité Séquentielle dans les Espaces Métriques (Théorème de Bolzano-Weierstrass)

**Théorème :** Dans un espace métrique $(X, d)$, la compacité topologique (Borel-Lebesgue) est équivalente à la compacité séquentielle : de toute suite $(x_n)_{n \in \mathbb{N}}$ d'éléments de $X$, on peut extraire une sous-suite convergente vers un élément $l \in X$.

**Démonstration (Implication Borel-Lebesgue $\implies$ Compacité séquentielle) :**
Soit $X$ un espace compact et $(x_n)_{n \in \mathbb{N}}$ une suite dans $X$. Supposons par l'absurde que cette suite n'admette aucune valeur d'adhérence.
Alors, pour tout point $y \in X$, $y$ n'est pas une valeur d'adhérence de la suite. Cela signifie qu'il existe un ouvert $U_y$ contenant $y$ tel que $U_y$ ne contient qu'un nombre fini de termes de la suite $(x_n)$.
La famille $(U_y)_{y \in X}$ constitue manifestement un recouvrement ouvert de $X$.
Puisque $X$ est compact, on peut en extraire un sous-recouvrement fini $U_{y_1}, U_{y_2}, \dots, U_{y_k}$.
Ainsi, $X = \bigcup_{i=1}^k U_{y_i}$.
Or, chaque ouvert $U_{y_i}$ ne contient qu'un nombre fini de termes de la suite. L'union finie $\bigcup_{i=1}^k U_{y_i}$ ne peut donc contenir qu'un nombre fini de termes de la suite.
Mais cette union est l'espace $X$ tout entier, qui contient la totalité des termes de la suite (qui sont en nombre infini). Nous aboutissons à une contradiction.
Par conséquent, la suite $(x_n)$ admet au moins une valeur d'adhérence $l \in X$. Dans un espace métrique, cela implique l'existence d'une sous-suite convergente vers $l$. $\blacksquare$


**Exemple Concret 3 (Image continue) :** Considérons la fonction sinus $f(x) = \sin(x)$ sur le segment compact $[0, 2\pi]$. Son image est $[-1, 1]$, qui est bien un compact (fermé et borné). Si on la considère sur l'ouvert non compact $(0, 2\pi)$, l'image est aussi $[-1, 1]$ (qui est compact), mais l'image d'un non-compact n'est pas obligatoirement non-compacte. Par contre, si on prend $f(x) = 1/x$ sur l'ouvert non compact $(0, 1)$, l'image est $(1, +\infty)$, qui n'est pas compact.

**Exemple Concret 4 (Bolzano-Weierstrass) :** Prenons la suite $x_n = (-1)^n (1 - 1/n)$. Elle vit dans le compact $[-1, 1]$. Elle n'est pas convergente, mais elle a deux valeurs d'adhérence: -1 et 1. On peut extraire la sous-suite des indices pairs qui converge vers 1, et des impairs vers -1.


## Applications en Physique, Logique et Intelligence Artificielle

En apprentissage statistique (Machine Learning), le théorème des bornes atteintes (corollaire direct du fait que l'image continue d'un compact est compacte) est fondamental. Pour entraîner un modèle paramétré par $\theta \in \Theta$, on cherche à minimiser une fonction de coût (ou perte empirique) $L(\theta)$.
Si l'espace des paramètres $\Theta$ est un compact de $\mathbb{R}^d$ (par exemple, grâce à une pénalisation en norme type régression Ridge ou Lasso qui contraint les paramètres dans une boule fermée) et que la fonction de coût $L$ est continue par rapport à $\theta$, alors l'existence d'un minimiseur global $\theta^\star$ est mathématiquement garantie : il existe $\theta^\star \in \Theta$ tel que $L(\theta^\star) = \min_{\theta \in \Theta} L(\theta)$.

De plus, en théorie de l'apprentissage PAC (Probably Approximately Correct), la notion de capacité d'un espace d'hypothèses (comme l'entropie métrique ou la dimension de Vapnik-Chervonenkis) repose sur la capacité de recouvrir cet espace par un nombre fini de boules de petit rayon (précompacité). La compacité des espaces de fonctions permet d'établir des bornes uniformes d'erreur de généralisation, empêchant le sur-apprentissage (overfitting) catastrophique en garantissant que l'espace des fonctions n'est pas "trop grand".
