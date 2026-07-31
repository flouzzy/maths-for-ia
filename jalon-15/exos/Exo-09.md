---
title: "Exercice 9 : Étude des valeurs d'adhérence d'une suite définie par deux récurrences imbriquées"
theme: "Sous-suites, valeurs d'adhérence et théorème de Bolzano-Weierstrass"
difficulty: 5 étoile(s)
jalon: 15
exercice_numero: 9
auteur: "Professeur Émérite de Mathématiques"
date: "2023-10-27"
---

Soit la suite $(x_n)_{n \in \mathbb{N}}$ définie par $x_0 \in [0,1]$ et pour tout $n \ge 0$ par les relations de récurrence suivantes :
$$
\begin{cases}
x_{2n+1} = x_{2n}^2 \\
x_{2n+2} = 1 - x_{2n+1}
\end{cases}
$$

1.  Montrer que si $x_0 \in [0,1]$, alors pour tout $n \in \mathbb{N}$, $x_n \in [0, 1]$.
2.  En déduire que la suite $(x_n)$ admet au moins une valeur d'adhérence.
3.  On définit les sous-suites $(y_n)_{n \in \mathbb{N}}$ et $(z_n)_{n \in \mathbb{N}}$ par $y_n = x_{2n}$ et $z_n = x_{2n+1}$.
    a.  Établir les relations de récurrence pour $(y_n)$ et $(z_n)$.
    b.  Déterminer les points fixes de ces récurrences dans l'intervalle $[0,1]$.
4.  Soit $S$ l'ensemble des valeurs d'adhérence de la suite $(x_n)$.
    a.  Montrer que $S$ est l'union des ensembles de valeurs d'adhérence de $(y_n)$ et $(z_n)$.
    b.  Pour $x_0 = \frac{\sqrt{5}-1}{2}$, déterminer l'ensemble $S$. Justifier rigoureusement.
    c.  Pour $x_0 = 0$, déterminer l'ensemble $S$. Justifier rigoureusement.

---

### Correction de l'exercice 9

#### 1. Montrer que si $x_0 \in [0,1]$, alors pour tout $n \in \mathbb{N}$, $x_n \in [0, 1]$.

Nous allons procéder par récurrence.
**Initialisation :** Pour $n=0$, $x_0 \in [0,1]$ par hypothèse.

**Hérédité :** Supposons que pour un certain $n \in \mathbb{N}$, $x_{2n} \in [0,1]$.
Alors, la première relation de récurrence donne $x_{2n+1} = x_{2n}^2$.
Puisque $x_{2n} \in [0,1]$, on a $0 \le x_{2n} \le 1$. En élevant au carré, on obtient $0^2 \le x_{2n}^2 \le 1^2$, ce qui implique $0 \le x_{2n+1} \le 1$. Donc $x_{2n+1} \in [0,1]$.

Ensuite, la deuxième relation de récurrence donne $x_{2n+2} = 1 - x_{2n+1}$.
Puisque $x_{2n+1} \in [0,1]$, on a $0 \le x_{2n+1} \le 1$.
En multipliant par $-1$, on obtient $-1 \le -x_{2n+1} \le 0$.
En ajoutant $1$, on obtient $1-1 \le 1-x_{2n+1} \le 1+0$, ce qui implique $0 \le x_{2n+2} \le 1$. Donc $x_{2n+2} \in [0,1]$.

Ainsi, si $x_{2n} \in [0,1]$, alors $x_{2n+1} \in [0,1]$ et $x_{2n+2} \in [0,1]$.
Cela signifie que si un terme d'indice pair est dans $[0,1]$, les deux termes suivants (un impair et un pair) sont également dans $[0,1]$.
Par conséquent, par récurrence, tous les termes de la suite $(x_n)$ sont dans $[0,1]$.

**Conclusion :** Pour tout $n \in \mathbb{N}$, $x_n \in [0, 1]$.

#### 2. En déduire que la suite $(x_n)$ admet au moins une valeur d'adhérence.

La suite $(x_n)$ est une suite de nombres réels.
D'après la question 1, nous avons montré que pour tout $n \in \mathbb{N}$, $x_n \in [0,1]$.
Cela signifie que la suite $(x_n)$ est bornée, car tous ses termes sont compris entre $0$ et $1$.
Le théorème de Bolzano-Weierstrass stipule que toute suite réelle bornée admet au moins une valeur d'adhérence.
Par conséquent, la suite $(x_n)$ admet au moins une valeur d'adhérence.

#### 3. On définit les sous-suites $(y_n)_{n \in \mathbb{N}}$ et $(z_n)_{n \in \mathbb{N}}$ par $y_n = x_{2n}$ et $z_n = x_{2n+1}$.

##### a. Établir les relations de récurrence pour $(y_n)$ et $(z_n)$.

Pour la suite $(y_n)$:
$y_n = x_{2n}$.
$y_{n+1} = x_{2(n+1)} = x_{2n+2}$.
D'après la deuxième relation de récurrence de $(x_n)$, nous avons $x_{2n+2} = 1 - x_{2n+1}$.
D'après la première relation de récurrence de $(x_n)$, nous avons $x_{2n+1} = x_{2n}^2$.
En substituant $x_{2n+1}$ dans l'expression de $x_{2n+2}$, nous obtenons $x_{2n+2} = 1 - x_{2n}^2$.
Puisque $y_n = x_{2n}$ et $y_{n+1} = x_{2n+2}$, la relation de récurrence pour $(y_n)$ est :
$$y_{n+1} = 1 - y_n^2$$
Le terme initial est $y_0 = x_0$.

Pour la suite $(z_n)$:
$z_n = x_{2n+1}$.
$z_{n+1} = x_{2(n+1)+1} = x_{2n+3}$.
D'après la première relation de récurrence de $(x_n)$, nous avons $x_{2n+3} = x_{2n+2}^2$.
D'après la deuxième relation de récurrence de $(x_n)$, nous avons $x_{2n+2} = 1 - x_{2n+1}$.
En substituant $x_{2n+2}$ dans l'expression de $x_{2n+3}$, nous obtenons $x_{2n+3} = (1 - x_{2n+1})^2$.
Puisque $z_n = x_{2n+1}$ et $z_{n+1} = x_{2n+3}$, la relation de récurrence pour $(z_n)$ est :
$$z_{n+1} = (1 - z_n)^2$$
Le terme initial est $z_0 = x_1 = x_0^2$.

##### b. Déterminer les points fixes de ces récurrences dans $[0,1]$.

Pour la récurrence $y_{n+1} = 1 - y_n^2$:
Un point fixe $L_y$ satisfait $L_y = 1 - L_y^2$.
Ceci est équivalent à $L_y^2 + L_y - 1 = 0$.
Les solutions de cette équation quadratique sont données par la formule $L_y = \frac{-1 \pm \sqrt{1^2 - 4(1)(-1)}}{2(1)} = \frac{-1 \pm \sqrt{1+4}}{2} = \frac{-1 \pm \sqrt{5}}{2}$.
Nous cherchons les points fixes dans l'intervalle $[0,1]$.
La solution $L_y = \frac{-1 - \sqrt{5}}{2}$ est négative (environ $-1.618$), donc elle n'est pas dans $[0,1]$.
La solution $L_y = \frac{-1 + \sqrt{5}}{2}$ est positive (environ $0.618$). Puisque $\sqrt{5} \approx 2.236$, $0 < \frac{-1 + \sqrt{5}}{2} < 1$.
Donc, le seul point fixe de la récurrence $(y_n)$ dans $[0,1]$ est $\alpha = \frac{\sqrt{5}-1}{2}$.

Pour la récurrence $z_{n+1} = (1 - z_n)^2$:
Un point fixe $L_z$ satisfait $L_z = (1 - L_z)^2$.
Ceci est équivalent à $L_z = 1 - 2L_z + L_z^2$.
Réarrangeant les termes, nous obtenons $L_z^2 - 3L_z + 1 = 0$.
Les solutions de cette équation quadratique sont données par la formule $L_z = \frac{-(-3) \pm \sqrt{(-3)^2 - 4(1)(1)}}{2(1)} = \frac{3 \pm \sqrt{9-4}}{2} = \frac{3 \pm \sqrt{5}}{2}$.
Nous cherchons les points fixes dans l'intervalle $[0,1]$.
La solution $L_z = \frac{3 + \sqrt{5}}{2}$ est supérieure à $1$ (environ $2.618$), donc elle n'est pas dans $[0,1]$.
La solution $L_z = \frac{3 - \sqrt{5}}{2}$ est positive (environ $0.382$). Puisque $\sqrt{5} \approx 2.236$, $0 < \frac{3 - \sqrt{5}}{2} < 1$.
Donc, le seul point fixe de la récurrence $(z_n)$ dans $[0,1]$ est $\beta = \frac{3-\sqrt{5}}{2}$.

#### 4. Soit $S$ l'ensemble des valeurs d'adhérence de la suite $(x_n)$.

##### a. Montrer que $S$ est l'union des ensembles de valeurs d'adhérence de $(y_n)$ et $(z_n)$.

Soit $S_y$ l'ensemble des valeurs d'adhérence de $(y_n)$ et $S_z$ l'ensemble des valeurs d'adhérence de $(z_n)$.
Par définition, $y_n = x_{2n}$ est la sous-suite des termes d'indices pairs de $(x_n)$, et $z_n = x_{2n+1}$ est la sous-suite des termes d'indices impairs de $(x_n)$.

1.  **Montrons que $S_y \cup S_z \subseteq S$ :**
    Soit $L \in S_y$. Par définition, il existe une sous-suite $(y_{n_k})$ de $(y_n)$ telle que $y_{n_k} \to L$.
    Puisque $y_{n_k} = x_{2n_k}$, la suite $(x_{2n_k})$ est une sous-suite de $(x_n)$ qui converge vers $L$.
    Donc $L$ est une valeur d'adhérence de $(x_n)$, ce qui signifie $L \in S$.
    De même, si $L \in S_z$, il existe une sous-suite $(z_{n_k})$ de $(z_n)$ telle que $z_{n_k} \to L$.
    Puisque $z_{n_k} = x_{2n_k+1}$, la suite $(x_{2n_k+1})$ est une sous-suite de $(x_n)$ qui converge vers $L$.
    Donc $L$ est une valeur d'adhérence de $(x_n)$, ce qui signifie $L \in S$.
    Par conséquent, $S_y \cup S_z \subseteq S$.

2.  **Montrons que $S \subseteq S_y \cup S_z$ :**
    Soit $L \in S$. Par définition, il existe une sous-suite $(x_{k_j})$ de $(x_n)$ telle que $x_{k_j} \to L$.
    La suite des indices $(k_j)$ peut contenir une infinité d'indices pairs, une infinité d'indices impairs, ou une infinité d'indices d'un seul type.
    *   **Cas 1 :** La sous-suite $(x_{k_j})$ contient une infinité de termes d'indices pairs.
        Alors il existe une sous-sous-suite $(x_{k_{j_m}})$ où tous les $k_{j_m}$ sont pairs.
        Soit $k_{j_m} = 2n_m$. Alors $(x_{2n_m})$ est une sous-suite de $(y_n)$ qui converge vers $L$.
        Donc $L \in S_y$.
    *   **Cas 2 :** La sous-suite $(x_{k_j})$ contient une infinité de termes d'indices impairs.
        Alors il existe une sous-sous-suite $(x_{k_{j_m}})$ où tous les $k_{j_m}$ sont impairs.
        Soit $k_{j_m} = 2n_m+1$. Alors $(x_{2n_m+1})$ est une sous-suite de $(z_n)$ qui converge vers $L$.
        Donc $L \in S_z$.
    *   **Cas 3 :** La sous-suite $(x_{k_j})$ contient un nombre fini d'indices pairs et un nombre fini d'indices impairs.
        Ceci est impossible car la suite $(k_j)$ est infinie. Elle doit contenir une infinité d'indices pairs ou une infinité d'indices impairs (ou les deux).

    Dans tous les cas, $L \in S_y$ ou $L \in S_z$.
    Par conséquent, $S \subseteq S_y \cup S_z$.

**Conclusion :** L'ensemble des valeurs d'adhérence de $(x_n)$ est l'union des ensembles de valeurs d'adhérence de $(y_n)$ et $(z_n)$, c'est-à-dire $S = S_y \cup S_z$.

##### b. Pour $x_0 = \frac{\sqrt{5}-1}{2}$, déterminer l'ensemble $S$. Justifier rigoureusement.

Soit $x_0 = \alpha = \frac{\sqrt{5}-1}{2}$.

Pour la suite $(y_n)$:
Nous avons $y_0 = x_0 = \alpha$.
La relation de récurrence est $y_{n+1} = 1 - y_n^2$.
D'après la question 3b, $\alpha$ est un point fixe de cette récurrence.
Donc, $y_1 = 1 - y_0^2 = 1 - \alpha^2 = \alpha$.
Par récurrence immédiate, $y_n = \alpha$ pour tout $n \in \mathbb{N}$.
La suite $(y_n)$ est la suite constante $(\alpha, \alpha, \alpha, \dots)$.
L'ensemble des valeurs d'adhérence de $(y_n)$ est $S_y = \{\alpha\}$.

Pour la suite $(z_n)$:
Nous avons $z_0 = x_0^2 = \alpha^2$.
Calculons $\alpha^2$:
$\alpha^2 = \left(\frac{\sqrt{5}-1}{2}\right)^2 = \frac{(\sqrt{5})^2 - 2\sqrt{5} + 1^2}{4} = \frac{5 - 2\sqrt{5} + 1}{4} = \frac{6 - 2\sqrt{5}}{4} = \frac{3 - \sqrt{5}}{2}$.
D'après la question 3b, $\beta = \frac{3-\sqrt{5}}{2}$ est le point fixe de la récurrence $z_{n+1} = (1 - z_n)^2$.
Donc $z_0 = \beta$.
Puisque $\beta$ est un point fixe, $z_1 = (1 - z_0)^2 = (1 - \beta)^2 = \beta$.
Par récurrence immédiate, $z_n = \beta$ pour tout $n \in \mathbb{N}$.
La suite $(z_n)$ est la suite constante $(\beta, \beta, \beta, \dots)$.
L'ensemble des valeurs d'adhérence de $(z_n)$ est $S_z = \{\beta\}$.

L'ensemble des valeurs d'adhérence de $(x_n)$ est $S = S_y \cup S_z = \{\alpha, \beta\}$.
Soit $S = \left\lbrace \frac{\sqrt{5}-1}{2}, \frac{3-\sqrt{5}}{2} \right\rbrace$.

##### c. Pour $x_0 = 0$, déterminer l'ensemble $S$. Justifier rigoureusement.

Soit $x_0 = 0$.

Pour la suite $(y_n)$:
Nous avons $y_0 = x_0 = 0$.
La relation de récurrence est $y_{n+1} = 1 - y_n^2$.
Calculons les premiers termes de $(y_n)$:
$y_0 = 0$
$y_1 = 1 - y_0^2 = 1 - 0^2 = 1$
$y_2 = 1 - y_1^2 = 1 - 1^2 = 0$
$y_3 = 1 - y_2^2 = 1 - 0^2 = 1$
La suite $(y_n)$ est la suite périodique $(0, 1, 0, 1, \dots)$.
Les valeurs d'adhérence de $(y_n)$ sont les limites des sous-suites convergentes.
La sous-suite des termes d'indices pairs $(y_{2k})$ est $(0, 0, 0, \dots)$, qui converge vers $0$.
La sous-suite des termes d'indices impairs $(y_{2k+1})$ est $(1, 1, 1, \dots)$, qui converge vers $1$.
Toute autre sous-suite de $(y_n)$ doit contenir une infinité de $0$ ou une infinité de $1$ (ou les deux). Si elle converge, sa limite doit être $0$ ou $1$.
Donc, l'ensemble des valeurs d'adhérence de $(y_n)$ est $S_y = \{0, 1\}$.

Pour la suite $(z_n)$:
Nous avons $z_0 = x_0^2 = 0^2 = 0$.
La relation de récurrence est $z_{n+1} = (1 - z_n)^2$.
Calculons les premiers termes de $(z_n)$:
$z_0 = 0$
$z_1 = (1 - z_0)^2 = (1 - 0)^2 = 1^2 = 1$
$z_2 = (1 - z_1)^2 = (1 - 1)^2 = 0^2 = 0$
$z_3 = (1 - z_2)^2 = (1 - 0)^2 = 1^2 = 1$
La suite $(z_n)$ est la suite périodique $(0, 1, 0, 1, \dots)$.
De manière similaire à $(y_n)$, l'ensemble des valeurs d'adhérence de $(z_n)$ est $S_z = \{0, 1\}$.

L'ensemble des valeurs d'adhérence de $(x_n)$ est $S = S_y \cup S_z = \{0, 1\} \cup \{0, 1\} = \{0, 1\}$.

**Conclusion :** Pour $x_0 = 0$, l'ensemble des valeurs d'adhérence de la suite $(x_n)$ est $S = \{0, 1\}$.
