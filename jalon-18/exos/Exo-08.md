# Exercice 8 : Continuité d'une fonction définie par morceaux sur les rationnels et les irrationnels

**Jalon 18 : Continuité des fonctions d'une variable réelle**
**Difficulté :** $\star\star\star\star\text{☆}$

---

### Énoncé

Soit $f: \mathbb{R} \to \mathbb{R}$ la fonction définie par :
$$ f(x) = \begin{cases} x^2 & \text{si } x \in \mathbb{Q} \\ x & \text{si } x \notin \mathbb{Q} \end{cases} $$
Déterminer l'ensemble des points où la fonction $f$ est continue. Justifier rigoureusement votre réponse en utilisant la définition séquentielle de la continuité et la définition $\varepsilon-\delta$.

---

### Corrigé

Pour déterminer l'ensemble des points de continuité de la fonction $f$, nous allons procéder en plusieurs étapes. Nous commencerons par identifier les points candidats à la continuité en utilisant la définition séquentielle, puis nous vérifierons rigoureusement la continuité (ou la discontinuité) en ces points et en tous les autres, en utilisant la définition $\varepsilon-\delta$ de la continuité.

Rappelons la définition de la continuité en un point $x_0$:
Une fonction $f: \mathbb{R} \to \mathbb{R}$ est continue en un point $x_0 \in \mathbb{R}$ si et seulement si pour tout $\varepsilon > 0$, il existe $\delta > 0$ tel que pour tout $x \in \mathbb{R}$, si $|x - x_0| < \delta$, alors $|f(x) - f(x_0)| < \varepsilon$.

Alternativement, par la définition séquentielle:
Une fonction $f: \mathbb{R} \to \mathbb{R}$ est continue en un point $x_0 \in \mathbb{R}$ si et seulement si pour toute suite $(x_n)_{n \in \mathbb{N}}$ de nombres réels convergeant vers $x_0$, la suite $(f(x_n))_{n \in \mathbb{N}}$ converge vers $f(x_0)$.

Nous utiliserons également la propriété de densité des nombres rationnels et irrationnels dans $\mathbb{R}$:
Pour tout intervalle ouvert non vide $(a, b) \subset \mathbb{R}$, il existe un nombre rationnel $q \in (a, b)$ et un nombre irrationnel $i \in (a, b)$. Cela implique que pour tout $x_0 \in \mathbb{R}$, il existe des suites de nombres rationnels $(q_n)$ et de nombres irrationnels $(i_n)$ telles que $q_n \to x_0$ et $i_n \to x_0$.

#### Étape 1 : Identification des points candidats à la continuité

Supposons que $f$ soit continue en un point $x_0 \in \mathbb{R}$. Par la définition séquentielle de la continuité, pour toute suite $(x_n)$ convergeant vers $x_0$, nous devons avoir $\lim_{n \to \infty} f(x_n) = f(x_0)$.

1.  **Cas où $x_0 \in \mathbb{Q}$ (rationnel) :**
    Dans ce cas, $f(x_0) = x_0^2$.
    *   Considérons une suite $(q_n)_{n \in \mathbb{N}}$ de nombres rationnels telle que $q_n \to x_0$. Puisque $q_n \in \mathbb{Q}$ pour tout $n$, nous avons $f(q_n) = q_n^2$. Par les propriétés des limites, $\lim_{n \to \infty} f(q_n) = \lim_{n \to \infty} q_n^2 = x_0^2$.
    *   Considérons une suite $(i_n)_{n \in \mathbb{N}}$ de nombres irrationnels telle que $i_n \to x_0$. Puisque $i_n \notin \mathbb{Q}$ pour tout $n$, nous avons $f(i_n) = i_n$. Par les propriétés des limites, $\lim_{n \to \infty} f(i_n) = \lim_{n \to \infty} i_n = x_0$.
    Pour que $f$ soit continue en $x_0$, il faut que ces deux limites soient égales à $f(x_0)$. Ainsi, nous devons avoir $x_0^2 = x_0$.
    L'équation $x_0^2 - x_0 = 0$ se factorise en $x_0(x_0 - 1) = 0$. Les solutions sont $x_0 = 0$ ou $x_0 = 1$.
    Puisque $0 \in \mathbb{Q}$ et $1 \in \mathbb{Q}$, ces deux points sont des candidats potentiels à la continuité.

2.  **Cas où $x_0 \notin \mathbb{Q}$ (irrationnel) :**
    Dans ce cas, $f(x_0) = x_0$.
    *   Considérons une suite $(q_n)_{n \in \mathbb{N}}$ de nombres rationnels telle que $q_n \to x_0$. Puisque $q_n \in \mathbb{Q}$ pour tout $n$, nous avons $f(q_n) = q_n^2$. Par les propriétés des limites, $\lim_{n \to \infty} f(q_n) = \lim_{n \to \infty} q_n^2 = x_0^2$.
    *   Considérons une suite $(i_n)_{n \in \mathbb{N}}$ de nombres irrationnels telle que $i_n \to x_0$. Puisque $i_n \notin \mathbb{Q}$ pour tout $n$, nous avons $f(i_n) = i_n$. Par les propriétés des limites, $\lim_{n \to \infty} f(i_n) = \lim_{n \to \infty} i_n = x_0$.
    Pour que $f$ soit continue en $x_0$, il faut que ces deux limites soient égales à $f(x_0)$. Ainsi, nous devons avoir $x_0^2 = x_0$.
    Comme précédemment, les solutions sont $x_0 = 0$ ou $x_0 = 1$.
    Cependant, dans ce cas, nous avons supposé que $x_0$ est irrationnel. Or, $0$ et $1$ sont des nombres rationnels. Par conséquent, il n'y a aucun point irrationnel $x_0$ pour lequel $f$ pourrait être continue.

En résumé, les seuls points où la fonction $f$ pourrait être continue sont $x=0$ et $x=1$.

#### Étape 2 : Vérification de la continuité aux points $x=0$ et $x=1$

Nous allons utiliser la définition $\varepsilon-\delta$ pour prouver la continuité en ces points.

1.  **Continuité en $x_0 = 0$ :**
    Nous avons $f(0) = 0^2 = 0$ (car $0 \in \mathbb{Q}$).
    Nous devons montrer que pour tout $\varepsilon > 0$, il existe $\delta > 0$ tel que si $|x - 0| < \delta$, alors $|f(x) - f(0)| < \varepsilon$. C'est-à-dire, si $|x| < \delta$, alors $|f(x)| < \varepsilon$.

    *   Si $x \in \mathbb{Q}$, alors $f(x) = x^2$. Donc $|f(x)| = |x^2| = |x|^2$.
    *   Si $x \notin \mathbb{Q}$, alors $f(x) = x$. Donc $|f(x)| = |x|$.

    Nous voulons que $|f(x)| < \varepsilon$ pour tout $x$ tel que $|x| < \delta$.
    Si nous choisissons $\delta \le 1$, alors pour tout $x$ tel que $|x| < \delta$, nous avons $|x| < 1$.
    Dans ce cas, $|x|^2 < |x|$.
    Donc, si $|x| < \delta$:
    *   Si $x \in \mathbb{Q}$, $|f(x)| = |x|^2 < |x| < \delta$.
    *   Si $x \notin \mathbb{Q}$, $|f(x)| = |x| < \delta$.
    Dans les deux cas, nous avons $|f(x)| < \delta$.
    Pour que $|f(x)| < \varepsilon$, il suffit de choisir $\delta$ tel que $\delta \le \varepsilon$.
    Ainsi, en prenant $\delta = \min(1, \varepsilon)$, si $|x| < \delta$, alors $|f(x)| < \varepsilon$.
    Par conséquent, la fonction $f$ est continue en $x=0$.

2.  **Continuité en $x_0 = 1$ :**
    Nous avons $f(1) = 1^2 = 1$ (car $1 \in \mathbb{Q}$).
    Nous devons montrer que pour tout $\varepsilon > 0$, il existe $\delta > 0$ tel que si $|x - 1| < \delta$, alors $|f(x) - f(1)| < \varepsilon$. C'est-à-dire, si $|x - 1| < \delta$, alors $|f(x) - 1| < \varepsilon$.

    *   Si $x \in \mathbb{Q}$, alors $f(x) = x^2$. Donc $|f(x) - 1| = |x^2 - 1| = |(x-1)(x+1)| = |x-1||x+1|$.
    *   Si $x \notin \mathbb{Q}$, alors $f(x) = x$. Donc $|f(x) - 1| = |x-1|$.

    Nous voulons que $|f(x) - 1| < \varepsilon$ pour tout $x$ tel que $|x - 1| < \delta$.
    Choisissons $\delta \le 1$. Si $|x - 1| < \delta$, alors $x$ est dans l'intervalle $(1-\delta, 1+\delta)$. Puisque $\delta \le 1$, $x \in (0, 2)$.
    En particulier, $0 < x < 2$, ce qui implique $1 < x+1 < 3$.
    Donc, si $|x - 1| < \delta$:
    *   Si $x \in \mathbb{Q}$, $|f(x) - 1| = |x-1||x+1| < \delta \cdot 3 = 3\delta$.
    *   Si $x \notin \mathbb{Q}$, $|f(x) - 1| = |x-1| < \delta$.
    Dans les deux cas, nous avons $|f(x) - 1| < 3\delta$.
    Pour que $|f(x) - 1| < \varepsilon$, il suffit de choisir $\delta$ tel que $3\delta \le \varepsilon$, c'est-à-dire $\delta \le \varepsilon/3$.
    Ainsi, en prenant $\delta = \min(1, \varepsilon/3)$, si $|x - 1| < \delta$, alors $|f(x) - 1| < \varepsilon$.
    Par conséquent, la fonction $f$ est continue en $x=1$.

#### Étape 3 : Vérification de la discontinuité aux points $x_0 \notin \{0, 1\}$

Nous allons montrer que pour tout $x_0 \notin \{0, 1\}$, la fonction $f$ est discontinue en $x_0$. Pour cela, il suffit de trouver une suite $(x_n)$ convergeant vers $x_0$ telle que $(f(x_n))$ ne converge pas vers $f(x_0)$.

1.  **Cas où $x_0 \in \mathbb{Q}$ et $x_0 \notin \{0, 1\}$ :**
    Dans ce cas, $f(x_0) = x_0^2$. Puisque $x_0 \notin \{0, 1\}$, nous avons $x_0^2 \ne x_0$.
    Considérons une suite $(i_n)_{n \in \mathbb{N}}$ de nombres irrationnels telle que $i_n \to x_0$. Une telle suite existe en vertu de la densité des irrationnels dans $\mathbb{R}$.
    Pour chaque $i_n$, $f(i_n) = i_n$ (car $i_n \notin \mathbb{Q}$).
    Alors $\lim_{n \to \infty} f(i_n) = \lim_{n \to \infty} i_n = x_0$.
    Cependant, $f(x_0) = x_0^2$. Puisque $x_0 \ne x_0^2$, nous avons $\lim_{n \to \infty} f(i_n) \ne f(x_0)$.
    Par la définition séquentielle de la continuité, $f$ est discontinue en $x_0$.

2.  **Cas où $x_0 \notin \mathbb{Q}$ (et donc $x_0 \notin \{0, 1\}$ puisque $0, 1 \in \mathbb{Q}$) :**
    Dans ce cas, $f(x_0) = x_0$. Puisque $x_0$ est irrationnel, $x_0 \ne 0$ et $x_0 \ne 1$. Par conséquent, $x_0^2 \ne x_0$.
    Considérons une suite $(q_n)_{n \in \mathbb{N}}$ de nombres rationnels telle que $q_n \to x_0$. Une telle suite existe en vertu de la densité des rationnels dans $\mathbb{R}$.
    Pour chaque $q_n$, $f(q_n) = q_n^2$ (car $q_n \in \mathbb{Q}$).
    Alors $\lim_{n \to \infty} f(q_n) = \lim_{n \to \infty} q_n^2 = x_0^2$.
    Cependant, $f(x_0) = x_0$. Puisque $x_0^2 \ne x_0$, nous avons $\lim_{n \to \infty} f(q_n) \ne f(x_0)$.
    Par la définition séquentielle de la continuité, $f$ est discontinue en $x_0$.

#### Conclusion

En combinant les résultats des trois étapes, nous avons montré que la fonction $f$ est continue uniquement aux points $x=0$ et $x=1$. Pour tous les autres points $x \in \mathbb{R} \setminus \{0, 1\}$, la fonction $f$ est discontinue.

L'ensemble des points où la fonction $f$ est continue est donc $\{0, 1\}$.

---