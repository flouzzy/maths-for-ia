# Exercice 03 - Théorèmes Fondamentaux de l'Analyse Fonctionnelle : L'Équivalence des Normes et au-delà

Cet exercice est conçu pour sonder votre compréhension des théorèmes fondamentaux de l'analyse fonctionnelle : le théorème de l'application ouverte, le théorème du graphe fermé et le théorème de l'isomorphisme de Banach. Une attention particulière doit être portée à la rigueur des démonstrations et à l'analyse des hypothèses.

Difficulté : $\bigstar\bigstar\bigstar\bigstar\bigstar$

---

**Partie I : Équivalence de Normes sur un Espace de Banach**

Soit $X$ un espace vectoriel sur $\mathbb{C}$ (ou $\mathbb{R}$). Soient $\|\cdot\|_1$ et $\|\cdot\|_2$ deux normes sur $X$.
Nous supposons que $(X, \|\cdot\|_1)$ est un espace de Banach et que $(X, \|\cdot\|_2)$ est également un espace de Banach.
De plus, nous supposons qu'il existe une constante $C > 0$ telle que pour tout $x \in X$, nous ayons $\|x\|_1 \le C \|x\|_2$.
L'objectif est de démontrer que ces deux normes sont équivalentes. C'est-à-dire qu'il existe une constante $D > 0$ telle que pour tout $x \in X$, nous ayons $\|x\|_2 \le D \|x\|_1$.

1.  Considérer l'application identité $I: (X, \|\cdot\|_2) \to (X, \|\cdot\|_1)$ définie par $I(x) = x$. Démontrer que $I$ est un opérateur linéaire continu.
2.  Expliquer pourquoi le Théorème de l'Application Ouverte (Open Mapping Theorem) peut être appliqué à l'opérateur $I$.
3.  En déduire la conclusion souhaitée concernant l'équivalence des normes.

**Partie II : L'Importance de la Complétude - Une Contre-Exemple**

Maintenant, nous allons examiner la nécessité de la condition de complétude.
Soit $X = C([0,1])$ l'espace des fonctions continues sur l'intervalle $[0,1]$ à valeurs réelles.
Pour $f \in X$, nous définissons deux normes :
$$ \left\|f\right\|_\infty = \sup_{t \in [0,1]} \left|f(t)\right| $$
$$ \left\|f\right\|_1 = \int_0^1 \left|f(t)\right| dt $$
Il est bien connu que $(X, \|\cdot\|_\infty)$ est un espace de Banach. Cependant, $(X, \|\cdot\|_1)$ n'est pas complet.
De plus, il est clair que pour tout $f \in X$, $\|f\|_1 \le \|f\|_\infty$.

1.  Démontrer que la condition $\|f\|_1 \le \|f\|_\infty$ est satisfaite.
2.  Démontrer par un contre-exemple explicite que l'inégalité inverse $\|f\|_\infty \le D \|f\|_1$ n'est pas vraie pour une constante $D > 0$ universelle. Ceci met en lumière la nécessité de la complétude de *deux* espaces pour appliquer le théorème d'équivalence.

**Partie III : Le Théorème du Graphe Fermé et les Opérateurs à Domaine Fermé**

Soit $X$ un espace de Banach et $Y$ un espace de Banach.
Soit $T: \mathcal{D}(T) \subset X \to Y$ un opérateur linéaire dont le domaine $\mathcal{D}(T)$ est un sous-espace vectoriel de $X$.
Supposons que $T$ est injectif et que son image $\mathcal{R}(T) = T(\mathcal{D}(T))$ est un sous-espace fermé de $Y$.
De plus, supposons que pour toute suite $(x_n)_{n \in \mathbb{N}}$ dans $\mathcal{D}(T)$ telle que $x_n \to x$ dans $X$ et $T(x_n) \to y$ dans $Y$, on a $x \in \mathcal{D}(T)$ et $T(x) = y$. (Cette condition signifie que $T$ est un opérateur à graphe fermé).

1.  On munit $\mathcal{D}(T)$ de la norme du graphe $\|x\|_G = \|x\|_X + \|T(x)\|_Y$. Démontrer que $(\mathcal{D}(T), \|\cdot\|_G)$ est un espace de Banach.
2.  Considérer l'opérateur $T_G: (\mathcal{D}(T), \|\cdot\|_G) \to Y$ défini par $T_G(x) = T(x)$. Démontrer que $T_G$ est un opérateur linéaire continu de $(\mathcal{D}(T), \|\cdot\|_G)$ vers $Y$. Préciser son image.
3.  Utiliser le Théorème de l'Application Ouverte pour démontrer que $T_G$ est un isomorphisme topologique de $(\mathcal{D}(T), \|\cdot\|_G)$ sur $\mathcal{R}(T)$.
4.  En déduire que l'opérateur inverse $T^{-1}: \mathcal{R}(T) \to \mathcal{D}(T)$ est continu lorsqu'on munit $\mathcal{D}(T)$ de la norme $\| \cdot \|_G$. C'est-à-dire qu'il existe une constante $M_2 > 0$ telle que pour tout $y \in \mathcal{R}(T)$, $\left\|T^{-1}(y)\right\|_G \le M_2 \left\|y\right\|_Y$.

---

## Correction Détaillée

### Partie I : Équivalence de Normes sur un Espace de Banach

1.  **Linéarité et continuité de $I$ :**
    L'application identité $I: (X, \|\cdot\|_2) \to (X, \|\cdot\|_1)$ est définie par $I(x) = x$.
    *   **Linéarité :** Soient $x_1, x_2 \in X$ et $\alpha \in \mathbb{C}$ (ou $\mathbb{R}$).
        $I(\alpha x_1 + x_2) = \alpha x_1 + x_2$.
        $\alpha I(x_1) + I(x_2) = \alpha x_1 + x_2$.
        Donc $I(\alpha x_1 + x_2) = \alpha I(x_1) + I(x_2)$, ce qui prouve la linéarité de $I$.
    *   **Continuité :** Pour qu'un opérateur linéaire soit continu, il faut et il suffit qu'il soit borné. C'est-à-dire qu'il existe une constante $M > 0$ telle que $\|I(x)\|_1 \le M \|x\|_2$ pour tout $x \in X$.
        D'après l'énoncé, nous avons la condition $\|x\|_1 \le C \|x\|_2$ pour tout $x \in X$, où $C > 0$ est une constante.
        En substituant $I(x)$ par $x$, nous obtenons $\|I(x)\|_1 \le C \|x\|_2$.
        Cette inégalité démontre que l'opérateur $I$ est continu avec une norme d'opérateur $\|I\| \le C$.

2.  **Application du Théorème de l'Application Ouverte :**
    Le Théorème de l'Application Ouverte (TAO) stipule que si $T: E \to F$ est un opérateur linéaire continu et surjectif entre deux espaces de Banach $E$ et $F$, alors $T$ est une application ouverte (i.e., l'image de tout ouvert de $E$ est un ouvert de $F$). Une conséquence directe est que $T$ est un isomorphisme topologique si et seulement si $T$ est bijectif.

    Vérifions les conditions pour $I: (X, \|\cdot\|_2) \to (X, \|\cdot\|_1)$ :
    *   **$E$ est un espace de Banach :** L'espace de départ est $(X, \|\cdot\|_2)$. Par hypothèse, $(X, \|\cdot\|_2)$ est un espace de Banach. Cette condition est satisfaite.
    *   **$F$ est un espace de Banach :** L'espace d'arrivée est $(X, \|\cdot\|_1)$. Par hypothèse, $(X, \|\cdot\|_1)$ est un espace de Banach. Cette condition est satisfaite.
    *   **$I$ est linéaire et continu :** Nous l'avons démontré au point précédent.
    *   **$I$ est surjectif :** L'application identité $I$ est par définition une surjection de $X$ sur $X$. Pour tout $y \in (X, \|\cdot\|_1)$, il existe $x=y \in (X, \|\cdot\|_2)$ tel que $I(x)=y$.

    Toutes les conditions du Théorème de l'Application Ouverte sont donc remplies pour l'opérateur $I$.

3.  **Déduction de l'équivalence des normes :**
    Puisque toutes les conditions du Théorème de l'Application Ouverte sont satisfaites, l'opérateur $I$ est une application ouverte.
    De plus, comme $I$ est bijectif (étant l'identité, il est trivialement injectif et surjectif), le Théorème de l'Application Ouverte implique que l'opérateur inverse $I^{-1}$ est également continu.
    L'opérateur inverse $I^{-1}: (X, \|\cdot\|_1) \to (X, \|\cdot\|_2)$ est aussi l'application identité, $I^{-1}(x) = x$.
    La continuité de $I^{-1}$ signifie qu'il existe une constante $D > 0$ telle que pour tout $x \in X$, nous avons $\|I^{-1}(x)\|_2 \le D \|x\|_1$.
    En substituant $I^{-1}(x)$ par $x$, nous obtenons $\|x\|_2 \le D \|x\|_1$.

    En combinant cette inégalité avec l'hypothèse initiale $\|x\|_1 \le C \|x\|_2$, nous avons démontré que les deux normes $\|\cdot\|_1$ et $\|\cdot\|_2$ sont équivalentes sur $X$.

### Partie II : L'Importance de la Complétude - Une Contre-Exemple

1.  **Démonstration de $\|f\|_1 \le \|f\|_\infty$ :**
    Soit $f \in C([0,1])$. Par définition, $\|f\|_\infty = \sup_{t \in [0,1]} |f(t)|$.
    Pour tout $t \in [0,1]$, nous avons $|f(t)| \le \|f\|_\infty$.
    En intégrant cette inégalité sur l'intervalle $[0,1]$ (qui est de longueur 1) :
    $$ \int_0^1 \left|f(t)\right| dt \le \int_0^1 \left\|f\right\|_\infty dt $$
    $$ \left\|f\right\|_1 \le \left\|f\right\|_\infty \int_0^1 dt $$
    $$ \left\|f\right\|_1 \le \left\|f\right\|_\infty \cdot 1 $$
    $$ \left\|f\right\|_1 \le \left\|f\right\|_\infty $$
    Cette condition est donc satisfaite avec $C=1$.

2.  **Contre-exemple explicite à l'inégalité inverse :**
    Nous cherchons une suite de fonctions $(f_n)_{n \in \mathbb{N}}$ dans $C([0,1])$ telle que $\|f_n\|_1 \to 0$ lorsque $n \to \infty$, mais $\|f_n\|_\infty$ ne reste pas bornée (tend vers l'infini). Si une telle suite existe, l'inégalité $\|f\|_\infty \le D \|f\|_1$ ne peut pas être vraie, car cela impliquerait $\|f_n\|_\infty \le D \|f_n\|_1 \to 0$, ce qui est une contradiction.

    Considérons la suite de fonctions $f_n: [0,1] \to \mathbb{R}$ définie pour $n \in \mathbb{N}^*$ par :
    $$ f_n(x) = n \exp(-n^2 x) $$
    Chaque $f_n(x)$ est une fonction continue sur $[0,1]$.
    *   **Calcul de $\|f_n\|_\infty$ :**
        La fonction $f_n(x)$ est décroissante sur $[0,1]$ puisque sa dérivée $f_n'(x) = -n^3 \exp(-n^2 x)$ est négative.
        Par conséquent, son maximum est atteint en $x=0$.
        $$ \left\|f_n\right\|_\infty = f_n(0) = n \exp(0) = n $$
        Ainsi, $\left\|f_n\right\|_\infty \to \infty$ lorsque $n \to \infty$.

    *   **Calcul de $\|f_n\|_1$ :**
        $$ \left\|f_n\right\|_1 = \int_0^1 \left|n \exp(-n^2 x)\right| dx = \int_0^1 n \exp(-n^2 x) dx $$
        $$ \left\|f_n\right\|_1 = n \left[ \frac{-1}{n^2} \exp(-n^2 x) \right]_0^1 = -\frac{1}{n} \left( \exp(-n^2 \cdot 1) - \exp(-n^2 \cdot 0) \right) $$
        $$ \left\|f_n\right\|_1 = -\frac{1}{n} \left( \exp(-n^2) - 1 \right) = \frac{1 - \exp(-n^2)}{n} $$
        Lorsque $n \to \infty$, $\exp(-n^2) \to 0$. Donc,
        $$ \lim_{n \to \infty} \left\|f_n\right\|_1 = \lim_{n \to \infty} \frac{1 - \exp(-n^2)}{n} = \frac{1-0}{\infty} = 0 $$
        Ainsi, $\left\|f_n\right\|_1 \to 0$ lorsque $n \to \infty$.

    Nous avons construit une suite $(f_n)$ telle que $\left\|f_n\right\|_1 \to 0$ et $\left\|f_n\right\|_\infty \to \infty$.
    Si l'inégalité $\|f\|_\infty \le D \|f\|_1$ était vraie pour une constante $D > 0$, alors on aurait $\left\|f_n\right\|_\infty \le D \left\|f_n\right\|_1$. En passant à la limite, cela impliquerait $\infty \le D \cdot 0 = 0$, ce qui est une contradiction manifeste.
    Ce contre-exemple démontre que la complétude des deux espaces normés est une condition essentielle pour l'équivalence des normes. Dans notre cas, $(C([0,1]), \|\cdot\|_\infty)$ est complet, mais $(C([0,1]), \|\cdot\|_1)$ ne l'est pas.

### Partie III : Le Théorème du Graphe Fermé et les Opérateurs à Domaine Fermé

1.  **Démonstration de la complétude de $(\mathcal{D}(T), \|\cdot\|_G)$ :**
    Soit $(x_n)_{n \in \mathbb{N}}$ une suite de Cauchy dans $(\mathcal{D}(T), \|\cdot\|_G)$.
    Par définition de la norme du graphe, $\|x\|_G = \|x\|_X + \|T(x)\|_Y$.
    Puisque $(x_n)$ est une suite de Cauchy pour $\|\cdot\|_G$, pour tout $\varepsilon > 0$, il existe $N \in \mathbb{N}$ tel que pour tous $m, n \ge N$, on a $\|x_n - x_m\|_G < \varepsilon$.
    Ceci implique :
    $$ \|x_n - x_m\|_X + \|T(x_n) - T(x_m)\|_Y < \varepsilon $$
    De cette inégalité, nous déduisons directement :
    *   $\|x_n - x_m\|_X < \varepsilon$, ce qui signifie que $(x_n)$ est une suite de Cauchy dans $(X, \|\cdot\|_X)$.
    *   $\|T(x_n) - T(x_m)\|_Y < \varepsilon$, ce qui signifie que $(T(x_n))$ est une suite de Cauchy dans $(Y, \|\cdot\|_Y)$.

    Étant donné que $X$ est un espace de Banach, la suite de Cauchy $(x_n)$ converge vers un certain $x \in X$.
    Étant donné que $Y$ est un espace de Banach, la suite de Cauchy $(T(x_n))$ converge vers un certain $y \in Y$.

    Nous utilisons maintenant la condition donnée dans l'énoncé concernant l'opérateur $T$ : pour toute suite $(x_n)$ dans $\mathcal{D}(T)$ telle que $x_n \to x$ dans $X$ et $T(x_n) \to y$ dans $Y$, on a $x \in \mathcal{D}(T)$ et $T(x) = y$. Cette condition est précisément la définition d'un opérateur à graphe fermé.
    Puisque $(x_n)$ converge vers $x$ dans $X$ et $(T(x_n))$ converge vers $y$ dans $Y$, la condition du graphe fermé implique que $x \in \mathcal{D}(T)$ et $T(x) = y$.

    Il reste à montrer que $x_n \to x$ dans $(\mathcal{D}(T), \|\cdot\|_G)$.
    $$ \left\|x_n - x\right\|_G = \left\|x_n - x\right\|_X + \left\|T(x_n) - T(x)\right\|_Y $$
    Puisque $T(x)=y$, nous avons :
    $$ \left\|x_n - x\right\|_G = \left\|x_n - x\right\|_X + \left\|T(x_n) - y\right\|_Y $$
    Comme $x_n \to x$ dans $X$, $\|x_n - x\|_X \to 0$.
    Comme $T(x_n) \to y$ dans $Y$, $\|T(x_n) - y\|_Y \to 0$.
    Par conséquent, $\|x_n - x\|_G \to 0$.
    La suite $(x_n)$ converge vers $x$ dans $(\mathcal{D}(T), \|\cdot\|_G)$.
    Donc, $(\mathcal{D}(T), \|\cdot\|_G)$ est un espace de Banach.

2.  **Linéarité, continuité de $T_G$ et son image :**
    L'opérateur $T_G: (\mathcal{D}(T), \|\cdot\|_G) \to Y$ est défini par $T_G(x) = T(x)$.
    *   **Linéarité :** $T_G$ est linéaire car $T$ est linéaire, et la définition de $T_G$ est simplement la restriction de $T$ au domaine $\mathcal{D}(T)$ avec une norme différente pour l'espace de départ.
    *   **Continuité :** Pour qu'un opérateur linéaire soit continu, il suffit de montrer qu'il est borné.
        $$ \left\|T_G(x)\right\|_Y = \left\|T(x)\right\|_Y $$
        Par définition de la norme du graphe, $\|x\|_G = \|x\|_X + \|T(x)\|_Y$.
        Il est clair que $\|T(x)\|_Y \le \|x\|_X + \|T(x)\|_Y = \|x\|_G$.
        Donc, $\left\|T_G(x)\right\|_Y \le \left\|x\right\|_G$ pour tout $x \in \mathcal{D}(T)$.
        Cela démontre que $T_G$ est continu avec une norme d'opérateur $\|T_G\| \le 1$.
    *   **Image :** L'image de $T_G$ est, par définition, $\mathcal{R}(T_G) = \{T_G(x) : x \in \mathcal{D}(T)\} = \{T(x) : x \in \mathcal{D}(T)\}$.
        Ceci est exactement $\mathcal{R}(T)$, l'image de $T$.

3.  **Utilisation du Théorème de l'Application Ouverte pour un isomorphisme topologique :**
    Nous voulons montrer que $T_G$ est un isomorphisme topologique de $(\mathcal{D}(T), \|\cdot\|_G)$ sur $\mathcal{R}(T)$.
    Pour cela, nous devons vérifier les conditions du Théorème de l'Application Ouverte pour l'opérateur $T_G: (\mathcal{D}(T), \|\cdot\|_G) \to (\mathcal{R}(T), \|\cdot\|_Y)$:
    *   **Espace de départ de Banach :** Nous avons démontré au point 1 que $(\mathcal{D}(T), \|\cdot\|_G)$ est un espace de Banach.
    *   **Espace d'arrivée de Banach :** L'espace d'arrivée est $\mathcal{R}(T)$ muni de la norme de $Y$. L'énoncé stipule que $\mathcal{R}(T)$ est un sous-espace fermé de $Y$. Comme $Y$ est un espace de Banach, tout sous-espace fermé de $Y$ est lui-même un espace de Banach. Donc $(\mathcal{R}(T), \|\cdot\|_Y)$ est un espace de Banach.
    *   **Opérateur linéaire et continu :** Nous l'avons démontré au point 2 que $T_G$ est linéaire et continu.
    *   **Opérateur surjectif :** L'opérateur $T_G$ est défini pour avoir pour espace d'arrivée $\mathcal{R}(T)$, donc par sa définition, $T_G$ est surjectif de $(\mathcal{D}(T), \|\cdot\|_G)$ sur $\mathcal{R}(T)$.

    Toutes les conditions du Théorème de l'Application Ouverte sont satisfaites.
    De plus, l'énoncé précise que $T$ est injectif. Donc $T_G$ est également injectif.
    Étant donné que $T_G$ est linéaire, continu, surjectif et injectif entre deux espaces de Banach, le Théorème de l'Application Ouverte garantit que $T_G$ est un isomorphisme topologique. Cela signifie que $T_G$ est une bijection continue dont l'inverse est également continu.

4.  **Déduction de la continuité de $T^{-1}$ :**
    Puisque $T_G: (\mathcal{D}(T), \|\cdot\|_G) \to (\mathcal{R}(T), \|\cdot\|_Y)$ est un isomorphisme topologique, son inverse $T_G^{-1}: (\mathcal{R}(T), \|\cdot\|_Y) \to (\mathcal{D}(T), \|\cdot\|_G)$ est également continu.
    L'opérateur $T^{-1}: \mathcal{R}(T) \to \mathcal{D}(T)$ est par définition l'inverse de $T$. Il est clair que $T_G^{-1}$ est précisément l'opérateur $T^{-1}$ muni de la norme du graphe sur son espace d'arrivée $\mathcal{D}(T)$.
    La continuité de $T_G^{-1}$ signifie qu'il existe une constante $M_2 > 0$ telle que pour tout $y \in \mathcal{R}(T)$,
    $$ \left\|T_G^{-1}(y)\right\|_G \le M_2 \left\|y\right\|_Y $$
    En remplaçant $T_G^{-1}(y)$ par $T^{-1}(y)$, nous obtenons la conclusion souhaitée :
    $$ \left\|T^{-1}(y)\right\|_G \le M_2 \left\|y\right\|_Y $$
    Ceci démontre que l'opérateur inverse $T^{-1}$ est continu de $(\mathcal{R}(T), \|\cdot\|_Y)$ vers $(\mathcal{D}(T), \|\cdot\|_G)$.