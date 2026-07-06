# Exercice 4 : Détermination d'un paramètre pour la continuité d'une fonction définie par morceaux

**Contexte théorique :**

Pour qu'une fonction $f: D \to \mathbb{R}$ soit continue en un point $c \in D$, il est nécessaire et suffisant que les trois conditions suivantes soient satisfaites :
1.  La fonction $f$ est définie au point $c$, c'est-à-dire $c \in D$.
2.  La limite de $f(x)$ lorsque $x$ tend vers $c$ existe. Cela signifie que les limites à gauche et à droite de $f$ en $c$ sont égales : $\lim_{x \to c^-} f(x) = \lim_{x \to c^+} f(x)$.
3.  La valeur de la fonction en $c$ est égale à cette limite : $\lim_{x \to c} f(x) = f(c)$.

Dans le cas d'une fonction définie par morceaux, la continuité sur les intervalles ouverts où chaque morceau est défini est généralement assurée par la nature des fonctions élémentaires (polynômes, fonctions rationnelles, fonctions trigonométriques, etc.). Le point crucial à examiner pour la continuité globale est alors le ou les points de raccordement entre les différents morceaux de la définition.

**Énoncé de l'exercice :**

Considérons la fonction $f: \mathbb{R} \to \mathbb{R}$ définie par :
\[
f(x) = \begin{cases}
ax^2 + 3 & \text{si } x \le 1 \\
5x - 2 & \text{si } x > 1
\end{cases}
\]
où $a$ est un paramètre réel. Déterminez la valeur de $a$ pour laquelle la fonction $f$ est continue sur tout $\mathbb{R}$.

**Corrigé :**

Pour que la fonction $f$ soit continue sur tout $\mathbb{R}$, nous devons examiner sa continuité sur les intervalles ouverts où elle est définie par une seule expression, puis au point de raccordement.

1.  **Continuité sur les intervalles ouverts :**
    *   Pour $x < 1$, la fonction $f(x) = ax^2 + 3$ est une fonction polynomiale. Les fonctions polynomiales sont continues sur tout $\mathbb{R}$. Par conséquent, $f$ est continue sur l'intervalle $(-\infty, 1)$.
    *   Pour $x > 1$, la fonction $f(x) = 5x - 2$ est également une fonction polynomiale (plus précisément, une fonction affine). Les fonctions polynomiales sont continues sur tout $\mathbb{R}$. Par conséquent, $f$ est continue sur l'intervalle $(1, \infty)$.

2.  **Continuité au point de raccordement $x=1$ :**
    C'est au point $x=1$ que la définition de la fonction change. Pour que $f$ soit continue en $x=1$, les trois conditions de continuité énoncées précédemment doivent être satisfaites.

    a.  **Calcul de $f(1)$ :**
        Selon la définition de $f(x)$ pour $x \le 1$, nous avons :
        \[
        f(1) = a(1)^2 + 3 = a \cdot 1 + 3 = a + 3
        \]
        La fonction est bien définie en $x=1$.

    b.  **Calcul des limites à gauche et à droite en $x=1$ :**
        *   **Limite à gauche :** Lorsque $x$ tend vers $1$ par des valeurs inférieures à $1$ (noté $x \to 1^-$), la fonction est définie par $f(x) = ax^2 + 3$.
            \[
            \lim_{x \to 1^-} f(x) = \lim_{x \to 1^-} (ax^2 + 3)
            \]
            Puisque $ax^2 + 3$ est un polynôme, la limite peut être trouvée par substitution directe :
            \[
            \lim_{x \to 1^-} (ax^2 + 3) = a(1)^2 + 3 = a + 3
            \]

        *   **Limite à droite :** Lorsque $x$ tend vers $1$ par des valeurs supérieures à $1$ (noté $x \to 1^+$), la fonction est définie par $f(x) = 5x - 2$.
            \[
            \lim_{x \to 1^+} f(x) = \lim_{x \to 1^+} (5x - 2)
            \]
            Puisque $5x - 2$ est un polynôme, la limite peut être trouvée par substitution directe :
            \[
            \lim_{x \to 1^+} (5x - 2) = 5(1) - 2 = 5 - 2 = 3
            \]

    c.  **Égalité des limites et de la valeur de la fonction :**
        Pour que la fonction $f$ soit continue en $x=1$, il faut que la limite à gauche, la limite à droite et la valeur de la fonction en $1$ soient toutes égales.
        Nous devons donc avoir :
        \[
        \lim_{x \to 1^-} f(x) = \lim_{x \to 1^+} f(x) = f(1)
        \]
        En substituant les valeurs calculées :
        \[
        a + 3 = 3 = a + 3
        \]
        De l'égalité $a + 3 = 3$, nous pouvons résoudre pour $a$ :
        \[
        a + 3 = 3
        \]
        \[
        a = 3 - 3
        \]
        \[
        a = 0
        \]

**Conclusion :**

Pour que la fonction $f$ soit continue sur tout $\mathbb{R}$, le paramètre $a$ doit être égal à $0$.
Dans ce cas, la fonction $f(x)$ s'écrit :
\[
f(x) = \begin{cases}
3 & \text{si } x \le 1 \\
5x - 2 & \text{si } x > 1
\end{cases}
\]
Et nous vérifions que $f(1) = 3$, $\lim_{x \to 1^-} f(x) = 3$, et $\lim_{x \to 1^+} f(x) = 3$. Toutes les conditions de continuité sont alors satisfaites.