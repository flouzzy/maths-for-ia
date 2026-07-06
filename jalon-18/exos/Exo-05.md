# Exercice 5 : Prolongement par continuité d'une fonction

$\star\star\star$

**Énoncé :**

Soit la fonction $f$ définie par $f(x) = \frac{\sqrt{1+x}-1}{x}$.

1.  Déterminer le domaine de définition de la fonction $f$.
2.  La fonction $f$ est-elle prolongeable par continuité au point $x=0$? Si oui, définir la fonction $g$ qui prolonge $f$ par continuité et préciser son domaine de définition.
3.  Démontrer que la fonction $g$ est continue sur son domaine de définition.

---

**Corrigé :**

**1. Détermination du domaine de définition de la fonction $f$.**

La fonction $f(x) = \frac{\sqrt{1+x}-1}{x}$ est définie si et seulement si deux conditions sont remplies :
*   Le terme sous la racine carrée doit être positif ou nul : $1+x \ge 0$, ce qui implique $x \ge -1$.
*   Le dénominateur ne doit pas être nul : $x \neq 0$.

En combinant ces deux conditions, le domaine de définition de $f$, noté $D_f$, est l'ensemble des réels $x$ tels que $x \ge -1$ et $x \neq 0$.
Ainsi, $D_f = [-1, 0) \cup (0, +\infty)$.

**2. Prolongement par continuité au point $x=0$.**

Pour que la fonction $f$ soit prolongeable par continuité au point $x=0$, il est nécessaire et suffisant que la limite de $f(x)$ lorsque $x$ tend vers $0$ existe et soit finie.

Calculons cette limite :
$$ \lim_{x \to 0} f(x) = \lim_{x \to 0} \frac{\sqrt{1+x}-1}{x} $$
Lorsque $x \to 0$, le numérateur $\sqrt{1+x}-1 \to \sqrt{1+0}-1 = \sqrt{1}-1 = 0$.
Le dénominateur $x \to 0$.
Nous sommes donc en présence d'une forme indéterminée du type $\frac{0}{0}$.

Pour lever cette indétermination, nous allons multiplier le numérateur et le dénominateur par l'expression conjuguée du numérateur, qui est $\sqrt{1+x}+1$.
$$ \lim_{x \to 0} \frac{(\sqrt{1+x}-1)(\sqrt{1+x}+1)}{x(\sqrt{1+x}+1)} $$
En utilisant l'identité remarquable $(a-b)(a+b) = a^2-b^2$ pour le numérateur :
$$ \lim_{x \to 0} \frac{(\sqrt{1+x})^2 - 1^2}{x(\sqrt{1+x}+1)} $$
$$ \lim_{x \to 0} \frac{(1+x) - 1}{x(\sqrt{1+x}+1)} $$
$$ \lim_{x \to 0} \frac{x}{x(\sqrt{1+x}+1)} $$
Pour $x \neq 0$, nous pouvons simplifier par $x$ :
$$ \lim_{x \to 0} \frac{1}{\sqrt{1+x}+1} $$
Maintenant, nous pouvons substituer $x=0$ sans problème :
$$ \frac{1}{\sqrt{1+0}+1} = \frac{1}{\sqrt{1}+1} = \frac{1}{1+1} = \frac{1}{2} $$
Puisque la limite $\lim_{x \to 0} f(x)$ existe et est finie (elle est égale à $\frac{1}{2}$), la fonction $f$ est prolongeable par continuité au point $x=0$.

La fonction $g$ qui prolonge $f$ par continuité est définie comme suit :
$$ g(x) = \begin{cases} \frac{\sqrt{1+x}-1}{x} & \text{si } x \in [-1, 0) \cup (0, +\infty) \\ \frac{1}{2} & \text{si } x = 0 \end{cases} $$
Le domaine de définition de la fonction $g$, noté $D_g$, est l'ensemble $D_f \cup \{0\}$, ce qui correspond à l'intervalle $[-1, +\infty)$.

**3. Démonstration de la continuité de la fonction $g$ sur son domaine de définition.**

Le domaine de définition de $g$ est $D_g = [-1, +\infty)$. Nous devons vérifier la continuité de $g$ sur cet intervalle. Cela implique de considérer trois types de points :
*   Les points de l'intervalle ouvert $(-1, +\infty)$ distincts de $0$.
*   Le point $x=0$.
*   Le point $x=-1$ (continuité à droite).

**a) Continuité sur $(-1, 0) \cup (0, +\infty)$ :**
Pour tout $x \in (-1, 0) \cup (0, +\infty)$, la fonction $g(x)$ est définie par $g(x) = \frac{\sqrt{1+x}-1}{x}$.
Considérons les fonctions suivantes :
*   La fonction $u(x) = 1+x$ est une fonction polynomiale, donc elle est continue sur $\mathbb{R}$.
*   La fonction $v(u) = \sqrt{u}$ est continue sur $[0, +\infty)$.
Par composition, la fonction $x \mapsto \sqrt{1+x}$ est continue sur l'intervalle où $1+x \ge 0$, c'est-à-dire sur $[-1, +\infty)$.
*   La fonction $h(x) = \sqrt{1+x}-1$ est la somme d'une fonction continue ($\sqrt{1+x}$) et d'une constante ($-1$), elle est donc continue sur $[-1, +\infty)$.
*   La fonction $k(x) = x$ est une fonction polynomiale, donc elle est continue sur $\mathbb{R}$.

La fonction $g(x)$ (pour $x \neq 0$) est le quotient de deux fonctions continues, $h(x)$ et $k(x)$. Un quotient de fonctions continues est continu partout où le dénominateur n'est pas nul.
Puisque $k(x) = x \neq 0$ pour $x \in (-1, 0) \cup (0, +\infty)$, la fonction $g$ est continue sur cet ensemble.

**b) Continuité au point $x=0$ :**
Pour que $g$ soit continue en $x=0$, il faut que $\lim_{x \to 0} g(x) = g(0)$.
D'après la question 2, nous avons calculé $\lim_{x \to 0} g(x) = \lim_{x \to 0} \frac{\sqrt{1+x}-1}{x} = \frac{1}{2}$.
Par définition de la fonction $g$, nous avons $g(0) = \frac{1}{2}$.
Puisque $\lim_{x \to 0} g(x) = g(0)$, la fonction $g$ est continue au point $x=0$.

**c) Continuité au point $x=-1$ (continuité à droite) :**
Pour que $g$ soit continue à droite en $x=-1$, il faut que $\lim_{x \to -1^+} g(x) = g(-1)$.
Pour $x > -1$, $g(x) = \frac{\sqrt{1+x}-1}{x}$.
Calculons la limite à droite :
$$ \lim_{x \to -1^+} g(x) = \lim_{x \to -1^+} \frac{\sqrt{1+x}-1}{x} $$
Lorsque $x \to -1^+$, le numérateur $\sqrt{1+x}-1 \to \sqrt{1+(-1)}-1 = \sqrt{0}-1 = -1$.
Lorsque $x \to -1^+$, le dénominateur $x \to -1$.
Donc, la limite est $\frac{-1}{-1} = 1$.

Maintenant, calculons $g(-1)$ en utilisant la définition de $g(x)$ pour $x \neq 0$ :
$$ g(-1) = \frac{\sqrt{1+(-1)}-1}{-1} = \frac{\sqrt{0}-1}{-1} = \frac{-1}{-1} = 1 $$
Puisque $\lim_{x \to -1^+} g(x) = g(-1)$, la fonction $g$ est continue à droite au point $x=-1$.

En résumé, la fonction $g$ est continue sur $(-1, 0) \cup (0, +\infty)$, elle est continue en $x=0$, et elle est continue à droite en $x=-1$. Par conséquent, la fonction $g$ est continue sur tout son domaine de définition $D_g = [-1, +\infty)$.