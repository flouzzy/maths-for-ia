# Exercice 4 - Continuité et Propriétés Fondamentales des Fonctions Réelles

## Partie 1 : Analyse de la continuité ponctuelle et globale

Soit $f: \mathbb{R} \to \mathbb{R}$ la fonction définie par:
$$ f(x) = \begin{cases} \frac{\sin(x^2)}{x} & \text{si } x \neq 0 \\ 0 & \text{si } x = 0 \end{cases} $$

1.  Démontrer, en utilisant la définition $\epsilon-\delta$ de la continuité, que $f$ est continue en $x=0$.
2.  Démontrer que $f$ est continue sur $\mathbb{R}^* = \mathbb{R} \setminus \{0\}$.
3.  En déduire que $f$ est continue sur $\mathbb{R}$.

## Partie 2 : Applications des Théorèmes Fondamentaux

1.  Soit $h: [0, 1] \to [0, 1]$ une fonction continue. Démontrer que $h$ admet au moins un point fixe, c'est-à-dire qu'il existe $c \in [0, 1]$ tel que $h(c) = c$.
2.  Soit $P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$ un polynôme à coefficients réels, où $n$ est un entier impair et $a_n \neq 0$. Démontrer que $P(x)$ admet au moins une racine réelle.

## Partie 3 : Continuité Uniforme

1.  Rappeler la définition de la continuité uniforme d'une fonction $f: I \to \mathbb{R}$ sur un intervalle $I$.
2.  Démontrer que la fonction $f(x) = x^2$ n'est pas uniformément continue sur $\mathbb{R}$.
3.  Démontrer que la fonction $g(x) = \sqrt{x}$ est uniformément continue sur $[0, +\infty)$.

---

# Correction de l'Exercice 4

## Partie 1 : Analyse de la continuité ponctuelle et globale

1.  **Démonstration de la continuité de $f$ en $x=0$ par la définition $\epsilon-\delta$ :**
    La fonction $f$ est continue en $x=0$ si et seulement si pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que pour tout $x \in \mathbb{R}$, si $|x - 0| < \delta$, alors $|f(x) - f(0)| < \epsilon$.
    Nous avons $f(0) = 0$. Pour $x \neq 0$, $f(x) = \frac{\sin(x^2)}{x}$.
    Nous devons donc montrer que pour tout $\epsilon > 0$, il existe $\delta > 0$ tel que si $0 < |x| < \delta$, alors $\left| \frac{\sin(x^2)}{x} - 0 \right| < \epsilon$.
    Considérons l'expression $\left| \frac{\sin(x^2)}{x} \right|$ pour $x \neq 0$.
    Nous pouvons la réécrire comme $\left| \frac{\sin(x^2)}{x^2} \cdot x \right| = \left| \frac{\sin(x^2)}{x^2} \right| \cdot |x|$.
    Nous utilisons l'inégalité fondamentale $|\sin(u)| \le |u|$ pour tout $u \in \mathbb{R}$.
    Si $u \neq 0$, alors $\left| \frac{\sin(u)}{u} \right| \le 1$.
    En particulier, pour $x \neq 0$, $x^2 \neq 0$, donc nous avons $\left| \frac{\sin(x^2)}{x^2} \right| \le 1$.
    Par conséquent, pour tout $x \neq 0$, nous avons $|f(x) - f(0)| = \left| \frac{\sin(x^2)}{x^2} \right| \cdot |x| \le 1 \cdot |x| = |x|$.
    Soit $\epsilon > 0$ donné. Nous voulons que $|f(x) - f(0)| < \epsilon$.
    Puisque nous avons montré que $|f(x) - f(0)| \le |x|$, il suffit de choisir $\delta$ tel que $|x| < \delta$ implique $|x| < \epsilon$.
    Nous pouvons donc choisir $\delta = \epsilon$.
    Vérification : Soit $\epsilon > 0$. Choisissons $\delta = \epsilon$.
    Si $x \in \mathbb{R}$ et $0 < |x| < \delta$, alors $0 < |x| < \epsilon$.
    Pour ces valeurs de $x$, nous avons $|f(x) - f(0)| = \left| \frac{\sin(x^2)}{x} \right| = \left| \frac{\sin(x^2)}{x^2} \right| \cdot |x|$.
    Puisque $x \neq 0$, $x^2 \neq 0$, et nous savons que $\left| \frac{\sin(u)}{u} \right| \le 1$ pour $u \neq 0$.
    Donc, $\left| \frac{\sin(x^2)}{x^2} \right| \le 1$.
    Par conséquent, $|f(x) - f(0)| \le 1 \cdot |x| = |x|$.
    Comme $|x| < \delta = \epsilon$, nous avons $|f(x) - f(0)| < \epsilon$.
    La fonction $f$ est donc continue en $x=0$.

2.  **Démonstration de la continuité de $f$ sur $\mathbb{R}^*$ :**
    Pour tout $x \in \mathbb{R}^*$, la fonction $f(x)$ est définie par $f(x) = \frac{\sin(x^2)}{x}$.
    Considérons les fonctions suivantes :
    *   La fonction $g_1(x) = x^2$. C'est une fonction polynomiale, donc elle est continue sur $\mathbb{R}$. En particulier, elle est continue sur $\mathbb{R}^*$.
    *   La fonction $g_2(u) = \sin(u)$. C'est une fonction trigonométrique élémentaire, donc elle est continue sur $\mathbb{R}$.
    La fonction $g_3(x) = \sin(x^2)$ est la composition de $g_2$ et $g_1$, c'est-à-dire $g_3(x) = g_2(g_1(x))$. Puisque $g_1$ est continue sur $\mathbb{R}$ et $g_2$ est continue sur $\mathbb{R}$, leur composition $g_3$ est continue sur $\mathbb{R}$. En particulier, $g_3$ est continue sur $\mathbb{R}^*$.
    *   La fonction $g_4(x) = x$. C'est une fonction polynomiale, donc elle est continue sur $\mathbb{R}$. En particulier, elle est continue sur $\mathbb{R}^*$.
    De plus, pour tout $x \in \mathbb{R}^*$, $g_4(x) = x \neq 0$.
    La fonction $f(x)$ est le quotient de $g_3(x)$ et $g_4(x)$, c'est-à-dire $f(x) = \frac{g_3(x)}{g_4(x)}$.
    Le théorème sur la continuité des quotients de fonctions stipule que si $A(x)$ et $B(x)$ sont continues sur un intervalle $I$ et $B(x) \neq 0$ pour tout $x \in I$, alors $\frac{A(x)}{B(x)}$ est continue sur $I$.
    Ici, $A(x) = \sin(x^2)$ est continue sur $\mathbb{R}^*$ et $B(x) = x$ est continue sur $\mathbb{R}^*$ et non nulle sur $\mathbb{R}^*$.
    Par conséquent, $f(x) = \frac{\sin(x^2)}{x}$ est continue sur $\mathbb{R}^*$.

3.  **Conclusion sur la continuité de $f$ sur $\mathbb{R}$ :**
    D'après la question 1, nous avons démontré que $f$ est continue au point $x=0$.
    D'après la question 2, nous avons démontré que $f$ est continue sur l'ensemble $\mathbb{R}^* = \mathbb{R} \setminus \{0\}$.
    L'ensemble $\mathbb{R}$ est l'union de $\mathbb{R}^*$ et du point $\{0\}$, c'est-à-dire $\mathbb{R} = \mathbb{R}^* \cup \{0\}$.
    Puisque $f$ est continue en chaque point de $\mathbb{R}^*$ et également au point $0$, nous pouvons conclure que $f$ est continue sur tout $\mathbb{R}$.

## Partie 2 : Applications des Théorèmes Fondamentaux

1.  **Démonstration de l'existence d'un point fixe pour $h: [0, 1] \to [0, 1]$ continue :**
    Soit $h: [0, 1] \to [0, 1]$ une fonction continue. Nous cherchons à montrer qu'il existe $c \in [0, 1]$ tel que $h(c) = c$.
    Considérons la fonction auxiliaire $g: [0, 1] \to \mathbb{R}$ définie par $g(x) = h(x) - x$.
    *   **Continuité de $g$ :** La fonction $h$ est continue sur $[0, 1]$ par hypothèse. La fonction $k(x) = x$ est une fonction polynomiale, donc elle est continue sur $\mathbb{R}$, et par conséquent continue sur $[0, 1]$. La différence de deux fonctions continues est continue, donc $g(x) = h(x) - x$ est continue sur l'intervalle fermé et borné $[0, 1]$.
    *   **Évaluation aux bornes de l'intervalle :**
        *   En $x=0$: $g(0) = h(0) - 0 = h(0)$. Puisque le codomaine de $h$ est $[0, 1]$, nous savons que $h(0) \in [0, 1]$. Par conséquent, $h(0) \ge 0$, ce qui implique $g(0) \ge 0$.
        *   En $x=1$: $g(1) = h(1) - 1$. Puisque le codomaine de $h$ est $[0, 1]$, nous savons que $h(1) \in [0, 1]$. Par conséquent, $h(1) \le 1$, ce qui implique $h(1) - 1 \le 0$, donc $g(1) \le 0$.
    *   **Application du Théorème des Valeurs Intermédiaires (TVI) :**
        Nous avons trois cas possibles :
        1.  Si $g(0) = 0$, alors $h(0) - 0 = 0$, ce qui signifie $h(0) = 0$. Dans ce cas, $c=0$ est un point fixe.
        2.  Si $g(1) = 0$, alors $h(1) - 1 = 0$, ce qui signifie $h(1) = 1$. Dans ce cas, $c=1$ est un point fixe.
        3.  Si $g(0) > 0$ et $g(1) < 0$. Dans ce cas, $g(0)$ et $g(1)$ ont des signes opposés. Puisque $g$ est continue sur l'intervalle fermé $[0, 1]$, et que $0$ est une valeur comprise entre $g(1)$ et $g(0)$, le Théorème des Valeurs Intermédiaires garantit l'existence d'au moins un $c \in (0, 1)$ tel que $g(c) = 0$.
            Le TVI stipule que si une fonction $f$ est continue sur un intervalle fermé $[a, b]$, alors pour toute valeur $y_0$ entre $f(a)$ et $f(b)$ (inclusivement), il existe au moins un $c \in [a, b]$ tel que $f(c) = y_0$.
            Ici, $a=0$, $b=1$, et $y_0=0$ est entre $g(1)$ et $g(0)$.
            Donc, il existe $c \in (0, 1)$ tel que $g(c) = 0$.
            Cela signifie $h(c) - c = 0$, d'où $h(c) = c$.
    Dans tous les cas, il existe au moins un $c \in [0, 1]$ tel que $h(c) = c$. Ce $c$ est un point fixe de $h$.

2.  **Démonstration de l'existence d'une racine réelle pour un polynôme de degré impair :**
    Soit $P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$ un polynôme à coefficients réels, où $n$ est un entier impair et $a_n \neq 0$. Nous voulons démontrer que $P(x)$ admet au moins une racine réelle.
    *   **Continuité de $P$ :** Toute fonction polynomiale est continue sur $\mathbb{R}$. Par conséquent, $P(x)$ est continue sur $\mathbb{R}$.
    *   **Comportement aux limites :** Nous allons examiner les limites de $P(x)$ lorsque $x \to +\infty$ et $x \to -\infty$. Le comportement d'un polynôme pour de grandes valeurs absolues de $x$ est dominé par son terme de plus haut degré, $a_n x^n$.
        Nous pouvons factoriser $a_n x^n$:
        $$ P(x) = a_n x^n \left( 1 + \frac{a_{n-1}}{a_n x} + \frac{a_{n-2}}{a_n x^2} + \dots + \frac{a_0}{a_n x^n} \right) $$
        Lorsque $x \to +\infty$, tous les termes $\frac{a_{k}}{a_n x^{n-k}}$ pour $k < n$ tendent vers $0$.
        Donc, $\lim_{x \to +\infty} \left( 1 + \frac{a_{n-1}}{a_n x} + \dots + \frac{a_0}{a_n x^n} \right) = 1$.
        Par conséquent, $\lim_{x \to +\infty} P(x) = \lim_{x \to +\infty} (a_n x^n \cdot 1) = \lim_{x \to +\infty} a_n x^n$.
        Puisque $n$ est un entier impair :
        *   Si $a_n > 0$, alors $\lim_{x \to +\infty} x^n = +\infty$, donc $\lim_{x \to +\infty} P(x) = +\infty$.
        *   Si $a_n < 0$, alors $\lim_{x \to +\infty} x^n = +\infty$, donc $\lim_{x \to +\infty} P(x) = -\infty$.

        De même, lorsque $x \to -\infty$:
        $\lim_{x \to -\infty} P(x) = \lim_{x \to -\infty} a_n x^n$.
        Puisque $n$ est un entier impair, $x^n$ a le même signe que $x$. Donc, $\lim_{x \to -\infty} x^n = -\infty$.
        *   Si $a_n > 0$, alors $\lim_{x \to -\infty} P(x) = -\infty$.
        *   Si $a_n < 0$, alors $\lim_{x \to -\infty} P(x) = +\infty$.

    *   **Synthèse des limites et application du TVI :**
        Nous observons que dans tous les cas, les limites de $P(x)$ en $+\infty$ et en $-\infty$ sont de signes opposés :
        *   Si $a_n > 0$: $\lim_{x \to -\infty} P(x) = -\infty$ et $\lim_{x \to +\infty} P(x) = +\infty$.
        *   Si $a_n < 0$: $\lim_{x \to -\infty} P(x) = +\infty$ et $\lim_{x \to +\infty} P(x) = -\infty$.

        Cela signifie qu'il existe des valeurs $x_1$ et $x_2$ telles que $P(x_1)$ et $P(x_2)$ ont des signes opposés.
        Plus précisément :
        *   Si $a_n > 0$: Puisque $\lim_{x \to -\infty} P(x) = -\infty$, il existe un $x_1 \in \mathbb{R}$ (suffisamment petit) tel que $P(x_1) < 0$. Puisque $\lim_{x \to +\infty} P(x) = +\infty$, il existe un $x_2 \in \mathbb{R}$ (suffisamment grand) tel que $P(x_2) > 0$. Nous pouvons choisir $x_1 < x_2$.
        *   Si $a_n < 0$: Puisque $\lim_{x \to -\infty} P(x) = +\infty$, il existe un $x_1 \in \mathbb{R}$ (suffisamment petit) tel que $P(x_1) > 0$. Puisque $\lim_{x \to +\infty} P(x) = -\infty$, il existe un $x_2 \in \mathbb{R}$ (suffisamment grand) tel que $P(x_2) < 0$. Nous pouvons choisir $x_1 < x_2$.

        Dans les deux cas, nous avons trouvé un intervalle fermé et borné $[x_1, x_2]$ sur lequel $P(x)$ est continue (car $P$ est continue sur $\mathbb{R}$), et les valeurs $P(x_1)$ et $P(x_2)$ ont des signes opposés.
        Par le Théorème des Valeurs Intermédiaires (TVI), puisque $0$ est une valeur comprise entre $P(x_1)$ et $P(x_2)$, il existe au moins un $c \in (x_1, x_2)$ tel que $P(c) = 0$.
        Ce $c$ est une racine réelle du polynôme $P(x)$.
        Par conséquent, tout polynôme de degré impair à coefficients réels admet au moins une racine réelle.

## Partie 3 : Continuité Uniforme

1.  **Définition de la continuité uniforme :**
    Une fonction $f: I \to \mathbb{R}$ est dite uniformément continue sur un intervalle $I$ si pour tout $\epsilon > 0$, il existe un $\delta > 0$ (qui ne dépend que de $\epsilon$ et de $f$, mais pas des points $x$ et $y$ spécifiques dans $I$) tel que pour tous $x, y \in I$, si $|x - y| < \delta$, alors $|f(x) - f(y)| < \epsilon$.

2.  **Démonstration que $f(x) = x^2$ n'est pas uniformément continue sur $\mathbb{R}$ :**
    Pour montrer que $f(x) = x^2$ n'est pas uniformément continue sur $\mathbb{R}$, nous devons nier la définition de la continuité uniforme. Cela signifie qu'il existe un $\epsilon_0 > 0$ tel que pour tout $\delta > 0$, il existe des $x, y \in \mathbb{R}$ tels que $|x - y| < \delta$ mais $|f(x) - f(y)| \ge \epsilon_0$.
    Choisissons $\epsilon_0 = 1$.
    Soit $\delta > 0$ un nombre réel arbitraire. Nous devons trouver $x, y \in \mathbb{R}$ tels que $|x - y| < \delta$ et $|x^2 - y^2| \ge 1$.
    Considérons l'expression $|x^2 - y^2| = |(x - y)(x + y)| = |x - y| |x + y|$.
    Pour satisfaire la condition $|x - y| < \delta$, nous pouvons choisir $y = x + \frac{\delta}{2}$.
    Alors $|x - y| = \left| x - \left(x + \frac{\delta}{2}\right) \right| = \left| -\frac{\delta}{2} \right| = \frac{\delta}{2}$.
    Puisque $\delta > 0$, nous avons $\frac{\delta}{2} < \delta$, donc la première condition est satisfaite.
    Maintenant, substituons ces valeurs dans l'expression de $|f(x) - f(y)|$:
    $|f(x) - f(y)| = \left| \frac{\delta}{2} \right| \left| x + \left(x + \frac{\delta}{2}\right) \right| = \frac{\delta}{2} \left| 2x + \frac{\delta}{2} \right|$.
    Nous voulons que cette expression soit supérieure ou égale à $\epsilon_0 = 1$.
    C'est-à-dire, nous voulons $\frac{\delta}{2} \left| 2x + \frac{\delta}{2} \right| \ge 1$.
    Cela est équivalent à $\left| 2x + \frac{\delta}{2} \right| \ge \frac{2}{\delta}$.
    Nous pouvons choisir $x$ de manière à satisfaire cette inégalité. Par exemple, choisissons $2x + \frac{\delta}{2} = \frac{2}{\delta}$.
    Alors $2x = \frac{2}{\delta} - \frac{\delta}{2}$, ce qui donne $x = \frac{1}{\delta} - \frac{\delta}{4}$.
    Avec ce choix de $x$, $y = x + \frac{\delta}{2} = \left( \frac{1}{\delta} - \frac{\delta}{4} \right) + \frac{\delta}{2} = \frac{1}{\delta} + \frac{\delta}{4}$.
    Pour tout $\delta > 0$ donné, nous avons trouvé $x = \frac{1}{\delta} - \frac{\delta}{4}$ et $y = \frac{1}{\delta} + \frac{\delta}{4}$.
    Vérifions les conditions :
    1.  $|x - y| = \left| \left(\frac{1}{\delta} - \frac{\delta}{4}\right) - \left(\frac{1}{\delta} + \frac{\delta}{4}\right) \right| = \left| -\frac{\delta}{2} \right| = \frac{\delta}{2}$. Puisque $\frac{\delta}{2} < \delta$, la première condition est satisfaite.
    2.  $|f(x) - f(y)| = |x^2 - y^2| = |(x-y)(x+y)| = \left| -\frac{\delta}{2} \right| \left| \left(\frac{1}{\delta} - \frac{\delta}{4}\right) + \left(\frac{1}{\delta} + \frac{\delta}{4}\right) \right|$
        $= \frac{\delta}{2} \left| \frac{2}{\delta} \right| = \frac{\delta}{2} \cdot \frac{2}{\delta} = 1$.
    Nous avons donc trouvé, pour tout $\delta > 0$, des points $x, y \in \mathbb{R}$ tels que $|x - y| < \delta$ mais $|f(x) - f(y)| = 1$.
    Puisque $1 \ge \epsilon_0 = 1$, la condition de non-uniforme continuité est satisfaite.
    Par conséquent, la fonction $f(x) = x^2$ n'est pas uniformément continue sur $\mathbb{R}$.

3.  **Démonstration que $g(x) = \sqrt{x}$ est uniformément continue sur $[0, +\infty)$ :**
    Nous voulons montrer que pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que pour tous $x, y \in [0, +\infty)$, si $|x - y| < \delta$, alors $|\sqrt{x} - \sqrt{y}| < \epsilon$.
    Soit $\epsilon > 0$ donné.
    Considérons l'expression $|\sqrt{x} - \sqrt{y}|$.
    Nous allons d'abord établir une inégalité utile : $|\sqrt{x} - \sqrt{y}| \le \sqrt{|x - y|}$ pour tous $x, y \ge 0$.
    **Preuve de l'inégalité $|\sqrt{x} - \sqrt{y}| \le \sqrt{|x - y|}$ :**
    Sans perte de généralité, supposons $x \ge y$. Alors $|x - y| = x - y$ et $|\sqrt{x} - \sqrt{y}| = \sqrt{x} - \sqrt{y}$ (puisque $\sqrt{x} \ge \sqrt{y}$ car la fonction racine carrée est croissante).
    Nous voulons montrer $\sqrt{x} - \sqrt{y} \le \sqrt{x - y}$.
    Puisque les deux membres de l'inégalité sont non-négatifs (car $x \ge y \ge 0$), nous pouvons élever les deux côtés au carré sans changer le sens de l'inégalité :
    $(\sqrt{x} - \sqrt{y})^2 \le (\sqrt{x - y})^2$
    $x - 2\sqrt{xy} + y \le x - y$
    Soustraire $x$ des deux côtés :
    $-2\sqrt{xy} + y \le -y$
    Ajouter $y$ aux deux côtés :
    $-2\sqrt{xy} \le -2y$
    Diviser par $-2$ et inverser le sens de l'inégalité :
    $\sqrt{xy} \ge y$
    Si $y=0$, l'inégalité devient $\sqrt{x \cdot 0} \ge 0$, soit $0 \ge 0$, ce qui est vrai.
    Si $y > 0$, nous pouvons diviser par $\sqrt{y}$ (qui est positif) :
    $\sqrt{x} \ge \sqrt{y}$
    Cette dernière inégalité est vraie car nous avons supposé $x \ge y$ et la fonction racine carrée est croissante.
    Puisque toutes les étapes sont réversibles (en respectant les conditions de non-négativité pour le carré et de non-nullité pour la division), l'inégalité originale $|\sqrt{x} - \sqrt{y}| \le \sqrt{|x - y|}$ est vraie pour $x \ge y$.
    Par symétrie, si $y \ge x$, alors $|\sqrt{y} - \sqrt{x}| \le \sqrt{|y - x|}$, ce qui est équivalent à $|\sqrt{x} - \sqrt{y}| \le \sqrt{|x - y|}$.
    L'inégalité $|\sqrt{x} - \sqrt{y}| \le \sqrt{|x - y|}$ est donc établie pour tous $x, y \in [0, +\infty)$.

    **Application de l'inégalité pour la continuité uniforme :**
    Nous voulons que $|\sqrt{x} - \sqrt{y}| < \epsilon$.
    En utilisant l'inégalité que nous venons de prouver, si nous assurons que $\sqrt{|x - y|} < \epsilon$, alors nous aurons $|\sqrt{x} - \sqrt{y}| < \epsilon$.
    Pour que $\sqrt{|x - y|} < \epsilon$, il suffit que $|x - y| < \epsilon^2$.
    Nous pouvons donc choisir $\delta = \epsilon^2$.

    **Vérification finale :**
    Soit $\epsilon > 0$ donné.
    Choisissons $\delta = \epsilon^2$.
    Soient $x, y \in [0, +\infty)$ tels que $|x - y| < \delta$.
    Nous voulons montrer que $|\sqrt{x} - \sqrt{y}| < \epsilon$.
    D'après l'inégalité établie, nous avons $|\sqrt{x} - \sqrt{y}| \le \sqrt{|x - y|}$.
    Puisque $|x - y| < \delta$, nous avons $\sqrt{|x - y|} < \sqrt{\delta}$.
    En substituant $\delta = \epsilon^2$, nous obtenons $\sqrt{\delta} = \sqrt{\epsilon^2} = \epsilon$ (car $\epsilon > 0$).
    Par conséquent, $|\sqrt{x} - \sqrt{y}| \le \sqrt{|x - y|} < \sqrt{\delta} = \epsilon$.
    Ainsi, pour tout $\epsilon > 0$, nous avons trouvé un $\delta = \epsilon^2 > 0$ tel que pour tous $x, y \in [0, +\infty)$, si $|x - y| < \delta$, alors $|\sqrt{x} - \sqrt{y}| < \epsilon$.
    Ceci démontre que la fonction $g(x) = \sqrt{x}$ est uniformément continue sur $[0, +\infty)$.
