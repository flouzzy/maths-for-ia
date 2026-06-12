En tant que Professeur de Mathématiques à l'ENS, je vous propose l'exercice suivant pour le Jalon 3. Il mettra à l'épreuve votre maîtrise de la quantification, de l'ordre des quantificateurs et de la négation, ainsi que votre rigueur dans la manipulation des définitions.

---

## Exercice 7 (Jalon 3 : Quantification, ordre des quantificateurs, négation)

**Niveau de difficulté :** $\star \star \star \star \text{ sur } 5$

Soit $f: \mathbb{R} \to \mathbb{R}$ une fonction.

On considère la propriété $P(f)$ suivante, exprimée en langage courant :

*« Pour tout point $x$ de $\mathbb{R}$, il existe un voisinage ouvert de $x$ sur lequel la fonction $f$ est uniformément continue. »*

---

### Énoncé

**Partie A : Formalisation et interprétation**

1.  Écrire la propriété $P(f)$ de manière formelle en utilisant des quantificateurs ($\forall, \exists$), des opérateurs logiques ($\land, \lor, \implies, \neg$) et en spécifiant strictement le type de chaque objet mathématique (par exemple, $x \in \mathbb{R}$, $r \in \mathbb{R}^*_+$, etc.). Pour un voisinage ouvert de $x$, on utilisera un intervalle ouvert centré en $x$, de la forme $]x-r, x+r[$ pour un certain $r > 0$.
2.  Quel est le nom usuel de cette propriété pour une fonction $f: \mathbb{R} \to \mathbb{R}$ ?

**Partie B : Négation**

1.  Écrire la négation de la propriété $P(f)$, notée $\neg P(f)$, de manière formelle. Détailler chaque étape de la négation.
2.  Écrire la propriété $\neg P(f)$ en langage courant, de la manière la plus claire et concise possible.

**Partie C : Application**

1.  Soit la fonction $f_1: \mathbb{R} \to \mathbb{R}$ définie par $f_1(x) = x^2$. Montrer, en utilisant la définition formelle de $P(f)$, que $f_1$ satisfait la propriété $P(f_1)$.
2.  Soit la fonction $f_2: \mathbb{R} \to \mathbb{R}$ définie par $f_2(x) = \begin{cases} \sin(1/x) & \text{si } x \neq 0 \\ 0 & \text{si } x = 0 \end{cases}$. Montrer, en utilisant la définition formelle de $\neg P(f)$, que $f_2$ satisfait la propriété $\neg P(f_2)$.

---

### Correction ultra-détaillée

#### Partie A : Formalisation et interprétation

1.  **Formalisation de $P(f)$ :**

    Décomposons l'énoncé en langage courant :
    *   « Pour tout point $x$ de $\mathbb{R}$ » : $\forall x \in \mathbb{R}$
    *   « il existe un voisinage ouvert de $x$ » : Cela signifie qu'il existe un nombre réel $r$ strictement positif tel que l'intervalle $]x-r, x+r[$ est un tel voisinage. Donc : $\exists r \in \mathbb{R}^*_+$
    *   « sur lequel la fonction $f$ est uniformément continue » : La définition de l'uniforme continuité d'une fonction $f$ sur un ensemble $A$ est : $\forall \epsilon > 0, \exists \delta > 0, \forall y \in A, \forall z \in A, (|y-z| < \delta \implies |f(y)-f(z)| < \epsilon)$. Ici, l'ensemble $A$ est le voisinage $]x-r, x+r[$.

    En combinant ces éléments, la propriété $P(f)$ s'écrit formellement :

    $$
    P(f) : \forall x \in \mathbb{R}, \exists r \in \mathbb{R}^*_+, \left( \forall \epsilon \in \mathbb{R}^*_+, \exists \delta \in \mathbb{R}^*_+, \forall y \in \mathbb{R}, \forall z \in \mathbb{R}, \left( (x-r < y < x+r \land x-r < z < x+r \land |y-z| < \delta) \implies |f(y)-f(z)| < \epsilon \right) \right)
    $$

    Pour plus de concision, on peut noter $V_r(x) = ]x-r, x+r[$ :

    $$
    P(f) : \forall x \in \mathbb{R}, \exists r \in \mathbb{R}^*_+, \left( \forall \epsilon \in \mathbb{R}^*_+, \exists \delta \in \mathbb{R}^*_+, \forall y \in V_r(x), \forall z \in V_r(x), \left( |y-z| < \delta \implies |f(y)-f(z)| < \epsilon \right) \right)
    $$

    **Typage strict des objets mathématiques :**
    *   $x \in \mathbb{R}$ (nombre réel)
    *   $r \in \mathbb{R}^*_+$ (nombre réel strictement positif)
    *   $\epsilon \in \mathbb{R}^*_+$ (nombre réel strictement positif)
    *   $\delta \in \mathbb{R}^*_+$ (nombre réel strictement positif)
    *   $y \in \mathbb{R}$ (nombre réel)
    *   $z \in \mathbb{R}$ (nombre réel)
    *   $f: \mathbb{R} \to \mathbb{R}$ (fonction de $\mathbb{R}$ dans $\mathbb{R}$)

2.  **Nom usuel de la propriété :**
    Cette propriété est appelée la **continuité uniforme locale** (ou "localement uniformément continue"). Pour une fonction définie sur $\mathbb{R}$, cette propriété est équivalente à la continuité de la fonction sur $\mathbb{R}$.

#### Partie B : Négation

1.  **Négation formelle de $P(f)$ :**

    Partons de la forme $P(f) : \forall x \in \mathbb{R}, \exists r \in \mathbb{R}^*_+, Q(x,r)$, où $Q(x,r)$ est la propriété "$f$ est uniformément continue sur $V_r(x)$".
    La négation $\neg P(f)$ se construit en appliquant les règles de négation des quantificateurs et de l'implication :
    *   $\neg (\forall A, B)$ devient $\exists A, \neg B$.
    *   $\neg (\exists A, B)$ devient $\forall A, \neg B$.
    *   $\neg (P \implies Q)$ devient $P \land \neg Q$.

    Appliquons ces règles étape par étape à $P(f)$ :

    $$
    P(f) : \forall x \in \mathbb{R}, \exists r \in \mathbb{R}^*_+, \left( \forall \epsilon \in \mathbb{R}^*_+, \exists \delta \in \mathbb{R}^*_+, \forall y \in V_r(x), \forall z \in V_r(x), \left( |y-z| < \delta \implies |f(y)-f(z)| < \epsilon \right) \right)
    $$

    1.  Négation du premier quantificateur :
        $$
        \neg P(f) : \exists x \in \mathbb{R}, \neg \left( \exists r \in \mathbb{R}^*_+, \left( \forall \epsilon \in \mathbb{R}^*_+, \exists \delta \in \mathbb{R}^*_+, \forall y \in V_r(x), \forall z \in V_r(x), \left( |y-z| < \delta \implies |f(y)-f(z)| < \epsilon \right) \right) \right)
        $$
    2.  Négation du deuxième quantificateur :
        $$
        \neg P(f) : \exists x \in \mathbb{R}, \forall r \in \mathbb{R}^*_+, \neg \left( \forall \epsilon \in \mathbb{R}^*_+, \exists \delta \in \mathbb{R}^*_+, \forall y \in V_r(x), \forall z \in V_r(x), \left( |y-z| < \delta \implies |f(y)-f(z)| < \epsilon \right) \right)
        $$
    3.  Négation du troisième quantificateur :
        $$
        \neg P(f) : \exists x \in \mathbb{R}, \forall r \in \mathbb{R}^*_+, \exists \epsilon \in \mathbb{R}^*_+, \neg \left( \exists \delta \in \mathbb{R}^*_+, \forall y \in V_r(x), \forall z \in V_r(x), \left( |y-z| < \delta \implies |f(y)-f(z)| < \epsilon \right) \right)
        $$
    4.  Négation du quatrième quantificateur :
        $$
        \neg P(f) : \exists x \in \mathbb{R}, \forall r \in \mathbb{R}^*_+, \exists \epsilon \in \mathbb{R}^*_+, \forall \delta \in \mathbb{R}^*_+, \neg \left( \forall y \in V_r(x), \forall z \in V_r(x), \left( |y-z| < \delta \implies |f(y)-f(z)| < \epsilon \right) \right)
        $$
    5.  Négation des cinquième et sixième quantificateurs :
        $$
        \neg P(f) : \exists x \in \mathbb{R}, \forall r \in \mathbb{R}^*_+, \exists \epsilon \in \mathbb{R}^*_+, \forall \delta \in \mathbb{R}^*_+, \exists y \in V_r(x), \exists z \in V_r(x), \neg \left( |y-z| < \delta \implies |f(y)-f(z)| < \epsilon \right)
        $$
    6.  Négation de l'implication $(A \implies B)$ qui est équivalente à $\neg A \lor B$. Sa négation est donc $\neg (\neg A \lor B)$, ce qui est équivalent à $A \land \neg B$.
        Ici, $A$ est "$|y-z| < \delta$" et $B$ est "$|f(y)-f(z)| < \epsilon$".
        Donc $\neg (A \implies B)$ devient "$|y-z| < \delta \land \neg (|f(y)-f(z)| < \epsilon)$", c'est-à-dire "$|y-z| < \delta \land |f(y)-f(z)| \ge \epsilon$".

    Finalement, la négation formelle de $P(f)$ est :

    $$
    \neg P(f) : \exists x \in \mathbb{R}, \forall r \in \mathbb{R}^*_+, \exists \epsilon \in \mathbb{R}^*_+, \forall \delta \in \mathbb{R}^*_+, \exists y \in \mathbb{R}, \exists z \in \mathbb{R}, \left( (x-r < y < x+r \land x-r < z < x+r \land |y-z| < \delta) \land |f(y)-f(z)| \ge \epsilon \right)
    $$

    Ou, avec la notation $V_r(x)$ :

    $$
    \neg P(f) : \exists x \in \mathbb{R}, \forall r \in \mathbb{R}^*_+, \exists \epsilon \in \mathbb{R}^*_+, \forall \delta \in \mathbb{R}^*_+, \exists y \in V_r(x), \exists z \in V_r(x), \left( |y-z| < \delta \land |f(y)-f(z)| \ge \epsilon \right)
    $$

2.  **Négation de $P(f)$ en langage courant :**

    « Il existe un point $x$ de $\mathbb{R}$ tel que, pour tout voisinage ouvert de $x$, la fonction $f$ n'est pas uniformément continue sur ce voisinage. »

    Ou, en détaillant la non-uniforme continuité :

    « Il existe un point $x$ de $\mathbb{R}$ tel que, pour tout voisinage ouvert $V$ de $x$, il existe un $\epsilon > 0$ tel que, pour tout $\delta > 0$, il existe deux points $y$ et $z$ dans $V$ vérifiant $|y-z| < \delta$ mais $|f(y)-f(z)| \ge \epsilon$. »

#### Partie C : Application

1.  **Montrer que $f_1(x) = x^2$ satisfait $P(f_1)$.**

    Nous devons montrer que :
    $$
    \forall x_0 \in \mathbb{R}, \exists r \in \mathbb{R}^*_+, \left( \forall \epsilon \in \mathbb{R}^*_+, \exists \delta \in \mathbb{R}^*_+, \forall y \in V_r(x_0), \forall z \in V_r(x_0), \left( |y-z| < \delta \implies |f_1(y)-f_1(z)| < \epsilon \right) \right)
    $$

    Soit $x_0 \in \mathbb{R}$ un point arbitraire mais fixé.

    **Choix de $r$ :**
    Nous devons trouver un $r \in \mathbb{R}^*_+$ tel que $f_1$ soit uniformément continue sur $V_r(x_0) = ]x_0-r, x_0+r[$.
    Puisque $f_1(x)=x^2$ est continue sur $\mathbb{R}$, elle est uniformément continue sur tout intervalle fermé et borné (compact). Choisissons un $r$ tel que $V_r(x_0)$ soit inclus dans un intervalle compact. Par exemple, prenons $r=1$.
    Ainsi, $V_1(x_0) = ]x_0-1, x_0+1[$. Sur cet intervalle, la fonction $f_1$ est uniformément continue.
    Alternativement, pour une preuve plus générale, on peut choisir n'importe quel $r \in \mathbb{R}^*_+$.

    Soit $r \in \mathbb{R}^*_+$ fixé (par exemple $r=1$).
    Considérons l'intervalle $V_r(x_0) = ]x_0-r, x_0+r[$.

    **Choix de $\delta$ pour un $\epsilon$ donné :**
    Soit $\epsilon \in \mathbb{R}^*_+$ un nombre réel strictement positif arbitraire mais fixé.
    Nous cherchons un $\delta \in \mathbb{R}^*_+$ tel que pour tout $y, z \in V_r(x_0)$, si $|y-z| < \delta$, alors $|f_1(y)-f_1(z)| < \epsilon$.

    Calculons $|f_1(y)-f_1(z)|$:
    $$
    |f_1(y)-f_1(z)| = |y^2-z^2| = |(y-z)(y+z)| = |y-z| \cdot |y+z|
    $$
    Puisque $y \in V_r(x_0)$ et $z \in V_r(x_0)$, nous avons :
    $x_0-r < y < x_0+r \implies |y| < |x_0|+r$
    $x_0-r < z < x_0+r \implies |z| < |x_0|+r$
    Donc,
    $|y+z| \le |y|+|z| < (|x_0|+r) + (|x_0|+r) = 2(|x_0|+r)$.

    En substituant dans l'expression de $|f_1(y)-f_1(z)|$:
    $$
    |f_1(y)-f_1(z)| < |y-z| \cdot 2(|x_0|+r)
    $$
    Nous voulons que cette quantité soit inférieure à $\epsilon$. Donc, nous voulons :
    $$
    |y-z| \cdot 2(|x_0|+r) < \epsilon
    $$
    Si $2(|x_0|+r) > 0$ (ce qui est vrai car $r>0$), nous pouvons diviser par $2(|x_0|+r)$ :
    $$
    |y-z| < \frac{\epsilon}{2(|x_0|+r)}
    $$
    Ceci nous donne une valeur pour $\delta$.

    Posons $\delta = \frac{\epsilon}{2(|x_0|+r)}$.
    Puisque $\epsilon > 0$, $|x_0| \ge 0$ et $r > 0$, nous avons $2(|x_0|+r) > 0$, donc $\delta > 0$.

    **Vérification :**
    Soient $y, z \in V_r(x_0)$ tels que $|y-z| < \delta$.
    Alors, d'après nos calculs :
    $|f_1(y)-f_1(z)| = |y-z| \cdot |y+z| < \delta \cdot 2(|x_0|+r)$
    En substituant la valeur de $\delta$ :
    $|f_1(y)-f_1(z)| < \frac{\epsilon}{2(|x_0|+r)} \cdot 2(|x_0|+r) = \epsilon$.

    Ainsi, pour tout $x_0 \in \mathbb{R}$, en choisissant $r=1$ (ou n'importe quel $r>0$), et pour tout $\epsilon > 0$, en choisissant $\delta = \frac{\epsilon}{2(|x_0|+r)}$, nous avons bien la condition d'uniforme continuité sur $V_r(x_0)$.

    Par conséquent, la fonction $f_1(x) = x^2$ satisfait la propriété $P(f_1)$.

2.  **Montrer que $f_2(x) = \begin{cases} \sin(1/x) & \text{si } x \neq 0 \\ 0 & \text{si } x = 0 \end{cases}$ satisfait $\neg P(f_2)$.**

    Nous devons montrer que :
    $$
    \exists x_0 \in \mathbb{R}, \forall r \in \mathbb{R}^*_+, \exists \epsilon \in \mathbb{R}^*_+, \forall \delta \in \mathbb{R}^*_+, \exists y \in V_r(x_0), \exists z \in V_r(x_0), \left( |y-z| < \delta \land |f_2(y)-f_2(z)| \ge \epsilon \right)
    $$

    **Choix de $x_0$ :**
    Le point de discontinuité de $f_2$ est $x=0$. C'est un bon candidat pour le point où la propriété $P(f_2)$ échoue.
    Posons $x_0 = 0 \in \mathbb{R}$.

    **Pour tout $r \in \mathbb{R}^*_+$ :**
    Soit $r \in \mathbb{R}^*_+$ un nombre réel strictement positif arbitraire mais fixé.
    Le voisinage $V_r(x_0)$ est donc $V_r(0) = ]-r, r[$.

    **Choix de $\epsilon$ :**
    Nous devons trouver un $\epsilon \in \mathbb{R}^*_+$ tel que la condition de non-uniforme continuité soit satisfaite.
    La fonction $\sin(1/x)$ oscille entre $-1$ et $1$ arbitrairement près de $0$. Nous pouvons donc trouver des points où la différence de valeur est $1 - (-1) = 2$.
    Choisissons $\epsilon = 1 \in \mathbb{R}^*_+$.

    **Pour tout $\delta \in \mathbb{R}^*_+$ :**
    Soit $\delta \in \mathbb{R}^*_+$ un nombre réel strictement positif arbitraire mais fixé.

    **Choix de $y, z \in V_r(0)$ :**
    Nous devons trouver $y, z \in ]-r, r[$ tels que $|y-z| < \delta$ et $|f_2(y)-f_2(z)| \ge 1$.
    Considérons les suites de points $y_k = \frac{1}{2\pi k}$ et $z_k = \frac{1}{2\pi k + \pi/2}$ pour $k \in \mathbb{N}^*$.
    Pour ces points, $y_k \neq 0$ et $z_k \neq 0$.
    $f_2(y_k) = \sin(2\pi k) = 0$.
    $f_2(z_k) = \sin(2\pi k + \pi/2) = 1$.
    Donc, $|f_2(y_k)-f_2(z_k)| = |0-1| = 1$.
    Cette valeur $1$ est bien $\ge \epsilon$ (car $\epsilon=1$).

    Maintenant, nous devons nous assurer que $y_k, z_k \in ]-r, r[$ et $|y_k-z_k| < \delta$.
    *   **Appartenance à $V_r(0)$ :**
        Pour $k \in \mathbb{N}^*$, $y_k > 0$ et $z_k > 0$.
        $y_k = \frac{1}{2\pi k} \to 0$ lorsque $k \to \infty$.
        $z_k = \frac{1}{2\pi k + \pi/2} \to 0$ lorsque $k \to \infty$.
        Donc, pour tout $r > 0$, il existe un entier $K_1 \in \mathbb{N}^*$ tel que pour tout $k \ge K_1$, $y_k < r$ et $z_k < r$.
        Ainsi, pour $k \ge K_1$, $y_k, z_k \in ]0, r[ \subset ]-r, r[$.

    *   **Condition sur la distance $|y_k-z_k|$ :**
        Calculons $|y_k-z_k|$ :
        $$
        |y_k-z_k| = \left| \frac{1}{2\pi k} - \frac{1}{2\pi k + \pi/2} \right| = \left| \frac{(2\pi k + \pi/2) - 2\pi k}{2\pi k (2\pi k + \pi/2)} \right| = \frac{\pi/2}{2\pi k (2\pi k + \pi/2)}
        $$
        Lorsque $k \to \infty$, cette quantité tend vers $0$.
        Donc, pour tout $\delta > 0$, il existe un entier $K_2 \in \mathbb{N}^*$ tel que pour tout $k \ge K_2$, $|y_k-z_k| < \delta$.

    **Conclusion pour $y, z$ :**
    Pour le $r$ et le $\delta$ fixés, choisissons un entier $k$ tel que $k \ge \max(K_1, K_2)$.
    Alors, pour ces $y=y_k$ et $z=z_k$ :
    1.  $y \in V_r(0)$ et $z \in V_r(0)$ (car $k \ge K_1$).
    2.  $|y-z| < \delta$ (car $k \ge K_2$).
    3.  $|f_2(y)-f_2(z)| = 1 \ge \epsilon$ (car $\epsilon=1$).

    Nous avons donc bien trouvé un $x_0=0$, et pour tout $r>0$, un $\epsilon=1$, et pour tout $\delta>0$, des $y, z$ dans $V_r(0)$ qui satisfont la condition de $\neg P(f_2)$.

    Par conséquent, la fonction $f_2(x)$ satisfait la propriété $\neg P(f_2)$.

---