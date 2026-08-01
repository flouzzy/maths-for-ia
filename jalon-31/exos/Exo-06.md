# Commutant d'un bloc de Jordan (⭐⭐⭐)

## Énoncé
Soit $J_n \in \mathcal{M}_n(\mathbb{R})$ le bloc de Jordan nilpotent canonique (des 1 sur la sur-diagonale, 0 ailleurs).
Soit $C(J_n) = \{ M \in \mathcal{M}_n(\mathbb{R}) \mid M J_n = J_n M \}$ le commutant de $J_n$.
1. Démontrer que si $M$ commute avec $J_n$, alors $M$ est un polynôme en $J_n$. (Indice : évaluer les relations de commutation sur les coefficients de la matrice).
2. En déduire la dimension de l'espace vectoriel $C(J_n)$.

## Corrigé Détaillé

### 1. Analyse de la commutation
Soit $M = (m_{i,j})_{1 \le i,j \le n}$ une matrice.
Le produit $J_n M$ est la matrice dont la $i$-ème ligne est la $(i+1)$-ème ligne de $M$ pour $i<n$, et la dernière ligne est nulle.
$(J_n M)_{i,j} = m_{i+1, j} \quad (\text{avec } m_{n+1, j} = 0)$
Le produit $M J_n$ est la matrice dont la $j$-ème colonne est la $(j-1)$-ème colonne de $M$ pour $j>1$, et la première colonne est nulle.
$(M J_n)_{i,j} = m_{i, j-1} \quad (\text{avec } m_{i, 0} = 0)$

L'égalité $M J_n = J_n M$ s'écrit composante par composante :
Pour tout $1 \le i \le n$ et $1 \le j \le n$, $m_{i, j-1} = m_{i+1, j}$.
- Pour $j=1$ : $m_{i+1, 1} = m_{i, 0} = 0$. Donc la première colonne de $M$ (sauf $m_{1,1}$) est nulle : $m_{2,1} = m_{3,1} = \dots = m_{n,1} = 0$.
- Pour $i=n$ : $m_{n, j-1} = m_{n+1, j} = 0$. Donc la dernière ligne de $M$ (sauf $m_{n,n}$) est nulle : $m_{n,1} = m_{n,2} = \dots = m_{n,n-1} = 0$.
- Par la relation $m_{i, j-1} = m_{i+1, j}$, la matrice $M$ est constante sur chaque diagonale parallèle à la diagonale principale. Une telle matrice s'appelle une matrice de Toeplitz.
Les coefficients sous-diagonaux sont nuls (car égaux aux éléments de la première colonne qui sont nuls).
Il ne reste que des valeurs arbitraires sur la diagonale principale ($a_0$) et les sur-diagonales ($a_1, a_2, \dots, a_{n-1}$).
$M$ a donc la forme :
$$M = \begin{pmatrix} a_0 & a_1 & a_2 & \dots & a_{n-1} \\ 0 & a_0 & a_1 & \dots & a_{n-2} \\ 0 & 0 & a_0 & \ddots & \vdots \\ \vdots & \vdots & \ddots & \ddots & a_1 \\ 0 & 0 & \dots & 0 & a_0 \end{pmatrix}$$
Or, on vérifie facilement que la matrice avec des 1 sur la $k$-ème sur-diagonale est exactement $(J_n)^k$.
Par convention, $(J_n)^0 = I_n$.
Ainsi, $M$ s'écrit de manière unique comme combinaison linéaire des puissances de $J_n$ :
$M = a_0 I_n + a_1 J_n + a_2 (J_n)^2 + \dots + a_{n-1} (J_n)^{n-1}$.
Cela montre que $M$ est un polynôme en $J_n$ : $M \in \mathbb{R}[J_n]$.

### 2. Dimension du commutant
Nous avons montré que $C(J_n) \subseteq \text{Vect}(I_n, J_n, (J_n)^2, \dots, (J_n)^{n-1})$.
Réciproquement, tout polynôme en $J_n$ commute évidemment avec $J_n$ (car les puissances commutent entre elles).
Donc $C(J_n) = \text{Vect}(I_n, J_n, (J_n)^2, \dots, (J_n)^{n-1})$.
Il reste à montrer que la famille $\mathcal{F} = (I_n, J_n, \dots, (J_n)^{n-1})$ est libre.
Soit une combinaison linéaire nulle : $\sum_{k=0}^{n-1} \lambda_k (J_n)^k = 0$.
La matrice résultante est exactement la matrice de Toeplitz avec les $\lambda_k$ sur les diagonales. Pour qu'elle soit nulle, il faut que tous ses coefficients soient nuls, c'est-à-dire $\lambda_0 = \lambda_1 = \dots = \lambda_{n-1} = 0$.
La famille est donc une base de $C(J_n)$.
La dimension du commutant est donc le nombre d'éléments de cette base, soit $n$.
