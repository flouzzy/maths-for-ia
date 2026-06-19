# Exercice 8 : Bases de polynômes de type Bernstein

## Énoncé

Soit $\mathbb{K}$ un corps commutatif.
Soit $n$ un entier naturel.
On considère $E = \mathbb{K}_n[X]$, le $\mathbb{K}$-espace vectoriel des polynômes à coefficients dans $\mathbb{K}$ de degré inférieur ou égal à $n$.
On définit la famille de polynômes $\mathcal{B} = (P_k)_{k=0}^n$ par $P_k(X) = X^k (1-X)^{n-k}$ pour tout $k \in \{0, 1, \dots, n\}$.

Démontrer que $\mathcal{B}$ est une base du $\mathbb{K}$-espace vectoriel $E$.

## Correction Détaillée

1.  **Nature des objets et appartenance à l'espace vectoriel :**
    *   $\mathbb{K}$ est un corps commutatif.
    *   $n$ est un entier naturel.
    *   $E = \mathbb{K}_n[X]$ est le $\mathbb{K}$-espace vectoriel des polynômes à coefficients dans $\mathbb{K}$ de degré inférieur ou égal à $n$.
    *   Pour tout $k \in \{0, 1, \dots, n\}$, le polynôme $P_k(X)$ est défini par $P_k(X) = X^k (1-X)^{n-k}$.
    *   Le degré du polynôme $X^k$ est $k$.
    *   Le degré du polynôme $(1-X)^{n-k}$ est $n-k$.
    *   Le degré du produit de deux polynômes est la somme de leurs degrés.
    *   Par conséquent, le degré de $P_k(X)$ est $\deg(P_k(X)) = \deg(X^k) + \deg((1-X)^{n-k}) = k + (n-k) = n$.
    *   Puisque $\deg(P_k(X)) = n$ et que $n \le n$, chaque polynôme $P_k(X)$ appartient bien à l'espace vectoriel $E$.
    *   La famille $\mathcal{B} = (P_0(X), P_1(X), \dots, P_n(X))$ est une famille de $n+1$ polynômes de $E$.

2.  **Dimension de l'espace vectoriel :**
    *   Le $\mathbb{K}$-espace vectoriel $E = \mathbb{K}_n[X]$ est un espace de dimension finie.
    *   Une base canonique de $E$ est la famille des monômes $(1, X, X^2, \dots, X^n)$.
    *   Cette base canonique contient $n+1$ éléments.
    *   Par conséquent, la dimension de $E$ est $\dim_{\mathbb{K}}(E) = n+1$.

3.  **Condition pour être une base :**
    *   Pour qu'une famille de vecteurs soit une base d'un espace vectoriel de dimension finie, il est nécessaire et suffisant qu'elle soit une famille libre et qu'elle contienne un nombre d'éléments égal à la dimension de l'espace.
    *   Nous avons établi que la famille $\mathcal{B}$ contient $n+1$ éléments et que $\dim_{\mathbb{K}}(E) = n+1$.
    *   Il nous reste donc à démontrer que la famille $\mathcal{B}$ est une famille libre.

4.  **Démonstration de la liberté de la famille $\mathcal{B}$ :**

    *   **Cas particulier $n=0$ :**
        *   Si $n=0$, alors $E = \mathbb{K}_0[X]$ est l'espace des polynômes constants. Sa dimension est 1.
        *   La famille $\mathcal{B}$ est $(P_0(X))$.
        *   $P_0(X) = X^0 (1-X)^0$. Par convention, $X^0=1$ et $(1-X)^0=1$. Donc $P_0(X) = 1$.
        *   Pour montrer que la famille $\mathcal{B}=(1)$ est libre, considérons un scalaire $a_0 \in \mathbb{K}$ tel que $a_0 \cdot P_0(X) = 0_E$.
        *   Ceci signifie $a_0 \cdot 1 = 0$.
        *   Puisque $1$ est l'élément neutre de la multiplication dans $\mathbb{K}$ et $1 \ne 0$ dans un corps, il s'ensuit que $a_0=0$.
        *   La famille $\mathcal{B}$ est donc libre. Ayant 1 élément dans un espace de dimension 1, c'est une base de $E$.

    *   **Cas général $n \ge 1$ :**
        *   Soient $a_0, a_1, \dots, a_n$ des scalaires de $\mathbb{K}$.
        *   Supposons que la combinaison linéaire de ces polynômes est le polynôme nul de $E$, c'est-à-dire :
            $\sum_{k=0}^n a_k P_k(X) = 0_E$
        *   En substituant l'expression de $P_k(X)$, nous obtenons l'identité polynomiale :
            $\sum_{k=0}^n a_k X^k (1-X)^{n-k} = 0$ (le polynôme nul de $\mathbb{K}[X]$).

        *   Nous allons démontrer par récurrence finie sur $j$ que tous les coefficients $a_j$ sont nuls pour $j \in \{0, 1, \dots, n\}$.

        *   **Initialisation (pour $j=0$) :**
            *   Évaluons le polynôme $\sum_{k=0}^n a_k X^k (1-X)^{n-k}$ en $X=0$.
            *   $\sum_{k=0}^n a_k (0)^k (1-0)^{n-k} = a_0 (0)^0 (1-0)^n + \sum_{k=1}^n a_k (0)^k (1-0)^{n-k}$.
            *   Par convention, $0^0=1$. Pour tout $k \ge 1$, $(0)^k = 0$.
            *   Donc, l'expression devient $a_0 \cdot 1 \cdot 1^n + \sum_{k=1}^n a_k \cdot 0 \cdot 1^{n-k} = a_0 + 0 = a_0$.
            *   Puisque le polynôme $\sum_{k=0}^n a_k X^k (1-X)^{n-k}$ est le polynôme nul, son évaluation en $X=0$ doit être $0$.
            *   Par conséquent, $a_0 = 0$.

        *   **Hypothèse de récurrence :**
            *   Supposons que pour un certain entier $j \in \{0, 1, \dots, n-1\}$, les coefficients $a_0, a_1, \dots, a_{j-1}$ sont tous nuls.
            *   C'est-à-dire, $a_i = 0$ pour tout $i \in \{0, 1, \dots, j-1\}$.

        *   **Étape de récurrence :**
            *   Sous l'hypothèse de récurrence, l'équation de la combinaison linéaire $\sum_{k=0}^n a_k X^k (1-X)^{n-k} = 0$ se simplifie en :
                $\sum_{k=j}^n a_k X^k (1-X)^{n-k} = 0$.
            *   Nous pouvons factoriser $X^j$ de chaque terme de la somme, puisque $k \ge j$ pour tous les termes restants :
                $X^j \left( \sum_{k=j}^n a_k X^{k-j} (1-X)^{n-k} \right) = 0$.
            *   Soit $Q_j(X) = \sum_{k=j}^n a_k X^{k-j} (1-X)^{n-k}$.
            *   L'équation est $X^j Q_j(X) = 0$.
            *   Puisque $X^j$ est un polynôme non nul de $\mathbb{K}[X]$ (pour tout $j \ge 0$) et que l'anneau des polynômes $\mathbb{K}[X]$ est un anneau intègre (car $\mathbb{K}$ est un corps), il s'ensuit que le polynôme $Q_j(X)$ doit être le polynôme nul.
            *   Donc, $Q_j(X) = 0$ pour tout $X \in \mathbb{K}$.
            *   Évaluons $Q_j(X)$ en $X=0$ :
                $Q_j(0) = \sum_{k=j}^n a_k (0)^{k-j} (1-0)^{n-k}$.
            *   Le terme de la somme pour $k=j$ est $a_j (0)^{j-j} (1-0)^{n-j} = a_j \cdot 1 \cdot 1^{n-j} = a_j$.
            *   Pour tout $k$ tel que $j < k \le n$, l'exposant $k-j$ est strictement positif, donc $(0)^{k-j} = 0$.
            *   Ainsi, tous les termes de la somme pour $k > j$ sont nuls.
            *   Par conséquent, $Q_j(0) = a_j$.
            *   Puisque $Q_j(X)$ est le polynôme nul, son évaluation en $X=0$ doit être $0$.
            *   Donc, $a_j = 0$.

        *   **Conclusion de la récurrence :**
            *   Par le principe de récurrence, nous avons montré que $a_j = 0$ pour tout $j \in \{0, 1, \dots, n\}$.
            *   Tous les coefficients $a_k$ sont nuls.
            *   Ceci démontre que la famille $\mathcal{B}$ est une famille libre dans $E$.

5.  **Conclusion finale :**
    *   La famille $\mathcal{B}$ est une famille de $n+1$ polynômes de $E$.
    *   La dimension de $E$ est $n+1$.
    *   La famille $\mathcal{B}$ est une famille libre.
    *   Par conséquent, la famille $\mathcal{B}$ est une base du $\mathbb{K}$-espace vectoriel $E$.
