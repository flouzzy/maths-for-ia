# Exercice 8 - Continuité des fonctions d'une variable réelle : Analyse approfondie et applications

Cet exercice explore la notion de continuité sous différents angles, allant de la démonstration formelle à l'application de théorèmes fondamentaux.

## Partie A : Démonstration formelle de continuité

Soit la fonction $f: \mathbb{R} \to \mathbb{R}$ définie par $f(x) = x^3$.
Démontrer, en utilisant la définition formelle $(\epsilon, \delta)$ de la continuité, que $f$ est continue en tout point $x_0 \in \mathbb{R}$.

## Partie B : Continuité d'une fonction définie par morceaux

Soit la fonction $g: \mathbb{R} \to \mathbb{R}$ définie par :
$$ g(x) = \begin{cases} \frac{\sin(ax)}{x} & \text{si } x < 0 \\ b & \text{si } x = 0 \\ \frac{e^{2x}-1}{x} & \text{si } x > 0 \end{cases} $$
Déterminer les valeurs des constantes réelles $a$ et $b$ pour que la fonction $g$ soit continue sur $\mathbb{R}$.

## Partie C : Application du Théorème des Valeurs Intermédiaires

Soit la fonction $h: \mathbb{R} \to \mathbb{R}$ définie par $h(x) = x^3 - 3x + 1$.
1.  Montrer que l'équation $h(x) = 0$ possède au moins une solution dans l'intervalle $]-2, -1[$.
2.  Montrer que l'équation $h(x) = 0$ possède au moins une solution dans l'intervalle $]0, 1[$.
3.  Montrer que l'équation $h(x) = 0$ possède au moins une solution dans l'intervalle $]1, 2[$.
4.  En déduire le nombre exact de racines réelles de l'équation $h(x) = 0$.

## Partie D : Point fixe d'une fonction continue

Soit $I = [a, b]$ un intervalle fermé et borné de $\mathbb{R}$, avec $a < b$. Soit $f: I \to I$ une fonction continue.
Démontrer qu'il existe au moins un point $c \in I$ tel que $f(c) = c$. (Un tel point $c$ est appelé un point fixe de $f$).

---

# Correction de l'Exercice 8

## Partie A : Démonstration formelle de continuité

Nous devons démontrer que la fonction $f(x) = x^3$ est continue en tout point $x_0 \in \mathbb{R}$ en utilisant la définition formelle $(\epsilon, \delta)$.

**Définition de la continuité en un point :**
Une fonction $f: \mathbb{R} \to \mathbb{R}$ est continue en un point $x_0 \in \mathbb{R}$ si et seulement si pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que pour tout $x \in \mathbb{R}$, si $|x - x_0| < \delta$, alors $|f(x) - f(x_0)| < \epsilon$.

**Démonstration :**
Soit $x_0 \in \mathbb{R}$ un point arbitraire.
Soit $\epsilon > 0$ un nombre réel strictement positif arbitraire. Nous cherchons à trouver un $\delta > 0$ tel que si $|x - x_0| < \delta$, alors $|f(x) - f(x_0)| < \epsilon$.

Nous commençons par analyser l'expression $|f(x) - f(x_0)|$:
$$ |f(x) - f(x_0)| = |x^3 - x_0^3| $$
Nous utilisons l'identité de factorisation de la différence de cubes, $A^3 - B^3 = (A - B)(A^2 + AB + B^2)$. Ici, $A=x$ et $B=x_0$.
$$ |x^3 - x_0^3| = |(x - x_0)(x^2 + x x_0 + x_0^2)| $$
Par la propriété du produit des valeurs absolues, $|AB| = |A||B|$ :
$$ |x^3 - x_0^3| = |x - x_0| |x^2 + x x_0 + x_0^2| $$
Notre objectif est de rendre cette expression inférieure à $\epsilon$. Nous avons déjà le facteur $|x - x_0|$, que nous pouvons rendre arbitrairement petit en choisissant $\delta$ petit. Le défi est de borner le second facteur, $|x^2 + x x_0 + x_0^2|$.

Pour borner ce facteur, nous allons d'abord imposer une condition sur $\delta$. Choisissons $\delta_1 = 1$.
Si $|x - x_0| < \delta_1 = 1$, alors nous avons :
$$ -1 < x - x_0 < 1 $$
En ajoutant $x_0$ à toutes les parties de l'inégalité, nous obtenons :
$$ x_0 - 1 < x < x_0 + 1 $$
Cela implique que $|x| < |x_0| + 1$. (Si $x_0 \ge 0$, $x < x_0+1 \implies |x| < x_0+1$. Si $x_0 < 0$, $x_0-1 < x \implies |x| < |x_0-1| = |x_0|+1$).

Maintenant, nous pouvons borner le facteur $|x^2 + x x_0 + x_0^2|$ en utilisant l'inégalité triangulaire, $|A+B+C| \le |A|+|B|+|C|$ :
$$ |x^2 + x x_0 + x_0^2| \le |x^2| + |x x_0| + |x_0^2| $$
$$ |x^2 + x x_0 + x_0^2| \le |x|^2 + |x||x_0| + |x_0|^2 $$
En utilisant l'estimation $|x| < |x_0| + 1$ :
$$ |x|^2 < (|x_0| + 1)^2 = |x_0|^2 + 2|x_0| + 1 $$
$$ |x||x_0| < (|x_0| + 1)|x_0| = |x_0|^2 + |x_0| $$
En substituant ces bornes dans l'inégalité :
$$ |x^2 + x x_0 + x_0^2| < (|x_0|^2 + 2|x_0| + 1) + (|x_0|^2 + |x_0|) + |x_0|^2 $$
$$ |x^2 + x x_0 + x_0^2| < 3|x_0|^2 + 3|x_0| + 1 $$
Soit $M = 3|x_0|^2 + 3|x_0| + 1$. $M$ est une constante positive qui dépend de $x_0$.

Maintenant, nous avons :
$$ |f(x) - f(x_0)| = |x - x_0| |x^2 + x x_0 + x_0^2| < |x - x_0| M $$
Nous voulons que $|f(x) - f(x_0)| < \epsilon$. Donc, nous voulons que $|x - x_0| M < \epsilon$.
Cela implique que nous devons choisir $|x - x_0| < \frac{\epsilon}{M}$.

Nous avons deux conditions sur $\delta$:
1.  $\delta \le 1$ (pour que la borne $M$ soit valide).
2.  $\delta \le \frac{\epsilon}{M}$ (pour que $|f(x) - f(x_0)| < \epsilon$).

Nous choisissons donc $\delta = \min\left(1, \frac{\epsilon}{M}\right)$. Puisque $M = 3|x_0|^2 + 3|x_0| + 1$ est toujours positif (et même strictement positif), $\frac{\epsilon}{M}$ est bien défini et positif.

**Récapitulatif de la preuve :**
Soit $x_0 \in \mathbb{R}$ et $\epsilon > 0$.
Posons $M = 3|x_0|^2 + 3|x_0| + 1$.
Choisissons $\delta = \min\left(1, \frac{\epsilon}{M}\right)$.
Alors, si $|x - x_0| < \delta$, nous avons deux conséquences :
1.  $|x - x_0| < 1$, ce qui implique $x_0 - 1 < x < x_0 + 1$. Par conséquent, $|x| < |x_0| + 1$.
2.  $|x - x_0| < \frac{\epsilon}{M}$.

Maintenant, nous évaluons $|f(x) - f(x_0)|$:
$$ |f(x) - f(x_0)| = |x^3 - x_0^3| $$
$$ |f(x) - f(x_0)| = |(x - x_0)(x^2 + x x_0 + x_0^2)| \quad \text{(par factorisation de la différence de cubes)} $$
$$ |f(x) - f(x_0)| = |x - x_0| |x^2 + x x_0 + x_0^2| \quad \text{(par propriété du produit des valeurs absolues)} $$
En utilisant l'inégalité triangulaire pour le second facteur :
$$ |x^2 + x x_0 + x_0^2| \le |x^2| + |x x_0| + |x_0^2| \quad \text{(par inégalité triangulaire)} $$
$$ |x^2 + x x_0 + x_0^2| \le |x|^2 + |x||x_0| + |x_0|^2 $$
Puisque $|x| < |x_0| + 1$ (dû au choix $\delta \le 1$) :
$$ |x|^2 < (|x_0| + 1)^2 = |x_0|^2 + 2|x_0| + 1 $$
$$ |x||x_0| < (|x_0| + 1)|x_0| = |x_0|^2 + |x_0| $$
En substituant ces bornes :
$$ |x^2 + x x_0 + x_0^2| < (|x_0|^2 + 2|x_0| + 1) + (|x_0|^2 + |x_0|) + |x_0|^2 $$
$$ |x^2 + x x_0 + x_0^2| < 3|x_0|^2 + 3|x_0| + 1 $$
Par définition, $M = 3|x_0|^2 + 3|x_0| + 1$. Donc :
$$ |x^2 + x x_0 + x_0^2| < M $$
En combinant avec $|x - x_0| < \frac{\epsilon}{M}$ :
$$ |f(x) - f(x_0)| < \left(\frac{\epsilon}{M}\right) M $$
$$ |f(x) - f(x_0)| < \epsilon $$
Nous avons ainsi montré que pour tout $\epsilon > 0$, il existe un $\delta > 0$ (spécifiquement $\delta = \min(1, \frac{\epsilon}{3|x_0|^2 + 3|x_0| + 1})$) tel que si $|x - x_0| < \delta$, alors $|f(x) - f(x_0)| < \epsilon$.
Par conséquent, la fonction $f(x) = x^3$ est continue en tout point $x_0 \in \mathbb{R}$.

## Partie B : Continuité d'une fonction définie par morceaux

La fonction $g: \mathbb{R} \to \mathbb{R}$ est définie par :
$$ g(x) = \begin{cases} \frac{\sin(ax)}{x} & \text{si } x < 0 \\ b & \text{si } x = 0 \\ \frac{e^{2x}-1}{x} & \text{si } x > 0 \end{cases} $$
Pour que la fonction $g$ soit continue sur $\mathbb{R}$, elle doit être continue sur les intervalles ouverts $]-\infty, 0[$ et $]0, \infty[$, et elle doit être continue au point de raccordement $x=0$.

**1. Continuité sur les intervalles ouverts :**
*   **Pour $x < 0$ :** La fonction $x \mapsto \sin(ax)$ est une composition de fonctions continues ($x \mapsto ax$ et $u \mapsto \sin(u)$), donc elle est continue. La fonction $x \mapsto x$ est continue et non nulle sur $]-\infty, 0[$. Par conséquent, le quotient $\frac{\sin(ax)}{x}$ est continu sur $]-\infty, 0[$ en tant que quotient de fonctions continues dont le dénominateur ne s'annule pas.
*   **Pour $x > 0$ :** La fonction $x \mapsto e^{2x}-1$ est une composition de fonctions continues ($x \mapsto 2x$, $u \mapsto e^u$, et $v \mapsto v-1$), donc elle est continue. La fonction $x \mapsto x$ est continue et non nulle sur $]0, \infty[$. Par conséquent, le quotient $\frac{e^{2x}-1}{x}$ est continu sur $]0, \infty[$ en tant que quotient de fonctions continues dont le dénominateur ne s'annule pas.

**2. Continuité au point $x=0$ :**
Pour que $g$ soit continue en $x=0$, il faut que la valeur de la fonction en $x=0$ soit égale à la limite de la fonction lorsque $x$ tend vers $0$. C'est-à-dire :
$$ \lim_{x \to 0^-} g(x) = g(0) = \lim_{x \to 0^+} g(x) $$

*   **Calcul de $g(0)$ :**
    Par définition de la fonction $g$, $g(0) = b$.

*   **Calcul de la limite à gauche, $\lim_{x \to 0^-} g(x)$ :**
    Pour $x < 0$, $g(x) = \frac{\sin(ax)}{x}$.
    Nous devons calculer $\lim_{x \to 0^-} \frac{\sin(ax)}{x}$.
    Nous utilisons le résultat de limite remarquable $\lim_{u \to 0} \frac{\sin(u)}{u} = 1$.
    Si $a=0$, alors $\lim_{x \to 0^-} \frac{\sin(0)}{x} = \lim_{x \to 0^-} \frac{0}{x} = \lim_{x \to 0^-} 0 = 0$.
    Si $a \ne 0$, nous pouvons réécrire l'expression :
    $$ \lim_{x \to 0^-} \frac{\sin(ax)}{x} = \lim_{x \to 0^-} a \cdot \frac{\sin(ax)}{ax} $$
    Posons $u = ax$. Lorsque $x \to 0^-$, $u \to 0$ (car $a$ est une constante finie).
    $$ \lim_{x \to 0^-} a \cdot \frac{\sin(ax)}{ax} = a \cdot \lim_{u \to 0} \frac{\sin(u)}{u} = a \cdot 1 = a $$
    Donc, $\lim_{x \to 0^-} g(x) = a$.

*   **Calcul de la limite à droite, $\lim_{x \to 0^+} g(x)$ :**
    Pour $x > 0$, $g(x) = \frac{e^{2x}-1}{x}$.
    Nous devons calculer $\lim_{x \to 0^+} \frac{e^{2x}-1}{x}$.
    Nous utilisons le résultat de limite remarquable $\lim_{u \to 0} \frac{e^u-1}{u} = 1$.
    Nous pouvons réécrire l'expression :
    $$ \lim_{x \to 0^+} \frac{e^{2x}-1}{x} = \lim_{x \to 0^+} 2 \cdot \frac{e^{2x}-1}{2x} $$
    Posons $u = 2x$. Lorsque $x \to 0^+$, $u \to 0$.
    $$ \lim_{x \to 0^+} 2 \cdot \frac{e^{2x}-1}{2x} = 2 \cdot \lim_{u \to 0} \frac{e^u-1}{u} = 2 \cdot 1 = 2 $$
    Donc, $\lim_{x \to 0^+} g(x) = 2$.

**3. Détermination des constantes $a$ et $b$ :**
Pour que $g$ soit continue en $x=0$, nous devons avoir :
$$ \lim_{x \to 0^-} g(x) = g(0) = \lim_{x \to 0^+} g(x) $$
En substituant les valeurs calculées :
$$ a = b = 2 $$
Par conséquent, pour que la fonction $g$ soit continue sur $\mathbb{R}$, les constantes $a$ et $b$ doivent prendre les valeurs $a=2$ et $b=2$.

## Partie C : Application du Théorème des Valeurs Intermédiaires

Soit la fonction $h: \mathbb{R} \to \mathbb{R}$ définie par $h(x) = x^3 - 3x + 1$.

**Propriété de $h(x)$ :**
La fonction $h(x)$ est un polynôme. Les fonctions polynomiales sont continues sur tout $\mathbb{R}$. Cette propriété est essentielle pour appliquer le Théorème des Valeurs Intermédiaires (TVI).

**Théorème des Valeurs Intermédiaires (TVI) :**
Si une fonction $f$ est continue sur un intervalle fermé $[a, b]$, alors pour toute valeur $k$ comprise entre $f(a)$ et $f(b)$ (c'est-à-dire $f(a) \le k \le f(b)$ ou $f(b) \le k \le f(a)$), il existe au moins un $c \in [a, b]$ tel que $f(c) = k$.
Dans notre cas, nous cherchons des solutions à $h(x)=0$, donc $k=0$. Le TVI garantit l'existence d'une racine si $h(a)$ et $h(b)$ sont de signes opposés.

**1. Solution dans l'intervalle $]-2, -1[$ :**
*   La fonction $h(x) = x^3 - 3x + 1$ est continue sur l'intervalle fermé $[-2, -1]$ car c'est un polynôme.
*   Évaluons $h(x)$ aux bornes de l'intervalle :
    *   $h(-2) = (-2)^3 - 3(-2) + 1 = -8 + 6 + 1 = -1$.
    *   $h(-1) = (-1)^3 - 3(-1) + 1 = -1 + 3 + 1 = 3$.
*   Nous observons que $h(-2) = -1 < 0$ et $h(-1) = 3 > 0$.
*   Puisque $h(-2)$ et $h(-1)$ sont de signes opposés, et que $h$ est continue sur $[-2, -1]$, le Théorème des Valeurs Intermédiaires garantit qu'il existe au moins une valeur $c_1 \in ]-2, -1[$ telle que $h(c_1) = 0$.
    Ainsi, l'équation $h(x)=0$ possède au moins une solution dans $]-2, -1[$.

**2. Solution dans l'intervalle $]0, 1[$ :**
*   La fonction $h(x) = x^3 - 3x + 1$ est continue sur l'intervalle fermé $[0, 1]$ car c'est un polynôme.
*   Évaluons $h(x)$ aux bornes de l'intervalle :
    *   $h(0) = (0)^3 - 3(0) + 1 = 0 - 0 + 1 = 1$.
    *   $h(1) = (1)^3 - 3(1) + 1 = 1 - 3 + 1 = -1$.
*   Nous observons que $h(0) = 1 > 0$ et $h(1) = -1 < 0$.
*   Puisque $h(0)$ et $h(1)$ sont de signes opposés, et que $h$ est continue sur $[0, 1]$, le Théorème des Valeurs Intermédiaires garantit qu'il existe au moins une valeur $c_2 \in ]0, 1[$ telle que $h(c_2) = 0$.
    Ainsi, l'équation $h(x)=0$ possède au moins une solution dans $]0, 1[$.

**3. Solution dans l'intervalle $]1, 2[$ :**
*   La fonction $h(x) = x^3 - 3x + 1$ est continue sur l'intervalle fermé $[1, 2]$ car c'est un polynôme.
*   Évaluons $h(x)$ aux bornes de l'intervalle :
    *   $h(1) = (1)^3 - 3(1) + 1 = 1 - 3 + 1 = -1$.
    *   $h(2) = (2)^3 - 3(2) + 1 = 8 - 6 + 1 = 3$.
*   Nous observons que $h(1) = -1 < 0$ et $h(2) = 3 > 0$.
*   Puisque $h(1)$ et $h(2)$ sont de signes opposés, et que $h$ est continue sur $[1, 2]$, le Théorème des Valeurs Intermédiaires garantit qu'il existe au moins une valeur $c_3 \in ]1, 2[$ telle que $h(c_3) = 0$.
    Ainsi, l'équation $h(x)=0$ possède au moins une solution dans $]1, 2[$.

**4. Nombre exact de racines réelles :**
Nous avons montré l'existence de trois racines $c_1, c_2, c_3$ dans les intervalles $]-2, -1[$, $]0, 1[$, et $]1, 2[$ respectivement. Ces trois intervalles sont disjoints :
*   $]-2, -1[ \cap ]0, 1[ = \emptyset$
*   $]-2, -1[ \cap ]1, 2[ = \emptyset$
*   $]0, 1[ \cap ]1, 2[ = \emptyset$
Cela signifie que les trois racines $c_1, c_2, c_3$ sont distinctes.

La fonction $h(x) = x^3 - 3x + 1$ est un polynôme de degré 3. Un théorème fondamental de l'algèbre stipule qu'un polynôme de degré $n$ a au plus $n$ racines réelles (ou complexes, mais ici nous nous intéressons aux réelles).
Puisque nous avons trouvé trois racines réelles distinctes pour un polynôme de degré 3, il ne peut pas y en avoir davantage.
Par conséquent, l'équation $h(x) = 0$ possède exactement trois racines réelles.

Pour une justification plus rigoureuse de l'unicité dans chaque intervalle, nous pouvons étudier la dérivée de $h(x)$:
$h'(x) = \frac{d}{dx}(x^3 - 3x + 1) = 3x^2 - 3$.
Factorisons $h'(x)$: $h'(x) = 3(x^2 - 1) = 3(x-1)(x+1)$.
Les racines de $h'(x)$ sont $x=-1$ et $x=1$. Ce sont les points critiques de $h(x)$.
*   Pour $x < -1$, $x-1 < 0$ et $x+1 < 0$, donc $h'(x) = 3(\text{négatif})(\text{négatif}) > 0$. $h$ est strictement croissante sur $]-\infty, -1]$.
*   Pour $-1 < x < 1$, $x-1 < 0$ et $x+1 > 0$, donc $h'(x) = 3(\text{négatif})(\text{positif}) < 0$. $h$ est strictement décroissante sur $[-1, 1]$.
*   Pour $x > 1$, $x-1 > 0$ et $x+1 > 0$, donc $h'(x) = 3(\text{positif})(\text{positif}) > 0$. $h$ est strictement croissante sur $[1, \infty[$.

Calculons les valeurs de $h$ aux points critiques :
$h(-1) = (-1)^3 - 3(-1) + 1 = -1 + 3 + 1 = 3$ (maximum local).
$h(1) = (1)^3 - 3(1) + 1 = 1 - 3 + 1 = -1$ (minimum local).

*   Sur $]-\infty, -1]$ : $h$ est strictement croissante. Puisque $h(-2) = -1$ et $h(-1) = 3$, et que $0 \in [-1, 3]$, il existe une unique racine dans $]-2, -1[$ par le corollaire du TVI (Théorème de la bijection).
*   Sur $[-1, 1]$ : $h$ est strictement décroissante. Puisque $h(-1) = 3$ et $h(1) = -1$, et que $0 \in [-1, 3]$, il existe une unique racine dans $]-1, 1[$. Cette racine est $c_2 \in ]0, 1[$ car $h(0)=1$ et $h(1)=-1$.
*   Sur $[1, \infty[$ : $h$ est strictement croissante. Puisque $h(1) = -1$ et $\lim_{x \to \infty} h(x) = \lim_{x \to \infty} x^3(1 - 3/x^2 + 1/x^3) = \infty$, et que $0 \in [-1, \infty[$, il existe une unique racine dans $]1, \infty[$. Cette racine est $c_3 \in ]1, 2[$ car $h(1)=-1$ et $h(2)=3$.

Cette analyse confirme l'existence et l'unicité de trois racines réelles distinctes.

## Partie D : Point fixe d'une fonction continue

Soit $I = [a, b]$ un intervalle fermé et borné de $\mathbb{R}$, avec $a < b$. Soit $f: I \to I$ une fonction continue.
Nous voulons démontrer qu'il existe au moins un point $c \in I$ tel que $f(c) = c$.

**Stratégie :**
Nous allons définir une nouvelle fonction auxiliaire $k(x)$ et appliquer le Théorème des Valeurs Intermédiaires à cette fonction.

**1. Définition de la fonction auxiliaire :**
Considérons la fonction $k: I \to \mathbb{R}$ définie par $k(x) = f(x) - x$.
Un point $c$ est un point fixe de $f$ si $f(c) = c$, ce qui est équivalent à $f(c) - c = 0$, c'est-à-dire $k(c) = 0$.
Notre objectif est donc de montrer qu'il existe au moins un $c \in I$ tel que $k(c) = 0$.

**2. Continuité de $k(x)$ :**
*   La fonction $f$ est continue sur l'intervalle $I$ par hypothèse.
*   La fonction $x \mapsto x$ (la fonction identité) est continue sur tout $\mathbb{R}$, et donc sur l'intervalle $I$.
*   La fonction $k(x)$ est la différence de deux fonctions continues sur $I$. Par les propriétés des fonctions continues, la différence de deux fonctions continues est continue.
*   Par conséquent, $k(x)$ est continue sur l'intervalle fermé et borné $I = [a, b]$.

**3. Évaluation de $k(x)$ aux bornes de l'intervalle :**
*   **Pour $x=a$ :**
    $k(a) = f(a) - a$.
    Puisque la fonction $f$ a pour codomaine $I = [a, b]$ (c'est-à-dire $f: I \to I$), cela signifie que pour tout $x \in I$, $f(x) \in [a, b]$.
    En particulier, $f(a) \in [a, b]$. Cela implique $f(a) \ge a$.
    Donc, $f(a) - a \ge 0$.
    Ainsi, $k(a) \ge 0$.

*   **Pour $x=b$ :**
    $k(b) = f(b) - b$.
    De même, puisque $f(b) \in [a, b]$, cela implique $f(b) \le b$.
    Donc, $f(b) - b \le 0$.
    Ainsi, $k(b) \le 0$.

**4. Application du Théorème des Valeurs Intermédiaires :**
Nous avons les conditions suivantes pour la fonction $k(x)$ sur l'intervalle $[a, b]$ :
*   $k(x)$ est continue sur $[a, b]$.
*   $k(a) \ge 0$.
*   $k(b) \le 0$.

Nous considérons trois cas possibles :
*   **Cas 1 : $k(a) = 0$.**
    Si $k(a) = 0$, alors $f(a) - a = 0$, ce qui signifie $f(a) = a$. Dans ce cas, $a$ est un point fixe de $f$.
*   **Cas 2 : $k(b) = 0$.**
    Si $k(b) = 0$, alors $f(b) - b = 0$, ce qui signifie $f(b) = b$. Dans ce cas, $b$ est un point fixe de $f$.
*   **Cas 3 : $k(a) > 0$ et $k(b) < 0$.**
    Dans ce cas, nous avons $k(a) > 0$ et $k(b) < 0$. Puisque $k(x)$ est continue sur l'intervalle fermé $[a, b]$, et que $0$ est une valeur comprise entre $k(b)$ et $k(a)$ (car $k(b) < 0 < k(a)$), le Théorème des Valeurs Intermédiaires garantit qu'il existe au moins un point $c \in ]a, b[$ tel que $k(c) = 0$.
    Si $k(c) = 0$, alors $f(c) - c = 0$, ce qui signifie $f(c) = c$. Dans ce cas, $c$ est un point fixe de $f$.

Dans tous les cas (que $k(a)=0$, $k(b)=0$, ou $k(a)>0$ et $k(b)<0$), nous avons démontré l'existence d'au moins un point $c \in I = [a, b]$ tel que $f(c) = c$.
Ceci conclut la démonstration.
