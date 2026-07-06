# Exercice 7 : Continuité d'une fonction définie par morceaux et application du Théorème des Valeurs Intermédiaires

**Difficulté :** $\star\star\star\star\text{☆}$

---

### Énoncé

Soit la fonction $f: \mathbb{R} \to \mathbb{R}$ définie par :
$$
f(x) = \begin{cases}
    \frac{\sqrt{x^2+x+1} - (ax+b)}{x} & \text{si } x < 0 \\
    c & \text{si } x = 0 \\
    \frac{\sin(x^2)}{x \ln(1+x)} & \text{si } x > 0
\end{cases}
$$
où $a, b, c$ sont des constantes réelles.

1.  Déterminer les valeurs de $a, b, c$ pour lesquelles la fonction $f$ est continue sur $\mathbb{R}$.
2.  En utilisant les valeurs de $a, b, c$ trouvées à la question 1, montrer que l'équation $f(x) = 0$ admet au moins une solution dans l'intervalle $(-3, -1)$.

---

### Corrigé

#### Question 1 : Détermination des constantes $a, b, c$ pour la continuité de $f$ sur $\mathbb{R}$.

Pour que la fonction $f$ soit continue sur $\mathbb{R}$, elle doit être continue sur les intervalles ouverts où elle est définie par une seule expression, et continue aux points de raccordement.

1.  **Continuité sur les intervalles ouverts :**
    *   Pour $x < 0$: La fonction $f(x) = \frac{\sqrt{x^2+x+1} - (ax+b)}{x}$ est un quotient de fonctions continues. Le numérateur $\sqrt{x^2+x+1} - (ax+b)$ est continu car $\sqrt{x^2+x+1}$ est continue (le discriminant de $x^2+x+1$ est $1^2 - 4(1)(1) = -3 < 0$, donc $x^2+x+1 > 0$ pour tout $x \in \mathbb{R}$) et $ax+b$ est un polynôme, donc continu. Le dénominateur $x$ est continu et non nul pour $x < 0$. Ainsi, $f$ est continue sur $(-\infty, 0)$.
    *   Pour $x > 0$: La fonction $f(x) = \frac{\sin(x^2)}{x \ln(1+x)}$ est un quotient de fonctions continues. Le numérateur $\sin(x^2)$ est continu comme composition de fonctions continues. Le dénominateur $x \ln(1+x)$ est continu comme produit de fonctions continues. Pour $x > 0$, $x \neq 0$ et $\ln(1+x) \neq 0$ (car $1+x > 1 \implies \ln(1+x) > 0$). Ainsi, $f$ est continue sur $(0, +\infty)$.

2.  **Continuité au point de raccordement $x=0$ :**
    Pour que $f$ soit continue en $x=0$, il faut que $\lim_{x \to 0^-} f(x) = \lim_{x \to 0^+} f(x) = f(0)$.
    Nous avons $f(0) = c$.

    *   **Calcul de $\lim_{x \to 0^-} f(x)$ :**
        $$ \lim_{x \to 0^-} \frac{\sqrt{x^2+x+1} - (ax+b)}{x} $$
        Pour que cette limite existe et soit finie, le numérateur doit tendre vers 0 lorsque $x \to 0$.
        $$ \lim_{x \to 0^-} (\sqrt{x^2+x+1} - (ax+b)) = \sqrt{0^2+0+1} - (a \cdot 0 + b) = \sqrt{1} - b = 1 - b $$
        Pour que la limite soit finie, il faut que $1-b=0$, ce qui implique $b=1$.

        Substituons $b=1$ dans l'expression de $f(x)$ pour $x < 0$:
        $$ \lim_{x \to 0^-} \frac{\sqrt{x^2+x+1} - (ax+1)}{x} $$
        Cette limite est de la forme $\frac{0}{0}$. Nous pouvons utiliser la multiplication par l'expression conjuguée du numérateur :
        \begin{align*}
        \frac{\sqrt{x^2+x+1} - (ax+1)}{x} &= \frac{(\sqrt{x^2+x+1} - (ax+1))(\sqrt{x^2+x+1} + (ax+1))}{x(\sqrt{x^2+x+1} + (ax+1))} \\
        &= \frac{(x^2+x+1) - (ax+1)^2}{x(\sqrt{x^2+x+1} + (ax+1))} \\
        &= \frac{x^2+x+1 - (a^2x^2+2ax+1)}{x(\sqrt{x^2+x+1} + (ax+1))} \\
        &= \frac{x^2(1-a^2) + x(1-2a)}{x(\sqrt{x^2+x+1} + (ax+1))} \\
        &= \frac{x(1-a^2) + (1-2a)}{\sqrt{x^2+x+1} + (ax+1)} \quad \text{pour } x \neq 0
        \end{align*}
        Maintenant, nous pouvons calculer la limite lorsque $x \to 0^-$ :
        $$ \lim_{x \to 0^-} \frac{x(1-a^2) + (1-2a)}{\sqrt{x^2+x+1} + (ax+1)} = \frac{0 \cdot (1-a^2) + (1-2a)}{\sqrt{0^2+0+1} + (a \cdot 0 + 1)} = \frac{1-2a}{1+1} = \frac{1-2a}{2} $$

    *   **Calcul de $\lim_{x \to 0^+} f(x)$ :**
        $$ \lim_{x \to 0^+} \frac{\sin(x^2)}{x \ln(1+x)} $$
        Cette limite est de la forme $\frac{0}{0}$. Nous utilisons les équivalents usuels au voisinage de 0 :
        $\sin(u) \sim u$ lorsque $u \to 0$. Donc $\sin(x^2) \sim x^2$ lorsque $x \to 0$.
        $\ln(1+x) \sim x$ lorsque $x \to 0$.
        Ainsi, $x \ln(1+x) \sim x \cdot x = x^2$ lorsque $x \to 0$.
        Par conséquent :
        $$ \lim_{x \to 0^+} \frac{\sin(x^2)}{x \ln(1+x)} = \lim_{x \to 0^+} \frac{x^2}{x^2} = 1 $$

    *   **Égalité des limites et $f(0)$ :**
        Pour la continuité en $x=0$, nous devons avoir :
        $$ \frac{1-2a}{2} = 1 = c $$
        De $c=1$, nous obtenons $c=1$.
        De $\frac{1-2a}{2} = 1$, nous avons $1-2a = 2$, ce qui implique $-2a = 1$, et donc $a = -\frac{1}{2}$.

3.  **Conclusion :**
    La fonction $f$ est continue sur $\mathbb{R}$ si et seulement si $a = -\frac{1}{2}$, $b = 1$, et $c = 1$.

#### Question 2 : Montrer que l'équation $f(x) = 0$ admet au moins une solution dans l'intervalle $(-3, -1)$.

Avec les valeurs trouvées à la question 1, la fonction $f$ est continue sur $\mathbb{R}$. En particulier, $f$ est continue sur l'intervalle fermé et borné $[-3, -1]$.
Nous allons appliquer le Théorème des Valeurs Intermédiaires (TVI). Pour cela, nous devons évaluer $f(-3)$ et $f(-1)$ et vérifier qu'ils sont de signes opposés.

Pour $x < 0$, la fonction est donnée par $f(x) = \frac{\sqrt{x^2+x+1} - (-\frac{1}{2}x+1)}{x}$.

*   **Calcul de $f(-3)$ :**
    $$ f(-3) = \frac{\sqrt{(-3)^2+(-3)+1} - (-\frac{1}{2}(-3)+1)}{-3} $$
    $$ f(-3) = \frac{\sqrt{9-3+1} - (\frac{3}{2}+1)}{-3} $$
    $$ f(-3) = \frac{\sqrt{7} - \frac{5}{2}}{-3} $$
    Nous savons que $2^2 = 4$ et $3^2 = 9$, donc $2 < \sqrt{7} < 3$. Plus précisément, $\sqrt{7} \approx 2.645$.
    Alors $\sqrt{7} - \frac{5}{2} = \sqrt{7} - 2.5 \approx 2.645 - 2.5 = 0.145$.
    Le numérateur $\sqrt{7} - \frac{5}{2}$ est positif.
    Le dénominateur est $-3$, qui est négatif.
    Donc, $f(-3) = \frac{\text{positif}}{\text{négatif}} < 0$.

*   **Calcul de $f(-1)$ :**
    $$ f(-1) = \frac{\sqrt{(-1)^2+(-1)+1} - (-\frac{1}{2}(-1)+1)}{-1} $$
    $$ f(-1) = \frac{\sqrt{1-1+1} - (\frac{1}{2}+1)}{-1} $$
    $$ f(-1) = \frac{\sqrt{1} - \frac{3}{2}}{-1} $$
    $$ f(-1) = \frac{1 - \frac{3}{2}}{-1} = \frac{-\frac{1}{2}}{-1} = \frac{1}{2} $$
    Donc, $f(-1) = \frac{1}{2} > 0$.

Nous avons $f(-3) < 0$ et $f(-1) > 0$.
Puisque $f$ est continue sur l'intervalle $[-3, -1]$ et que $f(-3)$ et $f(-1)$ sont de signes opposés, d'après le Théorème des Valeurs Intermédiaires, il existe au moins une solution $x_0 \in (-3, -1)$ telle que $f(x_0) = 0$.

L'équation $f(x) = 0$ admet donc au moins une solution dans l'intervalle $(-3, -1)$.