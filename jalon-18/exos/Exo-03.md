# Exercice 3 - Exploration Approfondie de la Continuité

Cet exercice vise à consolider votre compréhension de la continuité des fonctions d'une variable réelle, depuis sa définition formelle jusqu'à ses applications fondamentales.

**Partie A : Maîtrise de la définition formelle de la continuité.**

Soit la fonction $f$ définie sur $\mathbb{R}$ par $f(x) = x^2 - 2x + 3$.
En utilisant la définition $\epsilon-\delta$ de la continuité, démontrez que $f$ est continue au point $x_0 = 1$.

**Partie B : Analyse de la continuité sur un intervalle.**

Considérons la fonction $g$ définie par morceaux sur $\mathbb{R}$ comme suit :
$$ g(x) = \begin{cases} \frac{x^2 - 4}{x - 2} & \text{si } x < 2 \\ ax + b & \text{si } 2 \le x \le 3 \\ \sqrt{x^2 + 7} & \text{si } x > 3 \end{cases} $$
Déterminez les valeurs des constantes réelles $a$ et $b$ pour que la fonction $g$ soit continue sur l'ensemble de son domaine de définition, $\mathbb{R}$.

**Partie C : Application du Théorème des Valeurs Intermédiaires.**

Soit l'équation $(E) : x^3 - 3x + 1 = 0$.
1.  Montrez que l'équation $(E)$ possède au moins une solution réelle dans l'intervalle $(0, 1)$.
2.  Montrez que l'équation $(E)$ possède au moins une solution réelle dans l'intervalle $(-2, -1)$.
3.  En déduire que l'équation $(E)$ possède au moins deux solutions réelles distinctes.

---

# Correction de l'Exercice 3 - Exploration Approfondie de la Continuité

## Partie A : Maîtrise de la définition formelle de la continuité.

Nous devons démontrer que la fonction $f(x) = x^2 - 2x + 3$ est continue au point $x_0 = 1$ en utilisant la définition $\epsilon-\delta$.
La fonction $f$ est continue en $x_0 = 1$ si et seulement si pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que pour tout $x \in \mathbb{R}$, si $|x - 1| < \delta$, alors $|f(x) - f(1)| < \epsilon$.

Calculons d'abord la valeur de la fonction $f$ au point $x_0 = 1$:
$$ f(1) = (1)^2 - 2(1) + 3 = 1 - 2 + 3 = 2 $$

Nous devons donc montrer que pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que si $|x - 1| < \delta$, alors $|(x^2 - 2x + 3) - 2| < \epsilon$.
Simplifions l'expression $|f(x) - f(1)|$:
$$ |f(x) - f(1)| = |x^2 - 2x + 3 - 2| $$
$$ |f(x) - f(1)| = |x^2 - 2x + 1| $$
Nous reconnaissons l'identité remarquable $A^2 - 2AB + B^2 = (A - B)^2$. Ici, $A=x$ et $B=1$.
Donc, nous pouvons factoriser l'expression $x^2 - 2x + 1$ comme suit :
$$ x^2 - 2x + 1 = (x - 1)^2 $$
En substituant cette factorisation dans l'expression de la valeur absolue, nous obtenons :
$$ |f(x) - f(1)| = |(x - 1)^2| $$
Puisque le carré d'un nombre réel est toujours positif ou nul, c'est-à-dire $(x-1)^2 \ge 0$ pour tout $x \in \mathbb{R}$, la valeur absolue de $(x-1)^2$ est $(x-1)^2$ elle-même.
$$ |f(x) - f(1)| = (x - 1)^2 $$
Nous voulons que cette quantité soit inférieure à $\epsilon$, c'est-à-dire $(x - 1)^2 < \epsilon$.
Pour que $(x - 1)^2 < \epsilon$, il est nécessaire et suffisant que $|x - 1| < \sqrt{\epsilon}$.

Soit $\epsilon > 0$ un nombre réel arbitrairement choisi.
Nous cherchons un $\delta > 0$ tel que si $|x - 1| < \delta$, alors $|f(x) - f(1)| < \epsilon$.
Choisissons $\delta = \sqrt{\epsilon}$. Puisque $\epsilon > 0$, $\sqrt{\epsilon}$ est un nombre réel positif, donc $\delta > 0$.
Maintenant, supposons que $|x - 1| < \delta$.
En substituant la valeur de $\delta$, nous avons :
$$ |x - 1| < \sqrt{\epsilon} $$
Puisque les deux membres de cette inégalité sont positifs (la valeur absolue est non négative et $\sqrt{\epsilon}$ est positif), nous pouvons élever les deux membres au carré sans changer le sens de l'inégalité :
$$ (|x - 1|)^2 < (\sqrt{\epsilon})^2 $$
$$ (x - 1)^2 < \epsilon $$
Comme nous l'avons établi précédemment, $|f(x) - f(1)| = (x - 1)^2$.
Donc, nous avons :
$$ |f(x) - f(1)| < \epsilon $$
Nous avons ainsi démontré que pour tout $\epsilon > 0$, il existe un $\delta = \sqrt{\epsilon} > 0$ tel que si $|x - 1| < \delta$, alors $|f(x) - f(1)| < \epsilon$.
Par conséquent, la fonction $f$ est continue au point $x_0 = 1$ selon la définition $\epsilon-\delta$.

## Partie B : Analyse de la continuité sur un intervalle.

La fonction $g$ est définie par morceaux. Pour qu'elle soit continue sur $\mathbb{R}$, elle doit être continue sur chaque intervalle ouvert où elle est définie par une seule expression, et elle doit être continue aux points de raccordement.

1.  **Continuité sur les intervalles ouverts :**
    *   Pour $x < 2$, $g(x) = \frac{x^2 - 4}{x - 2}$. Cette fonction est un quotient de deux polynômes, $P(x) = x^2 - 4$ et $Q(x) = x - 2$. Les polynômes sont des fonctions continues sur $\mathbb{R}$. Le dénominateur $Q(x) = x - 2$ est non nul pour $x < 2$. Par conséquent, $g$ est continue sur l'intervalle $(-\infty, 2)$ en tant que quotient de fonctions continues dont le dénominateur ne s'annule pas.
    *   Pour $2 < x < 3$, $g(x) = ax + b$. Cette fonction est un polynôme de degré 1. Les polynômes sont des fonctions continues sur $\mathbb{R}$. Par conséquent, $g$ est continue sur l'intervalle $(2, 3)$.
    *   Pour $x > 3$, $g(x) = \sqrt{x^2 + 7}$. Cette fonction est une composition de deux fonctions : $h_1(x) = x^2 + 7$ et $h_2(y) = \sqrt{y}$. La fonction $h_1(x)$ est un polynôme, donc continue sur $\mathbb{R}$. Pour $x > 3$, $x^2 > 9$, donc $x^2 + 7 > 16 > 0$. La fonction $h_2(y) = \sqrt{y}$ est continue pour tout $y > 0$. Puisque $h_1(x) > 0$ pour $x > 3$, la composition $g(x) = h_2(h_1(x))$ est continue sur l'intervalle $(3, +\infty)$.

2.  **Continuité aux points de raccordement :**
    Nous devons assurer la continuité aux points $x = 2$ et $x = 3$. Pour qu'une fonction $g$ soit continue en un point $x_0$, il faut que la limite de $g(x)$ lorsque $x$ tend vers $x_0$ existe et soit égale à $g(x_0)$. Cela implique que la limite à gauche et la limite à droite doivent exister et être égales à $g(x_0)$. C'est-à-dire $\lim_{x \to x_0^-} g(x) = \lim_{x \to x_0^+} g(x) = g(x_0)$.

    **Au point $x_0 = 2$ :**
    *   Calculons la limite à gauche de $g(x)$ lorsque $x$ tend vers $2$ :
        $$ \lim_{x \to 2^-} g(x) = \lim_{x \to 2^-} \frac{x^2 - 4}{x - 2} $$
        Nous observons une forme indéterminée de type $\frac{0}{0}$. Nous factorisons le numérateur en utilisant l'identité remarquable $A^2 - B^2 = (A - B)(A + B)$, où $A=x$ et $B=2$.
        $$ x^2 - 4 = (x - 2)(x + 2) $$
        Substituons cette factorisation dans la limite :
        $$ \lim_{x \to 2^-} \frac{(x - 2)(x + 2)}{x - 2} $$
        Pour $x \ne 2$ (ce qui est le cas lorsque $x \to 2^-$), nous pouvons simplifier le terme $(x - 2)$ au numérateur et au dénominateur :
        $$ \lim_{x \to 2^-} (x + 2) $$
        La fonction $x+2$ est un polynôme, donc elle est continue. Nous pouvons évaluer la limite par substitution directe :
        $$ \lim_{x \to 2^-} (x + 2) = 2 + 2 = 4 $$
    *   Calculons la limite à droite de $g(x)$ lorsque $x$ tend vers $2$ :
        $$ \lim_{x \to 2^+} g(x) = \lim_{x \to 2^+} (ax + b) $$
        La fonction $ax+b$ est un polynôme, donc elle est continue. Nous pouvons évaluer la limite par substitution directe :
        $$ \lim_{x \to 2^+} (ax + b) = a(2) + b = 2a + b $$
    *   Calculons la valeur de la fonction $g$ au point $x = 2$ :
        Selon la définition de $g(x)$, pour $x = 2$, nous utilisons la deuxième expression :
        $$ g(2) = a(2) + b = 2a + b $$
    Pour que $g$ soit continue en $x = 2$, les trois valeurs doivent être égales :
    $$ \lim_{x \to 2^-} g(x) = \lim_{x \to 2^+} g(x) = g(2) $$
    Cela nous donne la première équation :
    $$ 4 = 2a + b \quad (1) $$

    **Au point $x_0 = 3$ :**
    *   Calculons la limite à gauche de $g(x)$ lorsque $x$ tend vers $3$ :
        $$ \lim_{x \to 3^-} g(x) = \lim_{x \to 3^-} (ax + b) $$
        La fonction $ax+b$ est un polynôme, donc elle est continue. Nous pouvons évaluer la limite par substitution directe :
        $$ \lim_{x \to 3^-} (ax + b) = a(3) + b = 3a + b $$
    *   Calculons la limite à droite de $g(x)$ lorsque $x$ tend vers $3$ :
        $$ \lim_{x \to 3^+} g(x) = \lim_{x \to 3^+} \sqrt{x^2 + 7} $$
        La fonction $\sqrt{x^2+7}$ est continue pour $x > 3$. Nous pouvons évaluer la limite par substitution directe :
        $$ \lim_{x \to 3^+} \sqrt{x^2 + 7} = \sqrt{(3)^2 + 7} = \sqrt{9 + 7} = \sqrt{16} = 4 $$
    *   Calculons la valeur de la fonction $g$ au point $x = 3$ :
        Selon la définition de $g(x)$, pour $x = 3$, nous utilisons la deuxième expression :
        $$ g(3) = a(3) + b = 3a + b $$
    Pour que $g$ soit continue en $x = 3$, les trois valeurs doivent être égales :
    $$ \lim_{x \to 3^-} g(x) = \lim_{x \to 3^+} g(x) = g(3) $$
    Cela nous donne la deuxième équation :
    $$ 3a + b = 4 \quad (2) $$

    Nous avons maintenant un système de deux équations linéaires à deux inconnues $a$ et $b$ :
    (1) $2a + b = 4$
    (2) $3a + b = 4$

    Pour résoudre ce système, nous pouvons soustraire l'équation (1) de l'équation (2) :
    $$ (3a + b) - (2a + b) = 4 - 4 $$
    $$ 3a - 2a + b - b = 0 $$
    $$ a = 0 $$
    Maintenant que nous avons la valeur de $a$, nous la substituons dans l'équation (1) pour trouver $b$ :
    $$ 2(0) + b = 4 $$
    $$ 0 + b = 4 $$
    $$ b = 4 $$

    Par conséquent, pour que la fonction $g$ soit continue sur l'ensemble de son domaine de définition $\mathbb{R}$, les constantes $a$ et $b$ doivent prendre les valeurs $a = 0$ et $b = 4$.

## Partie C : Application du Théorème des Valeurs Intermédiaires.

Soit l'équation $(E) : x^3 - 3x + 1 = 0$.
Considérons la fonction $h(x) = x^3 - 3x + 1$.
La fonction $h(x)$ est un polynôme. Les polynômes sont des fonctions continues sur l'ensemble de tous les nombres réels, $\mathbb{R}$. Par conséquent, $h(x)$ est continue sur tout intervalle fermé $[c, d]$ inclus dans $\mathbb{R}$.

1.  **Montrons que l'équation $(E)$ possède au moins une solution réelle dans l'intervalle $(0, 1)$.**
    Nous allons appliquer le Théorème des Valeurs Intermédiaires (TVI).
    *   **Condition 1 (Continuité) :** La fonction $h(x) = x^3 - 3x + 1$ est continue sur l'intervalle fermé $[0, 1]$ car c'est un polynôme.
    *   **Condition 2 (Valeurs aux bornes) :** Calculons les valeurs de $h$ aux bornes de l'intervalle $[0, 1]$ :
        $$ h(0) = (0)^3 - 3(0) + 1 = 0 - 0 + 1 = 1 $$
        $$ h(1) = (1)^3 - 3(1) + 1 = 1 - 3 + 1 = -1 $$
    *   **Condition 3 (Existence de $k$) :** Nous observons que $h(0) = 1$ et $h(1) = -1$. Puisque $h(1) < 0 < h(0)$, la valeur $k=0$ est comprise entre $h(1)$ et $h(0)$.
    *   **Conclusion par le TVI :** Le Théorème des Valeurs Intermédiaires stipule que si une fonction $h$ est continue sur un intervalle fermé $[c, d]$ et si $k$ est un nombre réel compris entre $h(c)$ et $h(d)$, alors il existe au moins un $x_1 \in (c, d)$ tel que $h(x_1) = k$.
        Dans notre cas, $c=0$, $d=1$, et $k=0$. Toutes les conditions du TVI sont remplies.
        Par conséquent, il existe au moins une solution $x_1 \in (0, 1)$ telle que $h(x_1) = 0$.
    Ainsi, l'équation $(E)$ possède au moins une solution réelle dans l'intervalle $(0, 1)$.

2.  **Montrons que l'équation $(E)$ possède au moins une solution réelle dans l'intervalle $(-2, -1)$.**
    Nous allons appliquer le Théorème des Valeurs Intermédiaires (TVI) de la même manière.
    *   **Condition 1 (Continuité) :** La fonction $h(x) = x^3 - 3x + 1$ est continue sur l'intervalle fermé $[-2, -1]$ car c'est un polynôme.
    *   **Condition 2 (Valeurs aux bornes) :** Calculons les valeurs de $h$ aux bornes de l'intervalle $[-2, -1]$ :
        $$ h(-2) = (-2)^3 - 3(-2) + 1 = -8 + 6 + 1 = -1 $$
        $$ h(-1) = (-1)^3 - 3(-1) + 1 = -1 + 3 + 1 = 3 $$
    *   **Condition 3 (Existence de $k$) :** Nous observons que $h(-2) = -1$ et $h(-1) = 3$. Puisque $h(-2) < 0 < h(-1)$, la valeur $k=0$ est comprise entre $h(-2)$ et $h(-1)$.
    *   **Conclusion par le TVI :** Toutes les conditions du TVI sont remplies pour l'intervalle $[-2, -1]$ et $k=0$.
        Par conséquent, il existe au moins une solution $x_2 \in (-2, -1)$ telle que $h(x_2) = 0$.
    Ainsi, l'équation $(E)$ possède au moins une solution réelle dans l'intervalle $(-2, -1)$.

3.  **En déduire que l'équation $(E)$ possède au moins deux solutions réelles distinctes.**
    D'après la question 1, nous avons montré l'existence d'une solution $x_1$ telle que $h(x_1) = 0$ et $x_1 \in (0, 1)$.
    D'après la question 2, nous avons montré l'existence d'une solution $x_2$ telle que $h(x_2) = 0$ et $x_2 \in (-2, -1)$.
    Les intervalles $(0, 1)$ et $(-2, -1)$ sont des intervalles disjoints.
    En effet, l'intervalle $(0, 1)$ contient des nombres strictement positifs, tandis que l'intervalle $(-2, -1)$ contient des nombres strictement négatifs. Il n'y a aucun nombre commun à ces deux intervalles, donc leur intersection est vide : $(0, 1) \cap (-2, -1) = \emptyset$.
    Puisque $x_1$ appartient à l'intervalle $(0, 1)$ et $x_2$ appartient à l'intervalle $(-2, -1)$, il est impossible que $x_1$ soit égal à $x_2$.
    Par conséquent, $x_1$ et $x_2$ sont deux solutions réelles distinctes de l'équation $(E)$.
    L'équation $(E)$ possède donc au moins deux solutions réelles distinctes.
