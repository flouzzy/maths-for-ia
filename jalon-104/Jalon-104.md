---
uuid: "jalon-104"
title: "Bases hilbertiennes"
year: 3
trimester: 9
tags:
  - math/analyse
  - ia/abstraction
prev: "[[Jalon 103 (Espaces de Hilbert généraux).md]]"
next: "[[Jalon 105 (Opérateurs adjoints).md]]"
---

# Jalon 104 : Bases hilbertiennes

## Présentation du concept clé

Travailler avec des fonctions est souvent complexe. Cependant, travailler avec des listes de nombres (des suites) est beaucoup plus simple sur le plan computationnel. Les bases hilbertiennes permettent de transformer de manière isométrique n'importe quel espace de Hilbert complexe (comme $L^2$) en un espace de suites simple (comme $\ell^2$). C'est la numérisation universelle de l'analyse, un concept d'une grande puissance géométrique.

Une base hilbertienne peut être pensée comme une collection minimale de vecteurs (orthogonaux entre eux) nécessaires pour reconstruire, à l'infini, n'importe quel élément de l'espace. La reconstruction d'un élément ne demande que de connaître sa composante exacte sur chacun de ces vecteurs de base (ce sont les coefficients de Fourier).

\begin{center}
\begin{tikzpicture}[scale=1.5]
    % Axes
    \draw[->, thick, gray] (-1.5,0) -- (2.5,0) node[right] {$e_1$};
    \draw[->, thick, gray] (0,-1) -- (0,2.5) node[above] {$e_2$};

    % Vector x
    \coordinate (x) at (1.8, 1.4);
    \draw[->, thick, blue] (0,0) -- (x) node[above right] {$x \in H$};

    % Projections
    \draw[dashed, blue] (x) -- (1.8,0);
    \draw[dashed, blue] (x) -- (0,1.4);

    % Projection vectors
    \draw[->, thick, red] (0,0) -- (1.8,0) node[midway, below] {$\langle x, e_1 \rangle e_1$};
    \draw[->, thick, red] (0,0) -- (0,1.4) node[midway, left] {$\langle x, e_2 \rangle e_2$};

    % Point at origin
    \filldraw (0,0) circle (1pt) node[below left] {$0$};
\end{tikzpicture}
\end{center}

L'idée fondamentale de la base hilbertienne généralise exactement ce processus de projection orthogonale à une infinité dénombrable de dimensions.

## Formalisation

Soit $H$ un espace de Hilbert, muni d'un produit scalaire $\langle \cdot, \cdot \rangle$ et de la norme induite $\| \cdot \|$.

### Familles Orthonormées

> **Définition (Famille orthonormée) :** Une famille $(e_i)_{i \in I}$ d'éléments de $H$ est dite **orthonormée** si :
> $$\forall i, j \in I, \quad \langle e_i, e_j \rangle = \delta_{ij} = \begin{cases} 1 & \text{si } i=j \\ 0 & \text{si } i \neq j \end{cases}$$

**Exemple concret 1 : Calcul sur une famille orthonormée finie**
Considérons $H = \mathbb{R}^3$ avec le produit scalaire usuel.
Soient $e_1 = (1, 0, 0)$, $e_2 = (0, 1, 0)$ et $e_3 = (0, 0, 1)$.
On vérifie l'orthonormalité :
$\|e_1\|^2 = \langle e_1, e_1 \rangle = 1 \times 1 + 0 \times 0 + 0 \times 0 = 1$.
$\langle e_1, e_2 \rangle = 1 \times 0 + 0 \times 1 + 0 \times 0 = 0$.
Cette famille est trivialement orthonormée, ce qui correspond géométriquement à trois axes perpendiculaires de longueur 1.

**Exemple concret 2 : La base de Fourier exponentielle dans $L^2(0, 2\pi)$**
Considérons l'espace des fonctions de carré intégrable $H = L^2([0, 2\pi], \mathbb{C})$ muni du produit scalaire :
$$ \langle f, g \rangle = \frac{1}{2\pi} \int_{0}^{2\pi} f(t) \overline{g(t)} dt $$
On pose $e_n(t) = e^{int}$ pour $n \in \mathbb{Z}$.
Calculons la norme :
$$ \|e_n\|^2 = \langle e_n, e_n \rangle = \frac{1}{2\pi} \int_{0}^{2\pi} e^{int} e^{-int} dt = \frac{1}{2\pi} \int_{0}^{2\pi} 1 dt = 1 $$
Calculons le produit scalaire pour $n \neq m$ :
$$ \langle e_n, e_m \rangle = \frac{1}{2\pi} \int_{0}^{2\pi} e^{int} e^{-imt} dt = \frac{1}{2\pi} \int_{0}^{2\pi} e^{i(n-m)t} dt $$
$$ = \frac{1}{2\pi} \left[ \frac{e^{i(n-m)t}}{i(n-m)} \right]_0^{2\pi} = \frac{1}{2\pi i (n-m)} (e^{i(n-m)2\pi} - e^0) $$
Puisque $n-m$ est un entier non nul, $e^{i(n-m)2\pi} = 1$. Donc :
$$ \langle e_n, e_m \rangle = \frac{1}{2\pi i (n-m)} (1 - 1) = 0 $$
La famille $(e_n)_{n \in \mathbb{Z}}$ est bien orthonormée dans $H$.

### Bases Hilbertiennes

> **Définition (Base Hilbertienne) :**
> Une famille orthonormée $(e_n)_{n \in \mathbb{N}}$ est une **base hilbertienne** de $H$ si elle est **totale**, c'est-à-dire que le sous-espace vectoriel qu'elle engendre algébriquement est dense dans $H$ ($\overline{\text{vect}(\{e_n \mid n \in \mathbb{N}\})} = H$).
>
> Dans ce cas, tout vecteur $x \in H$ s'écrit de manière unique comme somme d'une série convergente dans $H$ :
> $$x = \sum_{n=0}^\infty \langle x, e_n \rangle e_n$$
> Les scalaires $\langle x, e_n \rangle$ sont appelés les **coefficients de Fourier** de $x$ par rapport à la base $(e_n)$.

**Exemple concret 3 : Reconstruction d'un vecteur avec une base hilbertienne**
Prenons l'espace $\ell^2(\mathbb{N})$ des suites de carrés sommables. La base canonique est donnée par les suites $e_n$ où le $n$-ième terme est $1$ et les autres $0$.
Soit $x = (1, \frac{1}{2}, \frac{1}{4}, \frac{1}{8}, \dots) \in \ell^2(\mathbb{N})$.
Calculons les coefficients de Fourier $\langle x, e_n \rangle$.
$\langle x, e_0 \rangle = 1 \times 1 + 0 = 1$.
$\langle x, e_1 \rangle = \frac{1}{2} \times 1 = \frac{1}{2}$.
De manière générale, $\langle x, e_n \rangle = \frac{1}{2^n}$.
La série $\sum_{n=0}^N \langle x, e_n \rangle e_n$ est le vecteur $(1, \frac{1}{2}, \dots, \frac{1}{2^N}, 0, 0, \dots)$.
La distance au carré entre $x$ et cette somme partielle est :
$$ \| x - \sum_{n=0}^N \langle x, e_n \rangle e_n \|^2 = \sum_{k=N+1}^\infty \left(\frac{1}{2^k}\right)^2 = \sum_{k=N+1}^\infty \frac{1}{4^k} $$
C'est le reste d'une série géométrique convergente de raison $1/4$, qui tend vers $0$ lorsque $N \to \infty$. La série converge bien vers $x$ dans l'espace $\ell^2$.

### Théorèmes de Caractérisation

> **Théorème (Équivalences fondamentales) :** Soit $(e_n)_{n \in \mathbb{N}}$ une famille orthonormée de l'espace de Hilbert $H$. Les propositions suivantes sont strictement équivalentes :
> 1. $(e_n)$ est une base hilbertienne.
> 2. Pour tout $x \in H$, si $\forall n \in \mathbb{N}, \langle x, e_n \rangle = 0$, alors $x=0$ (l'orthogonal de la famille est réduit au vecteur nul).
> 3. **Identité de Parseval :** $\forall x \in H, \|x\|^2 = \sum_{n=0}^\infty |\langle x, e_n \rangle|^2$.

**Exemple concret 4 : Application de l'identité de Parseval**
Considérons à nouveau $H = L^2([0, 2\pi])$ et la base hilbertienne $e_n(t) = e^{int}$.
Soit la fonction $f(t) = t$. Calculons ses coefficients de Fourier (pour $n \neq 0$) :
$$ c_n = \langle f, e_n \rangle = \frac{1}{2\pi} \int_0^{2\pi} t e^{-int} dt $$
Par intégration par parties :
$$ u(t) = t \implies u'(t) = 1 $$
$$ v'(t) = e^{-int} \implies v(t) = \frac{e^{-int}}{-in} $$
$$ c_n = \frac{1}{2\pi} \left[ t \frac{e^{-int}}{-in} \right]_0^{2\pi} - \frac{1}{2\pi} \int_0^{2\pi} \frac{e^{-int}}{-in} dt $$
$$ c_n = \frac{1}{2\pi} \left( \frac{2\pi}{-in} - 0 \right) - 0 = \frac{i}{n} $$
Pour $n = 0$ :
$$ c_0 = \frac{1}{2\pi} \int_0^{2\pi} t dt = \frac{1}{2\pi} \left[ \frac{t^2}{2} \right]_0^{2\pi} = \pi $$
L'identité de Parseval affirme que $\|f\|^2 = \sum_{n=-\infty}^\infty |c_n|^2$.
Calculons d'abord $\|f\|^2$ directement :
$$ \|f\|^2 = \frac{1}{2\pi} \int_0^{2\pi} t^2 dt = \frac{1}{2\pi} \left[ \frac{t^3}{3} \right]_0^{2\pi} = \frac{4\pi^2}{3} $$
La somme des modules au carré des coefficients de Fourier est :
$$ |c_0|^2 + \sum_{n \neq 0} |c_n|^2 = \pi^2 + \sum_{n \neq 0} \frac{1}{n^2} = \pi^2 + 2 \sum_{n=1}^\infty \frac{1}{n^2} $$
En égalant les deux expressions selon Parseval :
$$ \frac{4\pi^2}{3} = \pi^2 + 2 \sum_{n=1}^\infty \frac{1}{n^2} \implies \frac{\pi^2}{3} = 2 \sum_{n=1}^\infty \frac{1}{n^2} \implies \sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6} $$
C'est une méthode magistrale pour retrouver la solution au problème de Bâle.

## Démonstrations

### Démonstration : Existence d'une base dans un espace séparable

Un espace de Hilbert $H$ est dit **séparable** s'il contient une partie dénombrable dense. Nous allons démontrer par construction (constructivisme) qu'un tel espace admet toujours une base hilbertienne.

1. **Choix d'une famille génératrice dénombrable :**
   Puisque $H$ est séparable, il existe une suite de vecteurs $(x_n)_{n \in \mathbb{N}}$ dense dans $H$. L'adhérence de cette suite est donc $H$.
2. **Élimination des dépendances linéaires (Extraction d'une base algébrique) :**
   On retire séquentiellement les $x_n$ qui sont combinaisons linéaires des vecteurs précédents. Formellement, on construit une sous-suite $(v_k)$ telle que pour tout $N$, la famille $(v_0, v_1, \dots, v_N)$ soit libre, et $\text{vect}(\{v_k \mid k \in \mathbb{N}\}) = \text{vect}(\{x_n \mid n \in \mathbb{N}\})$.
3. **Algorithme d'orthonormalisation de Gram-Schmidt :**
   On construit la famille $(e_n)$ par récurrence sur $n$ :
   - Pour l'initialisation : $e_0 = \frac{v_0}{\|v_0\|}$.
   - Hérédité : Supposons $e_0, \dots, e_n$ construits, formant une famille orthonormée telle que $\text{vect}(e_0, \dots, e_n) = \text{vect}(v_0, \dots, v_n)$.
   On pose d'abord le vecteur résiduel (la projection orthogonale) :
   $$ u_{n+1} = v_{n+1} - \sum_{k=0}^n \langle v_{n+1}, e_k \rangle e_k $$
   Puisque $(v_k)$ est libre, $v_{n+1} \notin \text{vect}(v_0, \dots, v_n) = \text{vect}(e_0, \dots, e_n)$, donc $u_{n+1} \neq 0$.
   On normalise ensuite ce vecteur :
   $$ e_{n+1} = \frac{u_{n+1}}{\|u_{n+1}\|} $$
4. **Propriétés de la construction :**
   - Par l'hypothèse de récurrence et la définition de $u_{n+1}$, pour tout $j \leq n$ :
     $$ \langle u_{n+1}, e_j \rangle = \langle v_{n+1}, e_j \rangle - \sum_{k=0}^n \langle v_{n+1}, e_k \rangle \langle e_k, e_j \rangle = \langle v_{n+1}, e_j \rangle - \langle v_{n+1}, e_j \rangle = 0 $$
   - Chaque $e_n$ est donc orthogonal à tous les précédents et est de norme unitaire par construction.
   - De plus, à chaque étape, l'espace vectoriel engendré reste inchangé : $\text{vect}(e_0, \dots, e_n) = \text{vect}(v_0, \dots, v_n)$.
5. **Conclusion sur la densité :**
   L'espace vectoriel engendré par la famille orthonormée $(e_n)_{n \in \mathbb{N}}$ est exactement $\text{vect}(\{v_k\}) = \text{vect}(\{x_n\})$.
   Comme l'ensemble $\{x_n \mid n \in \mathbb{N}\}$ est dense dans $H$ par hypothèse de séparabilité, son espace engendré l'est aussi.
   L'adhérence de $\text{vect}(\{e_n \mid n \in \mathbb{N}\})$ est donc bien $H$.
   La famille $(e_n)_{n \in \mathbb{N}}$ est totale et orthonormée, c'est formellement une base hilbertienne de $H$.

\begin{center}
\begin{tikzpicture}[scale=1.5]
    % Initial vectors
    \draw[->, thick, gray, dashed] (0,0) -- (1.5, 0.5) node[right] {$v_0$};
    \draw[->, thick, gray, dashed] (0,0) -- (1, 1.5) node[above] {$v_1$};

    % Gram-Schmidt step 1
    \draw[->, thick, red] (0,0) -- (0.948, 0.316) node[below right] {$e_0 = \frac{v_0}{\|v_0\|}$};

    % Projection of v_1 on e_0
    \draw[dashed, blue] (1, 1.5) -- (1.34, 0.45);
    \draw[->, thick, blue] (0,0) -- (1.34, 0.45) node[below, midway] {$\langle v_1, e_0 \rangle e_0$};

    % Residual u_1
    \draw[->, thick, orange] (1.34, 0.45) -- (1, 1.5) node[midway, right] {$u_1$};
    \draw[->, thick, orange] (0,0) -- (-0.34, 1.05) node[left] {$u_1$};

    % Final orthonormal basis
    \draw[->, thick, red] (0,0) -- (-0.306, 0.945) node[left] {$e_1 = \frac{u_1}{\|u_1\|}$};

    % Right angle
    \draw (0.1, 0.033) -- (0.067, 0.133) -- (-0.033, 0.1);
\end{tikzpicture}
\end{center}

**Exemple concret 5 : Gram-Schmidt explicite sur $\mathbb{R}^3$**
Soit $v_0 = (1, 1, 0)$, $v_1 = (1, 0, 1)$, $v_2 = (0, 1, 1)$.
Étape 1 : $e_0 = \frac{v_0}{\|v_0\|} = \frac{1}{\sqrt{2}}(1, 1, 0)$.
Étape 2 : Projection de $v_1$ sur $e_0$ : $\langle v_1, e_0 \rangle e_0 = (\frac{1}{\sqrt{2}} \times 1) \frac{1}{\sqrt{2}}(1, 1, 0) = (\frac{1}{2}, \frac{1}{2}, 0)$.
$u_1 = v_1 - \langle v_1, e_0 \rangle e_0 = (1, 0, 1) - (\frac{1}{2}, \frac{1}{2}, 0) = (\frac{1}{2}, -\frac{1}{2}, 1)$.
$\|u_1\| = \sqrt{\frac{1}{4} + \frac{1}{4} + 1} = \sqrt{\frac{3}{2}}$.
$e_1 = \sqrt{\frac{2}{3}}(\frac{1}{2}, -\frac{1}{2}, 1) = \frac{1}{\sqrt{6}}(1, -1, 2)$.
Étape 3 : Projection de $v_2$ sur $e_0$ et $e_1$.
$\langle v_2, e_0 \rangle = \frac{1}{\sqrt{2}} \times 1 = \frac{1}{\sqrt{2}}$.
$\langle v_2, e_1 \rangle = \frac{1}{\sqrt{6}} (-1 + 2) = \frac{1}{\sqrt{6}}$.
$u_2 = v_2 - \langle v_2, e_0 \rangle e_0 - \langle v_2, e_1 \rangle e_1 = (0, 1, 1) - (\frac{1}{2}, \frac{1}{2}, 0) - (\frac{1}{6}, -\frac{1}{6}, \frac{2}{6}) = (-\frac{2}{3}, \frac{2}{3}, \frac{2}{3})$.
$\|u_2\| = \sqrt{\frac{4}{9} + \frac{4}{9} + \frac{4}{9}} = \frac{2}{\sqrt{3}}$.
$e_2 = \frac{\sqrt{3}}{2}(-\frac{2}{3}, \frac{2}{3}, \frac{2}{3}) = \frac{1}{\sqrt{3}}(-1, 1, 1)$.
La famille $(e_0, e_1, e_2)$ est la base hilbertienne orthonormée issue de $(v_0, v_1, v_2)$.

## Isomorphisme Fondamental avec $\ell^2$

> **Théorème de Riesz-Fischer généralisé :**
> Tout espace de Hilbert $H$ séparable de dimension infinie est isométrique et isomorphe à l'espace $\ell^2(\mathbb{N})$ des suites de carré sommable.

**Démonstration :**
Soit $(e_n)_{n \in \mathbb{N}}$ une base hilbertienne de $H$.
On définit l'opérateur linéaire $\Phi : H \to \ell^2(\mathbb{N})$ par la relation $\Phi(x) = (\langle x, e_n \rangle)_{n \in \mathbb{N}}$.
Par l'identité de Parseval, pour tout $x \in H$, la suite $\Phi(x)$ est de carré sommable et :
$$ \|\Phi(x)\|_{\ell^2}^2 = \sum_{n=0}^\infty |\langle x, e_n \rangle|^2 = \|x\|_H^2 $$
$\Phi$ est donc une isométrie linéaire, ce qui garantit son injectivité.
Pour démontrer la surjectivité, soit $c = (c_n)_{n \in \mathbb{N}} \in \ell^2(\mathbb{N})$.
La série $\sum c_n e_n$ satisfait le critère de Cauchy dans $H$ car pour $M > N$ :
$$ \left\| \sum_{n=N}^M c_n e_n \right\|_H^2 = \sum_{n=N}^M |c_n|^2 $$
qui tend vers 0 puisque la série $\sum |c_n|^2$ converge. L'espace $H$ étant complet, la série converge vers une limite $x \in H$.
Par la continuité du produit scalaire, $\langle x, e_k \rangle = c_k$ pour tout $k$. Donc $\Phi(x) = c$, et l'opérateur est bien surjectif.
Il s'agit donc d'un isomorphisme isométrique de Hilbert.

**Exemple concret 6 : Mapping isométrique explicite**
Dans $H = L^2([-1, 1])$, la fonction polynôme $P(x) = x$ se développe dans la base des polynômes de Legendre normalisés.
Nous avons $e_0(x) = \frac{1}{\sqrt{2}}$ et $e_1(x) = \sqrt{\frac{3}{2}} x$.
$\langle P, e_0 \rangle = \int_{-1}^1 x \frac{1}{\sqrt{2}} dx = 0$.
$\langle P, e_1 \rangle = \int_{-1}^1 x \sqrt{\frac{3}{2}} x dx = \sqrt{\frac{3}{2}} \frac{2}{3} = \sqrt{\frac{2}{3}}$.
Pour $n \geq 2$, $\langle P, e_n \rangle = 0$ par orthogonalité des polynômes de Legendre de degré distincts.
L'image de $P$ dans $\ell^2(\mathbb{N})$ par l'isomorphisme de Riesz-Fischer est la suite $c = (0, \sqrt{\frac{2}{3}}, 0, 0, \dots)$.
On vérifie la conservation de la norme :
$\|P\|^2 = \int_{-1}^1 x^2 dx = \frac{2}{3}$.
$\|c\|_{\ell^2}^2 = 0^2 + (\sqrt{\frac{2}{3}})^2 + 0^2 + \dots = \frac{2}{3}$.
L'isométrie est parfaitement vérifiée numériquement.

## Application en Intelligence Artificielle et Science des Données

L'application de la théorie des bases hilbertiennes est omniprésente dans les algorithmes de représentation mathématique avancés.

- **Analyse en Composantes Principales (PCA) de dimension infinie :** Pour des données continues comme des séries temporelles (Functional Data Analysis), on cherche une base hilbertienne propre de l'opérateur de covariance. C'est la **Décomposition de Karhunen-Loève**, qui exprime chaque signal comme une somme pondérée d'une base orthogonale adaptative optimale pour compresser l'information.
- **Transformations en Ondelettes (Wavelets) :** Contrairement aux bases de Fourier (sinus et cosinus) qui ont un support global (elles "vivent" de $-\infty$ à $+\infty$), les ondelettes forment des bases hilbertiennes de $L^2(\mathbb{R})$ avec un support compact (elles sont localisées spatialement). Cela permet de représenter finement les discontinuités des images dans les réseaux convolutifs et les algorithmes de compression (JPEG 2000).
- **Geometric Deep Learning :** Sur les graphes complexes, il n'existe pas de translation naturelle. On utilise alors la base hilbertienne formée par les vecteurs propres de la matrice Laplacienne normalisée du graphe. Exprimer les données du graphe dans cette base permet de définir des convolutions spectrales pour les *Graph Neural Networks* (GNN).
