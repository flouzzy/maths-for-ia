# Exercice 01 : Les Trois Joyaux de Banach

Chers étudiants,
Nous allons explorer ensemble les fondements de l'analyse fonctionnelle moderne. Cet exercice, le premier d'une série que j'espère stimulante, vous mettra au défi de démontrer les interconnexions profondes entre trois théorèmes capitaux : le Théorème de l'Application Ouverte, le Théorème de l'Isomorphisme de Banach et le Théorème du Graphe Fermé. Votre rigueur et votre capacité à construire des démonstrations complètes et sans faille seront mises à l'épreuve. N'oubliez pas : en mathématiques, chaque étape doit être justifiée.

Difficulté : $\bigstar\star\star\star\star$

---

## Énoncé

Soient $X$ et $Y$ des espaces de Banach sur le corps $\mathbb{K}$ (où $\mathbb{K}=\mathbb{R}$ ou $\mathbb{K}=\mathbb{C}$).

### Rappel fondamental : Le Théorème de Baire
Pour toute suite dénombrable $(F_n)_{n \in \mathbb{N}}$ de sous-ensemaces fermés d'un espace métrique complet $M$ telle que $M = \bigcup_{n \in \mathbb{N}} F_n$, il existe au moins un $n_0 \in \mathbb{N}$ tel que l'intérieur de $F_{n_0}$, noté $\operatorname{int}(F_{n_0})$, soit non vide.

### Partie I : Le Théorème de l'Application Ouverte (Banach-Schauder)

Soit $T: X \to Y$ un opérateur linéaire continu et surjectif. Le but de cette partie est de démontrer que $T$ est une application ouverte, c'est-à-dire que pour tout ouvert $U \subseteq X$, $T(U)$ est un ouvert de $Y$. Il est équivalent de montrer qu'il existe une constante $\delta > 0$ telle que la boule unité ouverte de $Y$, $B_Y(0, \delta)$, soit contenue dans l'image de la boule unité ouverte de $X$, $T(B_X(0, 1))$. Plus généralement, nous montrerons que $T$ envoie un voisinage de $0$ dans $X$ sur un voisinage de $0$ dans $Y$.

1.  Démontrer que pour tout $n \in \mathbb{N}^*$, la fermeture de l'image de la boule unité ouverte $B_X(0, n)$ sous $T$, notée $\overline{T(B_X(0, n))}$, n'est pas d'intérieur vide dans $Y$.
    (Indication : Utilisez le Théorème de Baire et la surjectivité de $T$.)

2.  Soit $n_0 \in \mathbb{N}^*$ tel que $\operatorname{int}(\overline{T(B_X(0, n_0))}) \neq \emptyset$. Montrer que $0 \in \operatorname{int}(\overline{T(B_X(0, 2n_0))})$.
    (Indication : Considérez $B_Y(y_0, r_0) \subseteq \overline{T(B_X(0, n_0))}$ et utilisez les propriétés de l'opérateur linéaire $T$.)

3.  Déduire des questions précédentes que pour tout $\delta > 0$, il existe $\epsilon > 0$ tel que $B_Y(0, \epsilon) \subseteq T(B_X(0, \delta))$.
    (Ceci est l'étape cruciale. Vous devrez construire une suite d'éléments de $X$.)

4.  Conclure que $T$ est une application ouverte.

### Partie II : Le Théorème de l'Isomorphisme de Banach

Soit $T: X \to Y$ un opérateur linéaire continu et bijectif entre deux espaces de Banach $X$ et $Y$.

1.  En utilisant les résultats de la Partie I, démontrer que l'opérateur inverse $T^{-1}: Y \to X$ est continu.

2.  Donner la définition formelle d'un isomorphisme de Banach.

### Partie III : Le Théorème du Graphe Fermé

Soient $X$ et $Y$ des espaces de Banach. Soit $T: X \to Y$ un opérateur linéaire. On définit le graphe de $T$ comme $G(T) = \{(x, T(x)) \mid x \in X\} \subseteq X \times Y$. On suppose que $G(T)$ est un sous-espace fermé de $X \times Y$.

1.  Démontrer que $X \times Y$ muni de la norme $\|(x, y)\|_{X \times Y} = \|x\|_X + \|y\|_Y$ est un espace de Banach.

2.  Considérer l'opérateur $P_1: G(T) \to X$ défini par $P_1(x, T(x)) = x$.
    Démontrer que $P_1$ est un opérateur linéaire continu et bijectif.

3.  Appliquer le Théorème de l'Isomorphisme de Banach (Partie II) à $P_1$ pour démontrer que $P_1^{-1}: X \to G(T)$ est continu.

4.  Considérer l'opérateur $P_2: G(T) \to Y$ défini par $P_2(x, T(x)) = T(x)$.
    Démontrer que $P_2$ est un opérateur linéaire continu.

5.  Déduire de ce qui précède que $T$ est un opérateur continu.

---

## Correction Détaillée

### Partie I : Le Théorème de l'Application Ouverte (Banach-Schauder)

1.  **Démontrer que pour tout $n \in \mathbb{N}^*$, la fermeture de l'image de la boule unité ouverte $B_X(0, n)$ sous $T$, notée $\overline{T(B_X(0, n))}$, n'est pas d'intérieur vide dans $Y$.**

    Soit $n \in \mathbb{N}^*$. Nous considérons les ensembles $F_n = \overline{T(B_X(0, n))}$. Ce sont des sous-ensembles fermés de $Y$ par définition de la fermeture.
    Puisque $T: X \to Y$ est surjectif, pour tout $y \in Y$, il existe un $x \in X$ tel que $T(x) = y$.
    De plus, pour tout $x \in X$ non nul, on peut trouver un entier $n \in \mathbb{N}^*$ tel que $x \in B_X(0, n)$. Par exemple, on peut prendre $n = \lceil \|x\|_X \rceil + 1$.
    Ainsi, $y = T(x) \in T(B_X(0, n))$.
    Par conséquent, $Y = \bigcup_{n=1}^\infty T(B_X(0, n))$.
    Comme $T(B_X(0, n)) \subseteq \overline{T(B_X(0, n))}$, nous avons $Y = \bigcup_{n=1}^\infty \overline{T(B_X(0, n))}$.
    $Y$ est un espace de Banach, donc un espace métrique complet.
    En vertu du Théorème de Baire, puisque $Y$ est la réunion dénombrable des fermés $\overline{T(B_X(0, n))}$, il doit exister un entier $n_0 \in \mathbb{N}^*$ tel que $\operatorname{int}(\overline{T(B_X(0, n_0))}) \neq \emptyset$.
    La question est formulée "pour tout $n \in \mathbb{N}^*$". Ceci est un peu abusif dans la formulation originale de l'énoncé. La bonne conclusion est qu'il existe *au moins un* $n_0$. La suite des questions exploitera ce $n_0$.

2.  **Soit $n_0 \in \mathbb{N}^*$ tel que $\operatorname{int}(\overline{T(B_X(0, n_0))}) \neq \emptyset$. Montrer que $0 \in \operatorname{int}(\overline{T(B_X(0, 2n_0))})$.**

    Soit $y_0 \in \operatorname{int}(\overline{T(B_X(0, n_0))})$. Par définition de l'intérieur, il existe un rayon $r_0 > 0$ tel que la boule ouverte $B_Y(y_0, r_0)$ est entièrement contenue dans $\overline{T(B_X(0, n_0))}$. C'est-à-dire, $B_Y(y_0, r_0) \subseteq \overline{T(B_X(0, n_0))}$.
    Considérons la boule $B_Y(0, r_0)$. Pour tout $y \in B_Y(0, r_0)$, nous pouvons écrire $y = (y+y_0) - y_0$.
    Puisque $\|y\|_Y < r_0$, $\|y+y_0 - y_0\|_Y < r_0$. L'élément $y+y_0$ appartient à $B_Y(y_0, r_0)$, et donc $y+y_0 \in \overline{T(B_X(0, n_0))}$.
    De plus, $y_0$ lui-même appartient à $\overline{T(B_X(0, n_0))}$.
    Donc, tout $y \in B_Y(0, r_0)$ peut s'écrire comme la différence de deux éléments de $\overline{T(B_X(0, n_0))}$.
    Plus formellement, $B_Y(0, r_0) = B_Y(y_0, r_0) - y_0$.
    Par conséquent, $B_Y(0, r_0) \subseteq \overline{T(B_X(0, n_0))} - y_0$.
    Puisque $y_0 \in \overline{T(B_X(0, n_0))}$, nous avons $B_Y(0, r_0) \subseteq \overline{T(B_X(0, n_0))} - \overline{T(B_X(0, n_0))}$.
    Par la linéarité de $T$, on a $T(A) - T(B) = T(A-B)$.
    De plus, pour des ensembles $A, B \subseteq X$, $\overline{T(A)} - \overline{T(B)} \subseteq \overline{T(A-B)}$.
    (Pour justifier $\overline{A} - \overline{B} \subseteq \overline{A-B}$: soient $a \in \overline{A}$ et $b \in \overline{B}$. Il existe des suites $(a_k) \subseteq A$ et $(b_k) \subseteq B$ telles que $a_k \to a$ et $b_k \to b$. Alors $a_k - b_k \in A-B$ et $a_k - b_k \to a-b$. Donc $a-b \in \overline{A-B}$.)
    Ainsi, $B_Y(0, r_0) \subseteq \overline{T(B_X(0, n_0) - B_X(0, n_0))}$.
    Il est facile de voir que $B_X(0, n_0) - B_X(0, n_0) = \{x_1 - x_2 \mid \|x_1\|_X < n_0, \|x_2\|_X < n_0\}$. Pour tout tel $x_1 - x_2$, $\|x_1 - x_2\|_X \le \|x_1\|_X + \|x_2\|_X < n_0 + n_0 = 2n_0$. Donc $B_X(0, n_0) - B_X(0, n_0) \subseteq B_X(0, 2n_0)$.
    Et réciproquement, pour tout $x \in B_X(0, 2n_0)$, on peut écrire $x = x_1 - x_2$ avec $x_1, x_2 \in B_X(0, n_0)$ (par exemple, $x_1 = x/2$ et $x_2 = -x/2$). Non, ceci n'est pas correct. $B_X(0, r) + B_X(0, s) = B_X(0, r+s)$. Donc $B_X(0, n_0) - B_X(0, n_0) = B_X(0, n_0) + B_X(0, n_0) = B_X(0, 2n_0)$.
    Par conséquent, $B_Y(0, r_0) \subseteq \overline{T(B_X(0, 2n_0))}$.
    Ceci implique directement que $0 \in \operatorname{int}(\overline{T(B_X(0, 2n_0))})$, puisque $B_Y(0, r_0)$ est un voisinage ouvert de $0$ contenu dans $\overline{T(B_X(0, 2n_0))}$.

3.  **Déduire des questions précédentes que pour tout $\delta > 0$, il existe $\epsilon > 0$ tel que $B_Y(0, \epsilon) \subseteq T(B_X(0, \delta))$.**

    D'après la question précédente, il existe un $n_0 \in \mathbb{N}^*$ et un $r_0 > 0$ tels que $B_Y(0, r_0) \subseteq \overline{T(B_X(0, 2n_0))}$.
    Pour simplifier, posons $r_0 = \epsilon_0$ et $R_0 = 2n_0$. Ainsi, nous avons $B_Y(0, \epsilon_0) \subseteq \overline{T(B_X(0, R_0))}$.
    Nous voulons montrer que $B_Y(0, \epsilon_1) \subseteq T(B_X(0, \delta))$ pour un certain $\epsilon_1 > 0$.
    Par propriété d'échelle (linéarité), pour tout $\alpha > 0$, $B_Y(0, \alpha \epsilon_0) \subseteq \overline{T(B_X(0, \alpha R_0))}$.
    Soit $y \in B_Y(0, \epsilon_0)$. Nous allons construire une suite $(x_k)_{k \in \mathbb{N}^*}$ dans $X$ telle que $\sum_{k=1}^\infty x_k$ converge vers un $x \in X$ avec $T(x)=y$, et telle que $\|x\|_X < \delta$.

    Puisque $y \in B_Y(0, \epsilon_0) \subseteq \overline{T(B_X(0, R_0))}$, il existe un $x_1 \in B_X(0, R_0)$ tel que $\|y - T(x_1)\|_Y < \epsilon_0/2$.
    Posons $y_1 = y - T(x_1)$. Alors $y_1 \in B_Y(0, \epsilon_0/2)$.
    En utilisant la propriété d'échelle, nous savons que $B_Y(0, \epsilon_0/2) \subseteq \overline{T(B_X(0, R_0/2))}$.
    Puisque $y_1 \in B_Y(0, \epsilon_0/2) \subseteq \overline{T(B_X(0, R_0/2))}$, il existe un $x_2 \in B_X(0, R_0/2)$ tel que $\|y_1 - T(x_2)\|_Y < \epsilon_0/4$.
    Posons $y_2 = y_1 - T(x_2)$. Alors $y_2 \in B_Y(0, \epsilon_0/4)$.
    Nous pouvons répéter ce processus indéfiniment. Nous construisons ainsi des suites $(x_k)_{k \in \mathbb{N}^*}$ et $(y_k)_{k \in \mathbb{N}}$ avec $y_0 = y$, telles que pour tout $k \ge 1$:
    1.  $y_k = y_{k-1} - T(x_k)$
    2.  $x_k \in B_X(0, R_0/2^{k-1})$
    3.  $\|y_k\|_Y < \epsilon_0/2^k$

    De la condition (2), nous avons $\|x_k\|_X < R_0/2^{k-1}$.
    Considérons la série $\sum_{k=1}^\infty x_k$. La série des normes est $\sum_{k=1}^\infty \|x_k\|_X < \sum_{k=1}^\infty R_0/2^{k-1} = R_0 \sum_{k=0}^\infty (1/2)^k = R_0 \cdot 2 = 2R_0$.
    Puisque $X$ est un espace de Banach (donc complet) et que la série $\sum_{k=1}^\infty \|x_k\|_X$ converge, la série $\sum_{k=1}^\infty x_k$ converge absolument dans $X$. Soit $x = \sum_{k=1}^\infty x_k$.
    Alors $\|x\|_X = \left\| \sum_{k=1}^\infty x_k \right\|_X \le \sum_{k=1}^\infty \|x_k\|_X < 2R_0$.
    Puisque $T$ est continu et linéaire, il est continu au sens séquentiel.
    $T(x) = T\left(\sum_{k=1}^\infty x_k\right) = \sum_{k=1}^\infty T(x_k)$.
    D'autre part, $y_k = y_{k-1} - T(x_k) = y - \sum_{i=1}^k T(x_i)$.
    Comme $\|y_k\|_Y < \epsilon_0/2^k$, nous avons $\lim_{k \to \infty} \|y_k\|_Y = 0$, donc $\lim_{k \to \infty} y_k = 0$.
    En passant à la limite dans $y_k = y - \sum_{i=1}^k T(x_i)$, nous obtenons $0 = y - \sum_{i=1}^\infty T(x_i)$.
    Donc $y = \sum_{i=1}^\infty T(x_i) = T(x)$.
    Nous avons ainsi montré que pour tout $y \in B_Y(0, \epsilon_0)$, il existe un $x \in B_X(0, 2R_0)$ (car $\|x\|_X < 2R_0$) tel que $T(x)=y$.
    Ceci signifie que $B_Y(0, \epsilon_0) \subseteq T(B_X(0, 2R_0))$.
    Maintenant, généralisons cela pour un $\delta > 0$ arbitraire.
    Nous avons $B_Y(0, \epsilon_0) \subseteq T(B_X(0, 2R_0))$.
    Par la linéarité de $T$, pour tout $c > 0$, $T(c B_X(0, 2R_0)) = c T(B_X(0, 2R_0))$.
    Et $c B_X(0, 2R_0) = B_X(0, c \cdot 2R_0)$.
    Donc, si nous prenons $x' = (c/ (2R_0))x$, alors $\|x'\|_X < c$.
    Si nous prenons $y' = (c/(2R_0))y$, alors $y' \in B_Y(0, c \epsilon_0 / (2R_0))$.
    Alors $T(x') = T((c/(2R_0))x) = (c/(2R_0)) T(x) = (c/(2R_0))y$.
    Ceci veut dire que $T(B_X(0, c)) \supseteq B_Y(0, c \epsilon_0 / (2R_0))$.
    Pour tout $\delta > 0$, en choisissant $c=\delta$, nous obtenons $B_Y(0, \delta \epsilon_0 / (2R_0)) \subseteq T(B_X(0, \delta))$.
    En posant $\epsilon = \delta \epsilon_0 / (2R_0)$, nous avons le résultat désiré : $B_Y(0, \epsilon) \subseteq T(B_X(0, \delta))$.

4.  **Conclure que $T$ est une application ouverte.**

    Pour démontrer que $T$ est une application ouverte, il faut montrer que pour tout ouvert $U \subseteq X$, $T(U)$ est un ouvert de $Y$.
    Soit $U$ un sous-ensemble ouvert de $X$. Soit $y_0 \in T(U)$. Par définition, il existe $x_0 \in U$ tel que $T(x_0) = y_0$.
    Puisque $U$ est ouvert, il existe un $\delta > 0$ tel que la boule ouverte $B_X(x_0, \delta)$ est entièrement contenue dans $U$.
    Nous avons montré à la question précédente qu'il existe un $\epsilon > 0$ (dépendant de $\delta$) tel que $B_Y(0, \epsilon) \subseteq T(B_X(0, \delta))$.
    Considérons $T(B_X(x_0, \delta))$.
    Par la linéarité de $T$, $T(B_X(x_0, \delta)) = T(x_0 + B_X(0, \delta)) = T(x_0) + T(B_X(0, \delta))$.
    Comme $y_0 = T(x_0)$ et $B_Y(0, \epsilon) \subseteq T(B_X(0, \delta))$, nous avons :
    $T(B_X(x_0, \delta)) \supseteq y_0 + B_Y(0, \epsilon) = B_Y(y_0, \epsilon)$.
    Ainsi, $T(U)$ contient le voisinage ouvert $B_Y(y_0, \epsilon)$ de $y_0$.
    Puisque ce raisonnement est valable pour tout $y_0 \in T(U)$, $T(U)$ est un ouvert de $Y$.
    Par conséquent, $T$ est une application ouverte.

### Partie II : Le Théorème de l'Isomorphisme de Banach

1.  **En utilisant les résultats de la Partie I, démontrer que l'opérateur inverse $T^{-1}: Y \to X$ est continu.**

    Soit $T: X \to Y$ un opérateur linéaire continu et bijectif entre deux espaces de Banach $X$ et $Y$.
    Puisque $T$ est bijectif, son inverse $T^{-1}: Y \to X$ existe et est également linéaire.
    Pour montrer que $T^{-1}$ est continu, il suffit de montrer que pour tout ouvert $U \subseteq X$, l'image réciproque $(T^{-1})^{-1}(U)$ est un ouvert de $Y$.
    Par définition, $(T^{-1})^{-1}(U) = \{y \in Y \mid T^{-1}(y) \in U\}$.
    Puisque $T^{-1}(y) \in U \iff y \in T(U)$ (par bijectivité), nous avons $(T^{-1})^{-1}(U) = T(U)$.
    Selon le Théorème de l'Application Ouverte (Partie I), puisque $T$ est un opérateur linéaire continu et surjectif entre espaces de Banach, $T$ est une application ouverte.
    Par conséquent, pour tout ouvert $U \subseteq X$, $T(U)$ est un ouvert de $Y$.
    Ainsi, $(T^{-1})^{-1}(U)$ est un ouvert de $Y$ pour tout ouvert $U \subseteq X$.
    Ceci démontre que l'opérateur $T^{-1}$ est continu.

2.  **Donner la définition formelle d'un isomorphisme de Banach.**

    Un opérateur linéaire $T: X \to Y$ entre deux espaces de Banach $X$ et $Y$ est appelé un isomorphisme de Banach si $T$ est bijectif, continu, et si son inverse $T^{-1}: Y \to X$ est également continu.
    Deux espaces de Banach $X$ et $Y$ sont dits isomorphes de Banach s'il existe un isomorphisme de Banach entre eux.
    Le Théorème de l'Isomorphisme de Banach (aussi connu sous le nom de Théorème de l'Application Ouverte pour les bijections) nous dit qu'un opérateur linéaire bijectif *continu* entre deux espaces de Banach a automatiquement un inverse continu, simplifiant ainsi la vérification pour la définition d'un isomorphisme.

### Partie III : Le Théorème du Graphe Fermé

1.  **Démontrer que $X \times Y$ muni de la norme $\|(x, y)\|_{X \times Y} = \|x\|_X + \|y\|_Y$ est un espace de Banach.**

    Soient $(x_n, y_n)_{n \in \mathbb{N}}$ une suite de Cauchy dans $X \times Y$.
    Par définition de la norme, pour tout $\epsilon > 0$, il existe $N \in \mathbb{N}$ tel que pour tous $m, n \ge N$:
    $\|(x_m, y_m) - (x_n, y_n)\|_{X \times Y} < \epsilon$.
    Ceci signifie $\|x_m - x_n\|_X + \|y_m - y_n\|_Y < \epsilon$.
    De cette inégalité, on déduit que $\|x_m - x_n\|_X < \epsilon$ et $\|y_m - y_n\|_Y < \epsilon$.
    Par conséquent, $(x_n)_{n \in \mathbb{N}}$ est une suite de Cauchy dans $X$, et $(y_n)_{n \in \mathbb{N}}$ est une suite de Cauchy dans $Y$.
    Puisque $X$ est un espace de Banach, il existe $x \in X$ tel que $x_n \to x$ (convergence en norme dans $X$).
    Puisque $Y$ est un espace de Banach, il existe $y \in Y$ tel que $y_n \to y$ (convergence en norme dans $Y$).
    Considérons la limite $(x, y) \in X \times Y$. Nous devons montrer que $(x_n, y_n) \to (x, y)$ en norme $X \times Y$.
    $\|(x_n, y_n) - (x, y)\|_{X \times Y} = \|x_n - x\|_X + \|y_n - y\|_Y$.
    Comme $x_n \to x$, $\|x_n - x\|_X \to 0$ quand $n \to \infty$.
    Comme $y_n \to y$, $\|y_n - y\|_Y \to 0$ quand $n \to \infty$.
    Donc, $\|x_n - x\|_X + \|y_n - y\|_Y \to 0$ quand $n \to \infty$.
    Ainsi, la suite de Cauchy $(x_n, y_n)$ converge vers $(x, y)$ dans $X \times Y$.
    Par conséquent, $X \times Y$ est un espace de Banach.

2.  **Considérer l'opérateur $P_1: G(T) \to X$ défini par $P_1(x, T(x)) = x$. Démontrer que $P_1$ est un opérateur linéaire continu et bijectif.**

    Le graphe $G(T)$ est un sous-espace vectoriel de $X \times Y$. Étant donné qu'il est fermé (par hypothèse) et que $X \times Y$ est un espace de Banach (démontré en Q1), $G(T)$ lui-même est un espace de Banach (un sous-espace fermé d'un espace complet est complet).

    *   **Linéarité de $P_1$ :** Soient $(x_1, T(x_1))$ et $(x_2, T(x_2))$ deux éléments de $G(T)$, et $\alpha, \beta \in \mathbb{K}$.
        $P_1(\alpha(x_1, T(x_1)) + \beta(x_2, T(x_2))) = P_1(\alpha x_1 + \beta x_2, \alpha T(x_1) + \beta T(x_2))$.
        Puisque $T$ est linéaire, $\alpha T(x_1) + \beta T(x_2) = T(\alpha x_1 + \beta x_2)$.
        Donc, $P_1(\alpha(x_1, T(x_1)) + \beta(x_2, T(x_2))) = P_1(\alpha x_1 + \beta x_2, T(\alpha x_1 + \beta x_2)) = \alpha x_1 + \beta x_2$.
        D'autre part, $\alpha P_1(x_1, T(x_1)) + \beta P_1(x_2, T(x_2)) = \alpha x_1 + \beta x_2$.
        Ainsi, $P_1$ est linéaire.

    *   **Continuité de $P_1$ :** Pour tout $(x, T(x)) \in G(T)$:
        $\|P_1(x, T(x))\|_X = \|x\|_X$.
        Nous comparons cela à la norme de l'élément dans $G(T)$: $\|(x, T(x))\|_{X \times Y} = \|x\|_X + \|T(x)\|_Y$.
        Clairement, $\|x\|_X \le \|x\|_X + \|T(x)\|_Y$.
        Donc $\|P_1(x, T(x))\|_X \le \|(x, T(x))\|_{X \times Y}$.
        Ceci signifie que $P_1$ est continu, avec $\|P_1\| \le 1$.

    *   **Bijectivité de $P_1$ :**
        *   **Injectivité :** Supposons $P_1(x, T(x)) = 0$. Ceci implique $x = 0$. Puisque $T$ est linéaire, $T(0)=0$. Donc $(x, T(x)) = (0, 0)$. Ainsi, $P_1$ est injectif.
        *   **Surjectivité :** Pour tout $x' \in X$, l'élément $(x', T(x'))$ appartient à $G(T)$. Par définition de $P_1$, $P_1(x', T(x')) = x'$. Ainsi, $P_1$ est surjectif.

    En conclusion, $P_1: G(T) \to X$ est un opérateur linéaire continu et bijectif entre deux espaces de Banach ($G(T)$ et $X$).

3.  **Appliquer le Théorème de l'Isomorphisme de Banach (Partie II) à $P_1$ pour démontrer que $P_1^{-1}: X \to G(T)$ est continu.**

    D'après la question précédente, $P_1: G(T) \to X$ est un opérateur linéaire continu et bijectif. De plus, $G(T)$ est un espace de Banach (car c'est un sous-espace fermé de l'espace de Banach $X \times Y$), et $X$ est un espace de Banach par hypothèse.
    Selon le Théorème de l'Isomorphisme de Banach (Partie II, question 1), si un opérateur linéaire $T$ entre deux espaces de Banach est continu et bijectif, alors son inverse $T^{-1}$ est également continu.
    En appliquant ce théorème à $P_1$, nous concluons que son inverse $P_1^{-1}: X \to G(T)$ est continu.

4.  **Considérer l'opérateur $P_2: G(T) \to Y$ défini par $P_2(x, T(x)) = T(x)$. Démontrer que $P_2$ est un opérateur linéaire continu.**

    *   **Linéarité de $P_2$ :** Soient $(x_1, T(x_1))$ et $(x_2, T(x_2))$ deux éléments de $G(T)$, et $\alpha, \beta \in \mathbb{K}$.
        $P_2(\alpha(x_1, T(x_1)) + \beta(x_2, T(x_2))) = P_2(\alpha x_1 + \beta x_2, \alpha T(x_1) + \beta T(x_2))$.
        Puisque $T$ est linéaire, $\alpha T(x_1) + \beta T(x_2) = T(\alpha x_1 + \beta x_2)$.
        Donc, $P_2(\alpha(x_1, T(x_1)) + \beta(x_2, T(x_2))) = P_2(\alpha x_1 + \beta x_2, T(\alpha x_1 + \beta x_2)) = T(\alpha x_1 + \beta x_2)$.
        D'autre part, $\alpha P_2(x_1, T(x_1)) + \beta P_2(x_2, T(x_2)) = \alpha T(x_1) + \beta T(x_2)$.
        Puisque $T$ est linéaire, $T(\alpha x_1 + \beta x_2) = \alpha T(x_1) + \beta T(x_2)$.
        Ainsi, $P_2$ est linéaire.

    *   **Continuité de $P_2$ :** Pour tout $(x, T(x)) \in G(T)$:
        $\|P_2(x, T(x))\|_Y = \|T(x)\|_Y$.
        Nous comparons cela à la norme de l'élément dans $G(T)$: $\|(x, T(x))\|_{X \times Y} = \|x\|_X + \|T(x)\|_Y$.
        Clairement, $\|T(x)\|_Y \le \|x\|_X + \|T(x)\|_Y$.
        Donc $\|P_2(x, T(x))\|_Y \le \|(x, T(x))\|_{X \times Y}$.
        Ceci signifie que $P_2$ est continu, avec $\|P_2\| \le 1$.

5.  **Déduire de ce qui précède que $T$ est un opérateur continu.**

    Nous voulons montrer que $T: X \to Y$ est continu.
    Pour tout $x \in X$, nous avons $T(x) = P_2(x, T(x))$.
    De plus, nous savons que $P_1^{-1}(x) = (x, T(x))$ par définition de $P_1$ et de son inverse.
    En substituant $P_1^{-1}(x)$ dans l'expression de $T(x)$, nous obtenons :
    $T(x) = P_2(P_1^{-1}(x))$.
    Ainsi, l'opérateur $T$ peut être exprimé comme la composition de deux opérateurs : $T = P_2 \circ P_1^{-1}$.
    Nous avons démontré à la question 3 que $P_1^{-1}: X \to G(T)$ est continu.
    Nous avons démontré à la question 4 que $P_2: G(T) \to Y$ est continu.
    La composition de deux opérateurs linéaires continus est un opérateur linéaire continu.
    Par conséquent, $T = P_2 \circ P_1^{-1}$ est un opérateur continu.
    Ceci conclut la preuve du Théorème du Graphe Fermé.