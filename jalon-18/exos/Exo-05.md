# Exercice 5 - Exploration Approfondie de la Continuité et de ses Applications

## Énoncé de l'exercice

### Partie A: Maîtrise de la Définition Epsilon-Delta

Soit la fonction $f: \mathbb{R}^* \to \mathbb{R}$ définie par $f(x) = \frac{\sqrt{1+x^2} - 1}{x^2}$.

1.  Montrer que $\lim_{x \to 0} f(x)$ existe et déterminer sa valeur $L$.
2.  En utilisant la définition $\epsilon-\delta$ de la continuité, montrer que la fonction $g: \mathbb{R} \to \mathbb{R}$ définie par $g(x) = f(x)$ pour $x \neq 0$ et $g(0) = L$ est continue en $x=0$.

### Partie B: Continuité des Fonctions Définies par Morceaux et Paramètres

Soit la fonction $h: \mathbb{R} \to \mathbb{R}$ définie par:
$$ h(x) = \begin{cases} \frac{\sin(ax)}{x} & \text{si } x < 0 \\ b & \text{si } x = 0 \\ \frac{e^{2x} - 1}{x} & \text{si } x > 0 \end{cases} $$
où $a$ et $b$ sont des constantes réelles.

1.  Déterminer les valeurs de $a$ et $b$ pour lesquelles $h$ est continue en $x=0$.
2.  Pour les valeurs de $a$ et $b$ trouvées, montrer que $h$ est continue sur $\mathbb{R}$.

### Partie C: Application du Théorème des Valeurs Intermédiaires (TVI) et Propriétés Globales

1.  Soit $P(x)$ un polynôme de degré impair. Montrer que $P(x)$ admet au moins une racine réelle.
2.  Soit $f: [0, 1] \to [0, 1]$ une fonction continue. Montrer qu'il existe au moins un point fixe $c \in [0, 1]$ tel que $f(c) = c$.
3.  Soit $f: \mathbb{R} \to \mathbb{R}$ une fonction continue telle que $\lim_{x \to -\infty} f(x) = -\infty$ et $\lim_{x \to +\infty} f(x) = +\infty$. Montrer que pour tout $y \in \mathbb{R}$, il existe $x \in \mathbb{R}$ tel que $f(x) = y$.

### Partie D: Un Défi Théorique (Équation Fonctionnelle de Cauchy)

Soit $f: \mathbb{R} \to \mathbb{R}$ une fonction continue telle que $f(x+y) = f(x) + f(y)$ pour tout $x, y \in \mathbb{R}$.

1.  Montrer que $f(nx) = nf(x)$ pour tout $n \in \mathbb{Z}$ et $x \in \mathbb{R}$.
2.  Montrer que $f(qx) = qf(x)$ pour tout $q \in \mathbb{Q}$ et $x \in \mathbb{R}$.
3.  En utilisant la continuité de $f$, montrer que $f(x) = cx$ pour une certaine constante $c \in \mathbb{R}$ et pour tout $x \in \mathbb{R}$.

---

## Correction de l'exercice

### Partie A: Maîtrise de la Définition Epsilon-Delta

1.  **Montrer que $\lim_{x \to 0} f(x)$ existe et déterminer sa valeur $L$.**

    Nous devons évaluer la limite $\lim_{x \to 0} \frac{\sqrt{1+x^2} - 1}{x^2}$.
    Lorsque $x \to 0$, le numérateur tend vers $\sqrt{1+0^2} - 1 = \sqrt{1} - 1 = 0$, et le dénominateur tend vers $0^2 = 0$. Il s'agit d'une forme indéterminée de type $\frac{0}{0}$.
    Pour lever l'indétermination, nous allons multiplier le numérateur et le dénominateur par l'expression conjuguée du numérateur, qui est $\sqrt{1+x^2} + 1$.

    $$ f(x) = \frac{\sqrt{1+x^2} - 1}{x^2} = \frac{(\sqrt{1+x^2} - 1)(\sqrt{1+x^2} + 1)}{x^2(\sqrt{1+x^2} + 1)} $$
    En utilisant l'identité $(A-B)(A+B) = A^2 - B^2$ pour le numérateur, avec $A = \sqrt{1+x^2}$ et $B = 1$:
    $$ f(x) = \frac{(\sqrt{1+x^2})^2 - 1^2}{x^2(\sqrt{1+x^2} + 1)} = \frac{(1+x^2) - 1}{x^2(\sqrt{1+x^2} + 1)} $$
    $$ f(x) = \frac{x^2}{x^2(\sqrt{1+x^2} + 1)} $$
    Puisque nous calculons la limite lorsque $x \to 0$, nous considérons des valeurs de $x$ qui sont proches de 0 mais non nulles. Par conséquent, $x^2 \neq 0$, et nous pouvons simplifier l'expression en divisant le numérateur et le dénominateur par $x^2$:
    $$ f(x) = \frac{1}{\sqrt{1+x^2} + 1} \quad \text{pour } x \neq 0 $$
    Maintenant, nous pouvons évaluer la limite par substitution directe, car le dénominateur ne tend pas vers zéro:
    $$ \lim_{x \to 0} f(x) = \lim_{x \to 0} \frac{1}{\sqrt{1+x^2} + 1} $$
    La fonction $x \mapsto x^2$ est continue en $x=0$, donc $\lim_{x \to 0} x^2 = 0$.
    La fonction $u \mapsto 1+u$ est continue, donc $\lim_{x \to 0} (1+x^2) = 1 + \lim_{x \to 0} x^2 = 1+0 = 1$.
    La fonction $v \mapsto \sqrt{v}$ est continue pour $v > 0$. Puisque $1+x^2 \to 1 > 0$, $\lim_{x \to 0} \sqrt{1+x^2} = \sqrt{\lim_{x \to 0} (1+x^2)} = \sqrt{1} = 1$.
    Par conséquent, $\lim_{x \to 0} (\sqrt{1+x^2} + 1) = \lim_{x \to 0} \sqrt{1+x^2} + \lim_{x \to 0} 1 = 1+1 = 2$.
    Enfin, la fonction $w \mapsto \frac{1}{w}$ est continue pour $w \neq 0$. Puisque le dénominateur tend vers $2 \neq 0$:
    $$ \lim_{x \to 0} f(x) = \frac{1}{2} $$
    La limite existe et sa valeur est $L = \frac{1}{2}$.

2.  **En utilisant la définition $\epsilon-\delta$ de la continuité, montrer que la fonction $g: \mathbb{R} \to \mathbb{R}$ définie par $g(x) = f(x)$ pour $x \neq 0$ et $g(0) = L$ est continue en $x=0$.**

    La fonction $g(x)$ est définie par:
    $$ g(x) = \begin{cases} \frac{1}{\sqrt{1+x^2} + 1} & \text{si } x \neq 0 \\ \frac{1}{2} & \text{si } x = 0 \end{cases} $$
    Pour montrer que $g$ est continue en $x=0$ en utilisant la définition $\epsilon-\delta$, nous devons montrer que pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que si $|x - 0| < \delta$, alors $|g(x) - g(0)| < \epsilon$.

    Soit $\epsilon > 0$ donné.
    Nous voulons trouver $\delta > 0$ tel que pour tout $x \in \mathbb{R}$ avec $|x| < \delta$, nous ayons $|g(x) - g(0)| < \epsilon$.

    Considérons deux cas:
    *   **Cas 1: $x = 0$**.
        Alors $|g(0) - g(0)| = |L - L| = 0$. Puisque $0 < \epsilon$ pour tout $\epsilon > 0$, la condition est satisfaite pour $x=0$.

    *   **Cas 2: $x \neq 0$**.
        Alors $g(x) = \frac{1}{\sqrt{1+x^2} + 1}$ et $g(0) = \frac{1}{2}$.
        Nous devons majorer l'expression $|g(x) - g(0)|$:
        $$ |g(x) - g(0)| = \left| \frac{1}{\sqrt{1+x^2} + 1} - \frac{1}{2} \right| $$
        Mettons les fractions sur un dénominateur commun:
        $$ = \left| \frac{2 - (\sqrt{1+x^2} + 1)}{2(\sqrt{1+x^2} + 1)} \right| = \left| \frac{1 - \sqrt{1+x^2}}{2(\sqrt{1+x^2} + 1)} \right| $$
        Pour simplifier le numérateur, multiplions-le par son conjugué $1 + \sqrt{1+x^2}$. Pour maintenir l'égalité, nous devons aussi multiplier le dénominateur par cette même expression:
        $$ = \left| \frac{(1 - \sqrt{1+x^2})(1 + \sqrt{1+x^2})}{2(\sqrt{1+x^2} + 1)(1 + \sqrt{1+x^2})} \right| $$
        En utilisant l'identité $(A-B)(A+B) = A^2 - B^2$ pour le numérateur, avec $A=1$ et $B=\sqrt{1+x^2}$:
        $$ = \left| \frac{1^2 - (\sqrt{1+x^2})^2}{2(\sqrt{1+x^2} + 1)^2} \right| = \left| \frac{1 - (1+x^2)}{2(\sqrt{1+x^2} + 1)^2} \right| $$
        $$ = \left| \frac{-x^2}{2(\sqrt{1+x^2} + 1)^2} \right| = \frac{|-x^2|}{2(\sqrt{1+x^2} + 1)^2} = \frac{x^2}{2(\sqrt{1+x^2} + 1)^2} $$
        Maintenant, nous devons trouver une borne inférieure pour le dénominateur afin de majorer l'expression.
        Puisque $x^2 \ge 0$, nous avons $1+x^2 \ge 1$.
        En prenant la racine carrée (la fonction racine carrée est croissante), $\sqrt{1+x^2} \ge \sqrt{1} = 1$.
        En ajoutant 1, $\sqrt{1+x^2} + 1 \ge 1+1 = 2$.
        En élevant au carré (les deux membres sont positifs), $(\sqrt{1+x^2} + 1)^2 \ge 2^2 = 4$.
        En multipliant par 2, $2(\sqrt{1+x^2} + 1)^2 \ge 2 \times 4 = 8$.
        Par conséquent, $\frac{1}{2(\sqrt{1+x^2} + 1)^2} \le \frac{1}{8}$.
        Ainsi, nous pouvons majorer $|g(x) - g(0)|$:
        $$ |g(x) - g(0)| = \frac{x^2}{2(\sqrt{1+x^2} + 1)^2} \le \frac{x^2}{8} $$
        Nous voulons que cette expression soit inférieure à $\epsilon$:
        $$ \frac{x^2}{8} < \epsilon $$
        $$ x^2 < 8\epsilon $$
        $$ |x| < \sqrt{8\epsilon} $$
        Nous pouvons donc choisir $\delta = \sqrt{8\epsilon}$.

    **Conclusion pour la définition $\epsilon-\delta$**:
    Pour tout $\epsilon > 0$, choisissons $\delta = \sqrt{8\epsilon}$.
    Si $|x - 0| < \delta$, c'est-à-dire $|x| < \sqrt{8\epsilon}$:
    *   Si $x=0$, alors $|g(0) - g(0)| = 0 < \epsilon$.
    *   Si $x \neq 0$, alors $|g(x) - g(0)| = \frac{x^2}{2(\sqrt{1+x^2} + 1)^2}$.
        Comme nous l'avons montré, $2(\sqrt{1+x^2} + 1)^2 \ge 8$, donc $\frac{1}{2(\sqrt{1+x^2} + 1)^2} \le \frac{1}{8}$.
        Ainsi, $|g(x) - g(0)| \le \frac{x^2}{8}$.
        Puisque $|x| < \sqrt{8\epsilon}$, nous avons $x^2 < 8\epsilon$.
        Par conséquent, $|g(x) - g(0)| \le \frac{x^2}{8} < \frac{8\epsilon}{8} = \epsilon$.
    Dans tous les cas, si $|x| < \delta$, alors $|g(x) - g(0)| < \epsilon$.
    La fonction $g$ est donc continue en $x=0$.

### Partie B: Continuité des Fonctions Définies par Morceaux et Paramètres

1.  **Déterminer les valeurs de $a$ et $b$ pour lesquelles $h$ est continue en $x=0$.**

    Pour que la fonction $h$ soit continue en $x=0$, il faut que la limite de $h(x)$ lorsque $x$ tend vers $0$ existe et soit égale à $h(0)$. Cela implique que les limites à gauche et à droite en $x=0$ doivent exister et être égales à $h(0)$.
    $$ \lim_{x \to 0^-} h(x) = \lim_{x \to 0^+} h(x) = h(0) $$

    *   **Valeur de $h(0)$**:
        Par définition, $h(0) = b$.

    *   **Limite à gauche en $x=0$**:
        Pour $x < 0$, $h(x) = \frac{\sin(ax)}{x}$.
        $$ \lim_{x \to 0^-} h(x) = \lim_{x \to 0^-} \frac{\sin(ax)}{x} $$
        Si $a=0$, alors $\lim_{x \to 0^-} \frac{\sin(0)}{x} = \lim_{x \to 0^-} \frac{0}{x} = 0$.
        Si $a \neq 0$, nous utilisons la limite fondamentale $\lim_{u \to 0} \frac{\sin u}{u} = 1$.
        Posons $u = ax$. Lorsque $x \to 0^-$, $u \to 0$.
        $$ \lim_{x \to 0^-} \frac{\sin(ax)}{x} = \lim_{x \to 0^-} a \cdot \frac{\sin(ax)}{ax} $$
        Par la propriété des limites, $\lim_{x \to 0^-} a \cdot \frac{\sin(ax)}{ax} = a \cdot \lim_{u \to 0} \frac{\sin u}{u} = a \cdot 1 = a$.
        Donc, $\lim_{x \to 0^-} h(x) = a$.

    *   **Limite à droite en $x=0$**:
        Pour $x > 0$, $h(x) = \frac{e^{2x} - 1}{x}$.
        $$ \lim_{x \to 0^+} h(x) = \lim_{x \to 0^+} \frac{e^{2x} - 1}{x} $$
        Nous utilisons la limite fondamentale $\lim_{u \to 0} \frac{e^u - 1}{u} = 1$.
        Posons $u = 2x$. Lorsque $x \to 0^+$, $u \to 0$.
        $$ \lim_{x \to 0^+} \frac{e^{2x} - 1}{x} = \lim_{x \to 0^+} 2 \cdot \frac{e^{2x} - 1}{2x} $$
        Par la propriété des limites, $\lim_{x \to 0^+} 2 \cdot \frac{e^{2x} - 1}{2x} = 2 \cdot \lim_{u \to 0} \frac{e^u - 1}{u} = 2 \cdot 1 = 2$.
        Donc, $\lim_{x \to 0^+} h(x) = 2$.

    Pour que $h$ soit continue en $x=0$, nous devons avoir $a = b = 2$.

2.  **Pour les valeurs de $a$ et $b$ trouvées, montrer que $h$ est continue sur $\mathbb{R}$.**

    Avec $a=2$ et $b=2$, la fonction $h(x)$ s'écrit:
    $$ h(x) = \begin{cases} \frac{\sin(2x)}{x} & \text{si } x < 0 \\ 2 & \text{si } x = 0 \\ \frac{e^{2x} - 1}{x} & \text{si } x > 0 \end{cases} $$
    Nous allons étudier la continuité sur les intervalles ouverts $(-\infty, 0)$, $(0, +\infty)$ et au point $x=0$.

    *   **Continuité sur $(-\infty, 0)$**:
        Pour $x < 0$, $h(x) = \frac{\sin(2x)}{x}$.
        La fonction $x \mapsto 2x$ est un polynôme, donc elle est continue sur $\mathbb{R}$.
        La fonction $u \mapsto \sin(u)$ est continue sur $\mathbb{R}$.
        Par composition, la fonction $x \mapsto \sin(2x)$ est continue sur $\mathbb{R}$.
        La fonction $x \mapsto x$ est un polynôme, donc elle est continue sur $\mathbb{R}$.
        Pour $x < 0$, le dénominateur $x$ est non nul.
        Puisque $h(x)$ est le quotient de deux fonctions continues dont le dénominateur est non nul sur $(-\infty, 0)$, $h$ est continue sur $(-\infty, 0)$.

    *   **Continuité sur $(0, +\infty)$**:
        Pour $x > 0$, $h(x) = \frac{e^{2x} - 1}{x}$.
        La fonction $x \mapsto 2x$ est continue sur $\mathbb{R}$.
        La fonction $u \mapsto e^u$ est continue sur $\mathbb{R}$.
        Par composition, la fonction $x \mapsto e^{2x}$ est continue sur $\mathbb{R}$.
        La fonction $x \mapsto e^{2x} - 1$ est la différence de fonctions continues, donc elle est continue sur $\mathbb{R}$.
        La fonction $x \mapsto x$ est continue sur $\mathbb{R}$.
        Pour $x > 0$, le dénominateur $x$ est non nul.
        Puisque $h(x)$ est le quotient de deux fonctions continues dont le dénominateur est non nul sur $(0, +\infty)$, $h$ est continue sur $(0, +\infty)$.

    *   **Continuité en $x=0$**:
        D'après la question B.1, nous avons choisi $a=2$ et $b=2$ précisément pour assurer la continuité en $x=0$.
        Nous avons montré que $\lim_{x \to 0^-} h(x) = a = 2$.
        Nous avons montré que $\lim_{x \to 0^+} h(x) = 2$.
        Et $h(0) = b = 2$.
        Puisque $\lim_{x \to 0^-} h(x) = \lim_{x \to 0^+} h(x) = h(0) = 2$, la fonction $h$ est continue en $x=0$.

    En combinant ces résultats, la fonction $h$ est continue sur $(-\infty, 0)$, sur $(0, +\infty)$ et au point $x=0$. Par conséquent, $h$ est continue sur $\mathbb{R}$.

### Partie C: Application du Théorème des Valeurs Intermédiaires (TVI) et Propriétés Globales

1.  **Soit $P(x)$ un polynôme de degré impair. Montrer que $P(x)$ admet au moins une racine réelle.**

    Soit $P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$, où $a_n \neq 0$ et $n$ est un entier impair.
    Les polynômes sont des fonctions continues sur $\mathbb{R}$.
    Pour montrer que $P(x)$ admet au moins une racine réelle, nous allons utiliser le Théorème des Valeurs Intermédiaires (TVI). Le TVI stipule que si une fonction $f$ est continue sur un intervalle $[u, v]$, alors pour toute valeur $k$ entre $f(u)$ et $f(v)$, il existe au moins un $c \in [u, v]$ tel que $f(c) = k$. Dans notre cas, nous voulons montrer l'existence d'un $c$ tel que $P(c) = 0$.

    Considérons le comportement de $P(x)$ lorsque $x \to \pm \infty$. Le comportement d'un polynôme est dominé par son terme de plus haut degré.
    $$ \lim_{x \to +\infty} P(x) = \lim_{x \to +\infty} a_n x^n $$
    $$ \lim_{x \to -\infty} P(x) = \lim_{x \to -\infty} a_n x^n $$
    Puisque $n$ est un entier impair:
    *   Si $a_n > 0$:
        $\lim_{x \to +\infty} x^n = +\infty$, donc $\lim_{x \to +\infty} P(x) = +\infty$.
        $\lim_{x \to -\infty} x^n = -\infty$, donc $\lim_{x \to -\infty} P(x) = -\infty$.
    *   Si $a_n < 0$:
        $\lim_{x \to +\infty} x^n = +\infty$, donc $\lim_{x \to +\infty} P(x) = -\infty$.
        $\lim_{x \to -\infty} x^n = -\infty$, donc $\lim_{x \to -\infty} P(x) = +\infty$.

    Dans les deux cas, les limites de $P(x)$ en $+\infty$ et en $-\infty$ sont de signes opposés.
    *   Si $a_n > 0$:
        Puisque $\lim_{x \to +\infty} P(x) = +\infty$, il existe un nombre réel $x_1$ suffisamment grand tel que $P(x_1) > 0$.
        Puisque $\lim_{x \to -\infty} P(x) = -\infty$, il existe un nombre réel $x_2$ suffisamment petit (négatif) tel que $P(x_2) < 0$.
        Nous avons donc $P(x_2) < 0 < P(x_1)$.
    *   Si $a_n < 0$:
        Puisque $\lim_{x \to +\infty} P(x) = -\infty$, il existe un nombre réel $x_1$ suffisamment grand tel que $P(x_1) < 0$.
        Puisque $\lim_{x \to -\infty} P(x) = +\infty$, il existe un nombre réel $x_2$ suffisamment petit (négatif) tel que $P(x_2) > 0$.
        Nous avons donc $P(x_1) < 0 < P(x_2)$.

    Dans les deux scénarios, nous pouvons trouver un intervalle $[x_a, x_b]$ (en prenant $x_a = \min(x_1, x_2)$ et $x_b = \max(x_1, x_2)$) tel que $P(x_a)$ et $P(x_b)$ sont de signes opposés.
    Puisque $P(x)$ est une fonction continue sur $\mathbb{R}$, elle est en particulier continue sur l'intervalle fermé $[x_a, x_b]$.
    Comme $P(x_a)$ et $P(x_b)$ sont de signes opposés, $0$ est une valeur intermédiaire entre $P(x_a)$ et $P(x_b)$.
    Par le Théorème des Valeurs Intermédiaires, il existe au moins un $c \in (x_a, x_b)$ tel que $P(c) = 0$.
    Ce $c$ est une racine réelle du polynôme $P(x)$.

2.  **Soit $f: [0, 1] \to [0, 1]$ une fonction continue. Montrer qu'il existe au moins un point fixe $c \in [0, 1]$ tel que $f(c) = c$.**

    Un point fixe $c$ est une valeur telle que $f(c) = c$. Cela est équivalent à $f(c) - c = 0$.
    Considérons la fonction auxiliaire $g: [0, 1] \to \mathbb{R}$ définie par $g(x) = f(x) - x$.
    *   **Continuité de $g$**:
        La fonction $f$ est continue sur $[0, 1]$ par hypothèse.
        La fonction $x \mapsto x$ est un polynôme, donc elle est continue sur $\mathbb{R}$, et en particulier sur $[0, 1]$.
        La fonction $g(x)$ est la différence de deux fonctions continues sur $[0, 1]$, elle est donc continue sur $[0, 1]$.

    *   **Évaluation de $g$ aux bornes de l'intervalle**:
        Calculons les valeurs de $g(x)$ aux extrémités de l'intervalle $[0, 1]$:
        *   $g(0) = f(0) - 0 = f(0)$.
            Puisque $f: [0, 1] \to [0, 1]$, cela signifie que l'image de $f$ est contenue dans $[0, 1]$. Donc $0 \le f(0) \le 1$.
            Par conséquent, $g(0) = f(0) \ge 0$.
        *   $g(1) = f(1) - 1$.
            Puisque $f: [0, 1] \to [0, 1]$, nous avons $0 \le f(1) \le 1$.
            Par conséquent, $f(1) - 1 \le 1 - 1 = 0$.
            Donc, $g(1) = f(1) - 1 \le 0$.

    *   **Application du Théorème des Valeurs Intermédiaires**:
        Nous avons $g(0) \ge 0$ et $g(1) \le 0$.
        Trois cas sont possibles:
        1.  Si $g(0) = 0$, alors $f(0) = 0$. Dans ce cas, $c=0$ est un point fixe.
        2.  Si $g(1) = 0$, alors $f(1) = 1$. Dans ce cas, $c=1$ est un point fixe.
        3.  Si $g(0) > 0$ et $g(1) < 0$. Dans ce cas, nous avons $g(1) < 0 < g(0)$.
            Puisque $g$ est continue sur l'intervalle fermé $[0, 1]$ et que $0$ est une valeur intermédiaire entre $g(1)$ et $g(0)$, le Théorème des Valeurs Intermédiaires garantit l'existence d'au moins un $c \in (0, 1)$ tel que $g(c) = 0$.
            Si $g(c) = 0$, alors $f(c) - c = 0$, ce qui signifie $f(c) = c$.

    Dans tous les cas, il existe au moins un point $c \in [0, 1]$ tel que $f(c) = c$.

3.  **Soit $f: \mathbb{R} \to \mathbb{R}$ une fonction continue telle que $\lim_{x \to -\infty} f(x) = -\infty$ et $\lim_{x \to +\infty} f(x) = +\infty$. Montrer que pour tout $y \in \mathbb{R}$, il existe $x \in \mathbb{R}$ tel que $f(x) = y$.**

    Nous voulons montrer que la fonction $f$ est surjective, c'est-à-dire que pour tout $y \in \mathbb{R}$ (valeur cible), il existe au moins un $x \in \mathbb{R}$ (antécédent) tel que $f(x) = y$.

    Soit $y \in \mathbb{R}$ une valeur arbitraire.
    *   **Utilisation de la limite en $-\infty$**:
        Puisque $\lim_{x \to -\infty} f(x) = -\infty$, par définition de la limite, pour tout nombre réel $M_1$, il existe un $A \in \mathbb{R}$ tel que pour tout $x < A$, $f(x) < M_1$.
        En particulier, choisissons $M_1 = y$. Il existe donc un $x_1 \in \mathbb{R}$ (en prenant $x_1 < A$) tel que $f(x_1) < y$.

    *   **Utilisation de la limite en $+\infty$**:
        Puisque $\lim_{x \to +\infty} f(x) = +\infty$, par définition de la limite, pour tout nombre réel $M_2$, il existe un $B \in \mathbb{R}$ tel que pour tout $x > B$, $f(x) > M_2$.
        En particulier, choisissons $M_2 = y$. Il existe donc un $x_2 \in \mathbb{R}$ (en prenant $x_2 > B$) tel que $f(x_2) > y$.

    *   **Application du Théorème des Valeurs Intermédiaires**:
        Nous avons trouvé deux points $x_1$ et $x_2$ tels que $f(x_1) < y$ et $f(x_2) > y$. Nous pouvons toujours choisir $x_1 < x_2$ en prenant $A$ suffisamment petit et $B$ suffisamment grand.
        La fonction $f$ est continue sur $\mathbb{R}$ par hypothèse, donc elle est continue sur l'intervalle fermé $[x_1, x_2]$.
        Puisque $f(x_1) < y < f(x_2)$, la valeur $y$ est une valeur intermédiaire entre $f(x_1)$ et $f(x_2)$.
        Par le Théorème des Valeurs Intermédiaires, il existe au moins un $c \in (x_1, x_2)$ tel que $f(c) = y$.

    Puisque $y$ a été choisi arbitrairement dans $\mathbb{R}$, nous avons montré que pour toute valeur réelle $y$, il existe un $x \in \mathbb{R}$ tel que $f(x) = y$. Cela signifie que $f$ est surjective.

### Partie D: Un Défi Théorique (Équation Fonctionnelle de Cauchy)

Soit $f: \mathbb{R} \to \mathbb{R}$ une fonction continue telle que $f(x+y) = f(x) + f(y)$ pour tout $x, y \in \mathbb{R}$.

1.  **Montrer que $f(nx) = nf(x)$ pour tout $n \in \mathbb{Z}$ et $x \in \mathbb{R}$.**

    Nous allons démontrer cette propriété par étapes.

    *   **Cas $n \in \mathbb{N}$ (entiers naturels)**:
        Nous utilisons une preuve par récurrence sur $n$.
        *   **Initialisation**: Pour $n=1$, $f(1x) = f(x)$, et $1f(x) = f(x)$. Donc $f(1x) = 1f(x)$ est vraie.
        *   **Hérédité**: Supposons que $f(kx) = kf(x)$ est vraie pour un certain entier naturel $k \ge 1$.
            Nous voulons montrer que $f((k+1)x) = (k+1)f(x)$.
            $f((k+1)x) = f(kx + x)$.
            En utilisant la propriété donnée $f(u+v) = f(u) + f(v)$ avec $u=kx$ et $v=x$:
            $f(kx + x) = f(kx) + f(x)$.
            Par l'hypothèse de récurrence, $f(kx) = kf(x)$.
            Donc, $f(kx) + f(x) = kf(x) + f(x) = (k+1)f(x)$.
            Ainsi, $f((k+1)x) = (k+1)f(x)$.
        *   **Conclusion**: Par le principe de récurrence, $f(nx) = nf(x)$ pour tout $n \in \mathbb{N}^*$.

    *   **Cas $n=0$**:
        Posons $x=0$ dans l'équation fonctionnelle: $f(0+0) = f(0) + f(0)$, ce qui donne $f(0) = 2f(0)$.
        En soustrayant $f(0)$ des deux côtés, nous obtenons $f(0) = 0$.
        Alors $f(0x) = f(0) = 0$. Et $0f(x) = 0$.
        Donc $f(0x) = 0f(x)$ est vraie.

    *   **Cas $n \in \mathbb{Z}^-$ (entiers négatifs)**:
        Soit $n$ un entier négatif. Alors $n = -m$ pour un certain entier naturel $m \in \mathbb{N}^*$.
        Nous savons que $f(0) = 0$.
        Nous pouvons écrire $f(0) = f(mx + (-m)x)$.
        En utilisant la propriété $f(u+v) = f(u) + f(v)$ avec $u=mx$ et $v=(-m)x$:
        $f(0) = f(mx) + f((-m)x)$.
        Puisque $f(0)=0$ et que $m \in \mathbb{N}^*$, nous avons $f(mx) = mf(x)$ d'après le cas des entiers naturels.
        Donc, $0 = mf(x) + f((-m)x)$.
        Cela implique $f((-m)x) = -mf(x)$.
        En substituant $n = -m$, nous obtenons $f(nx) = nf(x)$.

    En combinant tous les cas, nous avons montré que $f(nx) = nf(x)$ pour tout $n \in \mathbb{Z}$ et $x \in \mathbb{R}$.

2.  **Montrer que $f(qx) = qf(x)$ pour tout $q \in \mathbb{Q}$ et $x \in \mathbb{R}$.**

    Soit $q \in \mathbb{Q}$. Par définition, $q$ peut s'écrire sous la forme $\frac{m}{n}$, où $m \in \mathbb{Z}$ et $n \in \mathbb{N}^*$ (donc $n \neq 0$).
    Nous voulons montrer que $f\left(\frac{m}{n}x\right) = \frac{m}{n}f(x)$.

    De la question D.1, nous savons que $f(kx) = kf(x)$ pour tout $k \in \mathbb{Z}$.
    Considérons l'expression $f(nx)$. Nous pouvons écrire $nx = n \left(\frac{m}{n}x\right)$.
    En utilisant la propriété pour l'entier $n$:
    $$ f\left(n \left(\frac{m}{n}x\right)\right) = n f\left(\frac{m}{n}x\right) $$
    D'autre part, nous pouvons écrire $f(nx)$ comme $f(mx)$ en considérant $y = \frac{m}{n}x$, alors $ny = mx$.
    Donc, $f(ny) = nf(y)$.
    Et $f(mx) = mf(x)$.
    Ainsi, $nf\left(\frac{m}{n}x\right) = mf(x)$.
    Puisque $n \neq 0$, nous pouvons diviser par $n$:
    $$ f\left(\frac{m}{n}x\right) = \frac{m}{n}f(x) $$
    Donc, $f(qx) = qf(x)$ pour tout $q \in \mathbb{Q}$ et $x \in \mathbb{R}$.

    Un cas particulier important est lorsque $x=1$. Posons $c = f(1)$.
    Alors pour tout $q \in \mathbb{Q}$, $f(q) = f(q \cdot 1) = qf(1) = cq$.

3.  **En utilisant la continuité de $f$, montrer que $f(x) = cx$ pour une certaine constante $c \in \mathbb{R}$ et pour tout $x \in \mathbb{R}$.**

    De la question D.2, nous avons établi que $f(x) = cx$ pour tout $x \in \mathbb{Q}$, où $c = f(1)$.
    Nous voulons maintenant étendre cette propriété à tous les nombres réels $x \in \mathbb{R}$. C'est ici que la continuité de $f$ est cruciale.

    Soit $x \in \mathbb{R}$ un nombre réel arbitraire.
    Nous savons que l'ensemble des nombres rationnels $\mathbb{Q}$ est dense dans $\mathbb{R}$. Cela signifie que pour tout nombre réel $x$, il existe une suite de nombres rationnels $(q_k)_{k \in \mathbb{N}}$ telle que $\lim_{k \to \infty} q_k = x$.

    Puisque $f$ est continue sur $\mathbb{R}$ (par hypothèse), la continuité de $f$ implique que si une suite $(q_k)$ converge vers $x$, alors la suite des images $(f(q_k))$ converge vers $f(x)$.
    C'est-à-dire:
    $$ \lim_{k \to \infty} f(q_k) = f\left(\lim_{k \to \infty} q_k\right) = f(x) $$
    D'autre part, puisque chaque $q_k$ est un nombre rationnel, nous savons d'après la question D.2 que $f(q_k) = cq_k$ (où $c = f(1)$).
    Donc, nous pouvons écrire:
    $$ \lim_{k \to \infty} f(q_k) = \lim_{k \to \infty} (cq_k) $$
    Puisque $c$ est une constante, nous pouvons la sortir de la limite:
    $$ \lim_{k \to \infty} (cq_k) = c \lim_{k \to \infty} q_k $$
    Comme $\lim_{k \to \infty} q_k = x$, nous avons:
    $$ c \lim_{k \to \infty} q_k = cx $$
    En égalant les deux expressions pour la limite de $f(q_k)$:
    $$ f(x) = cx $$
    Cette relation est vraie pour tout $x \in \mathbb{R}$.
    La constante $c$ est déterminée par la valeur de $f(1)$. Si $f(1)=0$, alors $f(x)=0$ pour tout $x$. Si $f(1)=1$, alors $f(x)=x$ pour tout $x$.

    Ainsi, toute fonction continue $f: \mathbb{R} \to \mathbb{R}$ satisfaisant l'équation fonctionnelle de Cauchy $f(x+y) = f(x) + f(y)$ est nécessairement de la forme $f(x) = cx$ pour une constante $c \in \mathbb{R}$.
