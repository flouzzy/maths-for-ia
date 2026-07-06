# Exercice 6 - Analyse Approfondie de la Continuité d'une Fonction Définie par Morceaux

Considérons la fonction $f: \mathbb{R} \to \mathbb{R}$ définie par :
$$ f(x) = \begin{cases} \frac{\sin(3x)}{x} & \text{si } x < 0 \\ A & \text{si } x = 0 \\ \frac{e^{3x} - 1}{x} & \text{si } x > 0 \end{cases} $$
où $A$ est un paramètre réel.

---

### Question 1 : Détermination du paramètre $A$

Déterminer la valeur du paramètre réel $A$ pour laquelle la fonction $f$ est continue au point $x_0 = 0$. Justifier rigoureusement chaque étape de calcul de limite.

#### Correction Question 1

Pour que la fonction $f$ soit continue au point $x_0 = 0$, il est nécessaire et suffisant que les trois conditions suivantes soient satisfaites :
1.  $f(0)$ est défini. (C'est le cas, $f(0) = A$).
2.  La limite de $f(x)$ lorsque $x$ tend vers $0$ existe. Cela signifie que les limites à gauche et à droite doivent exister et être égales.
    $$ \lim_{x \to 0^-} f(x) = \lim_{x \to 0^+} f(x) $$
3.  Cette limite doit être égale à $f(0)$.
    $$ \lim_{x \to 0} f(x) = f(0) $$

Calculons la limite à gauche :
$$ \lim_{x \to 0^-} f(x) = \lim_{x \to 0^-} \frac{\sin(3x)}{x} $$
Pour évaluer cette limite, nous allons utiliser un changement de variable.
Soit $u = 3x$. Lorsque $x \to 0^-$, $u$ tend également vers $0^-$.
L'expression devient :
$$ \lim_{u \to 0^-} \frac{\sin(u)}{u/3} = \lim_{u \to 0^-} 3 \cdot \frac{\sin(u)}{u} $$
Nous utilisons le résultat fondamental de limite bien connu : $\lim_{u \to 0} \frac{\sin(u)}{u} = 1$.
Par conséquent,
$$ \lim_{x \to 0^-} f(x) = 3 \cdot 1 = 3 $$

Calculons la limite à droite :
$$ \lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \frac{e^{3x} - 1}{x} $$
Pour évaluer cette limite, nous allons utiliser un changement de variable.
Soit $v = 3x$. Lorsque $x \to 0^+$, $v$ tend également vers $0^+$.
L'expression devient :
$$ \lim_{v \to 0^+} \frac{e^{v} - 1}{v/3} = \lim_{v \to 0^+} 3 \cdot \frac{e^{v} - 1}{v} $$
Nous utilisons le résultat fondamental de limite bien connu : $\lim_{v \to 0} \frac{e^{v} - 1}{v} = 1$.
Par conséquent,
$$ \lim_{x \to 0^+} f(x) = 3 \cdot 1 = 3 $$

Pour que la limite de $f(x)$ lorsque $x$ tend vers $0$ existe, il faut que les limites à gauche et à droite soient égales. Dans notre cas, $\lim_{x \to 0^-} f(x) = 3$ et $\lim_{x \to 0^+} f(x) = 3$. Elles sont égales.
Donc, $\lim_{x \to 0} f(x) = 3$.

Pour que $f$ soit continue en $x_0 = 0$, il faut que $\lim_{x \to 0} f(x) = f(0)$.
Nous avons $f(0) = A$.
Ainsi, nous devons avoir $A = 3$.

La valeur du paramètre $A$ pour laquelle la fonction $f$ est continue au point $x_0 = 0$ est $A=3$.

---

### Question 2 : Preuve $\epsilon-\delta$ de la continuité

Pour la valeur de $A$ trouvée à la question précédente, c'est-à-dire $A=3$, démontrer la continuité de $f$ au point $x_0 = 0$ en utilisant la définition formelle $(\epsilon, \delta)$ de la continuité. Chaque étape doit être explicitement justifiée.

#### Correction Question 2

Nous devons démontrer que $f$ est continue en $x_0 = 0$ avec $f(0) = 3$.
La définition formelle de la continuité en un point $x_0$ est la suivante :
Pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que pour tout $x \in \mathbb{R}$, si $|x - x_0| < \delta$, alors $|f(x) - f(x_0)| < \epsilon$.
Dans notre cas, $x_0 = 0$ et $f(x_0) = f(0) = 3$. Nous devons donc montrer que pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que pour tout $x \in \mathbb{R}$, si $|x| < \delta$, alors $|f(x) - 3| < \epsilon$.

Soit $\epsilon > 0$ un nombre réel arbitrairement petit. Nous devons trouver un $\delta > 0$.

Nous allons analyser trois cas pour $x$: $x=0$, $x<0$ et $x>0$.

**Cas 1 : $x = 0$**
Si $x=0$, alors $|f(0) - 3| = |3 - 3| = 0$. Puisque $0 < \epsilon$ pour tout $\epsilon > 0$, la condition est satisfaite pour $x=0$.

**Cas 2 : $x < 0$**
Pour $x < 0$, $f(x) = \frac{\sin(3x)}{x}$. Nous devons montrer que $|\frac{\sin(3x)}{x} - 3| < \epsilon$.
Nous savons que $\frac{\sin(3x)}{x} - 3 = 3 \left( \frac{\sin(3x)}{3x} - 1 \right)$.
Donc, nous devons montrer que $\left| 3 \left( \frac{\sin(3x)}{3x} - 1 \right) \right| < \epsilon$, ce qui est équivalent à $\left| \frac{\sin(3x)}{3x} - 1 \right| < \frac{\epsilon}{3}$.

Pour $u \in ]-\pi/2, \pi/2[ \setminus \{0\}$, nous utilisons l'inégalité fondamentale suivante :
$1 - \frac{u^2}{2} < \frac{\sin u}{u} < 1$ pour $u \in ]0, \pi/2[$ et $1 < \frac{\sin u}{u} < 1 - \frac{u^2}{2}$ pour $u \in ]-\pi/2, 0[$.
Plus précisément, pour $u \in ]-\pi/2, \pi/2[ \setminus \{0\}$, nous avons l'inégalité $|\frac{\sin u}{u} - 1| < \frac{u^2}{2}$.
(Cette inégalité peut être démontrée en utilisant le développement en série de Taylor de $\sin u = u - \frac{u^3}{3!} + \dots$ ou par des arguments géométriques et le théorème des accroissements finis si ces outils sont disponibles. Dans le cadre de la continuité, elle est souvent admise ou démontrée par des moyens élémentaires.)

Soit $u = 3x$. Puisque $x < 0$, $u < 0$.
Nous voulons que $|u| < \pi/2$, ce qui signifie $|3x| < \pi/2$, donc $|x| < \pi/6$.
Si $|x| < \pi/6$, alors $|3x| < \pi/2$, et nous pouvons appliquer l'inégalité :
$$ \left| \frac{\sin(3x)}{3x} - 1 \right| < \frac{(3x)^2}{2} = \frac{9x^2}{2} $$
Nous voulons que cette quantité soit inférieure à $\frac{\epsilon}{3}$.
$$ \frac{9x^2}{2} < \frac{\epsilon}{3} $$
$$ 9x^2 < \frac{2\epsilon}{3} $$
$$ x^2 < \frac{2\epsilon}{27} $$
$$ |x| < \sqrt{\frac{2\epsilon}{27}} $$
Soit $\delta_1 = \min\left(\frac{\pi}{6}, \sqrt{\frac{2\epsilon}{27}}\right)$. Si $0 < |x| < \delta_1$ et $x<0$, alors $|f(x) - 3| < \epsilon$.

**Cas 3 : $x > 0$**
Pour $x > 0$, $f(x) = \frac{e^{3x} - 1}{x}$. Nous devons montrer que $|\frac{e^{3x} - 1}{x} - 3| < \epsilon$.
Nous savons que $\frac{e^{3x} - 1}{x} - 3 = 3 \left( \frac{e^{3x} - 1}{3x} - 1 \right)$.
Donc, nous devons montrer que $\left| 3 \left( \frac{e^{3x} - 1}{3x} - 1 \right) \right| < \epsilon$, ce qui est équivalent à $\left| \frac{e^{3x} - 1}{3x} - 1 \right| < \frac{\epsilon}{3}$.

Pour $u > 0$ et $u$ suffisamment petit (par exemple $u \in ]0, 1[$), nous utilisons l'inégalité fondamentale suivante :
$1 < \frac{e^u - 1}{u} < e^u$.
(Cette inégalité peut être démontrée en utilisant le développement en série de Taylor de $e^u = 1 + u + \frac{u^2}{2!} + \dots$ ou par des arguments de convexité et le théorème des accroissements finis.)
De cette inégalité, nous déduisons que $0 < \frac{e^u - 1}{u} - 1 < e^u - 1$.
Nous voulons que $e^u - 1 < \frac{\epsilon}{3}$.
Soit $u = 3x$. Puisque $x > 0$, $u > 0$.
Nous voulons que $u$ soit suffisamment petit. Par exemple, si $u < 1$, alors $e^u - 1 < e - 1 \approx 1.718$.
Nous voulons que $e^{3x} - 1 < \frac{\epsilon}{3}$.
Puisque la fonction $y \mapsto e^y - 1$ est strictement croissante, nous pouvons prendre le logarithme naturel :
$3x < \ln\left(1 + \frac{\epsilon}{3}\right)$.
$$ x < \frac{1}{3} \ln\left(1 + \frac{\epsilon}{3}\right) $$
Soit $\delta_2 = \min\left(\frac{1}{3}, \frac{1}{3} \ln\left(1 + \frac{\epsilon}{3}\right)\right)$. Si $0 < x < \delta_2$, alors $|f(x) - 3| < \epsilon$.
(Note : $\ln(1+y) \approx y$ pour $y$ petit, donc $\frac{1}{3} \ln(1+\frac{\epsilon}{3}) \approx \frac{1}{3} \frac{\epsilon}{3} = \frac{\epsilon}{9}$. Nous pouvons donc choisir $\delta_2$ de l'ordre de $\epsilon/9$ pour $\epsilon$ petit.)

**Conclusion pour $\delta$**
Nous avons trouvé $\delta_1$ pour $x<0$ et $\delta_2$ pour $x>0$.
Pour que la condition $|f(x) - 3| < \epsilon$ soit satisfaite pour tout $x$ tel que $|x| < \delta$, nous devons choisir $\delta$ comme le minimum de ces valeurs.
Soit $\delta = \min\left(\delta_1, \delta_2\right) = \min\left(\frac{\pi}{6}, \sqrt{\frac{2\epsilon}{27}}, \frac{1}{3}, \frac{1}{3} \ln\left(1 + \frac{\epsilon}{3}\right)\right)$.
Avec ce choix de $\delta$, pour tout $x \in \mathbb{R}$ tel que $|x| < \delta$:
*   Si $x=0$, $|f(0)-3|=0 < \epsilon$.
*   Si $x<0$, alors $|x| < \delta_1$, ce qui implique $|f(x)-3| < \epsilon$.
*   Si $x>0$, alors $|x| < \delta_2$, ce qui implique $|f(x)-3| < \epsilon$.

Par conséquent, pour tout $\epsilon > 0$, il existe un $\delta > 0$ (défini comme ci-dessus) tel que si $|x - 0| < \delta$, alors $|f(x) - f(0)| < \epsilon$.
Ceci démontre que la fonction $f$ est continue au point $x_0 = 0$ pour $A=3$.

---

### Question 3 : Continuité sur les intervalles ouverts

Étudier la continuité de $f$ sur les intervalles $]-\infty, 0[$ et $]0, +\infty[$.

#### Correction Question 3

**Sur l'intervalle $]-\infty, 0[$ :**
Pour $x \in ]-\infty, 0[$, la fonction $f(x)$ est définie par $f(x) = \frac{\sin(3x)}{x}$.
Nous pouvons écrire $f(x) = \frac{1}{x} \cdot \sin(3x)$.
La fonction $x \mapsto x$ est une fonction polynomiale, donc elle est continue sur $\mathbb{R}$. En particulier, elle est continue et non nulle sur $]-\infty, 0[$.
La fonction $x \mapsto 3x$ est une fonction polynomiale, donc elle est continue sur $\mathbb{R}$.
La fonction $u \mapsto \sin(u)$ est une fonction trigonométrique, donc elle est continue sur $\mathbb{R}$.
Par composition, la fonction $x \mapsto \sin(3x)$ est continue sur $\mathbb{R}$.
Puisque $x \mapsto \sin(3x)$ est continue sur $]-\infty, 0[$ et $x \mapsto x$ est continue et non nulle sur $]-\infty, 0[$, le quotient $f(x) = \frac{\sin(3x)}{x}$ est continu sur $]-\infty, 0[$ en tant que quotient de fonctions continues dont le dénominateur ne s'annule pas.

**Sur l'intervalle $]0, +\infty[$ :**
Pour $x \in ]0, +\infty[$, la fonction $f(x)$ est définie par $f(x) = \frac{e^{3x} - 1}{x}$.
Nous pouvons écrire $f(x) = \frac{1}{x} \cdot (e^{3x} - 1)$.
La fonction $x \mapsto x$ est une fonction polynomiale, donc elle est continue sur $\mathbb{R}$. En particulier, elle est continue et non nulle sur $]0, +\infty[$.
La fonction $x \mapsto 3x$ est une fonction polynomiale, donc elle est continue sur $\mathbb{R}$.
La fonction $u \mapsto e^u$ est une fonction exponentielle, donc elle est continue sur $\mathbb{R}$.
Par composition, la fonction $x \mapsto e^{3x}$ est continue sur $\mathbb{R}$.
La fonction $x \mapsto e^{3x} - 1$ est continue sur $\mathbb{R}$ en tant que différence de fonctions continues.
Puisque $x \mapsto e^{3x} - 1$ est continue sur $]0, +\infty[$ et $x \mapsto x$ est continue et non nulle sur $]0, +\infty[$, le quotient $f(x) = \frac{e^{3x} - 1}{x}$ est continu sur $]0, +\infty[$ en tant que quotient de fonctions continues dont le dénominateur ne s'annule pas.

En résumé, la fonction $f$ est continue sur $]-\infty, 0[$ et sur $]0, +\infty[$.

---

### Question 4 : Prolongement par continuité et application du TVI

Soit $g(x)$ la fonction définie par $g(x) = f(x)$ pour $x \neq 0$ et $g(0) = A$, où $A$ est la valeur trouvée à la Question 1.
a) Montrer que $g$ est continue sur $\mathbb{R}$.
b) Démontrer que l'équation $g(x) = 2.5$ admet au moins une solution dans l'intervalle $]-1, 1[$. Justifier l'utilisation du Théorème des Valeurs Intermédiaires (TVI).

#### Correction Question 4

a) **Montrer que $g$ est continue sur $\mathbb{R}$.**
La fonction $g(x)$ est définie comme :
$$ g(x) = \begin{cases} \frac{\sin(3x)}{x} & \text{si } x < 0 \\ 3 & \text{si } x = 0 \\ \frac{e^{3x} - 1}{x} & \text{si } x > 0 \end{cases} $$
D'après la Question 3, la fonction $f$ (et donc $g$) est continue sur $]-\infty, 0[$ et sur $]0, +\infty[$.
D'après la Question 2, la fonction $f$ (et donc $g$) est continue au point $x_0 = 0$ pour $A=3$.
Puisque $g$ est continue sur $]-\infty, 0[$, sur $]0, +\infty[$ et au point $0$, elle est continue sur l'union de ces ensembles, c'est-à-dire sur $\mathbb{R}$.
Donc, $g$ est continue sur $\mathbb{R}$.

b) **Démontrer que l'équation $g(x) = 2.5$ admet au moins une solution dans l'intervalle $]-1, 1[$.**
Nous allons utiliser le Théorème des Valeurs Intermédiaires (TVI).
Le TVI stipule que si une fonction $h$ est continue sur un intervalle fermé $[a, b]$, alors pour toute valeur $k$ comprise entre $h(a)$ et $h(b)$ (inclusivement), il existe au moins un $c \in [a, b]$ tel que $h(c) = k$.

Appliquons le TVI à la fonction $g$ sur l'intervalle $[-1, 0]$.
1.  **Continuité de $g$ sur $[-1, 0]$ :**
    Nous avons montré en 4.a) que $g$ est continue sur $\mathbb{R}$. Par conséquent, $g$ est continue sur l'intervalle fermé $[-1, 0]$.

2.  **Calcul des valeurs aux bornes de l'intervalle :**
    *   Calculons $g(-1)$ :
        Puisque $-1 < 0$, $g(-1) = \frac{\sin(3 \cdot (-1))}{-1} = \frac{\sin(-3)}{-1} = \frac{-\sin(3)}{-1} = \sin(3)$.
        La valeur $3$ est en radians. Sachant que $\pi \approx 3.14159$, $3$ radians est légèrement inférieur à $\pi$.
        $\sin(3) \approx 0.14112$.
    *   Calculons $g(0)$ :
        Par définition, $g(0) = 3$.

3.  **Vérification de la condition du TVI :**
    Nous cherchons une solution à l'équation $g(x) = 2.5$.
    Nous avons $g(-1) = \sin(3) \approx 0.14112$ et $g(0) = 3$.
    Nous constatons que $g(-1) < 2.5 < g(0)$.
    Plus précisément, $0.14112 < 2.5 < 3$.

4.  **Conclusion par le TVI :**
    Puisque $g$ est continue sur l'intervalle fermé $[-1, 0]$ et que la valeur $2.5$ est strictement comprise entre $g(-1)$ et $g(0)$, le Théorème des Valeurs Intermédiaires garantit qu'il existe au moins un nombre réel $c \in ]-1, 0[$ tel que $g(c) = 2.5$.
    L'intervalle $]-1, 0[$ est un sous-ensemble de $]-1, 1[$.
    Par conséquent, l'équation $g(x) = 2.5$ admet au moins une solution dans l'intervalle $]-1, 1[$.
