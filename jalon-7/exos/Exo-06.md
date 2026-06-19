# Exercice 6 : Analyse d'une famille de polynômes sommatoires

## Énoncé

Soit $\mathbb{R}$ le corps des nombres réels.
Soit $n$ un entier naturel non nul, c'est-à-dire $n \in \mathbb{N}^*$.
Soit $E = \mathbb{R}_n[X]$ l'espace vectoriel des polynômes à coefficients réels de degré inférieur ou égal à $n$. Cet espace est un $\mathbb{R}$-espace vectoriel.

Pour tout entier $k \in \{0, 1, \dots, n\}$, nous définissons le polynôme $P_k(X) \in E$ par la somme suivante :
$$P_k(X) = \sum_{j=0}^k X^j = 1 + X + X^2 + \dots + X^k$$

Considérons la famille de polynômes $\mathcal{F} = (P_0(X), P_1(X), \dots, P_n(X))$.

1.  Démontrer que la famille $\mathcal{F}$ est une famille libre dans $E$.
2.  Démontrer que la famille $\mathcal{F}$ est une famille génératrice de $E$.
3.  En déduire que $\mathcal{F}$ est une base de $E$.

## Correction Détaillée

### 1. Démonstration que la famille $\mathcal{F}$ est une famille libre dans $E$

Pour démontrer que la famille $\mathcal{F} = (P_0(X), P_1(X), \dots, P_n(X))$ est une famille libre dans $E$, nous devons montrer que toute combinaison linéaire des polynômes de $\mathcal{F}$ égale au polynôme nul $0_E$ implique que tous les coefficients de cette combinaison linéaire sont nuls.

Soient $\lambda_0, \lambda_1, \dots, \lambda_n$ des scalaires appartenant à $\mathbb{R}$.
Supposons que la combinaison linéaire suivante est égale au polynôme nul $0_E$:
$$ \sum_{k=0}^n \lambda_k P_k(X) = 0_E $$

Nous substituons l'expression de $P_k(X)$ dans cette équation :
$$ \sum_{k=0}^n \lambda_k \left( \sum_{j=0}^k X^j \right) = 0_E $$

Nous allons réécrire cette somme en regroupant les termes par puissances de $X$. Pour un $X^j$ donné, il apparaît dans $P_k(X)$ si et seulement si $j \le k$. Donc, pour une puissance $X^j$, les coefficients $\lambda_k$ qui la multiplient sont ceux pour lesquels $k \ge j$.
$$ \sum_{j=0}^n \left( \sum_{k=j}^n \lambda_k \right) X^j = 0_E $$

L'ensemble $(1, X, X^2, \dots, X^n)$ est la base canonique de $E = \mathbb{R}_n[X]$. Par définition d'une base, cette famille est libre. Par conséquent, si un polynôme est égal au polynôme nul, tous ses coefficients dans la base canonique doivent être nuls.
Ainsi, pour chaque $j \in \{0, 1, \dots, n\}$, le coefficient de $X^j$ doit être nul :
$$ \sum_{k=j}^n \lambda_k = 0 \quad \text{pour tout } j \in \{0, 1, \dots, n\} $$

Nous obtenons le système d'équations linéaires suivant :
Pour $j=n$ :
$$ \lambda_n = 0 \quad (1) $$
Pour $j=n-1$ :
$$ \lambda_{n-1} + \lambda_n = 0 \quad (2) $$
Pour $j=n-2$ :
$$ \lambda_{n-2} + \lambda_{n-1} + \lambda_n = 0 \quad (3) $$
...
Pour $j=0$ :
$$ \lambda_0 + \lambda_1 + \dots + \lambda_n = 0 \quad (n+1) $$

Nous allons résoudre ce système en commençant par la dernière équation (correspondant à $j=n$) et en remontant.

De l'équation (1), nous avons :
$$ \lambda_n = 0 $$

Nous substituons cette valeur dans l'équation (2) :
$$ \lambda_{n-1} + 0 = 0 $$
$$ \lambda_{n-1} = 0 $$

Nous substituons les valeurs de $\lambda_n$ et $\lambda_{n-1}$ dans l'équation (3) :
$$ \lambda_{n-2} + 0 + 0 = 0 $$
$$ \lambda_{n-2} = 0 $$

En poursuivant ce processus par récurrence descendante, supposons que pour un certain $m \in \{1, \dots, n\}$, nous avons démontré que $\lambda_n = \lambda_{n-1} = \dots = \lambda_{n-m+1} = 0$.
L'équation correspondant à $j = n-m$ est :
$$ \lambda_{n-m} + \lambda_{n-m+1} + \dots + \lambda_n = 0 $$
En substituant les valeurs nulles des termes suivants :
$$ \lambda_{n-m} + 0 + \dots + 0 = 0 $$
$$ \lambda_{n-m} = 0 $$
Cette démonstration par récurrence descendante montre que tous les coefficients $\lambda_j$ doivent être nuls pour $j \in \{0, 1, \dots, n\}$.

Puisque $\lambda_0 = \lambda_1 = \dots = \lambda_n = 0$, la famille $\mathcal{F}$ est une famille libre dans $E$.

### 2. Démonstration que la famille $\mathcal{F}$ est une famille génératrice de $E$

Pour démontrer que la famille $\mathcal{F}$ est une famille génératrice de $E$, nous devons montrer que tout polynôme $Q(X) \in E$ peut être écrit comme une combinaison linéaire des polynômes de $\mathcal{F}$.

Soit $Q(X)$ un polynôme arbitraire dans $E = \mathbb{R}_n[X]$. Il peut s'écrire dans la base canonique $(1, X, \dots, X^n)$ sous la forme :
$$ Q(X) = \sum_{j=0}^n a_j X^j $$
où $a_j \in \mathbb{R}$ sont les coefficients de $Q(X)$.

Nous cherchons des scalaires $\mu_0, \mu_1, \dots, \mu_n \in \mathbb{R}$ tels que :
$$ Q(X) = \sum_{k=0}^n \mu_k P_k(X) $$

Nous allons d'abord exprimer les monômes $X^j$ en fonction des polynômes $P_k(X)$.
Par définition, nous avons :
$P_0(X) = 1$
$P_1(X) = 1 + X$
$P_2(X) = 1 + X + X^2$
...
$P_k(X) = 1 + X + \dots + X^k$

Nous pouvons observer la relation suivante pour $k \ge 1$ :
$P_k(X) = (1 + X + \dots + X^{k-1}) + X^k = P_{k-1}(X) + X^k$.
De cette relation, nous pouvons exprimer $X^k$ en fonction de $P_k(X)$ et $P_{k-1}(X)$ pour $k \in \{1, \dots, n\}$ :
$$ X^k = P_k(X) - P_{k-1}(X) \quad \text{pour } k \in \{1, \dots, n\} $$
Pour $k=0$, nous avons simplement :
$$ X^0 = 1 = P_0(X) $$

Maintenant, nous substituons ces expressions des monômes $X^j$ dans l'expression de $Q(X)$ :
$$ Q(X) = a_0 X^0 + a_1 X^1 + a_2 X^2 + \dots + a_n X^n $$
$$ Q(X) = a_0 P_0(X) + a_1 (P_1(X) - P_0(X)) + a_2 (P_2(X) - P_1(X)) + \dots + a_n (P_n(X) - P_{n-1}(X)) $$

Nous regroupons les termes par $P_k(X)$ :
$$ Q(X) = a_0 P_0(X) - a_1 P_0(X) + a_1 P_1(X) - a_2 P_1(X) + a_2 P_2(X) - \dots - a_n P_{n-1}(X) + a_n P_n(X) $$
$$ Q(X) = (a_0 - a_1) P_0(X) + (a_1 - a_2) P_1(X) + (a_2 - a_3) P_2(X) + \dots + (a_{n-1} - a_n) P_{n-1}(X) + a_n P_n(X) $$

Nous pouvons définir les coefficients $\mu_k$ comme suit :
$$ \mu_k = a_k - a_{k+1} \quad \text{pour } k \in \{0, 1, \dots, n-1\} $$
$$ \mu_n = a_n $$
Ces coefficients $\mu_k$ sont des nombres réels bien définis, car les $a_j$ sont des nombres réels.

Ainsi, tout polynôme $Q(X) \in E$ peut être écrit comme une combinaison linéaire des polynômes de la famille $\mathcal{F}$.
Par conséquent, la famille $\mathcal{F}$ est une famille génératrice de $E$.

### 3. Conclusion

Nous avons démontré dans la partie 1 que la famille $\mathcal{F} = (P_0(X), P_1(X), \dots, P_n(X))$ est une famille libre dans $E$.
Nous avons démontré dans la partie 2 que la famille $\mathcal{F}$ est une famille génératrice de $E$.

Par définition, une famille de vecteurs qui est à la fois libre et génératrice pour un espace vectoriel est une base de cet espace vectoriel.
De plus, nous savons que la dimension de $E = \mathbb{R}_n[X]$ est $\dim(E) = n+1$.
La famille $\mathcal{F}$ contient $n+1$ polynômes.
Puisque $\mathcal{F}$ est une famille libre de $n+1$ vecteurs dans un espace vectoriel de dimension $n+1$, elle est nécessairement une base de cet espace.
De même, puisque $\mathcal{F}$ est une famille génératrice de $n+1$ vecteurs dans un espace vectoriel de dimension $n+1$, elle est nécessairement une base de cet espace.

En conclusion, la famille $\mathcal{F}$ est une base de $E = \mathbb{R}_n[X]$.
