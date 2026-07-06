# Exercice 1 - Exploration de la Continuité des Fonctions d'une Variable Réelle

Cet exercice est conçu pour évaluer votre compréhension approfondie de la continuité des fonctions d'une variable réelle, depuis la définition fondamentale jusqu'à l'application de théorèmes clés. La rigueur de votre rédaction est primordiale.

---

## Énoncé de l'Exercice

### Partie A : Continuité par la Définition Epsilon-Delta

Soit la fonction $f: \mathbb{R} \to \mathbb{R}$ définie par $f(x) = x^2$.
En utilisant la définition formelle de la continuité (la définition $\epsilon-\delta$), démontrez que la fonction $f$ est continue au point $x_0 = 2$.

### Partie B : Continuité d'une Fonction Définie par Morceaux

Considérons la fonction $g: \mathbb{R} \to \mathbb{R}$ définie par :
$$
g(x) = \begin{cases}
    \frac{x^2 - 4}{x - 2} & \text{si } x < 2 \\
    ax + b & \text{si } 2 \le x \le 3 \\
    \sqrt{x + 1} & \text{si } x > 3
\end{cases}
$$
Déterminez les valeurs des constantes réelles $a$ et $b$ pour que la fonction $g$ soit continue sur l'ensemble de tous les nombres réels $\mathbb{R}$.

### Partie C : Application du Théorème des Valeurs Intermédiaires

Soit la fonction $h: \mathbb{R} \to \mathbb{R}$ définie par $h(x) = x^3 - 3x + 1$.
Démontrez que l'équation $h(x) = 0$ possède au moins trois racines réelles distinctes.

### Partie D : Continuité Epsilon-Delta pour une Fonction Rationnelle

Soit la fonction $k: \mathbb{R}^* \to \mathbb{R}$ définie par $k(x) = \frac{1}{x}$.
En utilisant la définition formelle de la continuité ($\epsilon-\delta$), démontrez que la fonction $k$ est continue au point $x_0 = 1$.

---

## Correction Détaillée

### Partie A : Continuité par la Définition Epsilon-Delta

Nous voulons démontrer que la fonction $f(x) = x^2$ est continue au point $x_0 = 2$.
La définition de la continuité d'une fonction $f$ au point $x_0$ est la suivante :
Pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que si $|x - x_0| < \delta$, alors $|f(x) - f(x_0)| < \epsilon$.

1.  **Identification de $f(x_0)$ :**
    Nous avons $x_0 = 2$, donc $f(x_0) = f(2) = 2^2 = 4$.

2.  **Expression de $|f(x) - f(x_0)|$ :**
    Nous devons analyser l'expression $|f(x) - f(2)| = |x^2 - 4|$.
    Par factorisation de la différence de carrés, nous obtenons :
    $$ |x^2 - 4| = |(x - 2)(x + 2)| = |x - 2| |x + 2| $$

3.  **Majoration du terme $|x+2|$ :**
    Nous voulons que $|x - 2|$ soit petit. Choisissons une première contrainte sur $\delta$. Supposons que $\delta \le 1$.
    Si $|x - 2| < \delta$ et $\delta \le 1$, alors $|x - 2| < 1$.
    Ceci implique que $-1 < x - 2 < 1$.
    En ajoutant $2$ à toutes les parties de l'inégalité, nous obtenons :
    $$ 2 - 1 < x < 2 + 1 $$
    $$ 1 < x < 3 $$
    Maintenant, nous voulons majorer $|x + 2|$. Puisque $1 < x < 3$, nous avons :
    $$ 1 + 2 < x + 2 < 3 + 2 $$
    $$ 3 < x + 2 < 5 $$
    Par conséquent, $|x + 2| < 5$.

4.  **Combinaison et choix de $\delta$ :**
    En utilisant la majoration précédente, nous avons :
    $$ |f(x) - f(2)| = |x - 2| |x + 2| < |x - 2| \cdot 5 $$
    Nous voulons que cette expression soit inférieure à $\epsilon$. Donc, nous voulons que $5|x - 2| < \epsilon$, ce qui implique $|x - 2| < \frac{\epsilon}{5}$.
    Nous avons deux contraintes sur $\delta$ : $\delta \le 1$ (pour majorer $|x+2|$) et $\delta \le \frac{\epsilon}{5}$ (pour obtenir la condition finale).
    Nous choisissons $\delta = \min\left(1, \frac{\epsilon}{5}\right)$.

5.  **Démonstration formelle :**
    Soit $\epsilon > 0$ un nombre réel arbitraire.
    Choisissons $\delta = \min\left(1, \frac{\epsilon}{5}\right)$. Par définition, $\delta > 0$.
    Supposons que $x$ est un nombre réel tel que $|x - 2| < \delta$.
    Puisque $\delta \le 1$, nous avons $|x - 2| < 1$.
    Ceci implique $-1 < x - 2 < 1$, ce qui donne $1 < x < 3$.
    En ajoutant $2$ à l'inégalité $1 < x < 3$, nous obtenons $3 < x + 2 < 5$.
    Par conséquent, $|x + 2| < 5$.
    Maintenant, considérons $|f(x) - f(2)|$:
    $$ |f(x) - f(2)| = |x^2 - 4| $$
    $$ |f(x) - f(2)| = |(x - 2)(x + 2)| \quad \text{(factorisation de la différence de carrés)} $$
    $$ |f(x) - f(2)| = |x - 2| |x + 2| \quad \text{(propriété du module : } |ab| = |a||b|) $$
    Puisque $|x - 2| < \delta$ et $|x + 2| < 5$, nous pouvons écrire :
    $$ |f(x) - f(2)| < \delta \cdot 5 $$
    De plus, par notre choix de $\delta$, nous savons que $\delta \le \frac{\epsilon}{5}$.
    Donc, $\delta \cdot 5 \le \left(\frac{\epsilon}{5}\right) \cdot 5 = \epsilon$.
    En combinant ces inégalités, nous obtenons :
    $$ |f(x) - f(2)| < \epsilon $$
    Ainsi, pour tout $\epsilon > 0$, il existe un $\delta = \min\left(1, \frac{\epsilon}{5}\right) > 0$ tel que si $|x - 2| < \delta$, alors $|f(x) - f(2)| < \epsilon$.
    Par conséquent, la fonction $f(x) = x^2$ est continue au point $x_0 = 2$.

### Partie B : Continuité d'une Fonction Définie par Morceaux

La fonction $g(x)$ est définie par morceaux. Pour qu'elle soit continue sur $\mathbb{R}$, elle doit être continue sur chaque intervalle ouvert de sa définition et aux points de raccordement ($x=2$ et $x=3$).

1.  **Continuité sur les intervalles ouverts :**
    *   **Pour $x < 2$ :** $g(x) = \frac{x^2 - 4}{x - 2}$. Pour $x \ne 2$, nous pouvons simplifier cette expression.
        $$ g(x) = \frac{(x - 2)(x + 2)}{x - 2} = x + 2 $$
        La fonction $x \mapsto x+2$ est une fonction polynomiale, et les fonctions polynomiales sont continues sur $\mathbb{R}$. Donc, $g$ est continue sur $(-\infty, 2)$.
    *   **Pour $2 < x < 3$ :** $g(x) = ax + b$. Cette fonction est une fonction polynomiale (linéaire), donc elle est continue sur $(2, 3)$.
    *   **Pour $x > 3$ :** $g(x) = \sqrt{x + 1}$. La fonction $u \mapsto \sqrt{u}$ est continue sur son domaine de définition $[0, +\infty)$. La fonction $x \mapsto x+1$ est continue sur $\mathbb{R}$. Pour $x > 3$, nous avons $x+1 > 4 > 0$. Par composition de fonctions continues, $g(x) = \sqrt{x+1}$ est continue sur $(3, +\infty)$.

2.  **Continuité aux points de raccordement :**
    Pour que $g$ soit continue en un point $x_0$, il faut que $\lim_{x \to x_0^-} g(x) = \lim_{x \to x_0^+} g(x) = g(x_0)$.

    *   **Au point $x_0 = 2$ :**
        *   **Valeur de la fonction en $x=2$ :** $g(2) = a(2) + b = 2a + b$.
        *   **Limite à gauche en $x=2$ :**
            $$ \lim_{x \to 2^-} g(x) = \lim_{x \to 2^-} \frac{x^2 - 4}{x - 2} $$
            Puisque $x \ne 2$ dans le calcul de la limite, nous pouvons factoriser le numérateur :
            $$ \lim_{x \to 2^-} \frac{(x - 2)(x + 2)}{x - 2} $$
            En simplifiant par $(x-2)$ (car $x \ne 2$), nous obtenons :
            $$ \lim_{x \to 2^-} (x + 2) $$
            La fonction $x \mapsto x+2$ est polynomiale, donc sa limite est obtenue par substitution directe :
            $$ \lim_{x \to 2^-} (x + 2) = 2 + 2 = 4 $$
        *   **Limite à droite en $x=2$ :**
            $$ \lim_{x \to 2^+} g(x) = \lim_{x \to 2^+} (ax + b) $$
            La fonction $x \mapsto ax+b$ est polynomiale, donc sa limite est obtenue par substitution directe :
            $$ \lim_{x \to 2^+} (ax + b) = a(2) + b = 2a + b $$
        *   **Condition de continuité en $x=2$ :** Pour que $g$ soit continue en $x=2$, il faut que $\lim_{x \to 2^-} g(x) = \lim_{x \to 2^+} g(x) = g(2)$.
            Donc, nous devons avoir $4 = 2a + b$. (Équation 1)

    *   **Au point $x_0 = 3$ :**
        *   **Valeur de la fonction en $x=3$ :** $g(3) = a(3) + b = 3a + b$.
        *   **Limite à gauche en $x=3$ :**
            $$ \lim_{x \to 3^-} g(x) = \lim_{x \to 3^-} (ax + b) $$
            La fonction $x \mapsto ax+b$ est polynomiale, donc sa limite est obtenue par substitution directe :
            $$ \lim_{x \to 3^-} (ax + b) = a(3) + b = 3a + b $$
        *   **Limite à droite en $x=3$ :**
            $$ \lim_{x \to 3^+} g(x) = \lim_{x \to 3^+} \sqrt{x + 1} $$
            La fonction $u \mapsto \sqrt{u}$ est continue pour $u \ge 0$. La fonction $x \mapsto x+1$ est continue. Pour $x \to 3^+$, $x+1 \to 4$. Puisque $4 > 0$, nous pouvons utiliser la continuité de la racine carrée :
            $$ \lim_{x \to 3^+} \sqrt{x + 1} = \sqrt{\lim_{x \to 3^+} (x + 1)} = \sqrt{3 + 1} = \sqrt{4} = 2 $$
        *   **Condition de continuité en $x=3$ :** Pour que $g$ soit continue en $x=3$, il faut que $\lim_{x \to 3^-} g(x) = \lim_{x \to 3^+} g(x) = g(3)$.
            Donc, nous devons avoir $3a + b = 2$. (Équation 2)

3.  **Résolution du système d'équations :**
    Nous avons un système de deux équations linéaires à deux inconnues $a$ et $b$ :
    1.  $2a + b = 4$
    2.  $3a + b = 2$

    Soustrayons l'Équation 1 de l'Équation 2 :
    $$ (3a + b) - (2a + b) = 2 - 4 $$
    $$ 3a - 2a + b - b = -2 $$
    $$ a = -2 $$
    Substituons la valeur de $a$ dans l'Équation 1 :
    $$ 2(-2) + b = 4 $$
    $$ -4 + b = 4 $$
    $$ b = 4 + 4 $$
    $$ b = 8 $$

    Par conséquent, pour que la fonction $g$ soit continue sur $\mathbb{R}$, les constantes doivent être $a = -2$ et $b = 8$.

### Partie C : Application du Théorème des Valeurs Intermédiaires

Nous voulons démontrer que l'équation $h(x) = x^3 - 3x + 1 = 0$ possède au moins trois racines réelles distinctes.

1.  **Vérification de la continuité :**
    La fonction $h(x) = x^3 - 3x + 1$ est une fonction polynomiale. Les fonctions polynomiales sont continues sur l'ensemble de tous les nombres réels $\mathbb{R}$. Par conséquent, $h$ est continue sur tout intervalle fermé $[c, d] \subset \mathbb{R}$.

2.  **Recherche d'intervalles où la fonction change de signe :**
    Pour appliquer le Théorème des Valeurs Intermédiaires (TVI), nous devons trouver des intervalles $[c, d]$ sur lesquels $h$ est continue et où $h(c)$ et $h(d)$ ont des signes opposés. Si c'est le cas, le TVI garantit l'existence d'au moins une racine dans l'intervalle ouvert $(c, d)$.

    Calculons les valeurs de $h(x)$ pour quelques points :
    *   $h(-2) = (-2)^3 - 3(-2) + 1 = -8 + 6 + 1 = -1$.
    *   $h(0) = (0)^3 - 3(0) + 1 = 0 - 0 + 1 = 1$.
    *   $h(1) = (1)^3 - 3(1) + 1 = 1 - 3 + 1 = -1$.
    *   $h(2) = (2)^3 - 3(2) + 1 = 8 - 6 + 1 = 3$.

3.  **Application du Théorème des Valeurs Intermédiaires :**

    *   **Premier intervalle : $[-2, 0]$**
        1.  La fonction $h$ est continue sur l'intervalle fermé $[-2, 0]$ car elle est polynomiale.
        2.  Nous avons $h(-2) = -1$ et $h(0) = 1$.
        3.  Puisque $h(-2) < 0$ et $h(0) > 0$, et que $0$ est une valeur intermédiaire entre $h(-2)$ et $h(0)$, le Théorème des Valeurs Intermédiaires garantit qu'il existe au moins une racine $c_1 \in (-2, 0)$ telle que $h(c_1) = 0$.

    *   **Deuxième intervalle : $[0, 1]$**
        1.  La fonction $h$ est continue sur l'intervalle fermé $[0, 1]$ car elle est polynomiale.
        2.  Nous avons $h(0) = 1$ et $h(1) = -1$.
        3.  Puisque $h(0) > 0$ et $h(1) < 0$, et que $0$ est une valeur intermédiaire entre $h(0)$ et $h(1)$, le Théorème des Valeurs Intermédiaires garantit qu'il existe au moins une racine $c_2 \in (0, 1)$ telle que $h(c_2) = 0$.

    *   **Troisième intervalle : $[1, 2]$**
        1.  La fonction $h$ est continue sur l'intervalle fermé $[1, 2]$ car elle est polynomiale.
        2.  Nous avons $h(1) = -1$ et $h(2) = 3$.
        3.  Puisque $h(1) < 0$ et $h(2) > 0$, et que $0$ est une valeur intermédiaire entre $h(1)$ et $h(2)$, le Théorème des Valeurs Intermédiaires garantit qu'il existe au moins une racine $c_3 \in (1, 2)$ telle que $h(c_3) = 0$.

4.  **Conclusion :**
    Nous avons trouvé trois racines $c_1, c_2, c_3$ qui appartiennent respectivement aux intervalles $(-2, 0)$, $(0, 1)$ et $(1, 2)$. Ces intervalles sont disjoints.
    *   $c_1 \in (-2, 0)$
    *   $c_2 \in (0, 1)$
    *   $c_3 \in (1, 2)$
    Puisque ces racines se trouvent dans des intervalles disjoints, elles sont nécessairement distinctes.
    Par conséquent, l'équation $x^3 - 3x + 1 = 0$ possède au moins trois racines réelles distinctes.

### Partie D : Continuité Epsilon-Delta pour une Fonction Rationnelle

Nous voulons démontrer que la fonction $k(x) = \frac{1}{x}$ est continue au point $x_0 = 1$.
La définition de la continuité d'une fonction $k$ au point $x_0$ est la suivante :
Pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que si $|x - x_0| < \delta$, alors $|k(x) - k(x_0)| < \epsilon$.

1.  **Identification de $k(x_0)$ :**
    Nous avons $x_0 = 1$, donc $k(x_0) = k(1) = \frac{1}{1} = 1$.

2.  **Expression de $|k(x) - k(x_0)|$ :**
    Nous devons analyser l'expression $|k(x) - k(1)| = \left|\frac{1}{x} - 1\right|$.
    Pour combiner les termes, nous mettons sur un dénominateur commun :
    $$ \left|\frac{1}{x} - 1\right| = \left|\frac{1 - x}{x}\right| $$
    En utilisant la propriété du module $|a/b| = |a|/|b|$ et $|1-x| = |x-1|$ :
    $$ \left|\frac{1 - x}{x}\right| = \frac{|1 - x|}{|x|} = \frac{|x - 1|}{|x|} $$

3.  **Majoration du terme $\frac{1}{|x|}$ :**
    Nous voulons que $|x - 1|$ soit petit. Choisissons une première contrainte sur $\delta$. Supposons que $\delta \le \frac{1}{2}$.
    Si $|x - 1| < \delta$ et $\delta \le \frac{1}{2}$, alors $|x - 1| < \frac{1}{2}$.
    Ceci implique $-\frac{1}{2} < x - 1 < \frac{1}{2}$.
    En ajoutant $1$ à toutes les parties de l'inégalité, nous obtenons :
    $$ 1 - \frac{1}{2} < x < 1 + \frac{1}{2} $$
    $$ \frac{1}{2} < x < \frac{3}{2} $$
    Puisque $x > \frac{1}{2}$, nous avons $0 < \frac{1}{x} < 2$.
    Par conséquent, $\frac{1}{|x|} < 2$.

4.  **Combinaison et choix de $\delta$ :**
    En utilisant la majoration précédente, nous avons :
    $$ |k(x) - k(1)| = \frac{|x - 1|}{|x|} < |x - 1| \cdot 2 $$
    Nous voulons que cette expression soit inférieure à $\epsilon$. Donc, nous voulons que $2|x - 1| < \epsilon$, ce qui implique $|x - 1| < \frac{\epsilon}{2}$.
    Nous avons deux contraintes sur $\delta$ : $\delta \le \frac{1}{2}$ (pour majorer $\frac{1}{|x|}$) et $\delta \le \frac{\epsilon}{2}$ (pour obtenir la condition finale).
    Nous choisissons $\delta = \min\left(\frac{1}{2}, \frac{\epsilon}{2}\right)$.

5.  **Démonstration formelle :**
    Soit $\epsilon > 0$ un nombre réel arbitraire.
    Choisissons $\delta = \min\left(\frac{1}{2}, \frac{\epsilon}{2}\right)$. Par définition, $\delta > 0$.
    Supposons que $x$ est un nombre réel tel que $|x - 1| < \delta$.
    Puisque $\delta \le \frac{1}{2}$, nous avons $|x - 1| < \frac{1}{2}$.
    Ceci implique $-\frac{1}{2} < x - 1 < \frac{1}{2}$, ce qui donne $\frac{1}{2} < x < \frac{3}{2}$.
    Puisque $x > \frac{1}{2}$, $x$ est non nul, et nous pouvons prendre l'inverse :
    $$ \frac{1}{3/2} < \frac{1}{x} < \frac{1}{1/2} $$
    $$ \frac{2}{3} < \frac{1}{x} < 2 $$
    Par conséquent, $\frac{1}{|x|} < 2$.
    Maintenant, considérons $|k(x) - k(1)|$:
    $$ |k(x) - k(1)| = \left|\frac{1}{x} - 1\right| $$
    $$ |k(x) - k(1)| = \left|\frac{1 - x}{x}\right| \quad \text{(mise au même dénominateur)} $$
    $$ |k(x) - k(1)| = \frac{|1 - x|}{|x|} \quad \text{(propriété du module : } |a/b| = |a|/|b|) $$
    $$ |k(x) - k(1)| = \frac{|x - 1|}{|x|} \quad \text{(propriété du module : } |1-x| = |x-1|) $$
    Puisque $|x - 1| < \delta$ et $\frac{1}{|x|} < 2$, nous pouvons écrire :
    $$ |k(x) - k(1)| < \delta \cdot 2 $$
    De plus, par notre choix de $\delta$, nous savons que $\delta \le \frac{\epsilon}{2}$.
    Donc, $\delta \cdot 2 \le \left(\frac{\epsilon}{2}\right) \cdot 2 = \epsilon$.
    En combinant ces inégalités, nous obtenons :
    $$ |k(x) - k(1)| < \epsilon $$
    Ainsi, pour tout $\epsilon > 0$, il existe un $\delta = \min\left(\frac{1}{2}, \frac{\epsilon}{2}\right) > 0$ tel que si $|x - 1| < \delta$, alors $|k(x) - k(1)| < \epsilon$.
    Par conséquent, la fonction $k(x) = \frac{1}{x}$ est continue au point $x_0 = 1$.
