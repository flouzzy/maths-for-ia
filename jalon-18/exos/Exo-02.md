# Exercice 2 - Exploration de la Continuité des Fonctions Réelles

Ce jalon explore la notion fondamentale de continuité pour les fonctions d'une variable réelle. Nous allons aborder la définition formelle, l'analyse de fonctions définies par morceaux et l'application de théorèmes clés.

---

## Énoncé de l'Exercice

**Partie A : Continuité par la définition $\epsilon-\delta$**

Soit la fonction $f: \mathbb{R} \to \mathbb{R}$ définie par $f(x) = x^2 + 3x$.
En utilisant la définition formelle de la continuité ($\epsilon-\delta$), démontrez que $f$ est continue au point $x_0 = 1$.

**Partie B : Continuité d'une fonction définie par morceaux**

Considérons la fonction $g: \mathbb{R} \to \mathbb{R}$ définie par :
$$ g(x) = \begin{cases} \frac{x^2 - 4}{x - 2} & \text{si } x \neq 2 \\ k & \text{si } x = 2 \end{cases} $$
Déterminez la valeur de la constante $k$ pour laquelle la fonction $g$ est continue au point $x = 2$.

**Partie C : Continuité sur un intervalle et Théorème des Valeurs Intermédiaires**

Soit la fonction $h: D \to \mathbb{R}$ définie par $h(x) = \sqrt{x+1}$.

1.  Déterminez le domaine de définition $D$ de la fonction $h$.
2.  Démontrez que la fonction $h$ est continue sur son domaine $D$.
3.  En utilisant le Théorème des Valeurs Intermédiaires (TVI), montrez qu'il existe au moins une valeur $c \in [0, 3]$ telle que $h(c) = 2$.

---

## Correction Détaillée

### Partie A : Continuité par la définition $\epsilon-\delta$

Nous devons démontrer que la fonction $f(x) = x^2 + 3x$ est continue au point $x_0 = 1$ en utilisant la définition $\epsilon-\delta$.
La fonction $f$ est continue en $x_0 = 1$ si et seulement si pour tout $\epsilon > 0$, il existe un $\delta > 0$ tel que pour tout $x \in \mathbb{R}$, si $|x - 1| < \delta$, alors $|f(x) - f(1)| < \epsilon$.

**Étape 1 : Calcul de $f(x_0)$**
Nous calculons la valeur de la fonction au point $x_0 = 1$:
$$ f(1) = (1)^2 + 3(1) = 1 + 3 = 4 $$

**Étape 2 : Analyse de l'expression $|f(x) - f(1)|$**
Nous considérons la différence $|f(x) - f(1)|$:
$$ |f(x) - f(1)| = |(x^2 + 3x) - 4| $$
Nous factorisons le polynôme $x^2 + 3x - 4$. Nous cherchons deux nombres dont la somme est $3$ et le produit est $-4$. Ces nombres sont $4$ et $-1$.
Ainsi, $x^2 + 3x - 4 = (x-1)(x+4)$.
L'expression devient :
$$ |f(x) - f(1)| = |(x-1)(x+4)| = |x-1||x+4| $$

**Étape 3 : Borner le terme $|x+4|$**
Nous voulons que $|f(x) - f(1)| < \epsilon$. Nous avons le terme $|x-1|$ que nous pouvons contrôler directement avec $\delta$. Le terme $|x+4|$ doit être borné.
Choisissons une première valeur pour $\delta$, par exemple $\delta_1 = 1$.
Si $|x-1| < \delta_1 = 1$, cela signifie que $-1 < x-1 < 1$.
En ajoutant $1$ à toutes les parties de l'inégalité, nous obtenons :
$$ 0 < x < 2 $$
Maintenant, nous voulons borner $|x+4|$. Si $0 < x < 2$, alors en ajoutant $4$ à toutes les parties de l'inégalité :
$$ 0+4 < x+4 < 2+4 $$
$$ 4 < x+4 < 6 $$
Puisque $x+4$ est positif dans cet intervalle, $|x+4| = x+4$.
Donc, nous avons $|x+4| < 6$.

**Étape 4 : Détermination de $\delta$ en fonction de $\epsilon$**
En utilisant la borne trouvée pour $|x+4|$, nous avons :
$$ |f(x) - f(1)| = |x-1||x+4| < |x-1| \cdot 6 $$
Nous voulons que cette expression soit inférieure à $\epsilon$:
$$ 6|x-1| < \epsilon $$
Ceci implique :
$$ |x-1| < \frac{\epsilon}{6} $$
Pour que les deux conditions $|x-1| < 1$ (pour borner $|x+4|$) et $|x-1| < \frac{\epsilon}{6}$ soient satisfaites simultanément, nous devons choisir $\delta$ comme le minimum de ces deux valeurs.
Soit $\delta = \min\left(1, \frac{\epsilon}{6}\right)$.

**Étape 5 : Conclusion de la démonstration**
Pour tout $\epsilon > 0$, nous avons trouvé un $\delta = \min\left(1, \frac{\epsilon}{6}\right) > 0$.
Si $|x-1| < \delta$, alors :
1.  $|x-1| < 1$, ce qui implique $0 < x < 2$, et donc $4 < x+4 < 6$, d'où $|x+4| < 6$.
2.  $|x-1| < \frac{\epsilon}{6}$.
En combinant ces deux inégalités, nous obtenons :
$$ |f(x) - f(1)| = |x-1||x+4| < \left(\frac{\epsilon}{6}\right) \cdot 6 = \epsilon $$
Par conséquent, la fonction $f(x) = x^2 + 3x$ est continue au point $x_0 = 1$ selon la définition $\epsilon-\delta$.

### Partie B : Continuité d'une fonction définie par morceaux

Pour que la fonction $g(x)$ soit continue au point $x = 2$, il faut que la limite de $g(x)$ lorsque $x$ tend vers $2$ soit égale à la valeur de la fonction en $x = 2$. C'est-à-dire :
$$ \lim_{x \to 2} g(x) = g(2) $$

**Étape 1 : Calcul de $g(2)$**
Par la définition de la fonction $g(x)$, lorsque $x = 2$, la valeur de la fonction est $k$.
$$ g(2) = k $$

**Étape 2 : Calcul de $\lim_{x \to 2} g(x)$**
Pour $x \neq 2$, la fonction $g(x)$ est définie par $g(x) = \frac{x^2 - 4}{x - 2}$.
Nous calculons la limite de cette expression lorsque $x$ tend vers $2$:
$$ \lim_{x \to 2} g(x) = \lim_{x \to 2} \frac{x^2 - 4}{x - 2} $$
Le numérateur $x^2 - 4$ est une différence de carrés, qui peut être factorisée comme $(x-2)(x+2)$.
$$ \lim_{x \to 2} \frac{(x-2)(x+2)}{x - 2} $$
Puisque $x \to 2$ signifie que $x$ s'approche de $2$ mais n'est pas égal à $2$, le terme $(x-2)$ est non nul. Nous pouvons donc simplifier l'expression en divisant le numérateur et le dénominateur par $(x-2)$:
$$ \lim_{x \to 2} (x+2) $$
Cette limite est celle d'un polynôme. Par les propriétés des limites (la limite d'une somme est la somme des limites, la limite d'une constante est la constante, la limite de $x$ est $x_0$), nous pouvons substituer $x=2$:
$$ \lim_{x \to 2} (x+2) = 2 + 2 = 4 $$

**Étape 3 : Détermination de $k$ pour la continuité**
Pour que $g(x)$ soit continue en $x=2$, nous devons avoir $\lim_{x \to 2} g(x) = g(2)$.
En substituant les valeurs calculées :
$$ 4 = k $$
Par conséquent, la fonction $g(x)$ est continue au point $x=2$ si et seulement si $k=4$.

### Partie C : Continuité sur un intervalle et Théorème des Valeurs Intermédiaires

Soit la fonction $h(x) = \sqrt{x+1}$.

**1. Détermination du domaine de définition $D$ de la fonction $h$**

Pour que la fonction $h(x) = \sqrt{x+1}$ soit définie dans l'ensemble des nombres réels, l'expression sous le radical (le radicande) doit être supérieure ou égale à zéro.
$$ x+1 \ge 0 $$
En soustrayant $1$ des deux côtés de l'inégalité, nous obtenons :
$$ x \ge -1 $$
Le domaine de définition $D$ de la fonction $h$ est l'ensemble de tous les nombres réels $x$ tels que $x \ge -1$.
$$ D = [-1, \infty) $$

**2. Démonstration de la continuité de $h$ sur son domaine $D$**

Nous allons utiliser les propriétés de continuité des fonctions élémentaires et des compositions de fonctions.
Considérons deux fonctions :
*   $f_1(x) = x+1$. Cette fonction est un polynôme de degré 1. Les fonctions polynomiales sont continues sur tout $\mathbb{R}$. Par conséquent, $f_1(x)$ est continue sur $[-1, \infty)$.
*   $f_2(y) = \sqrt{y}$. Cette fonction est la fonction racine carrée. La fonction racine carrée est continue sur son domaine de définition, qui est $[0, \infty)$.

La fonction $h(x)$ est la composition de $f_2$ et $f_1$, c'est-à-dire $h(x) = f_2(f_1(x))$.
Pour qu'une composition de fonctions $f_2 \circ f_1$ soit continue, il faut que :
a.  $f_1$ soit continue au point $x$.
b.  $f_2$ soit continue au point $f_1(x)$.

Pour tout $x \in D = [-1, \infty)$, nous avons $x+1 \ge 0$.
Donc, pour tout $x \in D$, la valeur $f_1(x) = x+1$ appartient au domaine de définition de $f_2$, qui est $[0, \infty)$.
Puisque $f_1(x)$ est continue sur $[-1, \infty)$ et $f_2(y)$ est continue sur $[0, \infty)$, la composition $h(x) = f_2(f_1(x)) = \sqrt{x+1}$ est continue sur son domaine $D = [-1, \infty)$.

**3. Application du Théorème des Valeurs Intermédiaires (TVI)**

Nous voulons montrer qu'il existe au moins une valeur $c \in [0, 3]$ telle que $h(c) = 2$.
Pour appliquer le Théorème des Valeurs Intermédiaires, nous devons vérifier trois conditions :

**Condition 1 : La fonction doit être continue sur l'intervalle fermé $[a, b]$.**
L'intervalle donné est $[0, 3]$.
D'après la partie C.2, la fonction $h(x) = \sqrt{x+1}$ est continue sur son domaine $D = [-1, \infty)$.
Puisque l'intervalle $[0, 3]$ est un sous-ensemble de $[-1, \infty)$, la fonction $h(x)$ est continue sur l'intervalle fermé $[0, 3]$.

**Condition 2 : Calculer les valeurs de la fonction aux bornes de l'intervalle.**
Nous calculons $h(0)$ et $h(3)$:
$$ h(0) = \sqrt{0+1} = \sqrt{1} = 1 $$
$$ h(3) = \sqrt{3+1} = \sqrt{4} = 2 $$

**Condition 3 : Vérifier que la valeur cible $y_0$ est comprise entre $h(a)$ et $h(b)$.**
La valeur cible est $y_0 = 2$.
Les valeurs aux bornes sont $h(0) = 1$ et $h(3) = 2$.
Nous observons que $1 \le 2 \le 2$.
La valeur $y_0 = 2$ est bien comprise dans l'intervalle $[h(0), h(3)] = [1, 2]$.

**Conclusion par le TVI :**
Puisque toutes les conditions du Théorème des Valeurs Intermédiaires sont satisfaites (la fonction $h$ est continue sur $[0, 3]$ et la valeur $2$ est entre $h(0)$ et $h(3)$), le TVI garantit qu'il existe au moins une valeur $c \in [0, 3]$ telle que $h(c) = 2$.
Dans ce cas précis, nous avons même trouvé que $h(3) = 2$, donc $c=3$ est une telle valeur.
