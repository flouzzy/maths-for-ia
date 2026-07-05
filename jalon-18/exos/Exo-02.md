# Exercice 2 : Vérification de la continuité d'une fonction affine en un point

**Jalon 18 : Continuité des fonctions d'une variable réelle**
**Difficulté :** $\star \rule{0.5cm}{0.05cm} \rule{0.5cm}{0.05cm} \rule{0.5cm}{0.05cm} \rule{0.5cm}{0.05cm}$ (1 étoile sur 5)

---

### Énoncé

Soit une fonction $f: \mathbb{R} \to \mathbb{R}$ définie par $f(x) = 3x - 2$.

En utilisant la définition formelle de la continuité en un point (la définition $\varepsilon-\delta$), démontrez que la fonction $f$ est continue au point $a = 1$.

---

### Corrigé

Pour démontrer qu'une fonction $f$ est continue en un point $a$ de son domaine de définition, nous devons vérifier que les trois conditions suivantes sont satisfaites :
1.  Le point $a$ appartient au domaine de définition de $f$, et la valeur $f(a)$ est bien définie.
2.  La limite de $f(x)$ lorsque $x$ tend vers $a$ existe, c'est-à-dire $\lim_{x \to a} f(x)$ existe.
3.  La limite est égale à la valeur de la fonction au point $a$, c'est-à-dire $\lim_{x \to a} f(x) = f(a)$.

Nous allons appliquer ces conditions à la fonction $f(x) = 3x - 2$ au point $a = 1$.

#### Étape 1 : Vérification de l'existence de $f(a)$

Le domaine de définition de la fonction $f(x) = 3x - 2$ est l'ensemble de tous les nombres réels, $\mathbb{R}$, car il s'agit d'un polynôme de degré 1. Le point $a = 1$ appartient bien à $\mathbb{R}$.
Calculons la valeur de la fonction en $a = 1$:
$$f(1) = 3(1) - 2 = 3 - 2 = 1$$
Ainsi, la valeur $f(1) = 1$ est bien définie.

#### Étape 2 : Vérification de l'existence de la limite $\lim_{x \to a} f(x)$ et de sa valeur

Nous devons montrer que $\lim_{x \to 1} (3x - 2)$ existe et déterminer sa valeur. Pour cela, nous utilisons la définition formelle de la limite, également connue sous le nom de définition $\varepsilon-\delta$.
La définition de $\lim_{x \to a} f(x) = L$ est la suivante :
Pour tout nombre réel $\varepsilon > 0$, il existe un nombre réel $\delta > 0$ tel que si $x$ est un nombre réel vérifiant $0 < |x - a| < \delta$, alors $|f(x) - L| < \varepsilon$.

Dans notre cas, $a = 1$ et $f(x) = 3x - 2$. D'après l'Étape 1, nous avons calculé $f(1) = 1$. Pour que la fonction soit continue en $a=1$, la limite doit être égale à $f(1)$. Nous allons donc *conjecturer* que la limite $L$ est égale à $1$. Nous devons ainsi montrer que pour tout $\varepsilon > 0$, il existe un $\delta > 0$ tel que si $0 < |x - 1| < \delta$, alors $|(3x - 2) - 1| < \varepsilon$.

Commençons par manipuler l'expression $|f(x) - L|$, c'est-à-dire $|f(x) - 1|$ :
$$|f(x) - 1| = |(3x - 2) - 1|$$
$$|f(x) - 1| = |3x - 3|$$
Nous pouvons factoriser le terme $3$ à l'intérieur de la valeur absolue :
$$|f(x) - 1| = |3(x - 1)|$$
En utilisant la propriété de la valeur absolue qui stipule que $|ab| = |a||b|$ pour tous nombres réels $a$ et $b$, nous obtenons :
$$|f(x) - 1| = |3| |x - 1|$$
Puisque $|3| = 3$, l'expression devient :
$$|f(x) - 1| = 3|x - 1|$$

Notre objectif est de rendre l'expression $3|x - 1|$ plus petite que $\varepsilon$.
Nous voulons que $3|x - 1| < \varepsilon$.
Pour que cette inégalité soit satisfaite, il suffit que $|x - 1| < \frac{\varepsilon}{3}$.

Nous pouvons donc choisir $\delta = \frac{\varepsilon}{3}$. Puisque $\varepsilon$ est un nombre strictement positif, il est clair que $\delta$ sera également un nombre strictement positif ($\delta > 0$).

Maintenant, rédigeons la démonstration formelle de la limite :
Soit $\varepsilon$ un nombre réel strictement positif ($\varepsilon > 0$).
Choisissons $\delta = \frac{\varepsilon}{3}$. Par construction, $\delta > 0$.
Supposons que $x$ est un nombre réel tel que $0 < |x - 1| < \delta$.
Puisque $|x - 1| < \delta$, nous avons $|x - 1| < \frac{\varepsilon}{3}$.
Multiplions les deux côtés de cette inégalité par $3$ (qui est un nombre positif, donc l'inégalité ne change pas de sens) :
$$3|x - 1| < 3 \left(\frac{\varepsilon}{3}\right)$$
$$3|x - 1| < \varepsilon$$
Nous avons précédemment établi que $3|x - 1| = |3(x - 1)| = |3x - 3| = |(3x - 2) - 1| = |f(x) - 1|$.
Par conséquent, nous avons démontré que $|f(x) - 1| < \varepsilon$.

Ceci prouve, par la définition $\varepsilon-\delta$, que la limite de $f(x)$ lorsque $x$ tend vers $1$ est égale à $1$. Autrement dit, $\lim_{x \to 1} f(x) = 1$.

#### Étape 3 : Comparaison de la limite et de la valeur de la fonction

Nous avons trouvé dans l'Étape 1 que la valeur de la fonction au point $a=1$ est $f(1) = 1$.
Nous avons trouvé dans l'Étape 2 que la limite de la fonction lorsque $x$ tend vers $1$ est $\lim_{x \to 1} f(x) = 1$.
Puisque $\lim_{x \to 1} f(x) = 1$ et $f(1) = 1$, nous avons bien l'égalité $\lim_{x \to 1} f(x) = f(1)$.

#### Conclusion

Toutes les conditions de la définition de la continuité en un point sont satisfaites pour la fonction $f(x) = 3x - 2$ au point $a = 1$.
Par conséquent, la fonction $f(x) = 3x - 2$ est continue au point $a = 1$.