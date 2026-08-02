# Exercice 04 : Bloc de Jordan fondamental (⭐⭐⭐)

## Énoncé
Soit $J \in \mathcal{M}_3(\mathbb{R})$ le bloc de Jordan nilpotent canonique :
$$J = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$
Soit $N \in \mathcal{M}_3(\mathbb{R})$ une matrice telle que $N^3 = 0$ et $N^2 \neq 0$.
1. Calculer les puissances successives de $J$.
2. Montrer que $\ker(N)$ est de dimension 1.
3. Démontrer qu'il existe un vecteur $x \in \mathbb{R}^3$ tel que la famille $\mathcal{B} = (N^2 x, Nx, x)$ est une base de $\mathbb{R}^3$.
4. Quelle est la matrice de l'endomorphisme associé à $N$ dans cette base $\mathcal{B}$ ? Conclure.

## Corrigé Rigoureux : Démonstration Complète

### 1. Puissances de $J$
$$J = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$$
On calcule $J^2$ :
$$J^2 = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$
On calcule $J^3$ :
$$J^3 = J^2 J = \begin{pmatrix} 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix} \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$$
L'indice de nilpotence de $J$ est exactement 3.

### 2. Dimension du noyau
Soit $u$ l'endomorphisme canoniquement associé à $N$. $u$ est nilpotent d'indice 3.
Nous avons la suite stricte des noyaux :
$\{0\} \subsetneq \ker(u) \subsetneq \ker(u^2) \subsetneq \ker(u^3) = \mathbb{R}^3$
Soit $d_k = \dim(\ker(u^k))$. La suite $(d_k)$ est strictement croissante.
De plus, $d_0 = 0$ et $d_3 = 3$.
Puisque les inclusions sont strictes, les dimensions sautent d'au moins 1 à chaque étape.
Il faut faire 3 sauts pour passer de 0 à 3, donc $d_k = k$ pour tout $k \in \{0, 1, 2, 3\}$.
En particulier, $\dim(\ker(u)) = 1$.

### 3. Construction de la base
Puisque $u^2 \neq 0$, il existe au moins un vecteur $x \in \mathbb{R}^3$ tel que $u^2(x) \neq 0$.
Considérons la famille $\mathcal{B} = (u^2(x), u(x), x)$.
Montrons qu'elle est libre.
Soit $a, b, c \in \mathbb{R}$ tels que $a u^2(x) + b u(x) + c x = 0$.
Appliquons $u^2$ à cette équation :
$a u^4(x) + b u^3(x) + c u^2(x) = 0$.
Puisque $u^3 = 0$ (donc $u^4 = 0$), il reste $c u^2(x) = 0$.
Comme $u^2(x) \neq 0$, nous déduisons $c = 0$.
L'équation initiale se réduit à $a u^2(x) + b u(x) = 0$.
Appliquons $u$ :
$a u^3(x) + b u^2(x) = 0$.
De nouveau, $u^3 = 0$, donc $b u^2(x) = 0$, ce qui implique $b = 0$.
L'équation se réduit à $a u^2(x) = 0$, donc $a = 0$.
La famille $\mathcal{B}$ est libre.
Puisque son cardinal est 3 et $\dim(\mathbb{R}^3) = 3$, c'est une base de $\mathbb{R}^3$.

### 4. Matrice dans la base $\mathcal{B}$
Posons $e_1 = u^2(x)$, $e_2 = u(x)$, $e_3 = x$.
Calculons l'image par $u$ des vecteurs de cette base :
- $u(e_1) = u(u^2(x)) = u^3(x) = 0 = 0 \cdot e_1 + 0 \cdot e_2 + 0 \cdot e_3$
- $u(e_2) = u(u(x)) = u^2(x) = e_1 = 1 \cdot e_1 + 0 \cdot e_2 + 0 \cdot e_3$
- $u(e_3) = u(x) = e_2 = 0 \cdot e_1 + 1 \cdot e_2 + 0 \cdot e_3$
La matrice de $u$ dans la base $\mathcal{B}$ est donc :
$$M = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix} = J$$
**Conclusion :** Tout endomorphisme nilpotent d'indice 3 en dimension 3 est semblable au bloc de Jordan canonique $J_3(0)$. Ce processus (choisir un vecteur qui ne s'annule qu'à la puissance maximale et construire la famille de ses images) s'appelle la construction d'une chaîne de Jordan.
