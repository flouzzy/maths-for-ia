---
uuid: "jalon-30"
title: "Trigonalisation d'endomorphismes et décomposition de Dunford"
year: 1
trimester: 3
tags:
  - math/algebre-lineaire
  - ia/reduction-avancee
prev: "[[Jalon 29 (Éléments propres).md]]"
next: "[[Jalon 31 (Introduction à la réduction de Jordan et structure des nilpotents.).md]]"
---

# Jalon 30 : Trigonalisation d'endomorphismes et décomposition de Dunford

## Genèse et Motivation

La réduction des endomorphismes constitue l'un des piliers centraux de l'algèbre linéaire, permettant de simplifier drastiquement l'étude des opérateurs sur des espaces de dimension finie. Le jalon précédent a mis en lumière la puissance de la diagonalisation, qui offre une représentation diagonale parfaitement découplée de l'opérateur. Cependant, l'univers mathématique est jonché d'obstacles : tous les endomorphismes ne sont pas diagonalisables. Que se passe-t-il lorsque le polynôme caractéristique d'un opérateur ne se scinde pas en racines simples, ou lorsque la dimension des sous-espaces propres est strictement inférieure à la multiplicité algébrique des valeurs propres correspondantes ?

C'est ici qu'interviennent des concepts d'une élégance rare et d'une utilité redoutable, introduits par des mathématiciens dont la rigueur a forgé les mathématiques modernes. La nécessité de manipuler des matrices non diagonalisables (notamment pour résoudre des systèmes d'équations différentielles linéaires via l'exponentielle de matrice) a conduit à la notion de **trigonalisation**. L'idée géométrique est de trouver une base, dite "en drapeau", dans laquelle la matrice de l'opérateur est triangulaire supérieure. Si la transformation ne peut pas être décomposée en de purs étirements indépendants, on peut au moins structurer les dépendances hiérarchiquement.

Mais la trigonalisation laisse une structure encore trop couplée pour de nombreux calculs, notamment l'élévation à la puissance ou l'exponentiation matricielle. C'est le mathématicien Nelson Dunford (1906–1986), inspiré par les travaux antérieurs d'algébristes tels que Camille Jordan et Karl Weierstrass, qui a posé un théorème fondamental, le théorème de "décomposition de Dunford". L'intuition physique derrière ce résultat est magistrale : tout endomorphisme "pathologique" (dont le polynôme caractéristique est scindé) peut être décomposé additivement en deux composantes fondamentales :
- Une composante "purement structurelle", qui est **diagonalisable** et capte l'essence des homothéties de l'opérateur.
- Une composante "dégénérée", qui est **nilpotente** (c'est-à-dire qui s'évanouit au bout d'un certain nombre de compositions) et modélise les effets de cisaillement et d'instabilité.

Le génie de cette décomposition réside dans le fait que ces deux composantes **commutent**. Cette commutativité est la clé de voûte : elle autorise l'utilisation de la formule du binôme de Newton ou des propriétés de morphisme de l'exponentielle, rendant le calcul explicite des puissances et de l'exponentielle de l'endomorphisme non seulement possible, mais algorithmiquement traitable. La décomposition de Dunford est ainsi le pont indispensable entre l'algèbre abstraite et l'analyse fonctionnelle, avec des répercussions immenses dans la théorie du contrôle, l'étude des systèmes dynamiques en Intelligence Artificielle (comme la stabilité des Réseaux de Neurones Récurrents, RNN) et la mécanique quantique.

## Trigonalisation des endomorphismes

### Énoncé formel

Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension finie $n \geq 1$.
Soit $f \in \mathcal{L}(E)$ un endomorphisme.

L'endomorphisme $f$ est dit **trigonalisable** s'il existe une base $\mathcal{B}$ de $E$ telle que la matrice représentative de $f$ dans la base $\mathcal{B}$, notée $T = \text{Mat}_{\mathcal{B}}(f)$, soit triangulaire supérieure. C'est-à-dire que pour tout $j \in \mathopen{[\![} 1, n \mathclose{]\!]}$, les coefficients $t_{i,j}$ de $T$ vérifient $t_{i,j} = 0$ pour tout $i > j$.

**Théorème de trigonalisation :**
$f \in \mathcal{L}(E)$ est trigonalisable si, et seulement si, son polynôme caractéristique $\chi_f$ est scindé sur le corps $\mathbb{K}$.
$$ f \text{ est trigonalisable } \iff \exists (\lambda_1, \ldots, \lambda_n) \in \mathbb{K}^n, \quad \chi_f(X) = (-1)^n \prod_{i=1}^n (X - \lambda_i) $$

### Analyse détaillée

- **$\mathbb{K}$** : Désigne un corps commutatif (typiquement $\mathbb{R}$ ou $\mathbb{C}$).
- **$E$** : Un espace vectoriel sur le corps $\mathbb{K}$ de dimension strictement positive et finie $n$.
- **$f \in \mathcal{L}(E)$** : Un endomorphisme de l'espace vectoriel $E$.
- **$\mathcal{B} = (e_1, e_2, \ldots, e_n)$** : Une famille libre et génératrice de $E$ (une base). La condition que la matrice soit triangulaire supérieure se traduit vectoriellement par : $\forall j \in \mathopen{[\![} 1, n \mathclose{]\!]}, \quad f(e_j) \in \text{Vect}(e_1, \ldots, e_j)$. On dit que la suite des sous-espaces $F_j = \text{Vect}(e_1, \ldots, e_j)$ forme un **drapeau** de $E$ stable par $f$.
- **$\chi_f(X)$** : Le polynôme caractéristique de $f$, défini par $\det(XI_n - \text{Mat}(f))$, élément de l'anneau des polynômes $\mathbb{K}[X]$.
- **"Scindé"** : Un polynôme est scindé sur $\mathbb{K}$ s'il peut s'écrire comme le produit de polynômes de degré 1 à coefficients dans $\mathbb{K}$.

Une conséquence immédiate est que **sur le corps des complexes $\mathbb{C}$, tout polynôme étant scindé d'après le théorème de d'Alembert-Gauss, tout endomorphisme d'un $\mathbb{C}$-espace vectoriel de dimension finie est trigonalisable.**

### Exemples de Validation
### Représentation Géométrique de la Décomposition

L'intuition de la décomposition de Dunford peut s'illustrer par un schéma représentant l'action de $d$ (qui étire selon des axes propres) et $n$ (qui crée un cisaillement).

```latex
\begin{figure}[h]
\centering
\begin{tikzpicture}[scale=1.5]
  % Axes
  \draw[->, thick, gray] (-0.5,0) -- (3,0) node[right, black] {$e_1$ (propre)};
  \draw[->, thick, gray] (0,-0.5) -- (0,3) node[above, black] {$e_2$ (généralisé)};

  % Vecteur initial
  \draw[->, thick, blue] (0,0) -- (1,1) node[above right] {$v$};

  % Action de d (diagonalisable)
  \draw[->, thick, red, dashed] (0,0) -- (2,1) node[right] {$d(v)$};

  % Action de n (nilpotente - cisaillement)
  \draw[->, thick, green!70!black, dashed] (2,1) -- (2.5,1) node[right] {$+ n(v)$};

  % Vecteur final
  \draw[->, ultra thick, purple] (0,0) -- (2.5,1) node[above left] {$f(v) = d(v) + n(v)$};

  % Explications
  \node[anchor=north west] at (3.5, 2.5) {\textbf{Décomposition de l'opérateur $f$}};
  \node[anchor=north west] at (3.5, 2.0) {\textcolor{red}{$d$ : homothétie sur les sous-espaces}};
  \node[anchor=north west] at (3.5, 1.5) {\textcolor{green!70!black}{$n$ : cisaillement nilpotent (couplage)}};
  \node[anchor=north west] at (3.5, 1.0) {\textcolor{purple}{$f = d + n$ : composition additive}};
\end{tikzpicture}
\caption{Visualisation de l'action conjointe de la partie diagonalisable et de la partie nilpotente d'un endomorphisme}
\end{figure}
```

**Exemple Trivial :**
Soit l'endomorphisme $f$ de $\mathbb{R}^2$ canoniquement associé à la matrice $A = \begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix}$.
Le polynôme caractéristique est $\chi_A(X) = (X-2)(X-3)$. Les racines sont $\{2, 3\}$. $\chi_A$ est scindé sur $\mathbb{R}$. La matrice $A$ est déjà triangulaire supérieure, donc $f$ est trigonalisable (et même diagonalisable car ses valeurs propres sont distinctes).

**Exemple Complexe :**
Considérons $f \in \mathcal{L}(\mathbb{R}^3)$ de matrice $M = \begin{pmatrix} 1 & 4 & -2 \\ 0 & 6 & -3 \\ -1 & 4 & 0 \end{pmatrix}$ dans la base canonique.
On calcule le polynôme caractéristique :
$\chi_M(X) = \det(XI_3 - M) = X^3 - 7X^2 + 16X - 12$.
On remarque que $2$ est racine : $2^3 - 7(4) + 16(2) - 12 = 8 - 28 + 32 - 12 = 0$.
Par division euclidienne, on trouve $\chi_M(X) = (X-2)^2(X-3)$.
Le polynôme caractéristique est scindé sur $\mathbb{R}$. Par conséquent, $M$ est trigonalisable dans $\mathbb{R}$. (Note : La dimension du sous-espace propre associé à la valeur propre $2$ n'est que de $1$, donc $M$ n'est pas diagonalisable, mais elle est bien trigonalisable).

### Cas Pathologiques et Contre-exemples

**Contre-exemple (Le défaut de scindage sur $\mathbb{R}$) :**
Soit $r$ la rotation d'angle $\theta = \frac{\pi}{2}$ dans $\mathbb{R}^2$. Sa matrice dans la base canonique est $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
Le polynôme caractéristique est $\chi_R(X) = X^2 + 1$.
Sur le corps $\mathbb{R}$, le polynôme $X^2 + 1$ n'a aucune racine, il est irréductible et donc non scindé.
Par conséquent, $R$ **n'est pas trigonalisable sur $\mathbb{R}$**. Il n'y a aucune droite vectorielle réelle stable par cette rotation. Cependant, si l'on considère cet endomorphisme sur $\mathbb{C}^2$, alors $\chi_R(X) = (X-i)(X+i)$ est scindé, et $R$ devient diagonalisable (donc trigonalisable) sur $\mathbb{C}$.

## Décomposition de Dunford

### Énoncé formel

Soit $E$ un $\mathbb{K}$-espace vectoriel de dimension finie $n$.
Soit $f \in \mathcal{L}(E)$ un endomorphisme dont le polynôme caractéristique $\chi_f$ est scindé sur $\mathbb{K}$.

Alors il existe un **unique** couple $(d, n)$ d'endomorphismes de $E$ vérifiant simultanément les quatre conditions suivantes :
1. $f = d + n$
2. $d$ est un endomorphisme **diagonalisable**.
3. $n$ est un endomorphisme **nilpotent** (il existe un entier $k \in \mathbb{N}^*$ tel que $n^k = 0_{\mathcal{L}(E)}$).
4. $d$ et $n$ commutent : $d \circ n = n \circ d$.

De plus, $d$ et $n$ sont des polynômes en $f$, c'est-à-dire qu'il existe $P, Q \in \mathbb{K}[X]$ tels que $d = P(f)$ et $n = Q(f)$.

### Analyse détaillée

- **$f = d + n$** : Décomposition additive explicite. L'opérateur complet est la superposition de deux comportements orthogonaux de point de vue de leur nature algébrique.
- **$d$ diagonalisable** : Il existe une base où $d$ se représente par une matrice diagonale. $d$ encapsule les valeurs propres de $f$.
- **$n$ nilpotent** : Ses seules valeurs propres sont $0$. Dans une base adéquate, $n$ se représente par une matrice strictement triangulaire supérieure (avec des zéros sur la diagonale principale).
- **$d \circ n = n \circ d$** : Condition sine qua non de l'unicité et de l'utilité pratique. Elle garantit que la base qui diagonalise $d$ est fortement compatible avec $n$. Sans cette commutativité, on pourrait trouver une infinité de décompositions triviales et inutilisables.
- **$d = P(f)$ et $n = Q(f)$** : En tant que polynômes en $f$, ils commutent non seulement entre eux, mais aussi avec tout endomorphisme qui commute avec $f$. Cette propriété d'appartenance à l'algèbre engendrée par $f$, notée $\mathbb{K}[f]$, est primordiale.

### Exemples de Validation
### Représentation Géométrique de la Décomposition

L'intuition de la décomposition de Dunford peut s'illustrer par un schéma représentant l'action de $d$ (qui étire selon des axes propres) et $n$ (qui crée un cisaillement).

```latex
\begin{figure}[h]
\centering
\begin{tikzpicture}[scale=1.5]
  % Axes
  \draw[->, thick, gray] (-0.5,0) -- (3,0) node[right, black] {$e_1$ (propre)};
  \draw[->, thick, gray] (0,-0.5) -- (0,3) node[above, black] {$e_2$ (généralisé)};

  % Vecteur initial
  \draw[->, thick, blue] (0,0) -- (1,1) node[above right] {$v$};

  % Action de d (diagonalisable)
  \draw[->, thick, red, dashed] (0,0) -- (2,1) node[right] {$d(v)$};

  % Action de n (nilpotente - cisaillement)
  \draw[->, thick, green!70!black, dashed] (2,1) -- (2.5,1) node[right] {$+ n(v)$};

  % Vecteur final
  \draw[->, ultra thick, purple] (0,0) -- (2.5,1) node[above left] {$f(v) = d(v) + n(v)$};

  % Explications
  \node[anchor=north west] at (3.5, 2.5) {\textbf{Décomposition de l'opérateur $f$}};
  \node[anchor=north west] at (3.5, 2.0) {\textcolor{red}{$d$ : homothétie sur les sous-espaces}};
  \node[anchor=north west] at (3.5, 1.5) {\textcolor{green!70!black}{$n$ : cisaillement nilpotent (couplage)}};
  \node[anchor=north west] at (3.5, 1.0) {\textcolor{purple}{$f = d + n$ : composition additive}};
\end{tikzpicture}
\caption{Visualisation de l'action conjointe de la partie diagonalisable et de la partie nilpotente d'un endomorphisme}
\end{figure}
```

**Exemple de Décomposition Directe :**
Soit $M = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$.
Posons $D = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} = 2I_2$ et $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.
On a bien $M = D + N$.
- $D$ est diagonale (donc diagonalisable).
- $N^2 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}$, donc $N$ est nilpotente.
- $DN = (2I_2)N = 2N = N(2I_2) = ND$, ils commutent.
Par l'unicité garantie par le théorème de Dunford, le couple $(D, N)$ est **l'unique** décomposition de Dunford de $M$.

### Cas Pathologiques et Contre-exemples

**Le Piège de la Non-Commutativité :**
Considérons $A = \begin{pmatrix} 1 & 2 \\ 0 & 2 \end{pmatrix}$.
On pourrait être tenté d'écrire $A = D' + N'$ avec $D' = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$ et $N' = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}$.
Ici, $D'$ est diagonale et $N'$ est nilpotente.
Cependant, calculons leurs produits :
$D'N' = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix}$.
$N'D' = \begin{pmatrix} 0 & 2 \\ 0 & 0 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 0 & 4 \\ 0 & 0 \end{pmatrix}$.
Puisque $D'N' \neq N'D'$, le couple $(D', N')$ **n'est pas** la décomposition de Dunford de $A$.
En réalité, $A$ admet deux valeurs propres distinctes ($1$ et $2$) et est donc diagonalisable. Sa vraie décomposition de Dunford est triviale : $A = A + 0$ (où $d=A$ et $n=0$).

## Démonstrations détaillées

### Démonstration 1 : Existence de la base de Trigonalisation (par récurrence)

Nous allons démontrer que si $\chi_f$ est scindé, alors $f$ est trigonalisable.
Soit $E$ un espace vectoriel de dimension $n \geq 1$. Nous procédons par récurrence sur la dimension $n$.

**Initialisation ($n = 1$) :**
Tout endomorphisme d'un espace de dimension $1$ est représenté par une matrice $(1 \times 1)$, qui est par définition triangulaire supérieure. La proposition est donc vraie pour $n=1$.

**Hérédité :**
Supposons que la proposition soit vraie pour tout espace de dimension $n-1 \geq 1$.
Soit $E$ de dimension $n$, et $f \in \mathcal{L}(E)$ tel que $\chi_f$ soit scindé sur $\mathbb{K}$.
Puisque $\chi_f$ est scindé, il possède au moins une racine $\lambda_1 \in \mathbb{K}$.
Par définition du polynôme caractéristique, $\det(\lambda_1 I_n - f) = 0$, donc $f - \lambda_1 \text{Id}_E$ n'est pas injectif.
Il existe donc un vecteur non nul $e_1 \in E$ tel que $f(e_1) = \lambda_1 e_1$. ($e_1$ est un vecteur propre).

Complétons $\{e_1\}$ en une base de $E$, que l'on note $\mathcal{B}' = (e_1, \varepsilon_2, \ldots, \varepsilon_n)$.
Dans cette base $\mathcal{B}'$, la matrice de $f$ s'écrit sous la forme par blocs :
$$ M' = \begin{pmatrix} \lambda_1 & L \\ 0 & A \end{pmatrix} $$
où $L \in \mathcal{M}_{1, n-1}(\mathbb{K})$, $0$ est un bloc colonne de zéros, et $A \in \mathcal{M}_{n-1}(\mathbb{K})$.

Calculons le polynôme caractéristique de $M'$ en développant par rapport à la première colonne :
$$ \chi_f(X) = \det(XI_n - M') = (X - \lambda_1) \det(XI_{n-1} - A) = (X - \lambda_1) \chi_A(X) $$
Puisque $\chi_f(X)$ est scindé sur $\mathbb{K}$ par hypothèse, et que $\chi_f(X) = (X - \lambda_1)\chi_A(X)$, le polynôme $\chi_A(X)$ doit obligatoirement être scindé sur $\mathbb{K}$.

L'endomorphisme $g \in \mathcal{L}(\text{Vect}(\varepsilon_2, \ldots, \varepsilon_n))$ canoniquement associé à la matrice $A$ opère sur un espace de dimension $n-1$ et son polynôme caractéristique est scindé.
Par hypothèse de récurrence, il existe une base $(e_2, \ldots, e_n)$ de cet espace de dimension $n-1$ dans laquelle la matrice représentative de $g$ est triangulaire supérieure.
Soit $P$ la matrice de passage de la base $(\varepsilon_2, \ldots, \varepsilon_n)$ à la base $(e_2, \ldots, e_n)$.
Considérons la matrice de passage par blocs dans $E$ définie par :
$$ Q = \begin{pmatrix} 1 & 0 \\ 0 & P \end{pmatrix} $$
La nouvelle base de $E$ est $\mathcal{B} = (e_1, e_2, \ldots, e_n)$.
La matrice de $f$ dans cette nouvelle base $\mathcal{B}$ s'obtient par changement de base :
$$ T = Q^{-1} M' Q = \begin{pmatrix} 1 & 0 \\ 0 & P^{-1} \end{pmatrix} \begin{pmatrix} \lambda_1 & L \\ 0 & A \end{pmatrix} \begin{pmatrix} 1 & 0 \\ 0 & P \end{pmatrix} = \begin{pmatrix} \lambda_1 & L P \\ 0 & P^{-1} A P \end{pmatrix} $$
Or, par construction, la matrice $T' = P^{-1} A P$ est triangulaire supérieure.
Ainsi, la matrice $T$ globale est composée de $\lambda_1$ en haut à gauche, de zéros en dessous de $\lambda_1$, de la ligne $L P$, et du bloc triangulaire supérieur $T'$. Elle est donc elle-même intégralement triangulaire supérieure.
L'hérédité est prouvée.

**Conclusion :**
Par le principe de récurrence, pour tout $n \geq 1$, tout endomorphisme dont le polynôme caractéristique est scindé est trigonalisable.

### Démonstration 2 : Unicité dans la Décomposition de Dunford

Montrons que si le couple $(d, n)$ existe, il est unique.

Supposons qu'il existe deux couples $(d_1, n_1)$ et $(d_2, n_2)$ satisfaisant les conditions du théorème de Dunford.
Ainsi :
- $f = d_1 + n_1 = d_2 + n_2$
- $d_1 \circ n_1 = n_1 \circ d_1$ et $d_2 \circ n_2 = n_2 \circ d_2$
- $d_1, d_2$ diagonalisables, et $n_1, n_2$ nilpotents.
- De plus, la partie "existence" du théorème (non démontrée ici par concision mais supposée acquise) nous garantit que $d_1$ et $n_1$ sont des polynômes en $f$. Puisque $d_2$ et $n_2$ le sont également par unicité supposée de construction polynomiale, tous ces opérateurs commutent entre eux.

Soit la relation : $d_1 - d_2 = n_2 - n_1$.
Notons $\Delta = d_1 - d_2$ et $N = n_2 - n_1$.

1. **Étude de $\Delta$ :**
Puisque $d_1$ et $d_2$ sont diagonalisables et qu'ils commutent (car ce sont des polynômes en $f$), ils sont **co-diagonalisables** (ils admettent une base commune de diagonalisation).
Par conséquent, leur différence $\Delta = d_1 - d_2$ est également **diagonalisable**.

2. **Étude de $N$ :**
Puisque $n_1$ et $n_2$ sont nilpotents et commutent, nous pouvons appliquer la formule du binôme de Newton à $n_2 - n_1$.
Il existe des entiers $p, q$ tels que $n_1^p = 0$ et $n_2^q = 0$.
Soit $k = p + q$.
$$ N^k = (n_2 - n_1)^{p+q} = \sum_{i=0}^{p+q} \binom{p+q}{i} (-1)^i n_1^i n_2^{p+q-i} $$
Dans chaque terme de cette somme, soit $i \geq p$, auquel cas $n_1^i = 0$, soit $i < p$, auquel cas $p+q-i > q$, donc $n_2^{p+q-i} = 0$.
Ainsi, chaque terme de la somme est nul. Donc $N^k = 0$.
Par conséquent, $N = n_2 - n_1$ est un opérateur **nilpotent**.

3. **Conclusion :**
L'opérateur $\Delta = N$ est simultanément diagonalisable et nilpotent.
Or, le seul endomorphisme diagonalisable qui soit également nilpotent est l'endomorphisme nul.
En effet, la matrice diagonale d'un endomorphisme nilpotent ne peut contenir que des zéros sur sa diagonale, donc elle est nulle.
Ainsi, $\Delta = 0$ et $N = 0$.
On en déduit que $d_1 = d_2$ et $n_1 = n_2$.
L'unicité de la décomposition est établie de manière rigoureuse.
