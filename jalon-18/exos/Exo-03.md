# Exercice 3 : Continuité d'une fonction définie par morceaux

Chers étudiants,

Pour ce troisième exercice de notre jalon sur la continuité, nous allons explorer la notion de continuité d'une fonction définie par morceaux. Il s'agit d'un concept fondamental qui met en jeu la définition de la continuité en un point.

Soit la fonction $f: \mathbb{R} \to \mathbb{R}$ définie par :
$$ f(x) = \begin{cases} x^2 + ax + 1 & \text{si } x < 1 \\ 3x - 1 & \text{si } x \ge 1 \end{cases} $$
où $a$ est un paramètre réel.

Déterminez la valeur du paramètre $a$ pour laquelle la fonction $f$ est continue sur l'ensemble des nombres réels $\mathbb{R}$. Justifiez rigoureusement votre réponse.

---

## Corrigé de l'Exercice 3

Mes chers étudiants,

Procédons à la résolution de cet exercice avec la rigueur qui s'impose. Pour qu'une fonction soit continue sur $\mathbb{R}$, elle doit être continue en tout point de $\mathbb{R}$. La fonction $f$ est définie par deux expressions polynomiales.

1.  **Continuité sur les intervalles ouverts :**
    *   Pour $x < 1$, la fonction $f(x) = x^2 + ax + 1$ est une fonction polynomiale. Nous savons que les fonctions polynomiales sont continues sur l'ensemble des nombres réels $\mathbb{R}$. Par conséquent, $f$ est continue sur l'intervalle ouvert $]-\infty, 1[$.
    *   Pour $x > 1$, la fonction $f(x) = 3x - 1$ est également une fonction polynomiale (plus précisément, une fonction affine). Elle est donc continue sur l'intervalle ouvert $]1, +\infty[$.

2.  **Continuité au point de raccordement :**
    Le seul point où la continuité de $f$ n'est pas garantie a priori est le point de raccordement des deux définitions, c'est-à-dire $x=1$.
    Pour que la fonction $f$ soit continue en $x=1$, il faut que la limite de $f(x)$ lorsque $x$ tend vers $1$ existe et soit égale à la valeur de la fonction en $x=1$. Autrement dit, les trois conditions suivantes doivent être satisfaites :
    $$ \lim_{x \to 1^-} f(x) = \lim_{x \to 1^+} f(x) = f(1) $$

    Calculons chacun de ces trois termes séparément :

    *   **Calcul de la valeur de la fonction en $x=1$ :**
        Puisque la définition de $f(x)$ pour $x \ge 1$ est $3x - 1$, nous utilisons cette expression pour évaluer $f(1)$ :
        $$ f(1) = 3(1) - 1 = 3 - 1 = 2 $$

    *   **Calcul de la limite à gauche en $x=1$ :**
        Lorsque $x \to 1^-$, cela signifie que $x$ approche $1$ par des valeurs strictement inférieures à $1$. Nous utilisons donc la première expression pour $f(x)$, qui est $x^2 + ax + 1$ :
        $$ \lim_{x \to 1^-} f(x) = \lim_{x \to 1^-} (x^2 + ax + 1) $$
        Étant donné que $x^2 + ax + 1$ est un polynôme, sa limite en $x=1$ est simplement sa valeur en $x=1$ (par propriété de continuité des polynômes) :
        $$ \lim_{x \to 1^-} f(x) = (1)^2 + a(1) + 1 = 1 + a + 1 = a + 2 $$

    *   **Calcul de la limite à droite en $x=1$ :**
        Lorsque $x \to 1^+$, cela signifie que $x$ approche $1$ par des valeurs strictement supérieures à $1$. Nous utilisons donc la deuxième expression pour $f(x)$, qui est $3x - 1$ :
        $$ \lim_{x \to 1^+} f(x) = \lim_{x \to 1^+} (3x - 1) $$
        De même, puisque $3x - 1$ est un polynôme, sa limite en $x=1$ est sa valeur en $x=1$ :
        $$ \lim_{x \to 1^+} f(x) = 3(1) - 1 = 3 - 1 = 2 $$

3.  **Détermination du paramètre $a$ :**
    Pour que la fonction $f$ soit continue en $x=1$, les trois valeurs calculées doivent être égales :
    $$ \lim_{x \to 1^-} f(x) = \lim_{x \to 1^+} f(x) = f(1) $$
    En substituant les valeurs que nous avons trouvées :
    $$ a + 2 = 2 = 2 $$
    De l'égalité $a + 2 = 2$, nous pouvons résoudre pour $a$ :
    $$ a + 2 - 2 = 2 - 2 $$
    $$ a = 0 $$

4.  **Conclusion :**
    Pour que la fonction $f$ soit continue sur l'ensemble des nombres réels $\mathbb{R}$, le paramètre $a$ doit être égal à $0$.
    Dans ce cas, la fonction $f(x)$ s'écrit :
    $$ f(x) = \begin{cases} x^2 + 1 & \text{si } x < 1 \\ 3x - 1 & \text{si } x \ge 1 \end{cases} $$
    Avec $a=0$, nous avons bien $f(1) = 3(1)-1 = 2$, $\lim_{x \to 1^-} (x^2+1) = 1^2+1 = 2$, et $\lim_{x \to 1^+} (3x-1) = 3(1)-1 = 2$. Toutes les conditions de continuité sont satisfaites en $x=1$, et la continuité est déjà établie sur les intervalles $]-\infty, 1[$ et $]1, +\infty[$. Par conséquent, la fonction $f$ est continue sur $\mathbb{R}$ lorsque $a=0$.