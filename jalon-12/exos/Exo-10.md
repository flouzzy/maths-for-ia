# Exercice 10 (5 $\star$) : Opérateur de Cohérence Sémantique et Dualité dans les Espaces de Plongement

## Énoncé
Soit $(V, \langle \cdot, \cdot \rangle)$ un espace vectoriel euclidien de dimension finie $n \ge 1$. Soit $U = \{u_1, \dots, u_k\}$ un ensemble de $k$ vecteurs non nuls de $V$, représentant des "concepts sémantiques" ou des "points d'intérêt" dans un espace de plongement. On suppose, sans perte de généralité, que les vecteurs sont normalisés, c'est-à-dire $\|u_i\| = 1$ pour tout $i \in \{1, \dots, k\}$.

On définit l'opérateur linéaire $T: V \to V$ par :
$$ T(x) = \sum_{i=1}^k \langle x, u_i \rangle u_i $$
Cet opérateur modélise la "cohérence sémantique" d'un vecteur $x$ par rapport à l'ensemble $U$.

1.  Démontrer que $T$ est un opérateur auto-adjoint.
2.  Caractériser le noyau $\text{Ker}(T)$ et l'image $\text{Im}(T)$ de $T$. Montrer que $\text{Im}(T) = \text{span}(u_1, \dots, u_k)$.
3.  Soit $q \in V$ un vecteur non nul. On définit la "mesure de cohérence sémantique" de $q$ par rapport à $U$ comme $C(q) = \frac{\langle q, Tq \rangle}{\|q\|^2}$.
    a.  Montrer que $C(q) = \sum_{i=1}^k \left( \frac{\langle q, u_i \rangle}{\|q\|} \right)^2$. Interpréter cette quantité en termes de similarité cosinus.
    b.  Démontrer que les valeurs propres de $T$ sont réelles et que $0 \le \lambda \le k$ pour toute valeur propre $\lambda$ de $T$.
    c.  Montrer que le maximum de $C(q)$ sur $V \setminus \{0\}$ est la plus grande valeur propre de $T$. Caractériser les vecteurs $q$ qui atteignent ce maximum.
4.  Soit $V^*$ le dual de $V$. On rappelle que l'application de Riesz $\Phi: V \to V^*$ définie par $\Phi(y)(x) = \langle x, y \rangle$ est un isomorphisme d'espaces vectoriels.
    a.  Pour chaque $u_j \in U$, on définit la forme linéaire $f_j = \Phi(u_j) \in V^*$. Montrer que $f_j(x) = \langle x, u_j \rangle$.
    b.  On définit l'opérateur $T^*: V^* \to V^*$ par $T^*(f)(x) = f(T(x))$ pour tout $f \in V^*$ et $x \in V$. Montrer que $T^*$ est l'opérateur adjoint de $T$ au sens de la dualité.
    c.  Exprimer $T^*(f_j)$ en fonction des $f_i$ et des coefficients de la matrice de Gram $G_{ij} = \langle u_i, u_j \rangle$.
    d.  Montrer que $T^*$ est auto-adjoint par rapport à la forme bilinéaire canonique sur $V^* \times V^*$ définie par $\langle f, g \rangle_{V^*} = \langle \Phi^{-1}(f), \Phi^{-1}(g) \rangle_V$.
    e.  Relier les valeurs propres et les vecteurs propres de $T^*$ à ceux de $T$.


### Concentration de la Mesure en Haute Dimension
Dans le cas où $d \to \infty$, le phénomène de concentration de la mesure stipule que deux vecteurs aléatoires générés uniformément sur la sphère unité $\mathbb{S}^{d-1}$ seront presque orthogonaux avec une très forte probabilité. La similarité cosinus espérée tendra vers 0, ce qui a des implications profondes pour la malédiction de la dimension dans les réseaux de neurones.

## Correction Détaillée
### Analyse et Stratégie
Cet exercice explore les propriétés d'un opérateur linéaire défini à partir d'un ensemble de vecteurs dans un espace euclidien, en le reliant aux concepts de cohérence sémantique, de similarité cosinus et de dualité. La difficulté réside dans la rigueur des démonstrations et la manipulation des concepts abstraits de l'algèbre linéaire avancée.

La première partie (question 1 et 2) se concentre sur les propriétés fondamentales de l'opérateur $T$: son auto-adjonction, son noyau et son image. L'auto-adjonction est cruciale car elle garantit la réalité des valeurs propres et l'existence d'une base orthonormée de vecteurs propres, simplifiant l'analyse spectrale. La caractérisation du noyau et de l'image permet de comprendre la structure de l'opérateur et sa relation avec le sous-espace engendré par les vecteurs $u_i$.

La deuxième partie (question 3) introduit une mesure de cohérence sémantique, qui est une forme quadratique associée à $T$. L'analyse de cette forme quadratique nous mènera naturellement aux valeurs propres de $T$. Le théorème variationnel de Rayleigh-Ritz sera implicitement utilisé pour relier le maximum de cette mesure à la plus grande valeur propre. L'interprétation en termes de similarité cosinus est directe et fondamentale pour le contexte de la recherche sémantique.

La troisième partie (question 4) aborde la dualité. Nous utiliserons l'isomorphisme de Riesz pour relier l'espace $V$ à son dual $V^*$. Nous définirons l'opérateur adjoint $T^*$ sur $V^*$ et étudierons ses propriétés, notamment son auto-adjonction par rapport à la forme bilinéaire induite sur $V^*$. Enfin, nous établirons la correspondance entre les valeurs propres et vecteurs propres de $T$ et $T^*$, démontrant ainsi une symétrie fondamentale entre l'opérateur et son dual.

### Résolution Pas-à-Pas

1.  **Démontrer que $T$ est un opérateur auto-adjoint.**
    Un opérateur $T: V \to V$ est auto-adjoint si $\langle T(x), y \rangle = \langle x, T(y) \rangle$ pour tous $x, y \in V$.
    Calculons $\langle T(x), y \rangle$:
    $$ \langle T(x), y \rangle = \left\langle \sum_{i=1}^k \langle x, u_i \rangle u_i, y \right\rangle $$
    Par la linéarité du produit scalaire par rapport à sa première composante (pour des scalaires réels) :
    $$ \langle T(x), y \rangle = \sum_{i=1}^k \langle x, u_i \rangle \langle u_i, y \rangle $$
    Maintenant, calculons $\langle x, T(y) \rangle$:
    $$ \langle x, T(y) \rangle = \left\langle x, \sum_{j=1}^k \langle y, u_j \rangle u_j \right\rangle $$
    Par la linéarité du produit scalaire par rapport à sa seconde composante (pour des scalaires réels) :
    $$ \langle x, T(y) \rangle = \sum_{j=1}^k \langle y, u_j \rangle \langle x, u_j \rangle $$
    Puisque le produit scalaire est symétrique dans un espace euclidien (réel), $\langle y, u_j \rangle = \langle u_j, y \rangle$.
    $$ \langle x, T(y) \rangle = \sum_{j=1}^k \langle u_j, y \rangle \langle x, u_j \rangle $$
    En réordonnant les termes et en changeant l'indice de sommation de $j$ à $i$ (ce qui est permis car c'est un indice muet) :
    $$ \langle x, T(y) \rangle = \sum_{i=1}^k \langle x, u_i \rangle \langle u_i, y \rangle $$
    Nous avons donc $\langle T(x), y \rangle = \langle x, T(y) \rangle$ pour tous $x, y \in V$.
    Par conséquent, $T$ est un opérateur auto-adjoint.

2.  **Caractériser le noyau $\text{Ker}(T)$ et l'image $\text{Im}(T)$ de $T$. Montrer que $\text{Im}(T) = \text{span}(u_1, \dots, u_k)$.**
    *   **Caractérisation de $\text{Ker}(T)$:**
        Un vecteur $x \in V$ appartient au noyau de $T$, noté $\text{Ker}(T)$, si et seulement si $T(x) = 0_V$.
        $$ T(x) = \sum_{i=1}^k \langle x, u_i \rangle u_i = 0_V $$
        Prenons le produit scalaire de cette équation avec $x$:
        $$ \left\langle \sum_{i=1}^k \langle x, u_i \rangle u_i, x \right\rangle = \langle 0_V, x \rangle $$
        Par linéarité du produit scalaire :
        $$ \sum_{i=1}^k \langle x, u_i \rangle \langle u_i, x \rangle = 0 $$
        Puisque $\langle u_i, x \rangle = \langle x, u_i \rangle$ (symétrie du produit scalaire) :
        $$ \sum_{i=1}^k (\langle x, u_i \rangle)^2 = 0 $$
        Chaque terme $(\langle x, u_i \rangle)^2$ est le carré d'un nombre réel, donc il est non négatif. La somme de termes non négatifs est nulle si et seulement si chaque terme est nul.
        $$ (\langle x, u_i \rangle)^2 = 0 \quad \text{pour tout } i \in \{1, \dots, k\} $$
        Ceci implique $\langle x, u_i \rangle = 0$ pour tout $i \in \{1, \dots, k\}$.
        Donc, $x \in \text{Ker}(T)$ si et seulement si $x$ est orthogonal à tous les vecteurs $u_i$.
        Ceci signifie que $x$ appartient à l'orthogonal du sous-espace engendré par l'ensemble $U$.
        Soit $L = \text{span}(u_1, \dots, u_k)$. Alors $\text{Ker}(T) = L^\perp$.

    *   **Caractérisation de $\text{Im}(T)$:**
        L'image de $T$, notée $\text{Im}(T)$, est l'ensemble des vecteurs $y \in V$ tels que $y = T(x)$ pour un certain $x \in V$.
        Par définition de $T(x)$:
        $$ y = T(x) = \sum_{i=1}^k \langle x, u_i \rangle u_i $$
        Cette expression montre que tout vecteur $y$ dans l'image de $T$ est une combinaison linéaire des vecteurs $u_1, \dots, u_k$ (avec les coefficients $\langle x, u_i \rangle$).
        Par conséquent, $\text{Im}(T) \subseteq \text{span}(u_1, \dots, u_k)$.
        Soit $L = \text{span}(u_1, \dots, u_k)$. Nous avons donc $\text{Im}(T) \subseteq L$.

        Puisque $T$ est un opérateur linéaire sur un espace euclidien de dimension finie, et $T$ est auto-adjoint (démontré en question 1), nous savons que $\text{Im}(T) = (\text{Ker}(T))^\perp$.
        En utilisant notre résultat pour $\text{Ker}(T)$:
        $$ \text{Im}(T) = (L^\perp)^\perp $$
        Dans un espace euclidien de dimension finie, pour tout sous-espace $L$, l'orthogonal de l'orthogonal de $L$ est $L$ lui-même, c'est-à-dire $(L^\perp)^\perp = L$.
        Donc, $\text{Im}(T) = L = \text{span}(u_1, \dots, u_k)$.

3.  **Soit $q \in V$ un vecteur non nul. On définit la "mesure de cohérence sémantique" de $q$ par rapport à $U$ comme $C(q) = \frac{\langle q, Tq \rangle}{\|q\|^2}$.**
    a.  **Montrer que $C(q) = \sum_{i=1}^k \left( \frac{\langle q, u_i \rangle}{\|q\|} \right)^2$. Interpréter cette quantité en termes de similarité cosinus.**
        Par définition de $T$:
        $$ \langle q, Tq \rangle = \left\langle q, \sum_{i=1}^k \langle q, u_i \rangle u_i \right\rangle $$
        Par la linéarité du produit scalaire par rapport à sa seconde composante :
        $$ \langle q, Tq \rangle = \sum_{i=1}^k \langle q, u_i \rangle \langle q, u_i \rangle = \sum_{i=1}^k (\langle q, u_i \rangle)^2 $$
        En substituant cette expression dans la définition de $C(q)$:
        $$ C(q) = \frac{\sum_{i=1}^k (\langle q, u_i \rangle)^2}{\|q\|^2} $$
        Nous pouvons réécrire chaque terme de la somme en divisant par $\|q\|^2$:
        $$ C(q) = \sum_{i=1}^k \frac{(\langle q, u_i \rangle)^2}{\|q\|^2} = \sum_{i=1}^k \left( \frac{\langle q, u_i \rangle}{\|q\|} \right)^2 $$
        Interprétation en termes de similarité cosinus :
        La similarité cosinus entre deux vecteurs non nuls $a$ et $b$ est définie par $\cos(\theta(a, b)) = \frac{\langle a, b \rangle}{\|a\| \|b\|}$.
        Dans notre cas, les vecteurs $u_i$ sont normalisés, c'est-à-dire $\|u_i\|=1$.
        Ainsi, la similarité cosinus entre $q$ et $u_i$ est $\cos(\theta(q, u_i)) = \frac{\langle q, u_i \rangle}{\|q\| \|u_i\|} = \frac{\langle q, u_i \rangle}{\|q\|}$.
        Par conséquent, $C(q) = \sum_{i=1}^k (\cos(\theta(q, u_i)))^2$.
        Cette quantité représente la somme des carrés des similarités cosinus entre le vecteur de requête $q$ et chacun des vecteurs de concept sémantique $u_i$. Une valeur élevée de $C(q)$ indique que $q$ est "cohérent" ou "pertinent" par rapport à l'ensemble des concepts $U$, car il a une forte similarité avec plusieurs d'entre eux.

    b.  **Démontrer que les valeurs propres de $T$ sont réelles et que $0 \le \lambda \le k$ pour toute valeur propre $\lambda$ de $T$.**
        Puisque $T$ est un opérateur auto-adjoint sur un espace euclidien (réel) de dimension finie (démontré en question 1), toutes ses valeurs propres sont nécessairement réelles. C'est un théorème fondamental de la théorie spectrale des opérateurs auto-adjoints.

        Soit $\lambda$ une valeur propre de $T$ et $q$ un vecteur propre associé, avec $q \neq 0_V$.
        Par définition, $T(q) = \lambda q$.
        En utilisant la définition de $C(q)$:
        $$ C(q) = \frac{\langle q, Tq \rangle}{\|q\|^2} = \frac{\langle q, \lambda q \rangle}{\|q\|^2} $$
        Par la propriété de linéarité du produit scalaire par rapport à sa seconde composante :
        $$ C(q) = \frac{\lambda \langle q, q \rangle}{\|q\|^2} = \frac{\lambda \|q\|^2}{\|q\|^2} = \lambda $$
        D'après la question 3.a, nous savons que $C(q) = \sum_{i=1}^k \left( \frac{\langle q, u_i \rangle}{\|q\|} \right)^2$.
        Puisque chaque terme $\left( \frac{\langle q, u_i \rangle}{\|q\|} \right)^2$ est le carré d'un nombre réel, il est non négatif.
        La somme de termes non négatifs est non négative. Donc $C(q) \ge 0$.
        Par conséquent, $\lambda \ge 0$.

        Pour la borne supérieure, nous utilisons l'inégalité de Cauchy-Schwarz : pour tous $x, y \in V$, $|\langle x, y \rangle| \le \|x\| \|y\|$.
        Appliquons-la à $\langle q, u_i \rangle$: $|\langle q, u_i \rangle| \le \|q\| \|u_i\|$.
        Puisque $\|u_i\|=1$ par hypothèse, nous avons $|\langle q, u_i \rangle| \le \|q\|$.
        En élevant au carré : $(\langle q, u_i \rangle)^2 \le (\|q\|)^2$.
        En divisant par $\|q\|^2$ (qui est non nul car $q \neq 0_V$):
        $$ \left( \frac{\langle q, u_i \rangle}{\|q\|} \right)^2 \le 1 $$
        En sommant sur $i$ de $1$ à $k$:
        $$ C(q) = \sum_{i=1}^k \left( \frac{\langle q, u_i \rangle}{\|q\|} \right)^2 \le \sum_{i=1}^k 1 = k $$
        Puisque $\lambda = C(q)$, nous avons $\lambda \le k$.
        En combinant les deux inégalités, nous obtenons $0 \le \lambda \le k$ pour toute valeur propre $\lambda$ de $T$.

    c.  **Montrer que le maximum de $C(q)$ sur $V \setminus \{0\}$ est la plus grande valeur propre de $T$. Caractériser les vecteurs $q$ qui atteignent ce maximum.**
        La quantité $C(q) = \frac{\langle q, Tq \rangle}{\|q\|^2}$ est le quotient de Rayleigh de l'opérateur $T$.
        Pour un opérateur auto-adjoint $T$ sur un espace euclidien de dimension finie, le théorème variationnel de Rayleigh-Ritz stipule que le maximum du quotient de Rayleigh est égal à la plus grande valeur propre de $T$.
        Soit $\lambda_{\text{max}}$ la plus grande valeur propre de $T$.
        Alors $\max_{q \in V \setminus \{0\}} C(q) = \lambda_{\text{max}}$.

        Pour caractériser les vecteurs $q$ qui atteignent ce maximum, nous utilisons la décomposition spectrale.
        Puisque $T$ est auto-adjoint, il existe une base orthonormée de vecteurs propres $\{e_1, \dots, e_n\}$ de $V$ telle que $T(e_j) = \lambda_j e_j$ pour chaque $j \in \{1, \dots, n\}$. Nous pouvons ordonner les valeurs propres de manière décroissante : $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_n$. Ainsi, $\lambda_{\text{max}} = \lambda_1$.
        Tout vecteur $q \in V$ peut être écrit comme une combinaison linéaire de ces vecteurs propres : $q = \sum_{j=1}^n \alpha_j e_j$ pour des scalaires $\alpha_j \in \mathbb{R}$.
        Alors $\|q\|^2 = \langle q, q \rangle = \left\langle \sum_{j=1}^n \alpha_j e_j, \sum_{l=1}^n \alpha_l e_l \right\rangle$.
        Par bilinéarité du produit scalaire et orthonormalité de la base $\{e_j\}$ ($\langle e_j, e_l \rangle = \delta_{jl}$):
        $$ \|q\|^2 = \sum_{j=1}^n \sum_{l=1}^n \alpha_j \alpha_l \langle e_j, e_l \rangle = \sum_{j=1}^n \alpha_j^2 $$
        De même, $\langle q, Tq \rangle = \left\langle \sum_{j=1}^n \alpha_j e_j, T\left(\sum_{l=1}^n \alpha_l e_l\right) \right\rangle = \left\langle \sum_{j=1}^n \alpha_j e_j, \sum_{l=1}^n \alpha_l \lambda_l e_l \right\rangle$.
        $$ \langle q, Tq \rangle = \sum_{j=1}^n \sum_{l=1}^n \alpha_j \alpha_l \lambda_l \langle e_j, e_l \rangle = \sum_{j=1}^n \alpha_j^2 \lambda_j $$
        Donc, le quotient de Rayleigh est :
        $$ C(q) = \frac{\sum_{j=1}^n \alpha_j^2 \lambda_j}{\sum_{j=1}^n \alpha_j^2} $$
        Puisque $\lambda_j \le \lambda_1$ pour tout $j \in \{1, \dots, n\}$:
        $$ \sum_{j=1}^n \alpha_j^2 \lambda_j \le \sum_{j=1}^n \alpha_j^2 \lambda_1 = \lambda_1 \sum_{j=1}^n \alpha_j^2 $$
        Ainsi, $C(q) \le \frac{\lambda_1 \sum_{j=1}^n \alpha_j^2}{\sum_{j=1}^n \alpha_j^2} = \lambda_1$.
        Le maximum de $C(q)$ est donc $\lambda_1 = \lambda_{\text{max}}$.

        Ce maximum est atteint lorsque l'égalité $\sum_{j=1}^n \alpha_j^2 \lambda_j = \lambda_1 \sum_{j=1}^n \alpha_j^2$ est vérifiée.
        Ceci est équivalent à $\sum_{j=1}^n \alpha_j^2 (\lambda_1 - \lambda_j) = 0$.
        Puisque $\lambda_1 - \lambda_j \ge 0$ et $\alpha_j^2 \ge 0$ pour tout $j$, cette somme est nulle si et seulement si chaque terme est nul : $\alpha_j^2 (\lambda_1 - \lambda_j) = 0$ pour tout $j$.
        Cela signifie que si $\lambda_j < \lambda_1$, alors $\alpha_j$ doit être nul.
        Par conséquent, $q$ doit être une combinaison linéaire des vecteurs propres associés à la valeur propre $\lambda_1$.
        Autrement dit, $q$ doit appartenir au sous-espace propre $E_{\lambda_1} = \text{Ker}(T - \lambda_1 I)$.
        Les vecteurs $q$ qui atteignent ce maximum sont les vecteurs propres non nuls de $T$ associés à la plus grande valeur propre $\lambda_{\text{max}}$.

4.  **Soit $V^*$ le dual de $V$. On rappelle que l'application de Riesz $\Phi: V \to V^*$ définie par $\Phi(y)(x) = \langle x, y \rangle$ est un isomorphisme d'espaces vectoriels.**
    a.  **Pour chaque $u_j \in U$, on définit la forme linéaire $f_j = \Phi(u_j) \in V^*$. Montrer que $f_j(x) = \langle x, u_j \rangle$.**
        Par définition de l'application de Riesz $\Phi$, pour tout vecteur $y \in V$, $\Phi(y)$ est la forme linéaire dans $V^*$ qui, appliquée à un vecteur $x \in V$, donne le produit scalaire $\langle x, y \rangle$.
        En remplaçant $y$ par $u_j$, nous obtenons la forme linéaire $f_j = \Phi(u_j)$.
        Donc, pour tout $x \in V$:
        $$ f_j(x) = \Phi(u_j)(x) = \langle x, u_j \rangle $$
        Ceci est la relation demandée.

    b.  **On définit l'opérateur $T^*: V^* \to V^*$ par $T^*(f)(x) = f(T(x))$ pour tout $f \in V^*$ et $x \in V$. Montrer que $T^*$ est l'opérateur adjoint de $T$ au sens de la dualité.**
        L'opérateur adjoint (ou transposé) d'un opérateur linéaire $T: V \to V$ est traditionnellement noté $T^t$ ou $T^*$. Il est défini comme l'opérateur $T^*: V^* \to V^*$ tel que pour tout $f \in V^*$ et tout $x \in V$, l'évaluation de la forme linéaire $T^*(f)$ sur $x$ est égale à l'évaluation de la forme linéaire $f$ sur le vecteur $T(x)$.
        La définition donnée dans l'énoncé, $(T^*(f))(x) = f(T(x))$, correspond précisément à cette définition standard de l'opérateur transposé (ou adjoint dual) de $T$.
        Par conséquent, $T^*$ est bien l'opérateur adjoint de $T$ au sens de la dualité.

    c.  **Exprimer $T^*(f_j)$ en fonction des $f_i$ et des coefficients de la matrice de Gram $G_{ij} = \langle u_i, u_j \rangle$.**
        Nous voulons exprimer la forme linéaire $T^*(f_j)$. Par définition de $T^*$:
        $$ (T^*(f_j))(x) = f_j(T(x)) \quad \text{pour tout } x \in V $$
        Substituons l'expression de $T(x)$ :
        $$ (T^*(f_j))(x) = f_j\left( \sum_{i=1}^k \langle x, u_i \rangle u_i \right) $$
        Puisque $f_j$ est une forme linéaire, elle est linéaire. Nous pouvons sortir la somme et les scalaires $\langle x, u_i \rangle$:
        $$ (T^*(f_j))(x) = \sum_{i=1}^k \langle x, u_i \rangle f_j(u_i) $$
        D'après la question 4.a, $f_j(u_i) = \langle u_i, u_j \rangle$.
        Nous reconnaissons $\langle u_i, u_j \rangle$ comme le coefficient $G_{ij}$ de la matrice de Gram $G$.
        $$ (T^*(f_j))(x) = \sum_{i=1}^k \langle x, u_i \rangle G_{ij} $$
        Nous savons également que $\langle x, u_i \rangle = f_i(x)$ d'après la question 4.a.
        $$ (T^*(f_j))(x) = \sum_{i=1}^k G_{ij} f_i(x) $$
        Puisque cette égalité est vraie pour tout $x \in V$, les formes linéaires sont égales :
        $$ T^*(f_j) = \sum_{i=1}^k G_{ij} f_i $$
        Ceci exprime $T^*(f_j)$ comme une combinaison linéaire des formes linéaires $f_i$, où les coefficients sont les éléments de la $j$-ième colonne de la matrice de Gram $G$.

    d.  **Montrer que $T^*$ est auto-adjoint par rapport à la forme bilinéaire canonique sur $V^* \times V^*$ définie par $\langle f, g \rangle_{V^*} = \langle \Phi^{-1}(f), \Phi^{-1}(g) \rangle_V$.**
        Pour montrer que $T^*$ est auto-adjoint par rapport à la forme bilinéaire $\langle \cdot, \cdot \rangle_{V^*}$, nous devons montrer que $\langle T^*(f), g \rangle_{V^*} = \langle f, T^*(g) \rangle_{V^*}$ pour tous $f, g \in V^*$.
        Soient $y_f = \Phi^{-1}(f)$ et $y_g = \Phi^{-1}(g)$. Puisque $\Phi$ est un isomorphisme, $y_f$ et $y_g$ sont des vecteurs uniques dans $V$.
        Par définition de $\Phi$, nous avons $f(x) = \langle x, y_f \rangle$ et $g(x) = \langle x, y_g \rangle$ pour tout $x \in V$.

        Calculons le membre de gauche de l'égalité à démontrer :
        $$ \langle T^*(f), g \rangle_{V^*} = \langle \Phi^{-1}(T^*(f)), \Phi^{-1}(g) \rangle_V $$
        Nous devons d'abord exprimer $\Phi^{-1}(T^*(f))$.
        Par définition de $T^*(f)$, $(T^*(f))(x) = f(T(x))$.
        En utilisant l'expression de $f(x) = \langle x, y_f \rangle$:
        $$ (T^*(f))(x) = \langle T(x), y_f \rangle $$
        Puisque $T$ est auto-adjoint (démontré en question 1), nous avons $\langle T(x), y_f \rangle = \langle x, T(y_f) \rangle$.
        Donc, $(T^*(f))(x) = \langle x, T(y_f) \rangle$.
        Par définition de l'application de Riesz $\Phi$, la forme linéaire $x \mapsto \langle x, T(y_f) \rangle$ est précisément $\Phi(T(y_f))$.
        Ainsi, $T^*(f) = \Phi(T(y_f))$.
        En appliquant l'isomorphisme inverse $\Phi^{-1}$ des deux côtés :
        $$ \Phi^{-1}(T^*(f)) = T(y_f) $$
        En substituant $y_f = \Phi^{-1}(f)$, nous obtenons :
        $$ \Phi^{-1}(T^*(f)) = T(\Phi^{-1}(f)) $$
        Maintenant, nous pouvons reprendre le calcul du membre de gauche :
        $$ \langle T^*(f), g \rangle_{V^*} = \langle T(\Phi^{-1}(f)), \Phi^{-1}(g) \rangle_V $$
        Puisque $T$ est auto-adjoint sur $V$, nous pouvons échanger les arguments du produit scalaire en appliquant $T$ à l'autre argument :
        $$ \langle T(\Phi^{-1}(f)), \Phi^{-1}(g) \rangle_V = \langle \Phi^{-1}(f), T(\Phi^{-1}(g)) \rangle_V $$
        En utilisant le même raisonnement que précédemment, $T(\Phi^{-1}(g)) = \Phi^{-1}(T^*(g))$.
        $$ \langle \Phi^{-1}(f), T(\Phi^{-1}(g)) \rangle_V = \langle \Phi^{-1}(f), \Phi^{-1}(T^*(g)) \rangle_V $$
        Par définition de la forme bilinéaire sur $V^*$:
        $$ \langle \Phi^{-1}(f), \Phi^{-1}(T^*(g)) \rangle_V = \langle f, T^*(g) \rangle_{V^*} $$
        Nous avons donc montré que $\langle T^*(f), g \rangle_{V^*} = \langle f, T^*(g) \rangle_{V^*}$ pour tous $f, g \in V^*$.
        Par conséquent, $T^*$ est auto-adjoint par rapport à la forme bilinéaire canonique sur $V^*$.

    e.  **Relier les valeurs propres et les vecteurs propres de $T^*$ à ceux de $T$.**
        Soit $\lambda$ une valeur propre de $T$ et $q$ un vecteur propre associé, tel que $T(q) = \lambda q$ avec $q \neq 0_V$.
        Considérons la forme linéaire $f_q = \Phi(q) \in V^*$. Puisque $q \neq 0_V$ et $\Phi$ est un isomorphisme, $f_q$ est une forme linéaire non nulle dans $V^*$.
        Appliquons l'opérateur $T^*$ à $f_q$:
        $$ (T^*(f_q))(x) = f_q(T(x)) \quad \text{pour tout } x \in V $$
        En utilisant la définition de $f_q(y) = \langle y, q \rangle$:
        $$ (T^*(f_q))(x) = \langle T(x), q \rangle $$
        Puisque $T$ est auto-adjoint (démontré en question 1), $\langle T(x), q \rangle = \langle x, T(q) \rangle$.
        $$ (T^*(f_q))(x) = \langle x, T(q) \rangle $$
        Nous savons que $T(q) = \lambda q$ (car $q$ est un vecteur propre de $T$ associé à $\lambda$):
        $$ (T^*(f_q))(x) = \langle x, \lambda q \rangle $$
        Par linéarité du produit scalaire par rapport à sa seconde composante :
        $$ (T^*(f_q))(x) = \lambda \langle x, q \rangle $$
        Et nous reconnaissons $\langle x, q \rangle = f_q(x)$.
        $$ (T^*(f_q))(x) = \lambda f_q(x) $$
        Puisque cette égalité est vraie pour tout $x \in V$, les formes linéaires sont égales :
        $$ T^*(f_q) = \lambda f_q $$
        Ceci montre que si $\lambda$ est une valeur propre de $T$, alors $\lambda$ est aussi une valeur propre de $T^*$.
        De plus, si $q$ est un vecteur propre de $T$ associé à $\lambda$, alors $f_q = \Phi(q)$ est un vecteur propre de $T^*$ associé à la même valeur propre $\lambda$.

        Réciproquement, soit $\mu$ une valeur propre de $T^*$ et $f \in V^*$ un vecteur propre associé, tel que $T^*(f) = \mu f$ avec $f \neq 0_{V^*}$.
        Soit $y_f = \Phi^{-1}(f) \in V$. Puisque $f \neq 0_{V^*}$ et $\Phi^{-1}$ est un isomorphisme, $y_f$ est un vecteur non nul dans $V$.
        Nous avons montré en question 4.d que $\Phi^{-1}(T^*(f)) = T(\Phi^{-1}(f))$.
        Appliquons l'isomorphisme $\Phi^{-1}$ à l'équation $T^*(f) = \mu f$:
        $$ \Phi^{-1}(T^*(f)) = \Phi^{-1}(\mu f) $$
        Puisque $\Phi^{-1}$ est linéaire, $\Phi^{-1}(\mu f) = \mu \Phi^{-1}(f)$.
        $$ T(\Phi^{-1}(f)) = \mu \Phi^{-1}(f) $$
        En substituant $y_f = \Phi^{-1}(f)$:
        $$ T(y_f) = \mu y_f $$
        Ceci montre que si $\mu$ est une valeur propre de $T^*$, alors $\mu$ est aussi une valeur propre de $T$.
        De plus, si $f$ est un vecteur propre de $T^*$ associé à $\mu$, alors $y_f = \Phi^{-1}(f)$ est un vecteur propre de $T$ associé à la même valeur propre $\mu$.

        En conclusion, les opérateurs $T$ et $T^*$ ont le même ensemble de valeurs propres. De plus, l'isomorphisme de Riesz $\Phi$ établit une correspondance bijective entre les sous-espaces propres de $T$ et ceux de $T^*$: si $E_\lambda$ est le sous-espace propre de $T$ associé à la valeur propre $\lambda$, alors $\Phi(E_\lambda)$ est le sous-espace propre de $T^*$ associé à la même valeur propre $\lambda$.

### Conclusion
Nous avons rigoureusement analysé les propriétés d'un opérateur de cohérence sémantique $T$ défini sur un espace euclidien $V$. Nous avons établi que $T$ est auto-adjoint, ce qui garantit la réalité de ses valeurs propres et l'existence d'une base orthonormée de vecteurs propres. Son noyau est l'orthogonal du sous-espace engendré par les vecteurs de concept $u_i$, et son image est précisément ce sous-espace.

La mesure de cohérence sémantique $C(q)$ a été explicitée comme la somme des carrés des similarités cosinus entre une requête $q$ et les concepts $u_i$. Nous avons démontré que les valeurs propres de $T$ sont bornées entre $0$ et $k$, et que le maximum de $C(q)$ est la plus grande valeur propre de $T$, atteinte par les vecteurs propres associés. Cela fournit une méthode pour trouver les requêtes "les plus cohérentes" avec un ensemble de concepts.

Enfin, nous avons exploré la dualité en caractérisant l'opérateur transposé $T^*$ sur le dual $V^*$. Nous avons montré que $T^*$ est également auto-adjoint par rapport à la forme bilinéaire induite sur $V^*$. Une correspondance bijective a été établie entre les valeurs propres et les vecteurs propres de $T$ et $T^*$ via l'isomorphisme de Riesz, soulignant la symétrie fondamentale entre un opérateur et son dual dans un espace euclidien. Ces résultats fournissent un cadre théorique solide pour la compréhension et l'optimisation des mécanismes de recherche sémantique basés sur la similarité cosinus dans des espaces de plongement.
