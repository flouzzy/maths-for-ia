# Exercice 6 : Détermination de paramètres pour la continuité d'une fonction définie par morceaux

**Difficulté :** $\star\star\star\protect\text{/}\star\star\star\star\star$

## Énoncé

Soit $f: \mathbb{R} \to \mathbb{R}$ la fonction définie par :
$$ f(x) = \begin{cases} x^2 + ax + 1 & \text{si } x < 1 \\ bx^2 + cx + 2 & \text{si } 1 \le x < 2 \\ \frac{1}{x-1} & \text{si } x \ge 2 \end{cases} $$
où $a, b, c$ sont des constantes réelles.

Déterminer toutes les valeurs possibles des constantes $a, b, c$ pour lesquelles la fonction $f$ est continue sur $\mathbb{R}$.

## Corrigé

Pour que la fonction $f$ soit continue sur $\mathbb{R}$, elle doit satisfaire deux conditions principales :
1.  Elle doit être continue sur chaque intervalle ouvert où elle est définie par une expression unique.
2.  Elle doit être continue aux points où la définition de la fonction change, c'est-à-dire aux points de raccordement.

### 1. Continuité sur les intervalles ouverts

Examinons la continuité de $f$ sur les intervalles ouverts $(-\infty, 1)$, $(1, 2)$ et $(2, \infty)$.

*   **Sur l'intervalle $(-\infty, 1)$ :**
    Pour tout $x \in (-\infty, 1)$, la fonction est définie par $f(x) = x^2 + ax + 1$. Cette expression est un polynôme du second degré. Les fonctions polynomiales sont connues pour être continues sur tout $\mathbb{R}$. Par conséquent, $f$ est continue sur $(-\infty, 1)$ pour toutes les valeurs réelles de la constante $a$.

*   **Sur l'intervalle $(1, 2)$ :**
    Pour tout $x \in (1, 2)$, la fonction est définie par $f(x) = bx^2 + cx + 2$. Cette expression est également un polynôme du second degré. Par conséquent, $f$ est continue sur $(1, 2)$ pour toutes les valeurs réelles des constantes $b$ et $c$.

*   **Sur l'intervalle $(2, \infty)$ :**
    Pour tout $x \in (2, \infty)$, la fonction est définie par $f(x) = \frac{1}{x-1}$. Cette expression est une fonction rationnelle. Une fonction rationnelle est continue sur son domaine de définition, c'est-à-dire partout où son dénominateur n'est pas nul. Ici, le dénominateur est $x-1$. Pour $x \in (2, \infty)$, nous avons $x > 2$, ce qui implique $x-1 > 1$. Puisque $x-1$ est strictement positif, il n'est jamais nul sur cet intervalle. Par conséquent, $f$ est continue sur $(2, \infty)$.

### 2. Continuité aux points de raccordement

Il nous reste à assurer la continuité de $f$ aux points de raccordement, qui sont $x=1$ et $x=2$.

#### 2.1. Continuité au point $x=1$

Pour que la fonction $f$ soit continue en $x=1$, il faut que la limite de $f(x)$ lorsque $x$ tend vers $1$ existe et soit égale à la valeur de la fonction en $x=1$. Cela se traduit par la condition :
$$ \lim_{x \to 1^-} f(x) = \lim_{x \to 1^+} f(x) = f(1) $$

*   **Calcul de $f(1)$ :**
    Selon la définition de $f(x)$, pour $x=1$ (qui satisfait $1 \le x < 2$), l'expression à utiliser est $bx^2 + cx + 2$.
    Donc, $f(1) = b(1)^2 + c(1) + 2 = b+c+2$.

*   **Calcul de la limite à gauche en $x=1$ :**
    Pour $x < 1$, l'expression de $f(x)$ est $x^2 + ax + 1$.
    $$ \lim_{x \to 1^-} f(x) = \lim_{x \to 1^-} (x^2 + ax + 1) $$
    Puisque $x^2 + ax + 1$ est un polynôme, sa limite en $x=1$ est obtenue par simple substitution :
    $$ \lim_{x \to 1^-} f(x) = (1)^2 + a(1) + 1 = 1+a+1 = 2+a $$

*   **Calcul de la limite à droite en $x=1$ :**
    Pour $x > 1$ (et $x < 2$), l'expression de $f(x)$ est $bx^2 + cx + 2$.
    $$ \lim_{x \to 1^+} f(x) = \lim_{x \to 1^+} (bx^2 + cx + 2) $$
    Puisque $bx^2 + cx + 2$ est un polynôme, sa limite en $x=1$ est obtenue par simple substitution :
    $$ \lim_{x \to 1^+} f(x) = b(1)^2 + c(1) + 2 = b+c+2 $$

Pour assurer la continuité en $x=1$, nous devons égaliser ces trois valeurs :
$$ 2+a = b+c+2 $$
En soustrayant $2$ des deux côtés de l'équation, nous obtenons la première condition sur les constantes $a, b, c$ :
$$ a = b+c \quad \text{(Équation 1)} $$

#### 2.2. Continuité au point $x=2$

Pour que la fonction $f$ soit continue en $x=2$, il faut que la limite de $f(x)$ lorsque $x$ tend vers $2$ existe et soit égale à la valeur de la fonction en $x=2$. Cela se traduit par la condition :
$$ \lim_{x \to 2^-} f(x) = \lim_{x \to 2^+} f(x) = f(2) $$

*   **Calcul de $f(2)$ :**
    Selon la définition de $f(x)$, pour $x=2$ (qui satisfait $x \ge 2$), l'expression à utiliser est $\frac{1}{x-1}$.
    Donc, $f(2) = \frac{1}{2-1} = \frac{1}{1} = 1$.

*   **Calcul de la limite à gauche en $x=2$ :**
    Pour $x < 2$ (et $x \ge 1$), l'expression de $f(x)$ est $bx^2 + cx + 2$.
    $$ \lim_{x \to 2^-} f(x) = \lim_{x \to 2^-} (bx^2 + cx + 2) $$
    Puisque $bx^2 + cx + 2$ est un polynôme, sa limite en $x=2$ est obtenue par simple substitution :
    $$ \lim_{x \to 2^-} f(x) = b(2)^2 + c(2) + 2 = 4b+2c+2 $$

*   **Calcul de la limite à droite en $x=2$ :**
    Pour $x > 2$, l'expression de $f(x)$ est $\frac{1}{x-1}$.
    $$ \lim_{x \to 2^+} f(x) = \lim_{x \to 2^+} \frac{1}{x-1} $$
    Puisque $\frac{1}{x-1}$ est une fonction rationnelle continue en $x=2$, sa limite est obtenue par simple substitution :
    $$ \lim_{x \to 2^+} f(x) = \frac{1}{2-1} = \frac{1}{1} = 1 $$

Pour assurer la continuité en $x=2$, nous devons égaliser ces trois valeurs :
$$ 4b+2c+2 = 1 $$
En soustrayant $2$ des deux côtés de l'équation, nous obtenons la deuxième condition sur les constantes $a, b, c$ :
$$ 4b+2c = -1 \quad \text{(Équation 2)} $$

### 3. Résolution du système d'équations

Nous avons maintenant un système de deux équations linéaires avec trois inconnues $a, b, c$ :
1.  $a = b+c$
2.  $4b+2c = -1$

Ce système est sous-déterminé, ce qui signifie qu'il n'y a pas une solution unique pour $a, b, c$, mais plutôt une infinité de solutions qui peuvent être exprimées en fonction d'un paramètre libre. Nous allons choisir d'exprimer $a$ et $c$ en fonction de $b$.

À partir de l'Équation 2, nous pouvons isoler $c$ :
$$ 2c = -1 - 4b $$
En divisant par $2$, nous obtenons :
$$ c = -\frac{1}{2} - 2b $$

Maintenant, nous substituons cette expression de $c$ dans l'Équation 1 :
$$ a = b + \left(-\frac{1}{2} - 2b\right) $$
$$ a = b - \frac{1}{2} - 2b $$
En regroupant les termes en $b$, nous obtenons :
$$ a = -\frac{1}{2} - b $$

Ainsi, pour que la fonction $f$ soit continue sur $\mathbb{R}$, les constantes $a, b, c$ doivent satisfaire les relations suivantes :
$$ a = -\frac{1}{2} - b $$
$$ c = -\frac{1}{2} - 2b $$
où $b$ peut être n'importe quel nombre réel.

### 4. Conclusion

La fonction $f$ est continue sur $\mathbb{R}$ si et seulement si les constantes $a, b, c$ vérifient les conditions suivantes :
$$ \begin{cases} a = -\frac{1}{2} - b \\ c = -\frac{1}{2} - 2b \\ b \in \mathbb{R} \end{cases} $$
Ces relations définissent l'ensemble de toutes les combinaisons de $(a, b, c)$ pour lesquelles $f$ est continue sur $\mathbb{R}$. Par exemple, si nous choisissons $b=0$, alors $a = -\frac{1}{2}$ et $c = -\frac{1}{2}$. Si nous choisissons $b=1$, alors $a = -\frac{3}{2}$ et $c = -\frac{5}{2}$. Toutes ces triades $(a, b, c)$ garantissent la continuité de la fonction $f$ sur l'ensemble des nombres réels.