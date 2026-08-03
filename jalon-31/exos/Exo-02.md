# Indice de nilpotence d'un opérateur de dérivation (⭐⭐)

## Énoncé
Soit $E = \mathbb{R}_3[X]$ l'espace vectoriel des polynômes à coefficients réels de degré au plus 3.
Soit $u \in \mathcal{L}(E)$ l'endomorphisme de dérivation : $\forall P \in E, u(P) = P'$.
1. Écrire la matrice de $u$ dans la base canonique $\mathcal{B} = (1, X, X^2, X^3)$.
2. Démontrer que $u$ est nilpotent et déterminer son indice de nilpotence $p$.
3. Calculer $\ker(u^k)$ pour $k \in \{1, 2, 3, 4\}$ et vérifier les inclusions strictes.

## Corrigé Détaillé

### 1. Matrice de $u$ dans la base canonique
La base canonique est $\mathcal{B} = (e_0, e_1, e_2, e_3) = (1, X, X^2, X^3)$. La dimension de $E$ est $n=4$.
Calculons l'image par $u$ de chaque vecteur de base :
- $u(e_0) = u(1) = 0 = 0 \cdot e_0 + 0 \cdot e_1 + 0 \cdot e_2 + 0 \cdot e_3$
- $u(e_1) = u(X) = 1 = 1 \cdot e_0 + 0 \cdot e_1 + 0 \cdot e_2 + 0 \cdot e_3$
- $u(e_2) = u(X^2) = 2X = 0 \cdot e_0 + 2 \cdot e_1 + 0 \cdot e_2 + 0 \cdot e_3$
- $u(e_3) = u(X^3) = 3X^2 = 0 \cdot e_0 + 0 \cdot e_1 + 3 \cdot e_2 + 0 \cdot e_3$

La matrice $M = \text{Mat}_{\mathcal{B}}(u)$ s'écrit en disposant ces coordonnées en colonnes :
$$M = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & 2 & 0 \\ 0 & 0 & 0 & 3 \\ 0 & 0 & 0 & 0 \end{pmatrix}$$

### 2. Nilpotence et indice
Calculons les puissances successives de $u$ (ou de $M$) :
- Pour tout $P = a_0 + a_1 X + a_2 X^2 + a_3 X^3$,
- $u(P) = P' = a_1 + 2a_2 X + 3a_3 X^2$ (degré $\le 2$)
- $u^2(P) = P'' = 2a_2 + 6a_3 X$ (degré $\le 1$)
- $u^3(P) = P''' = 6a_3$ (degré $0$, constante)
- $u^4(P) = P^{(4)} = 0$ (polynôme nul)
Puisque $u^4(P) = 0$ pour tout $P \in E$, on a $u^4 = 0_{\mathcal{L}(E)}$. L'endomorphisme $u$ est donc nilpotent.
L'indice de nilpotence est le plus petit entier $p$ tel que $u^p = 0$.
Ici, $u^3(X^3) = 6 \neq 0$, donc $u^3 \neq 0_{\mathcal{L}(E)}$.
Ainsi, l'indice de nilpotence de $u$ est exactement $p = 4$.

### 3. Étude des noyaux itérés
Nous devons trouver l'ensemble des polynômes $P$ tels que $u^k(P) = 0$.
- $\ker(u^1) = \{ P \in E \mid P' = 0 \}$. Ce sont les polynômes constants. $\ker(u^1) = \text{Vect}(1) = \mathbb{R}_0[X]$.
- $\ker(u^2) = \{ P \in E \mid P'' = 0 \}$. En intégrant deux fois, on trouve les polynômes de degré $\le 1$. $\ker(u^2) = \text{Vect}(1, X) = \mathbb{R}_1[X]$.
- $\ker(u^3) = \{ P \in E \mid P''' = 0 \}$. Les polynômes de degré $\le 2$. $\ker(u^3) = \text{Vect}(1, X, X^2) = \mathbb{R}_2[X]$.
- $\ker(u^4) = \{ P \in E \mid P^{(4)} = 0 \}$. L'espace $E$ tout entier. $\ker(u^4) = \mathbb{R}_3[X] = E$.
On vérifie la suite strictement croissante d'inclusions (jusqu'à $k=p=4$) :
$$\{0\} \subsetneq \text{Vect}(1) \subsetneq \text{Vect}(1, X) \subsetneq \text{Vect}(1, X, X^2) \subsetneq \mathbb{R}_3[X]$$
Les dimensions croissent strictement de 1 à chaque étape (1, 2, 3, 4).
