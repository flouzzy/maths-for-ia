# Exercice 6 : L'opérateur de différence finie sur les polynômes (Difficulté : ***)

## Énoncé du problème

Soit $n \in \mathbb{N}$ un entier naturel. On considère l'espace vectoriel réel $E = \mathbb{R}_n[X]$, l'ensemble des polynômes à coefficients réels de degré inférieur ou égal à $n$. La base canonique de $E$ est $B = (1, X, X^2, \dots, X^n)$.

On définit l'application $L: E \to E$ par :
$$L(P)(X) = P(X+1) - P(X)$$
pour tout polynôme $P \in E$.

1.  Démontrer que $L$ est une application linéaire.
2.  Déterminer le noyau $\mathrm{Ker}(L)$ de $L$. Donner une base de $\mathrm{Ker}(L)$ et sa dimension.
3.  Déterminer l'image $\mathrm{Im}(L)$ de $L$. Donner une base de $\mathrm{Im}(L)$ et sa dimension.
4.  Calculer le rang de $L$ et vérifier le théorème du rang.
5.  Déterminer la matrice $M_B(L)$ de $L$ dans la base canonique $B$ de $E$.

---

## Correction détaillée

### Question 1 : Démontrer que $L$ est une application linéaire.

Pour que $L$ soit linéaire, elle doit satisfaire deux propriétés :
a) $L(P+Q) = L(P) + L(Q)$ pour tous $P, Q \in E$.
b) $L(\lambda P) = \lambda L(P)$ pour tout $P \in E$ et tout scalaire $\lambda \in \mathbb{R}$.

Soient $P, Q \in E$ et $\lambda \in \mathbb{R}$.

a) Calculons $L(P+Q)(X)$:
$$L(P+Q)(X) = (P+Q)(X+1) - (P+Q)(X)$$
Par définition de l'addition de polynômes, $(P+Q)(X+1) = P(X+1) + Q(X+1)$ et $(P+Q)(X) = P(X) + Q(X)$.
Donc,
$$L(P+Q)(X) = (P(X+1) + Q(X+1)) - (P(X) + Q(X))$$
Regroupons les termes :
$$L(P+Q)(X) = (P(X+1) - P(X)) + (Q(X+1) - Q(X))$$
Par définition de $L$, ceci est égal à $L(P)(X) + L(Q)(X)$.
Ainsi, $L(P+Q) = L(P) + L(Q)$.

b) Calculons $L(\lambda P)(X)$:
$$L(\lambda P)(X) = (\lambda P)(X+1) - (\lambda P)(X)$$
Par définition de la multiplication d'un polynôme par un scalaire, $(\lambda P)(X+1) = \lambda P(X+1)$ et $(\lambda P)(X) = \lambda P(X)$.
Donc,
$$L(\lambda P)(X) = \lambda P(X+1) - \lambda P(X)$$
Mettons $\lambda$ en facteur :
$$L(\lambda P)(X) = \lambda (P(X+1) - P(X))$$
Par définition de $L$, ceci est égal à $\lambda L(P)(X)$.
Ainsi, $L(\lambda P) = \lambda L(P)$.

Les deux propriétés étant vérifiées, $L$ est bien une application linéaire.
De plus, si $P \in \mathbb{R}_n[X]$, alors $P(X+1)$ est également un polynôme de degré au plus $n$. La différence $P(X+1)-P(X)$ est donc un polynôme de degré au plus $n$. L'application $L$ est donc bien définie de $E$ vers $E$.

### Question 2 : Déterminer le noyau $\mathrm{Ker}(L)$.

Le noyau $\mathrm{Ker}(L)$ est l'ensemble des polynômes $P \in E$ tels que $L(P) = 0$.
$$P \in \mathrm{Ker}(L) \iff L(P)(X) = 0 \text{ pour tout } X \in \mathbb{R}$$
$$P(X+1) - P(X) = 0 \iff P(X+1) = P(X)$$
Un polynôme qui vérifie $P(X+1) = P(X)$ pour tout $X \in \mathbb{R}$ est un polynôme constant.
Pour le prouver, soit $P(X) = a_k X^k + a_{k-1} X^{k-1} + \dots + a_1 X + a_0$ un polynôme de degré $k \le n$, avec $a_k \neq 0$ si $k \ge 1$.
Alors $P(X+1) = a_k (X+1)^k + a_{k-1} (X+1)^{k-1} + \dots + a_1 (X+1) + a_0$.
Développons $(X+1)^k$ : $(X+1)^k = X^k + k X^{k-1} + \binom{k}{2} X^{k-2} + \dots + 1$.
$$P(X+1) = a_k (X^k + k X^{k-1} + \dots) + a_{k-1} (X^{k-1} + \dots) + \dots + a_0$$
$$P(X+1) - P(X) = a_k k X^{k-1} + (\text{termes de degré inférieur})$$
Si $k \ge 1$, alors le polynôme $P(X+1) - P(X)$ a pour degré $k-1$ et son coefficient dominant est $a_k k$.
Pour que $P(X+1) - P(X) = 0$, il faut que tous ses coefficients soient nuls. En particulier, $a_k k$ doit être nul.
Puisque $a_k \neq 0$ (par hypothèse $P$ est de degré $k$), il faut que $k=0$.
Si $k=0$, le polynôme $P(X)$ est de degré 0, c'est-à-dire une constante $P(X) = a_0$.
Dans ce cas, $L(a_0) = a_0 - a_0 = 0$.
Donc, les seuls polynômes dans $E$ qui appartiennent à $\mathrm{Ker}(L)$ sont les polynômes constants.
L'ensemble des polynômes constants dans $E$ est $\mathbb{R}_0[X]$.
Une base pour $\mathbb{R}_0[X]$ est le polynôme constant $1$.
Par conséquent, $\mathrm{Ker}(L) = \mathrm{Vect}(1)$.
La dimension de $\mathrm{Ker}(L)$ est $\mathrm{dim}(\mathrm{Ker}(L)) = 1$.

### Question 3 : Déterminer l'image $\mathrm{Im}(L)$.

L'image $\mathrm{Im}(L)$ est l'ensemble des polynômes $Q \in E$ tels que $Q = L(P)$ pour un certain $P \in E$.
D'après la question 2, si $P(X)$ est un polynôme de degré $k \ge 1$, alors $L(P)(X)$ est un polynôme de degré $k-1$.
Si $P(X)$ est un polynôme constant (de degré 0), $L(P)(X) = 0$.
Puisque $P \in \mathbb{R}_n[X]$, le degré maximal de $P$ est $n$.
Si $P$ est de degré $n$, $L(P)$ est de degré $n-1$.
Si $P$ est de degré $k < n$, $L(P)$ est de degré $k-1$ (si $k \ge 1$) ou 0 (si $k=0$).
Donc, tous les polynômes dans $\mathrm{Im}(L)$ ont un degré inférieur ou égal à $n-1$.
Cela signifie que $\mathrm{Im}(L) \subseteq \mathbb{R}_{n-1}[X]$.

Nous connaissons la dimension de l'espace de départ $E = \mathbb{R}_n[X]$, qui est $\mathrm{dim}(E) = n+1$.
Nous avons trouvé $\mathrm{dim}(\mathrm{Ker}(L)) = 1$.
D'après le théorème du rang (voir question 4), $\mathrm{dim}(\mathrm{Im}(L)) = \mathrm{dim}(E) - \mathrm{dim}(\mathrm{Ker}(L)) = (n+1) - 1 = n$.

Nous avons donc $\mathrm{Im}(L) \subseteq \mathbb{R}_{n-1}[X]$ et $\mathrm{dim}(\mathrm{Im}(L)) = n$.
Puisque $\mathrm{dim}(\mathbb{R}_{n-1}[X]) = n$, et que $\mathrm{Im}(L)$ est un sous-espace de $\mathbb{R}_{n-1}[X]$ de même dimension, nous pouvons conclure que $\mathrm{Im}(L) = \mathbb{R}_{n-1}[X]$.

Une base pour $\mathrm{Im}(L) = \mathbb{R}_{n-1}[X]$ est la base canonique $(1, X, X^2, \dots, X^{n-1})$.
La dimension de $\mathrm{Im}(L)$ est $n$.

### Question 4 : Calculer le rang de $L$ et vérifier le théorème du rang.

Le rang d'une application linéaire $L$, noté $\mathrm{rang}(L)$, est la dimension de son image $\mathrm{Im}(L)$.
D'après la question 3, $\mathrm{dim}(\mathrm{Im}(L)) = n$.
Donc, $\mathrm{rang}(L) = n$.

Le théorème du rang stipule que pour une application linéaire $L: E \to F$, où $E$ est un espace vectoriel de dimension finie, on a :
$$\mathrm{dim}(E) = \mathrm{dim}(\mathrm{Ker}(L)) + \mathrm{dim}(\mathrm{Im}(L))$$
Dans notre cas :
*   $\mathrm{dim}(E) = \mathrm{dim}(\mathbb{R}_n[X]) = n+1$.
*   $\mathrm{dim}(\mathrm{Ker}(L)) = 1$ (d'après la question 2).
*   $\mathrm{dim}(\mathrm{Im}(L)) = n$ (d'après la question 3).

Vérifions le théorème du rang :
$$(n+1) = 1 + n$$
L'égalité est bien vérifiée.

### Question 5 : Déterminer la matrice $M_B(L)$ de $L$ dans la base canonique $B$ de $E$.

La base canonique de $E = \mathbb{R}_n[X]$ est $B = (P_0, P_1, \dots, P_n)$ où $P_k(X) = X^k$.
Pour construire la matrice $M_B(L)$, nous devons calculer $L(P_k)$ pour chaque $k \in \{0, \dots, n\}$ et exprimer le résultat comme une combinaison linéaire des éléments de la base $B$. Le vecteur colonne $j$ de la matrice sera constitué des coefficients de $L(P_j)$.

1.  Pour $P_0(X) = 1$:
    $L(1)(X) = (1) - (1) = 0$.
    Donc, $L(1) = 0 \cdot 1 + 0 \cdot X + \dots + 0 \cdot X^n$. La première colonne de $M_B(L)$ est $(0, 0, \dots, 0)^T$.

2.  Pour $P_k(X) = X^k$, avec $k \ge 1$:
    $L(X^k)(X) = (X+1)^k - X^k$.
    Utilisons la formule du binôme de Newton : $(X+1)^k = \sum_{j=0}^k \binom{k}{j} X^j = \binom{k}{0} X^0 + \binom{k}{1} X^1 + \dots + \binom{k}{k-1} X^{k-1} + \binom{k}{k} X^k$.
    $L(X^k)(X) = \left( \sum_{j=0}^k \binom{k}{j} X^j \right) - X^k$.
    Comme $\binom{k}{k}=1$, le terme $X^k$ s'annule :
    $L(X^k)(X) = \sum_{j=0}^{k-1} \binom{k}{j} X^j = \binom{k}{0} + \binom{k}{1} X + \binom{k}{2} X^2 + \dots + \binom{k}{k-1} X^{k-1}$.
    Ce polynôme est de degré $k-1$.

Les colonnes de la matrice $M_B(L)$ sont les vecteurs de coordonnées de $L(X^j)$ dans la base $(1, X, \dots, X^n)$.
*   Colonne 0 (pour $X^0=1$): $(0, 0, \dots, 0)^T$.
*   Colonne 1 (pour $X^1=X$): $L(X) = \binom{1}{0} = 1$. Coordonnées: $(1, 0, \dots, 0)^T$.
*   Colonne 2 (pour $X^2$): $L(X^2) = \binom{2}{0} + \binom{2}{1} X = 1 + 2X$. Coordonnées: $(1, 2, 0, \dots, 0)^T$.
*   Colonne 3 (pour $X^3$): $L(X^3) = \binom{3}{0} + \binom{3}{1} X + \binom{3}{2} X^2 = 1 + 3X + 3X^2$. Coordonnées: $(1, 3, 3, 0, \dots, 0)^T$.
*   Généralement, pour la colonne $j$ (correspondant à $X^j$): les coefficients sont $\binom{j}{0}, \binom{j}{1}, \dots, \binom{j}{j-1}$, suivis de zéros.

La matrice $M_B(L)$ est de taille $(n+1) \times (n+1)$. Ses coefficients $(M_B(L))_{i,j}$ (où $i$ est l'indice de ligne et $j$ l'indice de colonne, tous deux allant de 0 à $n$) sont donnés par :
$$(M_B(L))_{i,j} = \begin{cases} \binom{j}{i} & \text{si } i < j \\ 0 & \text{si } i \ge j \end{cases}$$
(Notez que $\binom{j}{i}=0$ si $i>j$ ou $i<0$, donc la condition $i<j$ est suffisante).

Exemple pour $n=3$, $E = \mathbb{R}_3[X]$, base $(1, X, X^2, X^3)$:
$L(1) = 0$
$L(X) = 1$
$L(X^2) = 1 + 2X$
$L(X^3) = 1 + 3X + 3X^2$

La matrice $M_B(L)$ est :
$$
M_B(L) = \begin{pmatrix}
(M_B(L))_{0,0} & (M_B(L))_{0,1} & (M_B(L))_{0,2} & (M_B(L))_{0,3} \\
(M_B(L))_{1,0} & (M_B(L))_{1,1} & (M_B(L))_{1,2} & (M_B(L))_{1,3} \\
(M_B(L))_{2,0} & (M_B(L))_{2,1} & (M_B(L))_{2,2} & (M_B(L))_{2,3} \\
(M_B(L))_{3,0} & (M_B(L))_{3,1} & (M_B(L))_{3,2} & (M_B(L))_{3,3}
\end{pmatrix}
=
\begin{pmatrix}
0 & \binom{1}{0} & \binom{2}{0} & \binom{3}{0} \\
0 & 0 & \binom{2}{1} & \binom{3}{1} \\
0 & 0 & 0 & \binom{3}{2} \\
0 & 0 & 0 & 0
\end{pmatrix}
=
\begin{pmatrix}
0 & 1 & 1 & 1 \\
0 & 0 & 2 & 3 \\
0 & 0 & 0 & 3 \\
0 & 0 & 0 & 0
\end{pmatrix}
$$
Cette matrice est strictement triangulaire supérieure. Son rang est $n$, comme attendu.