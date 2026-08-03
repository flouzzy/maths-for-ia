---
uuid: "jalon-32"
title: "Preuve complète du théorème spectral pour les endomorphismes symétriques"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/optimisation-stochastique
prev: "[[Jalon 31 (Introduction à la réduction de Jordan et structure des nilpotents.).md]]"
next: "[[Jalon 33 (Formes quadratiques).md]]"
---

# Preuve complète du théorème spectral pour les endomorphismes symétriques

## Genèse et historique

L'algèbre linéaire classique, avec ses matrices et ses changements de base, permet de comprendre les transformations de l'espace. Cependant, lorsqu'on munit l'espace d'une structure euclidienne (un produit scalaire, permettant de mesurer des angles et des distances), on s'intéresse à des transformations qui "respectent" cette géométrie de manière particulière.
Le théorème spectral est sans doute le résultat le plus profond et le plus appliqué de l'algèbre linéaire en dimension finie. Historiquement, la genèse de ce concept provient de la mécanique céleste et de l'étude des axes principaux d'inertie des solides (Euler), ainsi que de l'étude des formes quadratiques et des surfaces du second degré (Cauchy). Cauchy, en 1829, a démontré que l'équation séculaire (le polynôme caractéristique) d'une matrice symétrique n'a que des racines réelles.

Pourquoi une telle importance ? En apprentissage automatique et en analyse de données (comme la PCA - Principal Component Analysis), on manipule des matrices de covariance qui sont intrinsèquement symétriques. Le théorème spectral garantit que l'on peut toujours trouver une base "parfaite", orthogonale, dans laquelle l'action de cette matrice se résume à de simples étirements sur des axes indépendants. Cela signifie qu'un problème complexe et couplé peut toujours être découplé en problèmes unidimensionnels complètement indépendants, pour peu que l'opérateur soit symétrique. C'est une simplification radicale de la réalité qui permet la compression de données et l'optimisation stochastique à grande échelle.

## Définitions et théorèmes

### Énoncé formel

Soit $E$ un espace vectoriel euclidien (donc de dimension finie sur le corps $\mathbb{R}$, muni d'un produit scalaire $\langle \cdot, \cdot \rangle$).
Un endomorphisme $u \in \mathcal{L}(E)$ est dit **symétrique** (ou auto-adjoint) si et seulement si :
$$\forall (x, y) \in E \times E, \quad \langle u(x), y \rangle = \langle x, u(y) \rangle$$

### Typage et variables

- $E$ : Un espace vectoriel sur le corps des réels $\mathbb{R}$, de dimension finie $n \in \mathbb{N}^*$.
- $\langle \cdot, \cdot \rangle$ : Une forme bilinéaire symétrique définie positive sur $E \times E$.
- $u \in \mathcal{L}(E)$ : Une application linéaire de $E$ dans lui-même.
- $x, y \in E$ : Deux vecteurs quelconques de l'espace $E$.

L'égalité $\langle u(x), y \rangle = \langle x, u(y) \rangle$ exprime que l'opérateur $u$ peut "traverser" le produit scalaire d'un argument à l'autre sans en altérer la valeur. En termes de matrices, dans une base orthonormée de $E$, la matrice $A$ de $u$ est symétrique, i.e., $A = A^\top$.

### Exemples immédiats

**Exemple trivial :** L'identité $\text{Id}_E$. Pour tout $x, y$, $\langle \text{Id}_E(x), y \rangle = \langle x, y \rangle = \langle x, \text{Id}_E(y) \rangle$. Son spectre est $\{1\}$ et n'importe quelle base orthonormée la diagonalise.

**Exemple complexe :** La projection orthogonale $p$ sur un sous-espace $F$. Soit $x = x_F + x_{F^\perp}$ et $y = y_F + y_{F^\perp}$.
$\langle p(x), y \rangle = \langle x_F, y_F + y_{F^\perp} \rangle = \langle x_F, y_F \rangle$.
D'autre part, $\langle x, p(y) \rangle = \langle x_F + x_{F^\perp}, y_F \rangle = \langle x_F, y_F \rangle$. L'égalité est vérifiée, $p$ est symétrique.

\begin{figure}[h!]
\centering
\begin{tikzpicture}[scale=1.5]
  % Axes
  \draw[->,thick] (-1,0) -- (3,0) node[right] {$x$};
  \draw[->,thick] (0,-1) -- (0,3) node[above] {$y$};

  % Sous-espace propre (axe des abscisses par exemple pour P)
  \draw[thick, blue] (-1,0) -- (2.5,0) node[above right] {$E_{\lambda=1} = F$};

  % Vecteur x
  \coordinate (X) at (1.5, 2);
  \draw[->, thick, red] (0,0) -- (X) node[above right] {$x$};

  % Projection orthogonale p(x)
  \coordinate (PX) at (1.5, 0);
  \draw[->, thick, violet] (0,0) -- (PX) node[below] {$p(x)$};

  % Ligne de projection
  \draw[dashed] (X) -- (PX);

  % Angle droit
  \draw (1.5, 0.2) -- (1.3, 0.2) -- (1.3, 0);

  % Composante orthogonale
  \draw[->, thick, orange] (0,0) -- (0, 2) node[left] {$x_{F^\perp}$};
  \draw[dashed] (X) -- (0,2);

\end{tikzpicture}
\caption{Projection orthogonale : un exemple fondamental d'endomorphisme symétrique. L'espace est somme directe orthogonale de $F$ et $F^\perp$.}
\end{figure}



### Cas pathologiques

- **Espace non euclidien :** Si la forme bilinéaire n'est pas définie positive (par exemple un espace de Minkowski), la notion d'adjoint et le théorème spectral standard s'effondrent.
- **Base non orthonormée :** Si l'on choisit une base quelconque (non orthonormée), un endomorphisme symétrique peut être représenté par une matrice qui *n'est pas* symétrique. C'est un piège classique !

## Démonstration du théorème spectral

### Énoncé du Théorème Spectral

Pour tout endomorphisme symétrique $u$ d'un espace vectoriel euclidien $E$ de dimension $n \ge 1$, il existe une base orthonormée de $E$ constituée de vecteurs propres de $u$. En corollaire, $u$ est diagonalisable.

### Lemme 1 : Stabilité de l'orthogonal

**Énoncé :** Soit $u$ un endomorphisme symétrique de $E$. Si un sous-espace vectoriel $F$ de $E$ est stable par $u$ (c'est-à-dire $u(F) \subset F$), alors son orthogonal $F^\perp$ est également stable par $u$.

**Démonstration :**
Soit $F$ un sous-espace vectoriel de $E$ tel que $u(F) \subset F$.
Soit $x \in F^\perp$. Montrons que $u(x) \in F^\perp$.
Pour montrer que $u(x) \in F^\perp$, il faut montrer que pour tout $y \in F$, $\langle u(x), y \rangle = 0$.
Soit $y \in F$. Comme $u$ est symétrique, on a la relation :
$$\langle u(x), y \rangle = \langle x, u(y) \rangle$$
Or, par hypothèse de stabilité, $F$ est stable par $u$. Donc, puisque $y \in F$, on a $u(y) \in F$.
Puisque $x \in F^\perp$, par définition de l'orthogonalité, son produit scalaire avec tout vecteur de $F$ est nul. Ainsi, comme $u(y) \in F$, on a :
$$\langle x, u(y) \rangle = 0$$
D'où l'on déduit immédiatement que $\langle u(x), y \rangle = 0$.
Ceci étant vrai pour tout $y \in F$, on conclut que $u(x) \in F^\perp$.
Donc $F^\perp$ est stable par $u$.

### Lemme 2 : Existence d'une valeur propre réelle

**Énoncé :** Tout endomorphisme symétrique en dimension finie $\ge 1$ admet au moins une valeur propre réelle.

**Démonstration :**
Soit $A$ la matrice de $u$ dans une base orthonormée $\mathcal{B}$. $A$ est une matrice réelle symétrique ($A = A^\top$).
On peut considérer $A$ comme une matrice à coefficients dans $\mathbb{C}$. D'après le théorème de d'Alembert-Gauss, le polynôme caractéristique $\chi_A(X)$ est scindé sur $\mathbb{C}$. Il admet donc au moins une racine complexe $\lambda \in \mathbb{C}$.
Soit $Z \in \mathbb{C}^n \setminus \{0\}$ un vecteur propre associé, de sorte que $AZ = \lambda Z$.
En passant à la conjugaison complexe, et puisque $A$ est à coefficients réels ($\overline{A} = A$), on obtient :
$A \overline{Z} = \overline{\lambda} \overline{Z}$
Transposons cette égalité (en se rappelant que $Z^\top$ est un vecteur ligne) :
$(A \overline{Z})^\top = (\overline{\lambda} \overline{Z})^\top \implies \overline{Z}^\top A^\top = \overline{\lambda} \overline{Z}^\top$
Puisque $A$ est symétrique, $A^\top = A$. On a donc :
$\overline{Z}^\top A = \overline{\lambda} \overline{Z}^\top$
Multiplions maintenant à droite par le vecteur colonne $Z$ :
$(\overline{Z}^\top A) Z = \overline{\lambda} \overline{Z}^\top Z$
Calculons différemment $\overline{Z}^\top (AZ)$ en utilisant la définition initiale $AZ = \lambda Z$ :
$\overline{Z}^\top (AZ) = \overline{Z}^\top (\lambda Z) = \lambda \overline{Z}^\top Z$
En identifiant les deux expressions de $\overline{Z}^\top A Z$, on obtient :
$\overline{\lambda} \overline{Z}^\top Z = \lambda \overline{Z}^\top Z$
Or, $\overline{Z}^\top Z = \sum_{i=1}^n \overline{z_i} z_i = \sum_{i=1}^n |z_i|^2 > 0$ car $Z$ est un vecteur non nul.
On peut donc diviser par $\overline{Z}^\top Z$, ce qui donne $\overline{\lambda} = \lambda$.
Ainsi, $\lambda \in \mathbb{R}$. La matrice $A$ admet une valeur propre réelle. Par équivalence, l'endomorphisme $u$ admet une valeur propre réelle.

### Démonstration Principale du Théorème Spectral

On procède par récurrence sur la dimension $n$ de l'espace euclidien $E$.

**Initialisation :**
Pour $n = 1$. L'espace $E$ est de dimension 1. Toute base $(e_1)$ de $E$ de norme 1 est une base orthonormée. L'endomorphisme $u$ s'écrit $u(e_1) = \lambda_1 e_1$, donc $e_1$ est un vecteur propre. Le théorème est trivialement vrai.

**Hérédité :**
Supposons le théorème vrai pour tout espace euclidien de dimension $n-1$.
Soit $E$ un espace euclidien de dimension $n \ge 2$, et $u \in \mathcal{L}(E)$ un endomorphisme symétrique.
D'après le Lemme 2, $u$ admet au moins une valeur propre réelle $\lambda_1$.
Soit $v_1$ un vecteur propre associé à cette valeur propre. On peut supposer $\|v_1\| = 1$ quitte à le diviser par sa norme.
Considérons le sous-espace $F = \text{Vect}(v_1)$. Ce sous-espace est de dimension 1.
Puisque $u(v_1) = \lambda_1 v_1 \in F$, le sous-espace $F$ est stable par $u$.
D'après le Lemme 1, le sous-espace orthogonal $F^\perp$ est également stable par $u$.
De plus, $E = F \oplus F^\perp$, donc la dimension de $F^\perp$ est $n - 1$.
Considérons la restriction de $u$ à $F^\perp$, notée $u_{|F^\perp}$.
Cette application $u_{|F^\perp}$ est un endomorphisme de l'espace euclidien $F^\perp$ (muni du produit scalaire induit).
Pour tout $x, y \in F^\perp$, on a $\langle u_{|F^\perp}(x), y \rangle = \langle u(x), y \rangle = \langle x, u(y) \rangle = \langle x, u_{|F^\perp}(y) \rangle$.
Donc $u_{|F^\perp}$ est un endomorphisme symétrique sur un espace euclidien de dimension $n-1$.
D'après l'hypothèse de récurrence, il existe une base orthonormée de $F^\perp$, notée $(e_2, e_3, \dots, e_n)$, constituée de vecteurs propres de $u_{|F^\perp}$ (donc de vecteurs propres de $u$).
Formons alors la famille $\mathcal{B} = (v_1, e_2, e_3, \dots, e_n)$.
Par construction :
1. Chaque vecteur est un vecteur propre de $u$.
2. $\|v_1\| = 1$ et $\|e_i\| = 1$ pour $i \ge 2$.
3. Les vecteurs $e_i$ sont deux à deux orthogonaux (hypothèse de récurrence).
4. Pour tout $i \ge 2$, $e_i \in F^\perp$, donc $e_i$ est orthogonal à $v_1 \in F$.
Ainsi, $\mathcal{B}$ est une base orthonormée de $E$ formée de vecteurs propres de $u$.

La propriété est démontrée au rang $n$.
Par le principe de récurrence, le théorème spectral est démontré pour tout entier $n \ge 1$.
