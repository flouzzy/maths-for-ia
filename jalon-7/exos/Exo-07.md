# Exercice 7 : Étude d'un sous-espace de polynômes et construction d'une base

## Énoncé

Soit $\mathbb{K}$ un corps commutatif. Nous considérons l'espace vectoriel $\mathbb{K}_n[X]$ des polynômes à coefficients dans $\mathbb{K}$ de degré inférieur ou égal à $n$, où $n$ est un entier naturel tel que $n \ge 2$.

Nous définissons l'ensemble $E$ comme suit :
$$ E = \left\{ P(X) \in \mathbb{K}_n[X] \mid P(1) = 0 \quad \text{et} \quad \int_0^1 P(x) dx = 0 \right\} $$
où l'intégrale est définie formellement pour les polynômes sur $\mathbb{K}$ (si $\mathbb{K} = \mathbb{R}$ ou $\mathbb{C}$, c'est l'intégrale usuelle ; sinon, c'est l'application linéaire qui à $P(X) = \sum_{i=0}^n c_i X^i$ associe $\sum_{i=0}^n \frac{c_i}{i+1}$).

1.  Démontrer que $E$ est un sous-espace vectoriel de $\mathbb{K}_n[X]$.
2.  Déterminer la dimension de $E$.
3.  On considère la famille de polynômes $\mathcal{F} = (P_k(X))_{k=2}^n$ définie pour tout $k \in \{2, \dots, n\}$ par :
    $$ P_k(X) = X^k - \frac{2k}{k+1}X + \frac{k-1}{k+1} $$
    a.  Vérifier que chaque polynôme $P_k(X)$ appartient à $E$.
    b.  Démontrer que la famille $\mathcal{F}$ est une famille libre dans $E$.
    c.  Démontrer que la famille $\mathcal{F}$ est une famille génératrice de $E$.
    d.  En déduire que $\mathcal{F}$ est une base de $E$.

## Correction Détaillée

Nous allons aborder chaque question avec la rigueur nécessaire, en détaillant chaque étape.

### Question 1 : Démontrer que $E$ est un sous-espace vectoriel de $\mathbb{K}_n[X]$.

Pour démontrer que $E$ est un sous-espace vectoriel de $\mathbb{K}_n[X]$, nous devons vérifier trois conditions fondamentales :
1.  $E$ est un sous-ensemble de $\mathbb{K}_n[X]$.
2.  Le vecteur nul de $\mathbb{K}_n[X]$ appartient à $E$.
3.  $E$ est stable par addition vectorielle et par multiplication par un scalaire.

**1. $E$ est un sous-ensemble de $\mathbb{K}_n[X]$ :**
Par définition, $E$ est l'ensemble des polynômes $P(X)$ qui appartiennent à $\mathbb{K}_n[X]$ et qui satisfont deux conditions supplémentaires. Il est donc clair que $E \subseteq \mathbb{K}_n[X]$.

**2. Le vecteur nul de $\mathbb{K}_n[X]$ appartient à $E$ :**
Soit $0_{\mathbb{K}_n[X]}$ le polynôme nul, c'est-à-dire le polynôme dont tous les coefficients sont nuls.
*   Évaluation en $X=1$ : $0_{\mathbb{K}_n[X]}(1) = 0$. La première condition est satisfaite.
*   Intégrale de $0_{\mathbb{K}_n[X]}$ : $\int_0^1 0_{\mathbb{K}_n[X]}(x) dx = \int_0^1 0 dx = 0$. La deuxième condition est satisfaite.
Puisque les deux conditions sont satisfaites, le polynôme nul $0_{\mathbb{K}_n[X]}$ appartient à $E$.

**3. $E$ est stable par addition vectorielle et par multiplication par un scalaire :**
Soient $P(X)$ et $Q(X)$ deux polynômes quelconques appartenant à $E$, et soit $\lambda$ un scalaire quelconque de $\mathbb{K}$.

*   **Stabilité par addition :**
    Puisque $P(X) \in E$ et $Q(X) \in E$, nous avons par définition :
    $P(1) = 0$ et $\int_0^1 P(x) dx = 0$.
    $Q(1) = 0$ et $\int_0^1 Q(x) dx = 0$.
    Considérons le polynôme somme $(P+Q)(X)$.
    *   Évaluation en $X=1$ : $(P+Q)(1) = P(1) + Q(1)$. Par les propriétés de l'évaluation polynomiale.
        Puisque $P(1)=0$ et $Q(1)=0$, nous obtenons $(P+Q)(1) = 0 + 0 = 0$.
    *   Intégrale de $(P+Q)(X)$ : $\int_0^1 (P+Q)(x) dx = \int_0^1 P(x) dx + \int_0^1 Q(x) dx$. Par la linéarité de l'intégrale.
        Puisque $\int_0^1 P(x) dx = 0$ et $\int_0^1 Q(x) dx = 0$, nous obtenons $\int_0^1 (P+Q)(x) dx = 0 + 0 = 0$.
    Les deux conditions étant satisfaites, le polynôme $(P+Q)(X)$ appartient à $E$.

*   **Stabilité par multiplication par un scalaire :**
    Considérons le polynôme $(\lambda P)(X)$.
    *   Évaluation en $X=1$ : $(\lambda P)(1) = \lambda \cdot P(1)$. Par les propriétés de l'évaluation polynomiale.
        Puisque $P(1)=0$, nous obtenons $(\lambda P)(1) = \lambda \cdot 0 = 0$.
    *   Intégrale de $(\lambda P)(X)$ : $\int_0^1 (\lambda P)(x) dx = \lambda \int_0^1 P(x) dx$. Par la linéarité de l'intégrale.
        Puisque $\int_0^1 P(x) dx = 0$, nous obtenons $\int_0^1 (\lambda P)(x) dx = \lambda \cdot 0 = 0$.
    Les deux conditions étant satisfaites, le polynôme $(\lambda P)(X)$ appartient à $E$.

Puisque les trois conditions sont vérifiées, nous pouvons conclure que $E$ est un sous-espace vectoriel de $\mathbb{K}_n[X]$.

### Question 2 : Déterminer la dimension de $E$.

L'espace vectoriel $\mathbb{K}_n[X]$ est de dimension finie, et sa dimension est $\dim(\mathbb{K}_n[X]) = n+1$.
Nous allons utiliser le théorème du rang pour les applications linéaires.
Définissons deux applications linéaires de $\mathbb{K}_n[X]$ vers $\mathbb{K}$ :
*   $\phi_1: \mathbb{K}_n[X] \to \mathbb{K}$ définie par $\phi_1(P) = P(1)$.
*   $\phi_2: \mathbb{K}_n[X] \to \mathbb{K}$ définie par $\phi_2(P) = \int_0^1 P(x) dx$.

Ces applications sont linéaires :
*   Pour $\phi_1$: $\phi_1(P+Q) = (P+Q)(1) = P(1)+Q(1) = \phi_1(P)+\phi_1(Q)$. $\phi_1(\lambda P) = (\lambda P)(1) = \lambda P(1) = \lambda \phi_1(P)$.
*   Pour $\phi_2$: $\phi_2(P+Q) = \int_0^1 (P+Q)(x)dx = \int_0^1 P(x)dx + \int_0^1 Q(x)dx = \phi_2(P)+\phi_2(Q)$. $\phi_2(\lambda P) = \int_0^1 (\lambda P)(x)dx = \lambda \int_0^1 P(x)dx = \lambda \phi_2(P)$.

L'ensemble $E$ est précisément l'intersection des noyaux de ces deux applications linéaires :
$E = \ker(\phi_1) \cap \ker(\phi_2)$.

Pour déterminer la dimension de $E$, nous allons considérer l'application linéaire $\Phi: \mathbb{K}_n[X] \to \mathbb{K}^2$ définie par $\Phi(P) = (\phi_1(P), \phi_2(P))$.
Le noyau de $\Phi$ est $\ker(\Phi) = \{ P \in \mathbb{K}_n[X] \mid \phi_1(P)=0 \text{ et } \phi_2(P)=0 \} = E$.
D'après le théorème du rang, $\dim(\mathbb{K}_n[X]) = \dim(\ker(\Phi)) + \dim(\text{Im}(\Phi))$.
Donc, $\dim(E) = \dim(\mathbb{K}_n[X]) - \dim(\text{Im}(\Phi))$.
Nous savons que $\dim(\mathbb{K}_n[X]) = n+1$. Il nous faut déterminer $\dim(\text{Im}(\Phi))$.
L'image $\text{Im}(\Phi)$ est un sous-espace vectoriel de $\mathbb{K}^2$. Sa dimension peut être 0, 1 ou 2.
$\dim(\text{Im}(\Phi))$ est égale au nombre de formes linéaires linéairement indépendantes parmi $\phi_1$ et $\phi_2$.

Vérifions si $\phi_1$ et $\phi_2$ sont linéairement indépendantes.
Supposons qu'il existe des scalaires $\alpha, \beta \in \mathbb{K}$ tels que $\alpha \phi_1 + \beta \phi_2 = 0$.
Ceci signifie que pour tout polynôme $P(X) \in \mathbb{K}_n[X]$, nous avons $\alpha P(1) + \beta \int_0^1 P(x) dx = 0$.

1.  Considérons le polynôme $P_A(X) = X-1$.
    *   $P_A(1) = 1-1 = 0$.
    *   $\int_0^1 P_A(x) dx = \int_0^1 (x-1) dx = \left[ \frac{x^2}{2} - x \right]_0^1 = \left( \frac{1^2}{2} - 1 \right) - \left( \frac{0^2}{2} - 0 \right) = \frac{1}{2} - 1 = -\frac{1}{2}$.
    En substituant $P_A(X)$ dans l'équation $\alpha P(1) + \beta \int_0^1 P(x) dx = 0$:
    $\alpha \cdot 0 + \beta \cdot \left(-\frac{1}{2}\right) = 0$.
    Ceci implique $-\frac{\beta}{2} = 0$, et donc $\beta = 0$.

2.  Maintenant que nous savons $\beta=0$, l'équation $\alpha P(1) + \beta \int_0^1 P(x) dx = 0$ se réduit à $\alpha P(1) = 0$ pour tout $P(X) \in \mathbb{K}_n[X]$.
    Considérons le polynôme $P_B(X) = 1$. Ce polynôme est bien dans $\mathbb{K}_n[X]$ puisque $n \ge 2$.
    *   $P_B(1) = 1$.
    En substituant $P_B(X)$ dans l'équation $\alpha P(1) = 0$:
    $\alpha \cdot 1 = 0$.
    Ceci implique $\alpha = 0$.

Puisque $\alpha=0$ et $\beta=0$ sont les seules solutions, les formes linéaires $\phi_1$ et $\phi_2$ sont linéairement indépendantes.
Cela signifie que $\dim(\text{Im}(\Phi)) = 2$.

En utilisant le théorème du rang :
$\dim(E) = \dim(\mathbb{K}_n[X]) - \dim(\text{Im}(\Phi)) = (n+1) - 2 = n-1$.

La dimension de $E$ est $n-1$.
Il est important de noter que cette formule est valide pour $n \ge 1$. Si $n=1$, $\dim(E)=0$, ce qui signifie $E=\{0\}$.
Pour $n=1$, $P(X)=c_0+c_1X$. $P(1)=c_0+c_1=0$. $\int_0^1 P(x)dx = c_0 + c_1/2 = 0$.
En soustrayant les deux équations : $(c_0+c_1)-(c_0+c_1/2)=0 \implies c_1/2=0 \implies c_1=0$.
Si $c_1=0$, alors $c_0=0$. Donc $E=\{0\}$. La formule $n-1$ est correcte.
L'énoncé spécifie $n \ge 2$, donc $\dim(E) = n-1 \ge 1$.

### Question 3 : Analyse de la famille $\mathcal{F} = (P_k(X))_{k=2}^n$.

La famille $\mathcal{F}$ est définie par $P_k(X) = X^k - \frac{2k}{k+1}X + \frac{k-1}{k+1}$ pour $k \in \{2, \dots, n\}$.

#### 3.a. Vérifier que chaque polynôme $P_k(X)$ appartient à $E$.

Pour que $P_k(X)$ appartienne à $E$, il doit satisfaire les deux conditions : $P_k(1)=0$ et $\int_0^1 P_k(x) dx = 0$.

1.  **Vérification de $P_k(1)=0$ :**
    Nous substituons $X=1$ dans l'expression de $P_k(X)$ :
    $P_k(1) = (1)^k - \frac{2k}{k+1}(1) + \frac{k-1}{k+1}$
    $P_k(1) = 1 - \frac{2k}{k+1} + \frac{k-1}{k+1}$
    Pour additionner ces termes, nous les mettons sur le même dénominateur $k+1$ :
    $P_k(1) = \frac{k+1}{k+1} - \frac{2k}{k+1} + \frac{k-1}{k+1}$
    $P_k(1) = \frac{(k+1) - 2k + (k-1)}{k+1}$
    $P_k(1) = \frac{k+1-2k+k-1}{k+1}$
    $P_k(1) = \frac{(k+k-2k) + (1-1)}{k+1}$
    $P_k(1) = \frac{0+0}{k+1}$
    $P_k(1) = 0$.
    La première condition est satisfaite pour tous les $P_k(X)$.

2.  **Vérification de $\int_0^1 P_k(x) dx = 0$ :**
    Nous calculons l'intégrale de $P_k(X)$ de $0$ à $1$ :
    $\int_0^1 P_k(x) dx = \int_0^1 \left( x^k - \frac{2k}{k+1}x + \frac{k-1}{k+1} \right) dx$
    Nous utilisons la linéarité de l'intégrale et la formule $\int x^m dx = \frac{x^{m+1}}{m+1}$ :
    $\int_0^1 P_k(x) dx = \left[ \frac{x^{k+1}}{k+1} - \frac{2k}{k+1} \frac{x^2}{2} + \frac{k-1}{k+1} x \right]_0^1$
    Nous évaluons cette expression entre $0$ et $1$. L'évaluation en $0$ donne $0$ pour tous les termes.
    $\int_0^1 P_k(x) dx = \left( \frac{1^{k+1}}{k+1} - \frac{2k}{k+1} \frac{1^2}{2} + \frac{k-1}{k+1} (1) \right) - (0)$
    $\int_0^1 P_k(x) dx = \frac{1}{k+1} - \frac{k}{k+1} + \frac{k-1}{k+1}$
    Nous additionnons ces termes qui ont déjà le même dénominateur $k+1$ :
    $\int_0^1 P_k(x) dx = \frac{1 - k + (k-1)}{k+1}$
    $\int_0^1 P_k(x) dx = \frac{1 - k + k - 1}{k+1}$
    $\int_0^1 P_k(x) dx = \frac{(1-1) + (-k+k)}{k+1}$
    $\int_0^1 P_k(x) dx = \frac{0+0}{k+1}$
    $\int_0^1 P_k(x) dx = 0$.
    La deuxième condition est satisfaite pour tous les $P_k(X)$.

Puisque les deux conditions sont satisfaites pour chaque $P_k(X)$, nous avons bien $P_k(X) \in E$ pour tout $k \in \{2, \dots, n\}$.

#### 3.b. Démontrer que la famille $\mathcal{F}$ est une famille libre dans $E$.

Pour démontrer que la famille $\mathcal{F} = (P_k(X))_{k=2}^n$ est libre, nous devons montrer que toute combinaison linéaire nulle de ces polynômes implique que tous les coefficients de la combinaison linéaire sont nuls.
Soient $\alpha_2, \alpha_3, \dots, \alpha_n$ des scalaires de $\mathbb{K}$ tels que :
$$ \sum_{k=2}^n \alpha_k P_k(X) = 0_{\mathbb{K}_n[X]} $$
Nous substituons l'expression de $P_k(X)$ :
$$ \sum_{k=2}^n \alpha_k \left( X^k - \frac{2k}{k+1}X + \frac{k-1}{k+1} \right) = 0 $$
Nous développons cette somme :
$$ \sum_{k=2}^n \alpha_k X^k - \sum_{k=2}^n \alpha_k \frac{2k}{k+1}X + \sum_{k=2}^n \alpha_k \frac{k-1}{k+1} = 0 $$
Nous regroupons les termes par puissance de $X$ :
$$ \alpha_n X^n + \alpha_{n-1} X^{n-1} + \dots + \alpha_2 X^2 + \left( - \sum_{k=2}^n \alpha_k \frac{2k}{k+1} \right) X + \left( \sum_{k=2}^n \alpha_k \frac{k-1}{k+1} \right) = 0 $$
Cette équation est une égalité de polynômes. Par définition, un polynôme est nul si et seulement si tous ses coefficients sont nuls.
En examinant les coefficients des puissances de $X$ :
*   Le coefficient de $X^n$ est $\alpha_n$. Pour que le polynôme soit nul, $\alpha_n$ doit être nul.
*   Le coefficient de $X^{n-1}$ est $\alpha_{n-1}$. Pour que le polynôme soit nul, $\alpha_{n-1}$ doit être nul.
*   ...
*   Le coefficient de $X^2$ est $\alpha_2$. Pour que le polynôme soit nul, $\alpha_2$ doit être nul.

Ainsi, nous avons $\alpha_k = 0$ pour tout $k \in \{2, \dots, n\}$.
Les coefficients des termes en $X$ et les termes constants sont alors automatiquement nuls si tous les $\alpha_k$ sont nuls.
Par exemple, le coefficient de $X$ est $- \sum_{k=2}^n \alpha_k \frac{2k}{k+1}$. Si tous les $\alpha_k=0$, cette somme est $0$.
De même, le terme constant est $\sum_{k=2}^n \alpha_k \frac{k-1}{k+1}$. Si tous les $\alpha_k=0$, cette somme est $0$.

Puisque la seule combinaison linéaire de polynômes de $\mathcal{F}$ qui est égale au polynôme nul est celle où tous les coefficients sont nuls, la famille $\mathcal{F}$ est une famille libre dans $E$.

#### 3.c. Démontrer que la famille $\mathcal{F}$ est une famille génératrice de $E$.

Nous avons déterminé à la question 2 que la dimension de $E$ est $\dim(E) = n-1$.
La famille $\mathcal{F} = (P_k(X))_{k=2}^n$ contient des polynômes indexés de $k=2$ à $k=n$.
Le nombre d'éléments dans la famille $\mathcal{F}$ est $n - 2 + 1 = n-1$.

Nous avons donc une famille $\mathcal{F}$ qui :
1.  Est composée de $n-1$ polynômes.
2.  Chacun de ces polynômes appartient à $E$ (démontré en 3.a).
3.  Est une famille libre dans $E$ (démontré en 3.b).
4.  Le nombre d'éléments de $\mathcal{F}$ est égal à la dimension de $E$.

Dans un espace vectoriel de dimension finie, toute famille libre dont le nombre d'éléments est égal à la dimension de l'espace est automatiquement une famille génératrice de cet espace.
Par conséquent, la famille $\mathcal{F}$ est une famille génératrice de $E$.

#### 3.d. En déduire que $\mathcal{F}$ est une base de $E$.

Une base d'un espace vectoriel est une famille qui est à la fois libre et génératrice de cet espace.
*   Nous avons démontré en 3.b que $\mathcal{F}$ est une famille libre dans $E$.
*   Nous avons démontré en 3.c que $\mathcal{F}$ est une famille génératrice de $E$.

Puisque la famille $\mathcal{F}$ est à la fois libre et génératrice de $E$, nous pouvons en déduire que $\mathcal{F}$ est une base de $E$.
