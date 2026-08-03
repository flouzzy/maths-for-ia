# Matrices triangulaires strictes (⭐⭐)

## Énoncé
Soit $T_n(\mathbb{K})$ l'ensemble des matrices triangulaires supérieures strictes de taille $n \times n$ (matrices dont tous les coefficients diagonaux et sous-diagonaux sont nuls).
Démontrer rigoureusement par récurrence que le produit de $k$ matrices triangulaires strictes est une matrice dont les $k$ premières sur-diagonales sont nulles. En déduire que toute matrice triangulaire stricte de taille $n$ est nilpotente d'indice au plus $n$.

## Corrigé Détaillé

### 1. Structure du produit de matrices triangulaires strictes
Soit $A = (a_{i,j})_{1 \le i,j \le n}$ une matrice triangulaire supérieure stricte.
Par définition, $a_{i,j} = 0$ si $j \le i$. (En d'autres termes, $a_{i,j} \neq 0 \implies j > i \implies j \ge i+1$).
Considérons la propriété $\mathcal{P}(k)$ : "Le produit de $k$ matrices triangulaires supérieures strictes $A^{(1)} A^{(2)} \dots A^{(k)}$ est une matrice $M = (m_{i,j})$ telle que $m_{i,j} = 0$ pour $j < i + k$."

**Initialisation ($k=1$) :**
Pour une seule matrice $M = A^{(1)}$, l'hypothèse est que $M$ est triangulaire stricte. Donc $m_{i,j} = 0$ pour $j \le i$, soit $j < i + 1$. La propriété $\mathcal{P}(1)$ est vraie.

**Hérédité :**
Supposons $\mathcal{P}(k)$ vraie pour un entier $k \ge 1$.
Soit $M = A^{(1)} \dots A^{(k)}$, avec $m_{i,j} = 0$ si $j < i + k$.
Soit $B = A^{(k+1)}$ une matrice triangulaire stricte, avec $b_{i,j} = 0$ si $j \le i$.
Calculons le produit $C = M B$. Ses coefficients sont $c_{i,j} = \sum_{\ell=1}^n m_{i,\ell} b_{\ell,j}$.
Nous voulons montrer que $c_{i,j} = 0$ si $j < i + k + 1$.
Analysons les termes de la somme : $m_{i,\ell} b_{\ell,j}$.
Pour qu'un terme soit non nul, il faut simultanément :
1. $m_{i,\ell} \neq 0 \implies \ell \ge i + k$ (d'après $\mathcal{P}(k)$).
2. $b_{\ell,j} \neq 0 \implies j \ge \ell + 1$ (car $B$ est triangulaire stricte).
En combinant ces deux inégalités strictes :
$j \ge \ell + 1 \ge (i + k) + 1 = i + k + 1$.
Ainsi, si $j < i + k + 1$, alors pour tout $\ell \in \{1, \dots, n\}$, soit $m_{i,\ell} = 0$, soit $b_{\ell,j} = 0$.
Par conséquent, la somme est nulle : $c_{i,j} = 0$.
La propriété $\mathcal{P}(k+1)$ est donc vérifiée.
Par principe de récurrence, $\mathcal{P}(k)$ est vraie pour tout $k \ge 1$.

### 2. Nilpotence
Appliquons $\mathcal{P}(n)$ en choisissant $A^{(1)} = A^{(2)} = \dots = A^{(n)} = A$.
La matrice $M = A^n$ vérifie $m_{i,j} = 0$ si $j < i + n$.
Or, les indices des lignes $i$ et des colonnes $j$ varient entre $1$ et $n$.
La plus grande valeur possible pour $j$ est $n$, et la plus petite valeur pour $i$ est $1$.
On a toujours $j \le n < n + 1 \le i + n$.
Donc la condition $j < i + n$ est vérifiée par tous les couples $(i,j)$ de la matrice.
Par conséquent, tous les coefficients de $A^n$ sont nuls : $A^n = 0_{\mathcal{M}_n(\mathbb{K})}$.
Toute matrice triangulaire stricte de taille $n$ est donc nilpotente, d'indice de nilpotence au plus $n$.
