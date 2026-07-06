# Exercice 7 - Exploration Approfondie de la Continuité des Fonctions d'une Variable Réelle

Cet exercice est conçu pour évaluer votre maîtrise des concepts fondamentaux et avancés de la continuité des fonctions d'une variable réelle. Il requiert une rigueur absolue dans la démonstration et l'application des théorèmes.

---

## Énoncé de l'Exercice

**Partie A : Démonstration par la Définition Epsilon-Delta**

Soit la fonction $f: \mathbb{R} \to \mathbb{R}$ définie par $f(x) = x^3$.
Démontrez, en utilisant la définition formelle $(\epsilon, \delta)$ de la continuité, que la fonction $f$ est continue en tout point $x_0 \in \mathbb{R}$.

**Partie B : Continuité d'une Fonction Définie par Morceaux avec Paramètres**

Considérons la fonction $g: \mathbb{R} \to \mathbb{R}$ définie par :
$$
g(x) = \begin{cases}
ax^2 + 3x - 1 & \text{si } x < 1 \\
b & \text{si } x = 1 \\
\frac{\sqrt{x+3}-2}{x-1} & \text{si } x > 1
\end{cases}
$$
Déterminez les valeurs des constantes réelles $a$ et $b$ pour lesquelles la fonction $g$ est continue en $x=1$.

**Partie C : Application du Théorème des Valeurs Intermédiaires**

Soit $h: [0,1] \to [0,1]$ une fonction continue sur l'intervalle fermé $[0,1]$.
Démontrez qu'il existe au moins un point $c \in [0,1]$ tel que $h(c) = c$. Un tel point $c$ est appelé point fixe de $h$.

---

## Correction Détaillée

### Partie A : Démonstration par la Définition Epsilon-Delta

Pour démontrer que $f(x) = x^3$ est continue en tout point $x_0 \in \mathbb{R}$, nous devons montrer que pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que si $|x - x_0| < \delta$, alors $|f(x) - f(x_0)| < \epsilon$.

Soit $x_0 \in \mathbb{R}$ un point arbitraire et soit $\epsilon > 0$ un nombre réel positif arbitraire.
Nous devons analyser l'expression $|f(x) - f(x_0)|$:
$$
|f(x) - f(x_0)| = |x^3 - x_0^3|
$$
Nous utilisons l'identité algébrique de la différence de cubes, $A^3 - B^3 = (A - B)(A^2 + AB + B^2)$.
$$
|x^3 - x_0^3| = |(x - x_0)(x^2 + x x_0 + x_0^2)|
$$
Par la propriété de la valeur absolue $|AB| = |A||B|$, nous obtenons :
$$
|x^3 - x_0^3| = |x - x_0| |x^2 + x x_0 + x_0^2|
$$
Nous voulons que cette expression soit inférieure à $\epsilon$. Nous avons un facteur $|x - x_0|$ que nous pouvons rendre arbitrairement petit en choisissant $\delta$. Le défi est de majorer le second facteur, $|x^2 + x x_0 + x_0^2|$.

Pour majorer $|x^2 + x x_0 + x_0^2|$, nous allons d'abord imposer une condition sur $\delta$. Choisissons $\delta \le 1$.
Si $|x - x_0| < \delta$ et $\delta \le 1$, alors $|x - x_0| < 1$.
Cette inégalité implique que $x_0 - 1 < x < x_0 + 1$.
En utilisant la propriété de la valeur absolue $|x| \le |x_0| + |x - x_0|$, nous avons :
$$
|x| < |x_0| + 1
$$
Maintenant, nous pouvons majorer le terme $|x^2 + x x_0 + x_0^2|$ en utilisant l'inégalité triangulaire $|A+B+C| \le |A| + |B| + |C|$ :
$$
|x^2 + x x_0 + x_0^2| \le |x^2| + |x x_0| + |x_0^2|
$$
Puisque $|A^2| = |A|^2$, nous avons :
$$
|x^2 + x x_0 + x_0^2| \le |x|^2 + |x||x_0| + |x_0|^2
$$
En substituant la majoration de $|x|$ que nous avons trouvée ($|x| < |x_0| + 1$) :
$$
|x^2 + x x_0 + x_0^2| < (|x_0| + 1)^2 + (|x_0| + 1)|x_0| + |x_0|^2
$$
Développons cette expression :
$$
(|x_0| + 1)^2 = x_0^2 + 2|x_0| + 1
$$
$$
(|x_0| + 1)|x_0| = |x_0|^2 + |x_0|
$$
En sommant ces termes :
$$
|x^2 + x x_0 + x_0^2| < (x_0^2 + 2|x_0| + 1) + (|x_0|^2 + |x_0|) + |x_0|^2
$$
$$
|x^2 + x x_0 + x_0^2| < 3x_0^2 + 3|x_0| + 1
$$
Soit $M = 3x_0^2 + 3|x_0| + 1$. Notez que $M$ est une constante positive qui dépend de $x_0$.
Alors, nous avons :
$$
|f(x) - f(x_0)| = |x - x_0| |x^2 + x x_0 + x_0^2| < |x - x_0| M
$$
Puisque nous avons $|x - x_0| < \delta$, nous obtenons :
$$
|f(x) - f(x_0)| < \delta M
$$
Nous voulons que cette expression soit inférieure à $\epsilon$. Donc, nous posons $\delta M < \epsilon$, ce qui implique $\delta < \frac{\epsilon}{M}$.

Pour satisfaire toutes les conditions, nous choisissons $\delta$ comme le minimum de notre condition initiale ($\delta \le 1$) et de la nouvelle condition ($\delta < \frac{\epsilon}{M}$).
$$
\delta = \min\left(1, \frac{\epsilon}{3x_0^2 + 3|x_0| + 1}\right)
$$
Avec ce choix de $\delta$, si $|x - x_0| < \delta$, alors :
1.  $|x - x_0| < 1$, ce qui nous a permis de majorer $|x^2 + x x_0 + x_0^2|$ par $M = 3x_0^2 + 3|x_0| + 1$.
2.  $|x - x_0| < \frac{\epsilon}{M}$.
Par conséquent,
$$
|f(x) - f(x_0)| = |x - x_0| |x^2 + x x_0 + x_0^2| < \left(\frac{\epsilon}{M}\right) M = \epsilon
$$
Ainsi, pour tout $x_0 \in \mathbb{R}$ et tout $\epsilon > 0$, nous avons trouvé un $\delta > 0$ tel que si $|x - x_0| < \delta$, alors $|f(x) - f(x_0)| < \epsilon$.
La fonction $f(x) = x^3$ est donc continue en tout point $x_0 \in \mathbb{R}$.

### Partie B : Continuité d'une Fonction Définie par Morceaux avec Paramètres

Pour que la fonction $g(x)$ soit continue en $x=1$, trois conditions doivent être satisfaites :
1.  La fonction $g(x)$ doit être définie en $x=1$. C'est le cas, $g(1) = b$.
2.  La limite de $g(x)$ lorsque $x$ tend vers $1$ doit exister. Cela signifie que les limites à gauche et à droite doivent exister et être égales.
3.  La limite de $g(x)$ lorsque $x$ tend vers $1$ doit être égale à $g(1)$.

**Étape 1 : Calcul de $g(1)$**
Par définition de la fonction $g(x)$, nous avons :
$$
g(1) = b
$$

**Étape 2 : Calcul de la limite à gauche en $x=1$**
Pour $x < 1$, la fonction est définie par $g(x) = ax^2 + 3x - 1$.
Puisque $P(x) = ax^2 + 3x - 1$ est une fonction polynomiale, elle est continue sur $\mathbb{R}$. Par conséquent, la limite de $P(x)$ lorsque $x$ approche $1$ par la gauche est simplement l'évaluation de $P(x)$ en $x=1$.
$$
\lim_{x \to 1^-} g(x) = \lim_{x \to 1^-} (ax^2 + 3x - 1)
$$
Par substitution directe, en raison de la continuité des polynômes :
$$
\lim_{x \to 1^-} (ax^2 + 3x - 1) = a(1)^2 + 3(1) - 1 = a + 3 - 1 = a + 2
$$

**Étape 3 : Calcul de la limite à droite en $x=1$**
Pour $x > 1$, la fonction est définie par $g(x) = \frac{\sqrt{x+3}-2}{x-1}$.
Nous calculons la limite :
$$
\lim_{x \to 1^+} g(x) = \lim_{x \to 1^+} \frac{\sqrt{x+3}-2}{x-1}
$$
Si nous substituons $x=1$ directement, nous obtenons $\frac{\sqrt{1+3}-2}{1-1} = \frac{\sqrt{4}-2}{0} = \frac{2-2}{0} = \frac{0}{0}$, qui est une forme indéterminée.
Pour lever cette indétermination, nous allons multiplier le numérateur et le dénominateur par le conjugué du numérateur, qui est $\sqrt{x+3}+2$.
$$
\lim_{x \to 1^+} \frac{\sqrt{x+3}-2}{x-1} = \lim_{x \to 1^+} \frac{(\sqrt{x+3}-2)(\sqrt{x+3}+2)}{(x-1)(\sqrt{x+3}+2)}
$$
En utilisant l'identité $(A-B)(A+B) = A^2 - B^2$ pour le numérateur :
$$
= \lim_{x \to 1^+} \frac{(x+3) - 2^2}{(x-1)(\sqrt{x+3}+2)}
$$
$$
= \lim_{x \to 1^+} \frac{x+3 - 4}{(x-1)(\sqrt{x+3}+2)}
$$
$$
= \lim_{x \to 1^+} \frac{x-1}{(x-1)(\sqrt{x+3}+2)}
$$
Puisque nous considérons la limite lorsque $x \to 1^+$, $x$ est proche de $1$ mais $x \ne 1$. Par conséquent, $x-1 \ne 0$, et nous pouvons simplifier le terme $(x-1)$ au numérateur et au dénominateur :
$$
= \lim_{x \to 1^+} \frac{1}{\sqrt{x+3}+2}
$$
Maintenant, la substitution directe de $x=1$ ne conduit plus à une forme indéterminée. La fonction $h(x) = \sqrt{x+3}+2$ est continue pour $x \ge -3$. Puisque $x=1$ est dans ce domaine, nous pouvons substituer :
$$
= \frac{1}{\sqrt{1+3}+2} = \frac{1}{\sqrt{4}+2} = \frac{1}{2+2} = \frac{1}{4}
$$

**Étape 4 : Égalisation des limites et de la valeur de la fonction**
Pour que $g(x)$ soit continue en $x=1$, les trois valeurs doivent être égales :
$$
\lim_{x \to 1^-} g(x) = \lim_{x \to 1^+} g(x) = g(1)
$$
En substituant les valeurs calculées :
$$
a + 2 = \frac{1}{4} = b
$$
De l'égalité $b = \frac{1}{4}$, nous obtenons la valeur de $b$.
De l'égalité $a + 2 = \frac{1}{4}$, nous résolvons pour $a$ :
$$
a = \frac{1}{4} - 2
$$
Pour soustraire, nous mettons $2$ au même dénominateur que $\frac{1}{4}$ : $2 = \frac{8}{4}$.
$$
a = \frac{1}{4} - \frac{8}{4} = \frac{1 - 8}{4} = -\frac{7}{4}
$$
Ainsi, pour que la fonction $g(x)$ soit continue en $x=1$, les constantes $a$ et $b$ doivent prendre les valeurs suivantes :
$$
a = -\frac{7}{4} \quad \text{et} \quad b = \frac{1}{4}
$$

### Partie C : Application du Théorème des Valeurs Intermédiaires

Nous voulons démontrer qu'il existe au moins un point $c \in [0,1]$ tel que $h(c) = c$.
Pour cela, nous allons définir une nouvelle fonction auxiliaire $k(x)$ et appliquer le Théorème des Valeurs Intermédiaires (TVI).

**Étape 1 : Définition de la fonction auxiliaire**
Soit la fonction $k: [0,1] \to \mathbb{R}$ définie par $k(x) = h(x) - x$.
Un point fixe $c$ de $h$ est une valeur pour laquelle $h(c) = c$, ce qui est équivalent à $h(c) - c = 0$, c'est-à-dire $k(c) = 0$. Notre objectif est donc de montrer l'existence d'une racine pour $k(x)$ dans l'intervalle $[0,1]$.

**Étape 2 : Vérification de la continuité de $k(x)$**
Pour appliquer le TVI, la fonction $k(x)$ doit être continue sur l'intervalle fermé $[0,1]$.
1.  La fonction $h(x)$ est continue sur $[0,1]$ par hypothèse de l'énoncé.
2.  La fonction $j(x) = x$ est une fonction polynomiale (spécifiquement, la fonction identité), et les fonctions polynomiales sont continues sur tout $\mathbb{R}$, et donc sur l'intervalle $[0,1]$.
3.  Le Théorème sur la somme/différence de fonctions continues stipule que si $f_1$ et $f_2$ sont continues sur un intervalle, alors $f_1 \pm f_2$ est aussi continue sur cet intervalle.
Puisque $h(x)$ et $j(x)=x$ sont continues sur $[0,1]$, leur différence $k(x) = h(x) - x$ est également continue sur $[0,1]$.

**Étape 3 : Évaluation de $k(x)$ aux bornes de l'intervalle**
Nous évaluons la fonction $k(x)$ aux extrémités de l'intervalle $[0,1]$ :
1.  Pour $x=0$:
    $k(0) = h(0) - 0 = h(0)$.
    Par hypothèse, la fonction $h$ a pour codomaine $[0,1]$, ce qui signifie que pour tout $x \in [0,1]$, $0 \le h(x) \le 1$.
    En particulier, pour $x=0$, nous avons $0 \le h(0) \le 1$.
    Donc, $k(0) = h(0) \ge 0$.

2.  Pour $x=1$:
    $k(1) = h(1) - 1$.
    De même, pour $x=1$, nous avons $0 \le h(1) \le 1$.
    En soustrayant $1$ de cette inégalité, nous obtenons :
    $0 - 1 \le h(1) - 1 \le 1 - 1$
    $-1 \le h(1) - 1 \le 0$.
    Donc, $k(1) = h(1) - 1 \le 0$.

**Étape 4 : Application du Théorème des Valeurs Intermédiaires**
Nous avons une fonction $k(x)$ qui est continue sur l'intervalle fermé $[0,1]$.
Nous avons également déterminé que $k(0) \ge 0$ et $k(1) \le 0$.
Le Théorème des Valeurs Intermédiaires (TVI) stipule que si une fonction $f$ est continue sur un intervalle fermé $[a,b]$, et si $y_0$ est un nombre quelconque entre $f(a)$ et $f(b)$ (inclusivement), alors il existe au moins un $c \in [a,b]$ tel que $f(c) = y_0$.

Considérons les cas possibles pour $k(0)$ et $k(1)$ :
*   **Cas 1 :** Si $k(0) = 0$.
    Alors $h(0) - 0 = 0$, ce qui signifie $h(0) = 0$. Dans ce cas, $c=0$ est un point fixe.
*   **Cas 2 :** Si $k(1) = 0$.
    Alors $h(1) - 1 = 0$, ce qui signifie $h(1) = 1$. Dans ce cas, $c=1$ est un point fixe.
*   **Cas 3 :** Si $k(0) > 0$ et $k(1) < 0$.
    Dans ce cas, $k(1) < 0 < k(0)$. Le nombre $0$ est strictement compris entre $k(1)$ et $k(0)$.
    Puisque $k(x)$ est continue sur $[0,1]$, le TVI garantit qu'il existe au moins un $c \in (0,1)$ tel que $k(c) = 0$.
    Par définition de $k(x)$, $k(c) = h(c) - c$. Donc, $h(c) - c = 0$, ce qui implique $h(c) = c$.

Dans tous les cas (que $k(0)$ ou $k(1)$ soit nul, ou que $0$ soit strictement entre eux), il existe au moins un $c \in [0,1]$ tel que $k(c) = 0$.
Par conséquent, il existe au moins un $c \in [0,1]$ tel que $h(c) = c$.
La fonction $h$ admet donc au moins un point fixe dans l'intervalle $[0,1]$.
