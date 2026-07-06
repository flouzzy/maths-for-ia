# Exercice 9 : Fonctions continues à valeurs rationnelles

**Énoncé théorique précis :**

Soit $f: \mathbb{R} \to \mathbb{R}$ une fonction. On suppose que $f$ satisfait les deux conditions suivantes :
1.  La fonction $f$ est continue sur l'ensemble des nombres réels $\mathbb{R}$.
2.  Pour tout $x \in \mathbb{R}$, l'image $f(x)$ est un nombre rationnel, c'est-à-dire $f(x) \in \mathbb{Q}$.

Démontrer que $f$ est nécessairement une fonction constante.

---

**Corrigé exhaustif :**

Nous allons démontrer ce résultat par l'absurde, en utilisant le Théorème des Valeurs Intermédiaires (TVI) et les propriétés de densité des nombres rationnels et irrationnels dans $\mathbb{R}$.

1.  **Analyse des hypothèses :**
    *   La fonction $f$ est définie sur $\mathbb{R}$ et prend ses valeurs dans $\mathbb{R}$.
    *   La continuité de $f$ sur $\mathbb{R}$ signifie que pour tout $x_0 \in \mathbb{R}$ et pour tout $\epsilon > 0$, il existe $\delta > 0$ tel que si $|x - x_0| < \delta$, alors $|f(x) - f(x_0)| < \epsilon$. Une conséquence fondamentale de la continuité sur un intervalle est le Théorème des Valeurs Intermédiaires.
    *   La condition $f(x) \in \mathbb{Q}$ pour tout $x \in \mathbb{R}$ signifie que l'ensemble image de $f$, noté $f(\mathbb{R})$, est un sous-ensemble de $\mathbb{Q}$.

2.  **Objectif de la démonstration :**
    Nous voulons prouver que $f$ est une fonction constante. Cela signifie qu'il existe un unique nombre $c \in \mathbb{Q}$ tel que pour tout $x \in \mathbb{R}$, $f(x) = c$.

3.  **Raisonnement par l'absurde :**
    Supposons, par l'absurde, que la fonction $f$ n'est *pas* constante.
    Si $f$ n'est pas constante, cela implique qu'il existe au moins deux points distincts $a$ et $b$ dans $\mathbb{R}$ tels que leurs images par $f$ sont différentes.
    Sans perte de généralité, nous pouvons supposer que $a < b$.
    Ainsi, nous avons $f(a) \neq f(b)$.

4.  **Nature des images $f(a)$ et $f(b)$ :**
    D'après l'hypothèse (2) de l'énoncé, pour tout $x \in \mathbb{R}$, $f(x)$ est un nombre rationnel.
    Par conséquent, $f(a)$ est un nombre rationnel et $f(b)$ est un nombre rationnel.
    Puisque $f(a) \neq f(b)$, nous avons deux nombres rationnels distincts.

5.  **Existence d'un nombre irrationnel entre $f(a)$ et $f(b)$ :**
    Une propriété fondamentale des nombres réels est la densité des nombres irrationnels. Entre deux nombres réels distincts quelconques, il existe toujours un nombre irrationnel.
    Appliquons cette propriété aux deux nombres rationnels distincts $f(a)$ et $f(b)$.
    Il existe un nombre irrationnel $\alpha$ tel que $\alpha$ est strictement compris entre $f(a)$ et $f(b)$.
    C'est-à-dire, si $f(a) < f(b)$, alors $f(a) < \alpha < f(b)$.
    Si $f(b) < f(a)$, alors $f(b) < \alpha < f(a)$.

    Pour être exhaustif, démontrons l'existence d'un tel $\alpha$. Supposons $f(a) < f(b)$.
    Considérons le nombre $\alpha = f(a) + \frac{1}{\sqrt{2}}(f(b) - f(a))$.
    Puisque $f(a) < f(b)$, nous avons $f(b) - f(a) > 0$.
    Puisque $0 < \frac{1}{\sqrt{2}} < 1$, il est clair que $f(a) < \alpha < f(b)$.
    Maintenant, montrons que $\alpha$ est irrationnel.
    Supposons par contradiction que $\alpha$ est rationnel.
    Alors $\alpha - f(a)$ serait rationnel.
    Donc $\frac{1}{\sqrt{2}}(f(b) - f(a))$ serait rationnel.
    Puisque $f(b) - f(a)$ est un nombre rationnel non nul (car $f(a) \neq f(b)$), cela impliquerait que $\frac{1}{\sqrt{2}}$ est rationnel.
    Cependant, $\sqrt{2}$ est irrationnel, donc $\frac{1}{\sqrt{2}}$ est également irrationnel.
    Ceci est une contradiction.
    Par conséquent, $\alpha$ doit être un nombre irrationnel.

6.  **Application du Théorème des Valeurs Intermédiaires (TVI) :**
    La fonction $f$ est continue sur $\mathbb{R}$ par hypothèse (1).
    En particulier, $f$ est continue sur l'intervalle fermé $[a, b]$ (ou $[b, a]$ si $b < a$).
    Le Théorème des Valeurs Intermédiaires (TVI) énonce que si une fonction $g$ est continue sur un intervalle fermé $[u, v]$, alors pour toute valeur $k$ qui est comprise entre $g(u)$ et $g(v)$ (inclusivement), il existe au moins un point $c \in [u, v]$ tel que $g(c) = k$.
    Dans notre situation, la valeur $\alpha$ (qui est irrationnelle) est strictement comprise entre $f(a)$ et $f(b)$.
    Par le TVI, il doit exister un point $c \in (a, b)$ (ou $(b, a)$ si $b < a$) tel que $f(c) = \alpha$.

7.  **Obtention d'une contradiction :**
    Nous avons trouvé un point $c \in \mathbb{R}$ tel que $f(c) = \alpha$.
    D'une part, par l'hypothèse (2) de l'énoncé, pour tout $x \in \mathbb{R}$, $f(x)$ doit être un nombre rationnel. Donc $f(c)$ doit être rationnel.
    D'autre part, nous avons établi que $\alpha$ est un nombre irrationnel.
    Nous arrivons donc à la conclusion que $f(c)$ est un nombre rationnel et $f(c)$ est un nombre irrationnel simultanément, ce qui est une contradiction flagrante.

8.  **Conclusion finale :**
    L'hypothèse initiale selon laquelle la fonction $f$ n'est pas constante a conduit à une contradiction logique.
    Par conséquent, notre hypothèse de départ doit être fausse.
    La fonction $f$ doit nécessairement être une fonction constante.
    Puisque toutes les valeurs de $f$ sont rationnelles par hypothèse, cette constante doit être un nombre rationnel.
    Ainsi, il existe un $c \in \mathbb{Q}$ tel que pour tout $x \in \mathbb{R}$, $f(x) = c$.

$\square$