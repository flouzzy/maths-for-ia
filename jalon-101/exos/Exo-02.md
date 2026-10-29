# Exercice 02 - Une Plongée Profonde dans les Théorèmes Fondamentaux de l'Analyse Fonctionnelle

Cet exercice explore les conséquences majeures du Théorème de l'Application Ouverte et du Théorème de l'Isomorphisme de Banach, en mettant en lumière la cruciale condition de "rang fermé" pour la continuité des opérateurs inverses.

Difficulté : $\bigstar\star\star\star\star$

---

Soient $X$ et $Y$ deux espaces de Banach sur le corps $\mathbb{K}$ (soit $\mathbb{R}$, soit $\mathbb{C}$). Soit $T: X \to Y$ un opérateur linéaire.

1.  **Théorème de l'Isomorphisme de Banach:** Soit $T: X \to Y$ un opérateur linéaire continu et bijectif. Montrer que son inverse $T^{-1}: Y \to X$ est également continu. On pourra s'appuyer sur le Théorème de l'Application Ouverte.
    *Rappel du Théorème de l'Application Ouverte:* Si $X$ et $Y$ sont des espaces de Banach, et $T: X \to Y$ est un opérateur linéaire continu et surjectif, alors $T$ est une application ouverte (i.e., l'image de tout ouvert de $X$ est un ouvert de $Y$).

2.  **Opérateurs à Rang Fermé:** Soit $T: X \to Y$ un opérateur linéaire continu et *injectif*. On suppose de plus que l'image $\text{Im}(T) = T(X)$ est un sous-espace fermé de $Y$.
    Montrer que $T$ admet un inverse continu $T^{-1}: \text{Im}(T) \to X$.

3.  **L'Importance Cruciale du Rang Fermé (Contre-exemple):**
    Considérons les espaces fonctionnels suivants sur l'intervalle $[0,1]$ :
    *   $X = (C^1([0,1]), \|\cdot\|_{C^1})$, où $C^1([0,1])$ est l'ensemble des fonctions continûment différentiables sur $[0,1]$, et la norme est définie par $\|f\|_{C^1} = \|f\|_\infty + \|f'\|_\infty$.
    *   $Y = (C([0,1]), \|\cdot\|_\infty)$, où $C([0,1])$ est l'ensemble des fonctions continues sur $[0,1]$, et la norme est la norme de la convergence uniforme $\|f\|_\infty = \sup_{x \in [0,1]} |f(x)|$.
    On admettra que $(C^1([0,1]), \|\cdot\|_{C^1})$ est un espace de Banach. On sait que $(C([0,1]), \|\cdot\|_\infty)$ est un espace de Banach.
    Soit $I: X \to Y$ l'opérateur d'inclusion canonique, défini par $I(f) = f$ pour tout $f \in X$.
    a. Montrer que $I$ est un opérateur linéaire continu et injectif.
    b. Montrer que l'image $\text{Im}(I)$ n'est pas fermée dans $Y$.
    c. Montrer que l'opérateur inverse $I^{-1}: \text{Im}(I) \to X$ n'est pas continu.
    d. Expliquer pourquoi ce contre-exemple n'est pas en contradiction avec le résultat de la question 2.

---

# Correction de l'Exercice 02

### Question 1 : Théorème de l'Isomorphisme de Banach

Soient $X$ et $Y$ des espaces de Banach, et $T: X \to Y$ un opérateur linéaire continu et bijectif. Nous voulons montrer que son inverse $T^{-1}: Y \to X$ est également continu.

Pour montrer la continuité de $T^{-1}$, nous devons démontrer que l'image réciproque de tout ouvert de $X$ par $T^{-1}$ est un ouvert de $Y$. Soit $U \subset X$ un ensemble ouvert arbitraire. Nous devons montrer que $(T^{-1})^{-1}(U)$ est un ouvert dans $Y$.

Par définition de l'opérateur inverse, $(T^{-1})^{-1}(U)$ est l'ensemble des $y \in Y$ tels que $T^{-1}(y) \in U$. Puisque $T^{-1}(y)$ est l'unique $x \in X$ tel que $T(x)=y$, nous pouvons écrire cet ensemble comme $\{y \in Y \mid \exists x \in U, T(x)=y\}$. Cela n'est rien d'autre que l'image de $U$ par $T$, c'est-à-dire $T(U)$.

Nous devons donc montrer que $T(U)$ est un ouvert de $Y$. C'est précisément ce que garantit le Théorème de l'Application Ouverte.
Le Théorème de l'Application Ouverte stipule que si $X$ et $Y$ sont des espaces de Banach et $T: X \to Y$ est un opérateur linéaire continu et *surjectif*, alors $T$ est une application ouverte.

Dans notre cas, $T$ est bijectif, ce qui implique qu'il est surjectif par définition. De plus, $X$ et $Y$ sont des espaces de Banach et $T$ est continu par hypothèse. Toutes les conditions du Théorème de l'Application Ouverte sont donc remplies.
Par conséquent, $T$ est une application ouverte. Cela signifie que pour tout ensemble ouvert $U \subset X$, l'image $T(U)$ est un ensemble ouvert dans $Y$.

Comme nous l'avons établi, $(T^{-1})^{-1}(U) = T(U)$. Puisque $T(U)$ est un ouvert de $Y$, cela signifie que $T^{-1}$ est continu.

Une méthode alternative, équivalente et plus quantitative, consiste à montrer qu'il existe une constante $C > 0$ telle que $\|T^{-1}(y)\|_X \le C \|y\|_Y$ pour tout $y \in Y$.
Puisque $T$ est un opérateur linéaire continu et surjectif entre espaces de Banach, le Théorème de l'Application Ouverte garantit que $T$ est ouvert. Cela implique, en particulier, qu'il existe une constante $M > 0$ telle que la boule ouverte $B_Y(0, M)$ de $Y$ (centrée en 0 et de rayon $M$) est contenue dans l'image de la boule unité $B_X(0,1)$ de $X$ par $T$. Autrement dit, $B_Y(0, M) \subset T(B_X(0,1))$.

Soit $y \in Y$ un vecteur non nul. Alors $y/\|y\|_Y$ est un vecteur de norme 1 dans $Y$.
Le vecteur $M \cdot (y/\|y\|_Y)$ a une norme $M$, donc $M \cdot (y/\|y\|_Y) \in B_Y(0, M)$.
Par la propriété ci-dessus, il existe un $x \in B_X(0,1)$ tel que $T(x) = M \cdot (y/\|y\|_Y)$.
Puisque $T$ est bijectif, $x = T^{-1}(M \cdot (y/\|y\|_Y))$.
Par linéarité de $T^{-1}$, nous avons $x = (M/\|y\|_Y) T^{-1}(y)$.
Étant donné que $x \in B_X(0,1)$, nous savons que $\|x\|_X < 1$.
Ainsi, $\| (M/\|y\|_Y) T^{-1}(y) \|_X < 1$.
Par les propriétés de la norme, $(M/\|y\|_Y) \|T^{-1}(y)\|_X < 1$.
En réarrangeant les termes, nous obtenons $\|T^{-1}(y)\|_X < \frac{1}{M} \|y\|_Y$.
Cette inégalité est valable pour tout $y \in Y$ non nul. Si $y=0$, alors $T^{-1}(0)=0$, et l'inégalité $\|0\|_X < \frac{1}{M}\|0\|_Y$ est trivialement vérifiée (i.e. $0 < 0$ qui est faux, mais $\|0\|_X = 0 \le \frac{1}{M}\|0\|_Y=0$ est vrai).
Nous pouvons donc prendre $C = 1/M$. L'existence d'une telle constante $C$ démontre la continuité de $T^{-1}$.

### Question 2 : Opérateurs à Rang Fermé

Soit $T: X \to Y$ un opérateur linéaire continu et injectif. On suppose que l'image $\text{Im}(T) = T(X)$ est un sous-espace fermé de $Y$. Nous voulons montrer que $T$ admet un inverse continu $T^{-1}: \text{Im}(T) \to X$.

Pour appliquer le Théorème de l'Isomorphisme de Banach (prouvé en Q1), nous avons besoin d'un opérateur linéaire continu et bijectif entre deux espaces de Banach.
Considérons l'opérateur $T_0: X \to \text{Im}(T)$ défini par $T_0(x) = T(x)$ pour tout $x \in X$.
Analysons les propriétés de $T_0$:

1.  **Linéarité de $T_0$**: Puisque $T$ est linéaire, $T_0$ est clairement linéaire car sa définition est la même que celle de $T$, seule la codomaine est modifiée.
2.  **Continuité de $T_0$**: L'opérateur $T_0$ est continu. En effet, la norme sur $\text{Im}(T)$ est la norme induite par $Y$. Donc, pour tout $x \in X$, $\|T_0(x)\|_{\text{Im}(T)} = \|T(x)\|_Y$. Puisque $T$ est continu par hypothèse, il existe une constante $M_T > 0$ telle que $\|T(x)\|_Y \le M_T \|x\|_X$ pour tout $x \in X$. Par conséquent, $\|T_0(x)\|_{\text{Im}(T)} \le M_T \|x\|_X$, ce qui prouve la continuité de $T_0$.
3.  **Injectivité de $T_0$**: $T_0$ est injectif car $T$ est injectif par hypothèse. Si $T_0(x_1) = T_0(x_2)$, alors $T(x_1) = T(x_2)$, ce qui implique $x_1 = x_2$ puisque $T$ est injectif.
4.  **Surjectivité de $T_0$**: Par définition de sa codomaine, $T_0$ est surjectif sur $\text{Im}(T)$. Pour tout $y \in \text{Im}(T)$, il existe un $x \in X$ tel que $T(x)=y$, et donc $T_0(x)=y$.
5.  **Espaces de Banach**:
    *   $X$ est un espace de Banach par hypothèse.
    *   $\text{Im}(T)$ est un sous-espace vectoriel de $Y$. L'hypothèse cruciale est que $\text{Im}(T)$ est fermé dans $Y$. Puisqu'un sous-espace fermé d'un espace de Banach est lui-même un espace de Banach (avec la norme induite), $\text{Im}(T)$ est un espace de Banach.

Maintenant, nous avons un opérateur $T_0: X \to \text{Im}(T)$ qui est linéaire, continu, bijectif, et opère entre deux espaces de Banach ($X$ et $\text{Im}(T)$). Toutes les conditions du Théorème de l'Isomorphisme de Banach (prouvé en Q1) sont remplies pour $T_0$.
Par conséquent, l'opérateur inverse $T_0^{-1}: \text{Im}(T) \to X$ est continu.
Cet opérateur $T_0^{-1}$ est précisément l'opérateur inverse $T^{-1}$ que nous cherchions.
Nous avons donc montré que $T$ admet un inverse continu $T^{-1}: \text{Im}(T) \to X$.

### Question 3 : L'Importance Cruciale du Rang Fermé (Contre-exemple)

Considérons les espaces $X = (C^1([0,1]), \|\cdot\|_{C^1})$ et $Y = (C([0,1]), \|\cdot\|_\infty)$, avec l'opérateur d'inclusion $I: X \to Y$ défini par $I(f) = f$.

a. **Montrer que $I$ est un opérateur linéaire continu et injectif.**
    *   **Linéarité**: Pour $f, g \in C^1([0,1])$ et $a, b \in \mathbb{K}$, $I(af+bg) = af+bg$. Par la linéarité des fonctions, $af+bg = aI(f) + bI(g)$. Donc $I$ est linéaire.
    *   **Injectivité**: Supposons $I(f) = 0$. Cela signifie que la fonction $f$ est la fonction nulle dans $C([0,1])$, c'est-à-dire $f(x)=0$ pour tout $x \in [0,1]$. Puisque $f \in C^1([0,1])$, $f$ est la fonction nulle de $C^1([0,1])$. Par conséquent, $I$ est injectif.
    *   **Continuité**: Nous devons montrer qu'il existe une constante $C>0$ telle que $\|I(f)\|_\infty \le C \|f\|_{C^1}$ pour tout $f \in X$.
        Par définition, $\|I(f)\|_\infty = \|f\|_\infty$.
        Par définition de la norme sur $X$, $\|f\|_{C^1} = \|f\|_\infty + \|f'\|_\infty$.
        Il est évident que $\|f\|_\infty \le \|f\|_\infty + \|f'\|_\infty$.
        Ainsi, $\|I(f)\|_\infty \le \|f\|_{C^1}$. Nous pouvons prendre la constante $C=1$.
        Donc, $I$ est un opérateur linéaire continu et injectif.

b. **Montrer que l'image $\text{Im}(I)$ n'est pas fermée dans $Y$.**
    L'image de $I$ est $\text{Im}(I) = C^1([0,1])$, vu comme un sous-espace de $C([0,1])$ muni de la norme $\|\cdot\|_\infty$. Pour montrer que $\text{Im}(I)$ n'est pas fermé dans $Y$, il suffit de trouver une suite de fonctions $(f_n)_{n \in \mathbb{N}}$ dans $C^1([0,1])$ qui converge uniformément (dans $Y$) vers une fonction $f \in C([0,1])$ telle que $f \notin C^1([0,1])$.

    Considérons la fonction $f(x) = |x - 1/2|$ pour $x \in [0,1]$. Cette fonction est continue sur $[0,1]$, donc $f \in C([0,1])$. Cependant, elle n'est pas différentiable au point $x=1/2$, donc $f \notin C^1([0,1])$.

    Il nous faut maintenant construire une suite $(f_n)_{n \in \mathbb{N}}$ de fonctions dans $C^1([0,1])$ qui converge uniformément vers $f$. Nous pouvons utiliser des approximations polynomiales lisses ou des mollifications.
    Considérons la suite de fonctions $g_n(t) = \sqrt{t^2 + 1/n}$ pour $t \in [0,1]$. Chaque $g_n$ est $C^\infty([0,1])$, donc $g_n \in C^1([0,1])$.
    Pour $f_n(x) = \sqrt{(x-1/2)^2 + 1/n}$:
    *   Chaque $f_n$ est dans $C^\infty([0,1])$, et donc dans $C^1([0,1])$.
    *   Pour la convergence uniforme : Pour tout $\epsilon > 0$, nous devons trouver $N$ tel que pour $n \ge N$, $\|f_n - f\|_\infty < \epsilon$.
        $|f_n(x) - f(x)| = |\sqrt{(x-1/2)^2 + 1/n} - |x-1/2||$.
        Multiplions par le conjugué :
        $|f_n(x) - f(x)| = \left| \frac{((x-1/2)^2 + 1/n) - (x-1/2)^2}{\sqrt{(x-1/2)^2 + 1/n} + |x-1/2|} \right| = \left| \frac{1/n}{\sqrt{(x-1/2)^2 + 1/n} + |x-1/2|} \right|$.
        Le dénominateur $\sqrt{(x-1/2)^2 + 1/n} + |x-1/2| \ge \sqrt{1/n} = 1/\sqrt{n}$.
        Ainsi, $|f_n(x) - f(x)| \le \frac{1/n}{1/\sqrt{n}} = \frac{1}{\sqrt{n}}$.
        Cette majoration est indépendante de $x$.
        Donc $\|f_n - f\|_\infty \le 1/\sqrt{n}$.
        Puisque $1/\sqrt{n} \to 0$ lorsque $n \to \infty$, la suite $(f_n)$ converge uniformément vers $f(x) = |x-1/2|$ dans $C([0,1])$.
    *   Comme $f \notin C^1([0,1])$, et $f_n \in C^1([0,1])$ pour tout $n$, nous avons montré que $\text{Im}(I) = C^1([0,1])$ n'est pas un sous-espace fermé de $Y = C([0,1])$.

c. **Montrer que l'opérateur inverse $I^{-1}: \text{Im}(I) \to X$ n'est pas continu.**
    L'opérateur $I^{-1}: C^1([0,1]) \to C^1([0,1])$ est défini par $I^{-1}(f) = f$, où le $f$ du domaine est muni de la norme $\|\cdot\|_\infty$ et le $f$ de la codomaine est muni de la norme $\|\cdot\|_{C^1}$.
    Si $I^{-1}$ était continu, il existerait une constante $K>0$ telle que pour tout $f \in C^1([0,1])$, nous aurions $\|I^{-1}(f)\|_{C^1} \le K \|f\|_\infty$.
    Ceci équivaut à $\|f\|_{C^1} \le K \|f\|_\infty$ pour tout $f \in C^1([0,1])$.
    En substituant la définition de la norme $\|\cdot\|_{C^1}$:
    $\|f\|_\infty + \|f'\|_\infty \le K \|f\|_\infty$.
    Cela implique $\|f'\|_\infty \le (K-1) \|f\|_\infty$.

    Pour montrer que cette inégalité ne peut pas être vraie pour une constante $K$ fixe, considérons une suite de fonctions qui "violent" cette condition.
    Soit la suite de fonctions $f_n(x) = \frac{1}{n} \sin(n^2 \pi x)$ pour $x \in [0,1]$ et $n \in \mathbb{N}^*$.
    *   Chaque $f_n \in C^\infty([0,1])$, donc $f_n \in C^1([0,1])$.
    *   Calculons les normes :
        $\|f_n\|_\infty = \sup_{x \in [0,1]} \left|\frac{1}{n} \sin(n^2 \pi x)\right| = \frac{1}{n} \cdot 1 = \frac{1}{n}$.
        La dérivée de $f_n$ est $f_n'(x) = \frac{1}{n} \cdot (n^2 \pi) \cos(n^2 \pi x) = n\pi \cos(n^2 \pi x)$.
        $\|f_n'\|_\infty = \sup_{x \in [0,1]} |n\pi \cos(n^2 \pi x)| = n\pi \cdot 1 = n\pi$.

    Substituons ces valeurs dans l'inégalité $\|f'\|_\infty \le (K-1) \|f\|_\infty$:
    $n\pi \le (K-1) \frac{1}{n}$.
    En multipliant par $n$ (qui est positif), on obtient $n^2 \pi \le K-1$.
    Cette inégalité doit être vraie pour tous les entiers positifs $n$. Cependant, le membre de gauche $n^2 \pi$ tend vers l'infini lorsque $n \to \infty$, tandis que le membre de droite $K-1$ est une constante.
    Il est impossible qu'une constante soit supérieure ou égale à une quantité qui tend vers l'infini.
    Par conséquent, une telle constante $K$ n'existe pas, et donc l'opérateur $I^{-1}$ n'est pas continu.

d. **Expliquer pourquoi ce contre-exemple n'est pas en contradiction avec le résultat de la question 2.**
    Le résultat de la question 2 stipule que si $T: X \to Y$ est un opérateur linéaire continu, injectif, et que son image $\text{Im}(T)$ est un *sous-espace fermé* de $Y$, alors son inverse $T^{-1}: \text{Im}(T) \to X$ est continu.

    Dans le contre-exemple de la question 3, nous avons un opérateur $I: X \to Y$ qui est linéaire, continu et injectif (comme montré en 3a).
    Cependant, la condition essentielle pour l'application du résultat de la question 2 n'est pas remplie : nous avons montré en 3b que l'image $\text{Im}(I) = C^1([0,1])$ n'est *pas un sous-espace fermé* de $Y = C([0,1])$ sous la norme $\|\cdot\|_\infty$.

    Puisque la prémisse "$\text{Im}(T)$ est fermé" du théorème de la question 2 n'est pas satisfaite, le théorème ne garantit pas la continuité de $I^{-1}$. Le fait que $I^{-1}$ s'avère ne pas être continu (comme démontré en 3c) ne contredit donc en aucun cas le théorème. Au contraire, ce contre-exemple met en évidence l'importance et la nécessité de la condition de "rang fermé" dans le Théorème de l'Isomorphisme de Banach appliqué aux opérateurs injectifs non surjectifs. C'est un exemple classique de la délicatesse des conditions des théorèmes fondamentaux de l'analyse fonctionnelle.